#html+css学习笔记

## CSS

### 用css创造三角形
```css
div {
    border-width: 20px;
    border-style: dashed solid dashed dashed; /* dashed兼容ie6*/
    border-color: transparent #000 transparent transparent;
    height: 0;
    width: 0;
    _overflow: hidden;
}
```

> 两个同样大小的三角形，第二个设置为背景色并且覆盖到第一个上面，可以模拟箭头**>**。

### 清除浮动：
1. 在父级设置

    ```css
    .clearfix:after {
        content: "";
        display: table;
        clear: both;
    }
    .clearfix {
       *zoom: 1;
    }
    ```
2. 截断不影响时，在父级设置

    ```css
    .father {
        overflow: hidden;
        _width: 100%;
    }
    ```

### 单行文本和多行文本超出宽度显示省略号
1. 单行

    ```css
    .ellipsis {
        _width: 100%;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }
    ```
2. 多行

    ```css
    .multi_ellipsis {
        line-height: 1;
        height: 2em;
        display: block;
        display: -webkit-box;
        *display: block;
        overflow: hidden;
        text-overflow: ellipsis;
        -webkit-box-orient: vertical;
        -webkit-line-clamp: 2;
    }
    ```

### 模糊效果滤镜（高斯模糊）
1. CSS3（除*ie10*与*ie11*外基本所有主流浏览器）

    ```css
    .filter {
        -webkit-filter: blur(10px);
        -moz-filter: blur(10px);
        -ms-filter: blur(10px);
        filter: blur(10px);
        filter: progid:DXImageTransform.Microsoft.Blur(PixelRadius=10, MakeShadow=false); /* ie6~ie9 */
    }
    ```
2. SVG（较新版本的FireFox、Chrome、Opera）

    >新建一个SVG文件，把滤镜方法放进去，然后css调用`filter: url(某.svg#某id);`

    ```svg
    <?xml version="1.0" standalone="no"?>
    <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
    <svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:ev="http://www.w3.org/2001/xml-events" baseProfile="full">
        <defs>
            <filter id="某id">
                <feGaussianBlur stdDeviation="10"/>
            </filter>
        </defs>
    </svg>
    ```
    ```css
    .filter {
        -webkit-filter: url(某文件.svg#某id);
        -moz-filter: url(某文件.svg#某id);
        filter: url(某文件.svg#某id);
    }
    ```

3. canvas

    （待续）

### 移动端半像素
不可以使用`border: 0.5px`，因为浏览器会把宽度换算成0或者1。

1. 整个边框0.5px

    ```css
    div {
        width: 宽度;
        position: relative;
    }
    div:before {
        position: absolute;
        top: 0;
        left: 0;
        content: "";
        width: 200%;
        height: 200%;
        border: 1px solid 颜色;
        transform: scale(.5, .5);
        transform-origin: 0 0;
        box-sizing: border-box;
    }
    ```
2. 某一边0.5px

    ```css
    div {
        width: 100px;
        position: relative;
    }
    div:before {
        position: absolute;
        top: 0;
        left: 0;
        content: "";
        width: 100%;
        height: 1px;
        border-top: 1px solid 颜色;
        transform: scaleY(.5);
        transform-origin: 0 0;
        box-sizing: border-box;
    }
    ```

### wap页面自适应图片
要求：图片根据浏览器窗口变化而宽高一同等比例变化，不使用`img`标签。

1. *横向、纵向百分比的`padding`（和`margin`）值都是以父元素的`width`为基础，`height`是以父元素的`height`为基础*

    ```css
    自适应图片 {
        height: 0;
        width: 宽%;
        padding-bottom: 高%;
        background-size: 100%;
        background: url(单图) 0 0 no-repeat;
    }
    ```

    >缺点：只能用于空标签
2. 宽高都用rem
    1. 单图

        ```css
        自适应图片 {
            width: 宽rem;
            height: 高rem;
            background-size: 100%;
            background: url(单图) center center no-repeat;
        }
        ```
    2. 雪碧图

        ```css
        自适应图片 {
            width: 宽rem;
            height: 高rem;
            background-size: 雪碧图宽rem;
            background: url(雪碧图) 0 -纵轴rem no-repeat;
        }
        ```
        >`background-position`用`rem`会出现换算小数导致定位偏离问题，改用以下百分比可以解决偏离问题。
