#js方法积累——实用方法

## 原生js方法

### *原生js*实现类似jQuery的`$(document).ready(function () {});`
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

### *原生js*实现类似jQuery的`.after()`
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

### *原生js*实现类似jQuery的`.next()`
```javascript
function getNextElement(node) {
    if (node === null || node.nextSibling === null) {
        return null;
    } else if (node.nextSibling.nodeType === 1) {
        return node.nextSibling;
    } else {
        return getNextElement(node.nextSibling);
    }
}
```

### *原生js*实现类似jQuery的`.addClass()`
```javascript
function addClass(node, newClassName) {
    var oldNames, i;

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

### *原生js*实现类似jQuery的`.removeClass()`
```javascript
function removeClass(node, removeClassName) {
    var newNames = [],
        flag = false,
        oldNames, i;

    if (node.className) {
        oldNames = node.className.split(' ');
        for (i = 0; i < oldNames.length; i++) {
            if (removeClassName !== oldNames[i]) {
                newNames.push(oldNames[i]);
            } else {
                flag = true;
            }
        }
        node.className = newNames.join(' ');
    }

    return flag;
}
```

### *原生js*实现类似jQuery的`$('html,body').animate({'scrollLeft': 像素, 'scrollTop': 像素}, 毫秒);`
```javascript
/*
 * 滚动到
 * @param {Number} endX 到达x轴像素
 * @param {Number} endY 到达y轴像素
 * @param {Number} time 所用毫秒
 * @returns undefined
 */
