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
        i += 1;

        window.scrollTo((scrollToX - scrollFromX) / time * i + scrollFromX, (scrollToY - scrollFromY) / time * i + scrollFromY);

        if (i >= time) {
            clearInterval(myself.setIntervalId);
        }
    }, runEvery);
}
```
>使用[velocity动画库](https://github.com/julianshapiro/velocity)（[中文文档](http://www.mrfront.com/docs/velocity.js/)）做所有的动画（包括JS和CSS）才是最简单且性能最佳的选择。
>如滚动到某位置：`$('html').velocity('scroll', {offset: y轴像素, duration: 毫秒});`。

### *原生JS*判断浏览器所在系统
```javascript
function detectOS (ua, pf) {
  ua = ua || window.navigator.userAgent
  pf = window.navigator.platform

  var os = ''

  if (/iPhone|iPad|iPod|iOS/.test(ua)) {
    os = 'iOS'
  } else if (/Android/.test(ua)) {
    os = 'Android'
  } else if (/\bWindows Phone/.test(ua)) {
    os = 'Windows Phone'
  } else {
    if (pf === 'Mac68K' || pf === 'MacPPC' || pf === 'Macintosh' || pf === 'MacIntel') {
      os = 'macOS'
    } else if (pf === 'Win32' || pf === 'Windows') {
      if (/Windows NT 5.0/.test(ua) || /Windows 2000/.test(ua)) {
        os = 'Win2000'
      } else if (/Windows NT 5.1/.test(ua) || /Windows XP/.test(ua)) {
        os = 'WinXP'
      } else if (/Windows NT 5.2/.test(ua) || /Windows 2003/.test(ua)) {
        os = 'Win2003'
      } else if (/Windows NT 6.0/.test(ua) || /Windows Vista/.test(ua)) {
        os = 'WinVista'
      } else if (/Windows NT 6.1/.test(ua) || /Windows 7/.test(ua)) {
        os = 'Win7'
      } else if (/Windows NT 10.0/.test(ua) || /Windows 10/.test(ua)) {
        os = 'Win10'
      } else {
        os = 'Windows'
      }
    } else if (pf === 'X11') {
      os = 'Unix'
    } else if (/Linux/.test(pf)) {
      os = 'Linux'
    }
  }

  return os
}
```

### *原生JS*返回用户所在移动平台
```javascript
// 返回用户所在平台（微信、QQ、微博、QQ空间）
function platform (ua) {
  ua = ua || window.navigator.userAgent

  var platform

  if (/MicroMessenger/.test(ua)) {
    platform = 'weixin'
  } else if (/QQ\//.test(ua)) {
    platform = 'qq'
  } else if (/\bWeibo|__weibo__\d/.test(ua)) {
    platform = 'weibo'
  } else if (/Qzone\//.test(ua)) {
    platform = 'qzone'
  } else {
    platform = 'other'
  }

  return platform
}
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
     * 读取一个cookie的值
     * @param {String} key - 名
     * @returns {String|Null} - 值 或 null
     */
    getItem: function (key) {
        if (!key) {

            return null;
        } else {

            return decodeURIComponent(document.cookie.replace(new RegExp('(?:(?:^|.*;)\\s*' + encodeURIComponent(key).replace(/[\-\.\+\*]/g, '\\$&') + '\\s*\\=\\s*([^;]*).*$)|^.*$'), '$1')) || null;
        }
    },

    /**
     * 新建或更新一个cookie
     * @param {String} key - 名
     * @param {String} value - 值
     * @param {Number|Date|String|Infinity} [deadline] - 过期时间。默认为关闭浏览器后过期
     * @param {String} [path] - 路径。默认为当前文档位置的路径
     * @param {String} [domain] - 域名。默认为当前文档位置的路径的域名部分
     * @param {Boolean} [secure] - 是否“仅通过https协议传输”。默认为否
     * @returns {Boolean} - 操作成功或失败
     */
    setItem: function (key, value, deadline, path, domain, secure) {
        if (!key || /^(?:expires|max\-age|path|domain|secure)$/i.test(key)) {

            return false;
        } else {
            var expires = '';

            if (deadline) {
                switch (deadline.constructor) {
                    case Number:
                        expires = deadline === Infinity ? '; expires=Fri, 31 Dec 9999 23:59:59 GMT' : '; max-age=' + deadline;
                        break;
                    case String:
                        expires = '; expires=' + deadline;
                        break;
                    case Date:
                        expires = '; expires=' + deadline.toUTCString();
                        break;
                }
            }

            document.cookie = encodeURIComponent(key) + '=' + encodeURIComponent(value) + expires + (domain ? '; domain=' + domain : '') + (path ? '; path=' + path : '') + (secure ? '; secure' : '');

            return true;
        }
    },

    /**
     * 删除一个cookie
     * @param {String} key - 名
     * @param {String} [path] - 路径。默认为当前文档位置的路径
     * @param {String} [domain] - 域名。默认为当前文档位置的路径的域名部分
     * @returns {Boolean} - 操作成功或失败
     */
    removeItem: function (key, path, domain) {
        if (!key || !this.hasItem(key)) {

            return false;
        } else {
            document.cookie = encodeURIComponent(key) + '=; expires=Thu, 01 Jan 1970 00:00:00 GMT' + ( domain ? '; domain=' + domain : '') + ( path ? '; path=' + path : '');

            return true;
        }
    },

    /**
     * 检查一个cookie是否存在
     * @param {String} key - 名
     * @returns {Boolean} - 存在与否
     */
    hasItem: function (key) {
        if (!key) {

            return false;
        } else {

            return (new RegExp('(?:^|;\\s*)' + encodeURIComponent(key).replace(/[\-\.\+\*]/g, '\\$&') + '\\s*\\=')).test(document.cookie);
        }
    },

    /**
     * 返回cookie名字的数组
     * @returns {Array} - 名的数组 或 []
     */
    listItems: function () {
        if (document.cookie === '') {

            return [];
        } else {
            var keys = document.cookie.replace(/((?:^|\s*;)[^\=]+)(?=;|$)|^\s*|\s*(?:\=[^;]*)?(?:\1|$)/g, '').split(/\s*(?:\=[^;]*)?;\s*/),
                i, len;

            for (i = 0, len = keys.length; i < len; i++) {
                keys[i] = decodeURIComponent(keys[i]);
            }

            return keys;
        }
    },

    /**
     * 清空所有cookie
     * @returns {Boolean} - 操作成功或失败
     */
    clear: function () {
        if (document.cookie === '') {

            return false;
        } else {
            var keys = document.cookie.replace(/((?:^|\s*;)[^\=]+)(?=;|$)|^\s*|\s*(?:\=[^;]*)?(?:\1|$)/g, '').split(/\s*(?:\=[^;]*)?;\s*/),
                i, len;

            for (i = 0, len = keys.length; i < len; i++) {
                this.removeItem(decodeURIComponent(keys[i]));
            }

            return true;
        }
    }
};
```
>参考[MDN:cookie](https://developer.mozilla.org/zh-CN/docs/Web/API/Document/cookie#一个小框架：一个完整支持unicode的cookie读取写入器)。

>简单判断是否存在某cookie：
>
>```javascript
>function hasCookie (checkKey) {
>  checkKey = checkKey.toString()
>
>  var cookieArr = document.cookie.split('; '),
>    tempArr, key, value
>
>  for (var i = 0, len = cookieArr.length; i < len; i++) {
>    if (cookieArr[i] !== '') {
>      tempArr = cookieArr[i].split('=')
>      key = tempArr.shift()
>      value = tempArr.join('=')
>
>      if (key === checkKey) {
>        /* 操作value*/
>
>        return true
>      }
>    }
>  }
>
>  return false
>}
>```

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

### *原生JS*获取URL相关信息
```javascript
/**
 * 获取URL相关信息
 * @param {String} [url = window.location.href] - URL
 * @returns {Object} location - 包括href、protocol、hostname、port、pathname、search、searchObj、hash的对象
 */
