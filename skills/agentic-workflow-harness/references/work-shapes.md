# Work Shapes

Agentic systems work best when the structure matches the task. Start with the smallest reliable shape, then add flexibility only where it improves quality, speed, coverage, or recovery.

## Direct Handling

Use direct handling when the task is small, bounded, and quickly checkable.

Good fit:

- Explain a file.
- Make a narrow change.
- Summarize a short artifact.
- Answer a question using already loaded context.

## Deterministic Tools

Use scripts or structured tools when inputs and outputs are stable.

Good fit:

- Repeating a transformation.
- Checking a file set.
- Producing structured artifacts.
- Reducing manual copying or transcription mistakes.

Tool outputs should be predictable, traceable, and easy to verify.

## Prompt Chaining

Use prompt chaining when a task has meaningful intermediate products.

Good fit:

- Extract facts, then classify them, then synthesize a result.
- Draft a plan, then critique it, then revise it.
- Turn raw notes into a stable knowledge entry.

Each step should produce something inspectable before the next step depends on it.

## Routing

Use routing when different inputs require different handling paths.

Good fit:

- Bug report vs. product question vs. documentation request.
- Code change vs. research task vs. project cleanup.
- Known path vs. unknown path.

Routing prevents one generic procedure from blurring distinct problems.

## Parallelization

Use parallel work when branches are independent and merging is simple.

Good fit:

- Inspect several files.
- Compare separate options.
- Gather independent evidence.
- Review disjoint areas of a large project.

Keep outputs concrete so the main agent can merge them without guesswork.

## Orchestrator-Workers

Use orchestrator-workers when the decomposition is not fully known in advance and a central agent must divide, assign, and merge work.

Good fit:

- Large repository exploration.
- Multi-part document restructuring.
- Several independent work streams with shared goals.

The orchestrator remains accountable for final decisions and validation.

## Review-Improve Loop

Use a review-improve loop when quality criteria can be expressed and iteration is cheaper than one-shot perfection.

Good fit:

- Polish a proposal.
- Tighten a design.
- Refine a generated artifact against a checklist.
- Improve a tool interface.

Keep the review criteria explicit and record what changed between iterations.

## When To Add Agency

Add more dynamic planning when:

- The task requires exploration.
- Information is incomplete.
- The next step depends on discoveries.
- Tool failures require adaptive recovery.
- Several plausible solution paths exist.

Even then, keep the harness external: record plan, state, decisions, and validation outside the chat.
