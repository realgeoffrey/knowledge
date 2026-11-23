# OpenClaw 笔记

| 对比维度 | [OpenClaw](https://github.com/openclaw/openclaw) | [QwenPaw（原 CoPaw）](https://github.com/agentscope-ai/QwenPaw) | [nanobot](https://github.com/HKUDS/nanobot) | [NanoClaw](https://github.com/nanocoai/nanoclaw) | [ZeroClaw](https://github.com/zeroclaw-labs/zeroclaw) | [memU](https://github.com/NevaMind-AI/memU) |
| --- | --- | --- | --- | --- | --- | --- |
| 核心定位 | 自托管、多渠道 AI 助手 | 个人 AI 助手，可在本机或云上部署，支持多聊天应用 | 轻量、可自托管的 Python 个人助手 | 在容器中运行智能体的轻量个人助手，默认使用 Claude Agent SDK，也可选 Codex、Cursor 或 OpenCode | 可替换组件的 Rust 智能体运行时 | 跨智能体、会话和设备共享的个人记忆系统。完整助理项目见 [memUBot](https://github.com/NevaMind-AI/memUBot) |
| 许可证 | MIT | Apache-2.0 | MIT | MIT | MIT 或 Apache-2.0，可任选其一 | README 标注 Apache-2.0，仓库许可文件第 2 条措辞有改动。[许可原文](https://github.com/NevaMind-AI/memU/blob/main/LICENSE.txt) |
| 核心实现语言 | TypeScript | Python | Python | TypeScript | Rust | Python |
| 安全与隔离 | 工具沙盒默认关闭，启用后也须控制宿主权限与文件挂载 | Tool Guard 检查工具调用，File Guard 保护敏感路径，可配置系统级沙盒 | 可分别配置工作区路径限制与 shell 进程沙盒 | 默认容器隔离，强度取决于镜像与挂载 | 默认受监督模式按风险控制操作，可另配系统沙盒 | 记忆层的系统级隔离依赖宿主与存储后端 |
| 架构与性能 | Gateway 统一接入渠道并调度智能体 | 多代理、工作空间、Skills | Python 网关服务 Web UI、终端及聊天应用 | 单个宿主进程调度每个会话的容器 | 单个 Rust 二进制，可替换模型、工具、记忆组件 | 智能体提炼记忆，memU 负责存储、索引与检索 |
| 渠道与集成 | WhatsApp、Telegram、Slack 等，支持渠道插件 | 钉钉、飞书、QQ、Discord、iMessage 等 | Web UI、终端、聊天通道，支持 MCP | WhatsApp、Telegram、Slack、Discord 等适配器按需安装 | Discord、Telegram、Matrix、邮件、CLI 等 | 接入已有智能体，共享同一记忆后端 |
| 记忆与上下文 | 工作区 `MEMORY.md` 保存长期事实与决策，`memory/YYYY-MM-DD.md` 保存每日记录 | ReMe 管理可编辑、可检索的 Markdown 记忆 | 内置跨会话的长期记忆，可通过 Dream 整理 | 每个智能体组有自己的工作区与记忆 | 支持 SQLite 记忆存储和嵌入检索 | 用 Wiki 组织可复用记忆，也可从历史任务中提炼 Markdown 技能 |
| 更贴场景 | 快速试全功能，安全与运维自理 | 个人助理、多通道与国内 IM、AgentScope 栈 | 使用 Python 定制个人 Bot | 默认容器化又要常见 IM | 偏好单二进制部署或已有 Rust 后端 | 给多个已有智能体共享长期记忆 |
| 一句话 | 跨平台、插件多 | AgentScope 系的多通道个人助手 | Python 轻量个人助手 | 容器隔离、多消息端、可选运行时 | Rust 自治助理基础设施 | 跨智能体的个人记忆系统 |

1. OpenClaw 流程图

    一条入站消息由 Gateway 路由到会话。智能体组装上下文、请求模型，必要时运行工具并把结果送回模型，最终由 Gateway 对应的渠道适配器投递回复。[网关架构](https://docs.openclaw.ai/concepts/architecture) · [智能体循环](https://docs.openclaw.ai/concepts/agent-loop)

    ```mermaid
    flowchart TB
        %% 定义颜色样式
        classDef layerL1 fill:#e1f5fe,stroke:#0288d1,stroke-width:2px,color:#000
        classDef layerL2 fill:#fff3e0,stroke:#f57c00,stroke-width:2px,color:#000
        classDef layerL3 fill:#e8f5e9,stroke:#388e3c,stroke-width:2px,color:#000
        classDef layerL4 fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px,color:#000
        classDef highlightNode fill:#fff9c4,stroke:#fbc02d,stroke-width:2px,color:#000
        classDef defaultNode fill:#fff,stroke:#999,stroke-width:1px,color:#333

        subgraph L1["1. 用户接入层 (User Access Layer)"]
            direction LR
            User((用户))
            Gateway["Gateway Control Plane<br/>(网关控制平面)<br/>WhatsApp, Telegram, ..."]
            Canvas["设备节点 (Nodes)<br/>可按设备能力提供 Canvas 等功能"]

            User -- "1.发送消息/交互" --> Gateway
            User -- "2.查看/操作 UI" --> Canvas
            Gateway <--> Canvas
        end
        class L1 layerL1

        subgraph L2["2. 智能体核心 (Agent Core)"]
            direction LR
            subgraph CoreService["OpenClaw 核心服务 (Local / Self-hosted)"]
                direction LR
                Context["上下文组装 (Context Engine)<br/>-------------------<br/>• 当前会话历史<br/>• 工作区记忆文件<br/>• 可用工具与技能说明"]
                Decision(("决策与推理循环<br/>(Decision Loop)"))

                Context <--> Decision
            end
            LLM{"多模型路由与容灾<br/>(Model Failover)<br/>Claude, DeepSeek, GPT, ..."}

            Decision -- "调用模型，可按配置轮换凭据或切换备用模型" --> LLM
            LLM -- "回复文本或工具调用请求" --> Decision
        end
        class L2 layerL2

        subgraph L3["3. 执行与能力生态 (Execution & Capability Layer)"]
            direction LR
            Tools["执行工具 (Tools)<br/>-------------------<br/>• 可配置沙盒执行<br/>• 节点命令受权限与审批控制<br/>(system.run)"]
            Skills["技能与插件 (Skills & Plugins)<br/>-------------------<br/>• SKILL.md 提供使用说明<br/>• 插件可注册工具和渠道"]
            Auto["主动触发引擎<br/>(Cron / Event / Webhook)"]
        end
        class L3 layerL3

        subgraph L4["4. 响应与持续性 (Response & Persistence)"]
            DB[("持久化存储<br/>会话历史、工作区记忆文件")]
        end
        class L4 layerL4

        %% 层级间核心连线
        Gateway -- "3.转发请求" --> Decision

        Decision -- "4.调用" --> Tools
        Tools -- "返回工具结果" --> Decision
        Skills -. "提供技能说明" .-> Context
        Skills -. "插件注册工具" .-> Tools
        Auto -- "唤醒会话或发起运行" --> Gateway

        Decision -. "持久化记忆/状态" .-> DB
        DB -. "读取会话与记忆" .-> Context

        Decision -- "5.返回最终响应" --> Gateway
        Gateway -- "6.向原渠道投递回复" --> User

        %% 节点基础样式应用
        class User,Gateway,Context,Decision,Tools,Auto,DB defaultNode
        %% 高亮显示节点、模型与扩展能力
        class Canvas,LLM,Skills highlightNode
    ```

    图中的沙盒只在启用时隔离工具执行，Tailscale 用于远程访问 Gateway。工作区 Markdown 文件保存长期记忆，搜索索引帮助检索。[沙盒](https://docs.openclaw.ai/gateway/sandboxing) · [Tailscale](https://docs.openclaw.ai/gateway/tailscale) · [记忆](https://docs.openclaw.ai/concepts/memory)
