# 兼容至ie6

>若要兼容低版本ie，需要在制作页面时就做向前兼容，最好不要在完成页面之后才开始修改渲染错乱的页面。

## 目录
1. [兼容ie的手段](#兼容ie的手段)
1. [haslayout](#haslayout)
1. [ie6的bug调试](#ie6的bug调试)

---
### 兼容ie的手段
1. 根据不同的ie版本进行操作（hack）

    1. CSS属性：

        1. ie6：`_`(在属性之前)。
        2. ie6、ie7：`*`(在属性之前)。
        3. ie6、ie7、ie8(部分ie9、ie10)：`\9`（在属性结束、分号之前）。
        4. ie8、ie9、ie10、ie11：`\0`（在属性结束、分号之前）。
    2. HTML条件注释法：

        >HTML条件注释法仅支持ie9-。支持的判断：`lt`小于；`lte`小于或等于；`gt`大于；`gte`大于或等于；`()`；`!`；`&`；`|`。

        1. ie9-按条件执行（非ie浏览器和ie10+都当做注释不执行）：

            ```html
            <!--[if lt IE 8]>
            ie6、ie7
            <![endif]-->

            <!--[if IE 8]>
            ie8
            <![endif]-->

            <!--[if gte IE 8]>
            ie8、ie9
            <![endif]-->
            ```
        2. 非ie浏览器和ie10+都无差别执行，ie9-按条件执行：

            ```html
            <!--[if gte IE 8]><!-->
            ie8、ie9、ie10+、其他非ie
            <!--<![endif]-->

            <!--[if !IE]><!-->
            ie10+、其他非ie
            <!--<![endif]-->
            ```
    3. JS判断：

        >策略：`navigator.userAgent`正则匹配（浏览器嗅探技术）、HTML条件注释法、怪癖检测（`try-catch`）。

        1. [HTML条件注释法判断ie6、7、8、9版本](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/JS方法积累/实用方法/README.md#原生js判断ie6789版本)。
        2. [用户代理判断ie所有版本](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/JS方法积累/实用方法/README.md#原生js判断ie所有版本)。

    ><details>
    ><summary>图片类型选择png-24透明图（png-32）</summary>
    >
    >1. 用gulp压缩图片后，图片在ie6~8表现出的颜色会改变，因此不要把背景切入图中，最好用透明的切图。
    >2. **png-24透明图（png-32）**和**png-24不透明图**或**png-8**压缩后的文件大小相差不大，因此可以都使用**png-24透明图**切图后再用gulp压缩。
    >3. png24透明图增加透明区域对文件大小增加很小，因此切图时不必特意限制纯透明区域大小。
    >4. 判断png类型：`file 文件名`
    >
    >    ```shell
    >    file *
    >    # 输出：
    >    /png-24.png:    PNG image data, 宽 x 高, 8-bit/color RGB, non-interlaced
    >    /png-32.png:    PNG image data, 宽 x 高, 8-bit/color RGBA, non-interlaced
    >    /png-8.png:     PNG image data, 宽 x 高, 8-bit colormap, non-interlaced
    >    ```
    ></details>
2. ie6/7替换写法：

    1. `float`：

        ```css
        float: left/right;
        _display: inline;
        ```
    2. `display: inline-block`：

        ```css
        display: inline-block;
        *display: inline;
        *zoom: 1;
        ```
    3. `.clearfix:after {content: ""; display: table; clear: both;}`

        ```css
        .clearfix {*zoom: 1;}
        ```
3. ie6的高度无法小于行高：

    - `_overflow: hidden;`（尤其对于设置背景的节点）
4. 兼容至ie6的：`position: absolute;`元素拉升至父容器（`position: relative;`）相同高宽：

    - `top: 0; bottom: 0; left: 0; right: 0; _height: 100%; _width: 100%;`
5. ie6图片无法用png-24透明图（png-32），会把透明部分显示为灰色：

    1. gulp压缩图片：

        用png-24透明图（png-32）切图，再用gulp压缩。

    2. ~~JS方法~~：

        ><details>
        ><summary>内部插件</summary>
        >
        >``` html
        ><!--[if IE 6]>
        ><script src="js/pngfilter.js"></script>
        ><script>
        >    DD_belatedPNG.fix('.j-png');
        ></script>
        ><![endif]-->
        >```
        >插件bug：用div透明背景图覆盖出圆角效果会单边缩短1px，要给背景图左右多出1px背景(JS的bug)。
        ></details>
6. ie6不支持`max-height`、`min-height`、`max-width`、`min-width`：

    - 用`_height/_width`等于固定值适量替代。
7. ie6字体渲染的高度和其他浏览器不同，`line-height`可能会渲染小一些：

    - 不处理，否则都要细微调节ie6的行高。
8. ie6的`text-decoration: underline;`的位置与其他主流浏览器不同：

    1. 不处理。
    2. 用`border-bottom`替代。
9. ie6的`:hover`效果：

    - 仅支持`<a>`且`href`属性要赋值

        `<a href="#"></a>`
10. ie6查看的网页文件若文件编码不是**utf-8**会乱码（若出现除了ie6之外都无错误，并且提示的错误位置排查后没有错误的，需要检查编码格式）：

    - 无论HTML/CSS/JS文件都要手动转化为**utf-8**。
11. ie6的`<tr>`、`<tbody>`不支持`border`：

    - `border`写在`td`或`td > *`中。
12. ie6的`width`、`height`、`line-height`写在`<td>`上时，内容超过后设置的限制无效：

    1. 在父级`<table>`上设置`table-layout: fixed;`，并在第一个`<tr>`的各个子级`<td>`或`<th>`上设置宽度，就能为整个表固定各项目宽度。
    2. `width`、`height`、`line-height`不设置在`<td>`上，设置在`<td>`的子级。
13. ie6的`<table>`、`<tr>`、`<td>`，用JS增加有背景色的class无效：

    - 要有原始的`background`值，才可以在添加class之后改变background值。
14. ie6下`<tr>`没有`:hover`效果：

    1. 用JS制作（mouseenter、mouseleave）。
    2. 不处理。平稳退化（优先完成全部功能，再针对浏览器测试和修复）。
15. ie6浮动元素的中间有注释会导致出现重复字符：

    - 删除浮动元素内的注释。
16. ie6不能使用**多类选择器**（不能连写class或id，e.g. `.a.b`、`.a#b`、`#a#b`），会自动忽略前面的选择器而仅剩下最后一个class或id。

    - 用`_`CSS属性hack，对ie6中平稳退化。
17. ie6不支持`position: fixed;`，需使用JS组建：

    1. 平稳退化。用`position: absolute;`模拟。
    2. 用JS插件：

        ><details>
        ><summary>内部插件</summary>
        >
        >``` html
        ><script src="js/jquery.js"></script>
        ><script src="js/ks.gototop.js"></script><!-- 依赖jQuery-->
        >
        ><script>
        >    ue.gototop({
        >        relative: $('.content-wrapper'),    // 相对定位的对象
        >        target: $('#j-sidenav'),    // gototop对象，必须设置具体width
        >        top/bottom: 270,    // 距离顶部或底部的高度
        >        left/right: 25,    // 距离相对定位对象的距离
        >        scrollTop: 123,     // y轴滚动条滚动到这个位置显示gototop对象，默认：0
        >        fade: false,    // 是否开启针对ie6取消渐隐渐现，默认：开启
        >        btn: $('#btn'),    // 到达scrollTop位置以内会隐藏
        >        onscroll: function () {    // 滚动页面回调函数
        >        }
        >    });
        ></script>
        >```
        ></details>
18. ie6的`<input>`有很多CSS问题，尽量不要设置复杂的CSS效果在`<input>`上：

    - `<input>`设`display: block;`会跟父级上下有1px间距，用`float`解决。
19. ie6/7不支持`:focus`：

    1. 用JS制作，又因为`<input>`问题多，在`<input>`外嵌套一层`<div>`，对其进行CSS样式修改。
    2. 平稳退化。
20. ie6/7的子节点脱离文档流后，父节点要截断子节点内容，必须使父节点也脱离文档流：

    1. 若要用`overflow: hidden;`作用于`position: relative/absolute;`的子节点，必须父级也设置`position: relative/absolute;`。
    2. 若要用`overflow: hidden;`作用于`float`的子节点，必须父级也`浮动`或`清除浮动`。
21. 若ie6/7下内置滚动条无法滚动，给产生滚动条的容器添加`position: relative;`（应该也是截断文档流问题）。
22. ie6的`z-index`使用：

    - 节点与要覆盖的节点之间，它们的第一个共同父级内的兄弟节点（2个节点分别的父级）设置`position: relative/absolute;`并且添加`z-index`（可以仅设置一方）才能对比覆盖。
23. ie6修改`absolute`的盒子为`display: none`会改变父级的高度：

    1. 父节点设定`height`，增加`overflow: hidden;`和`position: relative;`。
    2. 先`show()`出替换的内容，再`hide()`被替换的内容。
24. ie6的`a:hover`之后添加派生选择器CSS效果：

    >e.g. `a:hover .class{}`

    - 先要设置`a:hover{}`触发`:hover`时候的重绘（或重排）效果（可以用`zoom: 1;`），再添加`a:hover`之后的派生选择器CSS效果，如：显示/隐藏。

    >ie6用CSS控制子项根据父项`a:hover`的显示隐藏，仅作用于一些文本效果，因此还是要用JS的方式替代此种效果：mouseenter时候添加一个类，类控制CSS来操作子项内容的显示隐藏；mouseleave时候去除此类。
25. ie6的`:hover`的某些CSS属性值会导致高度变化，其实是触发了**haslayout**，可以设置CSS属性使`:hover`之前就已经haslayout。
26. ie6/7的`text-decoration`会被`overflow: hidden;`截断。
27. ie6/7/8不支持CSS3的透明，可以用ie特有的滤镜：

    1. 整个节点透明：

        1. ie6/7

            ```css
            filter: alpha(opacity=50);
            *zoom: 1;
            ```

        2. 现代浏览器

            `opacity: 0.5;`
    2. 仅仅背景透明，不影响子项内容：

        1. ie6/7/8/9

            ```css
            filter: progid:DXImageTransform.Microsoft.Gradient(startColorStr=#80000000, endColorStr=#80000000)\9;
            *zoom: 1;
            ```

            >- `startColorStr`是起色点，`endColorStr`是终色点（用于渐变色），两个值相同则单色；
            >- 值为16进制数，前两位表示alpha通道值（透明），后六位为RGB值。
        2. ie9+

            1. `background: rgba(0, 0, 0, .5);`
            2. 使用gif透明图（ie的24位PNG图透明时引起的内存泄漏）。
28. ie6/7/8/9没有console方法（执行会报错），可用alert替代：

    ```js
    if (typeof console === 'undefined' || typeof console.log === 'undefined') {
      console = {}
      console.log = function (msg) {
        alert(msg)
      }
    }
    ```
29. ie6下当子节点的宽度超过父节点设置的宽度时，会产生奇怪的样式效果，如：仅设置`padding-top`而会把`padding-bottom`也设置一样的值：

    - 计算好子节点不要超过父节点宽度。
30. ie6下[qrcode.js](https://github.com/davidshimjs/qrcodejs)要先把节点展示出来才能够调用方法产生效果，调用完之后再隐藏节点不会有影响（ie6下是用table模拟效果）。
31. ie6下`position: absolute`的文字宽度，若不设置宽度值，其最大宽度等于父级宽度的一半，而在其他主流浏览器下最大宽度等于父级宽度：

    1. 此文字的节点设置`width固定值`。
    2. `white-space: nowrap;`强制文本不换行。
32. ie6的`负margin`有些情况需要多设置一些，因为可能出现子节点内容超过设定值的情况。
33. ie6的某些兄弟节点间（如：`<img>`和其他`inline`或`inline-block`节点）因为出现如：`overflow: hidden;`造成相对于基线会有对齐问题：

    1. `vertical: top; margin-top: 某px;`
    2. 只对ie6进行hack操作，`_vertical-align: baseline; _margin-top: 某px;`或`_vertical-align: -某px;`。
34. ie6下的`absolute/float`节点在页面重新渲染时，可能出现`margin-left`、`maring-top`的渲染问题，导致位置发生变化：

    - 用`padding`、`margin-right`、`margin-bottom`替代。
35. ie6下调用的`function`在还未加载到的地方，因为兼容性差，会导致调用不成功的错误，受加载速度影响，现代浏览器不会出现类似情况。
36. ie6下，父级为`float`，其子级要根据内容宽度自适应：

    - ~~子级为`display: block;`，若要设置`height`就必须要设置`width`，否者会导致子级铺满父级。~~
    - **子级或子级包裹的内容设置为`display: inline-block; *display: inline; *zoom: 1;`，可以仅设置`height`，不用设定`width`。**
37. ie6下，图片类型直接改变后缀名会导致无法打开；当把`.jpg`的文件后缀保存为`.png`在ie6显示时，会阻塞之后所有图片的加载。
38. ie6下因为hover或改变视窗大小或改变DOM位置而导致元素高度变化（甚至移动到看不见地方）：

    - 可以试着往其父级层层向上增加`zoom: 1;`进行测试，若还是不行则在有高度的地方设置`overflow: hidden;`，甚至是最顶端的位置添加才可以修复（有时候基本是向上试错的碰运气）。
39. ie6下父级设置`height`、`width`，当子级超过限制后，会把父级撑大（没有`overflow: hidden;`情况）。
40. 若ie6下无法打开https链接：

    - 尝试**internet选项－－高级－－使用TLS1.0打钩**。
41. ie6/7（/8的低版本或怪异模式）的`document.getElementById`不区分**ID**大小写，CSS样式会区分大小写。
42. ie6/7的`document.getElementById`会获取`name`属性匹配的节点（如：表单节点或其他节点）：

    - 不要让节点的`name`属性与其他节点ID相同。
43. ie6/7/8/9的节点在Flash上可能需要添加`background`才可以点击到。

### haslayout

haslayout是ie6/7的一个私有概念，它决定了元素**如何对其内容定位和尺寸计算**，以及与其他元素的关系和相互作用。

若一个元素「拥有布局」，它会负责本身及其后代元素的尺寸和定位；若一个元素「没有拥有布局」，它的尺寸和位置由最近的拥有布局的祖先元素控制。

>对于早期的ie显示引擎来说，若所有元素都「拥有布局」的话，会导致很大的性能问题。因此ie开发团队决定使用布局概念来减少浏览器的性能开销，即只将布局应用于实际需要的那些元素，所以便出现了「拥有布局」和「没有拥有布局」两种情况。

1. 查看haslayout

    1. 可以用JS读取某DOM对象是否拥有布局（只读）：

        `某DOM.currentStyle.hasLayout;`，返回true：拥有，返回false：不拥有。

    2. 通过**IE Developer Toolbar**（打开*Show Default Style Values*）可以查看ie下HTML元素是否拥有布局（只读）：

        拥有`haslayout`的元素，属性显示为`haslayout = -1`；不拥有的，显示为`haslayout = 0`。
2. 默认拥有布局的元素：

    ```html
    html, body
    table, tr, th, td
    img
    hr
    input, select, textarea, button
    iframe, embed, object
    ```
3. 触发haslayout

    haslayout不是CSS属性，我们无法通过CSS显式的设置元素的haslayout，只能通过其他CSS样式触发。

    1. ie6/7：

        1. `float: left/right;`
        2. `display: inline-block;`
        3. `position: absolute;`
        4. `width: 除了auto之外任何值;`
        5. `height: 除了auto之外任何值;`
        6. `zoom: 除了normal之外任何值;`
        7. `writing-mode: tb-rl;`
    2. ie7独有

        1. `min-height: 任意值;`
        2. `min-width: 任意值;`
        3. `max-height: 除了none之外任意值;`
        4. `max-width: 除了none之外任意值;`
        5. `overflow: 除了visible之外任意值，仅用于块级元素;`
        6. `overflow-x: 除了visible之外任意值，仅用于块级元素;`
        7. `overflow-y: 除了visible之外任意值，仅用于块级元素;`
        8. `position: fixed;`

>一个「layout元素」只可能是一个**默认就拥有 layout 的元素**或一个**通过设置某些 CSS 属性得到 layout的元素**。
>
>ie6/7没有BFC，而有haslayout。

### ie6的bug调试
1. 尝试在Chrome下重现该bug，若能重现，就先把Chrome里能重现的bug修复。确定Chrome里不重现、但是ie6有问题的，再继续下一步；
2. 先尝试高版本ie（如：开发者工具还不错的ie9），可以断点、调用栈分析、控制台。若ie9里没问题，那就继续尝试ie8，一直定位到能重现该问题的最高版本的ie上。若不幸碰上仅出现在ie6的bug，再继续下一步；
3. ie6没有太好用的JS调试工具，一般就是**二分法**+`alert`的土法定位到出错行，加上耐心和时间，还有一点点运气。可以使用抓包工具辅助（Charles）；用虚拟机安装windows XP系统并且在ie6上安装IE6DevToolBar。
