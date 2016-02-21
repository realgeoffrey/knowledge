##CSS
### 使元素强制表现为`block`
- `float: left/right;`
- `position: absolute/fixed;`

### 用css创造三角形
```css
div {
    border-width: 20px;
    border-style: dashed solid dashed dashed; /* dashed兼容ie6不支持透明*/
    border-color: transparent #000 transparent transparent;
    height: 0;
    width: 0;
    _overflow: hidden;
}
```

> 两个同样大小的三角形，第二个设置为背景色并且覆盖到第一个上面，可以模拟箭头**>**

### 清除浮动：
- 在父级设置

    ```css
    .clearfix:after {
       display: block;
       clear: both;
       content: ".";
       visibility: hidden;
       height: 0;
    }
    .clearfix {
       zoom: 1;
    }
    ```
- 截断不影响时，在父级设置

    ```css
    .father {
        overflow: hidden;
        _width: 100%;
    }
    ```

>部分浏览器设置`clearfix`，会导致`:after`的内容有占高宽，必须使用`overflow: hidden;`代替使用

### 单行文本和多行文本超出宽度显示省略号
```css
.ellipsis { /* 单行*/
    _width: 100%;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}
.multi_ellipsis {   /* 多行*/
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

### 单词内断字换行
- ~~默认~~：
    若此行放不下则整个单词换行，若下行也放不下则溢出（保持单词不断词）
- ~~`word-break: break-all;`~~：
    若此行放不下则直接断词，不会尝试整个单词换行
- `word-wrap: break-word;`：
    若此行放不下则整个单词先换行，若下行也放不下再断词

### 块级元素的width
- `width: auto;`：
    默认值，换算具体值为：**本元素width = 父级width - 本元素（margin + padding + border）水平值**

    >当块级width为默认的auto时，设置负的水平margin会使width增加
- `width: 100%;`：
    父级的px为自己的px

### margin合并（非ie浏览器）
>[W3C]In CSS, the adjoining margins of two or more boxes (which might or might not be siblings) can combine to form a single margin. Margins that combine this way are said to collapse, and the resulting combined margin is called a collapsed margin.

- 在CSS中，两个或多个毗邻（父子元素或兄弟元素）的普通流中的块元素垂直方向上的margin会发生叠加。这种方式形成的外边距即可称为外边距叠加（collapsed margin）。

    >毗邻：是指没有被**非空内容**、**padding**、**border**或**clear**分隔开

    >普通流：除**浮动（float）**、**绝对定位（absolute）**外的代码
- 产生独立的BFC结构可避免margin合并

### BFC（Block Formatting Context）块级格式上下文
>- [W3C]Floats, absolutely positioned elements, block containers (such as inline-blocks, table-cells, and table-captions) that are not block boxes, and block boxes with ‘overflow’ other than ‘visible’ (except when that value has been propagated to the viewport) establish new block formatting contexts for their contents.
>- In a block formatting context, boxes are laid out one after the other, vertically, beginning at the top of a containing block. The vertical distance between two sibling boxes is determined by the ‘margin’ properties. Vertical margins between adjacent block-level boxes in a block formatting context collapse.
>- In a block formatting context, each box’s left outer edge touches the left edge of the containing block (for right-to-left formatting, right edges touch). This is true even in the presence of floats (although a box’s line boxes may shrink due to the floats), unless the box establishes a new block formatting context (in which case the box itself may become narrower due to the floats).

- 浮动元素和绝对定位元素，非块级盒子的块级容器（例如 inline-blocks、table-cells、和table-captions），以及overflow值不为“visiable”的块级盒子，都会为他们的内容创建新的块级格式化上下文。

    在一个块级格式化上下文里，盒子从包含块的顶端开始垂直地一个接一个地排列，两个盒子之间的垂直的间隙是由他们的margin 值所决定的。两个相邻的块级盒子的垂直外边距会发生叠加。

    在块级格式化上下文中，每一个盒子的左外边缘（margin-left）会触碰到容器的左边缘（border-left）（对于从右到左的格式来说，则触碰到右边缘），即使存在浮动也是如此，除非这个盒子创建一个新的块级格式化上下文。
- BFC是一个独立的布局环境，可以理解为一个箱子，箱子里面物品的摆放不受外界的影响，并且每个BFC都遵守同一套布局规则。
- 对容器添加以下css属性使其成为独立的BFC
    - `float: left / right;`
    - `overflow: hidden / auto / scroll;`
    - `display: inline-block / table-cell / flex / table-caption / inline-flex;`
    - `position: absolute / fixed;`

### word-spacing
对有空白字符包裹的非空白字符产生效果。

### z-index用于控制设置了absolute、relative或fixed定位的元素
应该只给有堆叠关系的节点设置此属性，而不要试图通过设定个别元素的z-index来确保元素不重叠。

### 模糊效果滤镜（高斯模糊）
- CSS3（除*ie10*与*ie11*外基本所有主流浏览器）

    ```css
    .filter {
        -webkit-filter: blur(10px);
        -moz-filter: blur(10px);
        -ms-filter: blur(10px);
        filter: blur(10px);
        filter: progid:DXImageTransform.Microsoft.Blur(PixelRadius=10, MakeShadow=false); /* ie6~ie9 */
    }
    ```
- SVG（较新版本的FireFox、Chrome、Opera）

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

- canvas

    （待续）

### css的小数
浏览器会把小数以及百分比换算成整数的单位（px）
- 四舍五入：ie8 ie9 chrome firefox
- 直接向下取整：ie7 safari

>有些浏览器会出现一列百分比相加为100%的节点换算之后无法占满整列

### font-size最小值
- wap端没有最小限制
- pc端最小限制为12px

### img标签的src属性
当img标签的地址为空或错误时，会出现浏览器默认灰色边框，无法去除。
- 不要用~~空的img标签加上背景来用作默认图~~，必须用其他标签来代替。
- img标签没有src属性或src属性为空隐藏

    ```css
    img[src=''] {   /* ie8+*/
        visibility: hidden; /* 属性为空隐藏*/
    }
    img:not([src]) {    /* ie9+*/
        visibility: hidden; /* 属性不存在隐藏*/
    }
    ```

### inline-block元素之间或与文本的水平对齐
并排排列的不同元素间，若不使用float，而使用inline-block
- 非img标签

    ```css
    标签 {
        display: inline-block;
        *display: inline;
        zoom: 1;
        height: 宽;
        width: 高;
        vertical-align: bottom;
        *vertical-align: middle;
    }
    ```
- img标签

    ```css
    img {
        display: inline-block;
        *display: inline;
        zoom: 1;
        height: 宽;
        width: 高;
        vertical-align: middle;
    }
    ```

### 滚动条
- 若`overflow-x`和`overflow-y`相同，则等同于`overflow`
- 若不同，且其中一个值为`visible`，另一个为`hidden/scroll/auto`，则`visible`重置为`auto`
- 默认滚动条均来自`html`标签，而不是body标签。因此，除去默认滚动条应在html上设置overflow值
- js滚动条高度为：`document.documentElement.scrollTop || document.body.scrollTop`
- 滚动条会占用容器的可用高度或宽度

### 移动端半像素
不可以使用`border: 0.5px`，因为浏览器会把宽度换算成0或者1

1. 整个边框0.5px

    ```css
    div {
        width: 宽度;
        position: relative;
    }
    div:before {
        position: absolute;
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
        content: "";
        width: 100%;
        height: 1px;
        border-top: 1px solid 颜色;
        transform: scaleY(.5);
        transform-origin: 0 0;
        box-sizing: border-box;
    }
    ```

### 内阴影效果
```css
div {
    box-shadow: 0 -2px 0 0 颜色 inset;  /* 左右偏移 上下偏移 模糊 尺寸*/
    border-radius: 5px;
}
```

### wap页面自适应图片
图片根据浏览器窗口变化而宽高一同等比例变化，不使用`img`标签
- 横向、纵向百分比的`padding`（和`margin`）值都是以父元素的`width`为基础，`height`是以父元素的`height`为基础

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
- 宽高都用rem（与html的font-size配合）
    - 单图

        ```css
        自适应图片 {
            width: 宽rem;
            height: 高rem;
            background-size: 100%;
            background: url(单图) 0 0 no-repeat;
        }
        ```
    - 雪碧图

        ```css
        自适应图片 {
            width: 宽rem;
            height: 高rem;
            background-size: 雪碧图宽rem;
            background: url(雪碧图) 0 -纵轴rem no-repeat;
        }
        ```
- 雪碧图并且`background-position`用百分比

    >百分比公式：
    >   - **横向百分比数值 = 小图横坐标 / ( 大图宽度 - 小图宽度 ) \* 100%**
    >   - **纵向百分比数值 = 小图纵坐标 / ( 大图高度 - 小图高度 ) \* 100%**

    - 百分比宽高

        ```css
            自适应图片 {
                height: 0;
                width: 宽%;
                padding-bottom: 高%;
                background-size: 雪碧图宽/单图宽度*100%;
                background: url(雪碧图) 0 计算出的百分比 no-repeat;
            }
        ```
    - rem宽高

        ```css
        自适应图片 {
            width: 宽rem;
            height: 高rem;
            background-size: 雪碧图宽rem;
            background: url(雪碧图) 0 计算出的百分比 no-repeat;
        }
        ```

### `table-layout: fixed;`
由第一行td或th的宽度来确定此table元素内的布局
```css
table {
    table-layout: fixed;
    width: 宽度;
}
td,th {
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}
.first {
    width: 第一列宽度;
}
.second {
    width: 第二列宽度;
}
...
```
>若`table-layout`使用默认值`automatic`，则td或th上设置宽度无效，列的宽度由列单元格中没有折行的最宽的内容决定

### `line-height`
- 单行文本情况下：内联元素的高度由`line-height`决定；块级元素的高度先由`height`决定，若没有设置`height`再由`line-height`决定（ie6是`line-height`优先决定）。
- 查看内联元素时，展示的高度（鼠标指示出的高度）为内容区域高度(height)，元素所占高度由`line-height`决定。
- 元素高度表现为： 内容区域+行间距，刚好等于行高。
    **内容区域（content area） + 行间距（vertical spacing） = 行高（line-height）**
        - 内容区域：只与字号（font-size）和font-family有关
        - 行间距：摇摆不定，可以为负值，仅为达成以上等式而变化

>ie6不能用line-height控制图片与文字的对齐位置

##HTML + CSS
### 垂直居中
```html
<div class="box">
    <img src=""> or <span>...</span>
