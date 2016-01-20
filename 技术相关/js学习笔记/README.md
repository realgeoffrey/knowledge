#js学习笔记

- if中用赋值（大部分是误用）并非总是返回真值，条件判断赋值内容Boolen后为假即判断为假：`if(a = false){...}`。

- JS性能
    - 平稳退化：当浏览器不支持或禁用了JS功能后，访问者也能完成最基本的内容访问。
        - 为JS代码预留出退路（html标签添加属性链接，用js事件绑定去拦截浏览器默认行为）
            >`<a href="真实地址" class="j-func">...</a>`

        - ~~伪协议(javascript:)~~
            >`<a href="javascript: func();">...</a>`

        - ~~内嵌事件处理函数~~
            >`<a href="#" onclick="func();return false;">...</a>`

    - 渐进增强：对具体某功能支持的判断，并向后兼容，用一些额外信息层去包裹原始内容。
    - 向后兼容：确保老版本浏览器功能，使之虽不能支持某些功能，但仍能基本访问。
        - 对象检测：`if(func){func();}`
        - ~~浏览器嗅探技术~~
    - 资源分离：把样式表和脚本分离出html。
        - 使用外部资源。
        - 不在html上用事件处理函数。
        - 对只为DOM增添的内容，转移到外部资源中动态创建。
    - 性能提升。
        - 减少访问DOM（搜索结果保存在变量中）。
        - 减少外链请求数量（合并js、css、图片）。
        - 压缩资源。
        - 脚本放置在`</body>`前。

- DOM加载步骤、jQuery的文档ready事件和js的onload事件顺序
    1. 解析Html结构
    2. 加载外部脚本和样式表文件
    3. 解析并执行脚本代码
    4. 构造Html DOM模型 ->完成后执行`$(document).ready(function(){});`
    5. 加载图片等外部文件
    6. 页面加载完毕 -> 完成后执行`window.onload();`

- 构造函数中的变量

    实例化（new）一个构造函数,得到的对象拥有构造函数内用`this`定义的属性(或方法),在构造函数内的`var`变量无法被这个对象使用,只能在构造函数里使用(类似私有变量).

- localStorage、sessionStorage、cookie

    都存储在本地

    - `web storage`

        - 除了ie6、ie7外其他浏览器都支持（ie及FF需在web服务器里运行），然而ie6、ie7的UserData通过代码封装可以统一到所有浏览器都支持web storage。`if(typeof window.localStorage == 'undefined'){...}`
        - 拥有方便的api（以sessionStorage为例，localStorage有完全同样用法）

            ```javascript
            /* setItem存储value(可以直接用"."和"[]"操作)*/
            window.sessionStorage.setItem("key1", "value1");    /* window.sessionStorage.key1 = "value1";或 window.sessionStorage['key1'] = "value1";*/

            /* getItem获取value(可以直接用"."和"[]"操作)*/
            var value1 = window.sessionStorage.getItem("key1");    /* var value1 = window.sessionStorage.key1或var value1 = window.sessionStorage['key1']*/

            /* removeItem删除key|value*/
            window.sessionStorage.removeItem("key1");

            /* 清除所有的key|value*/
            window.sessionStorage.clear();

            /* 遍历数据的key方法和length属性*/
            for (var i = 0; i  <  window.sessionStorage.length; i++){
                var key1 = window.sessionStorage.key(i);
                var value1 = window.sessionStorage.getItem(key1);
            }
            ```
        - `localStorage`:
            - 本地保存，字符串形式保存
            - 持久化本地存储
            - 同源,除非被清除，否则永久保存
            - 在所有同源窗口中共享（因为修改和访问的都是本地文件，因此随时修改一个会话的值,同域名下的其他会话的值也会变化).
            - 5m
            - 仅在客户端（即浏览器）中保存，不参与和服务器的通信
            - 源生接口方便操作（setItem,getItem,removeItem,clear等方法），亦可再次封装来对Object和Array有更好的支持
            - 应用场景:所有需要长期本地存储的数据
        - `sessionStorage`:
            - 本地保存，字符串形式保存
            - 会话级别存储
            - 同源且同会话(tab窗口)下有效,跳转页面为同源后仍旧有效，关闭页面或浏览器后被清除
            - 5m
            - 仅在客户端（即浏览器）中保存，不参与和服务器的通信
            - 源生接口方便操作（setItem,getItem,removeItem,clear等方法），亦可再次封装来对Object和Array有更好的支持
            - 应用场景:拆分成多个子页面的填写数据
            - 一个会话存储一个sessionStorage对象,不同tab的值不共通.
    - `cookie`:
        - 本地保存，字符串形式保存
        - 若不设置失效期则存储在内存中，若设置了失效期则存储在硬盘
        - 同源,默认是关闭浏览器后失效，设置失效时间则到期后才失效
        - 始终在同源的http请求中携带（即使不需要）
        - 单个cookie保存的数据不超过4k，单个域名有限制数量的cookie（最少20个）
        - 需要程序员自己封装get和set方法，源生的Cookie接口不友好
        - 应用场景:主要判断用户登录，需要个性化服务的需要用cookie来辨认用户
    - `session`:
        - 服务端保存，对象形式保存
        - 需要借助本地cookie进行控制
        - 无状态值（无法区分请求地址）