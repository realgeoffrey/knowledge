### 首屏渲染完成判断

todo: https://mp.weixin.qq.com/mp/appmsgalbum?action=getalbum&album_id=1997906031212888065

- 首先确定首屏渲染完成的标准

    比如，首屏内所有DOM或图片加载完成。

1. 针对“首屏内所有DOM或图片加载完成”的方案：

    1. 业务型：

        业务插一个一定会跨屏才会内容，观测其变化情况（`MutationObserver`触发后`performance.now()`）
    2. 通用型：

        1. 页面加载完毕事件之后，查看所有图片的位置和容器高度关系，只要找到一个位置大于屏幕高度的，当做首屏出现，去`performance.getEntriesByType('resource')`查看这个图片的加载时间。

            若没有图片，则记录DOM的渲染时间，取最大的渲染时间（`MutationObserver`，需要使用`performance.now()`及时获取时间）
        2. 上面的判断之前，首屏被滚动

            1. 可以当做渲染完成；
            2. 也可以当做是需要被去除上报的case（滚动事件先与上面的上报，可能导致上面逻辑不准确，能滚动屏幕也不一定确定首屏内容一定被加载完毕）。
