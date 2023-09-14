# JS废弃代码

## 目录
1. [原生JS方法](#原生js方法)

    1. 可用[moment](https://github.com/moment/moment/)（或[dayjs](https://github.com/iamkun/dayjs)、[date-fns](https://github.com/date-fns/date-fns)）代替

        1. [格式化日期](#原生js格式化日期)
        1. [获取年龄](#原生js获取年龄)
        1. [倒计时显示](#原生js倒计时显示)
        1. [倒计时组件](#vuereact倒计时组件)
    1. 可用[lodash](https://github.com/lodash/lodash)、[jQuery](https://github.com/jquery/jquery)或ES6或其他库代替

        1. [多异步返回后才执行总回调函数（利用jQuery的`$.ajax`）](#原生js多异步返回后才执行总回调函数利用jquery的ajax)
        1. [对象合二为一（改变第一个参数）](#原生js对象合二为一改变第一个参数)
        1. [通过类名获取DOM](#原生js通过类名获取dom)
    1. 可用[js-cookie](https://github.com/js-cookie/js-cookie)代替

        1. [操作cookie](#原生js操作cookie)
    1. 可用js原生代替

        1. [实现类似jQuery的`$('html,body').animate({'scrollLeft': 像素, 'scrollTop': 像素}, 毫秒);`](#原生js实现类似jquery的htmlbodyanimatescrollleft-像素-scrolltop-像素-毫秒)
1. [函数模板](#函数模板)
1. <details>

    <summary><a href="#polyfill">Polyfill</a></summary>

    1. [`requestAnimationFrame`和`cancelAnimationFrame`](#原生jsrequestanimationframe和cancelanimationframe的polyfill)
    1. [`Date.now`](#原生jsdatenow的polyfill)
    1. [`Array.isArray`](#原生jsarrayisarray的polyfill)
    1. [`Array.prototype.map`](#原生jsarrayprototypemap的polyfill)
    1. [`Function.prototype.bind`](#原生jsfunctionprototypebind的polyfill)
    1. [`String.prototype.trim`](#原生jsstringprototypetrim的polyfill)
    1. [`String.prototype.repeat`](#原生jsstringprototyperepeat的polyfill)
    1. [`Number.isNaN`](#原生jsnumberisnan的polyfill)
    1. [`Number.isFinite`](#原生jsnumberisfinite的polyfill)
    1. [`Number.isInteger`](#原生jsnumberisinteger的polyfill)
    1. [`Number.isSafeInteger`](#原生jsnumberissafeinteger的polyfill)
    </details>

---

## 原生JS方法

### *原生JS*格式化日期
```typescript
// 时间戳 -> yyyy.MM.dd
export function formatTimestamp(timestamp: number | string): string {
  const date = new Date(timestamp);
  const month = date.getMonth() + 1;
  const day = date.getDate();
  return `${date.getFullYear()}.${month >= 10 ? month : `0${month}`}.${day >= 10 ? day : `0${day}`}`;
}


/* 使用测试 */
formatTimestamp(new Date("2020/09/09").getTime())
```

```javascript
var format = {
  date: function (dateObj, fmt) {    /* 格式化日期 */
    var o = {
        'q+': Math.floor((dateObj.getMonth() + 3) / 3), // 季度
        'M+': dateObj.getMonth() + 1, // 月
        'd+': dateObj.getDate(), // 日
        'h+': dateObj.getHours() % 12 === 0 ? 12 : dateObj.getHours() % 12, // 12小时制
        'H+': dateObj.getHours(), // 24小时制
        'm+': dateObj.getMinutes(), // 分
        's+': dateObj.getSeconds(), // 秒
        'S': dateObj.getMilliseconds(), // 毫秒
      },
      week = {
        '0': '日',
        '1': '一',
        '2': '二',
        '3': '三',
        '4': '四',
        '5': '五',
        '6': '六',
      },
      i;

    /* [{y:'7'},{yy:'17'},{yyy+:'017'},{yyyy+:'2017'}] */
    if (/(y+)/.test(fmt)) {
      fmt = fmt.replace(RegExp.$1, (dateObj.getFullYear() + '').substring(4 - RegExp.$1.length));
    }
    /* [{E:'一'},{EE:'周一'},{EEE+:'星期一'}] */
    if (/(E+)/.test(fmt)) {
      fmt = fmt.replace(RegExp.$1, ((RegExp.$1.length > 1) ? (RegExp.$1.length > 2 ? '星期' : '周') : '') + week[dateObj.getDay() + '']);
    }
    for (i in o) {
      if (new RegExp('(' + i + ')').test(fmt)) {
        fmt = fmt.replace(RegExp.$1, (RegExp.$1.length === 1) ? (o[i]) : (('00' + o[i]).substr(('' + o[i]).length)));
      }
    }

    return fmt;
  },
};


/* 使用测试 */
var a = format.date(new Date(), 'yyyy-MM-dd HH:mm:ss S毫秒 EEE 季度q');
```
>可以使用[moment](https://github.com/moment/moment/)（或[dayjs](https://github.com/iamkun/dayjs)、[date-fns](https://github.com/date-fns/date-fns)）格式化时间，完全替代。

### *原生JS*获取年龄
```javascript
/**
 * 获取年龄
 * @param {String|Number} birthday - 年月日（8位，如：'19900220'或19900220） 或 空字符串
 * @returns {String} age - 年龄 或 空字符串
 */
function getAge (birthday) {
  birthday = birthday.toString()

  var age = 0

  if (birthday && birthday.length === 8) {
    var now = new Date()
    var nowYear = now.getFullYear()
    var nowMonth = now.getMonth() + 1
    var nowDay = now.getDate()

    if (nowMonth < 10) {
      nowMonth = '0' + nowMonth
    }
    if (nowDay < 10) {
      nowDay = '0' + nowDay
    }

    age = Math.floor((parseInt('' + nowYear + nowMonth + nowDay, 10) - parseInt(birthday, 10)) / 10000)
  }

  if (age > 0) {
    age = age.toString()
  } else {
    age = ''
  }

  return age
}
```
>可以使用[moment](https://github.com/moment/moment/)（或[dayjs](https://github.com/iamkun/dayjs)、[date-fns](https://github.com/date-fns/date-fns)）格式化时间，完全替代。

### *原生JS*倒计时显示
1. 统一输出

    ```javascript
    /**
     * 显示倒计时，统一输出
     * @constructor
     * @param {Object} data
     * @param {Number} data.deadline - 到期的时间戳
     * @param {Object} [data.dom] - 输出节点，若不是节点则console.log输出
     * @param {Function} [data.callback] - 到点后的回调函数
     * @param {Number} [data.leftSec = 0] - 提前到期的秒数
     * @param {Boolean} [data.completeZero = false] - 是否个位数补全0
     * @param {String} [data.dType = ' '] - 「天」后面的文字
     * @param {String} [data.hType = ' '] - 「时」后面的文字
     * @param {String} [data.mType = ' '] - 「分」后面的文字
     * @param {String} [data.sType = ' '] - 「秒」后面的文字
     */
    function CountDown (data) {
      const _dTypeSend = (typeof data.dType !== 'undefined') && data.dType !== ''
      const _hTypeSend = (typeof data.hType !== 'undefined') && data.hType !== ''
      const _mTypeSend = (typeof data.mType !== 'undefined') && data.mType !== ''
      const _sTypeSend = (typeof data.sType !== 'undefined') && data.sType !== ''
      const _isElement = ((o) => {  /* 是否为Element */
        return typeof HTMLElement === 'object' ? o instanceof HTMLElement : !!o && typeof o === 'object' && o !== null && o.nodeType === 1 && typeof o.nodeName === 'string'
      })(data.dom)

      const _formatNum = (number) => {    /* 格式化数字格式 */
        if (number < 10 && data.completeZero) {
          return '0' + number
        } else {
          return number.toString()
        }
      }

      const _SetInterval = function (func, millisecond) {  /* 周期执行 */
        let _setIntervalId

        if (typeof func === 'function') {
          _setIntervalId = setTimeout(function self () {
            _setIntervalId = setTimeout(self, millisecond)

            func()
          }, millisecond)
        }

        this.stop = () => {
          clearTimeout(_setIntervalId)
        }
      }

      const _print = (time) => {  /* 输出 */
        const day = _formatNum(Math.floor((time / (24 * 60 * 60))))
        const hour = _formatNum(Math.floor((time / (60 * 60)) % 24))
        const minute = _formatNum(Math.floor((time / 60) % 60))
        const second = _formatNum(time % 60)
        let text

        if (day != 0 || _dTypeSend) {
          text = day + data.dType + hour + data.hType + minute + data.mType + second + data.sType
        } else if (hour != 0 || _hTypeSend) {
          text = hour + data.hType + minute + data.mType + second + data.sType
        } else if (minute != 0 || _mTypeSend) {
          text = minute + data.mType + second + data.sType
        } else {
          text = second + data.sType
        }

        if (_isElement) {
          data.dom.innerHTML = text
        } else {
          console.log(text)
        }
      }

      if (!_dTypeSend) {
        data.dType = ' '
      }
      if (!_hTypeSend) {
        data.hType = ' '
      }
      if (!_mTypeSend) {
        data.mType = ' '
      }
      if (!_sTypeSend) {
        data.sType = ''
      }

      /* 初始化时就输出一遍 */
      _print(Math.round((data.deadline - Date.now()) / 1000))

      const obj = new _SetInterval(() => {
        const time = Math.round((data.deadline - Date.now()) / 1000)

        if (time < (data.leftSec || 0)) {
          obj.stop()
          if (typeof data.callback === 'function') {
            data.callback()
          }
          return
        }

        _print(time)
      }, 1000)

      this.stop = obj.stop
    }


    /* 使用测试 */
    var a = new CountDown({
      deadline: Date.now() + 10000,
      dom: document.getElementById('j-test'),
      callback: () => {
        console.log('完成')
      },
      leftSec: 1,
      completeZero: false,
      dType: '',
      hType: '小时',
      mType: '分',
      sType: '秒'
    })

    // a.stop();
    ```
2. 分开输出

    ```javascript
    /**
     * 显示倒计时，单独输出每一个位数（秒个位、秒十位、分个位、分十位、时个位、时十位、天）
     * @constructor
     * @param {Number} deadline - 到期的时间戳
     * @param {Function} [callback] - 到点后的回调函数
     * @param {Array} [DOMList] - 展示的DOM集合，前7个项有效（若存在，则从最小的时间开始展示；若不存在，则console.log）
     */
    function CountDown ({ deadline, callback = () => {}, DOMList = [] } = {}) {
      /* 周期执行 */
      const SetInterval = function (func, millisecond) {
        let setIntervalId

        if (typeof func === 'function') {
          setIntervalId = setTimeout(function self () {
            setIntervalId = setTimeout(self, millisecond)

            func()
          }, millisecond)
        }

        this.stop = () => {
          clearTimeout(setIntervalId)
        }
      }

      /* 秒数 -> 天、时、分、秒 */
      const formatSeconds = (seconds) => {
        const secondArr = (seconds % 60).toString().split('')
        const secondObj = {
          second0: secondArr.pop(), // 秒的个位数
          second00: secondArr.pop() || '0'  // 秒的十位数
        }

        const minuteArr = (Math.floor(seconds / 60) % 60).toString().split('')
        const minuteObj = {
          minute0: minuteArr.pop(), // 分的个位数
          minute00: minuteArr.pop() || '0'  // 分的十位数
        }

        const hourArr = (Math.floor(seconds / 3600) % 24).toString().split('')
        const hourObj = {
          hour0: hourArr.pop(), // 时的个位数
          hour00: hourArr.pop() || '0'  // 时的十位数
        }

        const dayObj = {
          day: (Math.floor(seconds / (3600 * 24))).toString() // 天的所有
        }

        return { ...secondObj, ...minuteObj, ...hourObj, ...dayObj }
      }

      const timeMapDom = [ // 映射 DOM和时间 的顺序
        'second0',  // 第一个DOM -> 'second0'
        'second00',
        'minute0',
        'minute00',
        'hour0',
        'hour00',
        'day'
      ]

      /* 输出 */
      const print = (time) => {
        const timeObj = formatSeconds(time)

        if (DOMList.length > 0) {
          DOMList.map((value, index) => { // 仅输出有给DOM展示的内容，多余的时间丢弃
            requestAnimationFrame(() => {
              value.innerText = timeObj[timeMapDom[index]]
            })
          })
        } else {
          console.log(timeObj)
        }
      }

      // 初始化时就输出一遍
      print(Math.round((deadline - Date.now()) / 1000))

      // 每秒输出一遍
      const obj = new SetInterval(() => {
        const time = Math.round((deadline - Date.now()) / 1000)

        if (time < 0) {
          obj.stop()
          if (typeof callback === 'function') {
            callback()
          }
        } else {
          print(time)
        }
      }, 1000)

      this.stop = obj.stop
    }


    /* 使用测试 */
    var a = new CountDown({
      deadline: Date.now() + 10000,
      callback: function () {
        console.log('完成')
      },
      DOMList: [
        document.getElementById('j-7'),
        document.getElementById('j-6'),
        document.getElementById('j-5'),
        document.getElementById('j-4'),
        document.getElementById('j-3'),
        document.getElementById('j-2'),
        document.getElementById('j-1')
      ].slice(0, Math.floor(Math.random() * 8))  // 0~7
    })

    // a.stop();
    ```
>可以使用[moment](https://github.com/moment/moment/)（或[dayjs](https://github.com/iamkun/dayjs)、[date-fns](https://github.com/date-fns/date-fns)）格式化时间，完全替代。

### *vue/react*倒计时组件
1. vue

    [vue-timer-countdown](https://github.com/realgeoffrey/vue-timer-countdown)
2. react

    [react-time-countdown](https://github.com/realgeoffrey/react-time-countdown)

### *原生JS*多异步返回后才执行总回调函数（利用jQuery的`$.ajax`）
```javascript
/**
 * 异步函数都成功返回后，执行func
 * @param {Function} func
 * @param {...String} url - AJAX请求的地址
 */
function multiCallback(func, url) {
    if (typeof func === 'function' && arguments.length >= 2) {
        var urlLength = arguments.length - 1,
            handle = function () {
                var self = arguments.callee;

                if (self.count === urlLength) {
                    func.call(undefined, self.result);
                }
            };

        handle.count = 0;
        handle.result = {};

        for (var i = 1; i <= urlLength; i++) {
            (function (url) {
                $.ajax({
                    url: url,
                    dataType: 'json',
                    data: {}
                    /*,
                     // Zepto默认：没有deferred的对象，用参数模式代替
                     success: function (data) {
                         handle.result[url] = data;
                         handle.count += 1;
                         handle();
                     }
                    */
                }).done(function (data) {
                    handle.result[url] = data;
                    handle.count += 1;
                    handle();
                });
            }(arguments[i]));
        }
    } else {

        return false;
    }
}
```
>1. 可以使用`Promise.all`或`async-await`方法实现。
>2. 可以使用jQuery的Deferred对象`$.when($.ajax()...).done(成功后方法)`，完全替代。

### *原生JS*对象合二为一（改变第一个参数）
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
>1. 可以使用lodash的`_.assign(object, [sources])`（浅复制）、`_.merge(object, [sources])`（深复制），完全替代。
>2. 可以使用[deepmerge](https://github.com/KyleAMathews/deepmerge)，完全替代。
>3. 可以使用jQuery的`$.extend(对象1, 对象2)`，完全替代。

### *原生JS*通过类名获取DOM
```javascript
/**
 * 通过类名获取一组元素
 * @param {String} className - 类名
 * @param {Object} [parentDom = document] - 父级DOM
 * @returns {Array} - 类名匹配的DOM数组
 */
function getElementsByClassName(className, parentDom) {
    parentDom = parentDom || document;

    className = className.replace(/(^\s+)|(\s+$)/g, ''); // 去除前后空格

    if (document.getElementsByClassName) {  /* ie9+ */

        return parentDom.getElementsByClassName(className);
    } else if (document.querySelectorAll) { /* ie8+ */

        className = '.' + className.split(/\s+/).join('.');

        return parentDom.querySelectorAll(className);
    } else {
        var doms = parentDom.getElementsByTagName('*'),
            nameArr = className.split(/\s+/),
            nameLen = nameArr.length,
            domArr = [],
            i, len, j, regex;

        for (i = 0, len = doms.length; i < len; i++) {  /* 遍历所有标签 */
            for (j = 0; j < nameLen; j++) { /* 遍历类名 */
                regex = new RegExp('\\b' + nameArr[j] + '\\b');

                if (!regex.test(doms[i].className)) {
                    break;
                }
            }

            if (j >= nameLen) {
                domArr.push(doms[i]);
            }
        }

        return domArr;
    }
}
```
>可以使用jQuery的`$('.类名')`，完全替代。

### *原生JS*操作cookie
>参考：[MDN:cookie](https://developer.mozilla.org/zh-CN/docs/Web/API/Document/cookie#一个小框架：一个完整支持unicode的cookie读取写入器)。

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
     * @param {Number|Date|String|Infinity} [deadline] - 过期时间。默认：关闭浏览器后过期
     * @param {String} [path] - 路径。默认：当前文档位置的路径
     * @param {String} [domain] - 域名。默认：当前文档位置的路径的域名部分
     * @param {Boolean} [secure] - 是否「仅通过https协议传输」。默认：否
     * @param {String} [samesite] - SameSite，取值：Strict、Lax。默认：无
     * @param {String} [priority] - 优先级，取值；Low、Medium、High。默认：Medium
     * @returns {Boolean} - 操作成功或失败
     */
    setItem: function (key, value, deadline, path, domain, secure, samesite, priority) {
      if (!key || (window.location.protocol === 'http:' && secure)) {   // todo: 更多设置cookie失败的情况

        return false;
      } else {
        var expires = "";

        if (deadline) {
          switch (deadline.constructor) {
            case Number:
              expires = deadline === Infinity ? "; expires=Fri, 31 Dec 9999 23:59:59 GMT" : "; max-age=" + deadline;
              break;
            case String:
              expires = "; expires=" + deadline;
              break;
            case Date:
              expires = "; expires=" + deadline.toUTCString();
              break;
          }
        }

        document.cookie = encodeURIComponent(key) + "=" + encodeURIComponent(value) + expires + (domain ? "; domain=" + domain : "") + (path ? "; path=" + path : "") + (secure ? "; secure" : "") + (samesite ? "; samesite=" + samesite : "") + (priority ? "; priority=" + priority : "");

        return true;
      }
    },

    /**
     * 删除一个cookie
     * @param {String} key - 名
     * @param {String} [path] - 路径。默认：当前文档位置的路径
     * @param {String} [domain] - 域名。默认：当前文档位置的路径的域名部分
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
>可以使用[js-cookie](https://github.com/js-cookie/js-cookie)，完全替代。

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
>1. 使用[velocity动画库](https://github.com/julianshapiro/velocity)（[中文文档](http://www.mrfront.com/docs/velocity.js/)）做所有的动画（包括JS和CSS）才是最简单且性能最佳的选择。
>
>    如：滚动到某位置`$('html').velocity('scroll', {offset: y轴像素, duration: 毫秒});`。
>2. 原生js已支持：支持顺滑滚动，但不支持设定滚动时间
>
>    1. `window.scroll/scrollTo(横轴坐标, 纵轴坐标)` 或 `window.scroll/scrollTo({ left: 横轴坐标, top: 纵轴坐标, behavior: 'smooth'或'auto' })`
>    2. `window.scrollBy(相对横轴坐标, 相对纵轴坐标)` 或 `window.scrollBy({ left: 相对横轴坐标, top: 相对纵轴坐标, behavior: 'smooth'或'auto' })`

---
### 函数模板
1. 构造函数

    1. 普通版：

        ```javascript
        var OneConstructor = function () {
            /* 私有的内容 */
            var _para = {a: '私有的变量_para'},
                _func = function () {
                    console.log('私有的业务逻辑_func', _para);
                },
                _bindEvent = function () {  /* 绑定事件 */

                },
                _init = function () {   /* 初始化 */
                    _func();
                    _bindEvent();
                };

            _init();

            for (var _arr = [], _i = 0; _i < arguments.length; _i++) {
                _arr.push(arguments[_i]);
            }

            /* 公开的内容 */
            this.para = _arr;
            this.para_1 = {b: '公开的变量para_1（每个实例不共享）'};
            this.func_1 = function () {
                console.log('公开的业务逻辑func_1（每个实例不共享）');
            };
        };
        ```
    2. 修改构造函数的原型对象（所有实例都共享）：

        ```javascript
        var OneConstructor = (function () {
            /* 私有的内容 */
            var _para = {a: '私有的变量_para'},
                _func = function () {
                    console.log('私有的业务逻辑_func', _para);
                },
                _bindEvent = function () {  /* 绑定事件 */

                },
                _init = function () {   /* 初始化 */
                    _func();
                    _bindEvent();
                };

            function Constructor() {
                _init();

                for (var _arr = [], _i = 0; _i < arguments.length; _i++) {
                    _arr.push(arguments[_i]);
                }

                /* 公开的内容 */
                this.para = _arr;
                this.para_1 = {b: '公开的变量para_1（每个实例不共享）'};
                this.func_1 = function () {
                    console.log('公开的业务逻辑func_1（每个实例不共享）');
                };
            }

            /* 构造函数的原型对象上，每个实例共享 */
            Constructor.prototype = {
                para_2: {c: '公开的变量para_2（每个实例共享）'},
                func_2: function () {
                    console.log('公开的业务逻辑func_2（每个实例共享）');
                }
            };

            /* 原型对象添加constructor属性 */
            if (typeof Object.defineProperty === 'function') {

                /* 使属性：不可以改变描述符、不可以删除、不可以枚举、不可以被赋值运算符改变 */
                Object.defineProperty(Constructor.prototype, 'constructor', {
                    value: Constructor
                });
            } else {
                Constructor.prototype.constructor = Constructor;
            }

            return Constructor;
        }());
        ```
2. 模块模式（单例模式+私有变量和特权方法）

    ```javascript
    var singletonObj = (function () {
        /* 私有变量和私有方法，无法直接访问，只能由return的对象字面量访问 */
        var _para = {a: '私有变量'},
            _func = function () {
                console.log('私有方法');
            };

        /* 单例模式，可以访问私有内容 */
        return {
            get: function () {  /* 特权方法 */
                _func();

                return _para;
            },
            set: function (para) {  /* 特权方法 */
                _func();

                _para = para;
            },
            para: {b: '公开对象'},
            func: function () {
                console.log('公开方法');
            }
        }
    }());
    ```
    >单例模式：
    >```javascript
    >var singletonObj = {
    >   para: {},
    >   func: function () {}
    >};
    >```

---
## Polyfill

### *原生JS*`requestAnimationFrame`和`cancelAnimationFrame`的Polyfill
>来自：[rAF.js](https://gist.github.com/paulirish/1579671)。

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

### *原生JS*`Date.now`的Polyfill
```javascript
if (typeof Date.now !== 'function') {
    Date.now = function () {
        return new Date().getTime();
    };
}
```
>`Date.now()`相对于`new Date().getTime()`及其他方式，可以避免生成不必要的`Date`对象，更高效。

### *原生JS*`Array.isArray`的Polyfill
>来自：[MDN:Array.isArray](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/isArray#Polyfill)。

```javascript
if (!Array.isArray) {
    Array.isArray = function (arg) {
        return Object.prototype.toString.call(arg) === '[object Array]';
    };
}
```

### *原生JS*`Array.prototype.map`的Polyfill
>来自：[MDN:Array.prototype.map](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/map#Compatibility)。

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

### *原生JS*`Function.prototype.bind`的Polyfill
>来自：[MDN:Function.prototype.bind](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Function/bind#Compatibility)。

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

### *原生JS*`String.prototype.trim`的Polyfill
>来自：[MDN:String.prototype.trim](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/String/Trim#兼容旧环境)。

```javascript
if (!String.prototype.trim) {
    String.prototype.trim = function () {
        return this.replace(/^[\s\uFEFF\xA0]+|[\s\uFEFF\xA0]+$/g, '');
    };
}
```

### *原生JS*`String.prototype.repeat`的Polyfill
>来自：[MDN:String.prototype.repeat](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/String/repeat#填充)。

```javascript
if (!String.prototype.repeat) {
  String.prototype.repeat = function (count) {
    'use strict';
    if (this == null) {
      throw new TypeError('can\'t convert ' + this + ' to object');
    }
    var str = '' + this;
    count = +count;
    if (count != count) {
      count = 0;
    }
    if (count < 0) {
      throw new RangeError('repeat count must be non-negative');
    }
    if (count == Infinity) {
      throw new RangeError('repeat count must be less than infinity');
    }
    count = Math.floor(count);
    if (str.length == 0 || count == 0) {
      return '';
    }
    // 确保 count 是一个 31 位的整数。这样我们就可以使用如下优化的算法。
    // 当前（2014年8月），绝大多数浏览器都不能支持 1 << 28 长的字符串，所以：
    if (str.length * count >= 1 << 28) {
      throw new RangeError('repeat count must not overflow maximum string size');
    }
    var rpt = '';
    for (; ;) {
      if ((count & 1) == 1) {
        rpt += str;
      }
      count >>>= 1;
      if (count == 0) {
        break;
      }
      str += str;
    }
    return rpt;
  };
}
```

### *原生JS*`Number.isNaN`的Polyfill
>来自：[MDN:Number.isNaN](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Number/isNaN#Polyfill)。

```javascript
Number.isNaN = Number.isNaN || function (value) {
  return typeof value === 'number' && isNaN(value);
};
```

### *原生JS*`Number.isFinite`的Polyfill
>来自：[MDN:Number.isFinite](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Number/isFinite#Polyfill)。

```javascript
Number.isFinite = Number.isFinite || function (value) {
  return typeof value === 'number' && isFinite(value);
};
```

### *原生JS*`Number.isInteger`的Polyfill
>来自：[MDN:Number.isInteger](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Number/isInteger#Polyfill)。

```javascript
Number.isInteger = Number.isInteger || function (value) {
  return typeof value === 'number' && isFinite(value) && Math.floor(value) === value;
};
```

### *原生JS*`Number.isSafeInteger`的Polyfill
>来自：[MDN:Number.isSafeInteger](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Number/isSafeInteger#Polyfill)。

```javascript
Number.isSafeInteger = Number.isSafeInteger || function (value) {
  return Number.isInteger(value) && Math.abs(value) <= Number.MAX_SAFE_INTEGER;
};
```
