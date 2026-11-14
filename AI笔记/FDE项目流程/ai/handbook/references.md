# 示例、术语与参考

> AI维护，仅查术语、示例或来源时读取。术语核查日期：2026-11-05；工具和框架按项目固定版本核对。

## 官方资料

| 来源 | 用途 |
| --- | --- |
| [Palantir：FDE](https://jobs.lever.co/palantir/2e6b0ac8-83e9-4be5-a3aa-cf319f751728) | 岗位英文与端到端落地含义 |
| [IREB 术语表](https://cpre.ireb.org/en/downloads-and-resources/glossary) / [ISTQB 验收测试](https://istqb.org/certifications/certified-tester-acceptance-testing/) | AC、BL、CR、UAT 概念 |
| [OpenAI：AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md) / [DeepSeek：Tool Calls](https://api-docs.deepseek.com/guides/tool_calls/) / [gitignore](https://git-scm.com/docs/gitignore) / [ripgrep：.ignore](https://github.com/BurntSushi/ripgrep/blob/master/GUIDE.md#automatic-filtering) | 按客户端核对加载与工具执行。检索排除用 `.ignore`，版本库排除用 `.gitignore`；两者都不等于访问隔离 |
| [RuoYi-Vue-Pro](https://github.com/YunaiV/ruoyi-vue-pro) / [项目结构](https://doc.iocoder.cn/project-intro/) | 固定分支/提交，遵循相邻代码，不混用其他若依项目 |
| [代码生成](https://doc.iocoder.cn/new-feature/) / [数据权限](https://doc.iocoder.cn/data-permission/) / [多租户](https://doc.iocoder.cn/saas-tenant/) / [测试](https://doc.iocoder.cn/unit-test/) | 按需核对采用能力；新业务仍须验证 |
| [设计来源与取舍](../specs/design.md#参考来源与本项目取舍) | 设计依据，不表示更换组件库 |

## 术语与编号

G/S 分级、编号格式和 R/P 前缀是模板约定，不是工具强制标准。阶段见 [八步流程](../../README.md#八步流程)，缺陷分级见 [开发手册](development.md#8-只读复核与缺陷处理)。

| 标记 | 含义 |
| --- | --- |
| FDE | Forward Deployed Engineer，贴近客户、推动工程落地的前线部署工程师 |
| G1～G5 | Gate：需求、原型、准备、开发、客户验收门槛 |
| S0～S3 | Severity：缺陷等级，S0/S1 阻断交付 |
| R / P | Requirements / Prototype：需求/原型版本，不表示软件发布版本 |
| REQ / AC | Requirement / Acceptance Criteria：需求/可观察验收条件 |
| OPEN | Open question：带来源、关联、答复与回写链的问题，入口为澄清台账 |
| ST / PAGE | State transition / Page：状态转换/原型页面 |
| MEET / FB | Meeting / Feedback：真实会议/待分类反馈 |
| CR / BL | Change Request / Baseline：改变已确认行为的申请/已批准完整组合；申请不等于批准 |
| TASK | 有产出与完成条件的工作，不限开发 |
| TEST / RUN | 验证用例或入口 / 可追溯的技术验证记录 |
| UAT | User Acceptance Testing，客户参与的验收；UAT-001 表示一轮记录 |
| BUG / LESSON | 违反有效规则的缺陷/有证据及防错动作的教训 |

`REQ-001 → AC-001-01 → TASK-001 → TEST-001 → RUN-001` 只示意关联，编号不要求同号，以追踪表为准；当前 BL 由项目状态指向。

## 本流程自行约定的部分

文件名、联合确认、固定组合、追踪映射、风险分层，以及模块化单体和 Vue 3 + Element Plus 后台默认建议均为本模板选择。采购规则仅是示例。不同 Agent 的发现、加载、权限和执行能力有差异，须验证实际结果。

<a id="example"></a>

## 贯穿示例：采购申请与规则变更

以下角色、阈值、版本和批准全部虚构。[采购原型](../prototypes/pages/index.html) 仅演示 R1.0，不含加签。

| 阶段 | 示例 |
| --- | --- |
| 准备/启动 | 默认设计只讨论表达；访谈正常和驳回案例，固定客户确认人，本期不含下单/付款/撤回/重提 |
| G1 | REQ-001 员工提交自己的申请，金额>0且最多两位小数；REQ-002 本部门主管审他人申请，驳回必填原因，终态不再处理；REQ-003 员工看自己、主管看本部门。主管来源未知进 OPEN，明确后确认 R1.0 |
| G2 | P1.0 演示列表→提交→主管处理→员工查询及失败场景，固定 R1.0/P1.0、资源清单和批准，形成 BL-001；模拟角色不证明权限 |
| G3/G4 | 固定工程/命令及精度/归属/状态/并发，跑通普通账号、接口/数据/权限/有断言测试。TASK-001 实现闭环，每条 AC 关联 TEST/RUN；未执行保持未验证 |
| G5/移交 | 全部有效 AC 做 UAT，失败修复复验；客户签认最终范围/版本/遗留后，移交或转已有上线流程，记接收证据及下一动作 |

收到“超过一万元加签”：先建 CR-001，不直接改代码。假设客户确认 `>10000.00` 才加签；负责人来自组织配置，缺配置/无合法审批人则提交失败。已提交按提交时规则，已通过不重审；负责人仅看需自己审批的记录，禁止自审批，身份重叠不自动跳步；驳回终态且不支持重提。

分析 REQ-002/003/004、页面/待办、接口/枚举调用方、权限、并发、旧数据及工期费用；固定 R1.1/P1.1 候选，批准后核对完整组合、形成 BL-002，再以 TASK-002 实现。旧 BL 保留；客户决定旧数据规则，规则快照只是实现选择。

回归区分 9999.99/10000.00 主管通过即完成与 10000.01 需负责人；旧规则待审/已通过大额行为不变。验证伪造身份、跨范围、自审批、重复审批、非法金额、重复提交，保留驳回与查询承诺；不能统一改掉旧“主管通过即完成”断言。技术验证、客户复验完成才关 CR，仍须经过 G5 与移交。

“处理时长降低”等上线后指标记录观察时间、客户数据及后续动作，未观察不报达成；新阈值/重提要求重新核对范围与 CR。