function getLocation (url) {
  url = url || window.location.href

  /* 为了方便阅读*/
  var _protocol = /^(?:([A-Za-z]+):)?/.source,
    _slash = /\/*/.source,
    _hostname = /([0-9A-Za-z.\-]+)/.source,
    _port = /(?::(\d+))?/.source,
    _pathname = /(\/[^?#]*)?/.source,
    _search = /(?:\?([^#]*))?/.source,
    _hash = /(?:#(.*))?$/.source

  var regex = new RegExp(_protocol + _slash + _hostname + _port + _pathname + _search + _hash, 'g'),
    regexArr = regex.exec(url),
    keyArr = ['href', 'protocol', 'hostname', 'port', 'pathname', 'search', 'hash'],
    location = { 'searchObj': {} },
    search, searchArr, searchItem, key, value

  keyArr.forEach(function (item, index) {
    location[item] = regexArr[index] || ''
  })

  search = location['search']

  searchArr = search.split('&')

  for (var i = 0, len = searchArr.length; i < len; i++) {
    if (searchArr[i] !== '') {
      searchItem = searchArr[i].split('=')
      key = searchItem.shift()
      value = searchItem.join('=')
      location['searchObj'][key] = value
    }
  }

  return location
}
```
>参考[用正则表达式分析 URL](http://harttle.com/2016/02/23/javascript-regular-expressions.html)。

>获取某search值：
>
>```javascript
>/**
> * 获取某search值
> * @param {String} checkKey - search的key
> * @param {String} [search = window.location.search] - search总字符串
> * @returns {String|Boolean} - search的value 或 不存在false
> */
>function getSearchValue (checkKey, search) {
>  checkKey = checkKey.toString()
>  search = search || window.location.search
>
>  if (search.slice(0, 1) === '?') {
>    search = search.slice(1)
>  }
>
>  var searchArr = search.split('&'),
>    tempArr, key, value
>
>  for (var i = 0, len = searchArr.length; i < len; i++) {
>    if (searchArr[i] !== '') {
>      tempArr = searchArr[i].split('=')
>      key = tempArr.shift()
>      value = tempArr.join('=')
>
>      if (key === checkKey) {
>
>        return value
>      }
>    }
>  }
>
>  return false
>}
>```

>拼接接口url时，可以在api字符串最后添加`?`并且加上一些固定不变的search参数，在使用url时候都以`&参数=值`的形式添加额外参数：
>
>>`xxx/xxx?&a=1`可以正常解析
>
>```javascript
>const api1 = 'xxx/xxx?'
>const api2 = 'xxx/xxx?v=1.0'
>
>// 使用时
>url1 = api1 + '&a=1' + '&b=2' + '&c=3'
>url2 = api2 + '&a=1' + '&b=2' + '&c=3'
>```

### *原生JS*在URL末尾添加查询名值对
```javascript
/**
 * 在URL末尾添加search名值对
 * @param {String} url - URL
 * @param {String} name - 名
 * @param {String} value - 值
 * @returns {String} - 添加完毕的URL
 */
function addUrlSearch(url, name, value) {
    if (!name || !value) {

        return url;
    }

    var hashIndex = url.indexOf('#') !== -1 ? url.indexOf('#') : url.length,
        newUrl = url.slice(0, hashIndex),
        hash = url.slice(hashIndex),
        searchIndex = newUrl.indexOf('?');

    if (searchIndex === -1) {
        newUrl += '?';
    } else if (searchIndex !== newUrl.length - 1) {
        newUrl += '&';
    }

    newUrl += encodeURIComponent(name) + '=' + encodeURIComponent(value) + hash;

    return newUrl;
}
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
            i += 1;

            return time + i - 1;
        }
    }());

    var run = function (url) {
        var data = window['imgLogData'] || (window['imgLogData'] = {}),
            img = new Image(),
            uid = _unique();

        data[uid] = img;    //防止img被垃圾处理

        img.onload = img.onerror = function () {    /* 成功或失败后销毁对象*/
            img.onload = img.onerror = null;
            img = null;
            delete data[uid];
        };

        img.src = url + '&_cache=' + uid;   //发送统计内容
    };

    return run;
}());


