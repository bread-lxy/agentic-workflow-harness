from __future__ import annotations

import argparse
import json
import re
from datetime import datetime
from pathlib import Path

DATE_RE = re.compile(r"(?:updated_at|verified_at)\s*:\s*[\"']?(\d{4}-\d{2}-\d{2})")
ALLOWED_STATUSES = {"pending", "in_progress", "blocked", "done"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Warn about stale knowledge entries and malformed feature_list.json items in a bootstrapped project. Advisory only: never fails the build."
    )
    parser.add_argument("--target", required=True, type=Path, help="Project directory to check.")
    parser.add_argument("--stale-days", type=int, default=90, help="Age in days before a knowledge entry is flagged as possibly stale.")
    return parser.parse_args()


def find_knowledge_root(target: Path) -> Path | None:
    knowledge = target / "knowledge"
    return knowledge if knowledge.is_dir() else None


def warn_stale_entries(knowledge_root: Path, stale_days: int) -> list[str]:
    warnings: list[str] = []
    now = datetime.now()
    for path in sorted(knowledge_root.rglob("*.md")):
        if "task_state" in path.parts or "archive" in path.parts:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        match = DATE_RE.search(text)
        if not match:
            continue
        try:
            stamped = datetime.strptime(match.group(1), "%Y-%m-%d")
        except ValueError:
            continue
        age_days = (now - stamped).days
        if age_days > stale_days:
            rel = path.relative_to(knowledge_root.parent)
            warnings.append(f"possibly stale ({age_days}d old): {rel}")
    return warnings


def warn_feature_list_shape(knowledge_root: Path) -> list[str]:
    warnings: list[str] = []
    for path in sorted(knowledge_root.rglob("feature_list.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            warnings.append(f"invalid json: {path}: {exc}")
            continue
        rel = path.relative_to(knowledge_root.parent)
        for index, item in enumerate(data.get("items", [])):
            if "id" not in item:
                warnings.append(f"{rel}: item {index} is missing 'id'")
            status = item.get("status")
            if status is None:
                warnings.append(f"{rel}: item {index} is missing 'status'")
            elif status not in ALLOWED_STATUSES:
                warnings.append(f"{rel}: item {index} has non-standard status '{status}' (expected one of {sorted(ALLOWED_STATUSES)})")
    return warnings


def main() -> None:
    args = parse_args()
    target = args.target.resolve()
    knowledge_root = find_knowledge_root(target)

    if knowledge_root is None:
        print(f"No knowledge/ directory found under {target}. Nothing to check.")
        return

    warnings = warn_stale_entries(knowledge_root, args.stale_days) + warn_feature_list_shape(knowledge_root)

    if not warnings:
        print("Project memory check: no issues found.")
        return

    print("Project memory check found advisory warnings (not blocking):")
    for warning in warnings:
        print(f"- {warning}")


if __name__ == "__main__":
    main()
