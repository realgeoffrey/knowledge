## 遇到的问题

1. hack：
	- ie6：`_`(在属性之前)。
	- ie6、ie7：`*`(在属性之前)。
	- ie6 ~ ie10：`\9`（在属性结束、分号之前）。
	- ie8 ~ ie10：`\0`（在属性结束、分号之前）。

2. ie6、ie7替换写法：
	- `float`：

	    `float: left/right;_display: inline;`
    - `display: inline-block`：

        `display: inline-block;*display: inline;zoom: 1;`

5. ie6的高度无法小于行高，用以下解决：
	- `overflow: hidden;`，尤其对于背景图片

6. ie6图片无法用png-24透明图，会把透明部分显示为灰色，用以下解决：
    - gulp压缩图片。

	- js方法，比较麻烦，不建议

        ``` html
        <!--[if IE 6]>
        <script src="js/pngfilter.js"></script>
        <script>
            DD_belatedPNG.fix('.j-png');
        </script>
        <![endif]-->
        ```

        >插件问题：用div透明背景图覆盖出圆角效果会单边缩短1px，要给背景图左右多出1px背景(js的bugs)。

8. ie6不支持`max-height/min-height/max-width/min-width`：
	- 用`_height/_width`等于固定值适量代替

9. ie6字体渲染的高度和其他浏览器不同，`line-height`可能会渲染小一些：
	- 不处理，否则都要细微调节ie6情况下的`line-height`

10. ie6的`text-decoration: underline`的位置与其他主流浏览器不同，可以尝试：
	- 用`border-bottom`替代

11. ie6的:hover效果：
	- 仅支持a标签并且要有`href=某值`

12. ie6查看的网页文件若文件编码不是utf-8会乱码。若出现除ie6外都无错误并且提示的错误位置排查后没有错误的，需要检查编码格式：
	- 无论html/css/js文件都要手动转化为**utf-8**

13. ie6的`tr/tbody`不支持`border`：
	- `border`写在`td/td > div`中

14. ie6的`width/height/line-height`写在td上时，内容超过后设置的限制无效：
	- `width/height/line-height`不写在td标签上，写在`td > div`中
	- 在父级table标签上设置`table-layout: layout:fixed;`,并在第一个tr的各个子级td上设置宽度，就能为整个表固定各td宽度

15. ie6的`table/tr/td`，用js增加有背景色的class无效：
	- 要有原始的`background`值，才可以在添加class之后改变background值

16. ie6下tr标签没有`:hover`效果：
	- 把tr标签的`:hover`效果用js制作
	- 优雅降级

17. ie6浮动元素的中间有注释会导致出现重复字符：
	- 删除浮动元素内的注释

18. ie6不能使用多类选择器(不能连写class或id，e.g. `.a.b/.a#b/#a#b`)，会自动忽略前面的选择器而仅剩下最后一个class/id

19. ie6不支持`position: fixed`，需使用js组建：

    ``` html
    <script src="js/jquery.js"></script>
    <script src="js/ks.gototop.js"></script>
    <script>
        ue.gototop({
            relative: $(".content_wrapper"),	// 相对定位的对象
            target: $('#j-sidenav'),	// gototop对象，必须设置具体width
            top/bottom: 270,	// 距离顶部或者底部的高度
            left/right: 25,	// 距离相对定位对象的距离
            scrollTop: 123, 	// y轴滚动条滚动到这个位置显示gototop对象 默认0
            fade: false,	// 是否开启针对ie6取消渐隐渐现 默认开启
            btn: $('#btn'),	// 到达scrollTop位置以内会隐藏
            onscroll: function(){	// 滚动页面回调函数
        }
        });
    </script>
    ```

20. ie6的input标签有很多css问题，尽量不要设置复杂的css效果在input标签上：
	- input设`display: block`会跟父级上下有1px间距，用`float`解决

21. ie6/7不支持`:focus`，用以下解决：
	- 用js制作，又因为input问题多，在input外嵌套一层div，对其进行css样式修改
	- 优雅降级

22. ie6的子节点脱离文档流后，父节点要截断子节点内容，必须使父节点也脱离文档流：
	- 若要用`overflow: hidden`作用于`position: relative/absolute`的子节点，必须父级也设置`position: relative/absolute`
	- 若要用`overflow: hidden`作用于`float`的子节点，必须父级也`浮动`或`清除浮动`

23. ie6的`z-index`使用：
	- 节点与要覆盖的节点之间，它们的第一个共同父级内的兄弟节点（2个节点分别的父级）设置`position: relative/absolut`并且添加`z-index`(可以仅设置一方)才能对比覆盖

24. ie6的`a:hover`之后添加派生选择器css效果，e.g. `a:hover .class{}`：
	- 先要设置`a:hover{}`触发`:hover`时候的重绘(或重排)效果，可以用`zoom: 1`再添加`a:hover`之后的派生选择器css效果，比如显示／隐藏
	
	>ie6用css控制子项根据父项`a:hover`的显示隐藏，仅作用于一些文本效果，因此还是要用js的方式替代此种效果：mouseenter时候添加一个类，类控制css来操作子项内容的显示隐藏；mouseleave时候去除此类

