# JS方法积累——废弃代码

### *原生JS*格式化日期
```javascript
var format = {
  date: function (dateObj, fmt) {    /* 格式化日期*/
    var o = {
        'q+': Math.floor((dateObj.getMonth() + 3) / 3), //季度
        'M+': dateObj.getMonth() + 1, //月
        'd+': dateObj.getDate(), //日
        'h+': dateObj.getHours() % 12 === 0 ? 12 : dateObj.getHours() % 12, //12小时制
        'H+': dateObj.getHours(), //24小时制
        'm+': dateObj.getMinutes(), //分
        's+': dateObj.getSeconds(), //秒
        'S': dateObj.getMilliseconds(), //毫秒
      },
      week = {
        '0': '一',
        '1': '二',
        '2': '三',
        '3': '四',
        '4': '五',
        '5': '六',
        '6': '日',
      },
      i;

    /* [{y:'7'},{yy:'17'},{yyy+:'017'},{yyyy+:'2017'}]*/
    if (/(y+)/.test(fmt)) {
      fmt = fmt.replace(RegExp.$1, (dateObj.getFullYear() + '').substring(4 - RegExp.$1.length));
    }
    /* [{E:'一'},{EE:'周一'},{EEE+:'星期一'}]*/
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


/* 使用测试*/
var a = format.date(new Date(), 'yyyy-MM-dd HH:mm:ss S毫秒 EEE 季度q');
```
>可以使用[moment](https://github.com/moment/moment/)格式化时间，完全替代。

### *原生JS*获取年龄
```javascript
/**
 * 获取年龄
 * @param {String|Number} birthday - 年月日（8位，如'19900220'或19900220） 或 空字符串
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
>可以使用[moment](https://github.com/moment/moment/)格式化时间，完全替代。

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
>可以使用[moment](https://github.com/moment/moment/)格式化时间。

### *原生JS*多异步返回后才执行总回调函数（利用jQuery或Zepto的`$.ajax`）
```javascript
/**
 * 异步函数都成功返回后，执行func
 * @param {Function} func
 * @param {...String} url - ajax请求的地址
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
                     //Zepto默认没有deferred的对象，用参数模式代替
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
>1. 可以使用Promise对象实现。
>2. 可以使用jQuery的Deferred对象`$.when($.ajax()...).done(成功后方法)`完全替代。

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
>可以使用jQuery的`$.extend(对象1, 对象2)`完全替代。

### *原生JS*深复制
```javascript
/**
 * 深复制，仅针对数组或对象，值可以是基本数据类型、数组、基本对象、方法（不复制方法内属性）
 * @param {Object|Array} obj - 被深复制的内容
 * @returns {Object|Array} - 深复制后的内容
 */
function deepCopy(obj) {
    var newObj, i;

    if (typeof obj !== 'object' || obj === null) {

        return obj;
    } else {
        newObj = Object.prototype.toString.call(obj) === '[object Array]' ? [] : {};

        for (i in obj) {
            newObj[i] = arguments.callee(obj[i]);
        }

        return newObj;
    }
}
```
>1. 可以使用jQuery的`$.extend(true, {}, 被复制对象)`完全替代。
>2. 可以使用lodash的`_.cloneDeep(被复制对象)`完全替代。

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

    className = className.replace(/(^\s+)|(\s+$)/g, ''); //去除前后空格

    if (document.getElementsByClassName) {  /* ie9+*/

        return parentDom.getElementsByClassName(className);
    } else if (document.querySelectorAll) { /* ie8+*/

        className = '.' + className.split(/\s+/).join('.');

        return parentDom.querySelectorAll(className);
    } else {
        var doms = parentDom.getElementsByTagName('*'),
            nameArr = className.split(/\s+/),
            nameLen = nameArr.length,
            domArr = [],
            i, len, j, regex;

        for (i = 0, len = doms.length; i < len; i++) {  /* 遍历所有标签*/
            for (j = 0; j < nameLen; j++) { /* 遍历类名*/
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
>可以使用jQuery的`$('.类名')`完全替代。