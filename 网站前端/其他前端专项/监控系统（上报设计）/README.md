### 监控系统（上报设计）
>开源监控系统（支持各种开发语言和系统、支持完备的前端监控）：[sentry](https://docs.sentry.io/)

- 确定上报口径（尤其是针对性能相关判断口径、标准）
- 异常告警通知机制
- 日志规范化

    - [前端日志输出规范（Native）](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/其他前端专项/前端日志输出规范（Native）/README.md)
- 堆栈聚合策略，数据抽样，数据清洗（重复，缺失，超出正常范围）

    >报错可能出现：突发、类似、重复、时间聚集。上报信息可能不完整（无法分析）、可能有极大值极小值情况（污染整体数据）。

1. 前端

    1. 上报内容

        1. 性能分析

            - 常规文档导航记录 `PerformanceNavigationTiming`，如 `responseStart` 和 `loadEventEnd`。业务路由、首屏内容、宿主启动分别定义起止点和单位。[浏览器性能 API 示例](../../前端内容/标准库文档.md#performance) · [首屏渲染完成判断](../首屏渲染完成判断/README.md)
            - 线上 Web Vitals 采用 `web-vitals` 的 `onLCP`、`onINP`、`onCLS`。同一采集口径在每个文档初始化一次。页面多次进入后台或启用 `reportAllChanges` 时，同一指标实例可能多次上报，服务端按指标名和 `metric.id` 保留最新的完整指标值 `value`（可由客户端附单调递增序号以应对乱序）。从后退缓存恢复会产生新的指标实例。按发布版本、路由和设备组计算 p75，同时给出有效样本数；无交互的访问缺少 INP，不能填零。[web-vitals 作者文档](https://github.com/GoogleChrome/web-vitals)
            - SPA 若要分析一次切页，可在支持的浏览器用 web-vitals v6 的 `{ reportSoftNavs: true }` 单独采集。按库提供的 `navigationId` 和 `navigationURL` 归属，避免延迟上报时读到下一页的 `location.href`。分别保留整次文档访问和分段口径，比较升级前后的数据时注明口径、浏览器覆盖率及未识别的路由比例。[Chrome 软导航采集示例](https://developer.chrome.com/docs/web-platform/soft-navigations)
            - `requestAnimationFrame` 回调间隔可观察前台页面调度抖动，后台节流和屏幕刷新率都会影响读数。排查掉帧时补录 Performance 的 Frames 轨道。排查慢交互时观察同一交互的输入、处理和呈现阶段。[Performance 面板](https://developer.chrome.com/docs/devtools/performance/reference)
        2. 用户行为

            >用户习惯、行为模式。

            1. PV、UV、访问时段、访问时长

                - SPA 可在路由切换成功后统计 PV。自行监听时，片段变化可用 `hashchange`，历史记录前进、后退可用 `popstate`；主动调用 `pushState`、`replaceState` 本身不会触发这两个事件，需在实际切页处记录并去重。
            2. 设备、浏览器语言、浏览器、活跃时间段、页面版本号等的用户特征（多维度）

                - 数据隐私和安全：信息脱敏（合规），通信安全。
            3. 染色（标记）某uid：获取某uid所有上报信息

                1. 用户的行为追踪：某uid，进入网站后的一系列操作或者跳转行为；

                    1. 页面间链路保存，顺序进行了哪些操作
                    2. 热力图
                2. [rrweb](https://github.com/rrweb-io/rrweb)录屏
            4. 业务曝光、点击上报。

            - 用户关键链路操作保存

                >（类似后端微服务的全链路监控，）把用户关键操作链路保留，压缩缓存起来，在其他上报时带上。可以利用本地缓存技术，如：sessionStorage。跨页面考虑在跳转url上带链路信息。e.g. 用户来源的活动页、点击跳转新页面按钮、点击付费等营收相关按钮。
        3. 错误上报

            1. JS代码运行错误

                - 浏览器在 window 上监听 `error` 和 `unhandledrejection`。Node.js 若只想记录致命异常，可监听 `uncaughtExceptionMonitor`，保留进程默认的退出行为。
                - React的错误边界
                - 异步错误（异步代码内`try-catch`）
            2. 静态资源加载错误

                资源DOM的`error`事件 或 统一到window监听`error`的捕获事件。
            3. 接口请求的 报错、状态码、响应时间

                封装或劫持 接口请求进行上报细节处理。

            - 合并相似错误信息，过滤异常数据

            >[白屏问题](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/其他前端专项/白屏问题/README.md)
        4. 资源监控

            >页面静态资源：js、css、图片、字体、video、audio。

            监控页面加载的静态资源的 加载时间、成功与否、资源大小、类型等信息，以便进行性能分析和优化。

            >[`performance.getEntriesByType("resource")`](https://developer.mozilla.org/en-US/docs/Web/API/Performance/getEntriesByType) 返回缓冲区内已有的资源计时条目，时间相对于 `performance.timeOrigin`。跨源资源的部分字段受 `Timing-Allow-Origin` 限制；判断资源能否使用还应结合元素的 `load`、`error` 或请求结果。
    2. 实现细节

        1. 上报方式：[`XMLHttpRequest`、`fetch`、`navigator.sendBeacon`、`<img src>`](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/前端内容/基础知识.md#浏览器发起网络请求方式)
        2. 减少对业务影响（不能影响客户端原有的 性能、首屏渲染时间）

            1. 加载时机

                - 页面最先挂载 上报用的空函数（空函数：仅保存调用的参数）；监控SDK异步加载后重写空函数，处理之前调用的参数。

                1. 先加载 最小化 需要立即监听的 逻辑。e.g. 路由变化、请求监听。
                2. 其他延后异步加载。e.g. 静态资源监控、性能上报。
            2. 使用小批量队列，按数量或时间在前台冲刷；`visibilitychange` 进入 `hidden` 时再尝试发送剩余数据。为每条事件生成稳定 ID，重复传输时在接收端去重。记录客户端排队失败数，接收端核对实际到达量；`sendBeacon()` 返回 `true` 只说明浏览器接受入队。[Beacon](https://www.w3.org/TR/beacon/)

                联调时保持 Network 的 Preserve log 开启，切到另一标签页后返回，再切出一次。检查第一批事件是否在隐藏时发出，第二批是否仅含新事件；用同一事件 ID 对照接收日志。随后测试离线或接收端失败，确认该类缺数在看板上有明确口径。

            - SDK容错，出现SDK异常不影响客户端功能（`try-catch`包裹SDK？）。
            - 减少上报数据类型，压缩上报数据。
        3. 插件化，功能可拔插，按需加载。
        4. 离线日志

            日志考虑在用户APP端本地保存一份，在必要时引导用户上传分析 或 网络恢复时补上报（方便专注分析当前用户日志；兜底弱网或其他上传失败的场景）。
2. 后端

    1. 监控、告警：接口稳定性，错误码、耗时、QPS 的变化。自动扩缩容。
    2. 微服务的 全链路监控（问题链路排障，服务间调用关系）

        ><https://github.com/open-telemetry/docs-cn>

- 结构：

    1. 数据采集
    2. 日志上报
    3. 数据整理、储存、可视化、配置，用户数据追踪系统

        1. 指标：用于衡量事物发展程度的单位或方法，度量。需要经过加和、平均等汇总计算方式得到，并且是需要在一定的前提条件（维度）进行汇总计算。e.g. 时长、xx率、计数。
        2. 维度：是事物或现象的某种特征，是对数据进行分组和分类的属性或特征。e.g. 用户维度（性别、年龄、等）、地理维度、时间维度、渠道维度、页面类别。

        >ElasticSearch、Kibana

>①先通过统计的数据找到问题页面，②再通过日志详情查找具体问题堆栈关键字，③配合真机模拟调试分析出问题原因，④最终推动上下游人员共同修复问题。
