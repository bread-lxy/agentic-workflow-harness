---
name: agentic-workflow-harness
description: Use when an AI coding agent (Codex, Claude Code, or similar) is doing complex agentic work, long-running tasks, workflow or tool design, durable memory design, handoff or resume across context compaction, or deciding between direct handling, workflow patterns, review-improve loops, and adaptive multi-agent collaboration.
---

# Agentic Workflow Harness

Use this skill to run durable, high-quality agentic work without overcomplicating it. The default stance is: choose the simplest effective work shape, externalize state for long-running tasks, verify outputs, and use multi-agent collaboration only when it materially improves the result.

## Quick Start

1. Inspect local project instructions and memory files before acting.
2. Decide the work shape: direct handling, deterministic tool, prompt chain, routing, parallelization, orchestrator-workers, review-improve loop, or multi-agent collaboration.
3. If the task is long-running, locate or create durable state files before relying on conversation memory.
4. Define the validation gate before major edits or irreversible decisions.
5. End with an updated handoff when work may continue later.

## Work Shape Selection

Prefer the least complex shape that can produce a reliable result:

- **Direct handling** for small, bounded tasks.
- **Deterministic scripts/tools** for repeatable transformations, syncs, audits, and checks.
- **Prompt chaining** when intermediate outputs should be inspected or constrained.
- **Routing** when inputs belong to different handling paths.
- **Parallelization** when independent branches can improve speed or coverage.
- **Orchestrator-workers** when a central agent must dynamically split and merge work.
- **Review-improve loop** when quality can be iteratively critiqued and revised.
- **Multi-agent collaboration** when context isolation, specialization, independent review, or parallel exploration improves outcome quality enough to justify coordination cost.

Do not use rigid multi-agent thresholds. Make the judgment from task shape, expected payoff, available verification, and coordination risk.

## Durable Memory

For tasks that cross sessions, dates, context compaction, multiple files, or multiple work streams, maintain durable state in the project:

- `feature_list.json` for capability or task inventory.
- `progress.md` for completed work, current status, validation, and next steps.
- `decision_log.md` for key decisions and tradeoffs.
- `handoff.md` for resume instructions.

If the project already has a state convention, use it. Otherwise, create a small `task_state/` folder near the relevant work.

## Reference Loading

Read only what the task needs:

- `references/work-shapes.md` for choosing the right execution shape.
- `references/durable-memory.md` for state files, resume, validation, and handoff.
- `references/project-knowledge-routing.md` for project memory layout and just-in-time loading.
- `references/multi-agent-collaboration.md` for adaptive multi-agent judgment, coordination patterns, and anti-patterns.
- `references/validation-and-handoff.md` for start, progress, and closeout checks.

Project-private knowledge belongs in project files, not in this global skill.
