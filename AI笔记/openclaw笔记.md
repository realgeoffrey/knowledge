# openclaw笔记

| 对比维度 | [OpenClaw](https://github.com/openclaw/openclaw) | [CoPaw](https://github.com/agentscope-ai/CoPaw) | [NanoBot](https://github.com/HKUDS/nanobot) | [NanoClaw](https://github.com/qwibitai/nanoclaw) | [ZeroClaw](https://github.com/zeroclaw-labs/zeroclaw) | [MemU](https://github.com/NevaMind-AI/memU) |
| --- | --- | --- | --- | --- | --- | --- |
| 核心定位 | 个人 AI 助手；任意 OS / 平台 | 个人 AI 助手；易装；本机或云；多聊天应用、易扩展 | 超轻量 OpenClaw（仓库副标题） | 容器内轻量替代 OpenClaw（强调安全）；多消息端；记忆与定时任务；Anthropic Agents SDK | 快、小、全自主的个人助理基础设施；任意 OS / 平台；随处部署、组件可换 | 面向 24/7 **主动式（proactive）** agent 的记忆框架；结构化记忆、降常驻 token；对标 OpenClaw 系产品的说法见 [memUBot](https://github.com/NevaMind-AI/memUBot) README |
| 开源许可 | MIT | Apache-2.0 | MIT | MIT | Apache-2.0 | Apache-2.0 |
| 主语言（GitHub 标注） | TypeScript | Python | Python | TypeScript | Rust | Python |
| 安全与隔离 | 配置与工具权限决定边界；本地执行命令有误操作与越权面 | 发行说明含敏感路径 file access guard 等；以当前版文档为准 | 轻量实现，策略多在部署与自改代码 | 默认容器收敛攻击面；强度取决于镜像与挂载 | Rust 内存安全；隔离看设计与部署 | 记忆与编排层；系统级安全依赖宿主与其它组件 |
| 架构与性能 | 功能面大，默认栈偏重 | 多代理、工作空间、Skills，偏工程化整合 | 刻意做减法，体量小 | 容器有固定开销，换稳定性与边界 | fast、small，资源敏感场景 | 记忆管线与外部存储有持续开销；长期在线成本为自述重点 |
| 渠道与集成 | 插件多；第三方协议变更可能波及个别通道 | 钉钉、飞书、QQ、Discord、iMessage 等（README Core capabilities）；细节以发行说明为准 | 易作轻量网关对接外部通道 | WhatsApp、Telegram、Slack、Discord、Gmail 等（自述） | 偏基础设施与吞吐，多平台 UI 非卖点 | 本库重心在记忆；完整助理形态见 memUBot |
| 记忆与上下文 | 依赖配置与插件；长期记忆需自设计一致性与清理 | 记忆与个性化可控；工作空间级隔离类能力 | 偏会话级，长期记忆需自研 | 记忆与定时任务；绑定 Anthropic Agents SDK | 深度记忆非主叙事 | 类文件系统结构化记忆、proactive 生命周期、意图捕捉 |
| 更贴场景 | 快速试全功能，安全与运维自理 | 个人助理、多通道与国内 IM、AgentScope 栈 | 少量代码定制极简 Bot | 默认容器化又要常见 IM | 低配机或偏后端高性能栈 | 长期记忆与 proactive 底座；若要对标 OpenClaw 产品路线看 memUBot |
| 一句话 | 生态大、跨平台、插件多 | AgentScope 系：多通道、工程化、路径类守护 | 极简 OpenClaw 路线 | 容器 + 多消息端 + Agents SDK | Rust、轻快的自治助理基础设施 | proactive 记忆框架；产品叙事在 memUBot |

1. 较完整openclaw流程图

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
            Canvas["Nodes & Live Canvas<br/>(终端节点与实时画布)<br/>Windows, macOS, 移动端"]

            User -- "1.发送消息/交互" --> Gateway
            User -- "2.查看/操作 UI" --> Canvas
            Gateway <--> Canvas
        end
        class L1 layerL1

        subgraph L2["2. 智能体核心 (Agent Core - 本地驻留 大脑与记忆)"]
            direction LR
            subgraph CoreService["OpenClaw 核心服务 (Local / Self-hosted)"]
                direction LR
                Context["上下文引擎(Context Engine)<br/>-------------------<br/>• 短期会话记忆<br/>• 长期语义知识库(Vector DB)<br/>• 本地配置<br/>(~/.openclaw/openclaw.json)"]
                Decision(("决策与推理循环<br/>(Decision Loop)"))

                Context <--> Decision
            end
            LLM{"多模型路由与容灾<br/>(Model Failover)<br/>Claude, DeepSeek, GPT, ..."}

            Decision -- "执行指令<br/>(支持OAuth/API密钥轮换)" --> LLM
            LLM -- "推理结果" --> Decision
        end
        class L2 layerL2

        subgraph L3["3. 执行与能力生态 (Execution & Capability Layer)"]
            direction LR
            Tools["沙盒系统工具(Sandboxed Tools)<br/>-------------------<br/>• Docker隔离 & Tailscale VPN<br/>• 节点命令白名单<br/>(system.run)"]
            Skills["扩展技能生态(Skills & Plugins)<br/>-------------------<br/>• 基于 SKILL.md 声明式驱动<br/>• NPM插件生态 (Voice,微信等)"]
            Auto["主动触发引擎<br/>(Cron / Event / Webhook)"]
        end
        class L3 layerL3

        subgraph L4["4. 响应与持续性 (Response & Persistence)"]
            DB[("本地存储 / 数据库<br/>(状态审计, 记录日志)")]
        end
        class L4 layerL4

        %% 层级间核心连线
        Gateway -- "3.转发请求" --> Decision
        Canvas -. "状态/UI 同步" .- Decision

        Decision -- "4.调用" --> Tools
        Decision -- "4.调用" --> Skills
        Auto -- "触发自动化任务" --> LLM

        Tools -. "写入执行结果" .-> DB
        Skills -. "写入执行结果" .-> DB
        Decision -. "持久化记忆/状态" .-> DB

        DB -- "5.生成最终响应" --> Gateway

        %% 节点基础样式应用
        class User,Gateway,Context,Decision,Tools,Auto,DB defaultNode
        %% 高亮显示最新架构中的核心升级点
        class Canvas,LLM,Skills highlightNode
    ```
