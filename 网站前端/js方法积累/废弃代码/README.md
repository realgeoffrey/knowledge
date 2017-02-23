# 废弃代码

明显已经不会再使用，但是不忍心删除的代码……

### *原生js*多异步返回后才执行总回调函数（利用jQuery或Zepto的`$.ajax`）
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
                    //Zepto没有deferred的对象，用参数模式代替
                    success: function (data) {
                        handle.result[url] = data;
                        handle.count++;
                        handle();
                    }*/
                }).done(function (data) {
                    handle.result[url] = data;
                    handle.count++;
                    handle();
                });
            }(arguments[i]));
        }
    } else {
        return false;
    }
}
```
>可以使用jQuery的`$.when`完全替代。