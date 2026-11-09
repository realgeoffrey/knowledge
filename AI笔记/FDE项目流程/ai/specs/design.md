---
{
  "version": "alpha",
  "name": "FDE 管理后台默认设计（含可选大屏）",
  "colors": {
    "primary": "#0e5f41",
    "primary-soft": "#eaf6f0",
    "text": "#16211d",
    "muted": "#50635b",
    "sidebar": "#103b2e",
    "sidebar-hover": "#1b4b3b",
    "sidebar-active": "#225944",
    "sidebar-text": "#f0f7f3",
    "sidebar-muted": "#b8d1c4",
    "sidebar-accent": "#9cdbb8",
    "brand-mark": "#d3ebdd",
    "canvas": "#f3f6f4",
    "surface": "#ffffff",
    "border": "#dce5e0",
    "control-border": "#72877c",
    "on-primary": "#ffffff",
    "success": "#17665b",
    "info": "#225888",
    "warning": "#8a5200",
    "danger": "#b42318",
    "screen-bg": "#0c1c16",
    "screen-surface": "#142d23",
    "screen-text": "#edf7f0",
    "screen-muted": "#a8c5b7",
    "screen-accent": "#a8c3a7"
  },
  "typography": {
    "body-md": {
      "fontFamily": "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Microsoft YaHei', sans-serif",
      "fontSize": "14px",
      "fontWeight": 400,
      "lineHeight": "22px"
    },
    "title": {
      "fontSize": "20px",
      "fontWeight": 600,
      "lineHeight": "28px"
    },
    "subtitle": {"fontSize": "16px", "fontWeight": 500, "lineHeight": "24px"},
    "caption": {"fontSize": "12px", "lineHeight": "20px"},
    "screen-body": {
      "fontFamily": "system-ui, 'PingFang SC', 'Microsoft YaHei', sans-serif",
      "fontSize": "14px",
      "fontWeight": 400,
      "lineHeight": 1.6
    }
  },
  "rounded": {"sm": "4px", "md": "8px", "lg": "12px"},
  "spacing": {"xs": "4px", "sm": "8px", "md": "16px", "lg": "24px", "xl": "32px"},
  "components": {
    "button-primary": {
      "backgroundColor": "{colors.primary}",
      "hoverBackgroundColor": "#157a54",
      "activeBackgroundColor": "#083d2c",
      "textColor": "{colors.on-primary}",
      "height": "32px"
    },
    "nav-item": {"minHeight": "44px", "lineHeight": "24px"},
    "table-row": {"height": "48px"},
    "table-row-compact": {"height": "40px"},
    "drawer": {"width": "520px"}
  }
}
---

# 默认设计规范

> **AI维护｜按设计任务读取相关章节。** 需求前可用的默认草稿，尚无客户批准；默认管理后台，大屏按需。

规范版本：D1.12

本文件是设计规则与 tokens 的唯一来源。[规范展示页](../prototypes/design-system.html) 用于讨论风格，[业务原型](../prototypes/README.md) 用于评审业务，两者均不代替客户批准。

## Overview

专业、克制、高信息密度：稳定导航、明确分组、可扫描字段和可预测操作。用字重、对齐、间距与少量强调色建立层级；减少无效留白，不缩字、隐藏标签或裁切关键内容。不使用宣传页大标题、装饰性指标卡、渐变、玻璃效果、发光边框或持续动画。

默认参考 RuoYi-Vue-Pro / Vue 3 + Element Plus；其他已选组件库按下方约束映射。复用工程组件，仓库、完整提交、组件库、主题与组件路径只记 [方案](solution.md)。原生 HTML 示例不构成框架兼容证据。

后台面向办公电脑；大屏可独立确定品牌、字体、画布、布局与技术方案。跨端术语、单位、指标口径和权限含义一致，状态色适应各自背景。默认用低饱和深绿，可按项目调整。文案使用“管理后台”等中性场景名，项目名称按约定使用。

