# Repository Instructions

## Context7

Use Context7 MCP to fetch current documentation whenever the user asks about a library, framework, SDK, API, CLI tool, or cloud service. This includes API syntax, configuration, version migration, library-specific debugging, setup instructions, and CLI usage.

Always start with `resolve-library-id` using the library name and the user's question, unless the user provides an exact library ID in `/org/project` format. Then use `query-docs` with the selected library ID and the user's full question. Prefer Context7 over web search for library documentation.

Do not use Context7 for refactoring, writing scripts from scratch, debugging business logic, code review, or general programming concepts.

## Agentic Workflow Harness

For complex agentic work, eval automation, long-running tasks, workflow/tool design, handoff or resume, and adaptive multi-agent orchestration, use the global `agentic-workflow-harness` skill. Prefer the simplest effective workflow shape, maintain durable project state for long-running work, validate outputs, and choose multi-agent collaboration adaptively based on task needs and outcome quality.

## Context Engineering Skills

Use the installed skills from `muratcankoylan/Agent-Skills-for-Context-Engineering` whenever the conversation naturally matches their trigger conditions. The user should not need to explicitly repeat "Triggers On"; treat these as internal activation cues.

- `context-fundamentals`: understanding context, explaining context windows, designing agent architecture, context components, attention mechanics, progressive disclosure, or context budgeting.
- `context-degradation`: diagnosing context problems, fixing lost-in-the-middle behavior, debugging agent failures, context poisoning, context clash, context confusion, or unexpected agent performance degradation.
- `context-compression`: compressing context, summarizing conversation history, implementing compaction, reducing token usage, structured summarization, or long-running sessions near context limits.
- `context-optimization`: optimizing context, reducing token costs, KV-cache optimization, observation masking, context partitioning, context budgeting, or extending effective context capacity.
- `latent-briefing`: KV cache compaction between agents, worker KV memory handoff, latent briefing, cross-agent memory without summarization, or hierarchical agent token explosion.
- `multi-agent-patterns`: designing multi-agent systems, supervisor/orchestrator patterns, swarm architecture, sub-agents, handoffs, context isolation, or parallel agent execution.
- `memory-systems`: implementing agent memory, persisting state across sessions, building knowledge graphs, tracking entities, or comparing memory frameworks.
- `tool-design`: designing agent tools, tool descriptions, MCP tools, reducing tool complexity, tool consolidation, namespacing, or agent-tool interfaces.
- `filesystem-context`: offloading context to files, dynamic context discovery, file-based memory, tool output persistence, agent scratch pads, or just-in-time context loading.
- `hosted-agents`: background agents, hosted coding agents, sandboxed execution, remote coding environments, Modal sandboxes, self-spawning agents, or multiplayer agent infrastructure.
- `evaluation`: evaluating agent performance, building test frameworks, measuring agent quality, quality gates, multi-dimensional evaluation, or validating context engineering choices.
- `advanced-evaluation`: LLM-as-judge systems, comparing model outputs, evaluation rubrics, direct scoring, pairwise comparison, position bias, bias mitigation, or automated quality assessment.
- `project-development`: starting an LLM project, designing batch pipelines, task-model fit analysis, agent-assisted development, cost estimation, structured output design, or choosing between LLM and traditional approaches.
- `bdi-mental-states`: modeling agent mental states, BDI architecture, belief-desire-intention models, transforming RDF to beliefs, cognitive agents, rational agency, or neuro-symbolic AI integration.