/* 使用测试*/
sendLog('统计url');
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
            flag = parseInt(arr1[i], 10) < parseInt(arr2[i], 10) ? '<' : '>';

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
>注意：
>
>1. 检查不同语言原始返回的随机值两边端点开闭情况——不同的开闭区间影响最终算法。
>2. 获取到的每个整数的概率是否均等——用向下取整代替四舍五入可以使概率均等。

```javascript
/**
 * 选取范围内随机值
 * @param {Number} min - 下限（或上限）
 * @param {Number} max - 上限（或下限）
 * @returns {Number} - 上下限区间内的随机值
 */
function randomFrom(min, max) {
    var temp;

    if (min > max) {
        temp = min;
        min = max;
        max = temp;
    }

    return Math.floor(Math.random() * (max - min + 1) + min);
}
```
>`Math.random()`返回`[0,1)`。假设返回的值的开闭区间改变：
>
>1. 如果返回的是：`(0,1)`，则返回`Math.floor(Math.random() * (max - min + 2) + min - 1);`。
>2. 如果返回的是：`(0,1]`，则返回`Math.floor(Math.random() * (max - min + 1) + min - 1);`。
>3. 如果返回的是：`[0,1]`，则返回`Math.floor(Math.random() * (max - min) + min);`。

### *原生JS*产生随机数
```javascript
/**
 * 随机数产生
 * @param {Number} length - 随机数长度
 * @param {String} [charset = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'] - 随机数的字符
 * @returns {String} - 随机数
 */
function random(length, charset) {
    charset = charset || 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';

    return Array.apply(null, new Array(length)).map(function () {

        return charset.charAt(Math.floor(Math.random() * charset.length));
    }).join('');
}
```

### *原生JS*格式化文件大小
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
  }
};


/* 使用测试*/
var a = format.fileSize(数字);
```

### *原生JS*判断对象是否为空
```javascript
function isObjEmpty(obj) {
    var i;

    if (obj !== Object(obj)) {  /* 参数不是对象*/
        throw new TypeError('参数不是对象');
    } else if (typeof Object.keys === 'function') { /* ie9+*/

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

### *原生JS*触摸屏模拟点击事件（消除“延时300毫秒后才触发click事件”，使点击事件提前触发）
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
        /* 触发滑动事件要做的事情（如什么都不做）*/
    } else {
        /* 触发点击事件要做的事情*/
    }
}, false);

/* 还要处理浏览器默认点击事件（如a标签）*/
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

