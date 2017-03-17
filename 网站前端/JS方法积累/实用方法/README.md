# JS方法积累——实用方法

## 原生JS方法

### *原生JS*用`setTimeout`模拟`setInterval`
```javascript
/**
 * 用setTimeout模拟setInterval
 * @constructor
 * @param {Function} func - 循环执行函数
 * @param {Number} millisecond - 间隔毫秒
 */
function SetInterval(func, millisecond) {
    var _setIntervalId;

    if (typeof func === 'function') {
        _setIntervalId = setTimeout(function () {
            _setIntervalId = setTimeout(arguments.callee, millisecond);

            func();
        }, millisecond);
    }

    this.stop = function () {
        clearTimeout(_setIntervalId);
    };
}


/* 使用测试*/
var a = new SetInterval(function () {
    console.log(1);

    if (...) {
        a.stop();
    }
}, 1000);

//a.stop();
```

### *原生JS*`requestAnimationFrame`的递归
```javascript
/**
 * 每一帧都执行一次func
 * @constructor
 * @param {Function} func - 执行的函数
 */
function RepeatRAF(func) {
    var _repeatRAFId;

    if (typeof func === 'function') {
        _repeatRAFId = requestAnimationFrame(function () {
            _repeatRAFId = requestAnimationFrame(arguments.callee);

            func();
        });
    }

    this.stop = function () {
        cancelAnimationFrame(_repeatRAFId);
    };
}


/* 使用测试*/
var a = new RepeatRAF(function () {
    console.log(1);

    if (...) {
        a.stop();
    }
});

//a.stop();
```

### *原生JS*实现类似jQuery的`$('html,body').animate({'scrollLeft': 像素, 'scrollTop': 像素}, 毫秒);`
```javascript
/**
 * 滚动到x、y轴指定位置
 * @param {Number} endX - 到达x轴像素
 * @param {Number} endY - 到达y轴像素
 * @param {Number} time - 所用毫秒
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
>使用[velocity动画库](https://github.com/julianshapiro/velocity)（[中文文档](http://www.mrfront.com/docs/velocity.js/)）做所有的动画（包括JS和CSS）才是最简单且性能最佳的选择。
>比如滚动到某位置：`$('html').velocity('scroll', {offset: y轴像素, duration: 毫秒});`。

### *原生JS*移动端获取触屏滚动距离(可改写为鼠标拖拽功能)
```javascript
function touchMoveAct(dom) {
    var beginX,
        beginY;

    function _touchStart(e) {
        beginX = e.touches[0].clientX;
        beginY = e.touches[0].clientY;

        dom.addEventListener('touchmove', _touchMove, false);
    }

    function _touchMove(e) {
        e.stopPropagation();
        e.preventDefault();

        var offsetX = e.touches[0].clientX - beginX,
            offsetY = e.touches[0].clientY - beginY;

        beginX = e.touches[0].clientX;
        beginY = e.touches[0].clientY;

        _movFuc(this, offsetX, offsetY);
    }

    function _movFuc(dom, x, y) {
        console.log(x, y);
        /* do sth...*/
    }

    dom.addEventListener('touchstart', _touchStart, false);

    dom.addEventListener('touchend', function () {
        dom.removeEventListener('touchmove', _touchMove, false);
    }, false);
}


/* 使用测试*/
touchMoveAct(document.getElementById('test'));
```
>可以用`mousedown`、`mousemove`代替`touchstart`、`touchmove`来改写成鼠标拖拽。

### *原生JS*判断浏览器userAgent（`window.navigator`）
```javascript
function SnifBrowser() {
    var self = this;

    self.isWebkit = false;
    self.isSafari = false;
    self.isIOS = false;
    self.isIpad = false;
    self.isIphone = false;
    self.isAndroid = false;
    self.isMobile = false;
    self.isWechat = false;
    self.device = '';
    self.version = '';
    self.standalone = '';

    var _init = function () {
        var navigator = window.navigator,
            userAgent = navigator.userAgent,
            ios = userAgent.match(/(iPad|iPhone|iPod)[^;]*;.+OS\s([\d_\.]+)/),
            android = userAgent.match(/(Android)[\s|\/]([\d\.]+)/);

        self.isWebkit = /WebKit\/[\d.]+/i.test(userAgent);
        self.isSafari = ios ? (navigator.standalone ? self.isWebkit : (/Safari/i.test(userAgent) && !/CriOS/i.test(userAgent) && !/MQQBrowser/i.test(userAgent))) : false;

        if (ios) {
            self.device = ios[1];
            self.version = ios[2].replace(/_/g, '.');
            self.isIOS = (/iphone|ipad|ipod/i).test(navigator.appVersion);
            self.isIpad = userAgent.match(/iPad/i) || false;
            self.isIphone = userAgent.match(/iPhone/i) || false;
        } else if (android) {
            self.device = android[1];
            self.version = android[2];
            self.isAndroid = (/android/i).test(navigator.appVersion);
        }

        self.isMobile = self.isAndroid || self.isIOS;
        self.standalone = navigator.standalone || false;
        self.isWechat = userAgent.indexOf('MicroMessenger') >= 0;
    };

    _init();
}


/* 使用测试*/
var a = new SnifBrowser();
```

### *原生JS*判断ie6、7、8、9版本
```javascript
/**
 * 判断ie6、7、8、9版本
 * @param {Number|String} [num] - ie版本号。可填6、7、8、9；若为空则只要是ie6~9则返回1
 * @returns {Number} - 0 或 1
 */
function isIE(num) {
    var dom = document.createElement('b');

    dom.innerHTML = '<!--[if IE ' + num + ']><i></i><![endif]-->';

    return dom.getElementsByTagName('i').length;
}
```

### *原生JS*判断ie所有版本
```javascript
/**
 * 判断ie所有版本
 * @returns {Number} - ie版本号 或 false
 */
function detectIE() {
    var ua = window.navigator.userAgent;

    var msie = ua.indexOf('MSIE ');
    if (msie > 0) {

        /* ie10- 返回版本号*/
        return parseInt(ua.substring(msie + 5, ua.indexOf('.', msie)), 10);
    }

    var trident = ua.indexOf('Trident/');
    if (trident > 0) {
        var rv = ua.indexOf('rv:');

        /* ie11 返回版本号*/
        return parseInt(ua.substring(rv + 3, ua.indexOf('.', rv)), 10);
    }

    var edge = ua.indexOf('Edge/');
    if (edge > 0) {

        /* Edge(ie 12+) 返回版本号*/
        return parseInt(ua.substring(edge + 5, ua.indexOf('.', edge)), 10);
    }

    /* 其他浏览器 返回false*/
    return false;
}
```

### *原生JS*操作cookie
```javascript
var cookieFuc = {
        /**
         * 读取一个cookie
         * @param {String} sKey - cookie名
         * @returns {String|Null} - cookie值 或 null
         */
        getItem: function (sKey) {

            return decodeURIComponent(document.cookie.replace(new RegExp("(?:(?:^|.*;)\\s*" + encodeURIComponent(sKey).replace(/[\-\.\+\*]/g, "\\$&") + "\\s*\\=\\s*([^;]*).*$)|^.*$"), "$1")) || null;
        },

        /**
         * 创建或覆盖一个cookie
         * @param {String} sKey - cookie名
         * @param {String} sValue - cookie值
         * @param {Number|Date|String|Infinity} [vEnd] - cookie过期时间。默认关闭浏览器后过期
         * @param {String} [sPath] - cookie路径。默认为当前文档位置的路径
         * @param {String} [sDomain] - cookie域名。默认为当前文档位置的路径的域名部分
         * @param {Boolean} [bSecure] - cookie是否“仅通过https协议传输”。默认否
         * @returns {Boolean} - 操作成功或失败
         */
        setItem: function (sKey, sValue, vEnd, sPath, sDomain, bSecure) {
            if (!sKey || /^(?:expires|max\-age|path|domain|secure)$/i.test(sKey)) {

                return false;
            }

            var sExpires = "";

            if (vEnd) {
                switch (vEnd.constructor) {
                    case Number:
                        sExpires = vEnd === Infinity ? "; expires=Fri, 31 Dec 9999 23:59:59 GMT" : "; max-age=" + vEnd;
                        break;
                    case String:
                        sExpires = "; expires=" + vEnd;
                        break;
                    case Date:
                        sExpires = "; expires=" + vEnd.toUTCString();
                        break;
                }
            }

            document.cookie = encodeURIComponent(sKey) + "=" + encodeURIComponent(sValue) + sExpires + (sDomain ? "; domain=" + sDomain : "") + (sPath ? "; path=" + sPath : "") + (bSecure ? "; secure" : "");

            return true;
        },

        /**
         * 删除一个cookie
         * @param {String} sKey - cookie名
         * @param {String} [sPath] - cookie路径。默认为当前文档位置的路径
         * @param {String} [sDomain] - cookie域名。默认为当前文档位置的路径的域名部分
         * @returns {Boolean} - 操作成功或失败
         */
        removeItem: function (sKey, sPath, sDomain) {
            if (!sKey || !this.hasItem(sKey)) {

                return false;
            }

            document.cookie = encodeURIComponent(sKey) + "=; expires=Thu, 01 Jan 1970 00:00:00 GMT" + ( sDomain ? "; domain=" + sDomain : "") + ( sPath ? "; path=" + sPath : "");

            return true;
        },

        /**
         * 检查一个cookie是否存在
         * @param {String} sKey - cookie名
         * @returns {Boolean} - 存在与否
         */
        hasItem: function (sKey) {

            return (new RegExp("(?:^|;\\s*)" + encodeURIComponent(sKey).replace(/[\-\.\+\*]/g, "\\$&") + "\\s*\\=")).test(document.cookie);
        },

        /**
         * 返回cookie名字的数组
         * @returns {Array} - cookie名字的数组 或 []
         */
        listItems: function () {
            if (document.cookie === '') {

                return [];
            }

            var aKeys = document.cookie.replace(/((?:^|\s*;)[^\=]+)(?=;|$)|^\s*|\s*(?:\=[^;]*)?(?:\1|$)/g, "").split(/\s*(?:\=[^;]*)?;\s*/);

            for (var nIdx = 0; nIdx < aKeys.length; nIdx++) {
                aKeys[nIdx] = decodeURIComponent(aKeys[nIdx]);
            }

            return aKeys;
        },

        /**
         * 清空所有cookie
         * @returns {Boolean} - 操作成功或失败
         */
        clear: function () {
            if (document.cookie === '') {

                return false;
            }

            var aKeys = document.cookie.replace(/((?:^|\s*;)[^\=]+)(?=;|$)|^\s*|\s*(?:\=[^;]*)?(?:\1|$)/g, "").split(/\s*(?:\=[^;]*)?;\s*/);

            for (var nIdx = 0; nIdx < aKeys.length; nIdx++) {
                this.removeItem(decodeURIComponent(aKeys[nIdx]));
            }

            return true;
        }
    };
