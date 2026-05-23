# Validation And Handoff

Use these checks as lightweight guards. Do not turn them into busywork for tiny tasks.

## Start Of Task

- Read relevant project instructions and memory files.
- Identify the user's real goal and likely success criteria.
- Choose the simplest effective work shape.
- Decide whether durable state is needed.
- Define the validation gate.
- Identify private data boundaries and avoid writing secrets.

## Tool And Workflow Design

- Is the input shape clear?
- Is output structured enough for downstream use?
- Can failures be localized?
- Is there a reproducible run path?
- Does the tool preserve evidence needed for later review?
- Is the user-facing result explainable?

## Progress Update

- What changed since the previous checkpoint?
- What has been verified?
- What is still uncertain?
- What decision was made and why?
- What should happen next?

## Closeout

- Output is usable without extra interpretation.
- Validation and limitations are explicit.
- State files are updated if the task may continue.
- Handoff is short, concrete, and path-based.
- No private credentials or personal access material were written.

## Handoff Contents

A good handoff includes:

- Current goal.
- Current status.
- Reading order for the next session.
- Completed work.
- Verified checks.
- Open risks.
- Next concrete steps.
- Things not to repeat.
