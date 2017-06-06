# JS方法积累——废弃代码

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
>可以使用jQuery的`$.when($.ajax()...).done(成功后方法)`完全替代。

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