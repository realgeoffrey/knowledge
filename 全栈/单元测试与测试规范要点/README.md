# 单元测试与测试规范要点

社区共识速查（Kent Beck / Feathers / Fowler / Google SWE & TotT / Khorikov / Spotify / P3C / xUnit Patterns / Kent C. Dodds 等）。数字为经验阈值，非硬指标。

---

## 关键词解释

### 原则与缩写

| 关键词 | 解释 |
|---|---|
| **Unit Test（单元测试）** | 在隔离条件下验证一小段逻辑（通常方法/类）的自动化测试。不碰真实 DB、网络、文件系统等（见 Feathers 规则）。古典派也可把「单元」理解为一段可观察行为，而非必须 Mock 到每个类。 |
| **FIRST** | 好单测五特征（Clean Code 等）：**F**ast 够快才愿常跑；**I**solated / Independent 用例互不依赖；**R**epeatable 任意环境结果一致；**S**elf-validating 用断言自动判对错；**T**imely 及时编写（贴近实现/TDD）。 |
| **AIR** | 阿里 P3C：**A**utomatic 全自动（禁 `System.out` 人肉验）；**I**ndependent 独立（禁用例互调、禁依赖顺序）；**R**epeatable 可重复（不依赖外部环境）。与 FIRST 高度重叠。 |
| **四支柱**（Khorikov） | 衡量测试价值：①**防回归**（少漏检）②**抗重构**（少误红）③**反馈快**④**可维护**。①②最关键且互相牵制；绑死实现细节会牺牲②。 |
| **测行为不测实现** | 断言对外可观察结果（返回值/状态/异常/对外副作用），不断言私有步骤、无关内部调用顺序。实现变、行为不变 → 测试应仍绿。 |
| **Clear / Complete / Concise / Resilient** | Google SWE / TotT 综合：清晰；信息自洽完整；无噪音；行为不变则测试不必改（韧性 / unchanging）。TotT 另有 **Fidelity / Resilience / Precision**（能抓缺陷、非缺陷不红、失败能定位）。 |
| **DAMP 与 DRY（测试里）** | Google / TotT：测试里权衡时偏 **D**escriptive **A**nd **M**eaningful **P**hrases（可读优先，可适当重复）；helper 仍可 DRY 藏噪音，但关键输入勿藏没。生产代码仍重 DRY。 |
| **Hermetic（密封）** | Google：测试自包含、不依赖共享可变环境/执行顺序；越大越难密封，但仍应尽量逼近。 |

### 策略与形态

| 关键词 | 解释 |
|---|---|
| **测试金字塔** | Mike Cohn / Fowler：底层大量快单测 → 中层适量集成 → 顶层极少 E2E。越高越慢越脆，故数量越少。 |
| **冰淇淋甜筒** | 反模式：E2E/UI 过多、单测过少 → 慢、脆、难维护。 |
| **沙漏** | 反模式：两端（单测+E2E）多、中间集成空 → 协作问题漏测。 |
| **Testing Trophy** | Kent C. Dodds（偏前端/JS）：Static → Unit → **Integration（最厚）** → 少量 E2E。强调「置信度 ROI」，与金字塔不对立，语境不同。 |
| **Testing Honeycomb** | Spotify 微服务：以服务边界 **Integration**（起本服务、显式交互点）为主；复杂内部逻辑才写 **Implementation Detail**；**Integrated**（依赖他服务对错）尽量少/理想为零。注意 Integration ≠ Integrated。 |
| **Feathers 规则** | 「不算单测」若：访问 DB、走网络、碰文件系统、不能与其他单测并行、要改环境配置才能跑。这类测试有价值，但须与真单测**分套件**，保证单测始终快。 |
| **Google 测试尺寸** | **Small**：单进程、禁阻塞 IO；**Medium**：可多进程/localhost 资源；**Large**：可跨机/外部系统。尺寸与「范围（unit/integration/e2e）」相关但不等同，可用规则强制约束。 |
| **E2E** | End-to-End：模拟真实用户路径，穿过多层系统。贵、慢、易 flaky，只保关键路径。 |
| **集成测试** | 验证多个组件协作或与真实依赖边界的正确性；比单测慢，比 E2E 窄。词义因团队而异，写清「测到哪一层」比纠结标签更重要。 |
| **契约测试（Contract / CDC）** | 验证接口约定（请求/响应形状、字段语义）。消费者驱动契约（如 Pact）可在不搭全链路环境时防服务间破坏性变更。 |