```
>参考[MDN:cookie](https://developer.mozilla.org/zh-CN/docs/Web/API/Document/cookie#一个小框架：一个完整支持unicode的cookie读取写入器)。

### *原生JS*加入收藏夹
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
        alert('加入收藏失败，请使用 ' + (navigator.userAgent.toLowerCase().indexOf('mac') !== -1 ? 'Command/Cmd' : 'Ctrl') + ' + D 进行添加。');
    }
}


/* 使用测试*/
addFavorite(window.location.href, '收藏名字');
```

### *原生JS*比较版本号大小（纯数字）
```javascript
    /**
     * 比较版本号大小（纯数字）
     * @param {Number|String} version - 比较数1
     * @param {Number|String} base - 比较数2
     * @param {String} [separator = '.'] - 版本分隔符
     * @returns {String} flag - '=' 或 '>' 或 '<'
     */
    function versionCompare(version, base, separator) {
        separator = separator || '.';

        var arr1 = version.toString().split(separator),
            arr2 = base.toString().split(separator),
            length = arr1.length > arr2.length ? arr1.length : arr2.length,
            flag = '=',
            i;

        for (i = 0; i < length; i++) {
            arr1[i] = arr1[i] || '0';
            arr2[i] = arr2[i] || '0';

            if (arr1[i] !== arr2[i]) {  /* 两值不同*/
                flag = parseInt(arr1[i]) < parseInt(arr2[i]) ? '<' : '>';

                break;
            }
        }

        return flag;
    }


    /* 使用测试*/
    console.log(versionCompare('1.1.10', '1.2'));
```

### *原生JS*判断检索内容是否在被检索内容的分隔符间
```javascript
/**
 * 判断key是否存在以separator分割的str当中
 * @param {Number|String} key - 检索内容
 * @param {Number|String} str - 被检索内容
 * @param {String} [separator = '|'] - str的分隔符
 * @returns {Boolean} flag
 */
function isKeyInStr(key, str, separator) {
    separator = separator || '|';

    var flag = false,
        strArr, i;

    key = key.toString();
    str = str.toString();

    strArr = str.split(separator);

    for (i = 0; i < strArr.length; i++) {
        if (key === strArr[i]) {
            flag = true;
            
            break;
        }
    }

    return flag;
}
```

### *原生JS*选取范围内随机值
```javascript
/**
 * 选取范围内随机值
 * @param {Number} minimum - 下限（或上限）
 * @param {Number} maximum - 上限（或下限）
 * @returns {Number} - 上下限区间内的随机值
 */
function randomFrom(minimum, maximum) {
    var medium;

    if (minimum > maximum) {
        medium = minimum;
        minimum = maximum;
        maximum = medium;
    }

    return Math.floor(Math.random() * (maximum - minimum + 1) + minimum);
}
```

### *原生JS*格式化文件属性（大小、日期）
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
                'M+': date.getMonth() + 1, /* 月*/
                'd+': date.getDate(), /* 日*/
                'h+': date.getHours() % 12 === 0 ? 12 : date.getHours() % 12, /* 12小时制*/
                'H+': date.getHours(), /* 24小时制*/
                'm+': date.getMinutes(), /* 分*/
                's+': date.getSeconds(), /* 秒*/
                'q+': Math.floor((date.getMonth() + 3) / 3), /* 季度*/
                'S': date.getMilliseconds() /* 毫秒*/
            },
            week = {
                /* [{E:'一'},{EE:'周一'},{EEE+:'星期一'}]*/
                '0': '一',
                '1': '二',
                '2': '三',
                '3': '四',
                '4': '五',
                '5': '六',
                '6': '日'
            },
            i;

        if (/(y+)/.test(fmt)) {
            fmt = fmt.replace(RegExp.$1, (date.getFullYear() + "").substr(4 - RegExp.$1.length));
        }
        if (/(E+)/.test(fmt)) {
            fmt = fmt.replace(RegExp.$1, ((RegExp.$1.length > 1) ? (RegExp.$1.length > 2 ? '星期' : '周') : "") + week[date.getDay() + ""]);
        }
        for (i in o) {
            if (new RegExp('(' + i + ')').test(fmt)) {
                fmt = fmt.replace(RegExp.$1, (RegExp.$1.length === 1) ? (o[i]) : (('00' + o[i]).substr(("" + o[i]).length)));
            }
        }

        return fmt;
    }
};


/* 使用测试*/
var a = format.date(new Date(Date.parse('Wed, 09 Aug 1995 00:00:00 GMT')),'yyyy-MM-dd HH:mm:ss');
```

### *原生JS*倒计时显示
```javascript
/**
 * 显示倒计时
 * @constructor
 * @param {Number} deadline - 到期的时间戳
 * @param {String} [id] - 输出节点id
 * @param {Function} [func] - 到点后的回调函数
 * @param {String} [dType = ' '] - “天”后面的文字
 * @param {String} [hType = ' '] - “时”后面的文字
 * @param {String} [mType = ' '] - “分”后面的文字
 * @param {String} [sType = ' '] - “秒”后面的文字
 */