</div>
```
```css
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
    margin-left: -1px;
}
ul li a {
    background: url(与li的margin-left大小一致的border样式图片) 100% center no-repeat;
}
ul li a:hover {
    background: 背景色;
}
```

>hover之后本身的背景被替换，前一个兄弟的背景被覆盖

### 自适应宽度布局
1. 中间内容自适应，两边固定（中间内容先加载）

    ```html
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
    ```css
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
    ```

    >DOM结构不能颠倒，需要中间结构放最前;
    >节点上能设定`clear: both;`。

2. 中间内容自适应，两边固定（中间内容后加载）

    ```html
    <div class="clearfix">
        <div class="float_l">左边内容</div>
        <div class="float_r">右边内容</div>
        <div class="middle">中间内容</div>
    </div>
    ```
    ```css
    。float_l {
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
    ```

    >DOM结构不能颠倒，需要中间结构放最后;
    >节点上能设定`clear: both;`。

    >float属性的节点可以填补在之后节点的水平margin区域内，padding区域内不可以;不可以填补于之前节点的水平margin区域内。

3. 中间与两边内容都自适应

    ```html
    <div class="clearfix">
        <div class="float_l">左边内容</div>
        <div class="float_r">右边内容</div>
        <div class="middle">中间内容</div>
    </div>
    ```
    ```css
    .float_l {
        float: left;
    }
    .float_r {
        float: right;
    }
    .middle {
        display: table-cell;
        *display: inline-block;
        width: 9999px;
        *width: auto;
    }
    ```

    >DOM结构不能颠倒，需要中间结构放最后;
    >节点上能设定`clear: both;`;
    >完全由内容决定布局。


