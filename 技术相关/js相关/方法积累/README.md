#js方法积累

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

        var actionDom,
            initialX = 0,
            initialY = 0;

        self.movFuc = function (dom, x, y) {
            console.log(x, y);
            /* do sth...*/
        };

        function init(dom) {
            actionDom = dom;

            /* 不能用attachEvent、ontouchstart或jQuery绑定*/
            dom.addEventListener("touchstart", touchStart, false);
        }

        function touchStart(e) {
            initialX = e.touches[0].clientX;
            initialY = e.touches[0].clientY;

            actionDom.addEventListener("touchmove", touchMove, false);
        }

        function touchMove(e) {
            /* 阻止冒泡和默认行为*/
            e.stopPropagation();
            e.preventDefault();

            var x = e.touches[0].clientX - initialX,
                y = e.touches[0].clientY - initialY;

            initialX = e.touches[0].clientX;
            initialY = e.touches[0].clientY;

            self.movFuc(this, x, y);

            actionDom.addEventListener("touchend", function () {
                actionDom.removeEventListener("touchmove", touchMove, false);
            }, false);
        }

        init(dom);
    }

    /* 实例化使用*/
    new TouchMoveAction(document.getElementById("test"));
    ```

- js实现图片延时加载（依赖jQuery或zepto）

    ```javascript
    <img class="j-img" src="images/2.png" alt="" data-src="images/1.png">

    /* 图片延时加载的构造函数*/
    function ImgLazyLoad(className, func) {
        var self = this;

        var timeoutId;

        function init(className, func) {
            bindEvent(className);

            $(window).on('scroll', function () {
                bindEvent(className, func);
            });
        }

        function bindEvent(className, func) {    /* 绑定触发事件*/
            clearTimeout(timeoutId);
            timeoutId = setTimeout(function () {
                lazyLoad(getImgArr(className), className, func);
            }, 500);
        }

        function getImgArr(className, offset) { /* 获取屏幕内dom数组*/
            var $all = $('.' + className),
                minHeight = document.body.scrollTop || document.documentElement.scrollTop,
                maxHeight = minHeight + $(window).height(),
                domArr = [];

            if (typeof offset !== 'number') {
                offset = 50;
            }

            $all.each(function (index, element) {
                var elemHeight = $(element).offset().top;

                if (elemHeight <= maxHeight + offset && elemHeight >= minHeight - offset) {
                    domArr.push(element);
                }
            });

            return domArr;
        }

        function lazyLoad(domArr, className, func) { /* 图片延时加载*/
            $.each(domArr, function (index, value) {
                var $this = $(value);
                var src = $this.attr('data-src'),
                    newImg = new Image();

                if (src !== undefined) {
                    newImg.src = src;

                    if (newImg.complete) {  /* 缓存加载*/
                        $this.attr('src', src)
                            .removeAttr('data-src')
                            .removeClass(className);
                    } else {
                        newImg.onload = function () {   /* 新加载*/
                            $this.attr('src', src)
                                .removeAttr('data-src')
                                .removeClass(className);
                        };
                    }
                    if (typeof func === "function") {
                        func.call($this);
                    }
                }
            });
        }

        init(className, func);
    }

    /* 实例化使用*/
    new ImgLazyLoad('j-img', function () {
        console.log(this);
    });
    ```