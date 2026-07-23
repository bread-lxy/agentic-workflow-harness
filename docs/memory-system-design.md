# Memory System Design

The memory system has three layers: entry, routing, and state.

## Entry Layer

`AGENTS.md` is the first instruction surface. It should stay short and stable.

It answers:

- What should the agent read first?
- Which files define durable memory?
- What boundaries must not be crossed?
- How should long-running work be recorded?

## Routing Layer

`knowledge/README.md` decides which memory files matter for the current task.

Good routing keeps context clean. It helps the agent avoid reading old history, bulky artifacts, or unrelated notes by default.

## State Layer

`task_state/` stores active or resumable work.

- `feature_list.json` is structured and machine-readable.
- `progress.md` is human-readable.
- `decision_log.md` explains why the project took a path.
- `handoff.md` is the resume entry.

## What Belongs In Memory

- Stable project rules.
- Current goals.
- Decisions and reasons.
- Source locators.
- Validation results.
- Handoff notes.

## What Does Not Belong In Memory

- Credentials or private access material.
- Large raw copies when a locator and summary are enough.
- Generated artifacts that can be recreated.
- Unchecked assumptions.
- Personal local paths.

## Archival Layer

Memory that only grows stops being compact. Long-running projects need an eviction path, not just an entry path.

- When `progress.md`'s Completed section grows past a quick read, move the older entries as a block into `task_state/archive/progress-YYYY-MM.md` and leave one line in `progress.md` pointing to the archive file.
- Never delete a decision from `decision_log.md`. Mark it `Superseded` and link to the entry that replaced it instead. History must stay auditable even after the project changes direction.
- Archived files are read on demand, not by default. `knowledge/README.md` routing should not point to `archive/` unless the task explicitly needs old history.

## Freshness

A stale reference in a memory file is worse than no reference, because the agent trusts it silently.

- Give durable knowledge entries an `updated_at` (or `verified_at`) marker.
- Before relying on a fact that looks old, verify it against the live project state rather than assuming it still holds.
- Prefer noting "checked on DATE, may have drifted" over presenting an old fact as current.

## Memory Tiers Are Not Exclusive

Some tools (including Claude Code) keep their own private, cross-project memory for user preferences and working style. That tier and this project's file-based memory serve different purposes and should not duplicate each other:

- Tool-private memory: how the user likes to work, general habits, preferences that outlive any single project.
- This project's memory: facts, decisions, and state that belong to this project, are version-controlled, and must be readable by any tool or teammate.

If both exist, record project facts here, not in the tool's private memory, so nothing depends on a memory store other contributors and tools cannot see.
