# HTML+CSS学习笔记

## CSS

### 限定布局宽度，让内容决定布局高度

### CSS选择器
1. 权重

    1. 优先级（从低到高）：

        >低等级的权重值叠加再多，也无法大于高等级的权重值（一个[反例](http://www.zhangxinxu.com/wordpress/2012/08/256-class-selector-beat-id-selector/)）。

        1. **1级**：

            元素选择器（type selectors）、伪元素选择器（pseudo-elements）。
        2. **2级**：

            类选择器（class selectors）、属性选择器（attribute selectors）、伪类选择器（pseudo-classes）。
        3. **3级**：

            ID选择器（ID selectors）。
        4. **4级**

            内嵌样式（标签的`style`属性值）。
        5. **5级**

            `!important`。

        - 不改变权重：

            `*`、关系符号（`,`、` `、`>`、`+`、`~`）、`:not()`。
    2. 原则：

        1. 元素应用属性值规则：

            1. 应用**权重大的**。
            2. 权重相等，应用**文档顺序最后的**（外联和内联也按文档顺序排列）。

            - 不影响应用：

                1. ~~元素在文档的位置、选择器间的距离。~~

                    >e.g. `body h1`与`html h1`权重相同，仅取决于样式顺序。
                2. ~~样式相对于元素的位置。~~

                    >e.g.
                    >```html
                    ><style>
                    >    /*权重相同，仅取决于样式顺序*/
                    >    .a p {color: red;}
                    >    .b p {color: blue;}
                    ></style>
                    >
                    ><div class="a">
                    >    <div class="b">
                    >        <p>.a -> .b -> p:blue</p>
                    >    </div>
                    ></div>
                    ><div class="b">
                    >    <div class="a">
                    >        <p>.b -> .a -> p:blue</p>
                    >    </div>
                    ></div>
                    >```
        2. 优先级基于形式，而不是结果。

            >e.g. `[id=foo]`依然是属性选择器优先级（2级），而不是~~ID选择器优先级（3级）~~。
2. 性能

    >CSS选择器对性能的影响源于**浏览器匹配选择器和文档元素时所消耗的时间**。

    1. 样式系统**从右向左**进行规则匹配

        1. 只要当前选择符的左边还有其他选择符，样式系统就会继续向左移动，直到找到和规则匹配的元素或因为不匹配而退出。
        2. 选择器最右边的选择符是决定效率的**关键选择器**，越具体的关键选择器，其性能越高。
    2. 效率（从高到低）

        1. ID选择器
        2. 类选择器
        3. 元素选择器
        4. 毗邻元素选择器（`+`）
        5. 子元素选择器（`>`）
        6. 后代元素选择器（` `）
        7. 通配符选择器（`*`）
        8. 属性选择器
        9. 伪类选择器、伪元素选择器
3. [类型](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/前端概念/基础概念.md#选择器类型)

### 层叠上下文（stacking context）
>参考：[张鑫旭：深入理解CSS中的层叠上下文和层叠顺序](http://www.zhangxinxu.com/wordpress/2016/01/understand-css-stacking-context-order-z-index/)。

1. 满足以下任意条件则形成层叠上下文：

    1. 根元素 (`HTML`)。
    2. `z-index`属性值不为~~`auto`~~的`position: relative/absolute;`定位元素。
    3. `position: fixed;`（仅限Chrome，其他浏览器遵循需要`z-index`为数值）。
    4. `z-index`属性值不为~~`auto`~~的`flex`项（父元素`display: flex/inline-flex;`）。
    5. `opacity`属性值`< 1`的元素。
    6. `transform`属性值不为~~`none`~~的元素。
    7. `mix-blend-mode`属性值不为~~`normal`~~的元素。
    8. `filter`属性值不为~~`none`~~的元素。
    9. `perspective`属性值不为~~`none`~~的元素。
    10. `isolation`属性值为`isolate`的元素。
    11. `will-change`属性值指定任意CSS属性（即便没有直接指定这些属性的值）。
    12. `-webkit-overflow-scrolling`属性值为`touch`的元素。
2. 层叠顺序（stacking order）

    1. 每个层叠上下文完全独立于兄弟元素，当处理层叠时只考虑子元素（`z-index`值只在父级层叠上下文中有意义）。
    2. 2个元素的层叠顺序，由各自祖先元素中拥有共同**层叠上下文父级**的层叠顺序决定（`z-index: auto;`不形成层叠上下文）。
3. `z-index`使用注意

    1. 应该只给堆叠在一起的节点设置此属性。
    2. 尽量在页面中不要使`z-index`的数值`> 4`，否则就要考虑是否过度使用此属性。

### `word-spacing`
对有空白字符包裹的非空白字符产生效果。

### `word-break`
单词内断字换行。

1. ~~默认~~

    若此行放不下则整个单词换行，若下行也放不下则溢出（保持单词不断字）。
2. ~~`word-break: break-all;`~~

    若此行放不下则直接断字，不会尝试整个单词换行。
3. `word-wrap: break-word;`

    若此行放不下则整个单词先换行，若下行也放不下才断字。

>1. 对于用户输入或不确定长度的内容，建议都加上`word-wrap: break-word;`，避免内容宽度溢出。
>2. 或直接在`body`上设置，让所有内容继承。

### 用CSS创造三角形、梯形
```css
.triangle {
    border-width: 20px;
    border-style: dashed solid dashed dashed; /* dashed兼容ie6*/
    border-color: transparent #000 transparent transparent;
    _overflow: hidden;
    height: 0;
    width: 0;
}
.trapezoid {
    border-width: 20px;
    border-style: dashed solid dashed dashed; /* dashed兼容ie6*/
    border-color: transparent #000 transparent transparent;
    _overflow: hidden;
    height: 20px;
    width: 20px;
}
```
>两个同样大小的三角形，第二个设置为背景色并且覆盖到第一个上面，可以模拟箭头`>`。

[JSFiddle Demo](https://jsfiddle.net/realgeoffrey/17v1cchL/)

### 清除浮动：
1. 在父级添加

    ```scss
    @mixin clearfix {
        *zoom: 1;

        &:after {
            content: "";
            display: table;
            clear: both;
        }
    }
    ```
2. 触发父级BFC

    1. 截断不影响时

        ```css
        .father {
            overflow: hidden;
            _width: 100%;
        }
        ```
    2. 父级设置`float: left/right;`
    3. 父级设置`position: absolute/fixed;`

### 单行或多行文本超出宽度则显示省略号
1. 单行

    ```scss
    @mixin ellipsis($boolen: true) {
        @if $boolen == true {
            _width: 100%;
        }
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }
    ```
2. 多行

    ```scss
    @mixin multi-ellipsis($line-height, $line) {
        line-height: $line-height;
        height: $line-height * $line;
        display: block;
        display: -webkit-box;
        *display: block;
        overflow: hidden;
        text-overflow: ellipsis;
        -webkit-box-orient: vertical;
        -webkit-line-clamp: $line;
    }
 
    //rem模式
    @mixin multi-ellipsis-rem($line-height, $line) {
        line-height: rem($line-height);
        height: rem($line-height * $line);  //或max-height: rem($line-height * $line);
        display: block;
        display: -webkit-box;
        overflow: hidden;
        text-overflow: ellipsis;
        -webkit-box-orient: vertical;
        -webkit-line-clamp: $line;
    }
    ```
    
[JSFiddle Demo](https://jsfiddle.net/realgeoffrey/5j8hxxLb/)

### `filter`滤镜
>暂时还没有兼容所有浏览器的方案。

1. CSS3图形特效

    >兼容性：除*ie10*与*ie11*外基本所有主流浏览器。

    1. 高斯模糊

        ```css
        .filter {
            -webkit-filter: blur(10px);
            -moz-filter: blur(10px);
            -ms-filter: blur(10px);
            filter: blur(10px);
            filter: progid:DXImageTransform.Microsoft.Blur(PixelRadius=10, MakeShadow=false); /* ie6~ie9 */
        }
        ```
    2.灰度

        ```css
        .filter {
            -webkit-filter: grayscale(100%);
            -moz-filter: grayscale(100%);
            -ms-filter: grayscale(100%);
            filter: grayscale(100%);
            filter: gray; /* ie6~ie9 */
        }
        ```
2. SVG滤镜元素

    >兼容性：较新版本的FireFox、Chrome、Opera。

    新建一个SVG文件，把滤镜方法放进去，然后CSS调用`filter: url(某.svg#某id);`。

    1. 高斯模糊

        ```svg
        <svg version="1.1" baseProfile="full" xmlns="http://www.w3.org/2000/svg">
            <defs>
                <filter id="某id">
                    <feGaussianBlur stdDeviation="10"/>
                </filter>
            </defs>
        </svg>
        ```
    2. 灰度

        ```svg
        <svg version="1.1" baseProfile="full" xmlns="http://www.w3.org/2000/svg">
            <defs>
                <filter id="某id">
                    <feColorMatrix type="matrix" values="0.3333 0.3333 0.3333 0 0 0.3333 0.3333 0.3333 0 0 0.3333 0.3333 0.3333 0 0 0 0 0 1 0"/>
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

### `table`
1. table属性为`table-layout: auto;/*默认*/`

    在`td`或`th`上设置宽度无效，各项宽度取决于内容宽度。
2. table属性为`table-layout: fixed;`

    1. 可以设置`td`或`th`宽度，没有设置宽度的所有项平分父级余下的宽度。
    2. 第一行宽度决定所有行宽度。

>默认各项内容垂直居中，用`vertical-align`调节垂直对齐（各项为`table-cell`）。

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
    .i-1 {
        width: 固定宽度1;
    }
    .i-2 {
        /*width: auto;*/
    }
    .i-3 {
        width: 固定宽度3;
    }
    .i-4 {
        width: 固定宽度4;
    }
    .i-5 {
        /*width: auto;*/
    }
</style>

<table>
    <tbody>
    <tr>
        <td class="i-1">
            固定宽度 内容1
        </td>
        <th class="i-2">
            平分余下宽度 内容2
        </th>
        <td class="i-3">
            固定宽度 内容3
        </td>
        <td class="i-4">
            固定宽度 内容4
        </td>
        <td class="i-5">
            平分余下宽度 内容5
        </td>
    </tr>
    ...
    </tbody>
</table>
```

### 使元素强制表现为`block`的CSS设置
1. `float: left/right;`
2. `position: absolute/fixed;`

>意味着有以上CSS属性的内联标签可以当做块级标签使用。

### 块级元素的width
1. `width: auto;`：

    默认值，换算具体值为：**本元素width = 父级width - 本元素（margin + padding + border）水平值**。

    >当块级width为默认的auto时，设置负的水平margin会使width增加。
2. `width: 100%;`：

    父级的px为自己的px。

### margin合并
1. W3C定义：在CSS中，两个或多个毗邻（父子元素或兄弟元素）的普通流中的块元素垂直方向上的margin会发生叠加。这种方式形成的外边距即可称为外边距叠加（collapsed margin）。

    1. 毗邻：是指没有被**非空内容**、**padding**、**border**或**clear**分隔开。
    2. 普通流：除`float: left/right`、`positon: absolute/fixed`外的代码。
2. 产生独立的BFC结构可避免margin合并

>ie6、7触发haslayout会影响margin合并的发生。

### BFC（Block Formatting Context）块级格式上下文
1. W3C定义：

    1. 浮动元素和绝对定位元素，非块级盒子的块级容器（例如 inline-blocks、table-cells、和table-captions），以及overflow值不为“visiable”的块级盒子，都会为他们的内容创建新的块级格式化上下文。
    2. 在一个块级格式化上下文里，盒子从包含块的顶端开始垂直地一个接一个地排列，两个盒子之间的垂直的间隙是由他们的margin 值所决定的。两个相邻的块级盒子的垂直外边距会发生叠加。
    3. 在块级格式化上下文中，每一个盒子的左外边缘（margin-left）会触碰到容器的左边缘（border-left）（对于从右到左的格式来说，则触碰到右边缘），即使存在浮动也是如此，除非这个盒子创建一个新的块级格式化上下文。
2. BFC是一个独立的布局环境，可以理解为一个箱子，箱子里面物品的摆放不受外界的影响，并且每个BFC都遵守同一套布局规则。
3. 对容器添加以下CSS属性使其成为独立的BFC

    1. `float: left / right;`
    2. `overflow: hidden / auto / scroll;`
    3. `display: inline-block / table-cell / table-caption / flex / inline-flex;`
    4. `position: absolute / fixed;`

>ie6、7不支持BFC，但是有haslayout。

### CSS的小数、百分比
1. 浏览器会把小数以及百分比换算成整数的单位（px）

    1. 四舍五入：ie8、ie9、chrome、firefox。
    2. 直接向下取整：ie7、safari。
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
3. 使用`rem`，因为换算成`px`而四舍五入或向下取整可能导致切图问题的解决方案：

    1. 切图四周多给2px透明距离。
    2. 内容填色的图片用`width: 100%;`。
    3. 内容的间隙多设置一些`padding`，再用`负margin`中和。

### 移动端半像素
不要使用`border: 0.5px`，因为浏览器会把数值换算成0或者1。

1. 整个边框0.5px

    ```scss
    div {
        width: 宽度;
        position: relative;

        &:before {
            position: absolute;
            top: 0;
            left: 0;
            content: "";
            width: 200%;
            height: 200%;
            border: 1px solid 颜色;
            transform: scale(.5);
            transform-origin: 0 0;
            box-sizing: border-box;
        }
    }
    ```
2. 某一边0.5px

    ```scss
    div {
        width: 100px;
        position: relative;

        &:before {
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
    }
    ```
    
[JSFiddle Demo](https://jsfiddle.net/realgeoffrey/3wbf62xj/)

### `line-height`
1. 单行文本情况下：

    1. 内联元素的高度由`line-height`决定。
    2. 块级元素的高度先由`height`决定，若没有设置`height`再由`line-height`决定（ie6是`line-height`优先决定）。
2. 元素高度表现为：

    **内容区域（content area） + 行间距（vertical spacing） = 行高（line-height）**

    >1. 内容区域（鼠标指示出的高度）：只与字号（font-size）和font-family有关。
    >2. 行间距：摇摆不定，可以为负值，仅为达成以上等式而变化。

>ie6以及其他渲染有误的浏览器不能用line-height控制图片与文字的对齐位置（可以使用[垂直居中](https://github.com/realgeoffrey/knowledge/tree/master/网站前端/HTML+CSS学习笔记#垂直居中)）。

### img标签的src属性
>当img标签的地址为空或错误时，会出现浏览器默认灰色边框，无法去除。

1. 不要用**空的img标签加上背景来用作默认图**，必须用其他标签来代替。
2. img标签没有src属性或src属性为空隐藏

    ```css
    img[src=""] {   /* ie8+*/
        visibility: hidden; /* 属性为空隐藏*/
    }
    img:not([src]) {    /* ie9+*/
        visibility: hidden; /* 属性不存在隐藏*/
    }
    ```
3. 要谨慎给img设置背景（比如内容图片或者头像的初始图，不要使用背景，应该使用[JS延时加载](https://github.com/realgeoffrey/knowledge/tree/master/网站前端/JS方法积累/实用方法#jquery或zepto图片延时加载)），因为当img是透明图的时候，会展示背景的内容。

### img标签的圆形、边框
1. 圆形+边框

    1. pc

        直接在img标签上设置`border`和`border-radius`。
    2. wap

        在img标签上设置`border-radius`，并且在父级标签嵌套一层设置`border`和`border-radius`。
2. 圆形（无边框）

    - pc、wap

        直接在img标签上设置`border-radius`。

### wap页面自适应图片
要求：图片根据浏览器窗口变化而宽高同时等比例变化，不使用`img`标签（只有内容图片才使用img标签）。

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

    >缺点：只能用于空标签。
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

    >1. 百分比公式：
    >
    >   1. `background-position-x = 小图横坐标px / ( 大图宽度px - 小图宽度px ) * 100%`
    >   2. `background-position-y = 小图纵坐标px / ( 大图高度px - 小图高度px ) * 100%`
    >2. 可以用预处理语言计算：
    >
    >   ```scss
    >   @function rem($px) {
    >       @return $px / 20 + rem;
    >   }
    >   @function position-one($positon, $singleSize, $spritesSize) {
    >       @if $positon == 0 {
    >           @return 0;
    >       } @else {
    >           @return percentage($positon / ($spritesSize - $singleSize));
    >       }
    >   }
    >   /* x轴排列雪碧图*/
    >   @mixin sprites-x($x: 0, $width: 单图固定宽度或0, $fullWidth: 合并图宽度) {
    >       background-image: url(图片);
    >       background-position: position-one($x, $width, $fullWidth) 0;
    >       background-size: rem($fullWidth) auto;
    >       background-repeat: no-repeat;
    >   }
    >   /*/x轴排列雪碧图*/
    >   /* y轴排列雪碧图*/
    >   @mixin sprites-y($y: 0, $height: 单图固定高度或0, $fullHeight: 合并图高度) {
    >       background-image: url(图片);
    >       background-position: 0 position-one($y, $height, $fullHeight);
    >       background-size: auto rem($fullHeight);
    >       background-repeat: no-repeat;
    >   }
    >   /*/y轴排列雪碧图*/
    >   /* x+y轴排列且等大雪碧图（参数：单图宽、高、x轴图片数量、y轴图片数量、图片间距）*/
    >   @mixin sprites-xy($width, $height, $x, $y, $gap: 2) {
    >       width: rem($width);
    >       height: rem($height);
    >       background-image: url(图片前缀#{$width}x#{$height}.png);
    >       background-size: rem(($width + $gap)*$x - $gap) rem(($height + $gap)*$y - $gap);
    >       background-repeat: no-repeat;
    >
    >       //$i：横轴；$j：纵轴
    >       @for $j from 1 through $y {
    >           @for $i from 1 through $x {
    >               &.i-#{$j}-#{$i} {
    >                   background-position: position-one(($width + $gap)*($i - 1), $width, ($width + $gap)*$x - $gap) position-one(($height + $gap)*($j - 1), $height, ($height + $gap)*$y - $gap);
    >               }
    >           }
    >       }
    >   }
    >   /*/x+y轴排列且等大雪碧图*/
    >   ```

    1. **rem宽高（最佳方式）**

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

### 3D按钮
```scss
.button3d {
    display: block;
    width: 300px;
    height: 50px;
    line-height: 50px;
    font-size: 20px;
    text-align: center;

    color: #fff;
    background-color: #a5de37;
    box-shadow: 0 7px 0 #8bc220, 0 8px 3px rgba(0, 0, 0, 0.3);
    position: relative;
    top: 0;
    transition: .3s;

    &:hover {
        background-color: #b9e563;
        box-shadow: 0 7px 0 #84b91f, 0 8px 3px rgba(0, 0, 0, 0.3);
    }
    &:active {
        color: #8bc220;
        background-color: #a1d243;
        box-shadow: 0 2px 0 #6b9619, 0 3px 3px rgba(0, 0, 0, 0.2);
        top: 5px;
        transition: .15s;
        text-shadow: 0 1px 0 rgba(255, 255, 255, 0.3);
    }
}
```
[JSFiddle Demo](https://jsfiddle.net/realgeoffrey/fd4qon26/)
>参考：[Buttons](https://github.com/alexwolfe/Buttons)。

### 滚动条
1. 若`overflow-x`和`overflow-y`相同，则等同于`overflow`；若不同，且其中一个值为`visible`，另一个为`hidden/scroll/auto`，则`visible`重置为`auto`。
2. 默认滚动条均来自`html`标签（而不是body标签）

    因此，除去默认滚动条应在`html`上设置overflow值。
3. JS获取文档滚动高度为：

    1. `document.body.scrollTop || document.documentElement.scrollTop`
    2. jQuery：`$(window).scrollTop()`或`$(document).scrollTop()`；Zepto：`$(window).scrollTop()`
4. 滚动条会占用容器的可用高度或宽度。

### 滚动条样式
1. `WebKit`：

    1. `::-webkit-scrollbar`：滚动条整体部分，可以设置`宽度`。
    2. `::-webkit-scrollbar-track`：滚动条轨道，可以设置`背景`、`圆角`。
    3. `::-webkit-scrollbar-thumb`：滑块，可以设置`背景`、`圆角`、`阴影`。
    4. `::-webkit-scrollbar-track-piece`：滚动条轨道上覆盖的一层轨道，可以设置`背景`、`圆角`。
    5. `::-webkit-scrollbar-thumb:window-inactive`：浏览器未被选中时的滑块（也可以用于其他伪类）。
    6. `::-webkit-scrollbar-button`：滚动条两端按钮，可以设置`背景`、`圆角`、`阴影`。
    7. `::-webkit-scrollbar-corner`：横竖滚动条相交的边角，可以设置`背景`、`圆角`。
    8. `::-webkit-resizer`：定义右下角拖动缩放节点高宽的内容。

    一般只需要设置：
    ```scss
    &::-webkit-scrollbar {
        width: 6px;
    }
    &::-webkit-scrollbar-track {
        border-radius: 3px;
        background-color: #dac3a2;
    }
    &::-webkit-scrollbar-thumb {
        border-radius: 3px;
        background-color: #ffe7c6;
        box-shadow: inset 0 0 0 1px #dac3a2;
    }
    ```
2. `ie`：

    1. `scrollbar-arrow-color: 颜色;`：三角箭头的颜色。
    2. `scrollbar-face-color: 颜色;`：立体滚动条的颜色（包括箭头部分的背景色）。
    3. `scrollbar-3dlight-color: 颜色;`：立体滚动条亮边的颜色。
    4. `scrollbar-highlight-color: 颜色;`：滚动条的高亮颜色（左阴影？）。
    5. `scrollbar-shadow-color: 颜色;`：立体滚动条阴影的颜色。
    6. `scrollbar-darkshadow-color: 颜色;`：立体滚动条外阴影的颜色。
    7. `scrollbar-track-color: 颜色;`：立体滚动条背景颜色。
    8. `scrollbar-base-color: 颜色;`：滚动条的基色。

>参考：[链接1（翻译）](http://alfred-sun.github.io/blog/2014/12/24/scrollbar-customized-with-css-style/)、[链接2（原文）](https://css-tricks.com/custom-scrollbars-in-webkit/)。

----
## HTML + CSS

### 自适应宽度布局
>`float`节点：可以填补于**之后节点**的水平`margin`内（`padding`内不可以）；不可以填补于*之前节点*的水平`margin`内。

1. 中间内容自适应，两边固定（中间内容最后加载）

    ```html
    <style type="text/css">
        .float_l {
            float: left;
            _display: inline;
            width: 左边块宽度;
        }
        .float_r {
            float: right;
            _display: inline;
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

    >1. DOM结构不能颠倒，需要中间结构放最后;
    >2. 节点上能设定`clear: both;`。
2. 中间内容自适应，两边固定（中间内容最先加载）

    >所谓的“双飞翼布局”。

    ```html
    <style type="text/css">
        .main_out,
        .float_l,
        .float_r {
            float: left;
            _display: inline;
        }
        .middle_out {
            width: 100%;
        }
        .middle_in {
            margin: 0 大于等于右边块宽度 0 大于等于左边块宽度;
        }
        .float_l {
            width: 左边块宽度;
            margin-left: -100%;
        }
        .float_r {
            width: 右边块宽度;
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

    >1. DOM结构不能颠倒，需要中间结构放最前;
    >2. 节点上能设定`clear: both;`。
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

    >1. DOM结构不能颠倒，需要中间结构放最后;
    >2. 节点上能设定`clear: both;`;
    >3. 完全由内容决定布局；
    >4. 第一块内容要给第二块内容留下足够空间，否则第二块放不下会整个换行；第一块+第二块要给第三块留下足够空间，否则第三块放不下会整个换行。

### 垂直居中
1. 图标和文字并排垂直居中

    1. 图标设置为`absolute`，用`margin-left`调整水平位置（没有设置`left`或`right`，则在文档流所在的水平位置开始定位，并且不在文档流中），用`top`和`margin-top`调整垂直位置。

        1. 图标后置
        
            1. 水平居左
            
                ```html
                <style>
                    .ico_r_1 {
                        position: relative;
                        padding-right: 100px;
                        _zoom: 1;

                        /*height、line-height、width、截断*/
                    }
                    .ico_r_1 i {
                        position: absolute;
                        width: 100px;
                        height: 20px;
                        top: 50%;
                        margin-top: -10px;
                        background-color: red;
                    }
                </style>
 
                <div class="ico_r_1">
                    S-水平居左，图标后置-E
                    <i>1</i>
                </div>
                ```        
            2. 水平居中
            
                ```html
                <style>
                    .ico_r_2 {
                        text-align: center;
                        position: relative;
                        padding-right: 100px;
                        _zoom: 1;

                        /*height、line-height、width、截断*/
                    }
                    .ico_r_2 i {
                        position: absolute;
                        width: 100px;
                        height: 20px;
                        top: 50%;
                        margin-top: -10px;
                        background-color: red;
                    }
                </style>
 
                <div class="ico_r_2">
                    S-水平居中，图标后置-E
                    <i>2</i>
                </div>
                ```
            3. 水平居右
            
                ```html
                <style>
                    .ico_r_3 {
                        text-align: right;
                        position: relative;
                        padding-right: 100px;
                        _zoom: 1;

                        /*height、line-height、width、截断*/
                    }
                    .ico_r_3 i {
                        position: absolute;
                        width: 100px;
                        height: 20px;
                        top: 50%;
                        margin-top: -10px;
                        background-color: red;
                    }
                </style>
 
                <div class="ico_r_3">
                    S-水平居右，图标后置-E
                    <i>3</i>
                </div>
                ```
        2. 图标前置

            1. 水平居左
            
                ```html
                <style>
                    .ico_l_1 {
                        position: relative;
                        padding-left: 100px;
                        _zoom: 1;

                        max-width: 文字宽度;
                        _width: 文字宽度;
                        white-space: nowrap;
                        overflow: hidden;
                        text-overflow: ellipsis;

                        /*height、line-height*/
                    }
                    .ico_l_1 i {
                        width: 100px;
                        height: 20px;
                        position: absolute;
                        top: 50%;
                        margin-top: -10px;
                        margin-left: -100px;
                        background-color: red;
                    }
                </style>
 
                <div class="ico_l_1">
                    <i>4</i>
                    S-水平居左，图标前置-E
                </div>
                ```
            2. 水平居中
            
                ```html
                <style>
                    .ico_l_2 {
                        display: inline-block;
                        *display: inline;
                        *zoom: 1;
                        position: relative;
                        padding-left: 100px;
                        font-size: ;

                        max-width: 文字宽度;
                        _width: 文字宽度;
                        white-space: nowrap;
                        overflow: hidden;
                        text-overflow: ellipsis;

                        /*height、line-height*/
                    }
                    .ico_l_2 i {
                        width: 100px;
                        height: 20px;
                        position: absolute;
                        top: 50%;
                        margin-top: -10px;
                        left: 0;
                        background-color: red;
                    }
                </style>
 
                <div style="text-align: center;font-size: 0;/*width、height、其他位置设置*/">
                    <div class="ico_l_2">
                        <i>5</i>
                        S-水平居中，图标前置-E
                    </div>
                </div>
                ```
            3. 水平居右
            
                ```html
                <style>
                    .ico_l_3 {
                        display: inline-block;
                        *display: inline;
                        *zoom: 1;
                        position: relative;
                        padding-left: 100px;
                        font-size: ;

                        max-width: 文字宽度;
                        _width: 文字宽度;
                        white-space: nowrap;
                        overflow: hidden;
                        text-overflow: ellipsis;

                        /*height、line-height*/
                    }
                    .ico_l_3 i {
                        position: absolute;
                        width: 100px;
                        height: 20px;
                        top: 50%;
                        margin-top: -10px;
                        left: 0;
                        background-color: red;
                    }
                </style>
 
                <div style="text-align: right;font-size: 0;/*width、height、其他位置设置*/">
                    <div class="ico_l_3">
                        <i>6</i>
                        S-水平居右，图标前置-E
                    </div>
                </div>
                ```    
        3. 图标前置+图标后置，水平居中

            ```html
            <style>
                .ico_l_r {
                    display: inline-block;
                    *display: inline;
                    *zoom: 1;
                    position: relative;
                    padding: 0 100px;
                    font-size: ;

                    max-width: 文字宽度;
                    _width: 文字宽度;
                    white-space: nowrap;
                    overflow: hidden;
                    text-overflow: ellipsis;

                    /*height、line-height*/
                }
                .ico_l_r i.i-l {
                    position: absolute;
                    width: 100px;
                    height: 20px;
                    top: 50%;
                    margin-top: -10px;
                    left: 0;
                    background-color: red;
                }
                .ico_l_r i.i-r {
                    position: absolute;
                    width: 100px;
                    height: 20px;
                    top: 50%;
                    margin-top: -10px;
                    right: 0;
                    background-color: red;
                }
            </style>

            <div style="text-align: right;font-size: 0;/*width、height、其他位置设置*/">
                <div class="ico_l_r">
                    <i class="i-l">7</i>
                    S-水平居中，图标前置+图标后置-E
                    <i class="i-r">7</i>
                </div>
            </div>
            ```

        [JSFiddle Demo](https://jsfiddle.net/realgeoffrey/4z8r51or/)
    2. ~~图标设置为`inline-block`，再用`vertical-align`微调。~~

        `vertical-align`在不同浏览器表现太不一致，垂直方向无法获得真正居中效果。
        
    3. 使用`float`。
2. 不确定高度的垂直居中

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
    [JSFiddle Demo](https://jsfiddle.net/realgeoffrey/c1pz8mow/)
    
### 水平居中
1. 内容宽度可变
    
    用`text-align: center;`控制`inline-block`水平居中。
    ```html
    <style>
        .outer_1 {
            text-align: center;
            font-size: 0;
        }
        .outer_1 li {
            display: inline-block;
            *display: inline;
            zoom: 1;
         
            font-size: ;
        }
    </style>

    <ul class="outer_1">
        <li>...</li>
        <li>...</li>
        <li>...</li>
    </ul>
    ```
2. 内容宽度固定

    ```html
    <style>
        .outer_2 {
            width: 总宽度;
            margin: 0 auto;
        }
        .outer_2 li {
            float: left;
            _display: inline;
            width: 单个宽度;
        }
    </style>

    <ul class="outer_2 clearfix">
        <li>...</li>
        <li>...</li>
        <li>...</li>
    </ul>
    ```

### 翻转效果（ie10+及高级浏览器）
```html
<style type="text/css">
    .item {
        position: relative;
        width: 宽度;
        height: 高度;
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
    .item .front img,
    .item .front img {
        display: block;
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
[JSFiddle Demo](https://jsfiddle.net/realgeoffrey/88hob0d7/)

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
                background: url(背景图) 0 100% no-repeat; /* 横版背景图，分别从左到右是头部、中间、底部内容*/
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
                background: url(背景图) -宽度 0 repeat-y;    /* 横版背景图，分别从左到右是头部、中间、底部内容*/
            }
            .middle {
                background: url(背景图) 0 0 no-repeat;
            }
            .in {
                background: url(背景图) -2*宽度 100% no-repeat;
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
            background: url(背景图) 0 100% no-repeat; /* 横版背景图，分别从左到右是头部、中间、底部内容*/
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
>要做到不同字数的一行文字等宽。

1. 用`inline-block`标签填补间隙

    ```html
    <style type="text/css">
        i {
            display: inline-block;
            *display: inline;
            zoom: 1;
            width: 1em;
        }
    </style>
    
    <p>文字文字</p>
    <p>文<i></i><i></i>字</p>
    ```
2. 用`&ensp;`（字体宽度1/2em）、`&emsp;`（字体宽度1em）填补间隙。
    
    ```html
    <p>三个字</p>
    <p>两&emsp;个</p>
    
    <p>四个字的</p>
    <p>三&ensp;个&ensp;字</p>
    ```
    
[JSFiddle Demo](https://jsfiddle.net/realgeoffrey/zdh8oxrt/)

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

### 实现hover去除左右间隔效果
图片法：hover之后本身的背景被替换，前一个兄弟的背景被覆盖

```scss
ul {
    overflow: hidden;

    li {
        @include left;
        margin-left: -1px;

        a {
            background: url(宽度根据li的margin-left、高度根据a的高度决定的border样式图片) 100% center no-repeat;
            display: block;

            &:hover {
                background: 背景色;
            }
        }
    }
}
```
>可以用`box-shadow`设置单边的间隔。

### 实现hover之后底部border替换父级border
1. 用`relative`控制

    ```scss
    ul {
        height: 高度1;
        border-bottom: 高度2 solid 颜色1;
        *zoom: 1;
        /* 不能overflow: hidden;*/

        &:after {
            content: "";
            display: table;
            clear: both;
        }
        li {
            width:;

            height: 高度1;
            float: left;
            _display: inline;
        }
        a {
            display: block;
            height: （高度1+高度2）;
            _position: relative;
            _bottom: -高度2;
            /* 不能有background*/

            &.hover,
            &:hover {
                height: （高度1+高度2-高度3）;
                border-bottom: 高度3 solid 颜色2;
            }
        }
    }
    ```
2. 用`absolute`控制

    ```scss
    ul {
        height: 高度1;
        border-bottom: 高度2 solid 颜色1;
        *zoom: 1;
        /* 能够overflow: hidden;*/

        &:after {
            content: "";
            display: table;
            clear: both;
        }
        li {
            width: 宽度;

            height: 高度1;
            float: left;
            _display: inline;

            a {
                width: 宽度;

                position: absolute;
                height: 高度1;
                /* 可以使用background*/

                &.hover,
                &:hover {
                    height: （高度1+高度2-高度3）;
                    border-bottom: 高度3 solid 颜色2;
                }
            }
        }
    }
    ```
3. 用`margin`控制

    ```scss
    ul {
        height: 高度1;
        border-bottom: 高度2 solid 颜色1;
        *zoom: 1;
        /* 不能overflow: hidden;*/

        &:after {
            content: "";
            display: table;
            clear: both;
        }
        li {
            width:;

            height: （高度1+高度2）;
            float: left;
            _display: inline;

            a {
                display: block;
                height: （高度1+高度2）;
                margin-bottom: -高度2;
                _position: relative;
                /* 不能有background*/

                &.hover,
                &:hover {
                    height: （高度1+高度2-高度3）;
                    _height: （高度1+高度2）;
                    border-bottom: 高度3 solid 颜色2;
                }
            }
        }

    }
    ```
    
[JSFiddle Demo](https://jsfiddle.net/realgeoffrey/3tw4mx7v/)

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
    [JSFiddle Demo](https://jsfiddle.net/realgeoffrey/1xbeo5cu/)
2. *ie6中，当.last_container高度变化的时候会渲染错误（每次改变高度，需要用JS给某些节点增加haslayout）*

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
    [JSFiddle Demo](https://jsfiddle.net/realgeoffrey/w6veg7ep/)

>有些插件效果不能支持`html,body {height: 100%;}`。

### CSS3的`animation`使用
>动画进行到一半取消动画（去除了相关类）或者替换动画，会导致节点突兀地回到初始位置。

1. 纯CSS触发（如`:hover`）
    ```css
    .dom:hover {
        animation: func 1s infinite;
    }
    @keyframes func {
       
    }
    ```
2. 用JS控制启动时的动画效果和关闭时的动画效果

    ```html
    <style>
        .dom.fade_in {
            animation: func_in 1s infinite;
        }
        .dom.fade_out {
            animation: func_out 1s 1;
        }
        @keyframes func_in {

        }
        @keyframes func_out {

        }
    </style>

    <div class="dom j-dom">...</div>

    <script>
        $(document).on('mouseenter', '.j-dom', function () {
            var self = $(this);
            
            self.removeClass('fade_out');
            setTimeout(function () {
               self.addClass('fade_in');
            }, 0);
        }).on('mouseleave', '.j-dom', function () {
            var self = $(this);
            
            self.removeClass('fade_in');
            setTimeout(function () {
               self.addClass('fade_out');
            }, 0);
        });
    </script>
    ```
3. [监听动画结束事件，在结束时候再去除动画](https://github.com/realgeoffrey/knowledge/tree/master/网站前端/JS方法积累/实用方法#jquery或zepto启动暂停css动画)

[JSFiddle Demo](https://jsfiddle.net/realgeoffrey/Lukonj4s/)

### 禁用`a`标签鼠标、键盘事件
1. `pointer-events: none;`穿透`a`标签的鼠标事件（包括点击和hover等，因为点击不到所以JS事件也不会触发）。
2. 不设置`href`属性，可以忽略键盘索引（tab键无法切换到）。

```html
<a style="pointer-events: none;">禁用鼠标和键盘的链接</a>
```

### 横竖屏切换
>1. 翻转效果的节点，如果要增加内嵌滚动条，不能在此节点上增加`border-radius`，否者滚动条横竖轴颠倒。
>2. 部分Android系统（或低端机）对内嵌的滚动条（`overflow: hidden/auto`）支持不佳，尤其增加了翻转效果后，设置的滚动条（甚至`overflow: hidden;`）会导致更多样式问题。除了去除内嵌滚动条的`border-radius`，还可以尝试给兄弟节点设置`z-index`。部分性能较差的webview对CSS3支持非常有限，无法做到**翻转+内嵌滚动条**（内嵌滚动条横竖轴颠倒）。
>
>- 其他解决方案：使用按钮（控制翻页或JS滚动）代替内嵌滚动条；使用`touchmove`实现滑动页面。

1. 媒体查询控制横竖屏添加翻转类

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
2. 用JS方法控制：[模拟手机翻转](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/JS方法积累/实用方法/README.md#jquery或zepto模拟手机翻转使页面都以横屏展示)。
3. 翻转使用的媒体查询：

    要求：页面没有滚动条，内容都在一屏视窗内；设计稿只有一份，但要适应各种分辨率机型。

    ```scss
    @function rem($px) {
        @return $px / 23 + rem;
    }

    /* 当竖屏时用屏幕宽度来判断*/
    @media (max-width: 351px) and (orientation: portrait) {
        html {font-size: 10px;}
    }
    @media (min-width: 352px) and (max-width: 383px) and (orientation: portrait) {
        html {font-size: 11px;}
    }
    @media (min-width: 384px) and (max-width: 415px) and (orientation: portrait) {
        html {font-size: 12px;}
    }
    @media (min-width: 416px) and (max-width: 447px) and (orientation: portrait) {
        html {font-size: 13px;}
    }
    @media (min-width: 448px) and (max-width: 479px) and (orientation: portrait) {
        html {font-size: 14px;}
    }
    @media (min-width: 480px) and (max-width: 511px) and (orientation: portrait) {
        html {font-size: 15px;}
    }
    @media (min-width: 512px) and (max-width: 543px) and (orientation: portrait) {
        html {font-size: 16px;}
    }
    @media (min-width: 544px) and (max-width: 575px) and (orientation: portrait) {
        html {font-size: 17px;}
    }
    @media (min-width: 576px) and (max-width: 607px) and (orientation: portrait) {
        html {font-size: 18px;}
    }
    @media (min-width: 608px) and (max-width: 639px) and (orientation: portrait) {
        html {font-size: 19px;}
    }
    @media (min-width: 640px) and (max-width: 671px) and (orientation: portrait) {
        html {font-size: 20px;}
    }
    @media (min-width: 672px) and (max-width: 703px) and (orientation: portrait) {
        html {font-size: 21px;}
    }
    @media (min-width: 704px) and (max-width: 735px) and (orientation: portrait) {
        html {font-size: 22px;}
    }
    @media (min-width: 736px) and (max-width: 767px) and (orientation: portrait) {
        html {font-size: 23px;}
    }
    @media (min-width: 768px) and (orientation: portrait) {
        html {font-size: 24px;}
    }

    /* 当横屏时用屏幕高度来判断*/
    @media (max-height: 223px) and (orientation: landscape) {
        html {font-size: 6px;}
    }
    @media (min-height: 224px) and (max-height: 255px) and (orientation: landscape) {
        html {font-size: 7px;}
    }
    @media (min-height: 256px) and (max-height: 287px) and (orientation: landscape) {
        html {font-size: 8px;}
    }
    @media (min-height: 288px) and (max-height: 319px) and (orientation: landscape) {
        html {font-size: 9px;}
    }
    @media (min-height: 320px) and (max-height: 351px) and (orientation: landscape) {
        html {font-size: 10px;}
    }
    @media (min-height: 352px) and (max-height: 383px) and (orientation: landscape) {
        html {font-size: 11px;}
    }
    @media (min-height: 384px) and (max-height: 415px) and (orientation: landscape) {
        html {font-size: 12px;}
    }
    @media (min-height: 416px) and (max-height: 447px) and (orientation: landscape) {
        html {font-size: 13px;}
    }
    @media (min-height: 448px) and (max-height: 479px) and (orientation: landscape) {
        html {font-size: 14px;}
    }
    @media (min-height: 480px) and (max-height: 511px) and (orientation: landscape) {
        html {font-size: 15px;}
    }
    @media (min-height: 512px) and (max-height: 543px) and (orientation: landscape) {
        html {font-size: 16px;}
    }
    @media (min-height: 544px) and (max-height: 575px) and (orientation: landscape) {
        html {font-size: 17px;}
    }
    @media (min-height: 576px) and (max-height: 607px) and (orientation: landscape) {
        html {font-size: 18px;}
    }
    @media (min-height: 608px) and (max-height: 639px) and (orientation: landscape) {
        html {font-size: 19px;}
    }
    @media (min-height: 640px) and (max-height: 671px) and (orientation: landscape) {
        html {font-size: 20px;}
    }
    @media (min-height: 672px) and (orientation: landscape) {
        html {font-size: 21px;}
    }
    ```

### 移动端制作类似pc端的`:active`效果（或`:hover`）
1. Android系统的浏览器大部分直接使用CSS伪类即可。
2. iOS系统的浏览器要添加以下代码触发使CSS伪类生效：

    ```javascript
    document.body.addEventListener('touchstart', function () {}, true);
    ```
3. ~~JS添加类的方法替代~~：

    ```html
    <style>
        .d:active,
        .d.active { }
    </style>

    <script type="text/javascript">
        var selector = '.a,.b .c,.d';   /* 选择器字符串*/

        $(document.body).on('touchstart', selector, function () {
            $(this).addClass('active');
        }).on('touchmove touchend touchcancel', selector, function () {
            $(this).removeClass('active');
        });
    </script>
    ```
    
简单情况下，页面添加`document.body.addEventListener('touchstart', function () {}, true);`即可。
>`a,button,input,textarea {-webkit-tap-highlight-color: rgba( , , , );}`是触碰到按钮时给按钮盖上一层颜色，而不是改变按钮自身样式。

### 繁星效果纯CSS实现
1. 纯色背景

    1. 底下一层：繁星用切图，其他区域透明再用背景色填充。
    2. 上面一层：用移动中的渐变背景色覆盖繁星。
2. 复杂背景

    1. 底下一层：移动中的渐变背景色（色值接近复杂背景颜色即可）。
    2. 上面一层：把繁星镂空的复杂背景。

[JSFiddle Demo](https://jsfiddle.net/realgeoffrey/qt0t668f/)

----
## 经验总结

### 自适应、布局的问题，都可以用[`flex`](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/HTML+CSS学习笔记/弹性盒子.md#flex)优雅解决

### 响应式设计
1. 媒体查询方式
    1. CSS属性：

        `@media (min-width: 360px) and (max-width: 640px) {...}`
    2. HTML标签：

        `<link rel="stylesheet" type="text/css" media="(min-width: 360px) and (max-width: 640px)" href="...">`
2. 响应式设计三大要素
    1. 媒体查询
    2. 流式布局：节点用百分比或rem
        
        >使用自适应结构，比如：[自适应宽度布局](https://github.com/realgeoffrey/knowledge/tree/master/网站前端/HTML+CSS学习笔记#自适应宽度布局)。
    3. 弹性图片：`img {max-width: 100%;}`

### 响应式页面解决方案：使用rem+媒体查询
>rem：相对于根元素的字体大小的单位。rem单位转换为具体px值：**rem乘于html的font-size像素**。

1. 媒体查询设置html的font-size，把要做成响应式的内容转换为rem单位。

    >假设页面按照320px宽度来制作。

    1. 最优解：需要使用CSS预处理语言（SCSS）

        1. 正常完成切图（可以用大于等于320px设计稿），大小值用**设计稿的px带入下面方法生成的rem值**。
        2. 媒体查询仅设置html的不同页面宽度下的font-size值。
        3. 调用的方法返回：**设计稿的px**除以**在320px宽度下的html的font-szie值**再除以**设计稿相对于320px放大倍数（一般是2x或者3x）**。
        4. 用预处理语言生成为CSS文件，其中所有单位都为`rem`。

        >1. 整个页面都是用rem进行制作。
        >2. 用scss预处理语言换算px->rem
        >
        >   ```scss
        >   @function rem($px) {
        >       @return $px / 20 + rem;
        >   }
        >   ```
    2. *不需要使用CSS预处理语言*

        1. 正常完成切图（只能用320px设计稿），用px作为单位。
        2. 媒体查询仅设置html的不同情况下的font-size值。
        3. 把CSS内需要响应式内容的px值，除以**在320px宽度下的html的font-szie值**（320px宽度时设置为10px方便计算），单位改为rem。

        >仅需要把要响应式布局的内容进行转变
2. *用JS根据是否是苹果设备进行判断：若是苹果设备则viewport设置为0.5，html的font-size设置为2倍；若非苹果设备则viewport设置为1，html的font-size设置为1倍*

    ```javascript
    var fontSize = 10;

    /* 实现根据iOS和Android不同设备设置不同的viewport*/
    if ((/iphone|ipad|ipod/i).test(navigator.appVersion) && window.devicePixelRatio >= 2) {
        document.getElementById('j-viewport').content = 'width=device-width, initial-scale=0.5, user-scalable=no, minimum-scale=0.5, maximum-scale=0.5';
        document.documentElement.style.fontSize = 2 * fontSize + 'px';
    } else {
        document.getElementById('j-viewport').content = 'width=device-width, initial-scale=1, user-scalable=no, minimum-scale=1, maximum-scale=1';
        document.documentElement.style.fontSize = fontSize + 'px';
    }
    ```

    >因为html的font-size是用JS写死的，而且viewport会变化，所以所有页面元素都要用百分比+rem。
3. *用JS根据浏览器宽度的改变修改html的font-size，页面总宽度固定为某rem。所有页面元素都要用百分比+rem*

### 不同PPI的设备使用不同分辨率的图片
>1. x1、x2、x3不同分辨率的图片放大倍数是**1倍、2倍、3倍**。
>2. 如果图片是雪碧图，则其间距也要是和放大倍数一致，x1、x2、x3分别间距是**2px、4px、6px**。
>3. `background-size`、`background-position`设置为最低分辨率时的值（单位用`px`、`rem`、`百分比`都可以）。

```scss
@mixin image($url) {
    background-image: url($url + "_x1.png");

    @media (min-resolution: 2dppx) {
        background-image: url($url + "_x2.png");
    }

    @media (min-resolution: 3dppx) {
        background-image: url($url + "_x3.png");
    }
}

.img {
    @include image("去除后缀的图片地址");
}
```

### 富文本
1. 富文本内容除了要检测用户输入标签的闭合性，还要注意**不要用`li`标签嵌套富文本**，因为代码中如果有单独的`li`（没有嵌套`ol`或`ul`），就会“升级”到跟祖先级li同级的内容。

2. 部分富文本会用标签`em`、`ol`、`ul`来表示**斜体**、**有序序列**、**无序序列**，因此如果用CSS重置了以上标签后，要在富文本内重载开启它们的默认效果。

3. 部分富文本还会在`table`标签上使用`cellspacing`、`border`、`bordercolor`属性来设置表格，又因为设置了`border: 0;`的表格标签无法重载开启以上属性作用，所以CSS重置时不要重置`table,tbody,tfoot,thead,tr,th,td`的`border`属性。

### 超出内容区域的内容
1. 用绝对定位把内容设置在外部

    不要把超出内容区域的绝对定位设置在`body`直接子级，而是设置在`body`下拥有`overflow: hidden;width: 100%;/* 默认*/`的父级下。
2. ~~用大背景模式~~

### 动画性能
>1. 为了视觉上连贯，浏览器对每一帧画面的渲染工作需要在16毫秒（1秒 / 60 = 16.66毫秒）之内完成。
>2. 实际上，在渲染某一帧画面的同时，浏览器还有一些流程工作要做（比如渲染队列的管理、渲染线程与其他线程之间的切换等）。
>3. 因此一次渲染增加的前端代码工作，需要控制在10毫秒之内完成（保证渲染工作+前端任务在16毫秒内完成），才能达到流畅的视觉效果，否则页面的渲染就会出现卡顿（帧率下降，一帧时间延长）。

1. CSS3动画性能最好、消耗最低的属性（只触发composite）：

    1. 位置：`transform: translate(xpx, ypx);`
    2. 缩放：`transform: scale(x, y);`
    3. 旋转：`transform: rotate(xdeg);`
    4. 倾斜：`transform: skew(xdeg,ydeg);`
    5. 透明：`opacity: x;`
2. 像素渲染流水线：

    `JS/CSS` -> `Style（计算样式）` >> `Layout（布局）` -> `Paint（绘制）` -> `Composite（渲染层合并）`

    >（布局、绘制、渲染层合并）改变前一个步骤需要后面一个步骤也做出处理，所以若能够仅处理越后面的步骤，对性能耗费则越少。

    1. `JS/CSS`：

        使用JS或CSS Animations、Transitions、Web Animation API来实现视觉变化效果。
    2. `Style`：

        根据CSS选择器，生成完整的CSSOM。
    3. `Layout`：

        具体计算每个DOM最终在屏幕上显示的大小和位置。web页面中元素的布局是相对的，因此一个元素的布局发生变化，会联动地引发其他元素的布局发生变化。
    4. `Paint`：

        填充像素的过程。包括绘制文字、颜色、图像、边框和阴影等，也就是DOM所有的可视效果。一般来说，这个绘制过程是在多个层上完成。
    5. `Composite`：

        在每个层（GraphicsLayer）上完成绘制过程之后，浏览器会将所有层按照合理的顺序合并成一个图层，然后显示在屏幕上。
3. 创建[GraphicsLayer](https://www.html5rocks.com/zh/tutorials/speed/layers/)（层、渲染层、复合层），交由GPU处理：

    >GPU（图形处理器）是与处理和绘制图形相关的硬件，专为执行复杂的数学和几何计算而设计的，可以让CPU从图形处理的任务中解放出来，从而执行其他更多的系统任务。

    1. 强制普通元素提升到单独层的方法：

        1. `will-change: ;`（高级浏览器，最佳方式）。
        2. `transform: translateZ(0);`（hack加速法）。
    2. 自带单独层的元素：

        1. 使用加速视频解码的`<video>`元素。
        2. 拥有 3D (WebGL) 上下文或加速的 2D 上下文的`<canvas>`元素。
        3. Flash等混合插件。
    3. 其他提升至单独层的方法：

        1. `transform`3D或`perspective`。
        2. 对自己的`opacity`做CSS动画或使用一个动画变换的元素。
        3. 拥有加速CSS过滤器的元素。
        4. 元素有一个包含层的后代节点（换句话说，就是一个元素拥有一个子元素，该子元素在自己的层里）。
        5. 如果有一个元素，它的兄弟元素在层中渲染，而这个兄弟元素的`z-index`比较小，那么这个元素（不管是不是应用了硬件加速样式）也会被放到层中。

    >**GraphicsLayer**（层）与**The stacking context**（层叠上下文）不同概念。
4. reflow和repaint产生卡顿：

    1. reflow（重排）：

        某个元素上执行动画时，浏览器需要每一帧都检测是否有元素受到影响，并调整他们的大小、位置，通常这种调整都是联动的。
    2. repaint（重绘）：

        浏览器还需要监听元素的外观变化，通常是背景色、阴影、边框等可视元素，并进行重绘。
        >Chrome并不会始终重绘整个层，它会尝试智能的去重绘DOM中失效的部分。
    3. composite：

        每次reflow、repaint后浏览器还需要层合并再输出到屏幕上。

    >1. repaint（或paint）单独消耗的性能最大。
    >2. reflow的成本比repaint的成本高得多。因为一个结点的reflow很有可能导致子结点、甚至父点以及同级结点的reflow，并且产生reflow一般也要进行repaint。
    >3. 那些容易忽略的**能引起布局改变的样式修改**，它们可能不产生动画，但当浏览器需要重新进行样式的计算和布局时，会产生reflow和repaint，这将产生高昂的性能代价并引起跳帧。
5. JS动画（命令式）比CSS动画（说明式）更消耗资源，浏览器会对CSS动画自动进行优化。
6. 滚动会触发高频率重新渲染，scroll事件的处理函数也会被高频率触发。
7. DOM转变成屏幕图像步骤：

    1. 首次创建帧：

        1. 获取DOM并将其分割为多个层；
        2. 将每个层独立绘制至位图中；
        3. 将层作为纹理上传至GPU；
        4. 复合多个层来生成最终的屏幕图像。
    2. 之后出现的帧：

        1. 如果某些特定CSS属性变化，并不需要发生重绘。Chrome可以使用早已作为纹理而存在于GPU中的层来重新复合，但会使用不同的复合属性(例如，出现在不同的位置，拥有不同的透明度等等)。
        2. 如果层的部分失效，它会被重绘并且重新上传。如果它的内容保持不变但是复合属性发生变化（例如，层被转化或透明度发生变化），Chrome可以让层保留在GPU中，并通过重新复合来生成一个新的帧。
8. [优化渲染性能](https://developers.google.com/web/fundamentals/performance/rendering/)：

    1. 优化JS的执行效率

        1. 对于动画效果的实现，避免使用`setTimeout`或`setInterval`，建议使用`requestAnimationFrame`（或[velocity动画库](https://github.com/julianshapiro/velocity)）。
        2. 把耗时长的JS代码放到`Web Workers`中去做（如果这些计算工作不会涉及DOM元素的存取）。
        3. 把DOM元素的更新划分为多个小任务，分别在多个帧中去完成。
    2. 降低样式计算的范围和复杂度

        1. 降低样式选择器的复杂度（使用基于class的方式，比如[BEM](https://en.bem.info/methodology/css/)）。
        2. 减少需要执行样式计算的元素的个数。
    3. 避免大规模、复杂的布局与重排

        1. 避免强制同步布局事件的发生

            为了避免触发不必要的布局过程，应该首先批量读取元素样式属性（浏览器将直接返回上一帧的样式属性值），然后再对样式属性进行写操作。
        2. 避免快速连续的布局

            使用先读后写的原则。
    4. 简化绘制的复杂度、减小绘制区域
    5. 优先使用层（GraphicsLayer）来统一操作动画，控制层数量

        1. 只使用`transform/opacity`来实现动画效果。
        2. 用`will-change/translateZ`属性把动画元素提升到单独的层中。
        3. 避免滥用层提升（更多的层需要更多的内存和更复杂的管理）。
    6. 对用户输入、滚动事件进行[函数防抖](https://github.com/realgeoffrey/knowledge/tree/master/网站前端/JS学习笔记#函数防抖函数节流)处理

        1. 避免使用运行时间过长的事件处理函数，它们会阻塞页面的滚动渲染。
        2. 避免在事件处理函数中修改样式属性。
        3. 对事件处理函数去抖动，存储事件对象的值，然后在requestAnimationFrame回调函数中修改样式属性。
9. 动画调优的策略与技巧：

    1. 尽可能地为产生动画的元素设置`fixed`或`absolute`。
    2. 阴影渐显动画尽量用伪类的opacity来实现。
    3. 使用3D硬件加速提升动画性能时，最好给元素增加一个z-index属性（改变层叠上下文的顺序），人为干扰层（GraphicsLayer）排序，可以有效减少chrome创建不必要的层，提升渲染性能，移动端优化效果尤为明显。
    4. 追查性能问题的时候打开**Layer Borders**选项；使用Chrome Timeline工具检查。
    5. 保证帧率平稳（避免跳帧）

        1. 不在连续的动画过程中做高耗时的操作（如大面积重绘、重排、复杂JS执行）。
        2. 若高耗时操作无法避免，则尝试化解，比如：

            1. 将高耗时操作放在动画开始或结尾处。
            2. 将高耗时操作分摊至动画的每一帧中处理。
    6. 针对硬件加速渲染通道的优化

        1. 合理划分层，动静分离，可避免大面积重绘。
        2. 使用分层优化动画时，需要留意内存消耗情况（使用Chrome Devtools监测）。
    7. 低性能设备（Android）优先调试。

        1. 除了**CSS3翻转属性**与**内嵌滚动条**同时出现无法解决，其他样式问题都可以像处理ie6问题一样通过真机试验出解决方案。
        2. 有些低版本机型会有类似ie6的CSS问题，包括**CSS3的厂商前缀（`-webkit-`等）**、**层叠关系（`z-index`）**，并且要更注意**动画性能（层产生）**。

### 经验技巧
1. 命名间隔

    1. HTML的class和id：`-`。
    2. 图片命名：`_`。
    3. JS的变量和函数：驼峰命名法（构造函数：大驼峰命名法）。
2. 引号使用

    1. HTML标签（以及内部属性）、CSS样式（如`content`、`font-family`、`quotes`）：

        双引号`"`
    2. JS代码：

        单引号`'`
3. CSS分类命名规范

    1. 布局`.g-`（grid）
    
        将页面分割为几个大块的布局，一般来说是页面最外层的类名。
    2. 模块`.m-`（module）
    
        可重复使用的较大的整体。
    3. 元件`.u-`（unit）
    
        不可再分的较为小巧的个体，通常被重复用于各种模块中。
    4. 状态`.z-`（zhuangtai）
    
        为状态类样式加入前缀，统一标识，方便识别，只作为后代选择器使用（如`.z-hover`或`.z-active`）。
    5. 样式区分`.i-`（icon）
    
        同一批内容的不同样式（比如仅背景不同的几个按钮），可以用`.i-1`、`.i-2`区分样式。
        >如果在模块上，可以使用**选择器扩展**而不加前缀`.i-`，比如`.m-xxx`扩展内容`.m-xxx-1`、`.m-xxx .btn`扩展内容`.m-xxx .btn-1`。
    6. JS功能`.j-`（javascript）
    
        仅作为JS锚点使用，不添加任何CSS样式。
        
    >- 皮肤`.s-`（skin）
    >
    >   把皮肤型的样式抽离出来。
4. 经验

    1. 标签语义化。

        先用纯HTML标签语义化结构，再加入CSS满足样式，最后加入交互。

        >1. 不要全用div标签；用`ul > li`、`ol > li`、`dl > dt`来代替p标签。
        >2. h1~h5标签不要根据其字体大小的不同来使用，应该根据页面内的重要程度来使用（SEO）。
    2. 减少层级嵌套，合理嵌套，行内元素不要嵌套块级元素（如a标签不嵌套div）。
    3. 用父节点的class去管理子节点（如父`ul`设定class，而子`li`不设定class）。
    4. 有些移动端（其实就是Android的各奇葩机型）页面的点击按钮，需要制作大一些，否者虽然看上去点击到了，但是不会触发JS效果。
5. CSS编码规范

    绝大部分同意[fex-team:tyleguide](https://github.com/fex-team/styleguide/blob/master/css.md#css编码规范)。

    >可以设置为IDE的**Reformat Code**的排版样式。

### 《高性能网站建设指南》自我总结
1. 减少HTTP请求，图片以及外链资源的优化，包括压缩与整合，服务器开启g-zip等（不要压缩图片与PDF，因为它们本身已经被压缩，再压缩可能会增加文件大小；压缩都耗费CPU）。
2. 图片的处理，包括压缩、大banner切分成多个小图、[小图合并成雪碧图](https://realgeoffrey.github.io/applets/sprites/index.html)、[图片的延迟加载](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/JS方法积累/实用方法/README.md#jquery或zepto图片延时加载)、Base64、WebP。
3. 不要缩小放大图片（使用原始大小展现）。
4. 使用CDN（Content Delivery Network，内容发布网络）。
5. 添加Expires报头（设置网页在浏览器中缓存过期时间）；配置ETags报头（用来验证浏览器缓存和原服务器上内容是否一致）。
6. 浏览器为了避免当样式变化时重绘页面中的元素，会阻塞页面内容的逐步呈现，样式表之前的内容和JS脚本之后的内容都会因为这些文件的下载而阻塞呈现。
7. 不要使用~~`@import`~~，只用`<link>`。
8. 避免~~CSS表达式（CSS expression）~~。
9. 虽然内联CSS和JS比外部文件快，但只有外部的才可能被浏览器缓存。
10. 减少DNS查找，设置合适的TTL值。
11. 避免重定向（`http://a.com/folder`会重定向到`http://a.com/folder/`，但根目录`http://a.com`不会发生重定向）。
12. 使Ajax可缓存（服务端的CDN缓存，可用jQuery的$.Ajax的cash属性设置为false，或url加时间戳，来避免缓存）。
13. 避免使用不可缓存且是外部HTTP请求的iFrame。

### 注意点
1. a标签的属性`target="_blank"`，在一些浏览器中，无论`href`值是什么内容（包括`#`和`javascript: void(0);`）都会打开新页面。
2. `absolute`元素用`top: 0; bottom: 0; left: 0; right: 0; _height: 100%; _width: 100%;`可以拉伸至父容器的高宽。
3. 没有设置宽度的`float`元素，其宽度等于子节点宽度：主流浏览器等于最外层子节点宽度，ie6等于所有子节点中最大的宽度。
4. `inline`或`inline-block`节点标签前可能导致其父级的宽度变大（其实是内联标签前面会有间隙，若拥有`font-size`之后便会有高度撑开），通过以下办法解决：

    1. 把`inline`节点设置为`block`。
    2. 给父级节点设置`font-size: 0;`（可用此方法排查是否是空格造成的）。
5. 页面是按照顺序加载资源，当且仅当有使用需求时才会去加载外部资源。

    已加载完成的CSS文件内有多个url请求（background），但仅在页面节点要引用某个url请求时（无论节点是否隐藏），才会去请求这个资源，而不是在加载CSS文件时就加载外部资源。
6. 使用动态DOM加载，代替内容的`display: none;`（有渲染）：

    1. `<script type="text/template"></script>`
    2. `<template></template>`
    3. `<textarea style="display:none;"></textarea>`
7. wap页面或支持伪类的浏览器，能用`:before/after`的就不要添加标签。
8. 单选、多选按钮开关自定义样式

    用`input:checked + 兄弟节点`（`<input type="radio">`或`<input type="checkbox">`）操作选项选中与否的不同样式；可以隐藏`input`元素，用自定义样式来制作单选框、复选框。完全代替JS。
9. Android2.3出现渲染问题可以在渲染错误的节点上添加`position: relative;`（类似ie6的haslayout）。