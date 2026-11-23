
# AI繁多的词汇

## 目录
1. [【一站式 LLM底层技术原理入门指南】](#一站式-llm底层技术原理入门指南)
1. [词汇表](#词汇表)

---
### [【一站式 LLM底层技术原理入门指南】](https://s3tlxskbq3.feishu.cn/docx/NyPqdCKraoXz9gxNVCfcIFdnnAc)
1. 人工智能（Artificial Intelligence，AI）：研究如何让机器具备感知、学习、推理和决策等能力的计算机科学分支，涵盖计算机视觉（Computer Vision，CV）、自然语言处理（Natural Language Processing，NLP）、自动语音识别（Automatic Speech Recognition，ASR）、文本转语音（Text to Speech，TTS）、知识图谱（Knowledge Graph）等领域。

    1. 机器学习（Machine Learning，ML）：从观测数据中学习规律，并将学到的规律用于新样本的预测或决策。下文的有监督、无监督、自监督和强化学习按学习信号来区分，特征和深度学习则涉及数据表示与模型结构。

        1. 有监督学习（Supervised Learning）：使用输入与目标成对的训练数据学习映射关系。目标可以来自人工标注，也可以来自实际观测，例如预测房价时使用真实成交价。
        1. 无监督学习（Unsupervised Learning）：从未标记数据中发现结构、模式或关联，例如按相似度对样本聚类。

            1. 自监督学习（Self-supervised Learning）：从数据本身构造预测目标。例如，将一段文本的前缀作为输入，用紧随其后的 token 作为训练目标，无需逐条人工标注。
        1. 强化学习（Reinforcement Learning）：智能体（Agent）根据与环境（Environment）交互得到的经验学习策略，目标是最大化期望累积奖励。
        1. 特征（Feature）：从原始数据中提取的、用于表示样本的属性或信息。

            > 例如，模型既可以直接使用原始像素，也可以学习边缘或纹理等中间特征。
        1. 深度学习（Deep Learning）：使用深层、复杂结构的神经网络进行学习的方法。通过多层学习抽象和高级特征表示，更好地捕捉数据的内在结构和特性。

            1. 端到端学习（End-to-End Learning）：用任务的最终目标联合优化从输入到输出的可训练模块。模块可以先分别预训练，再一起微调。

                > 例如，语音识别系统可以从语音输入直接学习输出文字，以转写目标联合训练各层。

### 词汇表
1. 模型（Model）：表示数据输入与输出之间映射关系的数学函数或算法结构。
1. Agent（智能体、代理）：能够感知环境、做出决策并执行行动的自主实体。多智能体框架（Multi-Agent Framework）支持多个智能体协同工作的开发平台。
1. 参数（Parameters）：模型在训练中学到的数值，如权重和偏置。80 亿个参数按 BF16 存储，单是权重就约占 16 GB。训练还需为激活、梯度和优化器状态留空间。自回归推理要预留运行缓冲，启用 KV 缓存时还要计入它的开销。[KV 缓存说明](https://huggingface.co/docs/transformers/kv_cache)
1. 量化（Quantization）：用较少的位数表示权重，有些方案也量化激活。它可以降低内存占用，推理速度和精度的变化取决于硬件、算法和任务。[Transformers 量化说明](https://huggingface.co/docs/transformers/quantization/overview)
1. 知识蒸馏（Distillation）：通过教师模型的输出等信号训练学生模型，常用于压缩模型。
1. 半监督学习（Semi-supervised Learning）：结合少量标注数据和大量未标注数据进行训练的学习范式。标注（Annotation）是为数据添加标签的过程。
1. Prompt（提示词）：提供给模型、用来引导输出的输入，可包含问题、指令、示例或参考材料。
1. 上下文长度（Context Length）：规格表中的「最大上下文长度」通常指一次请求能处理的 token 上限。输入和生成的输出通常共用额度，具体模型还可能单独限制输入或输出长度。
1. 上下文窗口（Context Window）：常与最大上下文长度同义。系统指令、本轮问题、实际传入的对话历史和工具结果都可能占用空间。长对话可通过截断、摘要或检索来选择本轮内容。[上下文窗口说明](https://platform.claude.com/docs/en/build-with-claude/context-windows)
1. Token（词元）：分词器将文本编码后得到的模型处理单位，可能是一个词、一个子词、标点或部分字节。同一段话换用不同分词器，token 数可能不同。
1. SOP（Standard Operating Procedure，标准操作程序）：通过标准化流程将复杂任务分解为可重复执行的具体步骤，实现效率提升、质量控制和经验传承。核心在于细节量化与流程固化，适用于企业生产、个人管理和技术系统设计。
1. 工具与框架：Ollama（可在本地运行模型）、Label Studio（数据标注平台）、Cherry Studio（多模型 AI 工作台）、Dify（支持 RAG 与工作流的低代码 LLM 应用开发平台）、LangChain（用代码构建 LLM 应用和智能体的框架）。
1. MCP（Model Context Protocol，模型上下文协议）：基于 JSON-RPC 2.0，连接 AI 应用与外部工具、资源和提示模板。标准传输包括 stdio 与 Streamable HTTP。2026-07-28 版将旧 HTTP+SSE 传输以及 Roots、Sampling、Logging 标为弃用。Streamable HTTP 仍可用 SSE 返回事件流，服务端也可通过多轮请求向客户端征询输入（Elicitation）。[协议更新](https://blog.modelcontextprotocol.io/posts/2026-07-28/) · [MCP 笔记](MCP笔记.md)
1. A2A（Agent2Agent Protocol）：面向智能体之间的协作。客户端通过 Agent Card 了解对方的能力，向服务端智能体发送消息，并可跟踪任务和接收产物。它与 MCP 的工具和数据接入能力互补。[A2A 核心概念](https://a2a-protocol.org/latest/topics/key-concepts/)
1. ANP（Agent Network Protocol）：面向开放网络的智能体协议，涵盖去中心化身份、能力描述、发现与通信，例如使用 `did:wba` 标识智能体。[ANP 规范](https://agent-network-protocol.com/)
1. 知识库（Knowledge Base，KB）：组织和存储知识、支持查询或检索的系统。内容可以是结构化的事实或规则，也可以是文档等非结构化资料。
1. RAG（Retrieval-Augmented Generation，检索增强生成）：先检索与问题相关的资料，再将检索结果作为生成回答的依据。检索可能遗漏资料，模型也可能误读资料，因此检索质量和回答是否有据需要分别评估。[RAG 原论文](https://arxiv.org/abs/2005.11401)
1. 召回率（Recall）：找回的相关结果数 ÷ 全部相关结果数。精确率（Precision）则用返回的结果数作分母。例如，共有 5 篇相关文档，前 10 条结果中有 3 篇相关，则 Recall@10 = 3/5，Precision@10 = 3/10。固定排序时，增大 K 会使召回率保持或上升，精确率取决于新增结果。检索工程里说「召回」也可指获取候选结果的阶段。
1. Embedding（嵌入）：将数据转换为数值向量的技术，用于表示语义信息。
1. 嵌入模型（Embedding Model）：将文本、图像等支持的数据编码为向量。用于检索时，查询和文档须映射到相互对齐的空间。例如，两款模型即使都输出 768 维向量，坐标的含义也可能不同。
1. 向量数据库（Vector Database）：存储向量及其关联数据，支持按余弦相似度、内积或距离检索近邻。大规模检索常用近似最近邻索引，在速度、内存与检索召回率之间权衡。
1. 对话式AI（Conversational AI）：能够进行自然对话交互的人工智能系统。
1. 自然语言处理（Natural Language Processing，NLP）：用计算机处理人类语言的领域，涵盖理解、检索、翻译和生成等任务。
1. 自动语音识别（Automatic Speech Recognition，ASR）：将语音转写成文本，例如生成会议逐字稿。
1. 自然语言理解（Natural Language Understanding，NLU）：从语言输入中识别意图、实体及其关系。例如，从「订明天去上海的车票」中识别订票意图、出行日期和目的地。生成回复属于自然语言生成（NLG）。
1. 文本转语音（Text to Speech，TTS）：将文本转换为语音输出的技术。
1. BERT（Bidirectional Encoder Representations from Transformers）：Google 提出的 Transformer 编码器模型。它结合左右两侧的上下文预测被遮盖的词元，原版预训练还包含下一句预测任务。微调后可做分类或抽取式问答。[BERT 原论文](https://aclanthology.org/N19-1423/)
1. 计算机视觉（Computer Vision，CV）：让计算机理解和分析视觉信息的技术。
1. Transformer 架构：基于自注意力机制（Self-Attention）的深度学习架构，序列中各位置能根据相关性汇集其他可见位置的信息。2017 年提出的原始架构包含编码器和解码器。BERT 使用编码器，GPT 类模型通常采用带因果掩码的解码器，使每个位置只能读取自身及之前的位置。[Transformer 原论文](https://arxiv.org/abs/1706.03762)
1. 预训练模型（Pre-trained Model）：在大规模数据上预先训练的模型，可通过微调适应特定任务。
1. Hugging Face：其 Hub 平台托管模型、数据集和演示应用，也提供 Transformers 等开源工具。Hub 上的模型各有自己的许可证和访问条件。
1. 推理（Inference）与推理模型（Reasoning Model）：前者是用训练好的模型进行预测或生成的运行阶段。后者指针对复杂多步求解优化的模型，例如 DeepSeek-R1。这类模型在生成答案时也经历推理运行阶段。[DeepSeek-R1 模型说明](https://github.com/deepseek-ai/DeepSeek-R1)
1. 大语言模型（Large Language Model，LLM）：在大规模语料上训练的语言模型，可用于生成、总结、翻译等任务。常见生成式 LLM 基于 **Transformer 架构**，预训练时自监督地预测下一个 token，之后还可通过指令微调、基于反馈的优化等后训练方法改善行为。

    1. 开放权重模型（Open Weights）：权重可获取，具体使用和再分发条件取决于版本许可证。OSI 的开源 AI 定义还要求提供用于修改系统的代码、数据信息等。[OSI 定义](https://opensource.org/ai/open-source-ai-definition)

        例如 Llama 3.3（Meta）、Qwen2.5-7B-Instruct（通义千问）、DeepSeek-R1、Mistral-7B-v0.1、BERT、Kimi-K2-Instruct（月之暗面）、Grok-1、Grok-2。Grok-2 的权重采用其社区许可证，Kimi-K2-Instruct 采用修改版 MIT 许可证。[Grok-2 模型卡](https://huggingface.co/xai-org/grok-2) · [Kimi-K2-Instruct 模型卡](https://huggingface.co/moonshotai/Kimi-K2-Instruct)
    2. 未公开权重的模型（Closed Weights）：通常通过 API 或应用访问，服务方运行模型。

        例如 GPT-4、Claude 3 Opus、Gemini 1.5 Pro。同一机构可能另行发布开放权重模型，如 OpenAI 的 gpt-oss。遇到文心一言、讯飞星火等产品名时，也需要查明背后的模型版本。[gpt-oss 官方仓库](https://github.com/openai/gpt-oss)
1. 记忆模组（Memory Module）：AI智能体维护上下文的机制，包括短期记忆（工作记忆）和长期记忆（持久化存储）。
1. 推理层（Reasoning Layer）：某些 AI 应用架构对负责规划、推导或选择行动的部分的称呼，具体职责由系统定义。
1. AI 智能体框架（AI Agent Framework）：提供模型调用、工具执行、状态管理等可复用组件的开发平台或库。应用仍需定义工具权限、任务结束条件和失败处理。
1. AI助手（AI Assistants）：协助用户完成任务的智能应用系统。
1. PyTorch：由 Meta/Facebook 发起的开源深度学习框架，现由 Linux Foundation 旗下 PyTorch Foundation 治理，提供动态计算图和丰富的工具生态。
1. 生成式 AI（Generative AI）：学习数据的模式并据此生成文本、图像、声音等内容。输出可由提示词、图像等条件引导。
1. 视觉语言模型（Vision-Language Model，VLM）：同时处理视觉与语言信息的模型。有的生成图像描述或回答视觉问题，有的仅为图像和文本编码、计算匹配度，例如用于图文检索的 CLIP。[CLIP 项目说明](https://openai.com/index/clip/)
1. 数字孪生（Digital Twin）：现实实体或流程的虚拟表示，按用途所需的频率和精度与现实状态同步，可用于监测、模拟和辅助决策。[Digital Twin Consortium 定义](https://www.digitaltwinconsortium.org/2020/12/digital-twin-consortium-defines-digital-twin/)
1. 神经网络（Neural Network）：由相互连接的计算单元组成，逐层变换输入。训练时，常用反向传播计算训练目标对参数的梯度，再由优化器更新权重和偏置。网络结构通常在训练前确定，所需数据量取决于模型和任务。

    1. 前馈神经网络（Feedforward Neural Network）：数据沿无环连接从输入流向输出。各层可使用非线性激活函数，因此能拟合复杂的输入输出关系。
    2. 循环神经网络（Recurrent Neural Network，RNN）：处理当前输入时沿用前一时刻的隐藏状态，让较早的输入影响后续输出，适合时序或文本等序列数据。
    3. 卷积神经网络（Convolutional Neural Network，CNN）：在不同位置复用同一组卷积核来提取局部模式，常用于图像，也可处理音频和其他序列。
    4. 生成对抗网络（Generative Adversarial Network，GAN）：由生成器和判别器组成。生成器学习产生样本，判别器学习区分训练数据与生成样本，双方的训练目标相互对抗，常用于图像生成。
1. AGI（通用人工智能，Artificial General Intelligence）：指具备广泛学习和跨任务解决问题能力的人工智能。不同定义对任务范围和表现水平的要求不同。「强人工智能」（Strong AI）在哲学语境中还涉及机器是否真正具有心智。[AGI 能力分级研究](https://deepmind.google/research/publications/66938/) · [Strong AI 的哲学语境](https://doi.org/10.1017/S0140525X00005756)
1. AIGC（人工智能生成内容，AI-Generated Content）：由生成式 AI 产生的内容，例如模型生成的摘要、插画或语音。
1. 幻觉（Hallucination）：模型生成了缺乏依据或与事实、给定资料相矛盾的内容，例如引用一篇实际不存在的论文。表达流畅、给出引文都不足以证明答案有据。
1. 微调（Fine-tuning）：在预训练模型基础上，使用特定任务或领域的数据继续训练，更新全部参数，或仅调整适配器等少量参数。
1. 指令微调（Instruction Tuning）：使用包含指令和示范回答的训练样本微调模型，使其更能遵循自然语言指令。单次对话中修改提示词只改变输入。[指令微调原论文](https://arxiv.org/abs/2109.01652)
1. FSD（Full Self-Driving）：特斯拉的驾驶辅助功能品牌名。面向驾驶员的 FSD（Supervised）要求驾驶员持续监督，并随时准备接管车辆。[特斯拉功能说明](https://www.tesla.com/support/fsd)
1. 边缘计算（Edge Computing）：在靠近数据源或用户的设备、网关等位置部署计算与推理，可减少网络往返延迟和传输的数据量。边缘算力指这些设备可提供的计算资源。
1. 具身智能（Embodied AI）：智能体通过身体的传感器和执行机构与环境形成「感知—行动」闭环。例如，机器人根据触觉反馈调整抓握力度。学习可以在部署前完成，也可以在真实或模拟环境中进行。
1. SDD（Spec-Driven Development，规格/规范驱动开发）：用规格说明预期行为、边界和验收条件，再据此设计、实现和验证。规格可以是有具体示例的文档，其中适合自动检查的条件可转成测试。

    相关实现：[Spec Kit](https://github.com/github/spec-kit) 提供 Specify CLI 与规格工作流，[OpenSpec](https://github.com/Fission-AI/OpenSpec) 用提案和规格差异记录变更。

    <details>
    <summary>SDD核心特征与实现原理</summary>

    1. 问题背景：使用 GitHub Copilot、Cursor、Claude Code、Codex 等编程助手时，如果需求主要保存在对话里，容易出现以下问题。

        - 需求分散：同一功能的验收条件分散在多轮对话中，难以评审。
        - 上下文丢失：新会话若没有收到先前的项目决策，就可能重复讨论同一问题。
        - 长上下文利用不均：即使尚未达到窗口上限，模型也可能漏用位于长材料中间的信息。[Lost in the Middle](https://arxiv.org/abs/2307.03172)
        - 约束遗漏：实现可能满足最近的请求，却违反早先约定的接口兼容性。
        - 规格碎片化：若多个文件重复描述同一行为，变更时容易出现冲突。
    1. SDD 的做法：将需要跨会话、跨成员复用的需求和设计决策写入可审阅的规格，并在实施后依照验收条件验证。例如，OpenSpec 的变更可以经历提案、实现和归档。

        1. 版本控制：规格、设计与任务清单可以和代码一起纳入 Git。把有关联的规格、实现与测试放在同一变更中，便于评审者核对它们是否一致。
        1. 模型无关性（Model Agnosticism）：文本规格可供不同模型和团队成员读取。能否运行特定工具链，还取决于宿主支持的命令、文件访问与工具接口。

            > 例如，同一份接口验收条件可交给不同编程助手实现，最后运行同一组契约测试来核对行为。
    1. <details>

        <summary>SDD 与相关开发工作流对比</summary>

        | 维度 | github/spec-kit | Fission-AI/OpenSpec | bmad-code-org/BMAD-METHOD | obra/superpowers |
        | :--- | :--- | :--- | :--- | :--- |
        | 定位 | 规格驱动开发工具包 | 变更提案与规格管理 | 敏捷开发方法与角色工作流 | 面向编程智能体的技能与方法 |
        | 场景举例 | 为新应用或新功能明确需求 | 管理既有系统的增量变更 | 协调产品、架构与开发决策 | 实施功能、系统化排错和审查 |
        | 典型流程 | 规格、计划、任务、实现与验证 | 提案、实现、归档 | 按任务规模选择分析、规划或直接实现 | 澄清设计、拆解计划。开发功能、修复缺陷和重构时默认遵循 TDD，先观察测试失败，再写实现。按需调用调试和审查技能。[TDD 适用范围](https://github.com/obra/superpowers/blob/main/skills/test-driven-development/SKILL.md#when-to-use) |
        | 主要产物 | 功能规格、技术计划与任务清单 | 变更提案、规格差异与任务清单 | 项目简报、架构、用户故事等 | 设计说明、实施计划、测试与审查结果 |

        | 工具 / 项目 | 实现形态 | 前端工程中的用法举例 |
        | :--- | :--- | :--- |
        | [github/spec-kit](https://github.com/github/spec-kit) | Specify CLI 与规格工作流 | 为新模块约定数据结构、接口契约和验收场景。 |
        | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | CLI 与版本化规格文件 | 用变更提案说明历史页面的新旧行为，供团队审阅。 |
        | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | 角色、技能与开发工作流 | 跨团队迁移时，用简报、架构决策和用户故事交接工作。 |
        | [obra/superpowers](https://github.com/obra/superpowers) | 可组合的开发技能 | 为高精度数值计算 Hook 写失败测试，再实现和验证修复。 |
        | [NeekChaw/RIPER-5](https://github.com/NeekChaw/RIPER-5) | 分阶段提示词协议 | 改造状态复杂的 Vue 组件时，按调研、构思、计划、执行、审查推进。 |
        | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | 提供 CLI 和 MCP 接口的任务管理工具 | 将复杂表单拆成有依赖关系的任务，跟踪各任务状态。 |
        | [GSD Core](https://github.com/open-gsd/gsd-core)（原 [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done)） | 分阶段规划、执行和验证的开发工作流 | 按模块安排国际化库迁移，分别验证每一阶段的目标。 |
        </details>
    </details>
1. OpenClaw

    > OpenClaw 是可自托管的 AI 助手系统。Gateway 接入聊天渠道并路由会话，智能体运行时调用配置的模型和工具。[Gateway 架构](https://docs.openclaw.ai/concepts/architecture) · [OpenClaw 笔记](openclaw笔记.md)

    模型（如 Claude、Gemini，或通过 Ollama 运行的本地模型）负责生成响应和工具调用请求。工具执行具体操作，技能以 `SKILL.md` 等文件说明如何完成任务，可通过 ClawHub 分发。[技能文档](https://docs.openclaw.ai/tools/skills) · [ClawHub](https://clawhub.ai/)

    ```mermaid
    flowchart TB
        U[用户] --> MG["Messaging Gateway<br/>(Telegram / Slack / etc)"]
        MG --> AC["智能体运行时<br/>调用语言模型"]
        AC --> T["工具<br/>如 Shell"]
        S["技能说明<br/>SKILL.md"] --> AC
        A["定时任务<br/>Gateway 调度"] --> AC
    ```

    > 浏览器截图可以在 headless 模式中直接生成。若在没有图形会话的 Linux 主机上运行需要显示环境的 headed 浏览器，可用 Xvfb 提供虚拟显示。[Playwright CI 文档](https://playwright.dev/docs/ci#running-headed)
    >
    >```mermaid
    >flowchart TB
    >   A["Playwright<br/>控制浏览器(真实内核)"] --> B{"浏览器运行模式<br/>是否需要界面display server"}
    >   B --> |headless|C["无需显示服务器，可直接截图"]
    >   B --> |headed|D{"需要display server"}
    >   D --> |已有图形会话|E["使用现有显示环境"]
    >   D --> |Linux 无图形会话|F["可用 Xvfb 提供虚拟显示"]
    >```
