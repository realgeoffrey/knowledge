# JS实用方法

## 目录
1. 根据UA或浏览器特性判断

    1. [判断所在系统](#原生js判断所在系统)
    1. [判断Android版本号](#原生js判断android版本号)
    1. [判断iOS版本号](#原生js判断ios版本号)
    1. [判断移动平台](#原生js判断移动平台)
    1. [判断ie6、7、8、9版本](#原生js判断ie6789版本)
    1. [判断ie所有版本](#原生js判断ie所有版本)
1. `键-值`操作

    1. [判断是否存在某cookie](#原生js判断是否存在某cookie)
    1. [获取URL相关信息](#原生js获取url相关信息)
    1. [在URL末尾修改search键-值](#原生js在url末尾修改search键-值)
1. 事件相关

    1. [绑定、解绑事件](#原生js绑定解绑事件)
    1. [阻止冒泡和阻止浏览器默认行为](#原生jsjquery阻止冒泡和阻止浏览器默认行为)
    1. [事件代理](#原生js事件代理)
    1. [实现判断按下具体某按键](#原生jsjquery实现判断按下具体某按键)
    1. [拖拽和放下](#原生js拖拽和放下)
    1. [触摸屏模拟点击事件（消除「延时300毫秒后才触发click事件」，使点击事件提前触发）](#原生js触摸屏模拟点击事件消除延时300毫秒后才触发click事件使点击事件提前触发)
    1. [判断事件在浏览器是否存在](#原生js判断事件在浏览器是否存在)
    1. [根据滚动方向执行函数](#原生js根据滚动方向执行函数)
1. 数字操作

    1. [科学计数法转换成字符串的数字](#原生js科学计数法转换成字符串的数字)
    1. [不同进制数互相转换](#原生js不同进制数互相转换)
    1. [选取范围内随机值](#原生js选取范围内随机值)
    1. [选取范围内多个随机值](#原生js选取范围内多个随机值)
    1. [阿拉伯数字转中文](#原生js阿拉伯数字转中文)
1. 字符串操作

    1. [转化为Unicode、反转字符串、字符串长度、所占字节数](#原生js转化为unicode反转字符串字符串长度所占字节数)
    1. [字符串匹配、替换](#原生js字符串匹配替换)
    1. [分割字符串](#原生js分割字符串)
    1. [数字增加分隔符](#原生js数字增加分隔符)
    1. [产生随机数](#原生js产生随机数)
    1. [判断版本号是否在某个版本区间（纯数字）](#原生js判断版本号是否在某个版本区间纯数字)
    1. [判断检索内容是否在被检索内容的分隔符间](#原生js判断检索内容是否在被检索内容的分隔符间)
    1. [格式化文件大小](#原生js格式化文件大小)
    1. [单词首字母大写](#原生js单词首字母大写)
    1. [文件扩展名](#原生js文件扩展名)
1. 数组操作

    1. [数组去重（项为对象）](#原生js数组去重项为对象)
    1. [数组去重](#数组去重)
    1. [数组删去某值](#数组删去某值)
    1. [数组的某项插入某位置](#数组的某项插入某位置)
    1. [声明某长度并设定值的数组](#声明某长度并设定值的数组)
1. 功能

    1. [用请求图片作log统计](#原生js用请求图片作log统计)
    1. [验证邮箱有效性](#原生js验证邮箱有效性)
    1. [创建兼容的XHR对象](#原生js创建兼容的xhr对象)
    1. [动态添加脚本、样式](#原生js动态添加脚本样式)
    1. [获取星座](#原生js获取星座)
    1. [加入收藏夹](#原生js加入收藏夹)
    1. [从字符串中获取绝对路径](#原生js从字符串中获取绝对路径)
    1. [不传递请求头的Referrer进行跳转](#原生js不传递请求头的referrer进行跳转)
    1. [格式化接口返回的数据](#原生js格式化接口返回的数据)
    1. [判断是否支持WebP](#原生js判断是否支持webp)
    1. [执行方法的前/后进行开/关loading](#原生js执行方法的前后进行开关loading)
    1. [点击下载](#原生js点击下载)
    1. [写入剪切板](#原生js写入剪切板)
    1. [React组件业务类似Promise.all的效果](#react组件业务类似promiseall的效果)
    1. [判断是否有循环引用](#原生js判断是否有循环引用)
1. DOM相关

    1. [DOM展示或消失执行方法（IntersectionObserver）](#原生jsdom展示或消失执行方法intersectionobserver)
    1. [判断是否为`Node`、是否为`Element`](#原生js判断是否为node是否为element)
    1. [输入框光标位置的获取和设置](#原生js输入框光标位置的获取和设置)
    1. [文本选区覆盖某DOM的文本范围](#原生js文本选区覆盖某dom的文本范围)
    1. [针对WAP的阻止滚动冒泡（仅DOM）](#原生js针对wap的阻止滚动冒泡仅dom)
    1. [获取滚动条宽度（或高度）](#原生js获取滚动条宽度或高度)
    1. [展示页面帧数](#原生js展示页面帧数)
    1. [默认图组件](#react默认图组件)
    1. [溢出文本的省略](#原生js溢出文本的省略)
    1. [九宫格抽奖](#九宫格抽奖)
1. 任务执行

    1. [sleep](#sleep)
    1. [轮询](#原生js轮询)
    1. [节流函数](#原生js节流函数)
    1. [用`setTimeout`模拟`setInterval`](#原生js用settimeout模拟setinterval)
    1. [`requestAnimationFrame`的递归](#原生jsrequestanimationframe的递归)
    1. [`requestAnimationFrame`模拟`setTimeout`和`setInterval`](#原生jsrequestanimationframe模拟settimeout和setinterval)
1. 算法思路

    1. [判断对象是否为空](#原生js判断对象是否为空)
    1. [无缝轮播](#无缝轮播)
    1. [获取某一位的数字](#获取某一位的数字)
1. Node.js相关

    1. [确保文件夹存在](#确保文件夹存在)
1. <details>

    <summary>jQuery方法</summary>

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
    </details>

---
## 根据UA或浏览器特性判断
>更全面判断所在系统、浏览器：[bowser](https://github.com/lancedikson/bowser)。

### *原生JS*判断所在系统
```js
/**
 * 判断所在系统
 * @param {String} [ua = window.navigator.userAgent] - 用户代理
 * @param {String} [pf = window.navigator.platform] - 系统平台类型
 * @returns {String} os - 系统名：'iOS'|'Android'|'Windows Phone'|'macOS'|'Win2000'|'WinXP'|'Win2003'|'WinVista'|'Win7'|'Win10'|'Windows'|'Unix'|'Linux'
 */
function detectOS (ua = window.navigator.userAgent, pf = window.navigator.platform) {
  let os = ''

  if (/iPhone|iPad|iPod|iOS/.test(ua)) {    // fixme: 注意iOS13之后的iPad可能会判断为macOS
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

### *原生JS*判断Android版本号
```js
function versionAndroid (ua = window.navigator.userAgent) {
  return ua.toLowerCase().match(/android (.*?);/)?.[1] || '';
}
```

### *原生JS*判断iOS版本号
```js
function versionIOS (ua = window.navigator.userAgent) {
  return ua.toLowerCase().match(/cpu iphone os (.*?) like mac os/)?.[1] || '';
}
```

### *原生JS*判断移动平台
```js
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

```js
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
```js
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

---
## `键-值`操作

### *原生JS*判断是否存在某cookie
```js
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
```js
/**
 * 获取URL相关信息
 * @param {String} [url = window.location.href] - URL
 * @returns {Object} location - 包括：href、protocol、hostname、port、pathname、search、searchObj、hash 的对象。若不是合法URL，返回false
 */
function getLocation(url = window.location.href) {
  try {
    /* 为了方便阅读 */
    const protocolStr = /^(?:([A-Za-z]+):)?/.source
    const slashStr = /\/*/.source
    const hostnameStr = /([0-9A-Za-z.-]+)/.source
    const portStr = /(?::(\d+))?/.source
    const pathnameStr = /(\/[^?#]*)?/.source
    const searchStr = /(?:\?([^#]*))?/.source
    const hashStr = /(?:#(.*))?$/.source

    const regex = new RegExp(protocolStr + slashStr + hostnameStr + portStr + pathnameStr + searchStr + hashStr, 'g');
    const regexArr = regex.exec(url);
    const keyArr = [ 'href', 'protocol', 'hostname', 'port', 'pathname', 'search', 'hash' ];
    const location = { 'searchObj': {} };

    keyArr.forEach(function (item, index) {
      location[item] = regexArr[index] || ''
    })

    const searchArr = location['search'].split('&')

    for (let i = 0; i < searchArr.length; i++) {
      if (searchArr[i] !== '') {
        const searchItem = searchArr[i].split('=')
        const key = searchItem.shift()
        const value = searchItem.join('=')
        if (!Object.prototype.hasOwnProperty.call(location['searchObj'], key)) {  // 用第一次出现的
          location['searchObj'][key] = value
        }
      }
    }

    return location
  } catch (e) {  // 不是合法URL
    return false
  }
}
```

>参考：[用正则表达式分析 URL](https://harttle.land/2016/02/23/javascript-regular-expressions.html)。

>1. 获取某search值：
>
>    ```js
>    /**
>     * 获取某search值
>     * @param {String} checkKey - search的key
>     * @param {String} [search = window.location.search] - search总字符串（不校验）
>     * @returns {String|Boolean} - search的value 或 不存在false
>     */
>    function getSearchValue (checkKey, search = window.location.search) {
>      checkKey = checkKey.toString()
>
>      if (search.slice(0, 1) === '?') {
>        search = search.slice(1)
>      }
>
>      for (let i = 0, searchArr = search.split('&'); i < searchArr.length; i++) {
>        if (searchArr[i] !== '') {
>          const tempArr = searchArr[i].split('=')
>          const key = tempArr.shift()
>          const value = tempArr.join('=')
>
>          if (key === checkKey) {
>
>            return decodeURIComponent(value)
>          }
>        }
>      }
>
>      return false
>    }
>    ```
>2. 拼接接口URL时，可以在路由最后添加`?`并且加上一些固定不变的search参数，在使用URL时候都以`&参数=值`的形式添加额外参数：
>
>    >`xxx/xxx?&a=1`可以正常解析
>
>    ```js
>    const api1 = 'xxx/xxx?'
>    const api2 = 'xxx/xxx?v=1.0'
>
>    // 使用时
>    url1 = api1 + '&a=1' + '&b=2' + '&c=3'
>    url2 = api2 + '&a=1' + '&b=2' + '&c=3'
>    ```
>3. URL携带JSON数据：
>
>    search某key的值为`encodeURIComponent(JSON.stringify(JSON数据))`，获取某key值后`JSON.parse(decodeURIComponent(前面的值))`。

### *原生JS*在URL末尾修改search键-值
1. 批量修改（未加`encodeURIComponent`）

    >对象转换为`a=1&b=2`：`Object.entries(对象).map((val) => val.join('=')).join('&')`。

    ```ts
    /**
     * 在URL末尾修改search键-值
     * @param {String} [url = window.location.href] - URL
     * @param {Object} searchObj - 修改的search键-值（若key-value的value设置为`false`，则删除这个key）
     * @returns {String} - 修改完毕的URL
     */
    function changeUrlSearch(url: string = window.location.href, searchObj: Record<string, string | false> = {}): string {
      if (Object.keys(searchObj).length === 0) {
        // 空对象不处理
        return url;
      }

      const hashIndex = url.includes("#") ? url.indexOf("#") : url.length; // "#"所在的字符串位置索引
      const urlWithoutHash = url.slice(0, hashIndex); // 去除hash后的url
      const searchIndex = urlWithoutHash.indexOf("?"); // "?"所在的字符串位置索引

      // 把原始search值写入对象
      const originalSearchObj: Record<string, string> = {};
      if (searchIndex !== -1) {
        const search = urlWithoutHash.slice(searchIndex + 1); // search值（不包括 ?）

        // 写入已存在search的键-值
        const searchArr = search.split("&");
        for (let i = 0; i < searchArr.length; i++) {
          if (searchArr[i] !== "") {
            const searchItem = searchArr[i].split("=");
            const key = searchItem.shift() as string;
            const value = searchItem.join("="); // 兜底有些值包含"="
            if (!Object.prototype.hasOwnProperty.call(originalSearchObj, key)) {  // 用第一次出现的
              originalSearchObj[key] = value;
            }
          }
        }
      }

      // 合并原始search和新增search（同名覆盖）
      const newSearchObj: Record<string, string | false> = Object.assign({}, originalSearchObj, searchObj);

      // 生成新的合并过后的search字符串
      const newSearch = Object.entries(newSearchObj)
        // 值为`false`的key被删除
        .filter(([key, value]) => {
          return value !== false;
        })
        .map((val) => {
          return val.join("=");
        })
        .join("&");

      const hash = url.slice(hashIndex); // 原始hash

      let urlWithoutSearch; // 去除search、hash后的url
      if (searchIndex !== -1) {
        urlWithoutSearch = urlWithoutHash.slice(0, searchIndex);
      } else {
        urlWithoutSearch = urlWithoutHash;
      }

      return urlWithoutSearch + (newSearch ? `?${newSearch}` : "") + hash;
    }
    ```
2. <details>

    <summary>单个修改</summary>

    ```js
    /**
     * 在URL末尾修改search键-值
     * @param {String} url - URL
     * @param {String} name - 名
     * @param {String|Boolean} value - 值（若传`false`则删除属性名）
     * @returns {String} - 添加完毕的URL
     */
    function changeUrlSearch (url, name, value) {
      if (!name) {
        return url
      }

      var hashIndex = url.includes('#') ? url.indexOf('#') : url.length
      var urlWithoutHash = url.slice(0, hashIndex)
      var hash = url.slice(hashIndex)
      var searchIndex = urlWithoutHash.indexOf('?')

      if (searchIndex === -1) {
        if (value === false) {
          return url
        }
        return urlWithoutHash + '?' + encodeURIComponent(name) + '=' + encodeURIComponent(value) + hash
      } else if (searchIndex === urlWithoutHash.length - 1) {
        if (value === false) {
          return url.slice(0, urlWithoutHash.length - 1) + hash
        }
        return urlWithoutHash + encodeURIComponent(name) + '=' + encodeURIComponent(value) + hash
      } else {
        const urlWithoutSearch = urlWithoutHash.slice(0, searchIndex)
        const search = urlWithoutHash.slice(searchIndex + 1)

        const originalSearchObj = {}

        // 写入已存在search的键-值
        const searchArr = search.split('&')
        for (let i = 0; i < searchArr.length; i++) {
          if (searchArr[i] !== '') {
            const searchItem = searchArr[i].split('=')
            const key = searchItem.shift()
            const value = searchItem.join('=')
            if (!Object.prototype.hasOwnProperty.call(originalSearchObj, key)) {  // 用第一次出现的
              originalSearchObj[key] = value
            }
          }
        }

        let newSearch
        if (value === false) {
          delete originalSearchObj[name]
          newSearch = Object.entries(originalSearchObj)
            .map((val) => {
              return val.join('=')
            })
            .join('&')
        } else {
          const newSearchObj = Object.assign({}, originalSearchObj, {
            [encodeURIComponent(name)]: encodeURIComponent(value)
          })
          newSearch = Object.entries(newSearchObj)
            .map((val) => {
              return val.join('=')
            })
            .join('&')
        }

        return urlWithoutSearch + (newSearch ? `?${newSearch}` : '') + hash
      }
    }
    ```
    </details>

---
## 事件相关

### *原生JS*绑定、解绑事件
```js
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

        ```js
        function stopBubble(e) {
            if (e && e.stopPropagation) {
                e.stopPropagation();
            } else {
                window.event.cancelBubble = true;
            }
        }
        ```
    2. jQuery

        ```js
        $('...').on('...', function (e) {
            e.stopPropagation();
        });
        ```
2. 阻止默认行为

    1. *原生JS*

        ```js
        function stopDefault(e) {
            if (e && e.preventDefault) {
                e.preventDefault();
            } else {
                window.event.returnValue = false;
            }
        }
        ```
    2. jQuery

        ```js
        $('...').on('...', function (e) {
            e.preventDefault();
        });
        ```
3. 阻止冒泡 && 阻止默认行为

    1. *原生JS*

        ```js
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

        ```js
        $('...').on('...', function () {

            return false;
        });
        // 或简写：$('...').on('...', false);
        ```

### *原生JS*事件代理
```js
dom.addEventListener('事件名', function (e) {
  const event = e || window.event
  const target = event.target || event.srcElement // 兼容ie8-

  // target为目标元素（捕获的终点、冒泡的起点）；可以用dom.matches(CSS选择器)判断是否是选择器
  // 对target满足的元素进行操作
})
```

### *原生JS*、jQuery实现判断按下具体某按键
1. `KeyboardEvent.key`

    >[MDN：KeyboardEvent.key](https://developer.mozilla.org/zh-CN/docs/Web/API/KeyboardEvent/key/Key_Values)、[W3C:KeyboardEvent.key](https://www.w3.org/TR/uievents-key/)。

    1. *原生JS*

        ```js
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

        ```js
        $(输入框选择器).on('keydown', function (e) {
            if (e.key === 'Enter') {   /* 查询键值表 例：'Enter' -> 换行 */
                /* 具体操作... */

                return false;   // 阻止冒泡&阻止默认行为
            }
        });
        ```
2. ~~`KeyboardEvent.which/keyCode/charCode`~~（已废弃）

    1. *原生JS*

        ```js
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

        ```js
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

    ```js
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

    ```js
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
```js
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
```js
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

### *原生JS*根据滚动方向执行函数
```js
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

---
## 数字操作

### *原生JS*科学计数法转换成字符串的数字
```js
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

### *原生JS*不同进制数互相转换
```js
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
>可以直接用库：[chancejs](https://github.com/chancejs/chancejs)，e.g. `chance.integer({ min: -20, max: 20 })`、`chance.floating({ min: 0, max: 100, fixed: 8 })`。

>注意：
>
>1. 检查不同语言原始返回的随机值两边端点开闭情况——不同的开闭区间影响最终算法。
>2. 获取到的每个整数的概率是否均等——用 向下/向上取整 替代四舍五入可以使概率均等。

```js
/**
 * 选取范围内随机值（仅整数）
 * @param {Number} min - 下限（或上限）
 * @param {Number} max - 上限（或下限）
 * @returns {Number} - 上下限区间内的随机值（闭区间，[下限, 上限]）
 */
function randomFrom(min, max) {
    if (min > max) [min, max] = [max, min];
    return Math.floor(Math.random() * (max - min + 1) + min);
}
```
><details>
><summary><code>Math.random()</code>返回<code>[0,1)</code>。</summary>
>
>假设返回的值的开闭区间改变，需要实现整数闭区间的[下限, 上限]：
>
>0. JS返回的是：`[0,1)`，则`Math.floor(Math.random() * (max - min + 1) + min)`。
>1. 若返回的是：`(0,1)`，则需要改为`Math.floor(Math.random() * (max - min + 1) + min);`。
>2. 若返回的是：`(0,1]`，则需要改为`Math.ceil(Math.random() * (max - min + 1) + min - 1);`。
>3. 若返回的是：`[0,1]`，则需要改为`Math.round(Math.random() * (max - min) + min);`。
></details>

```js
/**
 * 选取范围内随机值（仅小数）
 * @param {Number} min - 下限（或上限）
 * @param {Number} max - 上限（或下限）
 * @returns {Number} - 上下限区间内的随机值（前闭后开区间，[下限, 上限)）
 */
function randomFrom(min, max) {
    if (min > max) [min, max] = [max, min];
    return Math.random() * (max - min) + min;
}
```

><details>
><summary>获取小数位</summary>
>
>```js
>// 获取小数位（小数点后数字个数）
>function getDecimalPlaces(num) {
>  const str = String(num);
>  if (str.includes('.')) return str.split('.')[1].length;
>  return 0;
>}
>```
></details>

><details>
><summary>mock数值</summary>
>
>```js
>import Decimal from 'decimal.js'
>
>// 返回随机数，toDecimalPlaces 保留小数位数
>export function randomNum(num = 0, toDecimalPlaces = getDecimalPlaces(num)) {
>  return Decimal(randomFromDec(0, num)).toDecimalPlaces(toDecimalPlaces).toNumber()
>}
>// 获取小数位（小数点后数字个数）
>function getDecimalPlaces(num) {
>  const str = String(num)
>  if (str.includes('.')) return str.split('.')[1].length
>  return 0
>}
>// 选取范围内随机值（仅小数）
>function randomFromDec(min, max) {
>  if (min > max) [min, max] = [max, min]
>  return Math.random() * (max - min) + min
>}
>```
></details>

### *原生JS*选取范围内多个随机值
```js
/**
 * 选取范围内多个随机值
 * @param {Number} min - 下限（或上限）
 * @param {Number} max - 上限（或下限）
 * @param {Number} [num = 1] - 返回随机数的数量
 * @returns {Array|Boolean} - 上下限区间内的num个随机值组成的数组（闭区间，[下限, 上限]） 或 false（错误）
 */
function randomsFrom(min, max, num = 1) {
  if (min > max) [min, max] = [max, min];

  const count = max - min + 1;

  const arr = Array.from({length: count}).map(
    (item, index) => index + min
  );

  if (num <= 0 || num > count) {
    return false;
  } else if (num === count) {
    return arr;
  } else {
    const outs = [];
    while (num > outs.length) {
      outs.push(...arr.splice(Math.floor(Math.random() * arr.length), 1));
    }
    return outs.sort((a, b) => a - b);
  }
}
```

### *原生JS*阿拉伯数字转中文
```js
function intToChinese(num = 0) {
  // 不要超过最大安全数字，也就是 九千万亿多（其实是 亿亿之后的单位不想查了）
  if (!Number.isSafeInteger(num)) {
    return new Error(`超过${Number.MAX_SAFE_INTEGER}(${intToChinese(Number.MAX_SAFE_INTEGER)})`);
  }
  if (isNaN(num)) return "零";

  const CHINESE_NUMBERS = [ "零", "一", "二", "三", "四", "五", "六", "七", "八", "九" ];
  const CHINESE_UNITS = [ "", "十", "百", "千", "万", "十", "百", "千", "亿", "十", "百", "千", "万", "十", "百", "千", "亿" ];

  // 逆序一下，数组第一个项是个位数，第二个项是十位数，以此类推
  const numStr = num.toString().split("").reverse();
  let result = "";
  for (let i = 0; i < numStr.length; i++) {
    result = CHINESE_UNITS[i] + result; // 单位
    result = CHINESE_NUMBERS[numStr[i]] + result; // 值
  }

  // 处理中文数字的特殊情况
  result = result.replace(/零(千|百|十)/g, "零").replace(/十零/g, "十");
  result = result.replace(/零+/g, "零");
  result = result.replace(/零亿/g, "亿").replace(/零万/g, "万");
  result = result.replace(/亿万/g, "亿");
  result = result.replace(/零+$/, "");
  result = result.replace(/^一十/g, "十");

  return result;
}
```

---
## 字符串操作

### *原生JS*转化为Unicode、反转字符串、字符串长度、所占字节数
>注意：Unicode码点大于`\uFFFF`（65535）的字符，如：`'💩'.codePointAt(0) // 128169`

1. 转化为Unicode

    ```js
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

    ```js
    // 反转字符串
    function reverseWords (words) {
      return Array.from(words).reverse().join('')

      // 或：return [...words].reverse().join('');
    }


    /* 使用测试 */
    console.log(reverseWords('💩哈©')) // => ©哈💩
    ```
3. 字符串长度

    ```js
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

    ```js
    /**
     * 所占字节数
     *
     * UTF-8 一种可变长度的Unicode编码格式，使用一至四个字节为每个字符编码（Unicode在范围 D800-DFFF 中不存在任何字符）
     * 000000 - 00007F(128个代码)      0zzzzzzz(00-7F)                             一个字节
     * 000080 - 0007FF(1920个代码)     110yyyyy(C0-DF) 10zzzzzz(80-BF)             两个字节
     * 000800 - 00D7FF
     * 00E000 - 00FFFF(61440个代码)    1110xxxx(E0-EF) 10yyyyyy 10zzzzzz           三个字节
     * 010000 - 10FFFF(1048576个代码)  11110www(F0-F7) 10xxxxxx 10yyyyyy 10zzzzzz  四个字节
     *
     * UTF-16 编码65535以内使用两个字节编码，超出65535的使用四个字节（JS内部，字符储存格式是：UCS-2——UTF-16的子级；`<input>`的`maxlength/minlength`以UTF-16码元计算）
     * 000000 - 00FFFF  两个字节
     * 010000 - 10FFFF  四个字节
     * e.g. <input maxlength="3">：字符是65535以内的占用1，超过65535占用2。因此可以输入上限：'aaa'、'哈哈哈'、'𦤎1'、'💩1'
     *
     * GBK(ASCII的中文扩展) 除了0~126编号是1个字节之外，其他都2个字节（超过65535会由2个字显示）
     * GB 2312、GB 18030 与 GBK相同实现
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
    console.log(sizeofByte('𦤎'), sizeofByte('💩'), sizeofByte('哈'), sizeofByte('©')) // => 4 4 2 1
    ```

### *原生JS*字符串匹配、替换
```js
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
```js
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
console.log(split('💩1a💩哈。.↑'))  // => ["💩", "1", "a", "💩", "哈", "。", ".", "↑"]
```

### *原生JS*数字增加分隔符
```ts
// 每n位数添加一个分隔符
export function numberSeparator({
  num,
  gap = 3,
  separator = ","
}: {
  num: number;
  gap?: number;
  separator?: string;
}): string {
  const strSplit = num.toString().split(".");
  const integer = strSplit[0];
  const decimal = strSplit[1] ? `.${strSplit[1]}` : "";

  const reg = new RegExp(`\\B(?=(\\d{${gap}})+(?!\\d))`, "g");
  return integer.replace(reg, separator) + decimal;
}


/* 使用测试 */
numberSeparator({ num: 12345.123 })  // -> '12,345.123'
```

### *原生JS*产生随机数
```js
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

### *原生JS*判断版本号是否在某个版本区间（纯数字）
```js
/**
 * 判断版本号是否在某个版本区间（纯数字）
 * @param {Number|String} version - 判断的版本号
 * @param {Number|String} base - 版本区间或版本（如：123 或 123- 或 -123 或 123-456）
 * @param {String} [separator = '-'] - 版本区间
 * @returns {Boolean} - 是否在区间
 */
function isVersionIncluded (version, base, separator = '-') {
  version = String(version)
  base = String(base)

  if (version === base) {
    return true
  } else {
    const vArr = base.split(separator)
    if (vArr.length === 1) {
      return false
    } else {
      version = parseInt(version)
      if (vArr[0] === '') {
        if (vArr[1] && version <= parseInt(vArr[1])) {
          return true
        }
      } else if (vArr[1] === '') {
        if (vArr[0] && version >= parseInt(vArr[0])) {
          return true
        }
      } else {
        if ((vArr[0] && version >= parseInt(vArr[0])) && (vArr[1] && version <= parseInt(vArr[1]))) {
          return true
        }
      }
    }
  }

  return false
}


/* 使用测试 */
console.log(isVersionIncluded(123, '123'), '=> true')
console.log(isVersionIncluded(123, '-22'), '=> false')
console.log(isVersionIncluded(123, '-222'), '=> true')
console.log(isVersionIncluded(123, '123-'), '=> true')
console.log(isVersionIncluded(123, '124-'), '=> false')
console.log(isVersionIncluded(123, '1-122'), '=> false')
console.log(isVersionIncluded(123, '123-200'), '=> true')
console.log(isVersionIncluded('asd', '123-200'), '=> false')
console.log(isVersionIncluded('1', '5-6'), '=> false')
```

### *原生JS*判断检索内容是否在被检索内容的分隔符间
```js
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


/* 使用测试 */
isKeyInStr('d','abc|d|efg123','|')  // -> true
```

### *原生JS*格式化文件大小
```js
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
```js
function upperCaseWord(str) {

    return str.replace(/\b[a-zA-Z]/g, function (match) {

        return match.toUpperCase();
    });
}
```

### *原生JS*文件扩展名
```js
/**
 * 返回文件扩展名（注意，没有进行toLowerCase）：简单实现Node.js的path.extname，未处理非一般文件名的情况
 * @param {String} filename - 文件名字符串
 * @param {Boolean} [needSeparator = true] - 返回内容是否包含分隔符.
 * @returns {String} - 文件扩展名
 */
function getFileExtension(filename, needSeparator = true) {
  const firstDotIndex = filename.indexOf('.');
  const lastDotIndex = filename.lastIndexOf('.');

  if ((filename.startsWith('.') && firstDotIndex === lastDotIndex) || firstDotIndex === -1) {
    // 处理特殊情况
    return '';
  }

  return filename.slice(needSeparator ? lastDotIndex : lastDotIndex + 1);
}


/* 使用测试 */
const path = require('node:path');
console.log(`期望输出："${path.extname('')}"。`, getFileExtension('') === path.extname(''));
console.log(`期望输出："${path.extname('.')}"。`, getFileExtension('.') === path.extname('.'));
console.log(`期望输出："${path.extname('ABC.')}"。`, getFileExtension('ABC.') === path.extname('ABC.'));
console.log(`期望输出："${path.extname('ABC')}"。`, getFileExtension('ABC') === path.extname('ABC'));
console.log(`期望输出："${path.extname('.ABC')}"。`, getFileExtension('.ABC') === path.extname('.ABC'));
console.log(`期望输出："${path.extname('1.ABC')}"。`, getFileExtension('1.ABC') === path.extname('1.ABC'));
console.log(`期望输出："${path.extname('1.2.3.a.b.ABC')}"。`, getFileExtension('1.2.3.a.b.ABC') === path.extname('1.2.3.a.b.ABC'));
console.log(`期望输出："${path.extname('.ABC.md')}"。`, getFileExtension('.ABC.md') === path.extname('.ABC.md'));
```

---
## 数组操作

### *原生JS*数组去重（项为对象）
```js
/**
 * 获取对象指定深度属性（https://lodash.com/docs#get）
 * @param {Object} source - 要处理的对象
 * @param {Array} path - 路径深度
 * @returns result - 属性值
 */
function get(source, path) {
  let result = source;
  for (const key of path) {
    if (Object.hasOwn(result, key)) {
      result = result[key];
    } else {
      return undefined;
    }
  }
  return result;
}

/**
 * 数组去重（项为对象）
 * @param {Array} arr - 要处理的数组
 * @param {Array} path - 路径深度
 * @returns 去重后的数组
 */
function deduplicateArray (arr, path = []) {
  if (path.length > 0) {
    const newArr = [];
    return arr.filter((data) => {
      const id = get(data, path);
      if (newArr.includes(id)) {
        return false;
      } else {
        newArr.push(id);
        return true;
      }
    });
  } else {
    return Array.from(new Set(arr));
  }
}


/* 使用测试 */
deduplicateArray( // [id从1到4的对象]
  [
    { id: 1, text: "aaaaa" },
    { id: 2, text: "bbbb" },
    { id: 3, text: "cccc" },
    { id: 1, text: "dddd" },
    { id: 4, text: "eeee" }
  ],
  ["id"]
);
deduplicateArray([1, 2, 3, 1, 4]);    // [1, 2, 3, 4]
```

### 数组去重
>来自：[JavaScript 数组去重](https://github.com/hanzichi/underscore-analysis/issues/9)。

1. 定义一个空数组变量，遍历需要去重的数组：若项的值不存在新数组中，则放入新数组；若已经存在，则丢弃。

    >重复的项取最前的放入新数组。

    1. 使用`Array.prototype.indexOf`、`Array.prototype.filter`

        ```js
        function uniqueArr (arr) {
          return arr.filter((item, index, array) => array.indexOf(item) === index)
        }
        ```
    2. 不使用~~Array.prototype.indexOf~~、~~Array.prototype.filter~~

        ```js
        function uniqueArr(arr) {
            var newArr = [],
                i, j, iLen, jLen, item;

            for (i = 0, iLen = arr.length; i < iLen; i++) {
                item = arr[i];

                for (j = 0, jLen = newArr.length; j < jLen; j++) {
                    if (newArr[j] === item) {
                        break;
                    }
                }

                if (j === jLen) {
                    newArr.push(item);
                }
            }

            return newArr;
        }
        ```
    >时间复杂度：O(n^2)。
2. 定义一个空数组变量，遍历需要去重的数组：若项的值在原数组中唯一，则放入新数组；若不唯一，丢弃并继续向后遍历。

    >重复的项取最后的放入新数组。

    ```js
    function uniqueArr(arr) {
        var newArr = [],
            len = arr.length,
            i, j;

        for (i = 0; i < len; i++) {
            for (j = i + 1; j < len; j++) {
                if (arr[i] === arr[j]) {    // 若发现相同元素，则i自增并且进入下一个数的循环比较
                    i += 1;
                    j = i;
                }
            }

            newArr.push(arr[i]);
        }

        return newArr;
    }
    ```
    >时间复杂度：O(n^2)。
3. 先排序原始数组（需要额外排序算法，否则只能处理Number型数据），第一项加入，之后每个项对比前一个项：若不同，则加入；若相同，则丢弃。

    ```js
    function uniqueArr (arr) {
      return arr.concat().sort().filter((item, index, array) => !index || item !== array[index - 1])
    }
    ```
    >时间复杂度：O(n) + 数组排序。
4. 用对象（哈希表）去重（只能处理Number型数据）。

    ```js
    function uniqueArr (arr) {
      const obj = {}

      return arr.filter((item) => obj.hasOwnProperty(item) ? false : (obj[item] = true))
    }
    ```
    >时间复杂度：O(n)。
5. ES6的`Set`

    ```js
    function uniqueArr(arr) {
        return Array.from(new Set(arr));
        // 或：return [...new Set(arr)];
    }
    ```

### 数组删去某值
1. 使用`Array.prototype.splice`：

    ```js
    function reduceArr(arr, delValue) {
        arr = arr.slice();

        var i, len;

        for (i = 0, len = arr.length; i < len; i++) {
            if (arr[i] === delValue) {
                arr.splice(i, 1);
                i--;
            }
        }

        return arr;
    }
    ```
2. 使用新数组保存：

    ```js
    function reduceArr(arr, delValue) {
        var newArr = [],
            i, len;

        for (i = 0, len = arr.length; i < len; i++) {
            if (arr[i] !== delValue) {
                newArr.push(arr[i]);
            }
        }

        return newArr;
    }
    ```
3. 使用`Array.prototype.filter`（数组空位不遍历）：

    ```js
    function reduceArr (arr, delValue) {
      return arr.filter((value) => value !== delValue)
    }
    ```
4. leetcode解法：[移除元素](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/数据结构与算法/LeetCode记录/README.md#移除元素)

### 数组的某项插入某位置
```js
/**
 * 移动数组的项，从一个位置插入至另一个位置（不是调换位置）
 * @param {Array} arr - 数组
 * @param {Number} from - 原数组起始位置
 * @param {Number} to - 原数组插入位置
 * @param {Boolean} [isLeft = false] - 是否插入左边（默认：插入右边）
 * @returns {Array} arr - 调换位置的数组
 */
function switchArr ({ arr, from, to, isLeft = false }) {
  arr = arr.slice()

  if (isLeft) {
    if (from < to - 1) {
      arr.splice(to - 1, 0, ...arr.splice(from, 1))
    } else if (from >= to + 1) {
      arr.splice(to, 0, ...arr.splice(from, 1))
    }
  } else {
    if (from > to + 1) {
      arr.splice(to + 1, 0, ...arr.splice(from, 1))
    } else if (from < to) {
      arr.splice(to, 0, ...arr.splice(from, 1))
    }
  }

  return arr
}
```

### 声明某长度并设定值的数组
>e.g. 声明arr：长度为n，值为下标（或某固定值）

1. 直接创建并循环赋值

    1. 字面量

        ```js
        var n = 55;

        var arr = [],
            i;

        for (i = 0; i < n; i++) {
            arr[i] = i;
        }
        ```
    2. `Array`构造函数：

        ```js
        var n = 55;

        var arr = new Array(n),
            i, len;

        for (i = 0, len = arr.length; i < len; i++) {
            arr[i] = i;
        }
        ```
2. `Array.prototype.map`赋值

    1. `Array.apply`、`Array`构造函数：

        ```js
        var n = 55

        var arr = Array.apply(null, new Array(n)).map((item, index) => index)
        ```
    2. `Array`构造函数、`join`、`split`：

        ```js
        var n = 55

        var arr = new Array(n + 1).join().split('').map((item, index) => index)
        ```
    3. `Object.keys`、`Array`构造函数、`toString`、`split`：

        ```js
        var n = 55

        var arr = Object.keys(new Array(n + 1).toString().split('')).map((item, index) => index)
        ```
3. ES6的`Array.from`

    ```js
    var n = 55

    var arr = Array.from({ length: n }, (value, index) => index)
    ```
4. 纯手打字面量（性能最好方式）

---
## 功能

### *原生JS*用请求图片作log统计
```js
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

### *原生JS*验证邮箱有效性
>来自：[Stack Overflow: Validate email address in JavaScript?](http://stackoverflow.com/questions/46155/validate-email-address-in-javascript#answer-46181)。

```js
function validateEmail(email) {

    return /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(email);
}
```

>不存在可以判断世界任何一个有效邮箱的正则。

>匹配中国大陆手机号码的正则表达式：[ChinaMobilePhoneNumberRegex](https://github.com/VincentSit/ChinaMobilePhoneNumberRegex)。

### *原生JS*创建兼容的XHR对象
```js
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
    if (xhr.readyState === 4) {
        console.log(xhr.getResponseHeader(某响应头), xhr.getAllResponseHeaders());

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
xhr.setRequestHeader(某请求头, 值);
xhr.send(null);
```

### *原生JS*动态添加脚本、样式
1. 动态添加脚本

    1. 异步（JS文件地址）

        1. JSONP

            >动态创建的`<script>`默认是`async`（可以手动设置`dom.async = false`，这样就是`defer`效果——按添加顺序加载，尽管此时`dom.defer === false`）。

            ```js
            const newScript = document.createElement('script')
            const appendPlace = document.getElementsByTagName('body')[0] || document.getElementsByTagName('head')[0]

            newScript.src = 'JS文件地址'

            appendPlace.appendChild(newScript)
            ```

        2. <details>

            <summary>（文档未加载完成时）直接<code>document.write</code></summary>

            >因为`document.write`需要向文档流中写入内容，因此在关闭（已加载）的文档上调用`document.write`会自动调用`document.open`，这将清空该文档的内容。

            ```js
            document.write('<script src="JS文件地址"><\/script>');
            ```
            </details>
    2. 同步（JS代码文本）

        >动态创建的、没有`src`属性的、通过`text`属性设置JS代码文本的`<script>`，添加后的脚本被马上执行（可以认为是当前脚本一部分，但实际不是，作用域不同；这个也是jQuery的ajax加载执行外部JS脚本的方式）。

        ```js
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

        - <details>

            <summary>通过<code>XMLHttpRequest</code>的同步请求获得JS代码文本</summary>

            ```js
            /**
             * 同步加载JS脚本
             * @param {String} url - JS文件的相对路径或绝对路径
             * @returns {Boolean} - 是否加载成功
             */
            function syncLoadJS(url) {
              var xmlHttp, appendPlace, newScript;

              if (window.ActiveXObject) {
                /* ie */
                try {
                  xmlHttp = new ActiveXObject("Msxml2.XMLHTTP");
                } catch (e) {
                  xmlHttp = new ActiveXObject("Microsoft.XMLHTTP");
                }
              } else if (window.XMLHttpRequest) {
                xmlHttp = new XMLHttpRequest();
              }

              xmlHttp.open("GET", url, false); // 采用同步加载
              xmlHttp.send(null); // 发送同步请求，若浏览器为Chrome或Opera，则必须发布后才能运行，不然会报错

              /* 4代表数据发送完毕 */
              if (xmlHttp.readyState === 4) {
                /* 0为访问的本地，200到300代表访问服务器成功，304代表没做修改访问的是缓存 */
                if ((xmlHttp.status >= 200 && xmlHttp.status < 300) || xmlHttp.status === 0 || xmlHttp.status === 304) {
                  newScript = document.createElement("script");
                  appendPlace = document.getElementsByTagName("body")[0] || document.getElementsByTagName("head")[0];

                  try {
                    newScript.appendChild(document.createTextNode(xmlHttp.responseText));
                  } catch (e) {
                    newScript.text = xmlHttp.responseText;
                  }

                  appendPlace.appendChild(newScript);

                  return true;
                } else {
                  return false;
                }
              } else {
                return false;
              }
            }
            ```
            </details>
2. 动态添加样式

    >样式的所有3种情况（`<style>`、`<link>`、`style`内嵌样式），动态添加或删除之后都是马上重新计算CSSOM，然后渲染。

    1. 添加`<style>`

        ```js
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

        ```js
        var newLink = document.createElement('link');

        newLink.rel = 'styleSheet';
        newLink.type = 'text/css';

        newLink.href = 'CSS文件地址';

        document.getElementsByTagName('head')[0].appendChild(newLink);
        ```
    3. 添加`style`内嵌样式

        ```js
        var oneDom = document.getElementById('节点id');

        oneDom.style.cssText += '; CSS代码文本'
        ```

    >CSS代码文本，如：`div {background-color: yellow;}`。

### *原生JS*获取星座
```js
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
>```js
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

### *原生JS*加入收藏夹
```js
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
```js
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

```js
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
根据业务要求进行：数据结构转化（如：提取属性）、数据填补默认字段。

1. 数据结构转化

    ```js
    // 按keyName提取
    function groupArrayByKey(arr, keyName) {
      return arr.reduce((acc, current) => {
        if (!acc[current[keyName]]) {
          acc[current[keyName]] = [];
        }
        acc[current[keyName]].push(current);
        return acc;
      }, {});
    }


    /* 使用测试 */
    groupArrayByKey(
      [
        { classId: "1", name: "张三", age: 16 },
        { classId: "1", name: "李四", age: 15 },
        { classId: "2", name: "王五", age: 16 },
        { classId: "3", name: "赵六", age: 15 },
        { classId: "2", name: "孔七", age: 16 },
      ],
      "classId",
    )
    ```
2. 数据填补默认字段

    ```js
    /**
     * 每项都添加 键-值（默认值）
     * @param {Array|Object} data - 要处理的数据
     * @param {Object} [params = {}] - 要添加的键-值的对象。键是要添加的键，值是添加键的默认值
     * @returns {Array|Object} 处理好的数据
     */
    function formatData(data, params = {}) {
      if (isObjEmpty(params)) {
        return data;
      }

      // 是数组
      if (Array.isArray(data)) {
        return data.map((item) => {
          // 需要添加键-值
          for (let [key, value] of Object.entries(params)) {
            if (typeof item[key] === "undefined") {
              item[key] = value;
            }
          }

          return item;
        });
      }
      // 是对象
      else {
        // 需要添加键-值
        for (let [key, value] of Object.entries(params)) {
          if (typeof data[key] === "undefined") {
            data[key] = value;
          }
        }

        return data;
      }
    }

    // 是否是空对象
    const isObjEmpty = (obj) => {
      if (obj !== Object(obj)) {    /* 参数不是对象 */
        throw new TypeError("参数不是对象");
      } else if (typeof Object.keys === "function") {
        return Object.keys(obj).length === 0;
      } else {                      /* 兼容性，ie9- */
        for (let one in obj) {
          if (obj.hasOwnProperty(one)) {
            return false;
          }
        }
        return true;
      }
    };


    /* 使用测试 */
    formatData(
      [{}, { 参数1: "有值" }],
      { 参数1: "默认值", 参数2: false, 参数3: { a: "默认值" } }
    )
    formatData(
      { 参数1: "有值" },
      { 参数1: "默认值", 参数2: false, 参数3: { a: "默认值" } }
    )
    ```

### *原生JS*判断是否支持WebP
1. 同步判断

    ```js
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

    ```js
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

### *原生JS*执行方法的前/后进行开/关loading
```js
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
`<a href="文件资源地址" download="文件名.文件类型">文件资源地址：若是字符串，则同源就下载，不同源就依然是导航跳转；若是Blob或Data URL协议，则下载</a>`

>1. `download`指示浏览器下载文件资源地址而不是导航跳转（若href的字符串不同源，则退回未添加download的逻辑——导航跳转）。
>2. 支持多种文件类型。
>3. ~~兼容性不佳。~~
>4. 若download未指定值或未指定文件后缀（未指定文件后缀，会仅用传值作为文件名、后缀从后面信息获取），则从多种方式中设置`文件名.文件类型`：响应头的`Content-Disposition`、`Content-Type`，URL的最后一段，Data URL的开头，Blob的`type`。
>5. 响应头`Content-Disposition: inline`（默认）是预览，`Content-Disposition: attachment`是下载；可以通过先下载资源（blob格式），再设置a标签的`download`进行下载或预览。

以下方法均依赖`<a>`的`download`属性（JS的Blob或Data URL，都需要先[CORS](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/HTTP相关/README.md#corscross-origin-resource-sharing跨域资源共享)下载文件资源地址成功后再进行操作）：

1. 下载文件（利用文件URL，支持设置文件名）

    >需要文件资源响应头包含正确的Access-Control-Allow-Origin值（CORS）。

    ```js
    function getBlob(fileUrl, filename) {
      return new Promise((resolve, reject) => {
        const xhr = new XMLHttpRequest();
        xhr.open('GET', fileUrl, true);
        xhr.responseType = 'blob';
        xhr.onloadend = () => {
          // 若CORS报错，则status值不会满足条件
          if (xhr.status >= 200 && xhr.status < 300) {  // 只有部分2xx支持传递数据（建议只处理200的响应）；304不返回数据
            const link = document.createElement('a');
            link.href = URL.createObjectURL(xhr.response); // Blob URL。也可以用Data URL（base64）
            link.download = filename ?? ''; // 若没有加download，则就是直接打开链接的逻辑（预览），a的href类似于window.open等

            link.style.display = 'none';
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);

            window.URL.revokeObjectURL(link.href);

            resolve(xhr)
          } else {
            reject(xhr)
          }
        };
        xhr.send();
      })
    }
    ```

    >`loadend`事件针对`XMLHttpRequest`或`FileReader`实例的完成（无论成功、失败、终止）仅触发一次。

    ><details>
    ><summary>Data URL（base64）方案</summary>
    >
    >```js
    >...
    >if (xhr.status >= 200 && xhr.status < 300) {
    >  const reader = new window.FileReader()
    >  reader.addEventListener('loadend', (e) => {
    >    const link = document.createElement('a');
    >    link.href = e.target.result;
    >    link.download = filename ?? ''; // 若没有加download，则就是直接打开链接的逻辑（预览），a的href类似于window.open等。但base64大概率会超过浏览器导航栏输入长度
    >    link.style.display = 'none';
    >    document.body.appendChild(link);
    >    link.click();
    >    document.body.removeChild(link);
    >
    >    resolve(xhr)
    >  })
    >  reader.readAsDataURL(Blob实例 或 File实例)
    >}
    >...
    >```
    ></details>

    - 把下载地址直接通过`a`标签打开

        ```js
        const link = document.createElement('a');
        link.href = 下载地址;
        link.target = '_blank';
        link.style.display = 'none';
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
        ```
2. 下载文本（把JS字符串变成文本文件下载）

    >Blob。代码生成文本内容再创建下载。

    ```js
    /**
     * 下载文本
     * @param {String} content - 保存的字符串内容
     * @param {String} filename - 文件名（包括后缀）
     */
    function textDownload (content, filename) {
      // 创建隐藏的可下载链接
      const eleLink = document.createElement('a')
      eleLink.download = filename ?? ''
      eleLink.style.display = 'none'

      // 字符内容转变成Blob实例
      const blob = new window.Blob([content])
      // 创建Blob URL
      const url = URL.createObjectURL(blob)

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
3. 下载图片（利用Canvas）

    >1. Canvas。仅支持：png/jpg/webp。
    >2. 需要文件资源响应头包含正确的Access-Control-Allow-Origin值（CORS）。

    ```js
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
        // 若CORS报错，则触发error事件
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

        // 图片转Data URL（Base64）地址
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

### *原生JS*写入剪切板
```ts
async function clipboard (text: string | number): Promise<string> {
  text = String(text);

  try {
    await window.navigator.clipboard.writeText(text); // 新接口
  } catch {
    try {
      // 需要浏览器tab是active或有交互才能触发
      let textArea = document.createElement("input");

      textArea.value = text;
      document.body.appendChild(textArea);
      textArea.select();

      document.execCommand("cut"); // 已废弃
      document.body.removeChild(textArea);
    } catch {
      return Promise.reject(text);
    }
  }
  return Promise.resolve(text);
}


/* 使用测试 */
clipboard("写入的内容~")
  .then((text) => {console.log(`\`${text}\`写入成功！`)})
  .catch((text) => {console.warn(`\`${text}\`写入失败！`)})
```
>1. 注意，有些浏览器对不信任的域名会静默失败（resolved）。
>2. 可以使用[clipboard.js](https://github.com/zenorocha/clipboard.js)。

### React组件业务类似Promise.all的效果
```tsx
import React, { useEffect, useState, useRef } from "react";
import { notification, Button } from "antd";

// 模拟异步请求
function sleep(ms: number) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

export default function Demo(props: { show: boolean }) {
  const resolveFunc1 = useRef<Function>(() => {});
  const resolveFunc2 = useRef<Function>(() => {});
  const resolveFunc3 = useRef<Function>(() => {});

  // 若3个方法均被调用，则ready被赋值
  const [ready, setReady] = useState<any>(null);

  useEffect(() => {
    Promise.all([
      new Promise((resolve1) => {
        resolveFunc1.current = resolve1;
      }),
      new Promise((resolve2) => {
        resolveFunc2.current = resolve2;
      }),
      new Promise((resolve3) => {
        resolveFunc3.current = resolve3;
      }),
    ]).then((data) => {
      setReady(data);
    });
  }, []);

  useEffect(() => {
    if (ready) {
      const info = JSON.stringify(ready);
      console.log(info);
      notification.open({ message: info });
    }
  }, [ready]);

  // 以下模拟3个方法被调用成功

  const [asyncSelfShow, setAsyncSelfShow] = useState<boolean>(false);
  useEffect(() => {
    // 1. 模拟异步返回
    sleep(2000).then(() => {
      resolveFunc1.current({ a: 1 });

      setAsyncSelfShow(true);
    });
  }, []);

  const { show } = props;
  useEffect(() => {
    // 2. 参数传入满足
    show && resolveFunc2.current({ b: 2 });
  }, [show]);

  const [selfShow, setSelfShow] = useState<boolean>(false);

  return (
    <div>
      <h3>ready: {JSON.stringify(ready)}</h3>

      <p>props.show: {show ? "true" : "false"}</p>
      <p>asyncSelfShow： {asyncSelfShow ? "true" : "false"}</p>
      <p>
        selfShow: {selfShow ? "true" : "false"}
        <br/>
        <Button
          onClick={() => {
            // 3. 组件自身状态变化
            resolveFunc3.current({ c: 3 });

            setSelfShow(!selfShow);
          }}
        >
          setSelfShow{!selfShow ? "true" : "false"}
        </Button>
        </p>
    </div>
  );
}
```

### *原生JS*判断是否有循环引用
```js
function hasCircularReference(obj, weakmap = new WeakMap()) {
  // 基本数据类型
  if (obj === null || (typeof obj !== "object" && typeof obj !== "function")) {
    return false;
  }

  if (weakmap.has(obj)) {
    return true;
  } else {
    weakmap.set(obj, true);

    for (const key of Object.keys(obj)) {
      if (hasCircularReference(obj[key], weakmap)) {
        return true;
      }
    }
    return false;
  }
}
```

---
## DOM相关

### *原生JS*DOM展示或消失执行方法（IntersectionObserver）
1. class写法：

    ```ts
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
    export class DisplayDom {
      io: IntersectionObserver | undefined;

      constructor({
        target,
        show = () => {},
        hide = () => {},
        threshold = 0.01,
        once = false,
        root = null,
      }: {
        target: Element;
        show?: Function;
        hide?: Function;
        threshold?: number;
        once?: boolean;
        root?: Element | Document | null;
      }) {
        const thresholdSafe = Math.max(Math.min(threshold, 1), 0.01); // 取值在[0.01, 1]
        try {
          this.io = new window.IntersectionObserver(
            (entries) => {
              if (entries[0].intersectionRatio >= thresholdSafe) {
                // 出现
                show();

                if (once) {
                  this.stop();
                }
              } else {
                // 不出现
                hide();
              }
            },
            { threshold: [thresholdSafe], root },
          );

          this.io.observe(target); // 开始观察
        } catch (error) {
          console.error(
            error,
            `\n不支持IntersectionObserver，升级浏览器或代码使用polyfill: https://github.com/w3c/IntersectionObserver`,
          );
        }
      }

      stop() {
        this.io?.disconnect();
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
2. 构造函数写法：

    ```js
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

### *原生JS*判断是否为`Node`、是否为`Element`
```js
// 判断是否为Node
function isNode(o) {
  return typeof Node === 'object' ? o instanceof Node : !!o && typeof o === 'object' && typeof o.nodeType === 'number' && typeof o.nodeName === 'string';
}

// 判断是否为Element
function isElement(o) {
  return typeof HTMLElement === 'object' ? o instanceof HTMLElement : !!o && typeof o === 'object' && o !== null && o.nodeType === 1 && typeof o.nodeName === 'string';
}
```

### *原生JS*输入框光标位置的获取和设置
```js
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
```js
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

>参考：[ScrollFix](https://github.com/joelambert/ScrollFix)。

### *原生JS*获取滚动条宽度（或高度）
```js
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

### *原生JS*展示页面帧数
>类似效果；DevTools的Rendering中的FPS meter。

```js
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

>1. FrameTime：两帧画面间隔耗时（或单帧渲染耗时）。
>2. FPS：每秒刷新多少帧。
>
>    1. 帧率高，未必流畅。帧率稳定才流畅。
>    2. 静态页面，理论FPS应该为0，否则说明有冗余刷新，容易引起手机发热及耗电。
>    3. 滚动页面，关注FPS、卡顿率。
>3. 卡顿：掉帧，一帧渲染耗时大于显示器刷新间隔（如：占用2次或多次显示器刷新耗时），表明浏览器已刷新但画面没有刷新。若出现多次没有画面刷新，则可能是一次卡顿。
>4. 流畅度：原本保持着某个FPS，突然下降FPS扰乱用户视觉惯性、出现影响用户体验的卡顿感；或低于18~24帧，人眼基本能感觉画面不连续性，也就感觉到卡顿。

### *React*默认图组件
1. <details>

    <summary>class组件</summary>

    ```tsx
    import React, { Component } from "react";

    interface PropsType {
      src: string;
      defaultImage: string;
      className?: string;
      classNameForError?: string;
      style?: React.CSSProperties;
      onClick?: () => void;
      alt?: string;
    }

    export default class TheImage extends Component<PropsType> {
      state = {
        isError: false,
      };

      componentDidUpdate(prevProps: PropsType) {
        // 检测到图片有更新，需要重新加载
        if (prevProps.src !== this.props.src) {
          if (this.props.src && this.state.isError) {
            this.setState({
              isError: false,
            });
          }
          if (!this.props.src && !this.state.isError) {
            this.setState({
              isError: true,
            });
          }
        }
      }

      render() {
        const {
          src,
          defaultImage,
          className = "",
          classNameForError = "",
          style,
          onClick,
          alt,
        } = this.props;

        return (
          <img
            src={this.state.isError ? defaultImage : src}
            className={
              this.state.isError ? `${classNameForError} ${className}` : className
            }
            style={style}
            onClick={() => {
              onClick?.();
            }}
            onError={() => {
              this.setState({
                isError: true,
              });
            }}
            alt={alt || `图${src}`}
          />
        );
      }
    }
    ```
    </details>
2. hook函数组件

    ```tsx
    import React, { useEffect, useState } from "react";

    interface PropsType {
      src: string;
      defaultImage: string;
      className?: string;
      classNameForError?: string;
      style?: React.CSSProperties;
      onClick?: () => void;
      alt?: string;
    }

    export default function TheImage(props: PropsType) {
      const {
        src,
        defaultImage,
        className = "",
        classNameForError = "",
        style,
        onClick,
        alt,
      } = props;

      const [isError, setIsError] = useState(false);

      useEffect(() => {
        setIsError(!src);
      }, [src]);

      return (
        <img
          src={isError ? defaultImage : src}
          className={isError ? `${classNameForError} ${className}` : className}
          style={style}
          onClick={() => {
            onClick?.();
          }}
          onError={() => {
            setIsError(true);
          }}
          alt={alt || `图${src}`}
        />
      );
    }
    ```

<details>
<summary>使用测试</summary>

```tsx
/* 使用测试 */
<TheImage
  src={this.state.switch ? 'https://placehold.co/100/?text=true': '1'}
  defaultImage="https://placehold.co/100/?text=default"
  style={{ width: "100px", height: "100px" }}
  className='abc'
  classNameForError='abc-error'
  onClick={() => {
    this.setState({
      switch: !this.state.switch
    })
  }}
/>
```
</details>

### *原生JS*溢出文本的省略
```html
<style>
  p {
    font-size: 12px; /* 注意：太大的字体，一行撑起的scrollHeight可能超过line-height */
    height: 40px;
    line-height: 20px;
  }
</style>

<p id="container">
  123我是文本abc。123我是文本abc。123我是文本abc。123我是文本abc。123我是文本abc。123我是文本abc。123我是文本abc。123我是文本abc。123我是文本abc。123我是文本abc。123我是文本abc。123我是文本abc。123我是文本abc。</p>

<script>
  const container = document.getElementById('container');
  const defaultText = container.innerText;

  function setEllipsis() {
    const containerHeight = container.offsetHeight
    // fixme: （复杂实现，）不仅针对innerText，还可以针对innerHTML并把每个子节点container.childNodes，根据nodeType的值来分别处理。如：`Node.ELEMENT_NODE`当做一个整体，`Node.TEXT_NODE`分割每个文字
    for (let i = 0; i < defaultText.length; i++) {
      container.innerText = defaultText.substring(0, i)
      if (containerHeight < container.scrollHeight) {
        container.style.overflow = 'hidden'
        container.innerHTML = defaultText.substring(0, i - 3) + '<span style="cursor: pointer" onclick="container.innerHTML=defaultText; container.style.overflow=\'unset\'">...</span>'

        console.log('产生省略')
        break
      }
    }
  }

  window.addEventListener('resize', setEllipsis)
  setEllipsis()
</script>
```

>可参考：[Ant Design：Typography排版的`ellipsis`](https://ant.design/components/typography-cn#typography-demo-ellipsis-controlled)、[element-ui：Table 表格的`show-overflow-tooltip`](https://github.com/ElemeFE/element/blob/master/packages/table/src/table-body.js#L250-L283)。

### 九宫格抽奖
>canvas实现的抽奖插件（大转盘、九宫格、老虎机）：[lucky-canvas](https://github.com/buuing/lucky-canvas)。

1. 缓动函数触发回调，可以设置最终触发回调命中的index

    fixme
2. 原生JS，直接修改DOM

    ```ts
    type initData = {
      // 主容器
      container: Element;
      // 子级轮播的class名，若没传，则轮播用子级所有li标签
      subClass?: string;
      // 子级激活后添加的class名
      currentClass?: string;
      // 每走一格的时间(ms)
      speed?: number;
      // 循环的圈数
      lap?: number;
      // 动画结束回调
      callback?: Function;
    };

    export default class SlotMC {
      private domlist: NodeListOf<Element>;
      private container: Element;
      private currentClass: string;
      private speed: number;
      private ratio: number;
      private ease: boolean;
      private lap: number;
      private callback: Function;
      private playing: boolean;
      private length: number;
      private index: number;

      constructor(object: initData) {
        if (!object.container) {
          console.error('没有指定container参数,无法获取节点');
          return;
        }
        if (!object.subClass) {
          this.container = object.container;
          this.domlist = this.container.querySelectorAll('li');
        } else {
          this.container = object.container;
          this.domlist = this.container.querySelectorAll(`.${object.subClass.toString()}`);
        }
        this.currentClass = object.currentClass || 'current';
        this.speed = object.speed || 70; // 每转一格的时间(ms)(老虎机时为整个动画的时间)
        this.ratio = object.lap || 3; // 变速时，速度的倍数(九宫格,直)
        this.ease = true; // 先慢后快，结束时变慢(老虎机时为速度效果的速度曲线)
        this.lap = object.lap || 3; // 循环的圈数
        this.callback = object.callback || function () {}; // 结束后的回调函数

        this.playing = false;
        this.length = this.domlist.length;
        for (let i = 0; i < this.length; i++) {
          // @ts-ignore
          this.domlist[i].index = i;
        }
      }

      public hit(pos: number) {
        let { speed } = this;
        let roundIndex = 0; // 每圈内当前序列
        let lap = 0; // 圈数
        let slowStart = true;
        let slowEnd = true;
        let finish = false; // 结束的标识
        if (!this.playing) {
          this.playing = true;
          this.domlist[0].classList.add(this.currentClass);
          if (this.ease) {
            speed = this.speed * this.ratio;
          }
          /** 超出范围或者未提供位置 */
          if (!pos || pos > this.domlist.length) {
            // eslint-disable-next-line no-param-reassign
            pos = 1;
          }

          const loop = () => {
            const choose = this.container.querySelector(`.${this.currentClass}`);
            // @ts-ignore
            this.index = choose.index + 1;
            if (this.index === this.length) {
              this.index = 0;
            }
            choose.classList.remove(this.currentClass);
            this.domlist[this.index].classList.add(this.currentClass);

            // eslint-disable-next-line no-plusplus
            roundIndex++;
            if (roundIndex === this.length) {
              // 计算圈数
              // eslint-disable-next-line no-plusplus
              lap++;
              roundIndex = 0;
            }
            if (this.ease && roundIndex === Math.floor(this.length / 2) && slowStart) {
              clearInterval(timeout);
              speed = this.speed;
              slowStart = false;
              timeout = setInterval(loop, speed);
            }
            if (lap > this.lap) {
              // 圈跑完了
              if (this.ease && slowEnd) {
                // 圈跑完了，进入变速
                clearInterval(timeout);
                speed = this.speed * this.ratio;
                slowEnd = false;
                timeout = setInterval(loop, speed);
              }
              if (this.index + 1 === pos && finish) {
                clearInterval(timeout);
                this.playing = false;
                this.callback?.call(this, pos);
              }
              finish = true;
            }
          };
          let timeout = setInterval(loop, speed);
        }
      }
    }
    ```

    <details>
    <summary>使用测试</summary>

    ```html
    <!-- 使用测试 -->
    <style>
      .current {
        background-color: red;
      }
    </style>

    <ul id="j-ul">
      <li >不包含</li>
      <li class="box">1</li>
      <li class="box">2</li>
      <li class="box">3</li>
      <li class="box">4</li>
      <li class="box">5</li>
      <li class="box">6</li>
      <li class="box">7</li>
      <li class="box">8</li>
      <li class="box">9</li>
      <li class="box">...</li>
      <li class="box">第n个</li>
      <li >不包含</li>
    </ul>

    <script>
    let sl = new SlotMC({
      container: document.getElementById('j-ul'),
      subClass: 'box'
    });
    sl.hit(2);
    // 去除current类之后继续调用：sl.hit(n)
    </script>
    ```
    </details>

---
## 任务执行

### sleep
1. 要求：

    延时一段时间之后执行剩余代码。
2. 实现方式：

    1. `async-await`、`Promise`、`setTimeout`

        ```js
        function sleep (ms) {
          return new Promise((resolve) => setTimeout(resolve, ms))
        }

        async function demo () {
          // 使用
          console.time(1)
          await sleep(1000) // 延时执行
          console.timeEnd(1)
          console.time(2)
          await sleep(1000) // 延时执行
          console.timeEnd(2)
        }

        demo()
        ```

    - 支持取消的sleep：

        ```ts
        type CancelablePromise = Promise<any> & { cancel: any };

        function sleep(timeout: number): CancelablePromise {
          let res: (v: string) => void;
          let timer: ReturnType<typeof setTimeout>;
          const promise = new Promise((resolve) => {
            res = resolve;
            timer = setTimeout(() => {
              resolve("done");
            }, timeout);
          }) as CancelablePromise;
          promise.cancel = function (data: string) {
            res(data);
            clearTimeout(timer);
          };

          return promise;
        }
        ```
    2. `Promise`、`setTimeout`

        ```js
        function sleep (ms) {
          return new Promise((resolve) => setTimeout(resolve, ms))
        }

        // 使用
        console.time(1)
        sleep(1000).then(() => {    // 延时执行
          console.timeEnd(1)
          console.time(2)
          sleep(1000).then(() => {  // 延时执行
            console.timeEnd(2)
          })
        })
        ```
    3. `setTimeout`

        ```js
        // 使用
        console.time(1)
        setTimeout(() => {  // 延时执行
          console.timeEnd(1)
          console.time(2)
          setTimeout(() => {  // 延时执行
            console.timeEnd(2)
          }, 1000)
        }, 1000)
        ```

    4. <details>

        <summary>JS循环代码占用主线程（阻塞、卡死线程）</del></summary>

        ```js
        function sleep (ms) {
          ms += new Date().getTime()
          while (new Date() < ms) {}
        }

        // 使用
        console.time(1)
        sleep(1000) // 延时执行
        console.timeEnd(1)
        console.time(2)
        sleep(1000) // 延时执行
        console.timeEnd(2)
        ```
        </details>

### *原生JS*轮询
```ts
// 提供给 参数taskFn 返回 `失败的、值为CANCEL_TOKEN 的Promise实例`
export const CANCEL_TOKEN = new Error("主动结束整个轮询的标志");

interface Options<T> {

  // 轮询执行方法(参数1：轮询第几次，起始为1)
  //   若返回 Promise.resolve，则执行成功、整个轮询成功结束；
  //   若返回 Promise.reject，则执行失败：
  //     主动结束整个轮询 约定：返回 `失败的、值为CANCEL_TOKEN 的Promise实例`；
  //     若 轮询重试次数用完 或 主动结束整个轮询 或 整个轮询超时，则整个轮询失败结束，否则继续轮询。
  taskFn: (num: number) => Promise<T>;

  // 轮询重试次数，默认：5次
  retries?: number;
  // 重试间隔（毫秒），默认：1000ms
  retryInterval?: number;

  // 整个轮询超时时间（毫秒），若不传则没有整体超时时间
  masterTimeout?: number;
  // 重试回调(参数1：剩余重试次数, 参数2：本次错误信息)
  progressCallback?: (retriesRemain: number, err: unknown) => void;
}

// 轮询执行（轮询无法在外部终止，只能在 传参taskFn 返回Promise实例处理）
export const promisePoller = <T>(options: Options<T>): Promise<T> => {
  const { taskFn, retries = 5, retryInterval = 1000, masterTimeout, progressCallback } = options;

  let timeoutId: ReturnType<typeof setTimeout>;
  let pollingSafe = true; // 是否可以继续轮询
  const rejections: Array<unknown> = []; // 存放失败信息
  let retriesRemain = retries;  // 剩余重试次数

  return new Promise((resolve, reject) => {
    if (masterTimeout) {
      timeoutId = setTimeout(() => {
        pollingSafe = false;
        reject(rejections.concat("轮询总时间超时"));
      }, masterTimeout);
    }

    const poll = () => {
      taskFn(retries - retriesRemain + 1)
        .then((result) => {
          clearTimeout(timeoutId);
          resolve(result);
        })
        .catch((err: typeof CANCEL_TOKEN | unknown) => {
          if (err === CANCEL_TOKEN) {
            clearTimeout(timeoutId);
            reject(rejections.concat("主动结束整个轮询"));
          } else {
            // 存储轮询失败信息
            rejections.push(err);

            // 剩余重试次数减一
            retriesRemain -= 1;

            progressCallback?.(retriesRemain, err);

            if (retriesRemain > 0) {
              pollingSafe && new Promise((resolve2) => {
                setTimeout(resolve2, retryInterval)
              }).finally(() => {
                poll()
              });
            } else {
              clearTimeout(timeoutId);
              reject(rejections);
            }
          }
        });
    };

    poll();
  });
};


/* 使用测试 */
promisePoller({
  taskFn: async (num: number) => {
    console.log(`执行第${num}次`);
    await delay(200);
    if (Math.random() < 0.5) {
      // 失败
      return Promise.reject(new Error(`执行第${num}次失败`)); // 或： throw new Error(`执行第${num}次失败`)
    } else if (Math.random() < 0.5) {
      // 成功
      return num;
    } else {
      // 主动结束整个轮询
      return Promise.reject(CANCEL_TOKEN);  // 或： throw CANCEL_TOKEN
    }
  },
})
  .then((data) => console.log('整个轮询成功', data))
  .catch((err) => console.error('整个轮询失败', err));

function delay(ms: number) {
  return new Promise((resolve, reject) => {
    if (Math.random() < 0.5) {
      setTimeout(() => {
        reject('delay 随机失败')
      }, ms);
    } else {
      setTimeout(() => {
        resolve('delay 随机成功')
      }, ms);
    }
  });
}
```
>参考：[promise-poller](https://github.com/joeattardi/promise-poller)。

- 实现：轮询获取分页接口的所有数据（必须加上请求次数上限）

    ```js
    async function pollingPaging(maxFetchTimes = 5) {
      // 耦合写死了：后台接口请求的数据结构、后台接口返回的数据结构、本函数返回的数据结构
      const data = {
        list: [],
        pagination: {
          current: 1,
          pageSize: 1000,
          total: 0,
        },
      };
      let fetchTimes = 0;
      try {
        while (fetchTimes < maxFetchTimes) {
          fetchTimes++;

          const res = await 后台接口({
            current: data.pagination.current,
            pageSize: data.pagination.pageSize,
          });
          data.list.push(...res.list);
          data.pagination.total = res.pagination.total;

          // 能够继续请求的情况
          if (fetchTimes < maxFetchTimes && data.pagination.current * data.pagination.pageSize < res.pagination.total) {
            data.pagination.current++;
          } else {
            break;
          }
        }
      } catch (err) {
        // 请求报错，回退请求次数相关的值
        data.pagination.current--;
        fetchTimes--;
        console.error(err);
      }

      // 已达到最大请求次数，但数据未获取完全
      if (maxFetchTimes === 0 || (fetchTimes >= maxFetchTimes && data.pagination.current * data.pagination.pageSize < data.pagination.total)) {
        console.error('已达到最大轮询限制({0})，无法再获取更多数据'.replace('{0}', maxFetchTimes));
      }
      return data;
    }
    ```

### *原生JS*节流函数
```ts
class Throttle<T extends any[]> {
  constructor(func: (...args: T) => void, delay: number = 300, atBegin: boolean = true) {
    this.delay = delay;
    this.atBegin = atBegin;
    this.func = func;
  }

  private delay: number;
  private atBegin: boolean;
  private func: (...args: T) => void;

  private timer: number = 0;

  // 刷新执行
  public flush: (...args: T) => void = (...args: T) => {
    if (!this.timer) {
      this.atBegin && this.func.apply(this, args);
      this.timer = setTimeout(() => {
        !this.atBegin && this.func.apply(this, args);
        this.timer = 0;
      }, this.delay);
    }
  };

  // 取消执行
  public cancel: () => void = () => {
    if (this.timer) {
      clearTimeout(this.timer);
      this.timer = 0;
    }
  };

  // 判断是否节流中
  public isPending: () => boolean = () => {
    return this.timer !== 0;
  };
}


/* 使用测试 */
const a = new Throttle((a: number, b: string)=>{})
a.flush(1, '');a.flush(1, '');
a.isPending();
a.cancel()
```

### *原生JS*用`setTimeout`模拟`setInterval`
```js
/**
 * 用setTimeout模拟setInterval
 * @constructor
 * @param {Function} func - 循环执行函数
 * @param {Number} ms - 间隔毫秒
 */
function SetInterval(func, ms) {
  let timeoutId;

  if (typeof func === "function") {
    timeoutId = setTimeout(function cb() {
      timeoutId = setTimeout(cb, ms);

      func();
    }, ms);
  }

  this.stop = function () {
    clearTimeout(timeoutId);
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
```js
/**
 * 每一帧都执行一次func
 * @constructor
 * @param {Function} func - 执行的函数
 */
function RepeatRAF(func) {
  let requestId;

  if (typeof func === "function") {
    requestId = requestAnimationFrame(function cb() {
      requestId = requestAnimationFrame(cb);

      func();
    });
  }

  this.stop = function () {
    cancelAnimationFrame(requestId);
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

### *原生JS*`requestAnimationFrame`模拟`setTimeout`和`setInterval`
1. 模拟`setTimeout`

    ```js
    function SetTimeout(func, ms) {
      const start = Date.now();

      let requestId;

      if (typeof func === "function") {
        requestId = requestAnimationFrame(function cb() {
          if (Date.now() - start >= ms) {
            func();
          } else {
            requestId = requestAnimationFrame(cb);
          }
        });
      }

      this.stop = function () {
        cancelAnimationFrame(requestId);
      };
    }

    /* 使用测试 */
    var a = new SetTimeout(function () {
      console.log(1);

      if (...) {
        a.stop();
      }
    }, 1000);

    // a.stop();
    ```
2. 模拟`setInterval`

    ```js
    function SetInterval(func, ms) {
      let start = Date.now();

      let requestId;

      if (typeof func === "function") {
        requestId = requestAnimationFrame(function cb() {
          requestId = requestAnimationFrame(cb);

          if (Date.now() - start >= ms) {
            func();
            start = Date.now();
          }
        });
      }

      this.stop = function () {
        cancelAnimationFrame(requestId);
      };
    }

    /* 使用测试 */
    var a = new SetInterval(function () {
      console.log(1);

      if (...) {
        a.stop();
      }
    }, 100);

    // a.stop();
    ```

---
## 算法思路

### *原生JS*判断对象是否为空
```js
function isObjEmpty(obj) {
  if (obj !== Object(obj)) {  /* 参数不是对象 */
    throw new TypeError("参数不是对象");
  } else if (typeof Object.keys === "function") {
    return Object.keys(obj).length === 0;
  } else {                    /* 兼容性，ie9- */
    for (var one in obj) {
      if (obj.hasOwnProperty(one)) {
        return false;
      }
    }
    return true;
  }
}
```

### 无缝轮播
1. 要求：

    一共有`n`数量的项（**1**,**2**,**3**,...,**n**），中间展示内容有`i`数量的项，左右（或上下）分别展示待轮播有`m`数量的项（轮播到任何项都可以看见左右`m`数量的项），可以无缝向左右（或上下）轮播。
2. 实现方式：

    1. 方法1：

        1. *原始项*前面复制*原始项*最后的 **n-(m+i)+1**项~**n**项 的一共`m+i`数量的项；*原始项*后面复制*原始项*最前的 **1**项~**m+i**项 的一共`m+i`数量的项。
        2. 因为前后新增了项，滚动前的初始位置要向左（或上）移动`m+i`数量的项的距离。
        3. 轮播到达*原始项*边缘：

            1. 右（或下）轮播：当完全播放完原始最后一项时（最后`i`数量的项全部轮播完毕），把整个轮播内容向左（或上）移动整个*原始项*的距离。
            2. 左（或上）轮播：当完全播放完原始最前一项时（最前`i`数量的项全部轮播完毕），把整个轮播内容向右（或下）移动整个*原始项*的距离。
    2. 方法2：

        不复制、移动整个DOM的方法。
    3. 方法3：

        改变单个项的堆叠层级。

### 获取某一位的数字
1. 字符串化后获取那一位的字符

    ```js
    /**
     * 获取某一位的数字
     * @param {Number} num - 操作数
     * @param {Number} [index = 0] - 获取从右向左第index位置上的数字（若是10进制，则0：个位；1：十位；2：百位...）
     * @param {Number} [radix = 10] - 进制
     * @returns {Number} - 数字（十进制表示）
     */
    function getIndexNumber(num, index = 0, radix = 10) {
      const str = num.toString(radix);
      return parseInt(str[str.length - 1 - index], radix) || 0;
    }
    ```
2. 算术

    ```js
    /**
     * 获取某一位的数字
     * @param {Number} num - 操作数
     * @param {Number} [index = 0] - 获取从右向左第index位置上的数字（若是10进制，则0：个位；1：十位；2：百位...）
     * @param {Number} [radix = 10] - 进制
     * @returns {Number} - 数字（十进制表示）
     */
    function getIndexNumber(num, index = 0, radix = 10) {
      return Math.floor(num / Math.pow(radix, index)) % radix;
    }
    ```

<details>
<summary>数学公式</summary>

对于一个 $d$ 进制的数字 $x$，要获取其第 $k$ 位 $x_k$（k：0表示右边第一位、1表示右边第二位，以此类推）：

$x_k = \lfloor\frac{x}{d^k}\rfloor \bmod d$（ $\lfloor a \rfloor$表示对浮点数 $a$ 向下取整； $\bmod \space d$ 表示对 $d$ 取余）。
</details>

- <details>

    <summary>使用测试</summary>

    ```js
    /* 使用测试 */
    console.log(getIndexNumber(1, 0), 1);
    console.log(getIndexNumber(1, 1), 0);
    console.log(getIndexNumber(1, 2), 0);
    console.log("----");
    console.log(getIndexNumber(123456, 0), 6);
    console.log(getIndexNumber(123456, 1), 5);
    console.log(getIndexNumber(123456, 2), 4);
    console.log(getIndexNumber(123456, 3), 3);
    console.log(getIndexNumber(123456, 4), 2);
    console.log(getIndexNumber(123456, 5), 1);
    console.log(getIndexNumber(123456, 6), 0);
    console.log("----");
    console.log(getIndexNumber(0b101, 0, 2), 1);
    console.log(getIndexNumber(0b101, 1, 2), 0);
    console.log(getIndexNumber(0b101, 2, 2), 1);
    console.log(getIndexNumber(0b101, 3, 2), 0);
    console.log("----");
    console.log(getIndexNumber(0b101101, 0, 2), 1);
    console.log(getIndexNumber(0b101101, 1, 2), 0);
    console.log(getIndexNumber(0b101101, 2, 2), 1);
    console.log(getIndexNumber(0b101101, 3, 2), 1);
    console.log(getIndexNumber(0b101101, 4, 2), 0);
    console.log(getIndexNumber(0b101101, 5, 2), 1);
    console.log(getIndexNumber(0b101101, 6, 2), 0);
    console.log(getIndexNumber(0b101101, 7, 2), 0);
    console.log("----");
    console.log(getIndexNumber(0x4567890abcdef, 0, 16), 15);
    console.log(getIndexNumber(0x4567890abcdef, 1, 16), 14);
    console.log(getIndexNumber(0x4567890abcdef, 2, 16), 13);
    console.log(getIndexNumber(0x4567890abcdef, 3, 16), 12);
    console.log(getIndexNumber(0x4567890abcdef, 4, 16), 11);
    console.log(getIndexNumber(0x4567890abcdef, 5, 16), 10);
    console.log(getIndexNumber(0x4567890abcdef, 6, 16), 0);
    console.log(getIndexNumber(0x4567890abcdef, 7, 16), 9);
    console.log(getIndexNumber(0x4567890abcdef, 8, 16), 8);
    console.log(getIndexNumber(0x4567890abcdef, 9, 16), 7);
    console.log(getIndexNumber(0x4567890abcdef, 10, 16), 6);
    console.log(getIndexNumber(0x4567890abcdef, 11, 16), 5);
    console.log(getIndexNumber(0x4567890abcdef, 12, 16), 4);
    console.log(getIndexNumber(0x4567890abcdef, 13, 16), 0);
    ```
    </details>

---
## Node.js相关

### 确保文件夹存在
```js
const fs = require("fs");
const path = require("path");

// 确保文件夹存在（不存在则创建，可判断多层文件夹）
function validateFolder(pathWay) {
  if (fs.existsSync(pathWay)) {
    return true;
  } else {
    if (validateFolder(path.dirname(pathWay))) {
      fs.mkdirSync(pathWay);
      console.log(`创建 ${pathWay}`);
      return true;
    }
  }
}
```

---
### jQuery方法

#### jQuery滚动加载
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

#### jQuery图片延时加载（lazyload）
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
     * @param {Function} func - 图片加载成功后回调函数，this和参数为图片DOM
     * @param {String} [dataError = 'data-error'] - img标签上存放「真实地址加载失败后显示的地址」的属性
     * @param {Function} errorFunc - 图片加载失败后回调函数，this和参数为图片DOM
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

---
#### jQuery节点跟随屏幕滚动而相对静止
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

#### jQuery弹出toast
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

#### jQuery全选、取消全选
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

#### jQuery点击指定区域以外执行函数
1. jQuery

```js
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

```js
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

#### jQuery hover展示内容并且可跨越间隙到内容
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

#### jQuery启动、暂停CSS动画
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

#### jQuery获取`HTTP response header`信息
```js
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

#### jQuery修复HTML标签`placeholder`属性无效
```js
/**
 * 修复HTML标签`placeholder`属性无效
 * @param {Object} [$dom = $('input, textarea')] - jQuery节点
 */
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

#### jQuery模拟手机旋转（使页面都以「横屏」展示）
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
