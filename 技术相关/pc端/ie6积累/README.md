#ie6积累

1. hack：
	- ie6: _
	- ie6 ie7 : *
	- ie6 ~ ie10: \9 
	- ie8 ~ ie10: \0

2. ie6使用float会导致双边距问题，用以下解决：
	- `float: left/right;_display: inline;`

3. ie6/7的display: inline-block无效，用以下解决：
	- `display: inline-block; *display: inline; zoom: 1;`

4. ie6闭合BFC，阻止外边距重叠，清除浮动，触发haslayout：
	- `zoom: 1;`

5. ie6的高度无法小于行高，用以下解决：
	- `overflow: hidden;`

6. ie6图片无法用png-24透明图，会把透明部分显示为灰色，可以使用js插件或用gulp压缩png图片使其可以在ie6下正常显示来修复：
	- 不依赖其他插件

        ``` html
        <!--[if IE 6]>
        <script src="js/pngfilter.js" ></script>
        <script>
            DD_belatedPNG.fix('.j-png');
        </script>
        <![endif]-->
        ```

	>插件问题：
	>用div透明背景图覆盖出圆角效果会单边缩短1px，要给背景图左右多出1px背景(js的bugs)。

7. ie6/7的底部3px间距：
	- `vertical-align: 任意值`
	- `float: 除了none之外任意值`

8. ie6不支持max/min-height/width：
	- 用下划线height/width固定值代替，没有最大最小效果

9. ie6字体渲染的高度和其他浏览器不同，line-height可能会渲染小一些：
	- 不处理，否则都要细微调节ie6情况下的`line-height`

10. ie6的text-decoration: underline的位置与其他主流浏览器不同，可以尝试：
	- 用`border-bottom`替代

11. ie6的:hover效果：
	- 仅支持a标签并且要有`href=某值`

12. ie6查看的网页文件若文件编码不是utf-8会乱码：
	- 无论html/css/js文件都要手动转化为**utf-8**

13. ie6的tr/tbody不支持border：
	- `border`写在 **td/td > div**

14. ie6的width/height/line-height写在td上时，内容超过后设置的限制无效：
	- `width/height/line-height`不写在td标签上，写在**td > div**
	- 在父级table标签上设置`table-layout: layout:fixed;`,并在第一个tr的各个子级td上设置宽度，就能为整个表固定各td宽度

15. ie6的table/tr/td，用js增加有背景色的class无效：
	- **table/tr/td**要有原始的`background`值，才可以在添加class之后改变background值

16. ie6下tr标签没有:hover效果：
	- 把tr标签的:hover效果用js表示

17. ie6浮动元素的中间有注释会导致出现重复字符：
	- 删除浮动元素内的注释

18. ie6不能使用多类选择器(不能连写class或id，e.g. .a.b/.a#b/#a#b)，会自动忽略前面的选择器而仅剩下最后一个class/id

19. ie6不支持position: fixed，需使用js组建：
	- 依赖jquery

        ``` html
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
	- input设display: block会跟父级上下有1px间距，用`float`解决

21. ie6/7不支持:focus，用以下解决：
	- 用js制作，又因为input问题多，在input外嵌套一层div，对其进行css样式修改
	- 渐进增强，放弃ie6/7下的:focus效果

22. ie6的子节点脱离文档流后，父节点要截断子节点内容，必须使父节点也脱离文档流：
	- 若要用overflow: hidden作用于position: relative/absolute的子节点，必须父级也设置`position: relative/absolute`
	- 若要用overflow: hidden作用于float的子节点，必须父级也`浮动`或`清除浮动`

23. ie6的z-index使用：
	- 使用此css属性的盒子和要覆盖的盒子之间，要把它们第一个共同父子之内的兄弟节点设置`position: relative/absolut`并且添加`z-index`(可以仅设置一方)才能对比覆盖

24. ie6的a:hover之后添加派生选择器css效果，e.g. a:hover .class{}：
	- 先要设置a:hover{}触发:hover时候的重绘(或重排)效果，可以用zoom: 1；再添加a:hover之后的派生选择器css效果，比如显示／隐藏
	
	>ie6用css控制子项根据父项a:hover的显示隐藏，仅作用于一些文本效果，因此还是要用js的方式替代此种效果：mouseenter时候添加一个类，类控制css来操作子项内容的显示隐藏；mouseleave时候去除此类

25. ie6的:hover的某些css属性值会导致高度变化，用以下解决：
	- 父级设置固定height，如果可以，也增加`zoom: 1`或`overflow: hidden`

26. ie6修改absolute的盒子为display: none会改变父级的height：
	- 父节点设定height，增加`overflow: hidden和position: relative`
	- 先show()出替换的内容，再hide()被替换的内容

27. ie6的一些奇怪展示问题：
	- 给能确定高度的盒子加入`height`和`width`，并对能添加如下属性的盒子添加`overflow: hidden;position: relative; zoom: 1;`

28. ie6/7的text-decoration会被overflow: hidden截断

29. ie6不支持css3的透明，可以用ie特有的滤镜：
	- 整个节点透明：`filter: alpha(opacity=50);/*必须激活haslayout，比如zoom: 1;*/`，等价于高级浏览器的`opacity:0.5;`
	- 仅仅背景透明，不影响子项内容：`filter: progid:DXImageTransform.Microsoft.Gradient(startColorStr=#40000000, endColorStr=#40000000);/*必须激活haslayout，比如zoom: 1;*/`，等价于高级浏览器的`background: rgba(0,0,0,.5);`

30. ie6没有console方法（执行会报错），可用alert替代：

	``` js
	if(typeof console === "undefined" || typeof console.log === "undefined") {
		console = {};
		console.log = function(msg){
			alert(msg);
		};
	}
	```
	
31. ie6下当子节点的宽度超过父节点设置的宽度时，会产生奇怪的样式效果，比如仅设置padding-top而会把padding-bottom也设置一样的值，处理方式为：计算好子节点不要超过父节点宽度

32. ie6下qrcode.js要先把节点展示出来才能够调用方法产生效果，调用完之后再隐藏节点不会有影响（算是插件bugs），ie6下是用table模拟效果

33. ie6下position: absolute的文字宽度，若不设置宽度值，其最大宽度等于吧父级宽度的一半，而在其他主流浏览器下最大宽度等于父级宽度，用以下解决
	- 此文字的节点设置`width固定值`
	- `white-space: nowrap`强制文本不换行

34. 
	>ie6的负margin有些情况需要多设置一些，因为可能出现不是设定值的情况

35. 
	>ie6的某些兄弟间节点间（比如img和span）因为出现比如overflow: hidden造成相对于基线会有对齐问题，用以下解决
	>`vertical: top;margin-top: …`

36. 
	>ie6下，用js改变节点高度，有时会导致盒子无法渲染到新的位置，可以尝试
	>   - 去除不必要的position: relative
	>   - 在父级加上`zoom: 1`

37. 
	>ie6下的absolute/float节点在页面重新渲染时，可能出现margin-left/maring-top的渲染问题，导致位置发生变化，用以下解决
	>用`margin-right/margin-bottom/padding`替代

38. 一些情况下，inline-block节点标签前后的空格导致出现占位的间隙
	- 把此节点设置为`display: block`（可通过设置浮动、绝对定位、固定定位，自动转换为block）
	- 给img父级设置`font-size: 0`(可用这个方法排查是不是其前后的空格导致)

39. 
	>ie6下调用的function在还未加载到的地方，因为兼容性差，会导致调用不成功的错误，受加载速度影响，其他高级浏览器不会出现类似情况