### 响应式设计之媒体查询
- css属性：
    `@media (min-width: 360px) and (max-width: 640px) {...}`
- html标签：
    `<link rel="stylesheet" type="text/css" media="(min-width: 360px) and (max-width: 640px)" href="...">`

### 响应式设计三大要素
- 媒体查询
- 流式布局：节点用百分比
- 弹性图片：`img {max-width: 100%;}`
- wap可以用rem和html的font-size配合

### wap响应式页面解决方案：使用rem单位+媒体查询
rem（font size of the root element）：相对于根元素的字体大小的单位。

rem单位转换为具体px值：**rem乘于html的font-size像素**。

1. 媒体查询设置html的font-size，把要做成响应式的内容转换为rem单位。
    1. 正常完成切图：用正常的320px设计稿切完图，用px作为单位。
    2. 媒体查询仅设置html的不同情况下的font-size值。
    3. 把css内需要响应式内容的px值，除以在320px宽度下的html的font-szie值（320px宽度时设置为10px方便计算，设置为小于6px不起作用），单位改为rem。

    >仅需要把要响应式布局的内容进行转变
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

### img标签的圆形边框

1. 圆形+边框
    - pc：直接在img标签上设置`border`和`border-radius`
    - wap：在img标签上设置`border`和`border-radius`，并且在父级标签嵌套一层设置`border`和`border-radius`
