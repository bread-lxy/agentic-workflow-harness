# Agentic Workflow Harness

一套通用的 agent 工作底座，用来在任何项目里建立可恢复、可验证、可交接的长期记忆体系。

它不绑定具体业务，也不保存任何项目私有知识。它只解决一个问题：当一个 agent 面对跨会话、跨文件、跨时间的复杂工作时，如何稳定地读取上下文、选择工作方式、记录状态、恢复任务、做出决策并完成交接。

## 这个项目包含什么

- `skills/agentic-workflow-harness/`：可安装到 Codex 的通用 skill。
- `templates/project/`：新项目的记忆体系模板。
- `scripts/install_codex_skill.py`：把 skill 安装到本机 Codex skill 目录。
- `scripts/bootstrap_project.py`：在任意项目里初始化通用 harness 与记忆文件。
- `scripts/check_package.py`：检查包结构、模板、引用和边界。
- `docs/`：方法说明、迁移指南和记忆体系设计说明。

## 适合什么场景

- 一个项目会持续很多天，不能只依赖聊天上下文。
- 需要让不同对话、不同 agent 或未来的自己接上同一条工作线。
- 项目里有知识入口、决策记录、进度记录和交接说明的需求。
- 需要在直接处理、脚本化、分阶段处理、并行处理、多 agent 协作之间做稳妥选择。
- 需要把验证方式和完成标准写清楚，减少“看起来完成了”的错觉。

## 快速开始

克隆仓库：

```powershell
git clone https://github.com/bread-lxy/agentic-workflow-harness.git
cd agentic-workflow-harness
```

安装 Codex skill：

```powershell
python scripts/install_codex_skill.py
```

先预览安装动作：

```powershell
python scripts/install_codex_skill.py --dry-run
```

为一个新项目初始化记忆体系：

```powershell
python scripts/bootstrap_project.py --target C:\path\to\your-project --project-name YourProject
```

如果只想预览会生成哪些文件：

```powershell
python scripts/bootstrap_project.py --target C:\path\to\your-project --project-name YourProject --dry-run
```

## 初始化后如何使用

新项目会得到一组通用入口：

- `AGENTS.md`：告诉 agent 进入项目后先读什么、怎么工作、哪些边界不能越过。
- `knowledge/README.md`：项目知识的总路由。
- `knowledge/agent-memory/AGENT_MEMORY.md`：稳定记忆入口。
- `knowledge/agent-memory/WORKFLOW_PLAYBOOK.md`：工作形态选择和执行守则。
- `knowledge/agent-memory/task_state/feature_list.json`：能力、任务和状态清单。
- `knowledge/agent-memory/task_state/progress.md`：进展、验证、当前状态。
- `knowledge/agent-memory/task_state/decision_log.md`：关键决策和取舍理由。
- `knowledge/agent-memory/task_state/handoff.md`：下一次对话或上下文压缩后的恢复入口。

日常使用建议：

1. 新任务先读 `AGENTS.md` 和 `knowledge/README.md`。
2. 复杂或跨会话任务继续读 `knowledge/agent-memory/AGENT_MEMORY.md`。
3. 如果任务会持续，先确认或更新 `task_state/`。
4. 任务推进到关键节点时更新进度和决策。
5. 结束时写清楚验证结果、未完成事项和下一步。

## 工作方式原则

- 先用最简单有效的形态，不为了显得复杂而引入复杂流程。
- 能用确定性脚本完成的重复工作，优先脚本化。
- 需要分阶段检查的任务，使用 prompt chain 或清晰的中间产物。
- 需要并行探索时，拆成独立输出再整合。
- 多 agent 只在上下文隔离、专业角色、并行收益或独立复核确实有价值时使用。
- 长期任务必须把状态写入文件，不能只依赖聊天记忆。
- 每次重要行动前先定义验证方式，结束时说明哪些已验证、哪些未验证。

## 维护本包

修改本仓库后运行：

```powershell
python scripts/check_package.py
python scripts/install_codex_skill.py --dry-run
python scripts/bootstrap_project.py --target .tmp-demo --project-name Demo --dry-run
git diff --check
```

本包应保持通用。不要加入业务事实、私有系统说明、具体任务产物、个人本地路径或凭据。

## License

MIT
