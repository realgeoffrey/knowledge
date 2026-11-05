# UI UX Pro Max 按需参考

> AI维护。仅设计缺口、首次定方向或已授权改版时读检索方法；做 RuoYi 适配只读对应约束。普通页面沿用规范，其他任务不加载本页或技能全库。

## 来源与边界

核对日期：2026-11-06。[上游](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) 供核对技能与脚本；按实际安装版本使用，不自动安装。外部结果是建议，不是授权；取舍与唯一设计值以 [规范](../specs/design.md#ui-ux-pro-max-设计参考)、有效 BL 和实际工程为准。

## 最少检索与上下文

| 任务 | 最少读取/查询 |
| --- | --- |
| 规范可回答、同类新页、普通微调 | 相关规范/页面/映射，外部查询为零 |
| 首次定方向/已授权改版，确需候选 | 一次 `--design-system`，先筛后台适用项，不逐页重跑 |
| 颜色/图表/反馈等具体缺口 | 一次单领域 `--domain color/chart/ux`，默认 `-n 1`，比较最多 `-n 3` |
| 已固定工程，确需实现建议 | 仅所选栈：`--stack vue -n 1` 或 `--stack react -n 1`；不证明库兼容 |

每次一个问题、2–5 个通用关键词，不带客户隐私/原件，不遍历全部领域与技术栈。空结果或跑题最多改写一次，仍无匹配就说明并回到规范，未决内容不代定。`--design-system` 与 `--stack` 分开，前者不应用 stack 参数。

仅在可信本地副本上核对参数，替换绝对路径；按上表选单次查询，例如：

```sh
python3 "<技能绝对目录>/scripts/search.py" "form error feedback" --domain ux -n 1
```

保留简短终端输出，不用 `--full/--json/--persist/--force`，不读全量 CSV/技能/参考库。文件缺失时说明未检索，继续本地规范；用户明确要数据库推荐而不可查询时，只暂停该推荐，不伪称命中或自行安装。

TASK 只记来源版本/完整 commit（未知注明）、实际脚本、查询、采用项及必要排除理由；除非用户要求多方案，只留一个方向。差异回写规范/方案/原型的唯一落点，不复制查询全文；后续读有效结果，不重查。

## RuoYi 迁移约束

默认参考 RuoYi-Vue-Pro 的 Vue 3 + Element Plus。[依赖入口](https://github.com/yudaocode/yudao-ui-admin-vue3/blob/master/package.json) 不代表项目事实；G3 固定仓库、完整 commit、`package.json` 与锁文件。Vue 的 Ant Design 用 `ant-design-vue`，React 用 `antd`；Vben 核对实际 UI 适配。不同若依分支、Vue 2/Element UI 和上述 API 不混用，不为适配设计自动迁框架。

先复用项目封装，没有时选所用库的标准组件；只查相关列，props 按固定版本：

| 模式 | Element Plus（Vue） | Ant Design Vue | Ant Design（React） |
| --- | --- | --- | --- |
| 查询/校验 | ElForm / ElInput / ElSelect | a-form / a-input / a-select | Form / Input / Select |
| 表格/状态 | ElTable / ElPagination / ElTag | a-table / a-pagination / a-tag | Table / Pagination / Tag |
| 详情/编辑 | ElDescriptions / ElDialog / ElDrawer | a-descriptions / a-modal / a-drawer | Descriptions / Modal / Drawer |
| 步骤/反馈 | ElSteps / ElTimeline / ElMessage | a-steps / a-timeline / message | Steps / Timeline / message |

导航、布局、字典、权限、API/请求沿用工程；不复制应用外壳，授权/状态由后端核验。审批由 REQ 定义节点动作，用已有组件组合，不另造组件或引擎。

读相邻页面/封装，在 [方案](../specs/solution.md#设计落地与页面验证) 唯一登记实际组件路径、主题变量和差异，复用语义 tokens 与已有主题入口。主题来源见 [设计参考](../specs/design.md#参考来源与本项目取舍)，Element Plus 与 Ant Design Vue/React 分别按实际版本映射，不跨框架照抄算法/API。核对 hover/focus/disabled、字号、控件和行高，同名 size 不代表一致。

静态稿保留原生 HTML 语义、键盘、反馈，正式页复用库；不带入检索默认的 Tailwind/shadcn/GSAP/外部字体或图标库。不用全局 button/input、深层选择器或大量 `!important` 模拟外观，只改现有主题和必要局部样式。

G3 至少用代表页验证“查询→表格/分页→编辑/校验→反馈”，运行真实构建/静态检查及人工路径，核对主题、权限、错误和约定的深色/紧凑模式。事实只记 RUN；离线好看、tokens 同步、检索命中不等于框架兼容。