function CountDown(deadline, id, func, dType, hType, mType, sType) {
    if (typeof Date.now !== 'function') {
        Date.now = function () {
            return new Date().getTime();
        };
    }

    var _dTypeSend = (typeof dType !== 'undefined') && dType !== '',
        _hTypeSend = (typeof hType !== 'undefined') && hType !== '',
        _mTypeSend = (typeof mType !== 'undefined') && mType !== '',
        _sTypeSend = (typeof sType !== 'undefined') && sType !== '',
        _hasDom = !!document.getElementById(id),
        _formatNum = function (number) {    /* 格式化数字格式*/
            if (number < 10) {
                return '0' + number;
            } else {
                return number.toString();
            }
        },
        _SetInterval = function (func, millisecond) {  /* 周期执行*/
            var _setIntervalId;

            if (typeof func === 'function') {
                _setIntervalId = setTimeout(function () {
                    _setIntervalId = setTimeout(arguments.callee, millisecond);

                    func();
                }, millisecond);
            }

            this.stop = function () {
                clearTimeout(_setIntervalId);
            };
        },
        _print = function (time) {  /* 输出*/
            var day = _formatNum(Math.floor((time / (24 * 60 * 60)))),
                hour = _formatNum(Math.floor((time / (60 * 60)) % 24)),
                minute = _formatNum(Math.floor((time / 60) % 60)),
                second = _formatNum(time % 60),
                text;

            if (day !== '00' || _dTypeSend) {
                text = day + dType + hour + hType + minute + mType + second + sType;
            } else if (hour !== '00' || _hTypeSend) {
                text = hour + hType + minute + mType + second + sType;
            } else if (minute !== '00' || _mTypeSend) {
                text = minute + mType + second + sType;
            } else {
                text = second + sType;
            }

            if (_hasDom) {
                document.getElementById(id).innerHTML = text;
            } else {
                console.log(text);
            }
        };

    if (!_dTypeSend) {
        dType = ' ';
    }
    if (!_hTypeSend) {
        hType = ' ';
    }
    if (!_mTypeSend) {
        mType = ' ';
    }
    if (!_sTypeSend) {
        sType = '';
    }

    /* 初始化时就输出一遍*/
    _print(Math.round((deadline - Date.now()) / 1000));

    var obj = new _SetInterval(function () {
        var time = Math.round((deadline - Date.now()) / 1000);

        if (time < 0) {
            obj.stop();
            if (typeof func === 'function') {
                func();
            }
            return;
        }

        _print(time);
    }, 1000);

    this.stop = obj.stop;
}


/* 使用测试*/
var a = new CountDown(Date.now() + 500000, 'test1', function () {
    console.log('完成');
}, '', '时', '分', '秒');

