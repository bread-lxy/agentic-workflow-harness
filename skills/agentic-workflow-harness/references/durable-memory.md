# Durable Memory

Long-running agent work should not depend on chat memory. Durable memory externalizes state, makes progress inspectable, and supports resume after interruption, context compaction, or handoff.

## Required State Files

Use the project's existing convention when available. Otherwise create a compact `task_state/` folder with:

- `feature_list.json`: machine-readable inventory of capabilities, work streams, status, paths, and notes.
- `progress.md`: human-readable log of completed work, validation, current focus, blockers, and next steps.
- `decision_log.md`: key choices, tradeoffs, dates, and rationale.
- `handoff.md`: concise resume instructions for another session or agent.

Optional files can include run logs, source indexes, issue notes, or artifact manifests when the project needs them.

## Start Protocol

1. Read local instructions and memory files.
2. Inspect current files before assuming state.
3. Identify whether the task is short, complex, or long-running.
4. If long-running, locate or initialize state files.
5. Define the first validation gate.

## Progress Protocol

During work:

- Update state when a meaningful milestone is reached.
- Record decisions when choosing between viable options.
- Keep file paths and evidence concrete.
- Separate completed work from unverified assumptions.
- Avoid writing private credentials or secrets into state.

## Resume Protocol

On resume:

1. Read `handoff.md`.
2. Read `progress.md`.
3. Check `feature_list.json` for active or pending items.
4. Review recent decisions.
5. Verify the current filesystem or external system state before continuing.

Do not restart from scratch unless the state files are missing or obviously stale.

## Closeout Protocol

Before ending:

- Summarize what changed.
- Record what was validated and what was not.
- Update next steps.
- Note unresolved risks.
- Ensure another session can continue without the original chat context.

## Good Memory Is Compact

A good memory system should help the next agent answer:

- What are we trying to accomplish?
- What has already been done?
- What evidence supports that?
- What decisions shaped the current direction?
- What should happen next?
- What should not be repeated?
