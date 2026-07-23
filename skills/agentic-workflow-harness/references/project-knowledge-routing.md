# Project Knowledge Routing

A project should not load every memory file for every task. Use a small routing layer so the agent reads only the context needed for the current work.

## Recommended Layout

```text
AGENTS.md
CLAUDE.md (imports AGENTS.md, only needed for Claude Code)
knowledge/
  README.md
  agent-memory/
    AGENT_MEMORY.md
    WORKFLOW_PLAYBOOK.md
    task_state/
      feature_list.json
      progress.md
      decision_log.md
      handoff.md
```

## File Responsibilities

`AGENTS.md` is the first project instruction file. It should describe the default reading order, boundaries, and how to use the harness inside the project.

`CLAUDE.md` exists only so Claude Code loads `AGENTS.md` automatically via `@AGENTS.md` (Claude Code does not read `AGENTS.md` natively). Tools that already follow the AGENTS.md convention don't need it.

`knowledge/README.md` is the knowledge router. It should tell the agent which memory files to read for different kinds of work.

`AGENT_MEMORY.md` is the compact stable memory entry. It should hold durable rules, current project conventions, and links to deeper files.

`WORKFLOW_PLAYBOOK.md` explains how the project chooses work shapes and validates progress.

`task_state/` is the recovery layer for active or long-running work.

## Routing Rules

- Start from the smallest relevant entry.
- Read deeper files only when the task needs them.
- Keep historical or bulky artifacts out of the default path.
- Keep private credentials and personal access data out of memory files.
- Prefer source locators and summaries over raw dumps.

## When To Add More Memory Areas

Add a new knowledge area only when it has a stable purpose, such as:

- Product or domain facts.
- Technical architecture.
- User research notes.
- Data source indexes.
- Operations playbooks.

Each area should have its own compact entry file and should be linked from `knowledge/README.md`.
