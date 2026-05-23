# Multi-Agent Collaboration

Use multiple agents when the expected improvement in result quality, coverage, speed, context management, or independent review is worth the coordination cost.

Do not treat multi-agent orchestration as inherently better. It increases token use, latency, merge complexity, and the risk of duplicated or conflicting work.

## Valuable Uses

**Context separation.** Different agents can hold different slices of a large problem without crowding one context.

**Parallel exploration.** Independent agents can search different paths at the same time when the answer space is wide.

**Role specialization.** Agents can be assigned distinct lenses: implementer, reviewer, researcher, data auditor, documentation synthesizer, or release checker.

**Independent review.** One agent can produce and another can critique, reproduce, or test, reducing confirmation bias.

**Large surface area.** When a task touches many files, systems, or artifacts, workers with disjoint ownership can reduce bottlenecks.

## Coordination Costs

Before using multiple agents, account for:

- Setup time and prompt specificity.
- Shared context loss.
- Duplicate work.
- Merge conflicts or incompatible assumptions.
- Increased latency and cost.
- Need for a main integrator to adjudicate disagreements.

The main agent remains accountable for final synthesis and validation.

## Practical Patterns

**Scout agents** answer bounded questions: where is X, what does Y depend on, what are the likely risks?

**Worker agents** modify disjoint files or build isolated artifacts. Give them explicit ownership and tell them not to revert others' work.

**Reviewer agents** critique a concrete output against a checklist, requirements, or user intent.

**Research agents** gather evidence, source links, and uncertainty.

## Anti-Patterns

Avoid:

- Spawning agents because the task feels important but is actually linear.
- Giving vague tasks without a concrete output.
- Assigning overlapping write scopes.
- Letting agents decide incompatible standards without a shared checklist.
- Accepting sub-agent conclusions without integration or validation.
- Using multi-agent work to compensate for unclear goals.

## Adaptive Trigger

Ask:

1. What would a second agent know, inspect, or verify that the main agent would not handle as well?
2. Can the work be split without heavy shared state?
3. Is there a clear handoff artifact from each agent?
4. Does the task benefit from independent judgment rather than one continuous reasoning thread?
5. Is the final integration cost acceptable?

If the answers are strong, use multi-agent collaboration. If not, use a simpler workflow.
