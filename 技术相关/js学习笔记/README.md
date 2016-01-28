#js学习笔记

- if中用赋值（大部分是误用）并非总是返回真值，条件判断赋值内容Boolen后为假即判断为假：`if(a = false){...}`。

- 判断jQuery选择器选择到空内容

    无论选择器选取的内容是否为空，都返回数组，所以`if($(...)) {...}`永远成立。因此用以下方法
    - `if($(...).length > 0) {...}`
    - `if($(...)[]) {...}/* 若无则为undefined*/`

- 判断类型
    - `Object.prototype.toString.apply(值)`

        >[ECMA]When the toString method is called, the following steps are taken:
        >   - If the this value is undefined, return "[object Undefined]".
        >   - If the this value is null, return "[object Null]".
        >   - Let O be the result of calling ToObject passing the this value as the argument.
        >   - Let class be the value of the [[Class]] internal property of O.
        >   - Return the String value that is the result of concatenating the three Strings **"[object ", class, and "]"**.

        - 如果this的值为undefined,则返回"[object Undefined]".

          如果this的值为null,则返回"[object Null]".

          让O成为调用ToObject(this)的结果.

          让class成为O的内部属性[[Class]]的值.

          返回三个字符串"[object ", class, 以及 "]"连接后的新字符串.

    - `typeof 值`

    - `值 instanceof 值`

    - `值 in 值`

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

- web storage（localStorage、sessionStorage）、cookie、session
    - `web storage（localStorage、sessionStorage）`
        - 本地保存，字符串形式保存
        - 仅在客户端（即浏览器）中保存，不参与和服务器的通信
        - 除了ie6、ie7外其他浏览器都支持（ie及FF需在web服务器里运行）

            >ie6、ie7可以用它们独有的`UserData`代替使用（用对象检测封装）
        - 拥有方便的api

            ```javascript
            /* 以sessionStorage为例，localStorage有完全同样用法*/
            /* setItem存储value(可以直接用"."和"[]"操作)*/
            sessionStorage.setItem("key1", "value1");
            sessionStorage.key2 = "value2"; /* 或 sessionStorage['key2'] = "value2";*/

            /* getItem获取value(可以直接用"."和"[]"操作)*/
            var value1 = sessionStorage.getItem("key1");
            var value2 = sessionStorage.key2;   /* 或 var value1 = sessionStorage['key1']*/

            /* removeItem删除key|value*/
            sessionStorage.removeItem("key1");

            /* 清除所有的key|value*/
            sessionStorage.clear();

            /* 遍历数据的key方法和length属性*/
            for (var i = 0; i < sessionStorage.length; i++) {
                var key1 = sessionStorage.key(i);
                var value1 = sessionStorage.getItem(key1);
            }
            ```
        - localStorage、sessionStorage区别
            1. `localStorage`
                - 同源共享
                - 持久化本地存储。除非被清除，否则永久保存（因为修改和访问的都是本地文件，因此在一个会话中修改值,同域名下的其他会话的值也变化)
                - 5m
                - 应用场景:所有需要长期本地存储的数据
            2. `sessionStorage`
                - 同源且同会话(tab窗口)下共享
                - 会话级别存储。跳转页面为同源后仍旧有效，关闭浏览器后被清除（一个会话存储一个sessionStorage对象,不同tab的值不共通;关闭tab后恢复此tab可能恢复数据）
                - 5m
                - 应用场景:需要拆分成多个子页面的填写数据
    - `cookie`:
        - 本地保存，字符串形式保存
        - 若不设置失效期则存储在内存中；若设置了失效期则存储在硬盘
        - 同源同路径,默认是关闭浏览器后失效，设置失效时间则到期后才失效
        - 始终在http请求中携带
        - 单个cookie保存的数据不超过4k，单个域名有限制数量的cookie（最少20个）
        - 需要程序员自己封装get和set方法，源生的Cookie接口不友好
        - 应用场景:主要判断用户登录，用于辨认不同用户以提供不同个性化服务
    - `session`:
        - 服务端保存，对象形式保存
        - 无状态值（无法区分请求地址），需要借助本地cookie进行操作