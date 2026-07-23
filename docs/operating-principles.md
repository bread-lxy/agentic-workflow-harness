# Operating Principles

This package turns agent work into a durable project practice. It is intentionally small: a skill, a memory layout, templates, and standard-library scripts.

## 1. Start Simple

Use the simplest work shape that can reliably complete the task. A direct answer or deterministic script is often better than a more agentic setup.

Complexity is justified only when it improves outcome quality, speed, coverage, recovery, or clarity.

## 2. Externalize State

Chat memory is temporary. Project state should live in files that future sessions can inspect.

The minimum durable state is:

- `feature_list.json`
- `progress.md`
- `decision_log.md`
- `handoff.md`

## 3. Route Knowledge

Do not load every project file by default. Use a compact `knowledge/README.md` to route the agent to the smallest useful memory entry.

## 4. Validate Before Trusting

Before major action, decide how success will be checked. After action, record what passed and what remains uncertain.

## 5. Use Multi-Agent Work Sparingly

Multiple agents help when they provide context separation, parallel exploration, specialization, or independent review. They hurt when they duplicate work or create merge ambiguity.

The main agent remains responsible for synthesis.

## 6. Leave A Trail

If work may continue later, update the handoff. A good handoff lets another session resume without guessing.

## 7. Prune, Don't Just Accumulate

Durable state that only grows stops being durable — it becomes a junk drawer nobody reads in full. Archive old progress instead of piling it up, mark superseded decisions instead of deleting or ignoring them, and treat any memory file that has grown past a quick read as a signal to split it, not a signal to keep appending.