function animateTo(endX, endY, time) {
    var scrollFromX = document.body.scrollLeft || document.documentElement.scrollLeft,
        scrollFromY = document.body.scrollTop || document.documentElement.scrollTop,
        scrollToX = endX > document.documentElement.scrollWidth ? document.documentElement.scrollWidth : endX,
        scrollToY = endY > document.documentElement.scrollHeight ? document.documentElement.scrollHeight : endY,
        i = 0,
        runEvery = 5,
        myself = arguments.callee;

    time /= runEvery;

    clearInterval(myself.setIntervalId);

    myself.setIntervalId = setInterval(function () {
        i++;

        window.scrollTo((scrollToX - scrollFromX) / time * i + scrollFromX, (scrollToY - scrollFromY) / time * i + scrollFromY);

        if (i >= time) {
            clearInterval(myself.setIntervalId);
        }
    }, runEvery);
}
```

### *原生js*移动端获取触屏滚动距离(可改写为鼠标拖拽功能)
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

### *原生js*判断浏览器`userAgent`
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

### *原生js*判断ie各版本
```javascript
function isIE(num) {
    var dom = document.createElement("b");

    dom.innerHTML = "<!--[if IE " + num + "]><i></i><![endif]-->";

    return dom.getElementsByTagName("i").length;
}
```

### *原生js*操作cookie
```javascript
var cookieFuc = {
    get: function (name) {   /* 获取指定cookie*/
        var cookieArr = document.cookie.split("; "),
            cookieValue, i, temArr;

        for (i = 0; i < cookieArr.length; i++) {
            temArr = cookieArr[i].split("=");
            if (name === temArr[0]) {
                cookieValue = unescape(temArr[1]);
                break;
            }
        }

        return cookieValue;
    },
    set: function (c_name, value, days) {   /* 设置cookie*/
        var expiresDays = new Date();

        expiresDays.setDate(expiresDays.getDate() + days);
        document.cookie = c_name + "=" + escape(value) + ((typeof days === 'number') ? ';expires=' + expiresDays.toGMTString() : '');
    }
};
```

### *原生js*加入收藏夹
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

### *原生js*判断版本（e.g. 1.1.1）是否较低
```javascript
function isLowerVersion(version, base) {
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

### *原生js*选取范围内随机值
```javascript
/*
 * 选取范围内随机值
 * @param {Number} lowerNum 下限
 * @param {Number} upperNum 上限
 * @returns {Number} 上下限区间内的随机值
 */
function selectFrom(lowerNum, upperNum) {
    var choices = upperNum - lowerNum + 1;

    return Math.floor(Math.random() * choices + lowerNum);
}
```

### *原生js*格式化文件属性（大小、日期）
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

### *原生js*倒计时显示
```javascript
/*
 * 显示倒计时
 * @param {Number} deadline 将来的时间戳（秒）
 * @param {String} id 输出节点id
 * @param {Function} func 到点后的回调函数
 * @param {String} hType ‘时’后面的文字
 * @param {String} mType ‘分’后面的文字
 * @param {String} sType ‘秒’后面的文字
 * @returns undefined
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
        var now = (Date.parse(new Date())) / 1000,
            time = Math.round(deadline - now);

        var s, m, h;

        if (time < 0) {
            clearInterval(intervalId);
            if (typeof func === 'function') {
                func();
            }
            return;
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

### *原生js*判断对象是否为空
```javascript
function isObjEmpty(obj) {
    var i;

    if (obj !== Object(obj)) {  /* 参数不是对象*/
        throw new TypeError('参数不是对象');
    } else if (typeof Object.keys === "function") { /* ie9+及高级浏览器支持*/

        return Object.keys(obj).length === 0;
    } else {
        for (i in obj) {
            if (obj.hasOwnProperty(i)) {

                return false;
            }
        }

        return true;
    }
}
```

### *原生js*移动端模拟点击事件（避免300毫秒click）
```javascript
var start_x, start_y;

document.getElementById('...').addEventListener('touchstart', function (e) {
    start_x = e.changedTouches[0].clientX;
    start_y = e.changedTouches[0].clientY;
}, false);

document.getElementById('...').addEventListener('touchend', function (e) {
    var end_x = e.changedTouches[0].clientX,
        end_y = e.changedTouches[0].clientY;

    if (Math.abs(end_x - start_x) > 5 || Math.abs(end_y - start_y) > 5) {   /* 滑动则不是点击*/
        return false;
    }

    /* do click*/
}, false);
```

### *原生js*判断是否是数组
```javascript
function isArray(value) {
    if (typeof Array.isArray === "function") {    /* ie8及以下不支持*/

        return Array.isArray(value);
    } else {

        return Object.prototype.toString.call(value) === "[Object Array]";  /* instanceof不能跨帧*/
    }
}
```

### *原生js*深复制（仅针对原始类型、数组和最基本的对象，以及他们的组合）
```javascript
/*
 * @param {Object|Array|Undefined|Null|Boolean|Number|String} obj 深复制参数
 */
function deepCopy(obj) {
    var i, newObj;

    if (typeof obj !== 'object' || obj === null) {

        return obj;
    }

    newObj = Object.prototype.toString.call(obj) === '[object Array]' ? [] : {};
    for (i in obj) {
        newObj[i] = arguments.callee(obj[i]);
    }

    return newObj;
}
```

### *原生js*对象合二为一（改变第一个参数）
```javascript
function extend(target, options) {
    var copy, name;

    for (name in options) {
        copy = options[name];

        if (Object.prototype.toString.call(copy) === '[object Array]') {
            target[name] = arguments.callee([], copy);
        } else if (Object.prototype.toString.call(copy) === '[object Object]') {
            target[name] = arguments.callee(target[name] ? target[name] : {}, copy);
        } else {
            target[name] = options[name];
        }
    }

    return target;
}
```

### *原生js*从字符串中获取绝对路径
```javascript
function getAbsoluteUrl(url) {
    var domA;

    if (typeof url === 'undefined') {

        return document.location.href;
    } else {
        domA = document.createElement('a');
        domA.href = url;

        return domA.href;
    }
}
```

### *原生js*判断事件在浏览器是否存在
```javascript
/*
 * 判断DOM节点是否支持某事件
 * @param {String} eventName 事件名
 * @param {Object} element DOM的Document对象
 * @returns {Boolean} [true|false]
 */
function isEventSupported(eventName, element) {
    var tagNames = {
            'select': 'input',
            'change': 'input',
            'submit': 'form',
            'reset': 'form',
            'error': 'img',
            'load': 'img',
            'abort': 'img'
        },
        isSupported;

    element = element || document.createElement(tagNames[eventName] || 'div');
    eventName = 'on' + eventName;

    isSupported = eventName in element;

    if (!isSupported) {
        if (!element.setAttribute) {    /* 若节点没有setAttribute方法，则改用div节点进行测试*/
            element = document.createElement('div');
        }
        if (element.setAttribute && element.removeAttribute) {
            element.setAttribute(eventName, '');
            isSupported = typeof element[eventName] === 'function';

            if (element[eventName] !== undefined) { /* 内存回收*/
                element[eventName] = undefined;
            }
            element.removeAttribute(eventName); /* 内存回收*/
        }
    }

    element = null; /* 内存回收*/

    return isSupported;
}
```

### *原生js*用整数进行小数的四则运算（避免浮点数运算误差）
```javascript
var fourOperations = {
    add: function (arg1, arg2) {    /* 加*/
        var r1, r2, m, c, cm,
            int1 = Number(arg1.toString().replace('.', '')),
            int2 = Number(arg2.toString().replace('.', ''));

        try {
            r1 = arg1.toString().split('.')[1].length;
        } catch (e) {
            r1 = 0;
        }
        try {
            r2 = arg2.toString().split('.')[1].length;
        } catch (e) {
            r2 = 0;
        }

        c = Math.abs(r1 - r2);
        m = Math.pow(10, Math.max(r1, r2));

        if (c > 0) {
            cm = Math.pow(10, c);

            if (r1 > r2) {
                int2 = int2 * cm;
            } else {
                int1 = int1 * cm;
            }
        }

        return (int1 + int2) / m;
    },
    sub: function (arg1, arg2) {    /* 减*/

        return this.add(arg1, -arg2);
    },
    mul: function (arg1, arg2) {    /* 乘*/
        var m;

        try {
            m = arg1.toString().split('.')[1].length;
        } catch (e) {
            m = 0;
        }
        try {
            m = m + arg2.toString().split('.')[1].length;
        } catch (e) {

        }

        return Number(arg1.toString().replace('.', '')) * Number(arg2.toString().replace('.', '')) / Math.pow(10, m);
    },
    div: function (arg1, arg2) {    /* 除*/
        var r1, r2;

        try {
            r1 = arg1.toString().split('.')[1].length;
        } catch (e) {
            r1 = 0;
        }
        try {
            r2 = arg2.toString().split('.')[1].length;
        } catch (e) {
            r2 = 0;
        }

        return (Number(arg1.toString().replace('.', '')) / Number(arg2.toString().replace('.', ''))) * Math.pow(10, r2 - r1);
    }
};
```

### *原生js*用请求图片作log统计
```javascript
var sendLog = (function () {
    var _unique = (function () {    /* 产生唯一标识*/
        var time = (new Date()).getTime() + '_',
            i = 0;

        return function () {
            return time + (i++);
        }
    }());

    var run = function (url) {
        var data = window['imgLogData'] || (window['imgLogData'] = {}),
            img = new Image(),
            uid = _unique();

        data[uid] = img;    /* 防止img被垃圾处理*/

        img.onload = img.onerror = function () {    /* 成功或失败后销毁对象*/
            img.onload = img.onerror = null;
            img = null;
            delete data[uid];
        };

        img.src = url + '&_cache=' + uid;   /* 发送统计内容*/
    };

    return run;
}());


sendLog('统计url');
```

### *原生js*绑定、解绑事件
```javascript
/* 绑定*/
function addEvent(obj, type, handle) {
    if (typeof obj.addEventListener === 'function') {   /* DOM2级，除ie6~8外的高级浏览器*/
        obj.addEventListener(type, handle, false);
    } else if (typeof obj.attachEvent === 'function') { /* 所有ie浏览器*/
        obj.attachEvent('on' + type, handle);
    } else {    /* DOM0级，最早期的浏览器都支持*/
        obj['on' + type] = handle;
    }
}

addEvent(document.getElementById('test1'), 'keydown', func1);


/* 解绑*/
function removeEvent(obj, type, handle) {
    if (typeof obj.removeEventListener === 'function') {
        obj.removeEventListener(type, handle, false);
    } else if (typeof obj.detachEvent === 'function') {
        obj.detachEvent('on' + type, handle);
    } else {
        obj['on' + type] = null;
    }
}

removeEvent(document.getElementById('test1'), 'keydown', func1);
```

`addEventListener`与`removeEventListener`是高级浏览器都有的方法（ie8-不支持），必须一一对应具体的handle和布尔值，才可以解绑。

`attachEvent`与`detachEvent`是ie特有方法，必须一一对应具体的handle，才可以解绑。

`on+type`是所有浏览器都支持，用赋值覆盖解绑。

jQuery的`on`与`off`，不用一一对应某个handle：当写具体handle时解绑那个具体handle；不写默认解绑所有对象下某事件的方法。

### *原生js*、jQuery获取事件对象引用、目标元素引用
ie8-的DOM0事件（直接on+type）没有传递**事件对象**到**事件处理函数**中，有额外的`window.event`对象进行相关操作。

```javascript
/* js原生*/
function getEvent(event) {
    return event || window.event;
}
function getTarget(event) {
    if (event && event.target) {

        return event.target;
    } else {

        return window.event.srcElement;
    }
}

/* jQuery*/
$('...').on('...', function (e) {
    /* 可以直接使用事件对象引用e和目标引用e.target*/
});
```

### *原生js*、jQuery阻止冒泡和阻止浏览器默认行为
- 阻止冒泡
    ```javascript
    /* js原生*/
    function stopBubble(e) {
        if (e && e.stopPropagation) {
            e.stopPropagation();
        } else {
            window.event.cancelBubble = true;
        }
    }

    /* jQuery*/
    $('...').on('...', function (e) {
        e.stopPropagation();
    });
    ```
- 阻止默认行为
    ```javascript
    /* js原生*/
    function stopDefault(e) {
        if (e && e.preventDefault) {
            e.preventDefault();
        } else {
            window.event.returnValue = false;
        }
        return false;
    }

    /* jQuery*/
    $('...').on('...', function (e) {
        e.preventDefault();
    });
    ```
- 阻止冒泡&阻止默认行为
    ```javascript
    /* js原生*/
    function returnFalse(e) {
        if (e && e.stopPropagation) {
            e.stopPropagation();
            e.preventDefault();
        } else {
            window.event.cancelBubble = true;
            window.event.returnValue = false;
        }
        return false;
    }

    /* jQuery*/
    $('...').on('...', function () {
        return false;
    });
    ```

### *原生js*、jQuery实现判断按下具体某键值
```javascript
/* js原生*/
function checkKeyCode(event) {
    var e = event || window.event,
        keyCode = e.charCode || e.keyCode;  /* 获取键值*/

    if (keyCode === 13) {   /* 查询键值表 例:13->换行*/
        /* 具体操作...*/

        /* 取消默认行为*/
        if (window.event) {
            window.event.returnValue = false;
        } else {
            event.preventDefault();
        }
    }
}

addEvent(document.getElementById('test'), 'keydown', checkKeyCode);  /* 上面绑定事件*/


/* jQuery*/
$(...).on('keydown', function (e) {
    if (e.which === 13) {   /* 查询键值表 例:13->换行*/
        /* 具体操作...*/

        return false;   /* 取消默认行为*/
    }
});
```


## jQuery（或Zepto）方法

### jQuery或Zepto图片延时加载
```html
<img class="方法类" src="默认图地址" data-src="真实图地址">

<script>
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
                screenTop = document.body.scrollTop || document.documentElement.scrollTop,
                screenBottom = screenTop + $(window).height(),
                domArr = [];

            if (typeof offset !== 'number') {
                offset = 50;
            }

            $all.each(function (index, element) {
                var elemHeight = $(element).offset().top;

                if (elemHeight <= screenBottom + offset && elemHeight >= screenTop - offset) {
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
</script>
```

### jQuery或Zepto滚动加载
```html
<!-- data-next：是否还可以加载；data-status：是否正在加载-->
<div class="j-load" data-status="loading" data-next="123">触发滚动加载</div>

<script type="text/javascript">
    $(function () {
        function loadMore(next) {
            var $load = $('.j-load');

            if (next !== -1 && $load.length >= 1) {
                if ($load.attr('data-status') === 'loading') {
                    $load.attr('data-status', '');

                    $.ajax({
                        url: '',
                        dataType: 'json',
                        data: {}
                    }).done(function (data) {
                        /* do sth.*/

                        if (false/* 某条件*/) {   /* 不再加载*/
                            $(window).off('scroll.loading');
                        } else {
                            $load.attr('data-status', 'loading');
                            autoLoadMore($load.attr('data-next'));
                        }
                    }).fail(function () {
                        console.log("网络错误");
                        $load.attr('data-status', 'loading');
                    });
                }
            } else {
                $(window).off('scroll.postmore');
            }
        }

        function autoLoadMore(next) {   /* 若文档内容小于视窗则再次加载*/
            if ($(window).height() >= $(document).height()) {
                loadMore(next);
            }
        }

        var $load = $('.j-load'),
            scrollSetTimeoutId;

        autoLoadMore(parseInt($load.attr('data-next')));

        $(window).on('scroll.loading', function () {
            clearTimeout(scrollSetTimeoutId);
            scrollSetTimeoutId = setTimeout(function () {
                if ((+$(window).scrollTop() + $(window).height()) >= $load.offset().top) {  /* 滚动到屏幕内*/
                    loadMore(parseInt($load.attr('data-next')));
                }
            }, 200);
        });
    });
</script>
```

### jQuery或Zepto获取`HTTP response header`信息
```javascript
function getResponseHeaders(requestName) {
    var text;

    $.ajax({
        type: 'HEAD',
        url: document.location.href,
        async: false,
        complete: function (xhr, data) {
            var responseHeaders, headerArr, i;

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

### jQuery修复html标签`placeholder`属性无效
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

### jQuery或Zepto弹出toast
```javascript
/* jQuery*/
function alertToast(text) {
    if ($('.j-pop-text').length === 0) {
        $('body').append('<div class="j-pop-text 样式类" style="display: none;"></div>');
    }

    var $popText = $('.j-pop-text'),
        myself = arguments.callee;

    clearTimeout(myself.setTimeoutId);

    text = text || 'warning';
    $popText.text(text);

    $popText.show(function () {
        myself.setTimeoutId = setTimeout(function () {
            $popText.fadeOut();
        }, 2500);
    });
}
```
```html
<style>
    .hidden {
        display: none;
    }
</style>
<script >
    /* Zepto*/
    function alertToast(text) {
        if ($('.j-pop-text').length === 0) {
            $('body').append('<div class="j-pop-text hidden 样式类"></div>');  /* .hidden {display: none !important;}*/
        }

        var $popText = $('.j-pop-text');

        clearTimeout(arguments.callee.setTimeoutId);

        text = text || 'warning';
        $popText.text(text).removeClass('hidden');

        arguments.callee.setTimeoutId = setTimeout(function () {
            $popText.addClass('hidden').text('');
        }, 2500);
    }
</script>
```

### jQuery全选、取消全选
```html
所有：
<input type="checkbox" name="all">

单个：
<input type="checkbox" name="ones">
<input type="checkbox" name="ones">
<input type="checkbox" name="ones">
...
```
```javascript
var $allInput = $('[name="all"]'),
    $oneInput = $('[name="ones"]');

$allInput.on('click', function () {
    $oneInput.prop('checked', this.checked);
});

$oneInput.on('click', function () {
    var flag = true;

    $oneInput.each(function () {
        if (!this.checked) {
            flag = false;

            return false;
        }
    });

    $allInput.prop('checked', flag);
});
```

### jQuery节点跟随屏幕滚动
```javascript
/*
 * 跟随屏幕滚动
 * @param {wrapper} String 跟随节点的父级
 * @param {dependent} String 跟随节点的父级的兄弟参照物
 * @param {target} String 跟随节点
 * @returns undefined
 */
(function (wrapper, dependent, target) {
    var $wrapper = $(wrapper),
        wrapperHeight = $wrapper.height(),
        $dependent = $wrapper.siblings(dependent),
        max = $dependent.height() - wrapperHeight,
        $target = $(target),
        $targetPrev = $target.prev(),
        startOffset = $targetPrev.offset().top + $targetPrev.height();

    $(window).on('scroll', function () {
        var scollTop = $(document).scrollTop(),
            marginTop = 0;

        if (scollTop > startOffset) {
            marginTop = scollTop - startOffset;

            if (marginTop > max) {
                marginTop = max;
            }
        }

        $target.css({"marginTop": marginTop});
    });
}('.father', '.dependent', '.target'));
```

### jQuery或Zepto模拟手机翻转（使页面都以“横屏”展示）
```html
<style>
    .dom {
        position: fixed;
        top: 0;
        left: 0;
    }
    .reversal {
        top: 50%;
        left: 50%;
        -webkit-transform: translate(-50%, -50%) rotate(90deg);
        transform: translate(-50%, -50%) rotate(90deg);
    }
</style>

<div class="dom" id="j-dom-1">...</div>
<div class="dom" id="j-dom-2">...</div>

<script type="text/javascript">
    var reversalAct = {
        setTimeoutId1: '',
        setTimeoutId2: '',
        init: function (selector, className) {
            var self = this;

            var resizeEvent = "onorientationchange" in window ? "orientationchange" : "resize";

            $(window).on('resize', function () {
                clearTimeout(self.setTimeoutId2);

                self.setTimeoutId2 = setTimeout(function () {
                    self.resize(selector);
                }, 500);
            }).on(resizeEvent, function () {
                clearTimeout(self.setTimeoutId1);

                self.setTimeoutId1 = setTimeout(function () {
                    self.portrait(selector, className);
                }, 500);
            });

            self.resize(selector);

            self.portrait(selector, className);
        },
        portrait: function (selector, className) {    /* 屏幕高度>宽度（竖屏），增加“顺时针翻转90度的类”*/
            var $dom = $(selector);

            if ($(window).height() > $(window).width()) {
                $dom.addClass(className);
            } else {
                $dom.removeClass(className);
            }
        },
        resize: function (selector) {   /* 设置高宽的值（边长较长的一边设置为宽度，较短的设置为高度）*/
            var wHeight = $(window).height(),
                wWidth = $(window).width(),
                i;

            if (wHeight > wWidth) {
                i = wHeight;
                wHeight = wWidth;
                wWidth = i;
            }

            $(selector).css({'width': wWidth + 'px', 'height': wHeight + 'px'});
        }
    };

    reversalAct.init('#j-dom-1, #j-dom-2', 'reversal');
</script>
```

### jQuery或Zepto点击指定区域以外执行函数
1. jQuery

    ```javascript
    function beyongOneAct($dom, callback, namespace) {
        $(document.body).on('click.' + namespace, function (e) {
            var $area = $dom;

            if (!$area.is(e.target) && $area.has(e.target).length === 0) {    /* 点击不在指定区域内*/
                $(document.body).off('click.' + namespace);

                if (typeof callback === 'function') {
                    callback();
                }
            }
        });
    }
    ```
    [JSFiddle Demo](https://jsfiddle.net/realgeoffrey/enyxz9a6/)
2. Zepto

    ```javascript
    /*
     * 点击指定区域以外执行函数
     * @$dom {Object} jQuery节点
     * @callback {Function} 回调函数
     * @namespace {String} 事件命名空间
     * @returns undefined
     */
    function beyongOneAct($dom, callback, namespace) {
        $(document.body).on('click.' + namespace, function (e) {
            var $area = $dom,
                withinArea = false,
                i;
    
            for (i = 0; i < $area.length; i++) {
                if ($area.get(i) === e.target || $area.eq(i).has(e.target).length !== 0) {
                    withinArea = true;
                    break;
                }
            }
    
            if (!withinArea) {    /* 点击不在指定区域内*/
                $(document.body).off('click.' + namespace);
    
                if (typeof callback === 'function') {
                    callback();
                }
            }
        });
    }
    ```
    [JSFiddle Demo](https://jsfiddle.net/realgeoffrey/mvv9wxnw/)