# JS实用方法

## 目录
1. [原生JS方法](#原生js方法)

    1. 根据UA判断

        1. [判断所在系统](#原生js判断所在系统)
        1. [判断移动平台](#原生js判断移动平台)
        1. [判断ie6、7、8、9版本](#原生js判断ie6789版本)
        1. [判断ie所有版本](#原生js判断ie所有版本)
    1. `键-值`操作

        1. [判断是否存在某cookie](#原生js判断是否存在某cookie)
        1. [获取URL相关信息](#原生js获取url相关信息)
        1. [在URL末尾添加查询键-值](#原生js在url末尾添加查询键-值)
    1. 事件相关

        1. [绑定、解绑事件](#原生js绑定解绑事件)
        1. [阻止冒泡和阻止浏览器默认行为](#原生jsjquery阻止冒泡和阻止浏览器默认行为)
        1. [事件代理](#原生js事件代理)
        1. [实现判断按下具体某按键](#原生jsjquery实现判断按下具体某按键)
        1. [拖拽和放下](#原生js拖拽和放下)
        1. [触摸屏模拟点击事件（消除「延时300毫秒后才触发click事件」，使点击事件提前触发）](#原生js触摸屏模拟点击事件消除延时300毫秒后才触发click事件使点击事件提前触发)
        1. [判断事件在浏览器是否存在](#原生js判断事件在浏览器是否存在)
    1. 数字计算

        1. [科学计数法转换成字符串的数字](#原生js科学计数法转换成字符串的数字)
        1. [用整数进行小数的四则运算（避免浮点数运算误差）](#原生js用整数进行小数的四则运算避免浮点数运算误差)
        1. [大数加减法（不考虑小数和负数）](#原生js大数加减法不考虑小数和负数)
        1. [不同进制数互相转换](#原生js不同进制数互相转换)
        1. [选取范围内随机值](#原生js选取范围内随机值)
    1. 字符串操作

        1. [转化为Unicode、反转字符串、字符串长度、所占字节数](#原生js转化为unicode反转字符串字符串长度所占字节数)
        1. [字符串匹配、替换](#原生js字符串匹配替换)
        1. [分割字符串](#原生js分割字符串)
        1. [产生随机数](#原生js产生随机数)
        1. [比较版本号大小（纯数字）](#原生js比较版本号大小纯数字)
        1. [判断检索内容是否在被检索内容的分隔符间](#原生js判断检索内容是否在被检索内容的分隔符间)
        1. [格式化文件大小](#原生js格式化文件大小)
    1. 功能

        1. [实现类似jQuery的`$('html,body').animate({'scrollLeft': 像素, 'scrollTop': 像素}, 毫秒);`](#原生js实现类似jquery的htmlbodyanimatescrollleft-像素-scrolltop-像素-毫秒)
        1. [用请求图片作log统计](#原生js用请求图片作log统计)
        1. [判断是否为`Node`、是否为`Element`](#原生js判断是否为node是否为element)
        1. [判断对象是否为空](#原生js判断对象是否为空)
        1. [输入框光标位置的获取和设置](#原生js输入框光标位置的获取和设置)
        1. [文本选区覆盖某DOM的文本范围](#原生js文本选区覆盖某dom的文本范围)
        1. [针对WAP的阻止滚动冒泡（仅DOM）](#原生js针对wap的阻止滚动冒泡仅dom)
        1. [获取滚动条宽度（或高度）](#原生js获取滚动条宽度或高度)
        1. [验证邮箱有效性](#原生js验证邮箱有效性)
        1. [创建兼容的XHR对象](#原生js创建兼容的xhr对象)
        1. [动态添加脚本、样式](#原生js动态添加脚本样式)
        1. [单词首字母大写](#原生js单词首字母大写)
        1. [展示页面帧数](#原生js展示页面帧数)
        1. [获取星座](#原生js获取星座)
        1. [分割数组](#原生js分割数组)
        1. [加入收藏夹](#原生js加入收藏夹)
        1. [从字符串中获取绝对路径](#原生js从字符串中获取绝对路径)
        1. [不传递请求头的Referrer进行跳转](#原生js不传递请求头的referrer进行跳转)
        1. [格式化接口返回的数据](#原生js格式化接口返回的数据)
        1. [根据滚动方向执行函数](#原生js根据滚动方向执行函数)
        1. [判断是否支持WebP](#原生js判断是否支持webp)
        1. [DOM展示或消失执行方法（IntersectionObserver）](#原生jsdom展示或消失执行方法intersectionobserver)
        1. [执行方法的前/后进行开/关loading](#原生js执行方法的前后进行开关loading)
        1. [点击下载](#原生js点击下载)
    1. 提升性能

        1. [用`setTimeout`模拟`setInterval`](#原生js用settimeout模拟setinterval)
        1. [`requestAnimationFrame`的递归](#原生jsrequestanimationframe的递归)
1. [jQuery方法](#jquery方法)

    1. 延迟异步加载

        1. [滚动加载](#jquery滚动加载)
        1. [图片延时加载（lazyload）](#jquery图片延时加载lazyload)
    1. [节点跟随屏幕滚动而相对静止](#jquery节点跟随屏幕滚动而相对静止)
    1. [弹出toast](#jquery弹出toast)
    1. [全选、取消全选](#jquery全选取消全选)
    1. [点击指定区域以外执行函数](#jquery点击指定区域以外执行函数)
    1. [hover展示内容并且可跨越间隙到内容](#jquery-hover展示内容并且可跨越间隙到内容)
    1. [启动、暂停CSS动画](#jquery启动暂停css动画)
    1. [获取`HTTP response header`信息](#jquery获取http-response-header信息)
    1. [修复HTML标签`placeholder`属性无效](#jquery修复html标签placeholder属性无效)
    1. [模拟手机旋转（使页面都以「横屏」展示）](#jquery模拟手机旋转使页面都以横屏展示)

    >大部分情况下，jQuery内容适用于Zepto。

---
## 原生JS方法

>更全面判断所在系统、浏览器：[bowser](https://github.com/lancedikson/bowser)。

### *原生JS*判断所在系统
```javascript
/**
 * 判断所在系统
 * @param {String} [ua = window.navigator.userAgent] - 用户代理
 * @param {String} [pf = window.navigator.platform] - 系统平台类型
 * @returns {String} os - 系统名：'iOS'|'Android'|'Windows Phone'|'macOS'|'Win2000'|'WinXP'|'Win2003'|'WinVista'|'Win7'|'Win10'|'Windows'|'Unix'|'Linux'
 */
function detectOS (ua = window.navigator.userAgent, pf = window.navigator.platform) {
  let os = ''

  if (/iPhone|iPad|iPod|iOS/.test(ua)) {
    os = 'iOS'
  } else if (/Android/.test(ua)) {
    os = 'Android'
  } else if (/\bWindows Phone/.test(ua)) {
    os = 'Windows Phone'
  } else {
    if (pf === 'Mac68K' || pf === 'MacPPC' || pf === 'Macintosh' || pf === 'MacIntel') {    // pf.includes('Mac')
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
>判断是WAP或PC：`if (/AppleWebKit.*Mobile/.test(window.navigator.userAgent)) { /* WAP */ } else { /* PC */ }`

### *原生JS*判断移动平台
```javascript
// 判断移动平台（微信、QQ、微博、QQ空间、UC浏览器）
function platform (ua = window.navigator.userAgent) {
  let platform

  if (/MicroMessenger/.test(ua)) {
    platform = 'wx'
  } else if (/QQ\//.test(ua)) {
    platform = 'qq'
  } else if (/\bWeibo|__weibo__\d/.test(ua)) {
    platform = 'weibo'
  } else if (/Qzone\//.test(ua)) {
    platform = 'qzone'
  } else if (/UCBrowser/.test(ua)) {
    platform = 'uc'
  } else {
    platform = 'other'
  }

  return platform
}
```

### *原生JS*判断ie6、7、8、9版本
>HTML条件注释法仅支持ie9-。

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

        /* ie10- 返回版本号 */
        return parseInt(ua.substring(msie + 5, ua.indexOf('.', msie)), 10);
    }

    var trident = ua.indexOf('Trident/');
    if (trident > 0) {
        var rv = ua.indexOf('rv:');

        /* ie11 返回版本号 */
        return parseInt(ua.substring(rv + 3, ua.indexOf('.', rv)), 10);
    }

    var edge = ua.indexOf('Edge/');
    if (edge > 0) {

        /* Edge(ie 12+) 返回版本号 */
        return parseInt(ua.substring(edge + 5, ua.indexOf('.', edge)), 10);
    }

    /* 其他浏览器 返回false */
    return false;
}
```

### *原生JS*判断是否存在某cookie
```javascript
function hasCookie (checkKey) {
  checkKey = checkKey.toString()

  var cookieArr = document.cookie.split('; '),
    tempArr, key, value

  for (var i = 0, len = cookieArr.length; i < len; i++) {
    if (cookieArr[i] !== '') {
      tempArr = cookieArr[i].split('=')
      key = tempArr.shift()
      value = tempArr.join('=')

      if (key === checkKey) {
        /* 操作value */

        return true
      }
    }
  }

  return false
}
```
>全面操作cookie：[js操作cookie](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/JS方法积累/废弃代码/README.md#原生js操作cookie)。

### *原生JS*获取URL相关信息
```javascript
/**
 * 获取URL相关信息
 * @param {String} [url = window.location.href] - URL
 * @returns {Object} location - 包括href、protocol、hostname、port、pathname、search、searchObj、hash的对象。若不是合法URL，返回false
 */
function getLocation (url) {
  try {
    url = url || window.location.href

    /* 为了方便阅读 */
    var _protocol = /^(?:([A-Za-z]+):)?/.source,
      _slash = /\/*/.source,
      _hostname = /([0-9A-Za-z.-]+)/.source,
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
  } catch (e) {  // 不是合法URL
    return false
  }
}
```
>参考：[用正则表达式分析 URL](http://harttle.com/2016/02/23/javascript-regular-expressions.html)。

>获取某search值：
>
>```javascript
>/**
> * 获取某search值
> * @param {String} checkKey - search的key
> * @param {String} [search = window.location.search] - search总字符串
> * @returns {String|Boolean} - search的value 或 不存在false
> */
>function getSearchValue (checkKey, search = window.location.search) {
>  checkKey = checkKey.toString()
>
>  if (search.slice(0, 1) === '?') {
>    search = search.slice(1)
>  }
>
>  for (let i = 0, searchArr = search.split('&'), len = searchArr.length; i < len; i++) {
>    if (searchArr[i] !== '') {
>      const tempArr = searchArr[i].split('=')
>      const key = tempArr.shift()
>      const value = tempArr.join('=')
>
>      if (key === checkKey) {
>
>        return decodeURIComponent(value)
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

### *原生JS*在URL末尾添加查询键-值
1. 单个添加（未处理同名）

    ```javascript
    /**
     * 在URL末尾添加search键-值（未处理同名）
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
2. 批量添加

    >对象转换为`a=1&b=2`：`Object.entries(对象).map((val) => val.join('=')).join('&')`。

    ```javascript
    /**
     * 在URL末尾添加search键-值
     * @param {String} [url = window.location.href] - URL
     * @param {Object} searchObj - 新增的search键-值
     * @returns {String} - 添加完毕的URL
     */
    function addUrlSearch (url = window.location.href, searchObj = {}) {
      if (Object.keys(searchObj).length === 0) {  // 空对象不处理
        return url
      }

      const hashIndex = url.indexOf('#') !== -1 ? url.indexOf('#') : url.length // # 所在的字符串位置索引
      const newUrl = url.slice(0, hashIndex) // 去除hash后url
      const searchIndex = newUrl.indexOf('?')  // ? 所在的字符串位置索引

      // 把原始search值写入对象
      const originalSearchObj = {}
      if (searchIndex !== -1) {
        const search = newUrl.slice(searchIndex + 1)  // search值（不包括 ?）

        // 写入已存在search的键-值
        const searchArr = search.split('&')
        for (let i = 0, len = searchArr.length; i < len; i++) {
          if (searchArr[i] !== '') {
            const searchItem = searchArr[i].split('=')
            const key = searchItem.shift()
            const value = searchItem.join('=')
            originalSearchObj[key] = value
          }
        }
      }

      // 合并原始search和新增search（新增会覆盖原始）
      const newSearchObj = Object.assign({}, originalSearchObj, searchObj)

      // 生成新的合并过后的search字符串
      const newSearch = Object.entries(newSearchObj).map((val) => {
        return val.join('=')
      }).join('&')

      const hash = url.slice(hashIndex)  // 原始hash

      let originPath  // 原始 origin + pathname
      if (searchIndex !== -1) {
        originPath = newUrl.slice(0, searchIndex)
      } else {
        originPath = newUrl
      }

      return originPath + (newSearch ? `?${newSearch}` : '') + hash
    }
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
        if (typeof dom.addEventListener === 'function') {   /* DOM2级，除ie8- */
            dom.addEventListener(type, handle, false);
        } else if (typeof dom.attachEvent === 'function') { /* 所有ie浏览器 */
            dom.attachEvent('on' + type, handle);   // 注意：传入的参数和this的兼容
        } else {    /* DOM0级，最早期的浏览器都支持 */
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
            dom.detachEvent('on' + type, handle);   // 注意：传入的参数和this的兼容
        } else {
            dom['on' + type] = null;
        }
    }
};
```

### *原生JS*、jQuery阻止冒泡和阻止浏览器默认行为
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
    2. jQuery

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
    2. jQuery

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
    2. jQuery

        ```javascript
        $('...').on('...', function () {

            return false;
        });
        // 或简写：$('...').on('...', false);
        ```

### *原生JS*事件代理
```javascript
dom.addEventListener('事件名', function (e) {
  const event = e || window.event
  const target = event.target || event.srcElement // 兼容ie8-

  // target为目标元素（捕获的终点、冒泡的起点）；可以用dom.matches(CSS选择器)判断是否是选择器
  // 对target满足的元素进行操作
})
```

### *原生JS*、jQuery实现判断按下具体某按键
1. `KeyboardEvent.key`

    >[MDN:KeyboardEvent.key](https://developer.mozilla.org/zh-CN/docs/Web/API/KeyboardEvent/key/Key_Values)、[W3C:KeyboardEvent.key](https://www.w3.org/TR/uievents-key/)。

    1. *原生JS*

        ```javascript
        function checkKey(e) {
            var event = e || window.event,
                key = event.key;

            if (key === 'Enter') {   /* 查询键值表 例：'Enter' -> 换行 */
                /* 具体操作... */

                /* 阻止冒泡&阻止默认行为 */
                if (e && e.stopPropagation) {
                    e.stopPropagation();
                    e.preventDefault();
                } else {
                    window.event.cancelBubble = true;
                    window.event.returnValue = false;
                }
            }
        }


        /* 使用测试 */
        addEvent(document.getElementById('test'), 'keydown', checkKey);  // 上面绑定事件
        ```
    2. jQuery

        ```javascript
        $(输入框选择器).on('keydown', function (e) {
            if (e.key === 'Enter') {   /* 查询键值表 例：'Enter' -> 换行 */
                /* 具体操作... */

                return false;   // 阻止冒泡&阻止默认行为
            }
        });
        ```
2. ~~`KeyboardEvent.which/keyCode/charCode`~~（废弃）

    1. *原生JS*

        ```javascript
        function checkKeyCode(e) {
            var event = e || window.event,
                keyCode = event.keyCode || event.charCode;  /* 获取键值 */

            if (keyCode === 13) {   /* 查询键值表 例：13 -> 换行 */
                /* 具体操作... */

                /* 阻止冒泡&阻止默认行为 */
                if (e && e.stopPropagation) {
                    e.stopPropagation();
                    e.preventDefault();
                } else {
                    window.event.cancelBubble = true;
                    window.event.returnValue = false;
                }
            }
        }


        /* 使用测试 */
        addEvent(document.getElementById('test'), 'keydown', checkKeyCode);  // 上面绑定事件
        ```
    2. jQuery

        ```javascript
        $(输入框选择器).on('keydown', function (e) {
            if (e.which === 13) {   /* 查询键值表 例：13 -> 换行 */
                /* 具体操作... */

                return false;   // 阻止冒泡&阻止默认行为
            }
        });
        ```
>线上查询：[keycode.info](http://keycode.info/)。

### *原生JS*拖拽和放下
- 步骤：

    1. 在DOM上绑定`mousedown`（或`touchstart`），执行：

        1. 记录基础初始位置：初始鼠标（或touch点）位置、DOM自身位置
        2. 在DOM上绑定`mousemove`（或`touchmove`）

            1. 获取最终位置：`当前鼠标（或touch）位置 - 初始鼠标（或touch）位置 + DOM自身位置`
            2. 把最终位置赋予DOM
    2. 在DOM祖先上绑定`mouseup`、`mouseleave`（或`touchend`、`touchcancel`），执行：

        在DOM上解绑`mousemove`（或`touchmove`）

    >每一个事件处理，都可加入阻止冒泡。

1. PC端的鼠标事件

    ```javascript
    function Drag(dom, parentDom) {
        var maxX = parentDom.offsetWidth - dom.offsetWidth,
            maxY = parentDom.offsetHeight - dom.offsetHeight,
            domX, domY, beginX, beginY;

        /* 绑定事件 */
        function _addHandler(dom, type, handle) {
            if (typeof dom.addEventListener === 'function') {
                dom.addEventListener(type, handle, false);
            } else if (typeof dom.attachEvent === 'function') {
                dom.attachEvent('on' + type, handle);
            } else {
                dom['on' + type] = handle;
            }
        }

        /* 解绑事件 */
        function _removeHandler(dom, type, handle) {
            if (typeof dom.removeEventListener === 'function') {
                dom.removeEventListener(type, handle, false);
            } else if (typeof dom.detachEvent === 'function') {
                dom.detachEvent('on' + type, handle);
            } else {
                dom['on' + type] = null;
            }
        }

        /* 阻止冒泡&阻止默认行为 */
        function _returnFalse(e) {
            if (e && e.stopPropagation) {
                e.stopPropagation();
                e.preventDefault();
            } else {
                window.event.cancelBubble = true;
                window.event.returnValue = false;
            }
        }

        /* 拖拽开始 */
        function actBegin(e) {
            e = e || window.event;

            domX = dom.offsetLeft;
            domY = dom.offsetTop;

            beginX = e.clientX; // 或e.pageX/Y（ie不兼容）
            beginY = e.clientY;

            _addHandler(parentDom, 'mousemove', actMove);

            _returnFalse(e); // 阻止冒泡、阻止默认行为
        }

        /* 拖拽移动 */
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

            /* 具体移动（使用left、top） */
            // requestAnimationFrame(function () {
                dom.style.left = finalX + 'px';
                dom.style.top = finalY + 'px';
            // });

            _returnFalse(e); // 阻止冒泡、阻止默认行为
        }

        /* 拖拽取消 */
        function cancel(e) {
            _removeHandler(parentDom, 'mousemove', actMove);

            _returnFalse(e); // 阻止冒泡、阻止默认行为
        }

        /* 绑定事件 */
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


    /* 使用测试 */
    var dom = document.getElementById('j-rect');
    var action = new Drag(dom, dom.offsetParent);

    // action.stop();
    ```
    [CodePen demo](https://codepen.io/realgeoffrey/pen/GVNPeN)
2. WAP端的touch事件

    ```javascript
    function Drag(dom, parentDom) {
        var maxX = parentDom.offsetWidth - dom.offsetWidth,
            maxY = parentDom.offsetHeight - dom.offsetHeight,
            domX, domY, beginX, beginY;

        /* 拖拽开始 */
        function actBegin(e) {
            domX = dom.offsetLeft;
            domY = dom.offsetTop;

            beginX = e.touches[0].pageX;
            beginY = e.touches[0].pageY;

            parentDom.addEventListener('touchmove', actMove, false);

            /* 阻止冒泡、阻止默认行为 */
            e.stopPropagation();
            e.preventDefault();
        }

        /* 拖拽移动 */
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

            /* 具体移动（使用left、top） */
            requestAnimationFrame(function () {
                dom.style.left = finalX + 'px';
                dom.style.top = finalY + 'px';
            });

            /* 阻止冒泡、阻止默认行为 */
            e.stopPropagation();
            e.preventDefault();
        }

        /* 拖拽取消 */
        function cancel(e) {
            parentDom.removeEventListener('touchmove', actMove, false);

            /* 阻止冒泡、阻止默认行为 */
            e.stopPropagation();
            e.preventDefault();
        }

        /* 绑定事件 */
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


    /* 使用测试 */
    var dom = document.getElementById('j-rect');
    var action = new Drag(dom, dom.offsetParent);

    // action.stop();
    ```

### *原生JS*触摸屏模拟点击事件（消除「延时300毫秒后才触发click事件」，使点击事件提前触发）
```javascript
/* 不要绑定click事件，用touchstart和touchend模拟，以消除「延时300毫秒后才触发」的问题 */

var start_x, start_y;

document.getElementById('...').addEventListener('touchstart', function (e) {
    start_x = e.changedTouches[0].clientX;
    start_y = e.changedTouches[0].clientY;
}, false);

document.getElementById('...').addEventListener('touchend', function (e) {
    var end_x = e.changedTouches[0].clientX,
        end_y = e.changedTouches[0].clientY;

    if (Math.abs(end_x - start_x) > 5 || Math.abs(end_y - start_y) > 5) {
        /* 触发滑动事件要做的事情（如：什么都不做） */
    } else {
        /* 触发点击事件要做的事情 */
    }
}, false);

/* 还要处理浏览器默认点击事件（如：`<a>`） */
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
        if (!element.setAttribute) {    /* 若节点没有setAttribute方法，则改用div节点进行测试 */
            element = document.createElement('div');
        }
        if (element.setAttribute && element.removeAttribute) {
            element.setAttribute(eventName, '');
            isSupported = typeof element[eventName] === 'function';

            if (element[eventName] !== undefined) { /* 内存回收 */
                element[eventName] = undefined;
            }
            element.removeAttribute(eventName); /* 内存回收 */
        }
    }

    element = null; /* 内存回收 */

    return isSupported;
}
```

>更全面的性能监听：[stats.js](https://github.com/mrdoob/stats.js/)。

### *原生JS*科学计数法转换成字符串的数字
```javascript
function eToString(number) {
    number = number.toString(10);

    var regex = /^(\d)(?:\.(\d*))?[eE]([+-]?)(\d+)$/,   // 科学计数法
        regexArr = regex.exec(number);

    if (regexArr === null) {

        return number;
    } else {
        var dotNumber = regexArr[2] ? regexArr[2] : '',
            dotLength = dotNumber.length, // 小数位数
            multiple = regexArr[4], // 10进制位数
            gap = Math.abs(multiple - dotLength),
            tempArr = [],
            i, result;

        if (regexArr[3] !== '-') {  /* 大于1 */
            if (multiple >= dotLength) {    /* 没有小数 */
                for (i = 0; i < gap; i++) {
                    tempArr.push('0');
                }

                result = regexArr[1] + dotNumber + tempArr.join('');
            } else {  /* 有小数 */
                result = regexArr[1] + dotNumber.substr(0, multiple) + '.' + dotNumber.substr(multiple);
            }
        } else { /* 小于1 */
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
    add: function (arg1, arg2) {    /* 加 */
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
    sub: function (arg1, arg2) {    /* 减 */

        return this.add(arg1, -arg2);
    },
    mul: function (arg1, arg2) {    /* 乘 */
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
    div: function (arg1, arg2) {    /* 除 */
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
>类似[number-precision](https://github.com/nefe/number-precision)。

### *原生JS*大数加减法（不考虑小数和负数）
```javascript
var overRangeOperations = {
    add: function (arg1, arg2) {    /* 加 */
        /* 需要把科学计数法转化为字符串的数字 */
        arg1 = arg1.toString(10).split('');
        arg2 = arg2.toString(10).split('');

        var carry = 0,  // 进位
            result = [],
            temp;

        while (arg1.length || arg2.length || carry) {
            temp = parseInt(arg1.pop() || 0, 10) + parseInt(arg2.pop() || 0, 10) + carry;
            result.unshift(temp % 10);
            carry = Math.floor(temp / 10);
        }

        return result.join('');
    },

    sub: function (arg1, arg2) {    /* 减 */
        /* 需要把科学计数法转化为字符串的数字 */
        arg1 = arg1.toString(10).split('');
        arg2 = arg2.toString(10).split('');

        var isArg2Bigger, // 标记arg2是否大于arg1
            result = [],
            i, len, temp;

        (function () {  /* 确保大数减小数 */
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

                arg1[arg1.length - 1] -= 1; // 由于arg1一定大于等于arg2，所以不存在arg1[i-1]为undefined的情况
            }
        }

        result = result.join('').replace(/^0*/, '');    // 去掉前面的0

        if (result === '') {
            result = 0;
        } else {
            result = (isArg2Bigger ? '-' : '') + result;
        }

        return result;
    }
};
```

### *原生JS*不同进制数互相转换
```javascript
/**
 * 不同进制（2至36进制）换算（10个阿拉伯数字+26个字母）
 * @param {String} operand - 转换数（2进制仅使用0~1、8进制仅使用0~7、10进制仅使用0~9、16进制仅使用0~9和a~f，等）
 * @param {Number} fromRadix - 转换数的进制数（2~36）
 * @param {Number} toRadix - 结果的进制数
 * @returns {String|Boolean|Number} - 转换后的数值；进制数不在2~36：false；操作数与进制数不匹配：NaN
 */
function numConvert (operand, fromRadix, toRadix) {
  if (fromRadix > 36 || fromRadix < 2 || toRadix > 36 || toRadix < 2) {    /* 仅支持2至36进制 */
    console.log('进制数只能在2至36之间')
    return false
  } else {
    // 先转化为10进制
    if (fromRadix === 10) {
      operand = parseInt(operand, 10)
    } else {
      operand = parseInt(operand, fromRadix)  // 其他进制转化为10进制
    }

    // 再由10进制转化为其他进制
    return operand.toString(toRadix)
  }
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
>1. 若返回的是：`(0,1)`，则返回`Math.floor(Math.random() * (max - min + 2) + min - 1);`。
>2. 若返回的是：`(0,1]`，则返回`Math.floor(Math.random() * (max - min + 1) + min - 1);`。
>3. 若返回的是：`[0,1]`，则返回`Math.floor(Math.random() * (max - min) + min);`。

### *原生JS*转化为Unicode、反转字符串、字符串长度、所占字节数
>注意：Unicode码点大于`\uFFFF`（65535）的字符，如：`'💩'.codePointAt(0) // 128169`

1. 转化为Unicode

    ```javascript
    // 转化为Unicode
    function toUnicode (words) {
      const arr = []

      for (let i = 0; i < words.length; i++) {
        const unicode = words.charCodeAt(i).toString(16)
        arr[i] = '\\u' + '0'.repeat(4 - unicode.length) + unicode // 单个Unicode：\u+4位16进制数；一个字可能不止一个Unicode，如：💩
      }

      return arr.join('')
    }


    /* 使用测试 */
    console.log(toUnicode('💩'), toUnicode('哈'), toUnicode('©')) // => \ud83d\udca9 \u54c8 \u00a9
    ```
2. 反转字符串

    ```javascript
    // 反转字符串
    function reverseWords (words) {
      return Array.from(words).reverse().join('')

      // 或：return [...words].reverse().join('');
    }


    /* 使用测试 */
    console.log(reverseWords('💩哈©')) // => ©哈💩
    ```
3. 字符串长度

    ```javascript
    // 字符串长度
    function codePointLength (words) {
      const result = words.match(/[\s\S]/gu)
      return result ? result.length : 0

      // 或：return [...words].length;
    }


    /* 使用测试 */
    console.log(codePointLength('💩哈©'))  // => 3
    ```
4. 所占字节数

    ```javascript
    /**
     * 所占字节数
     *
     * UTF-8 一种可变长度的Unicode编码格式，使用一至四个字节为每个字符编码（Unicode在范围 D800-DFFF 中不存在任何字符）
     * 000000 - 00007F(128个代码)      0zzzzzzz(00-7F)                             一个字节
     * 000080 - 0007FF(1920个代码)     110yyyyy(C0-DF) 10zzzzzz(80-BF)             两个字节
     * 000800 - 00D7FF
     * 00E000 - 00FFFF(61440个代码)    1110xxxx(E0-EF) 10yyyyyy 10zzzzzz           三个字节
     * 010000 - 10FFFF(1048576个代码)  11110www(F0-F7) 10xxxxxx 10yyyyyy 10zzzzzz  四个字节
     * {@link https://zh.wikipedia.org/wiki/UTF-8}
     *
     * UTF-16 编码65535以内使用两个字节编码，超出65535的使用四个字节（JS内部，字符储存格式是：UCS-2——UTF-16的子级）
     * 000000 - 00FFFF  两个字节
     * 010000 - 10FFFF  四个字节
     * {@link https://zh.wikipedia.org/wiki/UTF-16}
     *
     * GBK(ASCII的中文扩展) 除了0~126编号是1个字节之外，其他都2个字节（超过65535会由2个字显示）
     * {@link https://zh.wikipedia.org/wiki/汉字内码扩展规范}
     *
     * @param  {String} str
     * @param  {String} [charset= 'gbk'] utf-8, utf-16
     * @return {Number}
     */
    function sizeofByte (str, charset = 'gbk') {
      let total = 0
      let charCode

      charset = charset.toLowerCase()

      if (charset === 'utf-8' || charset === 'utf8') {
        for (let i = 0, len = str.length; i < len; i++) {
          charCode = str.codePointAt(i)

          if (charCode <= 0x007f) {
            total += 1
          } else if (charCode <= 0x07ff) {
            total += 2
          } else if (charCode <= 0xffff) {
            total += 3
          } else {
            total += 4
            i++
          }
        }
      } else if (charset === 'utf-16' || charset === 'utf16') {
        for (let i = 0, len = str.length; i < len; i++) {
          charCode = str.codePointAt(i)

          if (charCode <= 0xffff) {
            total += 2
          } else {
            total += 4
            i++
          }
        }
      } else {
        total = str.replace(/[^\x00-\xff]/g, 'aa').length
      }

      return total
    }


    /* 使用测试 */
    console.log(sizeofByte('💩'), sizeofByte('哈'), sizeofByte('©')) // => 4 2 1
    ```

### *原生JS*字符串匹配、替换
```javascript
/**
 * 字符串匹配并替换一个字符串
 * @param {String} key - 被匹配内容
 * @param {String} sentence - 原始字符串
 * @param {String} prefix - 匹配处增加的前缀
 * @param {String} suffix - 匹配处增加的后缀
 * @param {String} [keyReplace = key] - 替换内容
 * @returns {String} - 匹配后的字符串
 */
function highlightWords ({ key, sentence, prefix = '', suffix = '', keyReplace = key }) {
  // 把需要匹配的字符串里`正则表达式需要转义的特殊字符`（除去原本在字符串中作为转义的`\`）前添加`\\`
  const keyReformat = key.replace(/([()[\]{}\\/^$|?*+.])/g, '\\$1')

  const regexp = new RegExp(keyReformat, 'g')

  return sentence.replace(regexp, `${prefix + keyReplace + suffix}`)
}


/* 使用测试 */
highlightWords({
  key: 'abc',
  sentence: 'abc123aabbccabc123',
  prefix: '<span style="color: red;">',
  suffix: '</span>',
  keyReplace: '被选中'
})
```

### *原生JS*分割字符串
```javascript
/**
 * 按单个字分割字符串（弥补String.prototype.split会分割65535以上的字为2个字）
 * @param  {String} str
 * @return {Array} resultArray - 分割字符串后的数组
 */
function split (str) {
  const resultArray = []

  for (let i = 0, len = str.length; i < len; i++) {
    if (str.codePointAt(i) <= 0xffff) {
      resultArray.push(str[i])
    } else {
      resultArray.push(str[i] + str[i + 1])
      i++
    }
  }

  return resultArray
}


/* 使用测试 */
console.log(split('💩1a💩哈。.↑'))  // =>  ["💩", "1", "a", "💩", "哈", "。", ".", "↑"]
```

### *原生JS*产生随机数
```javascript
/**
 * 随机数产生
 * @param {Number} length - 随机数长度
 * @param {String} [charset = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'] - 随机数的字符
 * @returns {String} - 随机数
 */
function random (length, charset = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789') {
  return Array.from({ length }, () => {
    return charset.charAt(Math.floor(Math.random() * charset.length))
  }).join('')
}
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

        if (arr1[i] !== arr2[i]) {  /* 两值不同 */
            flag = parseInt(arr1[i], 10) < parseInt(arr2[i], 10) ? '<' : '>';

            break;
        }
    }

    return flag;
}


/* 使用测试 */
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

### *原生JS*格式化文件大小
```javascript
/**
 * 格式化文件大小
 */
function fileSize (bytes = 0) {
  if (bytes === 0) {
    return '0'
  }

  const units = ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'] // 单位
  const rate = 1024 // 换算关系
  const exponent = Math.min( // 所在单位
    Math.floor(Math.log(bytes) / Math.log(rate)),
    units.length - 1
  )
  let value = bytes / (rate ** exponent)  // 值

  // 精确位数
  value = (exponent === 0 || value > 1000)
    ? Math.round(value)
    : value.toPrecision(3)

  return value + units[exponent]  // 值 + 单位
}


/* 使用测试 */
fileSize(数字)
```

### *原生JS*单词首字母大写
```javascript
function upperCaseWord(str) {

    return str.replace(/\b[a-zA-Z]/g, function (match) {

        return match.toUpperCase();
    });
}
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
>如：滚动到某位置`$('html').velocity('scroll', {offset: y轴像素, duration: 毫秒});`。

### *原生JS*用请求图片作log统计
```javascript
var sendLog = (function () {
    if (typeof Date.now !== 'function') {
        Date.now = function () {
            return new Date().getTime();
        };
    }

    var _unique = (function () {    /* 产生唯一标识 */
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

        data[uid] = img;    // 防止img被垃圾处理

        img.onload = img.onerror = function () {    /* 成功或失败后销毁对象 */
            img.onload = img.onerror = null;
            img = null;
            delete data[uid];
        };

        img.src = url + '&_cache=' + uid;   // 发送统计内容
    };

    return run;
}());


/* 使用测试 */
sendLog('统计url');
```

### *原生JS*判断是否为`Node`、是否为`Element`
```javascript
// 判断是否为Node
function isNode(o) {
  return typeof Node === 'object' ? o instanceof Node : !!o && typeof o === 'object' && typeof o.nodeType === 'number' && typeof o.nodeName === 'string';
}

// 判断是否为Element
function isElement(o) {
  return typeof HTMLElement === 'object' ? o instanceof HTMLElement : !!o && typeof o === 'object' && o !== null && o.nodeType === 1 && typeof o.nodeName === 'string';
}
```

### *原生JS*判断对象是否为空
```javascript
function isObjEmpty(obj) {
    if (obj !== Object(obj)) {  /* 参数不是对象 */
        throw new TypeError('参数不是对象');
    } else if (typeof Object.keys === 'function') { /* ie9+ */

        return Object.keys(obj).length === 0;
    } else {
        for (var one in obj) {
            if (obj.hasOwnProperty(one)) {

                return false;
            }
        }

        return true;
    }
}
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
        var start = 0,  // 光标起始位置
            selLen = 0, // 光标选中长度
            sel, ieSel;

        if ('selectionStart' in dom) {
            start = dom.selectionStart;
            selLen = dom.selectionEnd - start;
        } else if (document.selection) {    /* ie */
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

        /* 初始化start */
        start = parseInt(start, 10);
        if (!start) {
            start = 0;
        } else if (start > valueLen) {
            start = valueLen;
        }

        /* 初始化len */
        len = parseInt(len, 10);
        if (!len) {
            len = 0;
        }

        /* 初始化end */
        end = start + len;
        if (end > valueLen) {
            end = valueLen;
        }

        if (valueLen !== 0) {
            if (dom.setSelectionRange) {
                dom.setSelectionRange(start, end);
                dom.focus();
            } else {    /* ie */
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
            } else {    /* ie */
                ieSel = dom.createTextRange();
                ieSel.select();
            }
        }

        return end;
    }
};


/* 使用测试 */
$(输入框选择器).on('mouseup keyup', function () {
    console.log(cursorPosition.get(this));
});

console.log(cursorPosition.set(输入框dom, 起始位置, 选中长度));
```
[CodePen demo](https://codepen.io/realgeoffrey/pen/BXQvbZ)

### *原生JS*文本选区覆盖某DOM的文本范围
```javascript
/**
 * 文本选区覆盖某DOM文本范围
 * @param {Object} dom - DOM对象
 * @returns {Boolean} 是否成功
 */
function selectElement (dom) {
  if (window.getSelection && dom) {  // ie9+
    let sel = window.getSelection()
    sel.removeAllRanges()
    let range = document.createRange()
    range.selectNode(dom)
    sel.addRange(range)
    return true
  } else {
    return false
  }
}
```

### *原生JS*针对WAP的阻止滚动冒泡（仅DOM）
>1. 因为`scroll`事件不会冒泡，所以`stopPropagation`、`preventDefault`无法达到效果。
>2. iOS可以在DOM滚动到顶部或底部时，通过`-webkit-overflow-scrolling: touch;`继续触发「橡皮筋效果」。

```html
<style>
    .bounce {
        overflow-y: scroll;
        -webkit-overflow-scrolling: touch;  /* 增加DOM的回弹效果（iOS） */

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
const ScrollStopPropagation = function (dom) {
  const _stopPropagation = function () {
    const startTopScroll = dom.scrollTop  // 滚动高度
    const domHeight = dom.offsetHeight  // 占据高度
    const contentHeight = dom.scrollHeight  // 内容高度（占据高度+可滚动最大高度

    /*
     * 在触摸开始时，若发现滚动区域已经处于极限状态时，则手工设置 scrollTop 的值，
     * 将滚动内容向边缘方向偏移 1px（这实际上改变了滚动区域的极限状态），
     * 从而诱使浏览器对滚动区块使用橡皮筋效果，而不会把触摸事件向上传播到 DOM 树（引起整页滚动）。
     */
    if (startTopScroll <= 0) {
      dom.scrollTop = 1
    } else if (startTopScroll + domHeight >= contentHeight) {
      dom.scrollTop = contentHeight - domHeight - 1
    }
  }

  dom.addEventListener('touchstart', _stopPropagation, false)

  this.stop = () => {
    dom.removeEventListener('touchstart', _stopPropagation, false)
  }
}

/* 使用测试 */
const a = new ScrollStopPropagation(document.getElementById('j-bounce'))


// a.stop()
</script>
```
[CodePen demo](https://codepen.io/realgeoffrey/pen/oKYJOg)
>参考[ScrollFix](https://github.com/joelambert/ScrollFix)。

### *原生JS*获取滚动条宽度（或高度）
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

### *原生JS*验证邮箱有效性
>来自：[stackoverflow:Validate email address in JavaScript?](http://stackoverflow.com/questions/46155/validate-email-address-in-javascript#answer-46181)。

```javascript
function validateEmail(email) {

    return /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(email);
}
```

>不存在可以判断世界任何一个有效邮箱的正则。

>匹配中国大陆手机号码的正则表达式：[ChinaMobilePhoneNumberRegex](https://github.com/VincentSit/ChinaMobilePhoneNumberRegex)。

### *原生JS*创建兼容的XHR对象
```javascript
function createXHR() {
    if (typeof XMLHttpRequest !== 'undefined') {    // ie7+和其他浏览器

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
                    // 跳过
                }
            }
        }

        return new ActiveXObject(arguments.callee.activeXString);   // 返回ActiveXObject对象
    } else {// 全部不支持，抛出错误
        throw new Error('don\'t support XMLHttpRequest');
    }
}


/* 使用测试 */
var xhr = createXHR();

xhr.onreadystatechange = function () {  // 或DOM2级、ie事件绑定方式
    console.log(xhr.getResponseHeader(头), xhr.getAllResponseHeaders());

    if (xhr.readyState === 4) {
        if ((xhr.status >= 200 && xhr.status < 300) || xhr.status === 304) {
            console.log(xhr.responseText);
        } else {
            console.log('请求失败：' + xhr.status);
        }

        // xhr.abort();
        // xhr = null;
    }
};
xhr.open(请求类型, URL[, 是否异步[, 用户名[, 密码]]]);
xhr.setRequestHeader(头, 值);
xhr.send(null);
```

### *原生JS*动态添加脚本、样式
1. 动态添加脚本

    1. 异步（JS文件地址）

        1. 动态创建`<script>`

            >默认是`async`（可以手动设置`newScript.async = false`）；没有`async`时按动态添加的时序（与位置无关）执行。

            ```javascript
            const newScript = document.createElement('script')
            const appendPlace = document.getElementsByTagName('body')[0] || document.getElementsByTagName('head')[0]

            newScript.src = 'JS文件地址'

            appendPlace.appendChild(newScript)
            ```
        2. 改变已存在的`<script>`的`src`属性

            >效果类似于`async`。

            ```html
            <script type="text/javascript" id="节点id"></script>

            <script>
                document.getElementById('节点id').src = 'JS文件地址';
            </script>
            ```
        3. 直接`document.write`

            >因为`document.write`需要向文档流中写入内容，因此在关闭（已加载）的文档上调用`document.write`会自动调用`document.open`，这将清空该文档的内容。

            ```javascript
            document.write('<script src="JS文件地址"><\/script>');
            ```
    2. 同步（JS代码文本）

        >动态创建的、没有`src`属性的、通过`text`属性设置JS代码文本的`<script>`，添加后的脚本被马上执行（可以认为是当前脚本一部分，但实际不是，作用域不同；这个也是jQuery的ajax加载执行外部JS脚本的方式）。

        ```javascript
        var newScript = document.createElement('script')
        var appendPlace = document.getElementsByTagName('body')[0] || document.getElementsByTagName('head')[0]

        try {
            newScript.appendChild(document.createTextNode('JS代码文本'))
        } catch (e) {
            newScript.text = 'JS代码文本'  // ie8-，Safari老版本
        }

        appendPlace.appendChild(newScript)  // 开始同步执行`JS代码文本`（新建一个独立作用域）

        // 上面代码同步执行完毕再执行下面的代码
        ```

        ><details>
        ><summary>通过<code>XMLHttpRequest</code>的同步请求获得JS代码文本</summary>
        >
        >```javascript
        >/**
        > * 同步加载JS脚本
        > * @param {String} url - JS文件的相对路径或绝对路径
        > * @returns {Boolean} - 是否加载成功
        > */
        >function syncLoadJS(url) {
        >    var xmlHttp,
        >        appendPlace,
        >        newScript;
        >
        >    if (window.ActiveXObject) { /* ie */
        >        try {
        >            xmlHttp = new ActiveXObject('Msxml2.XMLHTTP');
        >        }
        >        catch (e) {
        >            xmlHttp = new ActiveXObject('Microsoft.XMLHTTP');
        >        }
        >    } else if (window.XMLHttpRequest) {
        >        xmlHttp = new XMLHttpRequest();
        >    }
        >
        >    xmlHttp.open('GET', url, false);    // 采用同步加载
        >    xmlHttp.send(null); // 发送同步请求，若浏览器为Chrome或Opera，则必须发布后才能运行，不然会报错
        >
        >    /* 4代表数据发送完毕 */
        >    if (xmlHttp.readyState == 4) {
        >        /* 0为访问的本地，200到300代表访问服务器成功，304代表没做修改访问的是缓存 */
        >        if ((xmlHttp.status >= 200 && xmlHttp.status < 300) || xmlHttp.status == 0 || xmlHttp.status == 304) {
        >            newScript = document.createElement('script');
        >            appendPlace = document.getElementsByTagName('body')[0] || document.getElementsByTagName('head')[0];
        >
        >            try {
        >                newScript.appendChild(document.createTextNode(xmlHttp.responseText));
        >            }
        >            catch (e) {
        >                newScript.text = xmlHttp.responseText;
        >            }
        >
        >            appendPlace.appendChild(newScript);
        >
        >            return true;
        >        }
        >        else {
        >
        >            return false;
        >        }
        >    }
        >    else {
        >
        >        return false;
        >    }
        >}
        >```
        ></details>
2. 动态添加样式

    1. 添加`<style>`

        ```javascript
        var newStyle = document.createElement('style');

        newStyle.type = 'text/css';

        try {
            newStyle.appendChild(document.createTextNode('CSS代码文本'));
        }
        catch (e) {
            newStyle.styleSheet.cssText = 'CSS代码文本';  // ie
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

        oneDom.style.cssText += '; CSS代码文本'
        ```

    >CSS代码文本，如：`div {background-color: yellow;}`。

### *原生JS*展示页面帧数
```javascript
/**
 * 展示fps
 * @constructor
 * @param {Object} [dom] - 展示的DOM
 */
function ShowFPS (dom) {
  let fps = 0
  let before = Date.now()
  let now
  const show = function (fps) {
    dom.innerHTML = 'fps: ' + fps
  }

  let father
  if (!dom) {
    dom = document.createElement('span')
    dom.style.cssText = 'position: fixed; top: 0px; background: white; color: black; z-index: 1;'

    father = document.getElementsByTagName('body')[0] || document.getElementsByTagName('head')[0]
    father.appendChild(dom)
  }

  const self = this

  this.id = requestAnimationFrame(function repeatShow () {
    now = Date.now()

    if (now - before >= 1000) {
      before = now
      show(fps)
      fps = 0
    } else {
      fps += 1
    }

    self.id = requestAnimationFrame(repeatShow)
  })

  this.stop = () => {
    cancelAnimationFrame(this.id)

    if (father) {
      father.removeChild(dom)
    } else {
      dom.innerHTML = ''
    }
  }
}


/* 使用测试 */
var a = new ShowFPS();

// a.stop();
```

### *原生JS*获取星座
```javascript
/**
 * 获取星座
 * @param {String|Number} birthday - 年月日（8位，如：'19900220'或19900220） 或 空字符串
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

>月份格式化为英文缩写：
>
>```javascript
>/**
> * 月份格式化
> * @param {Number} month - 月份编号：0：1月、11：12月
> * @returns {String} - 月份英文缩写
> */
>function monthFormat (month) {
>  const monthArr = ['Jan.', 'Feb.', 'Mar.', 'Apr.', 'May', 'June', 'July', 'Aug.', 'Sept.', 'Oct.', 'Nov.', 'Dec.']
>  return monthArr[month]
>}
>
>
>/* 使用测试 */
>monthFormat(new Date().getMonth())
>```

### *原生JS*分割数组
```javascript
/**
 * 分割数组，并以嵌套数组形式返回
 * @param {Array} arr - 数组
 * @param {Number} [divisor = 1] - 分割除数
 * @returns {Array} newArr - 如：[[0, 1, 2], [3, 4, 5], [6]]
 */
function divideArr(arr, divisor) {
    divisor = divisor || 1;
    arr = arr.slice();  // 浅复制

    var newArr = [];    // 数组中嵌套数组的形式返回
    var tempArr = [];   // 临时数组

    while (arr.length > 0) {
        for (var i = 0; i < divisor && arr.length > 0; i++) {
            tempArr.push(arr.shift());
        }
        newArr.push(tempArr);
        tempArr = [];
    }

    return newArr;
}
```

### *原生JS*加入收藏夹
```javascript
function addFavorite(url, title) {  /* url必须带有协议头 */
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


/* 使用测试 */
addFavorite(window.location.href, '收藏名字');
```

### *原生JS*从字符串中获取绝对路径
```javascript
function getAbsoluteUrl(url) {
    var domA;

    if (typeof url === 'undefined') {

        return window.location.href;
    } else {
        domA = document.createElement('a');
        domA.href = url;

        return domA.href;
    }
}
```

### *原生JS*不传递请求头的Referrer进行跳转
>1. 注意：内容安全策略（Content-Security-Policy，CSP）的`script-src`会限制脚本运行；非用户操作的打开新窗口也会受到浏览器的限制（`window.open`）。因此以下代码不靠谱。
>2. 建议使用`<a>`中添加`rel="noreferrer"`来替代。

```javascript
// 不发送referrer的当前页面跳转
function noreferrerOpen (link) {
  const iframe = document.createElement('iframe')
  iframe.style.display = 'none'
  iframe.src = `javascript: "<script>top.location.replace('${link}')<\/script>"`
  document.getElementsByTagName('body')[0].appendChild(iframe)
}


// 不发送referrer的新窗口打开
function noreferrerOpenNew (fullLink) {  // 需要完整URL
  // 此时只能父级向子级通信；若父级修改子级的location，则父子重新建立连接且子级有referrer
  return window.open(`javascript: window.name`, `<script>location.replace('${fullLink}')<\/script>`)
}
```

### *原生JS*格式化接口返回的数据
1. 格式化数组

    ```javascript
    /**
     * （针对接口返回）格式化数组。不是数组则返回[]；是数组则每项都添加键-值默认值
     * @param {Array} list - 要处理的数组
     * @param {Object} [params = {}] - 要添加的键-值的对象。键是要添加的键，值是添加键的默认值
     * @returns {Array} newList - 处理好的数组
     */
    function formatArr (list, params = {}) {
      // 是否是空对象
      const isObjEmpty = (obj) => {
        if (obj !== Object(obj)) {  /* 参数不是对象 */
          throw new TypeError('参数不是对象');
        } else if (typeof Object.keys === 'function') { /* ie9+ */
          return Object.keys(obj).length === 0;
        } else {
          for (let one in obj) {
            if (obj.hasOwnProperty(one)) {
              return false;
            }
          }

          return true;
        }
      };

      let newList = [];

      if (Array.isArray(list)) {
        if (isObjEmpty(params)) {
          newList = list;
        } else {  // 需要添加键-值
          newList = list.map((item) => {
            for (let one of Object.entries(params)) {
              if (typeof item[one[0]] === 'undefined') {  // 没有判断null
                item[one[0]] = one[1] || '';
              }
            }

            return item;
          });
        }
      }

      return newList;
    }


    /* 使用测试 */
    formatArr(
      [{}, { 参数1: '有值' }],
      { '参数1': '默认值1', '参数2': true, '参数3': { a: 1 } }
    );
    ```
2. 格式化对象

    ```javascript
    /**
     * （针对接口返回）格式化对象。不是对象则返回params；是对象则添加键-值默认值
     * @param {Object} obj - 要处理的对象
     * @param {Object} [params = {}] - 要添加的键-值的对象。键是要添加的键，值是添加键的默认值
     * @returns {Object} obj - 处理好的对象
     */
    function formatObj (obj = {}, params = {}) {
      // 是否是空对象
      const isObjEmpty = (obj) => {
        if (obj !== Object(obj)) {  /* 参数不是对象 */
          throw new TypeError('参数不是对象');
        } else if (typeof Object.keys === 'function') { /* ie9+ */
          return Object.keys(obj).length === 0;
        } else {
          for (let one in obj) {
            if (obj.hasOwnProperty(one)) {
              return false;
            }
          }

          return true;
        }
      };

      if (Object.prototype.toString.call(obj) === '[object Object]') {
        if (!isObjEmpty(params)) {  // 需要添加键-值
          for (let one of Object.entries(params)) {
            if (typeof obj[one[0]] === 'undefined') { // 没有判断null
              obj[one[0]] = one[1] || '';
            }
          }
        }
      } else {
        obj = params;
      }

      return obj;
    }


    /* 使用测试 */
    formatObj(
      { '参数1': '有值' },
      { '参数1': '默认值1', '参数2': true, '参数3': { a: 1 } }
    );
    ```

### *原生JS*根据滚动方向执行函数
```javascript
/**
 * 根据滚动方向直行对应
 * @constructor
 * @param {object} [dom = window] - 监听滚动的DOM
 * @param {Function} [up] - 向上滚动的回调
 * @param {Function} [down] - 向下滚动的回调
 * @param {Function} [left] - 向左滚动的回调
 * @param {Function} [right] - 向右滚动的回调
 */
function ScrollDirection ({dom = window, up = () => {}, down = () => {}, left = () => {}, right = () => {}} = {}) {
  let beforeV // 垂直滚动高度
  let beforeH // 水平滚动高度
  if (dom === window) {
    beforeV = document.body.scrollTop || document.documentElement.scrollTop
    beforeH = document.body.scrollLeft || document.documentElement.scrollLeft
  } else {
    beforeV = dom.scrollTop
    beforeH = dom.scrollLeft
  }

  const handleScroll = () => {
    let afterV  // 垂直滚动高度
    let afterH  // 水平滚动高度
    if (dom === window) {
      afterV = document.body.scrollTop || document.documentElement.scrollTop
      afterH = document.body.scrollLeft || document.documentElement.scrollLeft
    } else {
      afterV = dom.scrollTop
      afterH = dom.scrollLeft
    }

    const gapV = afterV - beforeV
    const gapH = afterH - beforeH

    if (gapV > 0) {
      down()
    } else if (gapV < 0) {
      up()
    }

    if (gapH > 0) {
      right()
    } else if (gapH < 0) {
      left()
    }

    beforeV = afterV
    beforeH = afterH
  }

  dom.addEventListener('scroll', handleScroll, false)

  this.stop = () => {
    dom.removeEventListener('scroll', handleScroll, false)
  }
}


/* 使用测试 */
var a = new ScrollDirection({
  up: () => {console.log('up')},
  down: () => {console.log('down')},
  left: () => {console.log('left')},
  right: () => {console.log('right')}
})
var b = new ScrollDirection({
  dom: document.getElementById('j-div'), up: () => {console.log('dom up')}, down: () => {console.log('dom down')}
})

// a.stop()
// b.stop()
```

### *原生JS*判断是否支持WebP
1. 同步判断

    ```javascript
    function checkWebp () { // Firefox返回false但是却支持WebP…
      try {
        return (document.createElement('canvas').toDataURL('image/webp').indexOf('data:image/webp') === 0)
      } catch (err) {
        return false
      }
    }
    ```

    [CodePen demo](https://codepen.io/realgeoffrey/pen/zMxadK)
2. 异步判断

    ```javascript
    // 'feature' can be one of 'lossy', 'lossless', 'alpha' or 'animation'.
    // 'callback(feature, result)' will be passed back the detection result (in an asynchronous way!)
    function checkWebpFeature (feature, callback) {
      const kTestImages = {
        lossy: 'UklGRiIAAABXRUJQVlA4IBYAAAAwAQCdASoBAAEADsD+JaQAA3AAAAAA',
        lossless: 'UklGRhoAAABXRUJQVlA4TA0AAAAvAAAAEAcQERGIiP4HAA==',
        alpha: 'UklGRkoAAABXRUJQVlA4WAoAAAAQAAAAAAAAAAAAQUxQSAwAAAARBxAR/Q9ERP8DAABWUDggGAAAABQBAJ0BKgEAAQAAAP4AAA3AAP7mtQAAAA==',
        animation: 'UklGRlIAAABXRUJQVlA4WAoAAAASAAAAAAAAAAAAQU5JTQYAAAD/////AABBTk1GJgAAAAAAAAAAAAAAAAAAAGQAAABWUDhMDQAAAC8AAAAQBxAREYiI/gcA'
      }

      const img = new Image()
      img.onload = function () {
        const result = (img.width > 0) && (img.height > 0)
        callback(feature, result)
      }
      img.onerror = function () {
        callback(feature, false)
      }
      img.src = 'data:image/webp;base64,' + kTestImages[feature]
    }


    /* 使用测试 */
    checkWebpFeature('lossless', function (feature, result) {
      console.log(result) // => true/false
    })
    ```

- 纯HTML方式

    ```html
    <picture>
      <source srcset="WebP图片地址" type="image/webp">
      <img src="非WebP图片地址">
    </picture>
    ```

    >`<img>`外嵌套一层`<picture>`，样式要注意，尤其是使用子元素选择器（`>`）时。如：`xx > img`时无法选中，需要`xx > picture > img`。

### *原生JS*DOM展示或消失执行方法（IntersectionObserver）
```javascript
/**
 * DOM展示或消失执行方法（IntersectionObserver）
 * @constructor
 * @param {Object} target - 观察的目标元素
 * @param {Function} [show = () => {}] - 展示时调用
 * @param {Function} [hide = () => {}] - 消失时调用
 * @param {Number} [threshold = 0] - 交叉比例
 * @param {Boolean} [once = false] - 是否仅执行一次，否则执行无数次（仅针对展示。若为true，则展示一次后，展示、消失方法均不再执行）
 * @param {Object} [root = null] - 观察的相对物。null: viewport；祖先元素
 */
function DisplayDom ({ target, show = () => {}, hide = () => {}, threshold = 0.01, once = false, root = null } = {}) {
  threshold = Math.max(Math.min(threshold, 1), 0.01)  // 取值在[0.01, 1]
  try {
    const io = new window.IntersectionObserver(
      (entries) => {
        if (entries[0].intersectionRatio >= threshold) { // 展示
          show()

          if (once) {
            this.stop()
          }
        } else {  // 消失
          hide()
        }
      },
      { threshold: [threshold], root }
    )

    io.observe(target)    // 开始观察

    this.stop = () => {
      io.disconnect()
    }
  } catch (error) {
    console.error(error.message, `\n不支持IntersectionObserver，升级浏览器或代码使用polyfill: https://github.com/w3c/IntersectionObserver`)
  }
}


/* 使用测试 */
var a = new DisplayDom({
  target: document.getElementById('asd'),
  show: () => { console.log('show') },
  hide: () => { console.log('hide') }
})

// a.stop()
```

### *原生JS*执行方法的前/后进行开/关loading
```javascript
async function loadingFetch (func) { // func：方法；若方法返回Promise实例，则完成/失败后关闭loading，否则同步关闭loading
  if (typeof func === 'function') {
    console.log('loading 开始')  // 打开loading

    try {await func()} catch (e) {}

    console.log('loading 结束')  // 关闭loading
  }
}


/* 使用测试 */
// 1s后触发关闭loading
loadingFetch(() => {
  return new Promise((resolve, reject) => {
    setTimeout(reject, 1000)
  })
})

// 同步触发关闭loading
loadingFetch(() => { console.log('同步方法') })
```

### *原生JS*点击下载
1. `<a>`的`download`属性

    >1. `download`指示浏览器下载URL而不是导航到它。
    >2. 下载的文件需要与页面同源。
    >3. 支持多种文件类型。

    `<a href="文件地址" download="文件名.文件类型">点击若同源就下载，不同源还是导航跳转</a>`
2. 下载文本

    >Blob。代码生成文本内容再进行下载。

    ```javascript
    /**
     * 下载文本
     * @param {String} content - 保存的字符串内容
     * @param {String} filename - 文件名（包括后缀）
     */
    function textDownload (content, filename) {
      // 创建隐藏的可下载链接
      const eleLink = document.createElement('a')
      eleLink.download = filename
      eleLink.style.display = 'none'

      // 字符内容转变成Blob对象
      const blob = new Blob([content])
      // 创建Blob URL
      const url = window.URL.createObjectURL(blob)

      eleLink.href = url

      // 触发下载
      document.body.appendChild(eleLink)
      eleLink.click()
      document.body.removeChild(eleLink)

      // 释放Blob URL
      window.URL.revokeObjectURL(url)
    }


    /* 使用测试 */
    textDownload('内容字符串', '文件名.文件类型')
    ```
3. 下载图片

    >1. Canvas。仅支持：png/jpg/webp。
    >2. 需要图片响应头包含正确的Access-Control-Allow-Origin值（CORS）。

    ```javascript
    /**
     * 下载图片
     * @param {String} imgSrc - 图片地址
     * @param {String} [filename = 'image.png'] - 文件名（包括后缀）
     */
    function imageDownload (imgSrc, filename = 'image.png') {
      let img = new Image()
      img.onload = function () {
        download(img)
        img.onload = img.onerror = null
        img = null
      }
      img.onerror = function () {
        img.onload = img.onerror = null
        img = null
      }
      img.crossOrigin = 'Anonymous'
      img.src = imgSrc

      // 下载逻辑
      function download (domImg) {
        // Canvas上绘制图像
        const canvas = document.createElement('canvas')
        canvas.width = domImg.naturalWidth
        canvas.height = domImg.naturalHeight
        const context = canvas.getContext('2d')
        context.drawImage(domImg, 0, 0)

        // 图片转Base64地址
        let base64
        if (filename.endsWith('.png')) {
          base64 = canvas.toDataURL('image/png')
        } else if (filename.endsWith('.webp')) {
          base64 = canvas.toDataURL('image/webp')
        } else {
          base64 = canvas.toDataURL('image/jpeg')
        }

        // 创建隐藏的可下载链接
        const eleLink = document.createElement('a')
        eleLink.download = filename
        eleLink.style.display = 'none'
        eleLink.href = base64

        // 触发下载
        document.body.appendChild(eleLink)
        eleLink.click()
        document.body.removeChild(eleLink)
      }
    }


    /* 使用测试 */
    imageDownload('图片地址', '图片文件名.文件类型')
    ```

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


/* 使用测试 */
var a = new SetInterval(function () {
    console.log(1);

    if (...) {
        a.stop();
    }
}, 1000);

// a.stop();
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


/* 使用测试 */
var a = new RepeatRAF(function () {
    console.log(1);

    if (...) {
        a.stop();
    }
});

// a.stop();
```

---
## jQuery方法

### jQuery滚动加载
1. 以**放置在底部的节点与屏幕的相对距离**作为是否滚动到底部的判断：

    ```html
    <!--
    data-next：加载内容标识（-1：去除滚动加载功能；0：单次不加载）
    data-status：是否正在加载（'ready'：不在加载中、可以进行加载；'busy'：加载中、不允许加载）
    -->
    <div class="j-load" data-next="1" data-status="ready">放置在底部的标记节点，内容添加在此节点前面</div>

    <script>
        var scrollLoadObj = {
            namespace: '', /*事件命名空间 */
            loadMore: function (next) { /*加载逻辑 */
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
                            /* 删除重复内容 */
                            /* 其他具体操作 */

                            newNext = data.next;

                            $load.attr('data-next', newNext);
                        }).fail(function () {
                            console.log('网络错误');
                        }).always(function () {
                            $load.attr('data-status', 'ready');

                            if (/* 某条件 */) {   /* 不再加载 */
                                $(window).off('scroll' + '.' + scrollLoadObj.namespace);
                                /* $load.hide(); */
                            } else {
                                scrollLoadObj.autoLoadMore(newNext);
                            }
                        });
                    }
                } else {
                    $(window).off('scroll' + '.' + scrollLoadObj.namespace);
                    /* $load.hide(); */
                }
            },
            autoLoadMore: function (next) { /* 若html小于视窗则触发加载 */
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
                            if ($load.offset().top <= $(window).scrollTop() + $(window).height()) {  /* 节点顶部在屏幕底部以上 */
                                scrollLoadObj.loadMore($load.attr('data-next'));
                            }
                        }, 200);
                    });
                });
            }
        };


        /* 使用测试 */
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
            namespace: '', /* 事件命名空间 */
            loadMore: function (next) { /* 加载逻辑 */
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
                            /* 删除重复内容 */
                            /* 其他具体操作 */

                            newNext = data.next;

                            $load.attr('data-next', newNext);
                        }).fail(function () {
                            console.log('网络错误');
                        }).always(function () {
                            $load.attr('data-status', 'ready');

                            if (/* 某条件 */) {   /* 不再加载 */
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
            autoLoadMore: function (next) { /* 若html小于视窗则触发加载 */
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
                            if ($(window).height() + $(window).scrollTop() >= $(document).height()) {  /* 文档滚动到底部 */
                                scrollLoadObj.loadMore($load.attr('data-next'));
                            }
                        }, 200);
                    });
                });
            }
        };


        /* 使用测试 */
        scrollLoadObj.init();
    </script>
    ```

>Zepto默认：没有`deferred`的对象、没有`outerHeight`方法。

### jQuery图片延时加载（lazyload）
>1. [lazysizes](https://github.com/aFarkas/lazysizes)
>2. vue的某个懒加载库：[vue-lazyload](https://github.com/hilongjw/vue-lazyload)。

```html
<img src="默认图地址" data-src="真实图地址" data-error="真实图错误后的默认图地址" class="j-img-1">
<img src="默认图地址" data-src-user="真实图地址" data-error-user="真实图错误后的默认图地址" class="j-img-2">

<script>
    /**
     * 图片延时加载
     * @constructor
     * @param {String} className - 触发的类名
     * @param {String} [dataSrc = 'data-src'] - img标签上存放「真实地址」的属性
     * @param {Function} func - 图片加载成功后回调函数，this和形参为图片DOM
     * @param {String} [dataError = 'data-error'] - img标签上存放「真实地址加载失败后显示的地址」的属性
     * @param {Function} errorFunc - 图片加载失败后回调函数，this和形参为图片DOM
     */
    function ImgLazyLoad(className, dataSrc, func, dataError, errorFunc) {
        if (typeof Date.now !== 'function') {
            Date.now = function () {
                return new Date().getTime();
            };
        }

        var _timeoutId,
            _namespace = Date.now(), /* 事件命名空间 */
            _lazyLoad = function (domArr, className, dataSrc, func, dataError, errorFunc) { /* 图片延时加载 */
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

                            /* 防止内存泄露 */
                            newImg.onload = null;
                            newImg.onerror = null;
                            newImg = null;
                        };

                        if (newImg.complete) {    /* 缓存加载 */
                            $this.attr('src', srcReal)
                                .removeAttr(dataSrc)
                                .removeClass(className);

                            if (typeof func === 'function') {
                                func.call(value, value);
                            }

                            /* 防止内存泄露 */
                            newImg.onerror = null;
                            newImg = null;
                        } else {
                            newImg.onload = function () {   /* 新加载 */
                                $this.attr('src', srcReal)
                                    .removeAttr(dataSrc)
                                    .removeClass(className);

                                if (typeof func === 'function') {
                                    func.call(value, value);
                                }

                                /* 防止内存泄露 */
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

                        /* 防止内存泄露 */
                        newImg = null;
                    }
                });
            },
            _getImgArr = function (className, offset) { /* 获取屏幕内dom数组 */
                var $all = $('.' + className),
                    screenTop = $(window).scrollTop(),
                    screenBottom = screenTop + $(window).height(),
                    domArr = [];

                if (typeof offset !== 'number') {
                    offset = 50;
                }

                $all.each(function (index, element) {
                    var elemTop = $(element).offset().top,
                        elemBottom = elemTop + $(element).height(); /* jQuery可以用outerHeight */

                    if (elemTop <= screenBottom + offset && elemBottom >= screenTop - offset) {  /* 节点顶部在屏幕底部以上 && 节点底部在屏幕顶部以下 */
                        domArr.push(element);
                    }
                });

                return domArr;
            },
            _run = function (className, func) {    /* 触发 */
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

        this.stop = function () {    /* 解绑事件绑定 */
            $(window).off('scroll' + '.' + _namespace);
        };

        _init(className, func);
    }


    /* 使用测试 */
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

    // a.stop();
    // b.stop();
</script>
```
[CodePen demo](https://codepen.io/realgeoffrey/pen/gVLZyg)

>滚动事件代理可以代理在`window`或监控图片加载的滚动节点上。

### jQuery节点跟随屏幕滚动而相对静止
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
         * 跟随屏幕滚动而相对静止（fixed），当到达底部某距离时「恢复」滚动
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

          var _namespace = Date.now(),  // 事件命名空间
            _isIE = function (num) {    // 判断ie版本
              var dom = document.createElement('b');

              dom.innerHTML = '<!--[if IE ' + num + ']><i></i><![endif]-->';

              return dom.getElementsByTagName('i').length;
            },
            _followFixed = function () {
              var scollTop = $(window).scrollTop(),
                documentHeight = $(document).height(),
                targetHeight = $target.height();   // jQuery可以用outerHeight

              if (scollTop >= topOffset) {    // 滚动距离超过topOffset
                if (!$target.hasClass(bottomClass)) {   // 没有添加bottomClass
                  if (documentHeight - ($target.offset().top + targetHeight) > bottomOffset) {    // 节点底部距离文档底部距离 > bottomOffet
                    requestAnimationFrame(function () {
                      $target.removeClass(bottomClass).addClass(topClass)
                        .removeAttr('style');
                    });
                  } else if (bottomClass) {   // 超过bottomOffet,并且bottomClass存在
                    requestAnimationFrame(function () {
                      $target.removeClass(topClass).addClass(bottomClass)
                        .css('top', documentHeight - $target.offsetParent().offset().top - targetHeight - bottomOffset);
                    });
                  }
                } else {    // 添加了bottomClass
                  if (scollTop < $target.offset().top) {  // 滚动小于节点
                    requestAnimationFrame(function () {
                      $target.removeClass(bottomClass).addClass(topClass)
                        .removeAttr('style');
                    });
                  }
                }
              } else {
                requestAnimationFrame(function () {
                  $target.removeClass(topClass + ' ' + bottomClass)
                    .removeAttr('style');
                });
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


        /* 使用测试 */
        var a = new FollowFixed($('.target'), $('.target').offset().top, 'z-affix-top', 200, 'z-affix-bottom');

        // a.stop();
    </script>
    ```
    [CodePen demo](https://codepen.io/realgeoffrey/pen/LwbMKE)
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
         * 跟随屏幕滚动而相对静止（margin-top变化）
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

          var namespace = Date.now(), /* 事件命名空间 */
            $target = $(target),
            startOffset = $target.offset().top,
            targetMarginTop = parseInt($target.css('margin-top'), 10) || 0,
            prevMarginBottom = parseInt($target.prev().css('margin-bottom'), 10) || 0,
            defaultMarginTop = Math.max(targetMarginTop, prevMarginBottom),
            maxMarginTop = $(dependent).height() - $(father).height() + defaultMarginTop; // jQuery可以用outerHeight

          $(window).on('scroll' + '.' + namespace, function () {
            var marginTop = $(window).scrollTop() - startOffset + defaultMarginTop;

            if (marginTop > defaultMarginTop) {
              if (marginTop > maxMarginTop) {
                marginTop = maxMarginTop;
              }
            } else {
              marginTop = defaultMarginTop;
            }

            requestAnimationFrame(function () {
              $target.css({ 'margin-top': marginTop });
            });
          });

          this.stop = function () {
            $target.css({ 'margin-top': targetMarginTop });
            $(window).off('scroll' + '.' + namespace);
          };
        }


        /* 使用测试 */
        var a = new FollowMarginTop('.target', '.father', '.dependent');

        // a.stop();
    </script>
    ```
    [CodePen demo](https://codepen.io/realgeoffrey/pen/xvRmov)

### jQuery弹出toast
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
                display: inline-block;
                *display: inline;
                *zoom: 1;
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


        /* 使用测试 */
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


        /* 使用测试 */
        alertToast('<span style="color: red;">red</span>', '哈哈');
    </script>
    ```

### jQuery全选、取消全选
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

### jQuery点击指定区域以外执行函数
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
            if (!$dom.is(e.target) && $dom.has(e.target).length === 0) {    /* 点击不在指定区域内 */
                $(document).off('click.' + namespace);

                if (typeof callback === 'function') {
                    callback();
                }
            }
        });
    }


    /* 使用测试 */
    beyongOneAct(
      $('.dom1,#dom2'),
      function () {
        console.log('点击区域外');
      },
      1000
    );
    ```
    [CodePen demo](https://codepen.io/realgeoffrey/pen/WVoLVM)
2. Zepto

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

            if (!withinArea) {    /* 点击不在指定区域内 */
                $(document.body).off('click.' + namespace);

                if (typeof callback === 'function') {
                    callback();
                }
            }
        });
    }


    /* 使用测试 */
    beyongOneAct(
      $('.dom1,#dom2'),
      function () {
        console.log('点击区域外');
      },
      1000
    );
    ```
    [CodePen demo](https://codepen.io/realgeoffrey/pen/BXQMbq)

### jQuery hover展示内容并且可跨越间隙到内容
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
[CodePen demo](https://codepen.io/realgeoffrey/pen/QeGYPP)

### jQuery启动、暂停CSS动画
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

        var _isStop = false, // 停止动画flag
            _namespace = Date.now(), // 事件命名空间
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


    /* 使用测试 */
    var a = new AnimationHover('.j-dom-1', 'z-hover');
    var b = new AnimationHover('.j-dom-2', 'z-hover');

    // a.stop;
    // b.stop;
</script>
```
[CodePen demo](https://codepen.io/realgeoffrey/pen/MNbZzB)

### jQuery获取`HTTP response header`信息
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
        url: window.location.href,
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

### jQuery模拟手机旋转（使页面都以「横屏」展示）
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
     * @param {String} className - 旋转类
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
            _portraitFunc = function (selector, className) {    /* 屏幕高度>宽度（竖屏），增加「顺时针旋转90度的类」 */
                var $dom = $(selector);

                if ($(window).height() > $(window).width()) {
                    $dom.addClass(className);
                } else {
                    $dom.removeClass(className);
                }
            },
            _resizeFunc = function (selector) {   /* 设置高宽的值（边长较长的一边设置为宽度，较短的设置为高度） */
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


    /* 使用测试 */
    var a = new ReversalAct('#j-dom-1, #j-dom-2', 'z-reversal');

    // a.stop();
</script>
```
>若对不是全屏的节点使用旋转函数，则需要给节点设置：`width: 宽度 !important;height: auto !important;`。