3. 宽高都用rem并且雪碧图并且`background-position`用百分比

    >百分比公式：
    >   - `background-position-x = 小图横坐标px / ( 大图宽度px - 小图宽度px ) \* 100%`
    >   - `background-position-y = 小图纵坐标px / ( 大图高度px - 小图高度px ) \* 100%`
    1. rem宽高（最佳情况）

        ```css
        自适应图片 {
            width: 宽rem;
            height: 高rem;
            background-size: 雪碧图宽rem;
            background: url(雪碧图) 计算出x轴的百分比 计算出y轴的百分比 no-repeat;
        }
        ```
    2. *百分比宽高*

        ```css
        自适应图片 {
            height: 0;
            width: 宽%;
            padding-bottom: 高%;
            background-size: 雪碧图宽/单图宽度*100%;
            background: url(雪碧图) 计算出x轴的百分比 计算出y轴的百分比 no-repeat;
        }
        ```

### `table`
1. table属性为`table-layout: fixed;`，其td或th的内容由第一行宽度决定。
2. 没有设定宽度的td或th宽度自适应（父级宽度减去其他固定宽度的兄弟td或th）。
3. 一个tr内的各项，随内容决定每一项占多少行，默认各项内容垂直居中，用`vertical-align`调节垂直对齐。

```html
<style>
    table {
        width: 宽度;
        table-layout: fixed;
    }
    td, th {
        word-wrap: break-word;
        /*vertical-align: top;*/
    }
    .piece_1 {
        width: 固定宽度1;
    }
    .piece_2 {

    }
    .piece_3 {
        width: 固定宽度3;
    }
    .piece_4 {
        width: 固定宽度4;
    }
</style>

<table>
    <tbody>
    <tr>
        <td class="piece_1">
            固定宽度内容1
        </td>
        <th class="piece_2">
            自适应宽度内容2
        </th>
        <td class="piece_3">
            固定宽度内容3
        </td>
        <td class="piece_4">
            固定宽度内容4
        </td>
    </tr>
    ...
    </tbody>
</table>
```

### 使元素强制表现为`block`的css设置
1. `float: left/right;`
2. `position: absolute/fixed;`

>意味着有以上css属性的内联标签可以当做块级标签使用。

### 单词内断字换行
1. ~~默认~~：
    *若此行放不下则整个单词换行，若下行也放不下则溢出（保持单词不断词）。*
2. ~~`word-break: break-all;`~~：
    *若此行放不下则直接断词，不会尝试整个单词换行。*
3. `word-wrap: break-word;`：
    若此行放不下则整个单词先换行，若下行也放不下再断词。

### 块级元素的width
1. `width: auto;`：
    默认值，换算具体值为：**本元素width = 父级width - 本元素（margin + padding + border）水平值**。

    >当块级width为默认的auto时，设置负的水平margin会使width增加。
2. `width: 100%;`：
    父级的px为自己的px。

### margin合并
>[W3C]In CSS, the adjoining margins of two or more boxes (which might or might not be siblings) can combine to form a single margin. Margins that combine this way are said to collapse, and the resulting combined margin is called a collapsed margin.

- 在CSS中，两个或多个毗邻（父子元素或兄弟元素）的普通流中的块元素垂直方向上的margin会发生叠加。这种方式形成的外边距即可称为外边距叠加（collapsed margin）。

    >- 毗邻：是指没有被**非空内容**、**padding**、**border**或**clear**分隔开。
    >- 普通流：除**浮动（float）**、**绝对定位（absolute）**外的代码。
- 产生独立的BFC结构可避免margin合并

>ie6、7触发haslayout会影响margin合并的发生。

### BFC（Block Formatting Context）块级格式上下文
- W3C定义：

    浮动元素和绝对定位元素，非块级盒子的块级容器（例如 inline-blocks、table-cells、和table-captions），以及overflow值不为“visiable”的块级盒子，都会为他们的内容创建新的块级格式化上下文。

    在一个块级格式化上下文里，盒子从包含块的顶端开始垂直地一个接一个地排列，两个盒子之间的垂直的间隙是由他们的margin 值所决定的。两个相邻的块级盒子的垂直外边距会发生叠加。

    在块级格式化上下文中，每一个盒子的左外边缘（margin-left）会触碰到容器的左边缘（border-left）（对于从右到左的格式来说，则触碰到右边缘），即使存在浮动也是如此，除非这个盒子创建一个新的块级格式化上下文。

    >- [W3C]Floats, absolutely positioned elements, block containers (such as inline-blocks, table-cells, and table-captions) that are not block boxes, and block boxes with ‘overflow’ other than ‘visible’ (except when that value has been propagated to the viewport) establish new block formatting contexts for their contents.
    >- In a block formatting context, boxes are laid out one after the other, vertically, beginning at the top of a containing block. The vertical distance between two sibling boxes is determined by the ‘margin’ properties. Vertical margins between adjacent block-level boxes in a block formatting context collapse.
    >- In a block formatting context, each box’s left outer edge touches the left edge of the containing block (for right-to-left formatting, right edges touch). This is true even in the presence of floats (although a box’s line boxes may shrink due to the floats), unless the box establishes a new block formatting context (in which case the box itself may become narrower due to the floats).

