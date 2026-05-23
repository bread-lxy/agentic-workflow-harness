# Repository Instructions

This repository packages a generic agentic workflow harness and durable memory system. Keep it domain-neutral.

## Boundaries

- Do not add project-specific business facts, private links, credentials, local personal paths, task artifacts, or one-off work history.
- Do not turn this package into a task template library. It should explain how an agent manages work, memory, validation, and handoff across projects.
- Keep examples generic: complex project, research notes, code change, document system, data processing, cross-session work.
- Prefer small, durable primitives over a heavy framework.

## Maintenance Rules

When changing the package:

1. Keep the skill, templates, scripts, and README aligned.
2. Update `scripts/check_package.py` when adding required files.
3. Run `python scripts/check_package.py`.
4. Run install and bootstrap dry runs before committing.
5. Keep scripts standard-library only.

## Core Promise

The harness should help any future agent answer:

- What is the current project trying to do?
- Which local memory files should be read first?
- What work shape is appropriate for this task?
- What state must survive context loss?
- What has been decided, verified, and handed off?
