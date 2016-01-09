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