- BFC是一个独立的布局环境，可以理解为一个箱子，箱子里面物品的摆放不受外界的影响，并且每个BFC都遵守同一套布局规则。
- 对容器添加以下css属性使其成为独立的BFC
    1. `float: left / right;`
    2. `overflow: hidden / auto / scroll;`
    3. `display: inline-block / table-cell / table-caption / flex / inline-flex;`
    4. `position: absolute / fixed;`

>ie6、7不支持BFC，但是有haslayout。

### `word-spacing`
对有空白字符包裹的非空白字符产生效果。

### `z-index`用于控制设置了absolute、relative或fixed定位的元素
应该只给有堆叠关系的节点设置此属性，而不要试图通过设定个别元素的z-index来确保元素不重叠。

### css的小数、百分比
1. 浏览器会把小数以及百分比换算成整数的单位（px）

    - 四舍五入：ie8 ie9 chrome firefox
    - 直接向下取整：ie7 safari

2. 多个子节点浮动的总宽度接近100%会表现成100%

    根据[Bootstrap's Grid system](http://getbootstrap.com/css/#grid)的标准，设置百分比宽度时，用百分比小数点后第六位的四舍五入值可以兼容大多数浏览器：
    ```css
    .col-1, .col-2, .col-3, .col-4, .col-5, .col-6, .col-7, .col-8, .col-9, .col-10, .col-11, .col-12 {
        float: left;
        _display: inline;
    }
    .col-1 {width: 8.333333%;}
    .col-2 {width: 16.666667%;}
    .col-3 {width: 25%;}
    .col-4 {width: 33.333333%;}
    .col-5 {width: 41.666667%;}
    .col-6 {width: 50%;}
    .col-7 {width: 58.333333%;}
    .col-8 {width: 66.666667%;}
    .col-9 {width: 75%;}
    .col-10 {width: 83.333333%;}
    .col-11 {width: 91.666667%;}
    .col-12 {width: 100%;}
    ```

### `font-size`最小值
1. wap端没有最小限制
2. pc端最小限制为12px

>chrome浏览器可以设置到的最小值为6px，因此为了浏览器模拟wap时不会影响效果，wap字体不要小于6px。

### 滚动条
1. 若`overflow-x`和`overflow-y`相同，则等同于`overflow`
2. 若不同，且其中一个值为`visible`，另一个为`hidden/scroll/auto`，则`visible`重置为`auto`
3. 默认滚动条均来自`html`标签，而不是body标签。因此，除去默认滚动条应在html上设置overflow值
4. js滚动条高度为：`document.documentElement.scrollTop || document.body.scrollTop`
5. 滚动条会占用容器的可用高度或宽度

### `line-height`
1. 单行文本情况下：内联元素的高度由`line-height`决定；块级元素的高度先由`height`决定，若没有设置`height`再由`line-height`决定（ie6是`line-height`优先决定）。
2. 查看内联元素时，展示的高度（鼠标指示出的高度）为内容区域高度(height)，元素所占高度由`line-height`决定。
3. 元素高度表现为： 内容区域+行间距，刚好等于行高。

    **内容区域（content area） + 行间距（vertical spacing） = 行高（line-height）**

    >   - 内容区域：只与字号（font-size）和font-family有关
    >   - 行间距：摇摆不定，可以为负值，仅为达成以上等式而变化

>ie6不能用line-height控制图片与文字的对齐位置

### img标签的src属性
当img标签的地址为空或错误时，会出现浏览器默认灰色边框，无法去除。

1. 不要用**空的img标签加上背景来用作默认图**，必须用其他标签来代替。
2. img标签没有src属性或src属性为空隐藏

    ```css
    img[src=''] {   /* ie8+*/
        visibility: hidden; /* 属性为空隐藏*/
    }
    img:not([src]) {    /* ie9+*/
        visibility: hidden; /* 属性不存在隐藏*/
    }
    ```

### 多列等高
```css
.father {
    overflow: hidden;
}
.sons {
    padding-bottom: 9999px;
    margin-bottom: -9999px;
}
```

### 实现hover去除左右间隔效果
```css
ul {
    overflow: hidden;
}
ul li {
    float: left;
    _display: inline;
    margin-left: -1px;
}
ul li a {
    background: url(宽度根据li的margin-left、高度根据a的高度决定的border样式图片) 100% center no-repeat;
    display: block;
}
ul li a:hover {
    background: 背景色;
}
```

>hover之后本身的背景被替换，前一个兄弟的背景被覆盖


##HTML + CSS

### 垂直居中
```html
<style type="text/css">
    .box { /* 此层不能是float或absolute，可以在此层外嵌套的设置为float或absolute*/
       display: table-cell;
       height: 114px; /* height/font-size = 1.14*/
       *font-size: 100px;
       vertical-align: middle; /* 无继承性*/
       text-align: center; /* 有继承性*/
    }
    span { /* 必须是内联元素*/
       display: inline-block;
       vertical-align: middle;
       /*font-size覆盖父级的字体*/
    }
    img {
       vertical-align: middle;
    }
</style>

<div class="box">
    <img src=""> or <span>...</span>
</div>
```

### 自适应宽度布局
1. 中间内容自适应，两边固定（中间内容先加载）

    ```html
    <style type="text/css">
        .main_out,
        .float_l,
        .float_r {
            float: left;
        }
        .middle_out {
            width: 100%;
        }
        .middle_in {
            margin: 0 大于等于右边块宽度 0 大于等于左边块宽度;
        }
        .float_l {
            width: 右边块宽度;
            margin-left: -100%;
        }
        .float_r {
            width: 左边块宽度;
            margin-left: -左边块宽度;
        }
    </style>

    <div class="clearfix">
        <div class="middle_out">
            <div class="middle_in">
                中间内容
            </div>
        </div>
        <div class="float_l">左边内容</div>
        <div class="float_r">右边内容</div>
    </div>
    ```

    >- DOM结构不能颠倒，需要中间结构放最前;
    >- 节点上能设定`clear: both;`。

2. 中间内容自适应，两边固定（中间内容后加载）

    ```html
    <style type="text/css">
        .float_l {
            float: left;
            width: 左边块宽度;
        }
        .float_r {
            float: right;
            width: 右边块宽度;
        }
        .middle {
            margin-left: 大于等于左边块宽度;
            margin-right: 大于等于右边块宽度;
        }
    </style>

    <div class="clearfix">
        <div class="float_l">左边内容</div>
        <div class="float_r">右边内容</div>
        <div class="middle">中间内容</div>
    </div>
    ```

    >- DOM结构不能颠倒，需要中间结构放最后;
    >- 节点上能设定`clear: both;`。
    >
    >float属性的节点可以填补在之后节点的水平margin区域内，padding区域内不可以；
    >不可以填补于之前节点的水平margin区域内。

3. 中间与两边内容都自适应

    ```html
    <style type="text/css">
        .float_l {
            float: left;
            _display: inline;
        }
        .float_r {
            float: right;
            _display: inline;
        }
        .middle {
            display: table-cell;
            *display: inline-block;
            width: 9999px;
            *width: auto;
        }
    </style>

    <div class="clearfix">
        <div class="float_l">左边内容</div>
        <div class="float_r">右边内容（没有足够空间则整体换行）</div>
        <div class="middle">中间内容（没有足够空间则整体换行）</div>
    </div>
    ```

    >- DOM结构不能颠倒，需要中间结构放最后;
    >- 节点上能设定`clear: both;`;
    >- 完全由内容决定布局；
    >- 第一块内容要给第二块内容留下足够空间，否则第二块放不下会整个换行；第一块+第二块要给第三块留下足够空间，否则第三块放不下会整个换行。

### 内容居中
1. 内容宽度可变，三层模式

    ```html
    <style>
        .outer_1 {
            text-align: center;
        }
        .inner {
            display: inline-block;
            *display: inline;
            zoom: 1;
        }
        .float_1 {
            float: left;
        }
    </style>

    <div class="outer_1">
        <div class="inner clearfix">
            <div class="float_1">...</div>
            <div class="float_1">...</div>
            <div class="float_1">...</div>
        </div>
    </div>
    ```
2. 内容宽度固定，二层结构

    ```html
    <style>
    .outer_2 {
        width: 总宽度;
        margin: 0 auto;
    }
    .float_2 {
        float: left;
        background: yellow;
        width: 单个宽度;
    }
    </style>

    <div class="outer_2 clearfix">
        <div class="float_2">...</div>
        <div class="float_2">...</div>
        <div class="float_2">...</div>
    </div>
    ```

### 翻转效果（ie9+及高级浏览器）
```html
<style type="text/css">
    .item {
        position: relative;
        display: inline-block;
        *display: inline;
        zoom: 1;
    }
    .front {
        backface-visibility: hidden;
        transition: 1s;
        transform: rotateY(0deg);
    }
    .back {
        backface-visibility: hidden;
        transition: 1s;
        transform: rotateY(180deg);
        position: absolute;
        top: 0;
    }
    .item:hover .front {
        transform: rotateY(180deg);
    }
    .item:hover .back {
        transform: rotateY(360deg);
    }
</style>

<div class="item">
    <div class="front">
        <img>
    </div>
    <div class="back">
        <img>
    </div>
</div>
```

### 复杂背景切图
1. （背景不透明情况）背景不规则，内容贯穿背景

    1. 上下级结构

        ```html
        <style type="text/css">
            .main {
                width: 宽度;
                overflow: hidden;
            }
            .top {
                background: url(背景图) 0 0 no-repeat; /* 横版背景图，分别从左到右是头部、中间、底部内容*/
                height: 高度1;
            }
            .content_3 {
                background: url(背景图) -宽度 0 repeat-y;
            }
            .content_2 {
                position: relative;
                top: -高度2;
                zoom: 1;
            }
            .content_1 {
                position: relative;
                margin-bottom: -2*高度2;
            }
            .bottom {
                background: url(背景图) -2*宽度 0 no-repeat;
                height: 高度1;
            }
        </style>

        <div class="main">
            <div class="top"></div>
            <div class="content_3">
                <div class="content_2">
                    <div class="content_1">
                        内容
                    </div>
                </div>
            </div>
            <div class="bottom"></div>
        </div>
        ```
    2. 层层覆盖

        ```html
        <style type="text/css">
            .main {
                width: 宽度;
            }
            .out {
                background: url(背景图) 0 0 repeat-y;    /* 横版背景图，分别从左到右是头部、中间、底部内容*/
            }
            .middle {
                background: url(背景图) -宽度 0 no-repeat;
            }
            .in {
                background: url(背景图) -2*宽度 bottom no-repeat;
            }
        </style>

        <div class="main">
            <div class="out"><!-- 中间平铺的背景-->
                <div class="middle"><!-- 头部背景（覆盖中间背景）-->
                    <div class="in"><!-- 底部背景（覆盖头部以及中间背景）-->
                        内容
                    </div>
                </div>
            </div>
        </div>
        ```
2. （背景可透明情况）背景不规则，内容不贯穿背景

    ```html
    <style type="text/css">
        .main {
            width: 宽度;
        }
        .top {
            background: url(背景图) 0 0 no-repeat; /* 横版背景图，分别从左到右是头部、中间、底部内容*/
            height: 高度;
        }
        .content {
            background: url(背景图) -宽度 0 repeat-y;
        }
        .bottom {
            background: url(背景图) -2*宽度 0 no-repeat;
            height: 高度;
        }
    </style>

    <div class="main">
        <div class="top"></div>
        <div class="content">
            内容
        </div>
        <div class="bottom"></div>
    </div>
    ```

### 等宽文字
要做到不同字数的一行文字等宽，可以用标签填补中间间隙。

```html
<style type="text/css">
    i {
        display: inline-block;
        *display: inline;
        zoom: 1;
        width: 1em;
    }
</style>

<标签>文字文字</标签>
<标签>文<i></i><i></i>字</标签>
```

### 标签溢出则换行隐藏、不截断
```html
<style>
    .test {
        height: 高度;
        line-height: 高度;
        /* white-space: nowrap; */
        text-overflow: ellipsis;
        overflow: hidden;
    }
    .test span {
        display: inline-block;
        *display: inline;
        *zoom: 1;
    }
</style>

<div class="test">
    内容
    <span>超出内容不截断，而是换行隐藏</span>
    <span>超出内容不截断，而是换行隐藏</span>
    <span>超出内容不截断，而是换行隐藏</span>
    <span>超出内容不截断，而是换行隐藏</span>
</div>
```
>无法出现`...`效果。

### 实现hover之后底部border替换父级border
```css
ul {
    height: 高度;
    border-bottom: 1px solid 父级颜色;
    /* 不能overflow: hidden;*/
}
li {
    width: 宽度;

    height: 高度+1;
    float: left;
    _display: inline;
}
a {
    width: 宽度;
    /* 不能background*/

    height: 高度+1;
    margin-bottom: -1px;
    display: block;
    _position: relative;
}
li.hover a,
li:hover a {
    height: 高度; /* 若border要超过原来的父级border，这里高度减少多少，下面border-bottom就增加多少*/
    border-bottom: 1px solid 子级颜色;
    _border-bottom: 2px solid 子级颜色;
}
```

### 页面高度不够时，footer依然置于页面最底部
1. 兼容大部分情况

    ```html
    <style type="text/css">
        html,
        body {
            height: 100%;
        }
        .content {
            min-height: 100%;
            height: auto !important;
            _height: 100%;
        }
        .last_content {
            padding-bottom: 底部高度;
        }
        .footer {
            margin-top: -底部高度;
            height: 底部高度;
        }
    </style>

    <div class="content">
        内容
        <div class="last_content">内容</div>
    </div>
    <div class="footer">底部内容</div>
    ```
2. *ie6中，当.last_container高度变化的时候会渲染错误*

    ```html
    <style type="text/css">
        html,
        body {
            height: 100%;
        }
        .wrapper {
            position: relative;
            height: auto !important;
            min-height: 100%;
            _height: 100%;
        }
        .last_container {
            padding-bottom: 底部高度;
        }
        .footer {
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            _width: 100%;
            height: 底部高度;
        }
    </style>

    <div class="wrapper">
        内容
        <div class="last_container">内容</div>
        <div class="footer">底部内容</div>
    </div>
    ```

>有些插件效果不能支持`html,body {height: 100%;}`。

### img标签的圆形边框
1. 圆形+边框

    1. pc

        直接在img标签上设置`border`和`border-radius`。
    2. wap

        在img标签上设置`border`和`border-radius`，并且在父级标签嵌套一层设置`border`和`border-radius`。
2. 圆形（无边框）

    - pc+wap

        直接在img标签上设置`border-radius`。

### css3的`animation`使用
> 动画进行到一半取消动画（去除了相关类）或者替换动画，会导致节点突兀地回到初始位置。

1. 用`:hover`触发

2. 在使用`animation`节点（或父节点）上加入两种状态的类，一个控制启动时的动画效果，一个控制关闭时的动画效果

    ```html
    <style>
        .dom {
            animation-duration: 1s;
            animation-iteration-count: 1;
        }
        .dom.fade_in {
            animation-name: in;
        }
        .dom.fade_out {
            animation-name: out;
        }
        @keyframes in {

        }
        @keyframes out {

        }
    </style>

    <div class="dom j-dom">...</div>

    <script>
        $(document).on('mouseenter', '.j-dom', function () {
            $('.j-dom').addClass('fade_in').removeClass('fade_out');
        }).on('mouseleave', '.j-dom', function () {
            $('.j-dom').addClass('fade_out').removeClass('fade_in');
        });
    </script>
    ```

3. 监听动画结束事件，在结束时候再去除动画

    ```html
    <style>
        .dom {

        }
        .dom.hover {
            animation: act 1s infinite;
        }
        @keyframes act {

        }
    </style>

    <div class="dom j-dom">...</div>

    <script>
        var animationHover = {
            isStop: false,
            init: function (selector, hoverClass) {
                var $dom = $(selector),
                    self = this;

                $dom.on('mouseover', function () {
                    $(this).addClass(hoverClass);

                    self.isStop = false;
                }).on('mouseout', function () {
                    self.isStop = true;
                }).on('animationiteration', function () {    /* css的animation结束触发*/
                    if (self.isStop) {
                        $dom.removeClass(hoverClass);

                        self.isStop = false;
                    }
                });
            }
        };
        animationHover.init('.j-dom', 'hover');
    </script>
    ```

### 禁用`a`标签鼠标、键盘事件
1. `pointer-events: none;`穿透`a`标签的鼠标事件（包括点击和hover等）。
2. 不设置`href`属性，可以忽略键盘索引（tab键无法切换到）。

```html
<a style="pointer-events: none;">禁用鼠标和键盘的链接</a>
```

### 横竖屏切换
1. 用js方法控制：[链接](../js方法积累/实用方法/README.md#jquery或Zepto模拟手机翻转使页面都以横屏展示)
2. 媒体查询控制

    ```css
    @media (orientation: portrait) {
        .dom {
            transform: rotate(90deg);
        }
    }
    @media (orientation: landscape) {
        .dom {

        }
    }
    ```

>横竖屏切换后2种状态的不同设置
>
>```css
>/* 当竖屏时用屏幕高度来判断*/
>@media (min-height: ) and (max-height: ) and (orientation: portrait) {
>    html {
>        font-size: ;
>    }
>}
>/* 当横屏时用屏幕宽度来判断*/
>@media (min-width: ) and (max-width: ) and (orientation: landscape) {
>    html {
>        font-size: ;
>    }
>}
>```

### 移动端制作类似pc端的`:active`效果（或`:hover`）
1. android系统的浏览器大部分直接使用css伪类即可。
2. ios系统的浏览器要添加以下代码触发使css伪类生效：

    ```javascript
    document.body.addEventListener('touchstart', function () {}, true);
    ```
3. ~~js添加类的方法替代~~：

    ```html
    <style>
        .d:active,
        .d.active { }
    </style>

    <script type="text/javascript">
        var selector = '.a,.b .c,.d';   /* 选择器字符串*/

        $(document.body).on("touchstart", selector, function () {
            $(this).addClass("active");
        }).on("touchmove touchend touchcancel", selector, function () {
            $(this).removeClass("active");
        });
    </script>
    ```
    >仅用来补充`.d:hover {-webkit-tap-highlight-color:rgba( , , , );}`。


##经验总结

### 响应式设计
- 媒体查询方式
    1. css属性：

        `@media (min-width: 360px) and (max-width: 640px) {...}`
    2. html标签：

        `<link rel="stylesheet" type="text/css" media="(min-width: 360px) and (max-width: 640px)" href="...">`
- 响应式设计三大要素
    1. 媒体查询
    2. 流式布局：节点用百分比或rem
    3. 弹性图片：`img {max-width: 100%;}`

### 响应式页面解决方案：使用rem单位+媒体查询
>- rem（font size of the root element）：相对于根元素的字体大小的单位。
>- rem单位转换为具体px值：**rem乘于html的font-size像素**。

1. 媒体查询设置html的font-size，把要做成响应式的内容转换为rem单位。

    1. *不需要使用css预处理语言的不全面方法*：

        1. 正常完成切图（只能用正常的320px设计稿切完图），用px作为单位。
        2. 媒体查询仅设置html的不同情况下的font-size值。
        3. 把css内需要响应式内容的px值，除以**在320px宽度下的html的font-szie值**（320px宽度时设置为10px方便计算，设置为小于6px不起作用），单位改为rem。

        >仅需要把要响应式布局的内容进行转变
    2. 需要使用css预处理语言的最优解：

        1. 正常完成切图（可以用大于320px设计稿切完图），大小值用**调用传入参数（设计稿是多大px就用多大值作为参数）的返回值**。
        2. 媒体查询仅设置html的不同情况下的font-size值。
        3. 调用的方法：返回 **参数**除以**在320px宽度下的html的font-szie值**再除以**2（设计稿放大倍数）**。如果设计稿大于320px并且想要最低适配至320px屏幕，这里返回的参数要再缩小一些。
        4. 用预处理语言生成为css文件，其中所有单位都为rem。

        >整个页面都是用rem进行制作。
2. *用js根据是否是苹果设备进行判断：若是苹果设备则viewport设置为0.5，html的font-size设置为2倍；若非苹果设备则viewport设置为1，html的font-size设置为1倍*

    ```javascript
    var fontSize = 10;

    /* 实现根据iOS和Android不同设备设置不同的viewport*/
    if ((/iphone|ipad|ipod/i).test(navigator.appVersion) && window.devicePixelRatio >= 2) {
        document.getElementById('j-viewport').content = 'width=device-width, initial-scale=0.5, user-scalable=no, minimum-scale=0.5, maximum-scale=0.5';
        document.documentElement.style.fontSize = 2 * fontSize + "px";
    } else {
        document.getElementById('j-viewport').content = 'width=device-width, initial-scale=1, user-scalable=no, minimum-scale=1, maximum-scale=1';
        document.documentElement.style.fontSize = fontSize + "px";
    }
    ```

    >因为html的font-size是用js写死的，而且viewport会变化，所以所有页面元素都要用百分比+rem。
3. *用js根据浏览器宽度的改变修改html的font-size，页面总宽度固定为某rem。所有页面元素都要用百分比+rem*

### 限定布局宽度，让内容决定布局高度

### 富文本
1. 富文本内容除了要检测用户输入标签的闭合性，还要注意**不要用`li`标签嵌套富文本**，因为代码中如果有单独的`li`（没有嵌套`ol`或`ul`），就会“升级”到跟祖先级li同级的内容。

2. 部分富文本会用标签`em`、`ol`、`ul`来表示**斜体**、**有序序列**、**无序序列**，因此如果用css重置了以上标签后，要在富文本内重载开启它们的默认效果；

3. 部分富文本还会在`table`标签上使用`cellspacing`、`border`、`bordercolor`属性来设置表格，又因为设置了`border: 0;`的表格标签无法重载开启以上属性作用，所以css重置时不要重置`table,tbody,tfoot,thead,tr,th,td`的`border`属性。

### 超出内容区域的内容
1. 用绝对定位把内容设置在外部

    不要把超出内容区域的绝对定位设置在`body`直接子级，而是设置在`body`下拥有`overflow: hidden;width: 100%;/* 默认*/`的父级下。
2. ~~用大背景模式~~

### html请求资源：
页面是按照顺序加载资源，当且仅当有使用需求时才会去加载外部资源。

比如已加载完成的css文件内有多个url请求（background），但也仅在页面要用到某个url请求时（比如某类有url背景），才会去请求这个资源，而不是在加载css文件时就加载外部资源。

### 知识点
1. a标签的属性`target="_blank"`，在一些浏览器中，无论`href`值是什么内容（包括#和javascript: void(0);）都会打开新的页面。
2. `absolute`元素用`top: 0; bottom: 0; left: 0; right: 0; _height: 100%; _width: 100%;`可以拉伸至父容器的高宽。
3. 没有设置宽度的`float`元素，其宽度等于子节点宽度：主流浏览器等于最外层子节点宽度，ie6等于所有子节点中最大的宽度。
4. `inline`或`inline-block`节点标签前可能导致其父级的宽度变大（其实是内联标签前面会有间隙，若拥有`font-size`之后便会有高度撑开），通过以下办法解决：

    1. 把`inline`节点设置为`block`。
    2. 给父级节点设置`font-size: 0;`（可用此方法排查是否是空格造成的）。

### 前端技巧
- 经验

    1. 标签语义化。

        先用纯html标签语义化结构，再加入css满足样式，最后加入交互

        >1. 不要全用div标签；用ul>li、ol>li、dl>dt来代替p标签。
        >2. h1~h5标签不要根据其字体大小的不同来使用，应该根据页面内的重要程度来使用（SEO）。
    2. 减少层级嵌套，合理嵌套，行内元素不要嵌套块级元素（如a标签不嵌套div）
    3. 用父节点的class去管理子节点
    4. 移动端大部分是webkit内核浏览器，因此可以使用较新的技术，如css3；pc端要适配到ie6
    5. js用变量保存下已经使用过的DOM对象
- 《高性能网站建设指南》自我总结

    1. 减少HTTP请求，图片以及外链资源的优化，包括压缩与整合，服务器开启g-zip等（不要压缩图片与PDF，因为它们本身已经被压缩，再压缩可能会增加文件大小；压缩都耗费CPU）
    2. 图片的处理，包括压缩、大banner切分成多个小图、小图合并成雪碧图、图片的延迟加载
    3. 不要缩小放大图片（使用原始大小展现）
    4. 使用内容发布网络CDN
    5. 添加Expires报头（设置网页在浏览器中缓存过期时间）；配置ETags报头（用来验证浏览器缓存和原服务器上内容是否一致）
    6. 浏览器为了避免当样式变化时重绘页面中的元素，会阻塞页面内容的逐步呈现，样式表之前的内容和JS脚本之后的内容都会因为这些文件的下载而阻塞呈现
    7. 不要使用~~`@import`~~，只用`<link>`
    8. 避免~~css表达式（CSS expression）~~
    9. 虽然内联css和js比外部文件快，但只有外部的才可能被浏览器缓存
    10. 减少DNS查找，设置合适的TTL值
    11. 避免重定向（`http://a.com/folder`会重定向到`http://a.com/folder/`，但根目录`http://a.com`不会发生重定向）
    12. 使Ajax可缓存（服务端的CDN缓存，可用jQuery的$.Ajax的cash属性设置为false，或url加时间戳，来避免缓存）
    13. 避免使用不可缓存且是外部HTTP请求的iFrame