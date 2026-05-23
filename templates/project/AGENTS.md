# Project Instructions

Use this project as a durable, file-backed working environment. Do not rely on chat memory alone for complex or long-running work.

## Default Reading Order

1. Read this file.
2. Read `knowledge/README.md`.
3. For complex or cross-session work, read `knowledge/agent-memory/AGENT_MEMORY.md`.
4. If resuming active work, read `knowledge/agent-memory/task_state/handoff.md`, then `progress.md`, `feature_list.json`, and `decision_log.md`.

## Working Rules

- Choose the simplest effective work shape: direct handling, deterministic tool, prompt chain, routing, parallelization, orchestrator-workers, review-improve loop, or multi-agent collaboration.
- Define a validation gate before major edits or irreversible decisions.
- For long-running work, update `task_state/` at meaningful milestones.
- Record important decisions in `decision_log.md`.
- End with a clear handoff when work may continue later.

## Boundaries

- Do not store credentials, private tokens, browser session data, personal access material, or raw private dumps in memory files.
- Do not treat historical notes as current truth without checking the live project state.
- Prefer source locators and concise summaries over bulky copied artifacts.

## Project Name

`{{PROJECT_NAME}}`