>更全面的性能监听：[stats.js](https://github.com/mrdoob/stats.js/)。

### *原生JS*科学计数法转换成字符串的数字
```javascript
function eToString(number) {
    number = number.toString(10);

    var regex = /^(\d)(?:\.(\d*))?[eE]([+-]?)(\d+)$/,   //科学计数法
        regexArr = regex.exec(number);

    if (regexArr === null) {

        return number;
    } else {
        var dotNumber = regexArr[2] ? regexArr[2] : '',
            dotLength = dotNumber.length, //小数位数
            multiple = regexArr[4], //10进制位数
            gap = Math.abs(multiple - dotLength),
            tempArr = [],
            i, result;

        if (regexArr[3] !== '-') {  /* 大于1*/
            if (multiple >= dotLength) {    /* 没有小数*/
                for (i = 0; i < gap; i++) {
                    tempArr.push('0');
                }

                result = regexArr[1] + dotNumber + tempArr.join('');
            } else {  /* 有小数*/
                result = regexArr[1] + dotNumber.substr(0, multiple) + '.' + dotNumber.substr(multiple);
            }
        } else { /* 小于1*/
            if (multiple === '0') {
                result = regexArr[1] + dotNumber;
            } else {
                for (i = 0; i < multiple - 1; i++) {
                    tempArr.push('0');
                }

                result = '0.' + tempArr.join('') + regexArr[1] + dotNumber;
            }
        }
    }

    return result;
}
```

### *原生JS*用整数进行小数的四则运算（避免浮点数运算误差）
```javascript
var fourOperations = {
    add: function (arg1, arg2) {    /* 加*/
        var int1 = parseInt(arg1.toString().replace('.', ''), 10),
            int2 = parseInt(arg2.toString().replace('.', ''), 10),
            dotLength1, dotLength2, gap, gapMultiple, multiple;

        try {
            dotLength1 = arg1.toString().split('.')[1].length;
        } catch (e) {
            dotLength1 = 0;
        }
        try {
            dotLength2 = arg2.toString().split('.')[1].length;
        } catch (e) {
            dotLength2 = 0;
        }

        gap = Math.abs(dotLength1 - dotLength2);

        if (gap > 0) {
            gapMultiple = Math.pow(10, gap);

            if (dotLength1 < dotLength2) {
                int1 = int1 * gapMultiple;
            } else {
                int2 = int2 * gapMultiple;
            }
        }

        multiple = Math.pow(10, Math.max(dotLength1, dotLength2));

        return (int1 + int2) / multiple;
    },
    sub: function (arg1, arg2) {    /* 减*/

        return this.add(arg1, -arg2);
    },
    mul: function (arg1, arg2) {    /* 乘*/
        var multiple;

        try {
            multiple = arg1.toString().split('.')[1].length;
        } catch (e) {
            multiple = 0;
        }
        try {
            multiple = multiple + arg2.toString().split('.')[1].length;
        } catch (e) {

        }

        return parseInt(arg1.toString().replace('.', ''), 10) * parseInt(arg2.toString().replace('.', ''), 10) / Math.pow(10, multiple);
    },
    div: function (arg1, arg2) {    /* 除*/
        var dotLength1, dotLength2;

        try {
            dotLength1 = arg1.toString().split('.')[1].length;
        } catch (e) {
            dotLength1 = 0;
        }
        try {
            dotLength2 = arg2.toString().split('.')[1].length;
        } catch (e) {
            dotLength2 = 0;
        }

        return parseInt(arg1.toString().replace('.', ''), 10) / parseInt(arg2.toString().replace('.', ''), 10) * Math.pow(10, dotLength2 - dotLength1);
    }
};
```

### *原生JS*大数加减法（不考虑小数和负数）
```javascript
var overRangeOperations = {
    add: function (arg1, arg2) {    /* 加*/
        /* 需要把科学计数法转化为字符串的数字*/
        arg1 = arg1.toString(10).split('');
        arg2 = arg2.toString(10).split('');

        var carry = 0,  //进位
            result = [],
            temp;

        while (arg1.length || arg2.length || carry) {
            temp = parseInt(arg1.pop() || 0, 10) + parseInt(arg2.pop() || 0, 10) + carry;
            result.unshift(temp % 10);
            carry = Math.floor(temp / 10);
        }

        return result.join('');
    },

    sub: function (arg1, arg2) {    /* 减*/
        /* 需要把科学计数法转化为字符串的数字*/
        arg1 = arg1.toString(10).split('');
        arg2 = arg2.toString(10).split('');

        var isArg2Bigger, // 标记arg2是否大于arg1
            result = [],
            i, len, temp;

        (function () {  /* 确保大数减小数*/
            isArg2Bigger = arg1.length < arg2.length;

            if (arg1.length === arg2.length) {
                for (i = 0, len = arg1.length; i < len; i++) {
                    if (arg1[i] === arg2[i]) {
                        continue;
                    }

                    isArg2Bigger = arg1[i] < arg2[i];

                    break;
                }
            }

            if (isArg2Bigger) {
                temp = arg1;
                arg1 = arg2;
                arg2 = temp;
            }
        }());

        while (arg1.length) {
            temp = parseInt(arg1.pop(), 10) - parseInt(arg2.pop() || 0, 10);

            if (temp >= 0) {
                result.unshift(temp);
            } else {
                result.unshift(temp + 10);

                arg1[arg1.length - 1] -= 1; //由于arg1一定大于等于arg2，所以不存在arg1[i-1]为undefined的情况
            }
        }

        result = result.join('').replace(/^0*/, '');    //去掉前面的0

        if (result === '') {
            result = 0;
        } else {
            result = (isArg2Bigger ? '-' : '') + result;
        }

        return result;
    }
};
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
        if (typeof dom.addEventListener === 'function') {   /* DOM2级，除ie8-*/
            dom.addEventListener(type, handle, false);
        } else if (typeof dom.attachEvent === 'function') { /* 所有ie浏览器*/
            dom.attachEvent('on' + type, handle);   //注意传入的参数和this的兼容
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
            dom.detachEvent('on' + type, handle);   //注意传入的参数和this的兼容
        } else {
            dom['on' + type] = null;
        }
    }
};
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
        }
        ```
    2. jQuery或Zepto
    
        ```javascript
        $('...').on('...', function (e) {
            e.preventDefault();
        });
        ```
3. 阻止冒泡 && 阻止默认行为

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
    function checkKeyCode(e) {
        var event = e || window.event,
            keyCode = event.charCode || event.keyCode;  /* 获取键值*/
    
        if (keyCode === 13) {   /* 查询键值表 例:13->换行*/
            /* 具体操作...*/
    
            /* 阻止冒泡&阻止默认行为*/
            if (e && e.stopPropagation) {
                e.stopPropagation();
                e.preventDefault();
            } else {
                window.event.cancelBubble = true;
                window.event.returnValue = false;
            }
        }
    }
    

    /* 使用测试*/
    addEvent(document.getElementById('test'), 'keydown', checkKeyCode);  //上面绑定事件
    ```
2. jQuery或Zepto

    ```javascript
    $(输入框选择器).on('keydown', function (e) {
        if (e.which === 13) {   /* 查询键值表 例:13->换行*/
            /* 具体操作...*/
    
            return false;   //阻止冒泡&阻止默认行为
        }
    });
    ```

### *原生JS*拖拽和放下
1. PC端的鼠标事件

    ```javascript
    function Drag(dom, parentDom) {
        var maxX = parentDom.offsetWidth - dom.offsetWidth,
            maxY = parentDom.offsetHeight - dom.offsetHeight,
            domX, domY, beginX, beginY;

        /* 绑定事件*/
        function _addHandler(dom, type, handle) {
            if (typeof dom.addEventListener === 'function') {
                dom.addEventListener(type, handle, false);
            } else if (typeof dom.attachEvent === 'function') {
                dom.attachEvent('on' + type, handle);
            } else {
                dom['on' + type] = handle;
            }
        }

        /* 解绑事件*/
        function _removeHandler(dom, type, handle) {
            if (typeof dom.removeEventListener === 'function') {
                dom.removeEventListener(type, handle, false);
            } else if (typeof dom.detachEvent === 'function') {
                dom.detachEvent('on' + type, handle);
            } else {
                dom['on' + type] = null;
            }
        }

        /* 阻止冒泡&阻止默认行为*/
        function _returnFalse(e) {
            if (e && e.stopPropagation) {
                e.stopPropagation();
                e.preventDefault();
            } else {
                window.event.cancelBubble = true;
                window.event.returnValue = false;
            }
        }

        /* 拖拽开始*/
        function actBegin(e) {
            e = e || window.event;

            domX = dom.offsetLeft;
            domY = dom.offsetTop;

            beginX = e.clientX; //或e.pageX/Y（ie不兼容）
            beginY = e.clientY;

            _addHandler(parentDom, 'mousemove', actMove);

            _returnFalse(e); //阻止冒泡、阻止默认行为
        }

        /* 拖拽移动*/
        function actMove(e) {
            e = e || window.event;

            var finalX = e.clientX - beginX + domX,
                finalY = e.clientY - beginY + domY;

            if (finalX > maxX) {
                finalX = maxX;
            } else if (finalX < 0) {
                finalX = 0;
            }
            if (finalY > maxY) {
                finalY = maxY;
            } else if (finalY < 0) {
                finalY = 0;
            }

            /* 具体移动（使用left、top）*/
            //requestAnimationFrame(function () {
                dom.style.left = finalX + 'px';
                dom.style.top = finalY + 'px';
            //});

            _returnFalse(e); //阻止冒泡、阻止默认行为
        }

        /* 拖拽取消*/
        function cancel(e) {
            _removeHandler(parentDom, 'mousemove', actMove);

            _returnFalse(e); //阻止冒泡、阻止默认行为
        }

        /* 绑定事件*/
        _addHandler(dom, 'mousedown', actBegin);
        _addHandler(parentDom, 'mouseup', cancel);
        _addHandler(parentDom, 'mouseleave', cancel);

        this.stop = function () {
            _removeHandler(dom, 'mousedown', actBegin);
            _removeHandler(parentDom, 'mouseup', cancel);
            _removeHandler(parentDom, 'mouseleave', cancel);
            _removeHandler(parentDom, 'mousemove', actMove);
        };
    }


    /* 使用测试*/
    var dom = document.getElementById('j-rect');
    var action = new Drag(dom, dom.offsetParent);

    //action.stop();
    ```
    [JSFiddle Demo](https://jsfiddle.net/realgeoffrey/7t25cm5t/)
2. WAP端的touch事件

    ```javascript
    function Drag(dom, parentDom) {
        var maxX = parentDom.offsetWidth - dom.offsetWidth,
            maxY = parentDom.offsetHeight - dom.offsetHeight,
            domX, domY, beginX, beginY;

        /* 拖拽开始*/
        function actBegin(e) {
            domX = dom.offsetLeft;
            domY = dom.offsetTop;

            beginX = e.touches[0].pageX;
            beginY = e.touches[0].pageY;

            parentDom.addEventListener('touchmove', actMove, false);

            /* 阻止冒泡、阻止默认行为*/
            e.stopPropagation();
            e.preventDefault();
        }

        /* 拖拽移动*/
        function actMove(e) {
            var finalX = e.touches[0].pageX - beginX + domX,
                finalY = e.touches[0].pageY - beginY + domY;

            if (finalX > maxX) {
                finalX = maxX;
            } else if (finalX < 0) {
                finalX = 0;
            }
            if (finalY > maxY) {
                finalY = maxY;
            } else if (finalY < 0) {
                finalY = 0;
            }

            /* 具体移动（使用left、top）*/
            requestAnimationFrame(function () {
                dom.style.left = finalX + 'px';
                dom.style.top = finalY + 'px';
            });

            /* 阻止冒泡、阻止默认行为*/
            e.stopPropagation();
            e.preventDefault();
        }

        /* 拖拽取消*/
        function cancel(e) {
            parentDom.removeEventListener('touchmove', actMove, false);

            /* 阻止冒泡、阻止默认行为*/
            e.stopPropagation();
            e.preventDefault();
        }

        /* 绑定事件*/
        dom.addEventListener('touchstart', actBegin, false);
        parentDom.addEventListener('touchend', cancel, false);
        parentDom.addEventListener('touchcancel', cancel, false);

        this.stop = function () {
            dom.removeEventListener('touchstart', actBegin, false);
            parentDom.removeEventListener('touchend', cancel, false);
            parentDom.removeEventListener('touchcancel', cancel, false);
            parentDom.removeEventListener('touchmove', actMove, false);
        };
    }


    /* 使用测试*/
    var dom = document.getElementById('j-rect');
    var action = new Drag(dom, dom.offsetParent);

    //action.stop();
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
        var start = 0, //光标起始位置
            selLen = 0, //光标选中长度
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
        start = parseInt(start, 10);
        if (!start) {
            start = 0;
        } else if (start > valueLen) {
            start = valueLen;
        }

        /* 初始化len*/
        len = parseInt(len, 10);
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
            var startTopScroll = dom.scrollTop, //滚动高度
                domHeight = dom.offsetHeight, //占据高度
                contentHeight = dom.scrollHeight; //内容高度（占据高度+可滚动最大高度

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

    dom.style.cssText = 'overflow: scroll; width: 100px; height: 100px;';

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
 * @param {Boolean} [immediate] - 设置为ture时，调用触发于开始边界而不是结束边界
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
 * @param {Object} [options] - 如果想忽略开始边界上的调用，传入{leading: false}；如果想忽略结尾边界上的调用，传入{trailing: false}
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
}, 1000);