### 写法与结构

| 关键词 | 解释 |
|---|---|
| **SUT** | System Under Test。单测里应对 SUT 用**真实实例**，对其依赖用替身。 |
| **AAA** | Arrange–Act–Assert：准备 → **一次** Act（一次有意义的触发）→ 断言。又称 Given–When–Then。同一场景可多条断言；忌一测多无关场景。 |
| **一测一场景** | 一条用例只验证一条业务规则/一个场景；失败时立刻知道坏了什么。 |
| **Happy Path** | 合法输入下的主成功路径；不能只测它，还须边界与错误路径。 |
| **副作用（Side Effect）** | 除返回值外的可观察影响：写库、发消息、改状态、调外部 API 等。 |
| **魔法值** | 测试里无语义的字面量；应提成有含义的常量/变量（与场景相关的值应出现在测试正文，勿藏进 helper）。 |
| **Fixture / Builder / Mother Object** | 测试数据构造：固定夹具、建造者、Object Mother。减少噪音；关键输入仍应在用例内可见。 |
| **beforeEach / beforeAll** | 每条前 / 整套一次前初始化。共享可变状态时 `beforeAll` 易导致顺序依赖，单测更常用 `beforeEach`。 |
| **表驱动 / 参数化** | 同一逻辑多组输入输出（JUnit `@ParameterizedTest`、表格用例）；减重复、扩边界，但勿把无关场景硬塞一张表。 |
| **状态验证 vs 交互验证** | 状态：断言结果/可观察状态（更抗重构）；交互：`verify` 调用（仅当「发出该调用」本身是契约）。 |
| **Sociable vs Solitary** | 社交式：进程内真实协作、只替进程外依赖；孤独式：协作者全 Mock。对应古典派 / 伦敦派倾向。 |

### 测试替身（Test Double）

| 关键词 | 解释 |
|---|---|
| **Test Double** | 测试中替代真实依赖的统称（xUnit Patterns / Meszaros）。 |
| **Dummy** | 仅占位、基本不会被用到的参数（如 `null`、空对象）；不提供行为。 |
| **Stub** | 按预设返回值/抛错，**提供间接输入**；一般不在测试里验证是否被调用。 |
| **Spy** | 记录对依赖的调用（间接输出），供 Act **之后**断言；本质是「可查询的 Stub」。≠「必须包装真实对象」（那是 partial mock，另当别论）。 |
| **Mock** | 预设行为 + **预先设定期望交互**（是否调用、参数、次数）；过度 verify 易绑实现、牺牲抗重构。 |
| **Fake** | 可用的简化实现（如内存 Repository），行为接近真实但无外部 IO。常比一堆 Mock 更稳。 |
| **古典派（Detroit/Classical）** | 隔离的是「测试之间」；单元偏**行为**；通常只替**进程外**依赖，进程内协作尽量真实（Sociable）。 |
| **伦敦派（London/Mockist）** | 隔离到**类**；协作者大量 Mock（Solitary）；粒度细，但易过度指定实现、测试更脆。 |

### 测点框架

| 关键词 | 解释 |
|---|---|
| **BCDE** | P3C：**B**order 边界（循环边界、特殊值、时间点、顺序等）；**C**orrect 正确输入；**D**esign 结合设计/契约；**E**rror 非法与异常路径。 |
| **RIGHT-BICEP** | Pragmatic Unit Testing：结果是否 Right；边界；反向关系；交叉检查；错误条件；性能特征等。 |
| **CORRECT** | 边界口诀：Conformance 格式、Ordering 顺序、Range 范围、Reference 引用、Existence 有无、Cardinality 多少、Time 时间。 |
| **等价类 / 边界值** | 经典黑盒：每类代表值 + 边界内侧外侧；与 CORRECT / Border 互补。 |

### 可测性与特殊手法

