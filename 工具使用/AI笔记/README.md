# AI笔记

## 目录
1. [【一站式 LLM底层技术原理入门指南】](#一站式-llm底层技术原理入门指南)
1. [词汇表](#词汇表)

---
### [【一站式 LLM底层技术原理入门指南】](https://s3tlxskbq3.feishu.cn/docx/NyPqdCKraoXz9gxNVCfcIFdnnAc)
1. 人工智能（Artificial Intelligence，AI）：让机器模拟生物智能，具备感知、学习、识别、推理等能力的计算机科学技术。作为计算机科学分支，涵盖计算机视觉（Computer Vision, CV）、自然语言处理（Natural Language Processing, NLP）、语音识别（Voice Recognition）、语音生成（Text to Speech, TTS）、知识图谱（Knowledge Graph）等领域。

    1. 机器学习（Machine Learning,ML)是实现人工智能的核心方法，是从有限的观测数据中“学习”（or“猜测”）出一个具有一般性的规律，并利用这些规律对未知数据进行预测的方法。

        1. 有监督学习（Supervised Learning）：使用带标签的训练数据训练模型，学习输入与输出的映射关系，用于预测未标签数据。训练集需包含输入（特征）和人工标注的输出（目标）。
        1. 无监督学习（Unsupervised Learning）：从未标记数据中自动发现结构、模式、关联或表示，无需人工标签或先验知识。

            1. 自监督学习（Self-supervised Learning）：通过辅助任务（Pretext）从大规模无监督数据中挖掘监督信息，训练网络学习对下游任务有价值的表征。
        1. 强化学习（Reinforcement Learning）：智能体（Agent）与环境（Environment）交互，学习决策策略以最大化累积奖励的机器学习方法。
        1. 特征（Feature）：从原始数据中提取的、用于表示样本的属性或信息。

            > 特征即基于原始信息，具体输入给机器的数据。
        1. 深度学习（Deep Learning）：使用深层、复杂结构的神经网络进行学习的方法。通过多层学习抽象和高级特征表示，更好地捕捉数据的内在结构和特性。

            1. 端到端学习（End-to-End Learning）：也称端到端训练，不进行分模块或分阶段训练，直接优化任务的总体目标。

                > 将复杂任务视为整体黑箱，仅关注输入输出对，基于输出结果调整模型。

### 词汇表
1. 模型（Model）：表示数据输入与输出之间映射关系的数学函数或算法结构。
1. Agent（智能体、代理）：能够感知环境、做出决策并执行行动的自主实体。多智能体框架（Multi-Agent Framework）支持多个智能体协同工作的开发平台。
1. 参数（Parameters）：模型内部可学习的权重，决定模型行为。显存大小（VRAM）影响可训练模型规模。模型蒸馏（Distillation）是将大模型知识压缩到小模型的技术。
1. 半监督学习（Semi-supervised Learning）：结合少量标注数据和大量未标注数据进行训练的学习范式。标注（Annotation）是为数据添加标签的过程。
1. Prompt（提示词）：向大型语言模型提供的精心制作的输入，用于引导生成期望的输出。
1. 上下文长度（Context Length）：LLM在生成输出时考虑的输入单词/token的最大数量。
1. 上下文窗口（Context Window）：模型处理完整交互过程的能力范围，包括多轮对话历史和当前响应。
1. Token：文本的最小处理单元，可能是单词、子词或字符，取决于分词策略。
1. SOP（Standard Operating Procedure，标准操作程序）：通过标准化流程将复杂任务分解为可重复执行的具体步骤，实现效率提升、质量控制和经验传承。核心在于细节量化与流程固化，适用于企业生产、个人管理和技术系统设计。
1. 工具与框架：ollama（本地LLM运行工具）、label-studio（数据标注平台）、cherry-studio（AI应用开发工具）、dify（LLM应用开发平台）、langchain（LLM应用开发框架）。
1. MCP（Model Context Protocol，模型上下文协议）：基于标准输入输出（STDIO）和JSON-RPC格式的通信协议，让不同进程像调用本地函数一样调用AI工具或服务。

    > MCP是进程通信规范，让AI模型、浏览器、终端、数据库等独立软件像乐高一样拼接，互相调用功能。

    核心优势：

    1. 轻量级：直接将本地进程注册为工具，无需REST API或SDK
    2. 本地通信：通过STDIO而非网络，延迟极低
    3. 隐私安全：数据不经过外部网络，所有调用在本地完成

    | 特性 | REST API/Playwright | MCP Server |
    | :--- | :--- | :--- |
    | 调用方式 | 远程网络请求 | 本地进程通信 |
    | 延迟 | 较高（网络开销） | 极低 |
    | 隐私安全 | 可能上传云端 | 完全本地 |
    | 集成复杂度 | 需要额外依赖 | 即插即用 |
1. A2A（Agent2Agent Protocol）：智能体间通信协议。
1. ANP（Agent Network Protocol）：智能体网络协议。
1. 知识库（Knowledge Base，KB）：包含文档集合的系统，用于存储和检索结构化信息。
1. RAG（Retrieval-Augmented Generation，检索增强生成）：结合信息检索和生成的技术，从知识库检索相关信息后生成回答，提升准确性和可追溯性。
1. Embedding（嵌入）：将数据转换为数值向量的技术，用于表示语义信息。
1. 嵌入模型（Embedding Model）：将文本、图像、图表、视频等数据转换为数值向量的模型，捕捉其在多维向量空间中的含义和细微差别。选择需兼顾语义深度、计算效率、数据类型和维度等因素。
1. 向量数据库（Vector Database）：组织有序的向量嵌入集合，支持创建、读取、更新和删除操作。向量嵌入将数据块（如文本或图像）表示为数值，便于相似度检索。
1. 对话式AI（Conversational AI）：能够进行自然对话交互的人工智能系统。
1. 自然语言处理（Natural Language Processing，NLP）：利用计算机和软件理解人类语言（书面或口语）含义的技术。
1. 自动语音识别（Automatic Speech Recognition，ASR）：收录人类语音并转换为可读文本的技术，也称语音转文本。支持免手动编辑文本消息，为机器理解提供框架。
1. 自然语言理解（Natural Language Understanding，NLU）：理解文本上下文和意图，生成智能回复的技术。
1. 文本转语音（Text to Speech，TTS）：将文本转换为语音输出的技术。
1. BERT（Bidirectional Encoder Representations from Transformers）：Google开发的自然语言处理模型，学习文本双向表示，显著提升理解无标记文本的能力。
1. 计算机视觉（Computer Vision，CV）：让计算机理解和分析视觉信息的技术。
1. Transformer架构：基于自注意力机制（Self-Attention）的深度学习模型架构，由Google团队在2017年论文《Attention Is All You Need》中提出。包含编码器（Encoder）和解码器（Decoder）结构，彻底改变NLP领域，成为现代大语言模型（如GPT、BERT）的核心基础。
1. 预训练模型（Pre-trained Model）：在大规模数据上预先训练的模型，可通过微调适应特定任务。
1. Hugging Face：提供预训练模型、数据集和工具的开源平台，简化NLP和AI模型的使用。
1. 推理模型（Inference Model）：用于实际预测和生成的已训练模型，区别于训练阶段的模型。
1. 大语言模型（Large Language Model，LLM）：使用超大数据集训练的深度学习算法，能够识别、总结、翻译、预测和生成内容。主要基于Transformer架构，通过追踪序列数据中的关系学习上下文和含义。采用无监督学习训练，无需大量人工标注，是构建AI模型的重大突破。

    代表模型：Claude、GPT、BERT、Gemini、Llama、Grok、DeepSeek、文心一言、通义千问、讯飞星火、Moonshot（Kimi）。
1. 记忆模组（Memory Module）：AI智能体维护上下文的机制，包括短期记忆（工作记忆）和长期记忆（持久化存储）。
1. 推理层（Reasoning Layer）：AI系统进行逻辑推理和决策的组件。
1. AI智能体框架（AI Agent Frameworks）：简化AI智能体构建、部署和管理的开发平台或库，消除底层复杂性，让开发者专注于应用和智能体行为。
1. AI助手（AI Assistants）：协助用户完成任务的智能应用系统。
1. PyTorch：Facebook开发的开源深度学习框架，提供动态计算图和丰富的工具生态。
1. 生成式AI（Generative AI）：根据输入快速生成新内容的AI技术。输入输出可包括文本、图像、声音、动画、3D模型等。使用神经网络识别数据模式和结构，生成原创内容。
1. 视觉语言模型（Vision-Language Models，VLM）：多模态生成式AI模型，能够理解和处理视频、图像和文本。
1. 数字孪生（Digital Twin）：产品、流程和设施的虚拟表示，企业用于设计、模拟和操作实体对应物。
1. 神经网络（neural network）：是一种受人脑启发的机器学习算法。这款强大的工具擅长解决传统计算机算法难以处理的复杂问题，例如图像识别和自然语言处理。神经网络由相互连接的节点（称为神经元）组成，它将这些单元分层排列。每个神经元接收来自其他神经元的输入、对其进行处理，并将输出传输给其他神经元。神经元之间的连接具有相关的权重，表示连接强度。在训练期间，神经网络会调整这些权重以改善其在给定任务上的表现。这种学习过程使得神经网络能够做出预测并识别模式，从而推动它们在图像识别、自然语言处理和机器翻译等各种领域的广泛应用。神经网络的学习是通过在训练过程中建立神经元之间的连接并调整连接权重来实现的。在该过程中，需要向神经网络提供海量数据集，之后神经网络会使用这些数据集来优化其权重，以最大限度地减少预测值与实际值之间的误差。这一过程与人类的学习过程类似，反复接触有助于识别模式。

    1. 前馈神经网络（Feedforward）：这是一种基本的神经网络，它以线性方式处理数据，即从输入到输出且没有循环。这类神经网络通常用于分类和回归等简单任务。
    2. 循环神经网络 (Recurrent，RNN)：RNN 专为时序或自然语言等序列数据而设计，它使用反馈环来保留先前输入的记忆，因此适合用于具有时间成分的数据。
    3. 卷积神经网络 (Convolutional，CNN)：CNN 专为图像相关任务而设计，使用卷积层从图像中提取特征，从而识别边缘和形状等模式。
    4. 生成对抗网络 (Generative Adversarial，GAN)：GAN 由生成器和判别器组成，并让这两个组件相互对抗。生成器负责创建数据，而判别器则评估其所创建数据的真实性。这种对抗过程使得生成器能够产生越来越真实的数据，通常用于生成图片、视频和音频。
1. AGI（通用人工智能，artificial general intelligence）、强人工智能（strong AI）：是具备与人类同等智能、或超越人类的人工智能，能表现正常人类所具有的所有智能行为
1. AIGC（人工智能生成内容，Artificial Intelligence Generated Content）
1. 幻觉（hallucination）
1. 微调（fine-tuning）：通过在特定任务或领域上进一步训练，使LLM适应特定任务或领域
1. 指令调优（instruction tuning）：通过提供具体的指导或指令来 fine-tuning LLM的行为
1. FSD（Full-Self Driving，完全自动驾驶）：是特斯拉研发的自动驾驶系统
1. ​边缘算力、边缘算力
1. ​具身智能（Embodied Artificial Intelligence, EAI）：是一种通过物理实体（如机器人、自动驾驶车辆等）与环境交互，实现感知、决策和行动的智能系统。其核心在于“具身性”，即智能体通过身体感知物理世界，并在交互中动态学习与适应，形成“感知—行动”闭环
1. SDD（Specification-Driven Development，规格/规范驱动开发）：通过可执行、可验收的规格，驱动人和 AI 协作交付的软件开发方式，是 Agent 化研发落地的核心基础设施。

    相关实现：<https://github.com/github/spec-kit>（重量级、针对从零开始的项目（Greenfield-first））、<https://github.com/Fission-AI/OpenSpec>（轻量级、**针对已成熟的项目（Brownfield-first）**）

    <details>
    <summary>SDD核心特征与实现原理</summary>

    1. 问题背景：现有 AI 编程助手（GitHub Copilot、Cursor、Claude Code 等）采用"基于对话的开发"（Chat-Driven Development, CDD）模式，存在以下局限：

        - "Vibe Coding"问题：需求分散在对话记录中，缺乏结构化文档，导致 AI 交互不可预测
        - 上下文丢失：项目需求、设计决策和架构约束仅存在于瞬时对话历史或开发者记忆中
        - 注意力分散：随着对话轮次增加，LLM 上下文窗口面临物理限制和注意力分散（Attention Dispersion）
        - 约束遗忘：模型易遗忘初始约束条件，产生"幻觉代码"或偏离预期的实现
        - 规格碎片化：传统方法将规格分散在多个文件中，难以整体把握系统意图，特征交互难以检测
    1. SDD 解决方案：将 状态（State） 从易失的内存（LLM 上下文）迁移至持久化的文件系统（Filesystem），构建轻量级、持久化、版本可控的"规范层"（Spec Layer），通过结构化工件（Artifacts）强制执行"先对齐，后构建"（Agree-Build-Archive）的工程流程。核心特征：

        1. 原子性与版本控制：需求变更（Proposal）、技术规格（Specs）、设计文档（Design）和任务清单（Tasks）以 Markdown 或 YAML 文件形式存储在代码仓库中。Git 每次提交不仅包含代码变更，还包含导致该变更的"思维链条"，实现代码与文档的原子性同步。
        1. 模型无关性（Model Agnosticism）：通过纯文本作为交互介质，解耦底层推理引擎。任何能读取文件系统并理解 Markdown 语法的模型（GPT-4、Claude 3.5 Sonnet、Llama 3 等）均可接入该系统。

            >模型无关性（Model Agnosticism）：通过 **统一的“模型调用抽象层” + 协议化的输入输出（通常基于 JSON/DSL） + 工具级插件式适配器**，将 “业务逻辑/工具能力” 与 “具体模型 API” 解耦，从而实现模型可插拔。
    1. spec-kit 与 OpenSpec 对比

        | 维度 | GitHub spec-kit | Fission-AI OpenSpec |
        | :--- | :--- | :--- |
        | 体量 | 重量级 | 轻量级 |
        | 场景 | 绿地（Greenfield）：从零立项 | 棕地（Brownfield）：存量改造 |
        | 流程 | 宏观瀑布：先完整规划再实施 | 微型瀑布/迭代：小步规格、小步实现 |
        | 隐喻 | 建筑师：蓝图驱动 | 外科医生：在现状上精准修改 |
        | 真理来源 | 文档为真，代码为副产品 | 代码库为真，Spec 为变更指令 |
        | 旧代码 | 要求合规新规范 | 理解并缝合进现有代码 |
    </details>
