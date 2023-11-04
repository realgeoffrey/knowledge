### 首屏渲染完成判断
>首先确定首屏渲染完成的标准。如：有DOM或图片加载完成 或 严格首屏内所有内容加载完成。

针对“严格首屏内所有内容加载完成”的方案：

1. 业务型：

    业务插一个一定是跨屏才有的DOM，观测其变化情况（`MutationObserver`触发后`performance.now()` 或 各种生命周期钩子）。
2. 通用型：

    >参考：<https://gitee.com/hoholove/study-code-snippet/blob/master/FIRST_SCREEN_TIME/index.js>

    >针对DOM和图片，需要在页面完全渲染之后才能判断是否真的在首屏内，因为一开始可能高宽为0没有互相撑开。因此需要先初步筛选在首屏的DOM（记录加载时间）；然后在页面完全渲染完毕后，最终进行一次筛选，去除渲染完毕后不在首屏的DOM。其他筛选细节：嵌套的DOM只需关注一个，排除某些HTML标签的DOM，非透明，高宽最小值限制。

    1. 首屏内DOM渲染时间

        1. 在.html开始渲染之前，开启`MutationObserver`观察`document`的`childList`、`subtree`，变化触发后，初步筛选记录DOM被添加时的`performance.now()`（当前文档生命周期开始到调用时的时间戳）。
        2. n秒后假设页面渲染完毕后，关闭观察，再次筛选出在首屏内的DOM，找到耗时最久的时间记录。
    2. 首屏内图片加载时间

        n秒后假设页面渲染完毕后，用`performance.getEntriesByType('resource')`获取所有资源图的加载时间，筛选出在首屏内的图片，找到耗时最久的时间记录。