2. 圆形（无边框）
    - pc+wap：直接在img标签上设置`border-radius`

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
<div class="item">
    <div class="front">
        <img>
    </div>
    <div class="back">
        <img>
    </div>
</div>
```
```css
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
```

### 复杂背景切图
- （背景不透明情况）背景不规则，内容贯穿背景
    1. 上下级结构

        ```html
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
        ```css
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
        ```
    2. 层层覆盖

        ```html
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
        ```css
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
        ```
- （背景可透明情况）背景不规则，内容不贯穿背景

    ```html
    <div class="main">
        <div class="top"></div>
        <div class="content">
            内容
        </div>
        <div class="bottom"></div>
    </div>
    ```
    ```css
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
    ```


##经验总结
### 限定布局宽度，让内容决定布局高度

### body标签设置min-width属性为项目内容宽度（不兼容ie6）
```css
body {
   min-width: ;
}
```

### 超出内容区域的内容
1. 用绝对定位把内容设置在外部

    >在ie6、ie7情况下，绝对定位内容在右边的（左边全部兼容），会根据超出内容出现滚动条并且背景颜色无法延伸。因此当ie6、ie7情况时，可以选择当窗口宽度小于文档宽度时隐藏右边隐藏内容。
2. ~~用大背景模式~~

### html请求资源：
页面是按照顺序加载资源，当且仅当有使用需求时才会去加载外部资源。
比如已加载完成的css文件内有多个url请求（background），但也仅在页面要用到某个url请求时（比如某类有url背景），才会去请求这个资源，而不是在加载css文件时就加载外部资源。

### 高性能网站建设指南
- 标签语义化，不能全用div。先用纯html标签语义化结构，再加入css满足样式，最后加入交互
- 减少层级嵌套，合理嵌套，行内元素不要嵌套块级元素（如a标签不嵌套div）
- 用父节点的class去管理子节点
- 移动端大部分是webkit内核浏览器，因此可以使用较新的技术，如css3；pc端要适配到ie6，因此要渐进增强
- js用变量保存下已经使用过的DOM对象

----
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