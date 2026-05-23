from __future__ import annotations

import argparse
import shutil
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_ROOT = REPO_ROOT / "templates" / "project"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Initialize a generic agent memory harness in a project.")
    parser.add_argument("--target", required=True, type=Path, help="Project directory to initialize.")
    parser.add_argument("--project-name", required=True, help="Name to place in generated templates.")
    parser.add_argument("--dry-run", action="store_true", help="Show planned writes without changing files.")
    parser.add_argument("--force", action="store_true", help="Overwrite existing generated files.")
    return parser.parse_args()


def render_text(value: str, project_name: str) -> str:
    return value.replace("{{PROJECT_NAME}}", project_name)


def copy_file(src: Path, dst: Path, project_name: str, force: bool, dry_run: bool) -> str:
    if dst.exists() and not force:
        return f"skip existing: {dst}"

    if dry_run:
        action = "overwrite" if dst.exists() else "write"
        return f"dry run: would {action}: {dst}"

    dst.parent.mkdir(parents=True, exist_ok=True)
    try:
        text = src.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        shutil.copy2(src, dst)
    else:
        dst.write_text(render_text(text, project_name), encoding="utf-8", newline="\n")
    return f"wrote: {dst}"


def main() -> None:
    args = parse_args()
    if not TEMPLATE_ROOT.exists():
        raise SystemExit(f"Missing template directory: {TEMPLATE_ROOT}")

    target = args.target.resolve()
    if args.dry_run:
        print(f"Dry run target: {target}")
    else:
        target.mkdir(parents=True, exist_ok=True)

    messages: list[str] = []
    for src in sorted(TEMPLATE_ROOT.rglob("*")):
        if src.is_dir():
            continue
        rel = src.relative_to(TEMPLATE_ROOT)
        dst = target / rel
        messages.append(copy_file(src, dst, args.project_name, args.force, args.dry_run))

    print("\n".join(messages))


if __name__ == "__main__":
    main()
