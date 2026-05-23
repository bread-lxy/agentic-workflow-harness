# Workflow Playbook

Use this playbook to choose the right work shape and keep tasks recoverable, verifiable, and easy to hand off.

## Work Shape Selection

**Direct handling.** Use when the task is small, bounded, and quick to check.

**Deterministic scripts or tools.** Use when input and output are stable, repeated, or structured.

**Prompt chaining.** Use when the task can be split into ordered stages and each stage produces an inspectable artifact.

**Routing.** Use when different input types require different handling paths.

**Parallelization.** Use when independent branches can improve speed or coverage and merging is simple.

**Orchestrator-workers.** Use when the main task must be dynamically split and then integrated by one accountable agent.

**Review-improve loop.** Use when the output can be critiqued against explicit criteria and improved in iterations.

**Multi-agent collaboration.** Use when context isolation, specialization, independent review, or parallel exploration clearly improves the result enough to justify coordination cost.

## Start Questions

Before complex work, answer:

1. What is the user's real goal?
2. What information is missing?
3. Can a deterministic step solve most of the task?
4. Does this need durable state?
5. What is the validation gate?
6. What should be written down for the next session?

## Long-Running State Protocol

Maintain:

- `task_state/feature_list.json`: capabilities, work streams, status, paths, notes.
- `task_state/progress.md`: completed work, validation, current focus, blockers, next steps.
- `task_state/decision_log.md`: key decisions, tradeoffs, dates, rationale.
- `task_state/handoff.md`: resume instructions for the next session.

Update state at meaningful milestones and at closeout.

## Multi-Agent Use

- Give each agent a concrete, independent, deliverable responsibility.
- Avoid overlapping write scopes.
- Use independent review intentionally, not by accident.
- Keep one main agent responsible for final synthesis and validation.

## Closeout Standard

Before ending:

1. Output is usable.
2. Validation is stated.
3. Unverified assumptions are named.
4. Durable state is updated when work may continue.
5. Handoff is short, concrete, and path-based.
