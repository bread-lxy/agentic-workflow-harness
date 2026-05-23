# Migration Guide

Use this guide to apply the harness to an existing project.

## 1. Install The Skill

From this repository:

```powershell
python scripts/install_codex_skill.py
```

Use `--dry-run` first if you want to preview the target path.

## 2. Bootstrap The Project

```powershell
python scripts/bootstrap_project.py --target C:\path\to\project --project-name ProjectName
```

The script does not overwrite existing files unless `--force` is provided.

## 3. Merge With Existing Instructions

If your project already has `AGENTS.md`, merge the generated instructions manually:

- Add the default reading order.
- Add the durable state policy.
- Add privacy and boundary rules.
- Link to `knowledge/README.md`.

## 4. Add Project Routes

Edit `knowledge/README.md` to point to stable project knowledge areas.

Keep the routing compact. Add only areas that future sessions will actually need.

## 5. Start Using State Files

For the first long-running task:

1. Add a work item to `feature_list.json`.
2. Record the starting point in `progress.md`.
3. Record important choices in `decision_log.md`.
4. Update `handoff.md` before stopping.

## 6. Keep It Alive

Memory systems fail when nobody maintains them. Update state at milestones, not after every small action.
