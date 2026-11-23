### 虚拟列表模拟长列表方案

滚动加载决定**何时取下一页数据**，虚拟列表决定**已有数据中哪些行需要渲染**。两者可以一起用。接口分了页，如果滚过的每一行都留在 DOM 里，节点数仍会随滚动增长。虚拟化能减少挂载的节点，已经加载的业务数据仍可能占用内存。[Vue 的长列表性能说明](https://vuejs.org/guide/best-practices/performance.html#virtualize-large-lists)

#### H5 等高行怎么算

以竖向列表为例，假设每行实际占用同样的高度（含行间距），可视区域和行高都大于 0。每次按当前滚动位置算整个区间。拖动滚动条可能一次跨过几百行，此时只增删一行会算错。

```js
// 返回 [start, end)，可直接用于 rows.slice(start, end)
function visibleRange(count, rowHeight, scrollTop, viewportHeight, buffer = 2) {
  const maxTop = Math.max(0, count * rowHeight - viewportHeight);
  const top = Math.min(Math.max(0, scrollTop), maxTop);
  const start = Math.max(0, Math.floor(top / rowHeight) - buffer);
  const end = Math.min(count, Math.ceil((top + viewportHeight) / rowHeight) + buffer);
  return [start, end];
}

visibleRange(100, 40, 85, 80, 0); // [2, 5)，行 2 和行 4 都只露出一部分
visibleRange(100, 40, 3920, 80);  // [96, 100)，底部保留上方两行缓冲
```

算出区间后，有两种常见布局。

- **行留在文档流内。** 列表顶部留出 `start * rowHeight`，底部留出 `(count - end) * rowHeight`。中间的行照常排版，三段合起来就是列表总高度。
- **行脱离文档流。** 用容器撑出 `count * rowHeight` 的总高度，把渲染区绝对定位到容器顶部，整体下移 `start * rowHeight`。

行高会随换行或图片加载而变化时，需要记录各行的实际高度，用累计高度定位首尾行，尺寸变化后更新偏移量。滚动期间可比较新区间与旧区间，只在边界变化时更新节点。`requestAnimationFrame` 可将 DOM 更新安排到绘制前，单独包一层通常不会降低滚动回调频率。[MDN 滚动事件说明](https://developer.mozilla.org/en-US/docs/Web/API/Document/scroll_event#scroll_event_throttling)

#### 类 RN（前端维护逻辑，客户端上屏）

1. 前端计算可见区间，只把区间内的视图描述交给客户端，沿用上面的窗口计算。
2. 使用 Native 长列表组件时，先看所用组件在哪一层复用视图。客户端可能已复用原生视图，而前端仍一次创建了整份数据的视图描述。排查内存时，两边分开看。
3. 如果瓶颈在前端构造大量节点或跨端传输，可考虑把数据和可复用的行模板交给 Native，由客户端按需生成行。前提是客户端组件支持这套协议。
