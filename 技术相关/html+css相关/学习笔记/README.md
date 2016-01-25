#html+css学习笔记

##CSS
- 限定布局宽度，让内容决定布局高度。

- z-index用于控制设置了absolute、relative或fixed定位的元素。
应该只给有堆叠关系的节点设置此属性，而不要试图通过设定个别元素的z-index来确保元素不重叠。

- 用css创造三角形

    ```css
    div {
        border: 12px solid;
        border-color: transparent #000 transparent transparent;
        height: 0;
        width: 0;
    }
    ```
    > 两个同样大小的三角形,第二个设置为背景色并且覆盖到第一个上面,可以模拟箭头**>**

- 清除浮动：
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

    >部分浏览器设置`.clear:after{display: block;clear: both;content: ".";visibility: hidden;height: 0;}`，会导致:after的内容有占高宽，必须使用`overflow: hidden;`代替使用。

- 单行文本和多行文本超出宽度显示省略号

    ```css
    .ellipsis {
        _width: 100%;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }
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

- 单词内断字换行
    - ~~默认~~
    若此行放不下则整个单词换行,若下行也放不下则溢出(保持单词不断词)
    - ~~`word-break: break-all;`~~
    若此行放不下则直接断词,不会尝试整个单词换行
    - `word-wrap: break-word;`
    若此行放不下则整个单词先换行,若下行也放不下再断词

- body标签设置min-width属性为项目内容宽度(忽略ie6)

    ```css
    body {
       min-width: ;
    }
    ```

-  块级元素的width
    - `width: auto;`
    默认值,换算具体值为:**本元素width = 父级width - 本元素(margin + padding + border)水平值**
        >当块级width为默认的auto时,设置负的水平margin会使width增加
    - `width: 100%;`
        父级的px为自己的px

- margin合并(非ie浏览器)

    >In CSS, the adjoining margins of two or more boxes (which might or might not be siblings) can combine to form a single margin. Margins that combine this way are said to collapse, and the resulting combined margin is called a collapsed margin.

    - 在CSS中，两个或多个毗邻（父子元素或兄弟元素）的普通流中的块元素垂直方向上的margin会发生叠加。这种方式形成的外边距即可称为外边距叠加(collapsed margin)
        - 毗邻：是指没有被**非空内容**、**padding**、**border**或**clear**分隔开
        - 普通流：除**浮动（float）**、**绝对定位（absolute）**外的代码
    - 产生独立的BFC结构可避免margin合并

- BFC(Block Formatting Context)块级格式上下文

    >Floats, absolutely positioned elements, block containers (such as inline-blocks, table-cells, and table-captions) that are not block boxes, and block boxes with ‘overflow’ other than ‘visible’ (except when that value has been propagated to the viewport) establish new block formatting contexts for their contents.
    >In a block formatting context, boxes are laid out one after the other, vertically, beginning at the top of a containing block. The vertical distance between two sibling boxes is determined by the ‘margin’ properties. Vertical margins between adjacent block-level boxes in a block formatting context collapse.
    >In a block formatting context, each box’s left outer edge touches the left edge of the containing block (for right-to-left formatting, right edges touch). This is true even in the presence of floats (although a box’s line boxes may shrink due to the floats), unless the box establishes a new block formatting context (in which case the box itself may become narrower due to the floats).

    - 浮动元素和绝对定位元素，非块级盒子的块级容器（例如 inline-blocks, table-cells, 和 table-captions），以及overflow值不为“visiable”的块级盒子，都会为他们的内容创建新的块级格式化上下文。
    在一个块级格式化上下文里，盒子从包含块的顶端开始垂直地一个接一个地排列，两个盒子之间的垂直的间隙是由他们的margin 值所决定的。两个相邻的块级盒子的垂直外边距会发生叠加。
    在块级格式化上下文中，每一个盒子的左外边缘（margin-left）会触碰到容器的左边缘(border-left)（对于从右到左的格式来说，则触碰到右边缘），即使存在浮动也是如此，除非这个盒子创建一个新的块级格式化上下文。
    - 首先BFC是一个独立的布局环境，可以理解为一个箱子，箱子里面物品的摆放不受外界的影响,并且每个BFC都遵守同一套布局规则
    - 对容器添加以下css属性使其成为独立的BFC
        - `float: left / right;`
        - `overflow: hidden / auto / scroll;`
        - `display: inline-block / table-cell / flex / table-caption / inline-flex;`
        - `position: absolute / fixed;`

- word-spacing

    对有空白字符包裹的非空白字符(中文、英文、标点)产生效果.


##HTML + CSS
- 垂直居中

    ```html
    <div class="box">
        <img src=""> or <span>...</span>
    </div>
    ```

    ```css
    .box { /* 此层不能是float或absolute，可以在此层外嵌套*/
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

- 多列等高

    ```css
    .father {
        overflow: hidden;
    }
    .sons {
        padding-bottom: 9999px;
        margin-bottom: -9999px;
    }
    ```
    >~~部分浏览器用url跳转到某id会导致页面向上溢出~~(未复现)

- 实现hover去除左右间隔效果

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
        background: #fff;;
    }
    ```
    >hover之后本身的背景被替换,前一个兄弟的背景被覆盖

- 自适应宽度布局
    1. 中间内容自适应,两边固定(中间内容先书写)

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

        >DOM结构不能颠倒,需要中间结构放最前;
        >节点上能设定`clear: both;`.

    2. 中间内容自适应,两边固定(中间内容后书写)

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

        >DOM结构不能颠倒,需要中间结构放最后;
        >节点上能设定`clear: both;`.

        >float属性的节点可以填补于之后节点的水平margin区域内,padding区域内不可以;不可以填补于之前节点的水平margin区域内.

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

        >DOM结构不能颠倒,需要中间结构放最后;
        >节点上能设定`clear: both;`;
        >完全由内容决定布局.


- 响应式设计之媒体查询
    - css属性：
    `@media (min-width: 360px) and (max-width: 640px) {...}`
    - html标签：
    `<link rel="stylesheet" type="text/css" media="(min-width: 360px) and (max-width: 640px)" href="...">`

- 响应式设计三大要素
    - 媒体查询
    - 流式布局：节点用百分比
    - 弹性图片： `img {max-width: 100%;}`
    - wap可以用rem和html的font-size配合

- wap响应式页面解决方案:使用rem单位+媒体查询

    rem(font size of the root element):相对于根元素的字体大小的单位.
    某样式的rem转换为具体px值的换算方式为:rem值乘于html的font-size像素值.
    1. 媒体查询设置html的font-size,把要做成响应式的内容转换为rem单位.
        1. 正常完成切图:用正常的320px设计稿切完图,用px作为单位.
        2. 媒体查询仅设置html的不同情况下的font-size值.
        3. 把css内需要响应式内容的px值,除以在320px宽度下的html的font-szie值(320px宽度时设置为10px方便计算,设置为小于6px不起作用),单位改为rem.

        >仅需要把要响应式布局的内容进行转变
    2. *用js根据是否是苹果设备进行判断：若是苹果设备则viewport设置为0.5，html的font-size设置为2倍；若非苹果设备则viewport设置为1，html的font-size设置为1倍*

        ```javascript
        var fontSize = 10;

        /* 实现根据iOS和Android不同设备设置不同的viewport*/
        if ((/iphone|ipad|ipod/i).test(navigator.appVersion) && window.devicePixelRatio >= 2) {
            document.getElementById('j-viewport').content = 'width=device-width, initial-scale=0.5, user-scalable=no, minimum-scale=0.5, maximum-scale=0.5'
            document.documentElement.style.fontSize = 2 * fontSize + "px";
        } else {
            document.getElementById('j-viewport').content = 'width=device-width, initial-scale=1, user-scalable=no, minimum-scale=1, maximum-scale=1'
            document.documentElement.style.fontSize = fontSize + "px";
        }
        ```

        >因为html的font-size是用js写死的，而且viewport会变化，所以所有大小都要用百分比+rem。
    3. *用js根据浏览器宽度的改变修改html的font-size,页面总宽度固定为某rem。所有大小都要用百分比+rem*

##经验总结
- html请求资源:
    页面是按照顺序加载资源,当且仅当有使用需求时才会去加载外部资源.
比如已加载完成的css文件内有多个url请求(background),但也仅在页面要用到某个url请求时(比如某类有url背景),才会去请求这个资源,而不是在加载css文件时就加载外部资源.
