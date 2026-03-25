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