| 关键词 | 解释 |
|---|---|
| **依赖注入（DI）** | 把 DB/时钟/随机/客户端等从构造/参数注入，单测才能替换替身；P3C 也强调可注入。 |
| **Humble Object** | 难测的 UI/框架边界变薄，逻辑抽到可单测的纯模块。 |
| **特性化测试（Characterization）** | 锁定遗留行为「现在是什么样」（Golden Master / Approval），再安全重构；断言的是现状，不是理想设计。 |
| **属性测试（Property-based）** | 用生成数据验证不变量（如「序列化再反序列化等价」）；补全手工用例盲区，不替代例证测试。 |
| **快照测试** | 固化大块输出再 diff；适合 UI/结构化文档，易变内容慎用，防「盲点批准」刷绿。 |

### 质量与流程

| 关键词 | 解释 |
|---|---|
| **覆盖率** | 行/语句/分支等被执行比例。是**结果指标**非目标；高覆盖 + 弱断言仍可能测了个寂寞。P3C 推荐：语句约 **70%**；核心模块语句与分支都要达到 **100%**（推荐项）。分支/条件通常比纯行覆盖更能暴露漏测。 |
| **变异测试（Mutation）** | 故意改生产代码（变异体），看测试是否失败。存活变异体 → 断言可能没真正抓住缺陷。 |
| **Flaky** | 同一代码反复跑时过时不过。多因时间、并发、顺序、外部依赖。摧毁 CI 信任，必须治理（隔离根因 / 重试仅作权宜 / **隔离检疫 quarantine** 防污染主线）。 |
| **TDD** | 先写失败测试再写实现：**Red → Green → Refactor**。Inside-out（由内而外）或 Outside-in（由外而内 + 验收/ATDD）皆可。 |
| **TDD 三定律**（Uncle Bob） | ①无失败测不写生产代码；②测只写到刚好失败；③代码只写到刚好让测通过。 |
| **弱断言** | 几乎不证明行为（仅非 null、仅未抛异常、过宽 `Exception`）；对回归保护弱。 |
| **窄断言 vs 宽断言** | TotT：优先只断言与本场景相关的字段/行为；整对象全等易脆。全等适合少量「契约形状」用例。 |
| **伪单测** | 挂着单测名字，实际依赖容器/真实中间件，慢且不稳。 |
| **抗重构** | 行为不变、结构变后测试仍通过；若常误红，说明测了实现细节。 |
| **测试含逻辑** | Google：测试体避免 if/循环/复杂计算期望；期望应是明显字面/常量，否则测试自己也可能错。 |

---

## 1. 好测试的标准

| 维度 | 要点 |
|---|---|
| FIRST / AIR | 快、独立、可重复、自动判定、及时写 |
| 四支柱 | 防回归 + 抗重构（最关键），兼反馈快、可维护 |
| 可读韧性 | 清晰、完整、简洁；DAMP；行为不变则测试不改 |
| 价值 | 保护行为、支撑重构、可执行文档；**不为刷覆盖率** |

**一句话：** 快、稳、独立、自动判定；测可观察行为，不绑实现细节。

---

## 2. 测试策略

```text
        E2E / UI     ← 极少
      集成 / 服务     ← 适量
    单元 / 窄范围     ← 大量   （金字塔）
```

| 语境 | 经验配比 / 形态 |
|---|---|
| Google（后端通用） | 约 **80%** 窄范围 + **20%** 更广；常细分为约 80% / 15% / 5%（**窄范围 unit / 中范围 integration / e2e**）。与 Small/Medium/Large **尺寸**相关但不等同（见上） |
| 微服务（Spotify） | Honeycomb：重本服务 Integration，少 Implementation Detail，尽量避免 Integrated |
| 前端/组件树（Dodds） | Trophy：静态检查 + 偏厚的 Integration（真实协作、少 Mock）+ 少量 E2E |
| 套件划分 | 触达 DB/网络/文件/需改配置 → 与真单测**分套件**（Feathers）；CI 先跑快套件 |

忌冰淇淋甜筒、沙漏；标签服从目的：慢脆的少写，快稳的多写。

---

## 3. 单元测试怎么写

### 边界

| 做 | 不做 |
|---|---|
| 测局部行为；真实 SUT + 替身依赖 | 当联调；真实 DB/MQ/HTTP/墙钟/随机源 |
| 测试与生产目录分离（如 `src/test/java`） | 起重量级容器只验局部 if/else |
| 注入 Clock / Random / 时间 | 测里 `sleep`、读系统时钟碰运气 |