25. ie6的`:hover`的某些css属性值会导致高度变化，其实是触发了haslayout，可以设置css属性使`:hover`之前就已经haslayout

26. ie6修改`absolute`的盒子为`display: none`会改变父级的`height`（可能也是haslayout作祟）：
	- 父节点设定`height`，增加`overflow: hidden和position: relative`
	- 先show()出替换的内容，再hide()被替换的内容

28. ie6/7的`text-decoration`会被`overflow: hidden`截断

29. ie6不支持css3的透明，可以用ie特有的滤镜：
	- 整个节点透明：

	    `filter: alpha(opacity=50);/*必须激活haslayout，比如zoom: 1;*/`；

	    高级浏览器：`opacity: 0.5;`
	- 仅仅背景透明，不影响子项内容：

	    `filter: progid:DXImageTransform.Microsoft.Gradient(startColorStr=#40000000, endColorStr=#40000000);/*必须激活haslayout，比如zoom: 1;*/`；

	    高级浏览器：`background: rgba(0,0,0,.5);`

30. ie6没有console方法（执行会报错），可用alert替代：

	``` js
	if(typeof console === "undefined" || typeof console.log === "undefined") {
		console = {};
		console.log = function(msg){
			alert(msg);
		};
	}
	```
	
31. ie6下当子节点的宽度超过父节点设置的宽度时，会产生奇怪的样式效果，比如仅设置`padding-top`而会把`padding-bottom`也设置一样的值，用以下解决：

    计算好子节点不要超过父节点宽度

32. ie6下qrcode.js要先把节点展示出来才能够调用方法产生效果，调用完之后再隐藏节点不会有影响（算是插件bugs），ie6下是用table模拟效果

33. ie6下`position: absolute`的文字宽度，若不设置宽度值，其最大宽度等于吧父级宽度的一半，而在其他主流浏览器下最大宽度等于父级宽度，用以下解决
	- 此文字的节点设置`width固定值`
	- `white-space: nowrap`强制文本不换行

34. 
	>ie6的负margin有些情况需要多设置一些，因为可能出现不是设定值的情况

35. 
	>ie6的某些兄弟间节点间（比如img和span）因为出现比如`overflow: hidden`造成相对于基线会有对齐问题，用以下解决
	>`vertical: top;margin-top: …`

37. 
	>ie6下的`absolute/float`节点在页面重新渲染时，可能出现`margin-left/maring-top`的渲染问题，导致位置发生变化，用以下解决
	>用`margin-right/margin-bottom/padding`替代

38. 一些情况下，`inline-block`节点标签前后的空格导致出现占位的间隙
	- 把此节点设置为`display: block`（可通过设置浮动、绝对定位、固定定位，自动转换为block）
	- 给img父级设置`font-size: 0`(可用这个方法排查是不是其前后的空格导致)

39. 
	>ie6下调用的function在还未加载到的地方，因为兼容性差，会导致调用不成功的错误，受加载速度影响，其他高级浏览器不会出现类似情况

40. ie6下，父级为`float`，其子级要根据内容宽度自适应：

    - ~~子级为`display: block;`，若要设置`height`就必须要设置`width`，否者会导致子级铺满父级。~~
    - 子级设置为`display: inline-block;*display: inline;zoom: 1;`，可以仅设置`height`，不用设定`width`。


## haslayout

layout是ie6、ie7的一个私有概念，它决定了元素如何对其内容定位和尺寸计算，以及与其他元素的关系和相互作用。当一个元素“拥有布局”时，它会负责本身及其子元素的尺寸和定位。而如果一个元素“没有拥有布局”，那么它的尺寸和位置由最近的拥有布局的祖先元素控制。

对于早期的IE显示引擎来说，如果所有元素都“拥有布局”的话，会导致很大的性能问题。因此IE开发团队决定使用布局概念来减少浏览器的性能开销，即只将布局应用于实际需要的那些元素，所以便出现了“拥有布局”和“没有拥有布局”两种情况。

- 默认拥有布局的元素：

    ```html
    html, body
    table
    tr, td, th
    img
    hr
    input, select, textarea, button
    iframe, embed, object, applet
    marquee
    ```
- 查看haslayout

    haslayout不是css属性，我们无法通过css显式的设置元素的haslayout。

    可以用js读取某dom对象是否拥有布局（只读）：`document.getElementById('某id').currentStyle.hasLayout;`，返回布尔值。
- 触发haslayout

    - ie6、7：

        ```css
        float: left/right;
        display: inline-block;
        position: absolute;
        width: 除auto外任何值;
        height: 除auto外任何值;
        zoom: 除normal外任何值;
        writing-mode: tb-rl;
        ```
    - ie7独有

        ```css
        min-height: 任意值;
        min-width: 任意值;
        max-height: 除none 外任意值;
        max-width: 除none 外任意值;
        overflow: 除visible外任意值，仅用于块级元素;
        overflow-x: 除visible 外任意值，仅用于块级元素;
        overflow-y: 除visible 外任意值，仅用于块级元素;
        position: fixed;
        ```