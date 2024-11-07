### 监控系统（上报设计）
- 确定上报口径（尤其是针对性能相关判断口径、标准）
- 异常告警通知机制
- 日志规范化

    - [前端日志输出规范（Native）](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/其他前端专项/前端日志输出规范（Native）/README.md)
- 堆栈聚合策略，数据抽样，数据清洗（重复，缺失，超出正常范围）

    >报错可能出现：突发、类似、重复、时间聚集。上报信息可能不完整（无法分析）、可能有极大值极小值情况（污染整体数据）。

1. 前端

    1. 上报内容

        1. 性能分析，利用[`PerformanceNavigationTiming`](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceNavigationTiming)获取页面加载完成时间数据

            - 若是客户端性能数据，则统一性能口径后在关键链路埋点上报。
            - 帧数（`requestAnimationFrame`）。
            - 自定义需要监测性能、测速的上报。

            >[首屏渲染完成判断](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/其他前端专项/首屏渲染完成判断/README.md)
        2. 用户行为

            >用户习惯、行为模式。

            1. PV、UV、访问时段、访问时长

                - SPA需要处理监听`hashchange`（hash）或`popstate`（history）事件
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

                - 兜底上报（浏览器的window监听`error`，`unhandledrejection`，Node.js的`process.on('uncaughtException', err => {})`、`process.on('unhandledRejection', err => {})`）
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

            >[`performance.getEntriesByType("resource")`](https://developer.mozilla.org/en-US/docs/Web/API/Performance/getEntriesByType)获得所有静态资源的`PerformanceResourceTiming`实例，根据每个`PerformanceResourceTiming`实例属性判断 各种绝对时间、加载成功/加载失败、资源大小、类型 等信息。
    2. 实现细节

        1. 上报方式：[`XMLHttpRequest`、`fetch`、`navigator.sendBeacon`、`<img src>`](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/前端内容/基础知识.md#浏览器发起网络请求方式)
        2. 减少对业务影响（不能影响客户端原有的 性能、首屏渲染时间）

            1. 加载时机

                - 页面最先挂载 上报用的空函数（空函数：仅保存调用的参数）；监控SDK异步加载后重写空函数，处理之前调用的参数。

                1. 先加载 最小化 需要立即监听的 逻辑。e.g. 路由变化、请求监听。
                2. 其他延后异步加载。e.g. 静态资源监控、性能上报。
            2. 上报时机：日志池，缓存后统一合并上报；`requestIdleCallback`；频控；根据网络情况、根据APP内存占用情况。

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