//a.stop();
```

### *原生JS*判断对象是否为空
```javascript
function isObjEmpty(obj) {
    var i;

    if (obj !== Object(obj)) {  /* 参数不是对象*/
        throw new TypeError('参数不是对象');
    } else if (typeof Object.keys === 'function') { /* ie9+及高级浏览器支持*/

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

### *原生JS*移动端模拟点击事件（消除“延时300毫秒后才触发click事件”，使点击事件提前触发）
```javascript
/* 不要绑定click事件，用touchstart和touchend模拟，以消除“延时300毫秒后才触发”的问题*/

var start_x, start_y;

document.getElementById('...').addEventListener('touchstart', function (e) {
    start_x = e.changedTouches[0].clientX;
    start_y = e.changedTouches[0].clientY;
}, false);

document.getElementById('...').addEventListener('touchend', function (e) {
    var end_x = e.changedTouches[0].clientX,
        end_y = e.changedTouches[0].clientY;

    if (Math.abs(end_x - start_x) > 5 || Math.abs(end_y - start_y) > 5) {
        /* 触发滑动事件要做的事情（比如什么都不做）*/
    } else {
        /* 触发点击事件要做的事情*/
    }
}, false);

/* 还要处理浏览器默认点击事件（如a标签）*/
```

### *原生JS*判断是否是数组
```javascript
function isArray(value) {
    if (typeof Array.isArray === 'function') {    /* ie8及以下不支持*/

        return Array.isArray(value);
    } else {

        return Object.prototype.toString.call(value) === '[Object Array]';
    }
}
```

### *原生JS*从字符串中获取绝对路径
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

### *原生JS*判断事件在浏览器是否存在
```javascript
/**
 * 判断DOM节点是否支持某事件
 * @param {String} eventName - 事件名
 * @param {Object} [element] - DOM的Document对象
 * @returns {Boolean} isSupported
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

### *原生JS*用整数进行小数的四则运算（避免浮点数运算误差）
```javascript
var fourOperations = {
    add: function (arg1, arg2) {    /* 加*/
        var int1 = Number(arg1.toString().replace('.', '')),
            int2 = Number(arg2.toString().replace('.', '')),
            r1, r2, m, c, cm;

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

### *原生JS*用请求图片作log统计
```javascript
var sendLog = (function () {
    if (typeof Date.now !== 'function') {
        Date.now = function () {
            return new Date().getTime();
        };
    }

    var _unique = (function () {    /* 产生唯一标识*/
        var time = Date.now() + '_',
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


/* 使用测试*/
sendLog('统计url');
```

### *原生JS*绑定、解绑事件
```javascript
var eventUtil = {
    /**
     * 绑定事件
     * @param {Object} dom - DOM对象
     * @param {String} type - 事件名
     * @param {Function} handle - 处理函数
     */
    addHandler: function (dom, type, handle) {
        if (typeof dom.addEventListener === 'function') {   /* DOM2级，除ie6~8外的高级浏览器*/
            dom.addEventListener(type, handle, false);
        } else if (typeof dom.attachEvent === 'function') { /* 所有ie浏览器*/
            dom.attachEvent('on' + type, handle);
        } else {    /* DOM0级，最早期的浏览器都支持*/
            dom['on' + type] = handle;
        }
    },

    /**
     * 解绑事件
     * @param {Object} dom - DOM对象
     * @param {String} type - 事件名
     * @param {Function} handle - 处理函数
     */
    removeHandler: function (dom, type, handle) {
        if (typeof dom.removeEventListener === 'function') {
            dom.removeEventListener(type, handle, false);
        } else if (typeof dom.detachEvent === 'function') {
            dom.detachEvent('on' + type, handle);
        } else {
            dom['on' + type] = null;
        }
    }
};
```

>1. `addEventListener`与`removeEventListener`是高级浏览器都有的方法（ie8-不支持），必须一一对应具体的**handle**和**布尔值**进行解绑。
>2. `attachEvent`与`detachEvent`是ie特有方法，必须一一对应具体的**handle**进行解绑。
>3. `on+type`是所有浏览器都支持，用赋值覆盖解绑。
>4. jQuery的`on`（或`one`）与`off`：当写具体handle时解绑具体handle；不写handle时默认解绑对象下某事件的所有方法；还可以对事件添加namespace。

### *原生JS*、jQuery或Zepto获取事件对象引用、目标元素引用
>ie8-的DOM0事件（直接on+type）没有传递**事件对象**到**事件处理函数**中，要额外的`window.event`对象进行相关操作。

1. *原生JS*

    ```javascript
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
    ```
2. jQuery或Zepto

    ```javascript
    $('...').on('...', function (e) {
        /* 可以直接使用事件对象引用e和目标引用e.target*/
    });
    ```

### *原生JS*、jQuery或Zepto阻止冒泡和阻止浏览器默认行为
1. 阻止冒泡

    1. *原生JS*
    
        ```javascript
        function stopBubble(e) {
            if (e && e.stopPropagation) {
                e.stopPropagation();
            } else {
                window.event.cancelBubble = true;
            }
        }
        ```
    2. jQuery或Zepto
    
        ```javascript
        $('...').on('...', function (e) {
            e.stopPropagation();
        });
        ```
2. 阻止默认行为

    1. *原生JS*
    
        ```javascript
        function stopDefault(e) {
            if (e && e.preventDefault) {
                e.preventDefault();
            } else {
                window.event.returnValue = false;
            }
     
            return false;
        }
        ```
    2. jQuery或Zepto
    
        ```javascript
        $('...').on('...', function (e) {
            e.preventDefault();
        });
        ```
3. 阻止冒泡&阻止默认行为

    1. *原生JS*

        ```javascript
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
        ```
    2. jQuery或Zepto

        ```javascript
        $('...').on('...', function () {
     
            return false;
        });
        ```

### *原生JS*、jQuery或Zepto实现判断按下具体某键值
1. *原生JS*

    ```javascript
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
    

    /* 使用测试*/
    addEvent(document.getElementById('test'), 'keydown', checkKeyCode);  /* 上面绑定事件*/
    ```
2. jQuery或Zepto

    ```javascript
    $(输入框选择器).on('keydown', function (e) {
        if (e.which === 13) {   /* 查询键值表 例:13->换行*/
            /* 具体操作...*/
    
            return false;   /* 取消默认行为*/
        }
    });
    ```

### *原生JS*输入框光标位置的获取和设置
```javascript
var cursorPosition = {
    /**
     * 获取光标位置和选中长度
     * @param {Object} dom - 标签input或textarea的DOM对象
     * @returns {Object} - {光标起始位置,选中长度}
     */
    get: function (dom) {
        var start = 0, /* 光标起始位置*/
            selLen = 0, /* 光标选中长度*/
            sel, ieSel;

        if ('selectionStart' in dom) {
            start = dom.selectionStart;
            selLen = dom.selectionEnd - start;
        } else if (document.selection) {    /* ie*/
            sel = document.selection.createRange();
            selLen = sel.text.length;

            if (dom.nodeName.toLowerCase() === 'textarea') {
                ieSel = document.body.createTextRange();
                ieSel.moveToElementText(dom);
            } else {
                ieSel = dom.createTextRange();
            }

            ieSel.setEndPoint('EndToEnd', sel);
            start = ieSel.text.length - selLen;
        }

        return {start: start, select: selLen};
    },

    /**
     * 设置光标起始位置和选中长度
     * @param {Object} dom - 标签input或textarea的DOM对象
     * @param {Number} start - 光标起始位置
     * @param {Number} len - 选中长度
     * @returns {Number} end - 结束位置（start+len）
     */
    set: function (dom, start, len) {
        var valueLen = dom.value.length,
            end, ieSel;

        /* 初始化start*/
        start = parseInt(start);
        if (!start) {
            start = 0;
        } else if (start > valueLen) {
            start = valueLen;
        }

        /* 初始化len*/
        len = parseInt(len);
        if (!len) {
            len = 0;
        }

        /* 初始化end*/
        end = start + len;
        if (end > valueLen) {
            end = valueLen;
        }

        if (valueLen !== 0) {
            if (dom.setSelectionRange) {
                dom.setSelectionRange(start, end);
                dom.focus();
            } else {    /* ie*/
                ieSel = dom.createTextRange();
                ieSel.moveStart('character', -valueLen);
                ieSel.moveEnd('character', -valueLen);
                ieSel.moveStart('character', start);
                ieSel.moveEnd('character', len);
                ieSel.select();
            }
        } else {
            if (dom.setSelectionRange) {
                dom.focus();
            } else {    /* ie*/
                ieSel = dom.createTextRange();
                ieSel.select();
            }
        }

        return end;
    }
};


/* 使用测试*/
$(输入框选择器).on('mouseup keyup', function () {
    console.log(cursorPosition.get(this));
});

console.log(cursorPosition.set(输入框dom, 起始位置, 选中长度));
```
[JSFiddle Demo](https://jsfiddle.net/realgeoffrey/L3k46dy3/)

### *原生JS*阻止嵌入滚动条冒泡“橡皮筋效果”（iOS）
```html
<style>
    .bounce {
        overflow-y: scroll;
        -webkit-overflow-scrolling: touch;

        height: 固定高度;
    }
</style>

<div class="bounce" id="j-bounce">
    a<br>
    b<br>
    c<br>
    d<br>
    e<br>
    f<br>
    g<br>
</div>

<script>
    var ScrollBounce = function (dom) {
        var _bounce = function () {
            var startTopScroll = dom.scrollTop, /* 滚动高度*/
                domHeight = dom.offsetHeight, /* 占据高度*/
                contentHeight = dom.scrollHeight; /* 内容高度（占据高度+可滚动最大高度）*/

            /*
             * 在触摸开始时，如果发现滚动区域已经处于极限状态时，就手工设置 scrollTop 的值，
             * 将滚动内容向边缘方向偏移 1px（这实际上改变了滚动区域的极限状态），
             * 从而诱使浏览器对滚动区块使用橡皮筋效果，而不会把触摸事件向上传播到 DOM 树（引起整页滚动）。
             */
            if (startTopScroll <= 0) {
                dom.scrollTop = 1;
            } else if (startTopScroll + domHeight >= contentHeight) {
                dom.scrollTop = contentHeight - domHeight - 1;
            }
        };

        this.stop = function () {};

        if ((/iphone|ipad|ipod/i).test(navigator.userAgent)) {  /* 仅iOS设备支持“橡皮筋效果”*/
            dom.addEventListener('touchstart', _bounce, false);

            this.stop = function () {
                dom.removeEventListener('touchstart', _bounce, false);
            };
        }
    };


    /* 使用测试*/
    var a = new ScrollBounce(document.getElementById('j-bounce'));

    //a.stop();
</script>
```
[JSFiddle Demo](https://jsfiddle.net/realgeoffrey/hbadqyew/)
>参考[ScrollFix](https://github.com/joelambert/ScrollFix)。

### *原生JS*获取滚动轴宽度（或高度）
```javascript
function getScrollBarWidth() {
    if (typeof arguments.callee.barWidth !== 'undefined') {

        return arguments.callee.barWidth;
    }

    var dom = document.createElement('div');

    dom.style.cssText = 'overflow:scroll;width:100px;height:100px;';

    document.body.appendChild(dom);

    arguments.callee.barWidth = dom.offsetWidth - dom.clientWidth;

    document.body.removeChild(dom);

    return arguments.callee.barWidth;
}
```

### *原生JS*防抖函数
```javascript
/**
 * 函数连续调用时，间隔时间必须大于或等于wait，func才会执行
 * @param {Function} func - 传入函数
 * @param {Number} wait - 函数触发的最小间隔
 * @param {Boolean} immediate - 设置为ture时，调用触发于开始边界而不是结束边界
 * @returns {Function} - 返回客户调用函数
 */
function debounce(func, wait, immediate) {
    if (typeof Date.now !== 'function') {
        Date.now = function () {
            return new Date().getTime();
        };
    }

    var timeout, args, context, timestamp, result;

    var later = function () {
        //据上一次触发时间间隔
        var last = Date.now() - timestamp;

        //上次被包装函数被调用时间间隔last小于设定时间间隔wait
        if (last < wait && last >= 0) {
            timeout = setTimeout(later, wait - last);
        } else {
            timeout = null;

            //如果设定为immediate===true，因为开始边界已经调用过了此处无需调用
            if (!immediate) {
                result = func.apply(context, args);

                if (!timeout) {
                    context = args = null;
                }
            }
        }
    };

    return function () {
        context = this;
        args = arguments;
        timestamp = Date.now();

        var callNow = immediate && !timeout;

        if (!timeout) {
            timeout = setTimeout(later, wait);
        }
        if (callNow) {
            result = func.apply(context, args);
            context = args = null;
        }

        return result;
    };
}


/* 使用测试*/
var a = debounce(function () {
    console.log(1);
}, 1000);

$(window).on('scroll', a);
```
>来自[underscore](https://github.com/jashkenas/underscore)。

### *原生JS*节流函数
```javascript
/**
 * 函数连续调用时，func在wait时间内，执行次数不得高于1次
 * @param {Function} func - 传入函数
 * @param {Number} wait - 函数触发的最小间隔
 * @param {Object} options - 如果想忽略开始边界上的调用，传入{leading: false}；如果想忽略结尾边界上的调用，传入{trailing: false}
 * @returns {Function} - 返回客户调用函数
 */
function throttle(func, wait, options) {
    if (typeof Date.now !== 'function') {
        Date.now = function () {
            return new Date().getTime();
        };
    }

    var context, args, result;
    var timeout = null;
    var previous = 0;   //上次执行时间点

    if (!options) {
        options = {};
    }

    //延迟执行函数
    var later = function () {
        //若设定了开始边界不执行选项，上次执行时间始终为0
        previous = options.leading === false ? 0 : Date.now();
        timeout = null;
        result = func.apply(context, args);
        if (!timeout) {
            context = args = null;
        }
    };

    return function () {
        var now = Date.now();

        //首次执行时，如果设定了开始边界不执行选项，将上次执行时间设定为当前时间。
        if (!previous && options.leading === false) {
            previous = now;
        }

        //延迟执行时间间隔
        var remaining = wait - (now - previous);

        context = this;

        args = arguments;

        //延迟时间间隔remaining小于等于0，表示上次执行至此所间隔时间已经超过一个时间窗口 || remaining大于时间窗口wait，表示客户端系统时间被调整过
        if (remaining <= 0 || remaining > wait) {
            if (timeout) {
                clearTimeout(timeout);
                timeout = null;
            }
            previous = now;
            result = func.apply(context, args);
            if (!timeout) {
                context = args = null;
            }
        } else if (!timeout && options.trailing !== false) { //如果延迟执行不存在，且没有设定结尾边界不执行选项
            timeout = setTimeout(later, remaining);
        }
        return result;
    };
}


/* 使用测试*/
var a = throttle(function () {
    console.log(1);
}, 300);

$(window).on('scroll', a);
```
>来自[underscore](https://github.com/jashkenas/underscore)。

### *原生JS*不同进制数转换
```javascript
/**
 * 不同进制（2至36进制）换算
 * @param {String} operand - 转换数（二进制仅使用0~1、八进制仅使用0~7、十进制仅使用0~9、十六进制仅使用0~9和a~f，等）
 * @param {Number} fromRadix - 转换数的进制数（2~36）
 * @param {Number} toRadix - 结果的进制数
 * @returns {String|Boolean|Number} - 转换后的数值；进制数不在2~36：false；操作数与进制数不匹配：NaN
 */
function numConvert(operand, fromRadix, toRadix) {
    var myself = arguments.callee;

    if (typeof myself.toDecimal !== 'function' || typeof myself.fromDecimal !== 'function') {
        myself.toDecimal = function (str, radix) {  /* 其他进制转化为十进制*/

            return parseInt(str, radix);
        };

        myself.fromDecimal = function (num, radix) {    /* 十进制转化为其他进制*/

            return num.toString(radix);
        };
    }

    if (fromRadix > 36 || fromRadix < 2 || toRadix > 36 || toRadix < 2) {    /* 仅支持2至36进制*/

        console.log('进制数只能在2至36之间');

        return false;
    } else {

        if (fromRadix === 10) {
            operand = parseInt(operand, 10);
        } else {
            operand = myself.toDecimal(operand, fromRadix);
        }

        return myself.fromDecimal(operand, toRadix);
    }
}
```

### *原生JS*`验证邮箱有效性
```javascript
function validateEmail(email) {

    return /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(email);
}
```
>来自[stackoverflow:Validate email address in JavaScript?](http://stackoverflow.com/questions/46155/validate-email-address-in-javascript#answer-46181)。

## Polyfill

### *原生JS*`Date.now`的**Polyfill**
```javascript
if (typeof Date.now !== 'function') {
    Date.now = function () {
        return new Date().getTime();
    };
}
```
>`Date.now()`相对于`new Date().getTime()`及其他方式，可以避免生成不必要的`Date`对象，更高效。

### *原生JS*`requestAnimationFrame`和`cancelAnimationFrame`的**Polyfill**
```javascript
(function () {
    var lastTime = 0,
        vendors = ['ms', 'moz', 'webkit', 'o'],
        x;

    for (x = 0; x < vendors.length && !window.requestAnimationFrame; ++x) {
        window.requestAnimationFrame = window[vendors[x] + 'RequestAnimationFrame'];
        window.cancelAnimationFrame = window[vendors[x] + 'CancelAnimationFrame'] || window[vendors[x] + 'CancelRequestAnimationFrame'];
    }

    if (!window.requestAnimationFrame) {
        window.requestAnimationFrame = function (callback, element) {
            var currTime = new Date().getTime(),
                timeToCall = Math.max(0, 16 - (currTime - lastTime)),
                id = window.setTimeout(function () {
                    callback(currTime + timeToCall);
                }, timeToCall);

            lastTime = currTime + timeToCall;

            return id;
        };
    }

    if (!window.cancelAnimationFrame) {
        window.cancelAnimationFrame = function (id) {
            clearTimeout(id);
        };
    }
}());
```
>来自[rAF.js](https://gist.github.com/paulirish/1579671)。

### *原生JS*`Array.prototype.map`的**Polyfill**
```javascript
if (!Array.prototype.map) {
    Array.prototype.map = function (callback, thisArg) {
        var T, A, k;

        if (this == null) {
            throw new TypeError(' this is null or not defined');
        }

        // 1. 将O赋值为调用map方法的数组.
        var O = Object(this);

        // 2.将len赋值为数组O的长度.
        var len = O.length >>> 0;

        // 3.如果callback不是函数,则抛出TypeError异常.
        if (Object.prototype.toString.call(callback) != '[object Function]') {
            throw new TypeError(callback + ' is not a function');
        }

        // 4. 如果参数thisArg有值,则将T赋值为thisArg;否则T为undefined.
        if (thisArg) {
            T = thisArg;
        }

        // 5. 创建新数组A,长度为原数组O长度len
        A = new Array(len);

        // 6. 将k赋值为0
        k = 0;

        // 7. 当 k < len 时,执行循环.
        while (k < len) {
            var kValue, mappedValue;

            //遍历O,k为原数组索引
            if (k in O) {

                //kValue为索引k对应的值.
                kValue = O[k];

                // 执行callback,this指向T,参数有三个.分别是kValue:值,k:索引,O:原数组.
                mappedValue = callback.call(T, kValue, k, O);

                // 返回值添加到新数组A中.
                A[k] = mappedValue;
            }
            // k自增1
            k++;
        }

        // 8. 返回新数组A
        return A;
    };
}
```
>来自[MDN:Array.prototype.map](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/map#Compatibility)。

### *原生JS*`Object.create`的**Polyfill**
```javascript
if (typeof Object.create !== 'function') {
    // Production steps of ECMA-262, Edition 5, 15.2.3.5
    // Reference: http://es5.github.io/#x15.2.3.5
    Object.create = (function () {
        //为了节省内存，使用一个共享的构造器
        function Temp() {}

        // 使用 Object.prototype.hasOwnProperty 更安全的引用
        var hasOwn = Object.prototype.hasOwnProperty;

        return function (O) {
            // 1. 如果 O 不是 Object 或 null，抛出一个 TypeError 异常。
            if (typeof O != 'object') {
                throw TypeError('Object prototype may only be an Object or null');
            }

            // 2. 使创建的一个新的对象为 obj ，就和通过
            //    new Object() 表达式创建一个新对象一样，
            //    Object是标准内置的构造器名
            // 3. 设置 obj 的内部属性 [[Prototype]] 为 O。
            Temp.prototype = O;
            var obj = new Temp();
            Temp.prototype = null; // 不要保持一个 O 的杂散引用（a stray reference）...

            // 4. 如果存在参数 Properties ，而不是 undefined ，
            //    那么就把参数的自身属性添加到 obj 上，就像调用
            //    携带obj ，Properties两个参数的标准内置函数
            //    Object.defineProperties() 一样。
            if (arguments.length > 1) {
                // Object.defineProperties does ToObject on its first argument.
                var Properties = Object(arguments[1]);

                for (var prop in Properties) {
                    if (hasOwn.call(Properties, prop)) {
                        obj[prop] = Properties[prop];
                    }
                }
            }

            // 5. 返回 obj
            return obj;
        };
    })();
}
```
>来自[MDN:Object.create](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Object/create#Polyfill)。

----
## jQuery（或Zepto）方法

### jQuery或Zepto滚动加载
1. 以**放置在底部的节点与屏幕的相对距离**作为是否滚动到底部的判断：

    ```html
    <!--
    data-next：加载内容标识（-1：去除滚动加载功能；0：单次不加载）
    data-status：是否正在加载（'ready'：不在加载中、可以进行加载；'busy'：加载中、不允许加载）
    -->
    <div class="j-load" data-next="1" data-status="ready">放置在底部的标记节点，内容添加在此节点前面</div>

    <script>
        var scrollLoadObj = {
            namespace: '', /*事件命名空间*/
            loadMore: function (next) { /*加载逻辑*/
                var $load = $('.j-load'),
                    newNext = 0;

                next = parseInt(next);

                if (next !== -1 && $load.length >= 1) {
                    if ($load.attr('data-status') === 'ready' && next !== 0) {
                        $load.attr('data-status', 'busy');

                        $.ajax({
                            url: '',
                            dataType: 'json',
                            data: {
                                id: next
                            }
                        }).done(function (data) {
                            /* 删除重复内容*/
                            /* 其他具体操作*/

                            newNext = data.next;

                            $load.attr('data-next', newNext);
                        }).fail(function () {
                            console.log('网络错误');
                        }).always(function () {
                            $load.attr('data-status', 'ready');

                            if (/* 某条件*/) {   /* 不再加载*/
                                $(window).off('scroll' + '.' + scrollLoadObj.namespace);
                                /*$load.hide();*/
                            } else {
                                scrollLoadObj.autoLoadMore(newNext);
                            }
                        });
                    }
                } else {
                    $(window).off('scroll' + '.' + scrollLoadObj.namespace);
                    /*$load.hide();*/
                }
            },
            autoLoadMore: function (next) { /* 若html小于视窗则触发加载*/
                if ($('html').outerHeight(true) <= $(window).height()) {
                    scrollLoadObj.loadMore(next);
                }
            },
            init: function () {
                if (typeof Date.now !== 'function') {
                    Date.now = function () {
                        return new Date().getTime();
                    };
                }

                scrollLoadObj.namespace = Date.now();

                $(function () {
                    var $load = $('.j-load'),
                        scrollSetTimeoutId;

                    scrollLoadObj.autoLoadMore($load.attr('data-next'));

                    $(window).on('scroll' + '.' + scrollLoadObj.namespace, function () {
                        clearTimeout(scrollSetTimeoutId);

                        scrollSetTimeoutId = setTimeout(function () {
                            if ($load.offset().top <= $(window).scrollTop() + $(window).height()) {  /* 节点顶部在屏幕底部以上*/
                                scrollLoadObj.loadMore($load.attr('data-next'));
                            }
                        }, 200);
                    });
                });
            }
        };


        /* 使用测试*/
        scrollLoadObj.init();
    </script>
    ```
2. 以**文档是否滚动到底部**作为是否滚动到底部的判断：

    ```html
    <!--
    data-next：加载内容标识（-1：去除滚动加载功能；0：单次不加载）
    data-status：是否正在加载（'ready'：不在加载中、可以进行加载；'busy'：加载中、不允许加载）
    -->
    <div class="j-load" data-next="1" data-status="ready">不作为标记节点，仅作为内容添加容器</div>

    <script type="text/javascript">
        var scrollLoadObj = {
            namespace: '', /*事件命名空间*/
            loadMore: function (next) { /*加载逻辑*/
                var $load = $('.j-load'),
                    newNext = 0;

                next = parseInt(next);

                if (next !== -1 && $load.length >= 1) {
                    if ($load.attr('data-status') === 'ready' && next !== 0) {
                        $load.attr('data-status', 'busy');

                        $.ajax({
                            url: '',
                            dataType: 'json',
                            data: {
                                id: next
                            }
                        }).done(function (data) {
                            /* 删除重复内容*/
                            /* 其他具体操作*/

                            newNext = data.next;

                            $load.attr('data-next', newNext);
                        }).fail(function () {
                            console.log('网络错误');
                        }).always(function () {
                            $load.attr('data-status', 'ready');

                            if (/* 某条件*/) {   /* 不再加载*/
                                $(window).off('scroll' + '.' + scrollLoadObj.namespace);
                            } else {
                                scrollLoadObj.autoLoadMore(newNext);
                            }
                        });
                    }
                } else {
                    $(window).off('scroll' + '.' + scrollLoadObj.namespace);
                }
            },
            autoLoadMore: function (next) { /* 若html小于视窗则触发加载*/
                if ($('html').outerHeight(true) <= $(window).height()) {
                    scrollLoadObj.loadMore(next);
                }
            },
            init: function () {
                if (typeof Date.now !== 'function') {
                    Date.now = function () {
                        return new Date().getTime();
                    };
                }

                scrollLoadObj.namespace = Date.now();

                $(function () {
                    var $load = $('.j-load'),
                        scrollSetTimeoutId;

                    scrollLoadObj.autoLoadMore($load.attr('data-next'));

                    $(window).on('scroll' + '.' + scrollLoadObj.namespace, function () {
                        clearTimeout(scrollSetTimeoutId);

                        scrollSetTimeoutId = setTimeout(function () {
                            if ($(window).height() + $(window).scrollTop() >= $(document).height()) {  /* 文档滚动到底部*/
                                scrollLoadObj.loadMore($load.attr('data-next'));
                            }
                        }, 200);
                    });
                });
            }
        };


        /* 使用测试*/
        scrollLoadObj.init();
    </script>
    ```

> Zepto默认没有`deferred`的对象、没有`outerHeight`方法。

### jQuery或Zepto图片延时加载
```html
<img src="默认图地址" data-src="真实图地址" data-error="真实图错误后的默认图地址" class="j-img-1">
<img src="默认图地址" data-src-user="真实图地址" data-error-user="真实图错误后的默认图地址" class="j-img-2">

<script>
    /**
     * 图片延时加载
     * @constructor
     * @param {String} className - 触发的类名
     * @param {String} [dataSrc = 'data-src'] - img标签上存放“真实地址”的属性
     * @param {Function} func - 图片加载成功后回调函数，this和形参为图片DOM
     * @param {String} [dataError = 'data-error'] - img标签上存放“真实地址加载失败后显示的地址”的属性
     * @param {Function} errorFunc - 图片加载失败后回调函数，this和形参为图片DOM
     */
    function ImgLazyLoad(className, dataSrc, func, dataError, errorFunc) {
        if (typeof Date.now !== 'function') {
            Date.now = function () {
                return new Date().getTime();
            };
        }

        var _timeoutId,
            _namespace = Date.now(), /* 事件命名空间*/
            _lazyLoad = function (domArr, className, dataSrc, func, dataError, errorFunc) { /* 图片延时加载*/
                dataSrc = dataSrc || 'data-src';
                dataError = dataError || 'data-error';

                $.each(domArr, function (index, value) {
                    var $this = $(value);

                    var srcReal = $this.attr(dataSrc),
                        srcError = $this.attr(dataError),
                        newImg = new Image();

                    if (srcReal) {
                        newImg.src = srcReal;

                        newImg.onerror = function () {
                            if (srcError) {
                                $this.attr('src', srcError)
                                    .removeAttr(dataError);
                            }

                            $this.removeClass(className);

                            if (typeof errorFunc === 'function') {
                                errorFunc.call(value, value);
                            }

                            /* 防止内存泄露*/
                            newImg.onload = null;
                            newImg.onerror = null;
                            newImg = null;
                        };

                        if (newImg.complete) {    /* 缓存加载*/
                            $this.attr('src', srcReal)
                                .removeAttr(dataSrc)
                                .removeClass(className);

                            if (typeof func === 'function') {
                                func.call(value, value);
                            }

                            /* 防止内存泄露*/
                            newImg.onerror = null;
                            newImg = null;
                        } else {
                            newImg.onload = function () {   /* 新加载*/
                                $this.attr('src', srcReal)
                                    .removeAttr(dataSrc)
                                    .removeClass(className);

                                if (typeof func === 'function') {
                                    func.call(value, value);
                                }

                                /* 防止内存泄露*/
                                newImg.onload = null;
                                newImg.onerror = null;
                                newImg = null;
                            };
                        }
                    } else {
                        if (srcError) {
                            $this.attr('src', srcError)
                                .removeAttr(dataError);
                        }

                        $this.removeClass(className);

                        if (typeof errorFunc === 'function') {
                            errorFunc.call(value, value);
                        }

                        /* 防止内存泄露*/
                        newImg = null;
                    }
                });
            },
            _getImgArr = function (className, offset) { /* 获取屏幕内dom数组*/
                var $all = $('.' + className),
                    screenTop = $(window).scrollTop(),
                    screenBottom = screenTop + $(window).height(),
                    domArr = [];

                if (typeof offset !== 'number') {
                    offset = 50;
                }

                $all.each(function (index, element) {
                    var elemTop = $(element).offset().top,
                        elemBottom = elemTop + $(element).height(); /* jQuery可以用outerHeight*/

                    if (elemTop <= screenBottom + offset && elemBottom >= screenTop - offset) {  /* 节点顶部在屏幕底部以上 && 节点底部在屏幕顶部以下*/
                        domArr.push(element);
                    }
                });

                return domArr;
            },
            _run = function (className, func) {    /* 触发*/
                clearTimeout(_timeoutId);
                _timeoutId = setTimeout(function () {
                    _lazyLoad(_getImgArr(className), className, dataSrc, func, dataError, errorFunc);
                }, 200);
            },
            _init = function (className, func) {
                _run(className, func);

                $(window).on('scroll' + '.' + _namespace, function () {
                    _run(className, func);
                });
            };

        this.stop = function () {    /* 解绑事件绑定*/
            $(window).off('scroll' + '.' + _namespace);
        };

        _init(className, func);
    }

    /* 使用测试*/
    var a = new ImgLazyLoad('j-img-1'),
        b = new ImgLazyLoad(
            'j-img-2',
            'data-src-user',
            function (e) {
                console.log('成功', this, this === e);
            },
            'data-error-user',
            function (e) {
                console.log('失败', this, this === e);
            }
        );

    //a.stop();
    //b.stop();
</script>
```
[JSFiddle Demo](https://jsfiddle.net/realgeoffrey/j9dkuwwv/)

### jQuery或Zepto获取`HTTP response header`信息
```javascript
/**
 * 获取HTTP response header信息
 * @param {String} [requestName] - 协议头字段名；若不传值，则返回完整HTTP头
 * @returns {String|Boolean} text - HTTP头信息 或 '' 或 false
 */
function getResponseHeaders(requestName) {
    var text = '';

    $.ajax({
        type: 'HEAD',
        url: document.location.href,
        async: false,
        complete: function (xhr, data) {
            var responseHeaders, headerArr, i;

            if (data !== 'error' && data !== 'timeout' && data !== 'parsererror') {
                responseHeaders = xhr.getAllResponseHeaders();

                if (requestName) {
                    requestName += ': ';

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
                text = false;

                console.log('获取头信息错误: ' + data);
            }
        }
    });

    return text;
}
```

### jQuery修复HTML标签`placeholder`属性无效
```javascript
function fixPlaceholder($dom) {
    $dom = $dom || $('input, textarea');

    if (!('placeholder' in document.createElement('input'))) {
        $dom.each(function (index, element) {
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
1. jQuery

    ```html
    <style>
        .样式类 {
            position: fixed;
            _position: absolute;
            left: 50%;
            top: 50%;
            margin-top: -30px;
            margin-left: -450px;
            width: 900px;
            text-align: center;

            p {
                @include inline-block;
                max-width: 840px;
                _width: 840px;
                padding: 15px 30px;
                line-height: 30px;
                font-size: 14px;
                color: #fff;
                word-wrap: break-word;
                background-color: rgba(0, 0, 0, .7);
                filter: progid:DXImageTransform.Microsoft.Gradient(startColorStr=#70000000, endColorStr=#70000000)\9;
                *zoom: 1;
            }
        }
    </style>
    <script>
        function alertToast() {
            if ($('.j-pop-toast').length === 0) {
                $('body').append('<div class="j-pop-toast 样式类" style="display: none;"><p></p></div>');
            }
    
            var $toast = $('.j-pop-toast'),
                $text = $toast.children('p'),
                self = arguments.callee,
                textArr = [],
                i, text;
    
            clearTimeout(self.setTimeoutId);
    
            for (i = 0; i < arguments.length; i++) {
                textArr.push(arguments[i]);
            }
    
            text = textArr.join('<br>');

            $text.html(text);

            setTimeout(function () {
                $toast.fadeIn(1000);
            }, 0);

            self.setTimeoutId = setTimeout(function () {
                $toast.fadeOut(1000);
            }, 2500);
        }


        /* 使用测试*/
        alertToast('<span style="color: red;">red</span>', '哈哈');
    </script>
    ```
2. Zepto

    ```html
    <style>
        .样式类 {
            transition: 1s;
            position: fixed;
            left: 50%;
            top: 50%;
            margin-left: rem(-230);
            margin-top: rem(-49);
            width: rem(460);
            text-align: center;

            p {
                display: inline-block;
                max-width: rem(460);    /* box-sizing:border-box*/
                min-width: rem(166);
                padding: rem(29) rem(30);
                line-height: rem(40);
                font-size: rem(28);
                color: #fff;
                word-wrap: break-word;
                background-color: rgba(0, 0, 0, .7);
                border-radius: rem(4);
            }
            &.z-hidden {
                visibility: hidden;
                opacity: 0;
            }
        }
    </style>
    <script>
        function alertToast() {
            if ($('.j-pop-toast').length === 0) {
                $('body').append('<div class="j-pop-toast z-hidden 样式类"><p></p></div>');
            }
    
            var $toast = $('.j-pop-toast'),
                $text = $toast.children('p'),
                self = arguments.callee,
                textArr = [],
                i, text;
    
            clearTimeout(self.setTimeoutId);
    
            for (i = 0; i < arguments.length; i++) {
                textArr.push(arguments[i]);
            }
    
            text = textArr.join('<br>');
    
            $text.html(text);

            setTimeout(function () {
                $toast.removeClass('z-hidden');
            }, 0);
    
            self.setTimeoutId = setTimeout(function () {
                $toast.addClass('z-hidden');
            }, 2500);
        }
     

        /* 使用测试*/
       alertToast('<span style="color: red;">red</span>', '哈哈');
    </script>
    ```

### jQuery或Zepto全选、取消全选
```html
所有：
<input type="checkbox" name="all">

单个：
<input type="checkbox" name="ones">
<input type="checkbox" name="ones">
<input type="checkbox" name="ones">
...

<script>
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
</script>
```

### jQuery或Zepto节点跟随屏幕滚动（`margin-top`）
```html
<div class="clearfix">
    <div class="father">
        可有可无的、带margin或不带margin的节点
        <div class="target">target内容</div>
        可有可无的、带margin或不带margin的节点，ie6、7下可能需要触发hasLayout
    </div>
    <div class="dependent">
        父级的兄弟节点
    </div>
</div>

<script>
    /**
     * 跟随屏幕滚动（margin-top变化）
     * @constructor
     * @param {String} target - 目标节点
     * @param {String} father - 目标节点的父级节点
     * @param {String} dependent - 目标节点的父级节点的兄弟参照物（跟随不超过此参照物）
     */
    function FollowMarginTop(target, father, dependent) {
        if (typeof Date.now !== 'function') {
            Date.now = function () {
                return new Date().getTime();
            };
        }

        var namespace = Date.now(), /* 事件命名空间*/
            $target = $(target),
            startOffset = $target.offset().top,
            targetMarginTop = parseInt($target.css('margin-top')) || 0,
            prevMarginBottom = parseInt($target.prev().css('margin-bottom')) || 0,
            defaultMarginTop = Math.max(targetMarginTop, prevMarginBottom),
            maxMarginTop = $(dependent).height() - $(father).height() + defaultMarginTop; /* jQuery可以用outerHeight*/

        $(window).on('scroll' + '.' + namespace, function () {
            var marginTop = $(window).scrollTop() - startOffset + defaultMarginTop;

            if (marginTop > defaultMarginTop) {
                if (marginTop > maxMarginTop) {
                    marginTop = maxMarginTop;
                }
            } else {
                marginTop = defaultMarginTop;
            }

            $target.css({'margin-top': marginTop});
        });

        this.stop = function () {
            $target.css({'margin-top': targetMarginTop});
            $(window).off('scroll' + '.' + namespace);
        };
    }


    /* 使用测试*/
    var a = new FollowMarginTop('.target', '.father', '.dependent');

    //a.stop();
</script>
```
[JSFiddle Demo](https://jsfiddle.net/realgeoffrey/gc45ehdb/)

### jQuery或Zepto节点跟随屏幕滚动（`fixed`）
```html
<style>
    .z-affix-top {
        width: 宽度;
        position: fixed;
        left: ;
        margin-left: ;
        top: ;
    }
    .z-affix-bottom {
        width: 宽度;
        position: absolute;
        left: ;
    }
</style>

<script>
    /**
     * 跟随屏幕滚动（fixed）
     * @constructor
     * @param {Object} $target - 跟屏目标的jQuery对象
     * @param {Number} topOffset - 触发添加topClass的距文档顶部的距离
     * @param {String} topClass - 跟随屏幕的类，要规定节点的宽度、位置（fixed）
     * @param {Number} [bottomOffset = 0] - 触发添加bottomClass的距文档底部的距离
     * @param {String} [bottomClass = ''] - 触底的类，要规定节点的宽度、位置（absolute），top由代码计算获得
     */
    function FollowFixed($target, topOffset, topClass, bottomOffset, bottomClass) {
        if (typeof Date.now !== 'function') {
            Date.now = function () {
                return new Date().getTime();
            };
        }

        var _namespace = Date.now(), //事件命名空间
            _isIE = function (num) {    //判断ie版本
                var dom = document.createElement('b');

                dom.innerHTML = '<!--[if IE ' + num + ']><i></i><![endif]-->';

                return dom.getElementsByTagName('i').length;
            },
            _followFixed = function () {
                var scollTop = $(window).scrollTop(),
                    documentHeight = $(document).height(),
                    targetHeight = $target.height();   //jQuery可以用outerHeight

                if (scollTop >= topOffset) {    //滚动距离超过topOffset
                    if (!$target.hasClass(bottomClass)) {   //没有添加bottomClass
                        if (documentHeight - ($target.offset().top + targetHeight) > bottomOffset) {    //节点底部距离文档底部距离 > bottomOffet
                            $target.removeClass(bottomClass).addClass(topClass)
                                .removeAttr('style');
                        } else if (bottomClass) {   //超过bottomOffet,并且bottomClass存在
                            $target.removeClass(topClass).addClass(bottomClass)
                                .css('top', documentHeight - $target.offsetParent().offset().top - targetHeight - bottomOffset);
                        }
                    } else {    //添加了bottomClass
                        if (scollTop < $target.offset().top) {  //滚动小于节点
                            $target.removeClass(bottomClass).addClass(topClass)
                                .removeAttr('style');
                        }
                    }
                } else {
                    $target.removeClass(topClass + ' ' + bottomClass)
                        .removeAttr('style');
                }
            };

        if (!_isIE(6)) {
            bottomOffset = bottomOffset || 0;
            bottomClass = bottomClass || '';

            _followFixed();

            $(window).on('scroll' + '.' + _namespace, _followFixed);
        }

        this.stop = function () {
            $target.removeClass(topClass + ' ' + bottomClass);
            $(window).off('scroll' + '.' + _namespace);
        };
    }


    /* 使用测试*/
    var a = new FollowFixed($('.target'), $('.target').offset().top, 'z-affix-top', 200, 'z-affix-bottom');

    //a.stop();
</script>
```
[JSFiddle Demo](https://jsfiddle.net/realgeoffrey/v69fr64x/)

### jQuery或Zepto模拟手机翻转（使页面都以“横屏”展示）
```html
<style>
    .dom {
        position: fixed;
        top: 0;
        left: 0;
    }
    .z-reversal {
        top: 50%;
        left: 50%;
        /*margin: 0;*/
        -webkit-transform: translate(-50%, -50%) rotate(90deg);
        transform: translate(-50%, -50%) rotate(90deg);
    }
</style>

<div class="dom" id="j-dom-1">...</div>
<div class="dom" id="j-dom-2">...</div>

<script type="text/javascript">
    /**
     * 横屏展示
     * @constructor
     * @param {String} selector - 选择器
     * @param {String} className - 翻转类
     */
    var ReversalAct = function (selector, className) {
        if (typeof Date.now !== 'function') {
            Date.now = function () {
                return new Date().getTime();
            };
        }

        var _setTimeoutId1 = '',
            _setTimeoutId2 = '',
            _namespace = Date.now(),
            _resizeEvent = 'onorientationchange' in window ? 'orientationchange' : 'resize',
            _portraitFunc = function (selector, className) {    /* 屏幕高度>宽度（竖屏），增加“顺时针翻转90度的类”*/
                var $dom = $(selector);

                if ($(window).height() > $(window).width()) {
                    $dom.addClass(className);
                } else {
                    $dom.removeClass(className);
                }
            },
            _resizeFunc = function (selector) {   /* 设置高宽的值（边长较长的一边设置为宽度，较短的设置为高度）*/
                var wHeight = $(window).height(),
                    wWidth = $(window).width(),
                    i;

                if (wHeight > wWidth) {
                    i = wHeight;
                    wHeight = wWidth;
                    wWidth = i;
                }

                $(selector).css({'width': wWidth + 'px', 'height': wHeight + 'px'});
            },
            _bindEvent = function (selector, className) {
                $(window).on('resize' + '.' + _namespace, function () {
                    clearTimeout(_setTimeoutId2);

                    _setTimeoutId2 = setTimeout(function () {
                        _resizeFunc(selector);
                    }, 500);
                }).on(_resizeEvent + '.' + _namespace, function () {
                    clearTimeout(_setTimeoutId1);

                    _setTimeoutId1 = setTimeout(function () {
                        _portraitFunc(selector, className);
                    }, 500);
                });
            },
            _init = function (selector, className) {
                _bindEvent(selector, className);
                _resizeFunc(selector);
                _portraitFunc(selector, className);
            };

        _init(selector, className);

        this.stop = function () {
            $(window).off('resize' + '.' + _namespace)
                .off(_resizeEvent + '.' + _namespace);

            $(selector).removeClass(className)
                .removeAttr('style');
        };
    };


    /* 使用测试*/
    var a = new ReversalAct('#j-dom-1, #j-dom-2', 'z-reversal');

    //a.stop();
</script>
```
> 如果对不是全屏的节点使用翻转函数，需要给节点设置`width: 宽度 !important;height: auto !important;`。

### jQuery或Zepto点击指定区域以外执行函数
1. jQuery

    ```javascript
    /**
     * 点击指定区域以外执行函数（一次性）
     * @param {Object} $dom - jQuery节点
     * @param {Function} callback - 回调函数
     * @param {Number} [limit] - 自动失效时间，若没有传或者传0则不会自动失效
     * @param {String|Number} [namespace = Date.now()] - 事件命名空间
     */
    function beyongOneAct($dom, callback, limit, namespace) {
        if (typeof Date.now !== 'function') {
            Date.now = function () {
                return new Date().getTime();
            };
        }

        namespace = namespace || Date.now();

        if (limit) {
            setTimeout(function () {
                $(document).off('click.' + namespace);
            }, limit);
        }

        $(document).on('click.' + namespace, function (e) {
            if (!$dom.is(e.target) && $dom.has(e.target).length === 0) {    /* 点击不在指定区域内*/
                $(document).off('click.' + namespace);

                if (typeof callback === 'function') {
                    callback();
                }
            }
        });
    }


    /* 使用测试*/
    beyongOneAct($('.dom1,#dom2'), function () {
        console.log('点击区域外');
    }, 1000);
    ```
    [JSFiddle Demo](https://jsfiddle.net/realgeoffrey/enyxz9a6/)
2. Zepto

    ```javascript
    function beyongOneAct($dom, callback, limit, namespace) {
        if (typeof Date.now !== 'function') {
            Date.now = function () {
                return new Date().getTime();
            };
        }

        namespace = namespace || Date.now();

        if (limit) {
            setTimeout(function () {
                $(document.body).off('click.' + namespace);
            }, limit);
        }

        $(document.body).on('click.' + namespace, function (e) {
            var withinArea = false,
                i;

            for (i = 0; i < $dom.length; i++) {
                if ($dom.get(i) === e.target || $dom.eq(i).has(e.target).length !== 0) {
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


    /* 使用测试*/
    beyongOneAct($('.dom1,#dom2'), function () {
        console.log('点击区域外');
    }, 1000);
    ```
    [JSFiddle Demo](https://jsfiddle.net/realgeoffrey/mvv9wxnw/)

### jQuery或Zepto hover展示内容并且可跨越间隙到内容
```html
<div class="j-box">
    <div class="j-trigger">
        hover
    </div>
    
    <div class="j-bullet" style="display: none;">
        展示内容
    </div>
</div>

<script type="text/javascript">
    var globalObj = {setTimeoutId: ''};

    $(document).on('mouseenter', '.j-trigger', function () {
        clearTimeout(globalObj.setTimeoutId);

        $(this).closest('.j-box').find('.j-bullet').show();
    }).on('mouseleave', '.j-trigger', function () {
        clearTimeout(globalObj.setTimeoutId);

        globalObj.setTimeoutId = setTimeout(function () {
            $('.j-bullet').hide();
        }, 500);
    }).on('mouseenter', '.j-bullet', function () {
        clearTimeout(globalObj.setTimeoutId);
    }).on('mouseleave', '.j-bullet', function () {
        globalObj.setTimeoutId = setTimeout(function () {
            $('.j-bullet').hide();
        }, 100);
    });
</script>
```
[JSFiddle Demo](https://jsfiddle.net/realgeoffrey/zs6a7aco/)

### jQuery或Zepto启动、暂停CSS动画
```html
<style>
    .dom.z-hover {
        animation: func 1s infinite;
    }
    @keyframes func {

    }
</style>

<div class="dom j-dom-1">...</div>
<div class="dom j-dom-2">...</div>

<script>
    /**
     * hover触发animation
     * @constructor
     * @param {String} selector - 选择器
     * @param {String} hoverClass - 类名
     */
    function AnimationHover(selector, hoverClass) {
        if (typeof Date.now !== 'function') {
            Date.now = function () {
                return new Date().getTime();
            };
        }

        var _isStop = false, /* 停止动画flag*/
            _namespace = Date.now(), /* 事件命名空间*/
            _init = function (selector, hoverClass) {
                $(document).on('mouseenter' + '.' + _namespace, selector, function () {
                    $(this).addClass(hoverClass);

                    _isStop = false;
                }).on('mouseleave' + '.' + _namespace, selector, function () {
                    _isStop = true;
                }).on('animationiteration' + '.' + _namespace, selector, function () {
                    if (_isStop) {
                        $(this).removeClass(hoverClass);

                        _isStop = false;
                    }
                });
            };

        _init(selector, hoverClass);

        this.stop = function () {
            $(selector).removeClass(hoverClass);

            $(document).off('mouseenter' + '.' + _namespace + ' ' + 'mouseleave' + '.' + _namespace + ' ' + 'animationiteration' + '.' + _namespace, selector);
        }
    }


    /* 使用测试*/
    var a = new AnimationHover('.j-dom-1', 'z-hover');
    var b = new AnimationHover('.j-dom-2', 'z-hover');

    //a.stop;
    //b.stop;
</script>
```
[JSFiddle Demo](https://jsfiddle.net/realgeoffrey/Lukonj4s/)