### 结构

- **AAA**：准备 → **一次** Act → 断言；一测一场景
- 命名可读：`XxxTest`、`method_should_expected_when_state` 或行为句；禁 `test1`
- 断言优先级：返回值 → 状态 → 异常 → 对外副作用（交互 verify 最后且克制）
- 禁：弱断言、用逻辑**计算**期望值、过宽 `Exception`、测私有方法（应测通过公有行为；难测先改设计）

### 替身

| 通常替身 | 通常不 Mock |
|---|---|
| Repository、RPC、缓存、MQ、Clock、IO、随机源 | DTO、枚举、值对象、纯函数、SUT 自身 |

能 Fake 优于堆 Mock；`verify` 仅当交互本身是契约；倾向古典派「测结果」，避免伦敦派过度 Mock。

### 测点顺序

主路径 → 边界（CORRECT / 等价类）→ 非法/异常 → 依赖失败 → 副作用（BCDE / RIGHT-BICEP 作检查表）。

### 数据与设计

最小化；禁魔法值；Builder/Fixture 藏噪音、露关键；慎全局 Setup；难测先改设计（DI、拆 Humble Object）再堆 Mock。

### P3C 补充（Java 团队常用）

- 用例间禁止互相调用、禁止依赖执行顺序
- 粒度至多到类、一般为方法；手册把「跨类/跨系统协作」划给集成测——这是 **P3C 的粒度/套件命名**。古典派可将「单元」视为可观察行为，**进程内**多类真实协作仍可放快套件（Sociable）；**跨进程 / 真实外部依赖**再按 Feathers 分套件。两套标准勿混用标签硬套。
- 核心增量代码应及时补测并通过
- 为可测避免：构造器过重、过多全局/静态、过多外部依赖、过深嵌套条件（宜卫语句/策略等）

---

## 4. 覆盖率、Flaky、流程

| 主题 | 共识 |
|---|---|
| 覆盖率 | 结果非目标；P3C 语句约 70%，核心看分支；勿为数字写空测 |
| 变异测试 | 检验断言是否真能抓缺陷；适合核心域补强 |
| Flaky | 必须治理；查时间/线程/顺序/共享状态/外部依赖；检疫区隔离，修根因优于盲目重试 |
| TDD | Red → Green → Refactor（可选但经典） |
| 补测步骤 | 契约/行为 → 测点清单 → AAA → 自检隔离、可读、有无逻辑/弱断言 |
| 遗留代码 | 先特性化/关键路径锁定，再重构；不必一次性追求高覆盖 |

---

## 5. 红旗（危险信号）

单测碰真实外部世界；容器测局部逻辑；一测多场景；测私有/过度 verify；测试含业务逻辑或计算期望；弱断言刷覆盖；宽断言导致重构必红；E2E 过多；共享可变 Fixture 导致顺序依赖；Flaky 靠重试「养着」；重构就大面积红。

---

## 6. 速记

> **FIRST/AIR + 测行为不测实现；金字塔底部要厚，Trophy/Honeycomb 则腰部（Integration）要厚；一测一规则用 AAA；隔离外部世界；测试偏 DAMP 可读；覆盖率服务于质量，不为数字而测。**

---

## 7. 主要出处（便于深挖）

| 主题 | 来源 |
|---|---|
| FIRST / TDD 定律 | Clean Code；Uncle Bob |
| Feathers 规则 | *Working Effectively with Legacy Code* |
| 金字塔 | Cohn；Fowler bliki |
| 四支柱 / 古典vs伦敦 | Khorikov *Unit Testing Principles* |
| Test Double 术语 | Meszaros *xUnit Test Patterns* |
| AIR / BCDE / 覆盖率建议 | 阿里巴巴 Java 开发手册（P3C） |
| 80/20、尺寸、清晰测试 | *Software Engineering at Google*；Testing Blog / TotT |
| Honeycomb | Spotify Engineering《Testing of Microservices》 |
| Trophy | Kent C. Dodds |
| RIGHT-BICEP / CORRECT | *Pragmatic Unit Testing* |
