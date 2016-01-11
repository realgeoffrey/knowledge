#js方法积累

- js实现类似jQuery的`$(function(){})`

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
    
- js实现类似jQuery的`after`

    ```javascript
    function insertAfter(elem, target) {
        var parent = target.parentNode;

        if (parent.lastChild == target) {
            parent.appendChild(elem);
        } else {
            parent.insertBefore(elem, target.nextSibling);
        }
    }
    ```

- js实现类似jQuery的`next`

    ```javascript
    function getNextElement(node) {
        if (node.nextSibling.nodeType === 1) {
            return node.nextSibling;
        } else if (node.nextSibling !== null) {
            return getNextElement(node.nextSibling);
        } else {
            return null;
        }
    }
    ```

- js实现类似jQuery的`addClass`

    ```javascript
    function addClass(node, newClassName) {
        var oldNames,
            i;

        if (!node.className) {
            node.className = newClassName;
        } else {
            oldNames = node.className.split(' ');
            for (i = 0; i < oldNames.length; i++) {
                if (newClassName === oldNames[i]) {
                    return false;
                }
            }
            node.className = node.className + ' ' + newClassName;
        }

        return true;
    }
    ```

- js移动端获取触屏滚动距离

    ```javascript
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

- jQuery或zepto图片延时加载

    ```javascript
    <img class="j-img" src="images/2.png" alt="" data-src="images/1.png">

    function ImgLazyLoad(className, func) {
        var self = this;

        var timeoutId,
            timeStamp = (new Date()).valueOf(); /* 事件命名空间*/

        function init(className, func) {
            bindEvent(className);

            $(window).on('scroll' + '.' + timeStamp, function () {
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

        self.unbindEvent = function () {    /* 解绑事件绑定*/
            $(window).off('scroll' + '.' + timeStamp);
        };

        init(className, func);
    }


    var test = new ImgLazyLoad('j-img', function () {
        console.log(this);
    });

    test.unbindEvent();
    ```

- js判断浏览器`userAgent`

    ```javascript
    var snifBrowser = {
        isWebkit: false,
        isSafari: false,
        isIDevice: false,
        isIpad: false,
        isIphone: false,
        isAndroid: false,
        isMobile: false,
        isWechat: false,
        device: '',
        version: '',
        standalone: '',
        init: function () {
            var navigator = window.navigator,
                userAgent = navigator.userAgent,
                ios = userAgent.match(/(iPad|iPhone|iPod)[^;]*;.+OS\s([\d_\.]+)/),
                android = userAgent.match(/(Android)[\s|\/]([\d\.]+)/);

            this.isWebkit = /WebKit\/[\d.]+/i.test(userAgent);
            this.isSafari = ios ? (navigator.standalone ? this.isWebkit : (/Safari/i.test(userAgent) && !/CriOS/i.test(userAgent) && !/MQQBrowser/i.test(userAgent))) : false;

            if (ios) {
                this.device = ios[1];
                this.version = ios[2].replace(/_/g, '.');
                this.isIDevice = (/iphone|ipad|ipod/i).test(navigator.appVersion);
                this.isIpad = userAgent.match(/iPad/i);
                this.isIphone = userAgent.match(/iPhone/i);
            } else if (android) {
                this.version = android[2];
                this.isAndroid = (/android/i).test(navigator.appVersion);
            }

            this.isMobile = this.isAndroid || this.isIDevice;
            this.standalone = navigator.standalone;
            this.isWechat = userAgent.indexOf("MicroMessenger") >= 0;
        }
    };

    snifBrowser.init();
    ```

- js判断IE各版本

    ```javascript
    function isIE(num) {
        var dom = document.createElement("b");

        dom.innerHTML = "<!--[if IE " + num + "]><i></i><![endif]-->";

        return dom.getElementsByTagName("i").length;
    }
    ```

- js操作cookie

    ```javascript
    var cookieFuc = {
        getCookie: function (name) {   /* 获取指定cookie*/
            var cookieArr = document.cookie.split("; "),
                cookieValue,
                i,
                temArr;

            for (i = 0; i < cookieArr.length; i++) {
                temArr = cookieArr[i].split("=");
                if (name === temArr[0]) {
                    cookieValue = unescape(temArr[1]);
                    break;
                }
            }

            return cookieValue;
        },
        setCookie: function (c_name, value, days) {   /* 设置cookie*/
            var expiresDays = new Date();

            expiresDays.setDate(expiresDays.getDate() + days);
            document.cookie = c_name + "=" + escape(value) + ((typeof days === 'number') ? ';expires=' + expiresDays.toGMTString() : '');
        }
    };
    ```

- jQuery或zepto获取`response header`信息

    ```javascript
    function getResponseHeaders(requestName) {
        var text;

        $.ajax({
            type: 'HEAD',
            url: document.location.href,
            async: false,
            complete: function (xhr, data) {
                var responseHeaders,
                    headerArr,
                    i;

                if (data !== "error" && data !== "timeout" && data !== "parsererror") {
                    responseHeaders = xhr.getAllResponseHeaders();

                    if (requestName) {
                        requestName += ": ";
                        headerArr = responseHeaders.split(/[\r\n]+/);

                        for (i = 0; i < headerArr.length; i++) {
                            if (headerArr[i].indexOf(requestName) === 0) {
                                text = headerArr[i].slice(requestName.length);
                                break;
                            }
                        }
                    } else {
                        text = responseHeaders;
                    }
                } else {
                    alert("获取头信息: " + data);
                }
            }
        });

        return text;
    }
    ```

- jQuery修复html标签`placeholder`属性无效

    ```javascript
    function fixPlaceholder($dom) {
        var $input = $dom || $('input, textarea');

        if (!('placeholder' in document.createElement("input"))) {
            $input.each(function (index, element) {
                var placeText = $(element).attr('placeholder');

                if ($(element).val() === '') {
                    $(element).val(placeText);
                }

                $(this).on('focus', function () {
                    if ($(this).val() === placeText) {
                        $(this).val('');
                    }
                }).on('blur', function () {
                    if ($(this).val() === '') {
                        $(this).val(placeText);
                    }
                });
            });
        }
    }
    ```

- js加入收藏夹

    ```javascript
    function addFavorite(url, title) {  /* url必须带有协议头*/
        if (window.external && 'addFavorite' in window.external) {
            window.external.addFavorite(url, title);
        } else if (window.sidebar && window.sidebar.addPanel) {
            window.sidebar.addPanel(url, title);
        } else if (window.opera && window.print) {
            this.title = title;
            return true;
        } else {
            alert('加入收藏失败，请使用' + (navigator.userAgent.toLowerCase().indexOf('mac') !== -1 ? 'Command/Cmd' : 'Ctrl') + '+D 进行添加');
        }
    }
    ```

- js实现类似jQuery的`$('html,body').animate({'scrollTop':scrollTo},time);`（scrollTo和time是变量）

    ```javascript
    function animateToTop(scrollTo, time) { /* time毫秒*/
        var scrollFrom = parseInt(document.body.scrollTop),
            i = 0,
            runEvery = 5;

        time /= runEvery;

        var interval = setInterval(function () {
            i++;
            document.body.scrollTop = (parseInt(scrollTo) - scrollFrom) / time * i + scrollFrom;
            if (i >= time) {
                clearInterval(interval);
            }
        }, runEvery);
    }
    ```

- js判断version是否较低

    ```javascript
    function lowerVersion(version, base) {
        var arr1 = version.toString().split('.'),
            arr2 = base.toString().split('.'),
            length = arr1.length > arr2.length ? arr1.length : arr2.length,
            i;

        /* 两值不同*/
        for (i = 0; i < length; i++) {
            if (arr1[i] !== arr2[i]) {

                return parseInt(arr1[i]) < parseInt(arr2[i]);
            }
        }

        /* 两值相同*/
        return false;
    }
    ```

- js格式化文件属性

    ```javascript
    var format = {
        fileSize: function (bytes) {    /* 格式化文件大小*/
            if (bytes === 0) {
                return '0';
            }
            var rate = 1024,
                units = ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
                exponent = Math.floor(Math.log(bytes) / Math.log(rate));

            return (bytes / Math.pow(rate, exponent)).toPrecision(3) + units[exponent];
        },
        date: function (date, fmt) {    /* 格式化日期*/
            var o = {
                    "M+": date.getMonth() + 1, /* 月*/
                    "d+": date.getDate(), /* 日*/
                    "h+": date.getHours() % 12 === 0 ? 12 : date.getHours() % 12, /* 12小时制*/
                    "H+": date.getHours(), /* 24小时制*/
                    "m+": date.getMinutes(), /* 分*/
                    "s+": date.getSeconds(), /* 秒*/
                    "q+": Math.floor((date.getMonth() + 3) / 3), /* 季度*/
                    "S": date.getMilliseconds() /* 毫秒*/
                },
                week = {
                    /* [{E:"一"},{EE:"周一"},{EEE+:"星期一"}]*/
                    "0": "一",
                    "1": "二",
                    "2": "三",
                    "3": "四",
                    "4": "五",
                    "5": "六",
                    "6": "日"
                },
                i;

            if (/(y+)/.test(fmt)) {
                fmt = fmt.replace(RegExp.$1, (date.getFullYear() + "").substr(4 - RegExp.$1.length));
            }
            if (/(E+)/.test(fmt)) {
                fmt = fmt.replace(RegExp.$1, ((RegExp.$1.length > 1) ? (RegExp.$1.length > 2 ? "星期" : "周") : "") + week[date.getDay() + ""]);
            }
            for (i in o) {
                if (new RegExp("(" + i + ")").test(fmt)) {
                    fmt = fmt.replace(RegExp.$1, (RegExp.$1.length === 1) ? (o[i]) : (("00" + o[i]).substr(("" + o[i]).length)));
                }
            }

            return fmt;
        }
    };
    ```

- js倒计时显示

    ```javascript
    /*
     * @deadline：将来的时间戳（秒）
     * @id：输出节点id
     * @func：到点后的回调函数
     * @hType：'时'后面的文字
     * @mType：'分'后面的文字
     * @sType：'秒'后面的文字
     */
    function countDown(deadline, id, func, hType, mType, sType) {
        function formatNum(number) {    /* 格式化数字格式*/
            if (number < 10) {
                return '0' + number;
            } else {
                return number;
            }
        }

        hType = hType || ' ';
        mType = mType || ' ';
        sType = sType || ' ';

        var intervalId = setInterval(function () {
            var now = (Date.parse(new Date())) / 1000;
            var time = Math.round(deadline - now);

            var s, m, h;

            if (time < 0) {
                clearInterval(intervalId);
                if (typeof func === 'function') {
                    func();
                }
                return true;
            }
            h = formatNum(Math.floor(time / (60 * 60)));
            m = formatNum(Math.floor((time - (h * 60 * 60)) / 60));
            s = formatNum(time % 60);
            if (document.getElementById(id)) {
                document.getElementById(id).innerHTML = h + hType + m + mType + s + sType;
            } else {
                console.log(h + hType + m + mType + s + sType);
            }
        }, 1000);
    }
    ```