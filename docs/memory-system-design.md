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
