#学习笔记

##CSS
- 限定布局宽度，让内容决定布局高度。

- z-index用于控制设置了absolute、relative或fixed定位的元素。应该只给有堆叠关系的节点设置此属性，而不要试图通过设定个别元素的z-index来确保元素不重叠。

- 用css创造三角形

    ```css
    div {
        border: 12px solid;
        border-color: transparent #000 transparent transparent;
        height: 0;
        width: 0;
    }
    ```

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
       /* font-size覆盖父级的字体*/
    }
    img {
       vertical-align: middle;
    }
    ```

- 响应式设计之媒体查询
    - css属性：`@media (min-width: 360px) and (max-width: 640px) {...}`
    - html标签：`<link rel="stylesheet" type="text/css" media="(min-width: 360px) and (max-width: 640px)" href="...">`

- 响应式设计三大要素
    - 媒体查询
    - 流式布局：节点用百分比
    - 弹性图片： `img {max-width: 100%;}`
    - wap可以用rem和html的font-size配合


##JavaScript
- if中用赋值（大部分是误用）并非总是返回真值，条件判断赋值内容Boolen后为假即判断为假：`if(a = false){...}`。

- JS性能
    - 平稳退化：当浏览器不支持或禁用了JS功能后，访问者也能完成最基本的内容访问。
        - 为JS代码预留出退路（html使用常规链接，用js事件绑定去拦截浏览器默认行为）
            >`<a href="真实地址" class="j-func">...</a>`

        - ~~伪协议(javascript:)~~
            >`<a href="javascript: func();">...</a>`

        - ~~内嵌事件处理函数~~
            >`<a href="#" onclick="func();return false;">...</a>`

    - 渐进增强：对具体某功能支持的判断，并向后兼容，用一些额外信息层去包裹原始内容。
    - 向后兼容：确保老版本浏览器功能，使之虽不能支持某些功能，但仍能基本访问。
        - 对象检测：`if(func){func();}`
        - ~~浏览器嗅探技术~~
    - 资源分离：把样式表和脚本分离出html。
        - 使用外部资源。
        - 不在html上用事件处理函数。
        - 对只为DOM增添的内容，转移到外部资源中动态创建。
    - 性能提升。
        - 减少访问DOM（搜索结果保存在变量中）。
        - 减少外链请求数量（合并js、css、图片）。
        - 压缩资源。
        - 脚本放置在`</body>`前。

- js实现类似jQuery的`$(function(){})`方法

    ```javascript
    function onloads(func) {
        var oldOnLoad = window.onload;

        if (typeof window.onload !== 'function') { /* 未绑定*/
            window.onload = func;
        } else {  /* 已绑定*/
            window.onload = function () {
                oldOnLoad();
                func();
            };
        }
    }
    ```
    
- js实现类似jQuery的after方法
    ```javascript
    function after(elem, target) {
        var parent = target.parentNode;

        if (parent.lastChild == target) {
            parent.appendChild(elem);
        } else {
            parent.insertBefore(elem, target.nextSibling);
        }
    }
    ```

- js实现wap触屏滚动距离模拟构造函数

    ```javascript
    /* wap触屏滚动距离模拟的构造函数*/
    function TouchMoveAction(dom) {
        var self = this;

        self.actionDom = null;
        self.initialX = 0;
        self.initialY = 0;
        self.movFuc = function (dom, x, y) {
            console.log(x, y);
            /* do sth...*/
        };

        function init(dom) {
            self.actionDom = dom;

            /* 不能用attachEvent、ontouchstart或jQuery绑定*/
            dom.addEventListener("touchstart", touchStart, false);
        }

        function touchStart(e) {
            self.initialX = e.touches[0].clientX;
            self.initialY = e.touches[0].clientY;

            self.actionDom.addEventListener("touchmove", touchMove, false);
        }

        function touchMove(e) {
            /* 阻止冒泡和默认行为*/
            e.stopPropagation();
            e.preventDefault();

            var x = e.touches[0].clientX - self.initialX,
                y = e.touches[0].clientY - self.initialY;

            self.initialX = e.touches[0].clientX;
            self.initialY = e.touches[0].clientY;

            self.movFuc(this, x, y);

            self.actionDom.addEventListener("touchend", function () {
                self.actionDom.removeEventListener("touchmove", touchMove, false);
            }, false);
        }

        init(dom);
    }

    /* 实例化使用*/
    var a = new TouchMoveAction(document.getElementById("aa"));
    ```