$(window).on('scroll', a);
```
>来自[underscore](https://github.com/jashkenas/underscore)。

### *原生JS*不同进制数转换
```javascript
/**
 * 不同进制（2至36进制）换算（10个阿拉伯数字+26个字母）
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

### *原生JS*验证邮箱有效性
```javascript
function validateEmail(email) {

    return /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(email);
}
```
>来自[stackoverflow:Validate email address in JavaScript?](http://stackoverflow.com/questions/46155/validate-email-address-in-javascript#answer-46181)。

### *原生JS*创建兼容的XHR对象
```javascript
function createXHR() {
    if (typeof XMLHttpRequest !== 'undefined') {    //ie7+和其他浏览器

        return new XMLHttpRequest();
    } else if (typeof ActiveXObject !== 'undefined') {
        if (typeof arguments.callee.activeXString !== 'string') {
            var versions = ['MSXML2.XMLHttp.6.0', 'MSXML2.XMLHttp.3.0', 'MSXML2.XMLHttp'],
                i, len;

            for (i = 0, len = versions.length; i < len; i++) {
                try {
                    new ActiveXObject(versions[i]);
                    arguments.callee.activeXString = versions[i];
                    break;
                } catch (e) {
                    //跳过
                }
            }
        }

        return new ActiveXObject(arguments.callee.activeXString);   //返回ActiveXObject对象
    } else {//全部不支持，抛出错误
        throw new Error('don\'t support XMLHttpRequest');
    }
}


/* 使用测试*/
var xhr = createXHR();

