
# 🤖 AI Agent Framework

基于 Plan-Execute 架构的 AI 代理框架，支持 LLM 驱动的任务规划、执行和重新规划。

## 架构

```
  User Input
       │
       ▼
 Planner ──计划步骤──► Executor ──工具调用──► Tools
 (LLM)                 (LLM)
       ▲                  │
       └──评估结果────────┘
       │
       ├── 需要调整 → 重新规划
       └── 完成 → 输出结果
```

采用 Plan-Execute 循环：Planner 制定计划 → Executor 逐步执行 → Planner 评估 → 决定继续或重新规划。

## 快速开始

```bash
pip install -r requirements.txt
```

在项目根目录创建 `apikey.json`：

```json
{
    "key": "your-deepseek-api-key",
    "key2": "your-siliconflow-api-key"
}
```

运行：

```bash
python main.py
```

## 项目结构

```
Agent/
├── main.py                  # 入口：CLI 交互
├── agent/
│   ├── core.py              # Agent 主循环（plan → execute → replan）
│   ├── planner.py           # Planner：制定计划、评估结果、重新规划
│   ├── executor.py          # Executor：执行步骤、调用工具
│   ├── llm.py               # LLM 客户端（DeepSeek / SiliconFlow）
│   ├── tools.py             # 工具动态加载（按需扩展）
│   └── logger.py            # 对话日志
├── agent/utils/             # 工具目录（可扩展）
├── apikey.json              # API 密钥
└── pyproject.toml
```

## 核心设计

### 双角色循环

| 角色 | 职责 | 决策依据 |
|------|------|---------|
| **Planner** | 拆解任务、制定步骤、评估结果 | 完整对话历史 |
| **Executor** | 执行单步、调用工具、返回结果 | 当前步骤 + 工具列表 |

### LLM 驱动

- 基于 DeepSeek Chat 模型
- 支持切换 SiliconFlow 等 OpenAI 兼容 API
- Planner 和 Executor 共享同一模型，但使用不同的 System Prompt

### 工具系统

- 自动扫描 `utils/` 目录动态加载工具
- 工具类需包含 `desc` 属性用于 LLM 识别
- 通过函数名和参数实现动态调用

### 工作流程

1. 用户输入指令（`>` 前缀重置状态）
2. Planner 生成执行计划（多个步骤）
3. Executor 逐步骤执行（调用工具或直接回复）
4. Planner 评估执行结果
5. 需要调整 → 返回步骤 3 重新规划
6. 任务完成 → 输出结果

## 依赖

- Python >= 3.13
- openai（LLM API 客户端）
