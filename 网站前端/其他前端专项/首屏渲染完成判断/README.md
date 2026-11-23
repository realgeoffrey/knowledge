### 首屏渲染完成判断
>首先确定首屏渲染完成的标准。如：有DOM或图片加载完成 或 严格首屏内所有内容加载完成。

若关注首屏主体内容何时可见，可观察 [Largest Contentful Paint（LCP）](https://web.dev/articles/lcp)。它记录视口内符合条件的最大图片或文本块的绘制时间。若业务要求首屏内所有内容就绪，还需单独定义哪些内容必须完成。

1. 业务型：

    在首屏业务内容的末尾放置标记节点，可在 `MutationObserver` 或组件挂载回调中用 `performance.now()` 记录 DOM 已更新的时刻。若首屏还依赖异步数据或图片，应在必要内容就绪后再打点；这些回调本身无法确认像素何时上屏。
2. 通用型：

    >参考：<https://gitee.com/hoholove/study-code-snippet/blob/master/FIRST_SCREEN_TIME/index.js>

    >针对DOM和图片，需要在页面完全渲染之后才能判断是否真的在首屏内，因为一开始可能高宽为0没有互相撑开。因此需要先初步筛选在首屏的DOM（记录加载时间）；然后在页面完全渲染完毕后，最终进行一次筛选，去除渲染完毕后不在首屏的DOM。其他筛选细节：嵌套的DOM只需关注一个，排除某些HTML标签的DOM，非透明，高宽最小值限制。

    1. 首屏内DOM渲染时间

        1. 在.html开始渲染之前，开启`MutationObserver`观察`document`的`childList`、`subtree`，变化触发后，初步筛选记录DOM被添加时的`performance.now()`（当前文档生命周期开始到调用时的时间戳）。
        2. n秒后假设页面渲染完毕后，关闭观察，再次筛选出在首屏内的DOM，找到耗时最久的时间记录。
    2. 首屏内图片加载时间

        先记录首屏必需图片的加载结果（`load`、`error`）。到截止时仍有图片在加载，就上报超时。有图片失败则记录失败。全部加载成功后，可用 `img.currentSrc` 查找候选资源计时条目，再结合 `initiatorType`、请求时机等信息确认条目对应本次图片加载。同一 URL 可能有多条记录。每张图片都能确认归属时，取最晚的 `responseEnd`。条目缺失或归属不明确时，标记计时不完整。这个值表示资源接收结束，图片解码和绘制还可能发生在之后。[W3C Resource Timing](https://www.w3.org/TR/resource-timing/#resources-included)
