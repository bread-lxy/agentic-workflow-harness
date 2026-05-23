# Agent Memory

Long-running or complex work should read this file first after `knowledge/README.md`. This file keeps stable operating rules only; detailed history belongs in `task_state/` or a project-specific history area.

## Default Work Shape

- Use the simplest effective way to solve the problem: direct handling, deterministic tool, prompt chain, routing, parallelization, orchestrator-workers, review-improve loop, or multi-agent collaboration.
- Use multi-agent collaboration only when context separation, parallel coverage, specialization, or independent review materially improves the result.
- For code or knowledge changes, define the validation path before making the change.

## Durable State

- Current resume entry: `knowledge/agent-memory/task_state/handoff.md`.
- Capability and work inventory: `knowledge/agent-memory/task_state/feature_list.json`.
- Progress summary: `knowledge/agent-memory/task_state/progress.md`.
- Decisions and tradeoffs: `knowledge/agent-memory/task_state/decision_log.md`.

## Project-Specific Routes

Add stable project routes here as they emerge.

Example:

- Architecture entry: `knowledge/architecture/README.md`.
- Research entry: `knowledge/research/README.md`.
- Operations entry: `knowledge/operations/README.md`.

## Prohibited Memory

- Credentials, private tokens, browser session data, personal access material.
- Full raw dumps when a source locator and summary would be enough.
- One-off artifacts that can be regenerated.
- Unchecked assumptions presented as current facts.
