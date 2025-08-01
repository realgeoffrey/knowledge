# AI笔记

## 目录
1. [词汇表](#词汇表)

---
### 词汇表
1. 模型（Model）、Agent（智能体、代理）与多智能体框架（Multi-Agent Framework）
1. 参数、显存大小、蒸馏
1. 无监督学习、有监督学习、半监督学习、标注
1. prompt：向大型语言模型提供精心制作的输入，以生成期望的输出
1. 上下文长度（context-length）：LLM在生成输出时考虑的输入单词/token的最大数量
1. 上下文窗口（context window）：强调模型对完整交互过程的处理能力，包括多轮对话的历史记录和当前生成的响应
1. token
1. SOP（Standard Operating Procedure）是通过标准化流程将复杂任务分解为可重复执行的具体步骤，以实现效率提升、质量控制和经验传承的核心工具。其核心在于细节量化与流程固化，适用于企业生产、个人管理乃至技术系统设计等领域
1. ollama、label-studio、cherry-studio、dify、langchain
1. MCP（Model Context Protocol）模型上下文协议
1. A2A（the Agent2Agent Protocol）
1. ANP（Agent Network Protocol）
1. 知识库（knowledge base，KB）：一个包含文档集合的系统，用于存储和检索信息
1. RAG（Retrieval-Augmented Generation，检索增强生成）
1. embedding（嵌入）
1. 嵌入模型（embedding model）：会将各种数据 (例如文本、图像、图表和视频) 转换为数值向量，以便捕捉其在多维向量空间中的含义和细微差别。嵌入技术的选择取决于应用需求，同时要兼顾语义深度、计算效率、要编码的数据的类型、维度等因素
1. 向量数据库（Vector Database）：是一种组织有序的向量嵌入集合，整合了可以随时创建、读取、更新和删除的向量嵌入。向量嵌入将数据块 (例如文本或图像) 表示为数值
1. 对话式AI
1. 自然语言处理（Natural Language Processing，NLP）：是一项利用计算机和软件获取人类语言（书面或口语）含义的技术
1. 自动语音识别（Automatic Speech Recognition，ASR）：会收录人类语音，然后将其转换为可读文本
1. 自然语言理解（Natural Language Understanding，NLU）：会录入文本，理解上下文和意图，然后生成智能回复
1. 文本转语音（Text To Speech，TTS）
1. 自动语音识别（Automatic Speech Recognition, ASR）或语音转文本：是流程和软件的组合,能够解码人类语音并将其转换为数字化文本。会收录人类语音，然后将其转换为可读文本。ASR 能够帮助我们免手动操作地编辑文本消息，并提供用于机器理解的框架
1. BERT：是由Google开发的自然语言处理模型，可学习文本的双向表示，显著提升在情境中理解许多不同任务中的无标记文本的能力
1. 计算机视觉（Computer Vision，CV）
1. Transformer架构（encoder-decoder、self-attention）

    是一种基于自注意力机制（Self-Attention）​的深度学习模型架构，由 Google 团队在 2017 年的论文《Attention Is All You Need》中首次提出。它彻底改变了自然语言处理（NLP）领域，并成为现代大语言模型（如 GPT、BERT）的核心基础。
1. 预训练模型
1. huggingface
1. 推理模型
1. 大语言模型（large language model，LLM）

    是一种深度学习算法，可以使用非常大的数据集来识别、总结、翻译、预测和生成内容。大语言模型在很大程度上代表了一类名为转换器网络（transformer networks）的深度学习架构。转换器模型是一种神经网络，通过追踪序列数据 (如本句中的单词) 中的关系学习上下文及其含义。

    大语言模型采用无监督式学习进行训练。通过无监督式学习，模型可以使用无标签数据集在数据中找到先前未知的模式。这样也无需再对大量数据进行标记，这项工作是构建AI模型的巨大挑战之一。

    代表：Claude、GPT、BERT、Gemini、Llama、Grok、DeepSeek、文心一言、通义千问、讯飞星火、Moonshot（Kimi）。
1. 记忆模组：AI智能体（Ai agents）依靠记忆来维护上下文：短期记忆、长期记忆
1. 推理层
1. AI智能体框架（AI Agent Frameworks）

    AI智能体框架为专用开发平台或库，旨在简化AI智能体的构建、部署和管理流程。这些框架消除了构建智能体系统的过程中存在的大部分底层复杂问题，使开发者能够专注于特定的应用和智能体行为，而非实施的技术细节。
1. AI助手（ai assistants）
1. 机器学习（machine learning，ML）：采用算法和统计模型，使计算机系统能够在大量数据中找到规律，然后使用可识别这些模式的模型来预测或描述新数据。
1. 深度学习（deep leaning，DL）：是人工智能 (AI) 和机器学习 (ML) 的一个分支，其使用多层人工神经网络精准完成物体检测、语音识别、语言翻译等任务。
1. 强化学习（Reinforcement learning，RL）：一种机器学习技术，使机器人能够通过从经验中学习来做出智能决策。通过获得程序化的奖励或惩罚，驱动机器人的AI模型在试错的过程中不断改进
1. PyTorch：一种开源深度学习框架
1. 生成式AI（Generative AI）：使用户能够根据各种输入快速生成新内容。这些模型的输入和输出可以包括文本、图像、声音、动画、3D 模型或其他类型的数据。使用神经网络来识别现有数据中的模式和结构，以生成新的原创内容
1. 视觉语言模型（Vision-Language Models，VLM）：是一种多模态、生成式AI模型，能够理解和处理视频、图像和文本
1. 数字孪生（Digital Twin）：是产品、流程和设施的虚拟表示，企业用它来设计、模拟和操作其实体对应物
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
