## 原生JS宽高（横轴为例）

1. `client`

    1. `document.body`或`DOM`的`.clientWidth` = ` 可视部分宽度 ＋ padding左右宽度 - 滚动条宽度`。

        使用方式：`document.documentElement.clientWidth || document.body.clientWidth`。
    2. `document.body`或`DOM`的`.clientLeft` = `border左宽度`。
2. `offset`

    1. `document.body`或`DOM`的`.offsetWidth` = ` 可视部分宽度 ＋ padding左右宽度 + border左右宽度`。
    2. `document.body`或`DOM`的`.offsetLeft`

        >相对于`offsetParent`(祖先节点有定位或body)。

        1. ie6/7：

            `.offsetLeft` = `当前元素的margin左宽度 + offsetParent的(padding左宽度)`。
        2. ie8/9/10、chrome：

            `.offsetLeft` = `当前元素的margin左宽度 + offsetParent的(padding左宽度 + margin左宽度 + border左宽度)`。
        3. Firefox：

            `.offsetLeft` = `当前元素的margin左宽度 + offsetParent的(padding左宽度 + margin左宽度)`。
3. `scroll`

    1. `.scrollWidth`

        >`document.body`和`DOM`有区别。

        1. `document.body`

            1. 给定宽度 < 浏览器窗口宽度：

                `document.body.scrollWidth` = `浏览器窗口宽度`。
            2. 内容宽度 < 给定宽度 > 浏览器窗口宽度：

                `document.body.scrollWidth` = `给定宽度 + padding左右宽度 + border左右宽度 + margin左右宽度`。
            3. 内容宽度 > 给定宽度 > 浏览器窗口宽度：

                `document.body.scrollWidth` = `内容宽度 + padding未超出边宽度 + border未超出边宽度 + margin未超出边宽度`。
        2. `DOM`

            1. 内容宽度 < 给定宽度

                1. 无滚动轴：

                    `DOM.scrollWidth` = `DOM.clientWidth` = `给定宽度 + padding左右宽度`。
                2. 有滚动轴：

                    `DOM.scrollWidth` = `内容宽度 + padding左右宽度`。
    2. `.scrollLeft`

        可读写。是内容宽度超出其宽度时，元素**被卷起**的宽度。