xhr.onreadystatechange = function () {  //或DOM2级、ie事件绑定方式
    console.log(xhr.getResponseHeader(头), xhr.getAllResponseHeaders());

    if (xhr.readyState === 4) {
        if ((xhr.status >= 200 && xhr.status < 300) || xhr.status === 304) {
            console.log(xhr.responseText);
        } else {
            console.log('请求失败：' + xhr.status);
        }

        //xhr.abort();
        //xhr = null;
    }
};
xhr.open(请求类型, URL[, 是否异步[, 用户名[, 密码]]]);
xhr.setRequestHeader(头, 值);
xhr.send(null);
```

### *原生JS*动态添加样式、脚本
1. 动态添加样式

    1. 添加`<style>`

        ```javascript
        var newStyle = document.createElement('style');

        newStyle.type = 'text/css';

        try {
            newStyle.appendChild(document.createTextNode('CSS代码'));
        }
        catch (e) {
            newStyle.styleSheet.cssText = 'CSS代码';  //ie
        }

        document.getElementsByTagName('head')[0].appendChild(newStyle);
        ```
    2. 添加`<link>`

        >必须将`<link>`添加到`<head>`，才能保证在所有浏览器中的行为一致。

        ```javascript
        var newLink = document.createElement('link');

        newLink.rel = 'styleSheet';
        newLink.type = 'text/css';

        newLink.href = 'CSS文件地址';

        document.getElementsByTagName('head')[0].appendChild(newLink);
        ```
    3. 添加内嵌样式

        ```javascript
        var oneDom = document.getElementById('节点id');

        oneDom.style.cssText += '; CSS代码'
        ```

    >CSS代码，如 `div {background-color: yellow;}`。
2. 动态添加脚本

    1. 异步

        1. 直接`document.write`

            ```javascript
            document.write('<script src="JS文件地址"><\/script>');
            ```
        2. 动态改变已存在的`<script>`的`src`属性

            ```html
            <script type="text/javascript" id="节点id"></script>

            <script>
                document.getElementById('节点id').src = 'JS文件地址';
            </script>
            ```
        3. 动态创建`<script>`

            ```javascript
            var newScript = document.createElement('script'),
                appendPlace = document.body || document.getElementsByTagName('head')[0];

            newScript.type = 'text/javascript';

            newScript.src = 'JS文件地址';

            appendPlace.appendChild(newScript);
            ```
    2. 同步

        1. 添加JS代码

            ```javascript
            var newScript = document.createElement('script'),
                appendPlace = document.body || document.getElementsByTagName('head')[0];

            newScript.type = 'text/javascript';

            try {
                newScript.appendChild(document.createTextNode('JS代码'));
            }
            catch (e) {
                newScript.text = 'JS代码';  //ie8-，Safari老版本
            }

            appendPlace.appendChild(newScript);
            ```
        2. 添加`<script>`

            ```javascript
            /**
             * 同步加载JS脚本
             * @param {String} url - JS文件的相对路径或绝对路径
             * @returns {Boolean} - 是否加载成功
             */
            function syncLoadJS(url) {
                var xmlHttp,
                    appendPlace,
                    newScript;

                if (window.ActiveXObject) { /* ie*/
                    try {
                        xmlHttp = new ActiveXObject('Msxml2.XMLHTTP');
                    }
                    catch (e) {
                        xmlHttp = new ActiveXObject('Microsoft.XMLHTTP');
                    }
                } else if (window.XMLHttpRequest) {
                    xmlHttp = new XMLHttpRequest();
                }

                xmlHttp.open('GET', url, false);    //采用同步加载
                xmlHttp.send(null); //发送同步请求，如果浏览器为Chrome或Opera，必须发布后才能运行，不然会报错

                /* 4代表数据发送完毕*/
                if (xmlHttp.readyState == 4) {
                    /* 0为访问的本地，200到300代表访问服务器成功，304代表没做修改访问的是缓存*/
                    if ((xmlHttp.status >= 200 && xmlHttp.status < 300) || xmlHttp.status == 0 || xmlHttp.status == 304) {
                        newScript = document.createElement('script');
                        appendPlace = document.body || document.getElementsByTagName('head')[0];

                        newScript.type = 'text/javascript';

                        try {
                            newScript.appendChild(document.createTextNode(xmlHttp.responseText));
                        }
                        catch (e) {
                            newScript.text = xmlHttp.responseText;
                        }

                        appendPlace.appendChild(newScript);

                        return true;
                    }
                    else {

                        return false;
                    }
                }
                else {

                    return false;
                }
            }
            ```

### *原生JS*单词首字母大写
```javascript
function upperCaseWord(str) {

    return str.replace(/\b[a-zA-Z]/g, function (match) {

        return match.toUpperCase();
    });
}
```

### *原生JS*展示页面帧数
```javascript
/**
 * 展示fps
 * @constructor
 * @param {Object} [dom] - 展示的DOM
 */
