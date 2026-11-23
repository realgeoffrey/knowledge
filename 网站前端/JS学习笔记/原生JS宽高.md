### 原生JS宽高（以横轴为例）

1. `client`

    1. 普通块元素的 `.clientWidth` 是内边距盒的宽度，扣除占据布局空间的垂直滚动条，不含边框和外边距。

        读布局视口宽度（不含滚动条）时，标准模式使用 `document.documentElement.clientWidth`，怪异模式使用 `document.body.clientWidth`。
    2. `.clientLeft` 通常等于左边框宽度；当垂直滚动条位于元素左侧并占用空间时，还包括该滚动条的宽度。
2. `offset`

    1. 普通块元素的 `.offsetWidth` 是布局边框盒的整数宽度，包含内边距、边框和占据布局空间的滚动条。
    2. `.offsetLeft`

        有 `offsetParent` 时，取元素第一个布局盒的左边框外缘到 `offsetParent` 左内边距边缘的横向距离。它取决于实际布局，计算时忽略 CSS 变换。

        >`body` 或没有布局盒的元素返回 0；其他没有 `offsetParent` 的元素按初始包含块的原点计算。
3. `scroll`

    1. `.scrollWidth`

        1. 文档的滚动宽度：标准模式读取 `document.documentElement.scrollWidth`，其值至少等于布局视口宽度。
        2. 普通块元素：包含溢出内容在内的滚动区域宽度。没有横向溢出时通常等于 `clientWidth`，横向滚动可见的内容会使它增大。
    2. `.scrollLeft`

        可读写，表示水平滚动位置。常见的从左向右布局中，向右滚动时数值增大；从右向左布局中，向左滚动时可取负值。

参考：[CSSOM View 规范](https://drafts.csswg.org/cssom-view/#extensions-to-the-element-interface)。
