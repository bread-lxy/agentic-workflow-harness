from __future__ import annotations

import json
import re
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
TEXT_SUFFIXES = {".md", ".py", ".json", ".txt", ".yml", ".yaml"}
SKIP_DIRS = {".git", "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache", ".venv", "venv"}

REQUIRED_FILES = [
    "README.md",
    "LICENSE",
    "AGENTS.md",
    "skills/agentic-workflow-harness/SKILL.md",
    "skills/agentic-workflow-harness/references/work-shapes.md",
    "skills/agentic-workflow-harness/references/durable-memory.md",
    "skills/agentic-workflow-harness/references/project-knowledge-routing.md",
    "skills/agentic-workflow-harness/references/multi-agent-collaboration.md",
    "skills/agentic-workflow-harness/references/validation-and-handoff.md",
    "templates/project/AGENTS.md",
    "templates/project/CLAUDE.md",
    "templates/project/knowledge/README.md",
    "templates/project/knowledge/agent-memory/AGENT_MEMORY.md",
    "templates/project/knowledge/agent-memory/WORKFLOW_PLAYBOOK.md",
    "templates/project/knowledge/agent-memory/task_state/feature_list.json",
    "templates/project/knowledge/agent-memory/task_state/progress.md",
    "templates/project/knowledge/agent-memory/task_state/decision_log.md",
    "templates/project/knowledge/agent-memory/task_state/handoff.md",
    "docs/operating-principles.md",
    "docs/memory-system-design.md",
    "docs/migration-guide.md",
    "scripts/install_codex_skill.py",
    "scripts/bootstrap_project.py",
    "scripts/check_package.py",
    "scripts/check_project_memory.py",
]


def iter_files() -> list[Path]:
    files: list[Path] = []
    for path in REPO_ROOT.rglob("*"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.is_file():
            files.append(path)
    return files


def require_files(errors: list[str]) -> None:
    for rel in REQUIRED_FILES:
        if not (REPO_ROOT / rel).is_file():
            errors.append(f"missing required file: {rel}")


def validate_json(errors: list[str]) -> None:
    for path in iter_files():
        if path.suffix != ".json":
            continue
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"invalid json: {path.relative_to(REPO_ROOT)}: {exc}")


def validate_skill_references(errors: list[str]) -> None:
    skill = REPO_ROOT / "skills" / "agentic-workflow-harness" / "SKILL.md"
    if not skill.exists():
        return
    text = skill.read_text(encoding="utf-8")
    refs = sorted(set(re.findall(r"`(references/[^`]+?\.md)`", text)))
    for ref in refs:
        if not (skill.parent / ref).is_file():
            errors.append(f"missing skill reference: {ref}")


def blocked_terms() -> list[str]:
    return [
        "".join(["V", "id", "M", "use"]),
        "".join(["F", "ei", "shu"]),
        "".join(["\u98de", "\u4e66"]),
        "".join(["E", "vals", "-bread"]),
        "".join(["s", "and", "-", "e", "val", "-", "s", "ample"]),
        "".join(["base", "_", "to", "ken"]),
        "".join(["e", "val"]),
        "".join(["\u8bc4", "\u6d4b"]),
        "".join(["\u6253", "\u5206"]),
        "".join(["\u6a21\u578b", "\u5bf9\u6bd4"]),
        "".join(["Be", "ar", "er"]),
        "".join(["Auth", "or", "ization"]),
        "".join(["co", "ok", "ie"]),
    ]


def scan_boundaries(errors: list[str]) -> None:
    terms = blocked_terms()
    for path in iter_files():
        if path.suffix not in TEXT_SUFFIXES:
            continue
        rel = path.relative_to(REPO_ROOT)
        text = path.read_text(encoding="utf-8", errors="ignore")
        lowered = text.lower()
        for term in terms:
            target = term if any(ord(ch) > 127 for ch in term) else term.lower()
            haystack = text if any(ord(ch) > 127 for ch in term) else lowered
            if target in haystack:
                errors.append(f"blocked term in {rel}: {term}")


def main() -> None:
    errors: list[str] = []
    require_files(errors)
    validate_json(errors)
    validate_skill_references(errors)
    scan_boundaries(errors)

    if errors:
        print("Package check failed:")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)

    print("Package check passed.")


if __name__ == "__main__":
    main()