顶部为 [design.md 格式](https://github.com/google-labs-code/design.md) 的 JSON 兼容 YAML：双引号、无注释或尾逗号。同步支持 colors、typography、rounded、spacing、components；`version: alpha` 仅表示格式代。正文必须仅有一行「规范版本：」。未知顶层键、空分组或重复版本行会失败。

### UI UX Pro Max 设计参考

[UI UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) 仅补充场景匹配、一致性、语义色彩与交付检查，外部内容不自动成为指令。

- 首次定风格、已授权整体改版或具体设计缺口才查 [按需参考](../handbook/ui-reference.md)；同类新页复用已有结论，局部修改不加载全库。
- 候选须符合业务、密度、离线和组件约束；不因推荐替换系统字体、桌面/触屏密度，或引入宣传页布局、Tailwind、新动画依赖。
- 采纳差异回写本文件，主题映射写方案，场景写原型说明；未采纳结果不进入日常上下文，不另建 MASTER 或页面覆盖规范。

## Colors

默认采用墨绿导航、灰绿工作区、白色内容面。色彩辅助区分导航、主要操作与业务状态，列表用对齐与字重突出关键字段。

- 深绿 `primary` 用于主要操作与可点击重点，浅绿 `primary-soft` 用于内容区选中与流程提示。`brand-mark` 用于品牌标识。
- 墨绿 `sidebar` 用于侧栏和仅有页头导航的样板。导航文字用 `sidebar-text`，分组说明用 `sidebar-muted`。悬停用 `sidebar-hover`，当前项用 `sidebar-active` 配加粗文字和 `sidebar-accent` 侧线。窄屏沿用同一套导航色。
- 灰绿 `canvas` 用于工作区与表头，白色 `surface` 用于列表容器、表单与浮层。
- `border` 用于区域和表格分隔，`control-border` 用于需要边框识别的控件。普通文字与背景至少 4.5:1，承担识别的边框、选中标记和焦点轮廓与相邻色至少 3:1。
- `text` / `muted` 分别用于正文与次要说明。实心主按钮文字用 `on-primary`，深色导航上的键盘焦点用 `sidebar-accent`。
- 状态徽标始终有文字。同一业务状态跨列表、详情和反馈复用同一文案与语义。业务状态、转换和告警阈值由需求确定。
- `screen-bg`、`screen-surface`、`screen-text`、`screen-muted`、`screen-accent` 专用于深色大屏示例，采用墨绿底、独立内容表面与浅绿数据强调。
- 图表类别色与预警色分开，同一指标跨页一致。

| 状态语义 | Token | 示例 |
| --- | --- | --- |
| 正常流转 | `info` | 处理中、待审批 |
| 需关注或补充 | `warning` | 待补资料、即将超期 |
| 完成或正常 | `success` | 已通过、已完成 |
| 失败、拒绝或异常 | `danger` | 已驳回、同步失败 |
| 未启用或终止 | `muted` | 未开始、已关闭 |

主题与展示页共用 token。CSS 名由分组/名称连接，驼峰转连字符：`colors.primary` → `--colors-primary`，`typography.body-md.fontSize` → `--typography-body-md-font-size`；`{colors.primary}` → `var(--colors-primary)`。

## Typography

本地系统字体：正文 14px/22px、区块标题 16px/24px、页面标题 20px/28px、辅助信息 12px/20px；正文 400，标题与关键字段 500/600，核心字段不降至 12px。目标终端确定后可调整默认值。数字用 `tabular-nums`，金额、数量右对齐；时间、状态、操作完整，长名称换行或提供可聚焦的完整查看入口。

侧栏菜单用 14px 字号、24px 行高和常规字重，当前项用 600 字重。每项至少 44px 高，长名称换行并随内容增高。分组标题用 12px/20px 和 500 字重，与上一组留出间隔。窄屏横排的规范目录用 12px/20px，触屏菜单项仍至少 44px 高。

大屏数字、标签按真实屏幕像素、比例与观看距离校准，不照搬后台 14px；示意画布不构成分辨率或兼容性承诺。

## Layout

以 8px 为节奏，紧密项 4px。内容留白与区块间距默认 16px，大区分隔 24/32px。桌面用稳定侧栏、轻量顶栏与自适应工作区；规范页目录可直接定位章节，并标明当前章节。窄屏目录随内容换行，核心列表优先占用可用宽度。

后台顺序：“面包屑/标题 → 查询 → 操作栏 → 列表/内容 → 分页”；桌面首屏可见常用筛选、主操作、表头与部分记录。

- 查询首行通常 2–4 个高频条件，其余按需展开。查询与重置相邻，显示明确标签。查询、重置或更换条件后从结果第一页开始。从详情返回时保留原筛选和分页。
- 列表左侧放新增与必要批量动作，右侧放密度等视图设置；每个区域一个主要操作，查询与新增属于不同区域。
- 列表有记录数、列名与单位。数字右对齐，时间、状态与操作保持完整，名称占余宽。金额精度和单位随业务约定统一；有汇总时标明当前页或全部结果等范围，与明细使用同一统计口径。空字段为“—”，0 为有效值。无数据、无匹配、无权限分别提示。
- 窄屏少量字段可改带列名的记录卡；密集表格在自身容器滚动，页面不横向溢出，不靠缩字适配。
- 表单按基本信息、归属、补充说明分组，标签对齐一致。桌面短且无强顺序字段可两列，长文本通栏；窄屏单列、标签在上。输入宽度匹配内容；必填/错误靠近字段，失败保留输入并聚焦首错。
- 列表发起的详情、新建、编辑与审批默认用右侧抽屉。桌面默认宽 520px，表格或并排信息较多时可用 640–820px，窄屏用全宽。标题与关闭入口固定在顶部，主体独立滚动，提交和取消固定在底部。
- 抽屉关闭后保留原列表筛选、分页和滚动位置，键盘焦点回到触发入口。支持 Esc 退出；提交失败留在抽屉内，保留输入并就地反馈。短弹窗用于二次确认与授权。
- 详情分基本信息、状态、处理记录与当前操作，短字段用描述列表。审批先展示决策信息与状态，再放意见、通过/驳回和记录；危险动作依需求确认，不为示例增节点，合法转换来自 REQ。
- 大屏按重点指标、趋势、构成、异常组织；轮播、钻取、筛选、刷新按需求，数字可辨统计范围、单位、数据时间和无数据状态。

## Elevation & Depth

用背景、边框、留白分层；阴影只辅助浮层与悬浮操作，不把所有区域做成厚卡片。大屏用深浅表面分层，装饰不抢图表、告警和关键数字。

## Shapes

控件/常规容器/大区块圆角默认 4/8/12px，业务优先常规容器。按钮与单行输入 32px；桌面列表默认紧凑 40px，标准 48px，多行自然增高。密度只改留白。触屏的按钮、导航和行内操作至少 44×44 CSS px，相邻独立操作尽量留出 8px，窄屏触控输入字号至少 16px。

沿用组件库形态与尺寸，仅覆盖明确设计值；不同库的 size 名与行高按固定版本映射，不能假定 small 等价。这些尺寸是项目取舍，非统一强制标准。

## Components

| 模式 | 必须表达 | 由业务确定 |
| --- | --- | --- |
| 按钮 | 主/次/危险/禁用/处理中及操作反馈 | 权限、可用条件、二次确认 |
| 右侧抽屉 | 标题、关闭、独立滚动、底部操作、退出后还原焦点 | 默认宽度之外的尺寸、分段及未保存退出规则 |
| 表单 | 标签、必填、示例、错误、只读；失败保留输入 | 范围、默认、联动、校验 |
| 表格与查询 | 列名、排序/查询、空态、详情、可读长文本 | 列、权限、规模、导出、分页 |
| 详情与步骤 | 分组、状态文字、历史、操作区 | 状态转换、节点、责任 |
| 页面反馈 | 正常、加载、空、失败、无权限、冲突；原因与下一动作 | 错误语义、安全重试/刷新 |
| 大屏 | 单位、范围、更新时间、失效提示，颜色外的含义提示 | 口径、刷新/轮播、屏幕、实时性 |

正式后端验证权限与状态；页面模拟不证明授权、性能、实时数据或业务规则。

### 实心主按钮

- 每个操作区域突出一个主动作。深绿实底配白字和透明边框，悬停时提亮，按下时加深。默认、悬停、按下的文字对比度均须达到 4.5:1。
- 按钮悬停只通过背景或文字反馈。已有的中性或危险边框保持稳定，文字和图标按钮不出现描边。键盘焦点用独立外描边显示。禁用时改用中性色，取消悬停与按压反馈，并说明禁用原因。
- 默认参考 [Element Plus Button](https://element-plus.org/zh-CN/component/button.html) 的状态层级。当前主题用自己的对比度达标色值。正式工程在实心主按钮主题中映射 `--el-button-bg-color`、`--el-button-hover-bg-color` 和 `--el-button-active-bg-color`，保持文字变量和透明边框在各启用状态一致。

### 顶栏入口

消息和登录信息用图标、未读数、头像与姓名区分，入口和展开菜单项采用无框样式。展开面板位于顶栏下方，用背景、留白与轻阴影分层，未读消息和当前用户用浅色底突出。

### 组件选择与框架兼容

- 一个运行时组件库：Vue 选 Element Plus 或 Ant Design Vue，React 选 Ant Design（`antd`）；不混 API、同时装多库或自动替换 RuoYi 前端。
- 复用顺序：工程封装 → 所选库标准组件 → 确有业务缺口的最小组合。表格、分页、筛选、校验、弹窗、抽屉、日期、上传和反馈不另造机制，不包装跨库统一接口。
- 先查相邻页面、依赖与组件路径，沿用权限、字典、请求、校验及加载/错误处理；定制须在任务说明现有组件的具体缺口。
- 设计意图和语义 tokens 共用，props、主题与尺寸分别按 [所选库映射](../handbook/ui-reference.md#ruoyi-迁移约束) 核对，不同时加载多库文档。正式主题通过既有入口调整，保留键盘、焦点和错误行为。

### RuoYi-Vue-Pro 功能与页面模式

[上游内置功能](https://github.com/YunaiV/ruoyi-vue-pro#-内置功能) 仅作覆盖索引，不代表本期启用；先覆盖实际选用的系统功能与基础设施。

| 能力 | 默认模式 | 核对项 |
| --- | --- | --- |
| 用户、部门、岗位 | 部门树＋列表，详情与编辑用抽屉 | 切换保留上下文、查询范围；账号与显示名分开 |
| 角色、菜单、数据范围 | 角色列表＋权限树/分组 | 菜单/按钮/数据范围分开，部分选中与不可分配原因 |
| 字典、配置、通知模板 | 主列表＋详情/子项/编辑 | 显示值与编码、类型、启停、修改影响 |
| 登录/操作/API 日志、定时任务 | 时间筛选＋只读详情/执行记录 | 时间范围、结果、失败原因，长日志可复制 |
| 文件、导入导出 | 列表＋上传反馈/任务结果 | 类型、大小、进度、失败行、重试边界 |
| 工作流、业务单据（按需） | 待办＋详情＋处理记录 | 状态、动作、意见、错误保留；简单状态流/BPM 按需选 |
| 租户、支付、消息、业务模块（按需） | 复用上述模式 | 隔离、金额、外部发送另行确认与验证，不默认启用 |

无权限时不展示受限内容；条件不满足可禁用并解释，隐藏按钮不代替后端授权。批量动作说明选择范围与成功/失败数量。危险动作确认时写明对象与后果，按钮用具体动词，并保留取消与返回焦点的路径。审批意见、二次授权等条件按需求确定。行内通常 1–3 个高频动作，其余收入更多操作。

### 可选大屏边界

大屏不属于默认交付或阶段门槛；选用后约定范围、口径、目标屏幕与 AC。独立 `screen-*` 和 `screen-body` tokens 可单改；iframe/独立应用不自动继承后台主题，映射分别登记。

比较类别用条形图、看时间变化用折线图，坐标/单位/范围可辨；0 与缺失分开，缺失时间点不随意连线，跨图比较尺度一致。保留延迟/无数据提示，不用装饰性 3D、发光描边或无业务含义的滚动数字。

## Do's and Don'ts

- 同类操作/状态一致；正文对比度至少 4.5:1，数字图表对比可辨，键盘焦点可见且无遮挡。
- 每个动作有反馈，禁用说明原因，核心操作不依赖悬停发现。
- 沿用工程图标；静态稿用本地 SVG，不用 emoji 代功能图标，纯图标按钮有可访问名称。尊重 `prefers-reduced-motion`，动效中断仍保留状态与焦点。
- 示例用虚构名称/数据，不生成真实 REQ/AC/PAGE 或客户批准；不从展示推断权限、阈值、口径或擅增业务。
- 展示页离线，无网络、CDN、外部字体、后端、账号或构建依赖；正式系统离线/内网要求另行确认。

### 原型交付检查

1. 对比与键盘。检查正文、各语义徽标、主按钮各状态及控件边界；焦点清楚且无遮挡。抽屉和确认弹窗支持 Esc 退出并恢复焦点，确认关闭抽屉后列表上下文仍在。
2. 布局与触屏。检查 375、768、1024、1440px；后台另查 1366、1920px。页面不横向溢出，密集表格在表格区域内滚动，标签与长内容完整可读。按粗指针检查触控尺寸。
3. 表单与反馈。标签可见，首错可聚焦，错误贴近对应字段且保留输入。核对加载、空态、无权限、失败、冲突及恢复动作；状态以文字表达并尊重减少动效设置。
4. 数据与一致性。检查等宽数字、金额与单位、0 与空值、同一状态的跨页表达。图表需能读出系列、单位、范围与更新时间；只评审选用的图表和大屏。

视口检查档位用于原型走查，客户兼容范围由项目约定。

## 修改与项目确认

需求前可直接调整默认设计；已有需求以真实业务及有效 BL 为约束。设计、原型、页面任务按需读取本文件章节/tokens、REQ/AC、有效 BL 和方案主题/组件入口；大屏选用才读其独立规则。

1. 设计值先改顶部数据；意图、布局、交互或范围变化同步正文和样例，并更新 `规范版本`。仅整理文字与路径不改变版本。
2. 在项目根执行 `python3 ai/scripts/sync_design.py`，同步已登记页面的 tokens 和设计版本标签；原型目录有未登记 HTML 时先补 `PAGE_FILES`，生成槽不手改，业务 R/P 版本独立。脚本不生成正文、布局或交互。
3. 执行 `python3 ai/scripts/check_context.py`，再离线复核受影响布局、交互、桌面与窄屏；正式系统另核组件映射、受影响 AC，并保存 RUN。
4. 首次定风格打磨一张覆盖本期列表/筛选、表单、详情或审批的代表页，采纳入口与版本记原型说明，新页复用。新模式、整体改版或共享主题变化实际渲染检查对齐、密度、长文本、状态、窄屏，不能只看代码。G1 约定显示环境 AC，G2 确认真实原型和规范，G3 用实际组件代表页核对样板。
5. 客户采纳的章节、场景、承诺与必要资源随需求/原型进入 [固定基线清单](../records/acceptance.md)；未采纳章节不算承诺。草稿直接迭代，违反已确认承诺记 BUG，改变承诺/AC 走 CR，普通且不触及承诺/行为的微调记 TASK。
6. 新项目固定规范来源版本；既有项目不自动升级 BL。冲突按澄清/变更规则处理，不能用默认设计覆盖已批准需求。问题记 OPEN、映射记方案、证据记 RUN，其他位置只链接；无实际拆分需求不建独立设计仓库。

## 参考来源与本项目取舍

核对日期：2026-11-09。离线展示不加载参考网站，新增组件/API 按既有工程和实际需求核验。

| 来源 | 采用的原则 / 项目取舍 |
| --- | --- |
| [Ant Design 字体](https://ant.design/docs/spec/font-cn/) / [布局](https://ant.design/docs/spec/layout-cn/) | 中文层级、数字等宽、自适应与 8px 节奏；14/22px 正文、20px 标题和具体留白为项目选择 |
| 《设计规范 · 徐州供应链》（本地参考） | 参考绿白层次、分章目录、可核对的表格、状态映射及右侧抽屉。供应链业务流程和权限随实际需求确定 |
| [国家农产品质量安全追溯管理信息平台](https://www.qsst.moa.gov.cn/xxcj/) | 参考农产品追溯、监管与监测的业务场景 |
| [Ant Design 色彩](https://ant.design/docs/spec/colors/) / [WCAG 文字对比](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) / [非文本对比](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html) | 以中性色分层，品牌色用于重点与反馈，分别核对文字和控件识别所需的对比度 |
| [数据展示](https://ant.design/docs/spec/data-display-cn/) / [数据录入](https://ant.design/docs/spec/data-entry-cn/) | 列表优先级、状态/操作完整、标签与上下文 |
| [TDesign 尺寸](https://github.com/Tencent/tdesign-common/blob/develop/style/web/theme/_size.less) / [字体](https://github.com/Tencent/tdesign-common/blob/develop/style/web/theme/_font.less) | 尺寸与字阶分级；32px 控件、48/40px 行高为本项目组合 |
| [Element Plus Table](https://element-plus.org/zh-CN/component/table.html) | 复用表格、列宽、固定列与选择能力，按固定版本核对 props |
| [Ant Design 主题](https://ant.design/docs/react/customize-theme) / [Ant Design Vue ConfigProvider](https://github.com/vueComponent/ant-design-vue/blob/main/components/config-provider/index.en-US.md) | 项目统一主题，Vue/React 分别核对 API |
| [UI UX Pro Max Web UX 指南](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/main/.claude/skills/ui-ux-pro-max/references/quick-reference.md) | 采用场景匹配、语义 tokens、键盘焦点、响应式、状态反馈与减少动效原则。桌面后台保留 14px 正文、32px 控件和紧凑列表，触屏单独适配 |
| [AntV 原则](https://antv.antgroup.com/zh/specification/principles/basic/) | 大屏可靠、易读、辅助判断，装饰不妨碍数据表达 |