function ShowFPS(dom) {
    var self = this;

    var fps = 0,
        before = Date.now(),
        now,
        show = function (fps) {
            dom.innerHTML = 'fps: ' + fps;
        };

    if (!dom) {
        dom = document.createElement('span');
        dom.style.position = 'fixed';
        dom.style.top = '0';
        document.getElementsByTagName('body')[0].appendChild(dom);
    }

    self.id = requestAnimationFrame(function () {
        now = Date.now();

        if (now - before >= 1000) {
            before = now;
            show(fps);
            fps = 0;
        } else {
            fps += 1;
        }

        self.id = requestAnimationFrame(arguments.callee);
    });

    self.stop = function () {
        cancelAnimationFrame(self.id);
    };
}


/* 使用测试*/
var a = new ShowFPS();

//a.stop();
```

### *原生JS*获取星座
```javascript
/**
 * 获取星座
 * @param {String|Number} birthday - 年月日（8位，如'19900220'或19900220） 或 空字符串
 * @returns {String} constellation - 星座 或 空字符串
 */
function getConstellation (birthday) {
  birthday = birthday.toString()

  var constellation = ''

  if (birthday && birthday.length === 8) {
    var month = birthday.slice(4, 6)
    var day = birthday.slice(6, 8)
    var conStr = '魔羯水瓶双鱼白羊金牛双子巨蟹狮子处女天秤天蝎射手魔羯'
    var dayArr = [20, 19, 21, 20, 21, 22, 23, 23, 23, 24, 23, 22]

    constellation = conStr.substr(month * 2 - (day < dayArr[month - 1] ? 2 : 0), 2)

    if (constellation) {
      constellation += '座'
    }
  }

  return constellation
}
```

---
## Polyfill

### *原生JS*`requestAnimationFrame`和`cancelAnimationFrame`的Polyfill
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

### *原生JS*`Date.now`的Polyfill
```javascript
if (typeof Date.now !== 'function') {
    Date.now = function () {
        return new Date().getTime();
    };
}
```
>`Date.now()`相对于`new Date().getTime()`及其他方式，可以避免生成不必要的`Date`对象，更高效。

### *原生JS*`Object.create`的Polyfill
```javascript
if (typeof Object.create !== 'function') {
    Object.create = (function () {
        function Temp() {}

        var hasOwn = Object.prototype.hasOwnProperty;

        return function (O) {
            if (typeof O != 'object') {
                throw TypeError('Object prototype may only be an Object or null');
            }

            Temp.prototype = O;
            var obj = new Temp();
            Temp.prototype = null; // 不要保持一个 O 的杂散引用（a stray reference）...

            if (arguments.length > 1) {
                var Properties = Object(arguments[1]);

                for (var prop in Properties) {
                    if (hasOwn.call(Properties, prop)) {
                        obj[prop] = Properties[prop];
                    }
                }
            }

            return obj;
        };
    })();
}
```
>来自[MDN:Object.create](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Object/create#Polyfill)。

### *原生JS*`Array.isArray`的Polyfill
```javascript
if (!Array.isArray) {
    Array.isArray = function (arg) {
        return Object.prototype.toString.call(arg) === '[object Array]';
    };
}
```
>来自[MDN:Array.isArray](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/isArray#Polyfill)。

### *原生JS*`Array.prototype.map`的Polyfill
```javascript
if (!Array.prototype.map) {
    Array.prototype.map = function (callback, thisArg) {
        var T, A, k;

        if (this == null) {
            throw new TypeError(' this is null or not defined');
        }

        var O = Object(this);

        var len = O.length >>> 0;

        if (Object.prototype.toString.call(callback) != '[object Function]') {
            throw new TypeError(callback + ' is not a function');
        }

        if (thisArg) {
            T = thisArg;
        }

        A = new Array(len);

        k = 0;

        while (k < len) {
            var kValue, mappedValue;

            if (k in O) {

                kValue = O[k];

                mappedValue = callback.call(T, kValue, k, O);

                A[k] = mappedValue;
            }

            k += 1;
        }

        return A;
    };
}
```
>来自[MDN:Array.prototype.map](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/map#Compatibility)。

### *原生JS*`Function.prototype.bind`的Polyfill
```javascript
if (!Function.prototype.bind) {
    Function.prototype.bind = function (oThis) {
        if (typeof this !== 'function') {
            throw new TypeError('Function.prototype.bind - what is trying to be bound is not callable');
        }

        var aArgs = Array.prototype.slice.call(arguments, 1),
            fToBind = this,
            fNOP = function () {
            },
            fBound = function () {
                return fToBind.apply(this instanceof fNOP
                        ? this
                        : oThis || this,
                    aArgs.concat(Array.prototype.slice.call(arguments)));
            };

        fNOP.prototype = this.prototype;
        fBound.prototype = new fNOP();

        return fBound;
    };
}
```
>来自[MDN:Function.prototype.bind](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Function/bind#Compatibility)。

### *原生JS*`String.prototype.trim`的Polyfill
```javascript
if (!String.prototype.trim) {
    String.prototype.trim = function () {
        return this.replace(/^[\s\uFEFF\xA0]+|[\s\uFEFF\xA0]+$/g, '');
    };
}
```
>来自[MDN:String.prototype.trim](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/String/Trim#兼容旧环境)。

---
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

                next = parseInt(next, 10);

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

                next = parseInt(next, 10);

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

>Zepto默认没有`deferred`的对象、没有`outerHeight`方法。

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

>滚动事件代理可以代理在要`window`或监控图片加载的滚动节点上。

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
                max-width: rem(460);    /*box-sizing: border-box;*/
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
<div id="j-form">
  <label for="all">
    <input id="all" type="checkbox" name="all">
    全选
  </label>

  <br>

  <label for="1">
    <input id="1" type="checkbox" name="ones" value="1">
    1
  </label>
  <label for="2">
    <input id="2" type="checkbox" name="ones" value="2">
    2
  </label>
  <label for="3">
    <input id="3" type="checkbox" name="ones" value="3">
    3
  </label>
  <label for="a">
    <input id="a" type="checkbox" name="ones" value="a">
    a
  </label>
  <label for="b">
    <input id="b" type="checkbox" name="ones" value="b">
    b
  </label>
</div>

<a href="#" id="j-submit">提交</a>

<script>
  var $allInput = $('#j-form').find('[name="all"]')
  var $oneInput = $('#j-form').find('[name="ones"]')

  $allInput.on('click', function () {
    $oneInput.prop('checked', this.checked)
  })

  $oneInput.on('click', function () {
    var flag = true

    $oneInput.each(function () {
      if (!this.checked) {
        flag = false

        return false
      }
    })

    $allInput.prop('checked', flag)
  })

  // 提交
  $('#j-submit').on('click', function () {
    var arr = []

    $('#j-form').find('[name="ones"]').each(function (index, item) {
      if (item.checked) {
        arr.push($(item).val())
      }
    })

    var data = arr.join(',')

    console.log(data)
  })
</script>
```

### jQuery或Zepto节点跟随屏幕滚动
1. `fixed`：

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
2. `margin-top`：

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
                targetMarginTop = parseInt($target.css('margin-top'), 10) || 0,
                prevMarginBottom = parseInt($target.prev().css('margin-bottom'), 10) || 0,
                defaultMarginTop = Math.max(targetMarginTop, prevMarginBottom),
                maxMarginTop = $(dependent).height() - $(father).height() + defaultMarginTop; //Query可以用outerHeight

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
>如果对不是全屏的节点使用翻转函数，需要给节点设置：`width: 宽度 !important;height: auto !important;`。

### jQuery或Zepto点击指定区域以外执行函数
1. jQuery

    ```javascript
    /**
     * 点击指定区域以外执行函数（一次性）
     * @param {Object} $dom - jQuery节点
     * @param {Function} callback - 回调函数
     * @param {Number} [limit] - 自动失效时间，若没有传或传0则不会自动失效
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

        var _isStop = false, //停止动画flag
            _namespace = Date.now(), //事件命名空间
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