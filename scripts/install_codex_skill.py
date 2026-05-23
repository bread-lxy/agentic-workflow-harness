from __future__ import annotations

import argparse
import shutil
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_NAME = "agentic-workflow-harness"
SOURCE = REPO_ROOT / "skills" / SKILL_NAME
TARGET = Path.home() / ".codex" / "skills" / SKILL_NAME


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Install the agentic workflow harness Codex skill.")
    parser.add_argument("--dry-run", action="store_true", help="Show what would happen without copying files.")
    parser.add_argument("--force", action="store_true", help="Replace an existing installed skill.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if not SOURCE.exists():
        raise SystemExit(f"Missing source skill directory: {SOURCE}")

    print(f"Source: {SOURCE}")
    print(f"Target: {TARGET}")

    if args.dry_run:
        action = "replace with --force" if TARGET.exists() else "copy"
        print(f"Dry run: would {action} skill directory.")
        return

    if TARGET.exists() and not args.force:
        raise SystemExit("Target already exists. Use --force to replace it.")

    TARGET.parent.mkdir(parents=True, exist_ok=True)
    if TARGET.exists():
        shutil.rmtree(TARGET)
    shutil.copytree(SOURCE, TARGET)
    print("Installed.")


if __name__ == "__main__":
    main()
