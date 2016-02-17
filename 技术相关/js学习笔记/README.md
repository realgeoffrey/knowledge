#js学习笔记

### `if`判断中用赋值操作
（大部分是误用）赋值的内容Boolen后为假会导致条件判断为假：`if(a = false){/* 不执行*/}`。

### 判断jQuery选择器选择到空内容
无论选择器选取的内容是否为空，都返回数组，所以`if($(...)) {...}`永远成立。因此用以下方法

- `if($(...).length > 0) {...}`
- `if($(...)[]) {...}/* 若无则为undefined*/`

### 判断类型
- `Object.prototype.toString.apply(值)`（或call）

    >[ECMA]When the toString method is called, the following steps are taken:
    >   - If the this value is undefined, return "[object Undefined]".
    >   - If the this value is null, return "[object Null]".
    >   - Let O be the result of calling ToObject passing the this value as the argument.
    >   - Let class be the value of the [[Class]] internal property of O.
    >   - Return the String value that is the result of concatenating the three Strings **"[object ", class, and "]"**.

    - 如果this的值为undefined，则返回"[object Undefined]"。

        如果this的值为null，则返回"[object Null]"。

        让O成为调用ToObject(this)的结果。

        让class成为O的内部属性[[Class]]的值。

        返回三个字符串"[object "、class以及"]"连接后的新字符串。
    - 除了放入undefined或null外，放入**对象**，返回`"[object 构造函数的名称]"`的字符串

        `Object.prototype.toString.call(值);` -> 输出字符串
        - `undefined` 或 不填 -> `[object Undefined]`
        - `null` -> `[object Null]`
        - `function(){}`（匿名与不匿名） -> `[object Function]`
        - `{}` -> `[object Object]`

        只要是内置对象，则返回其构造函数名。举例为：
        - `[]` -> `[object Array]`
        - 数字 -> `[object Number]`
        - 字符串 -> `[object String]`
        - 布尔型对象 -> `[object Boolean]`
        - Date对象 -> `[object Date]`
        - RegExp对象 -> `[object RegExp]`
        - arguments对象 -> `[object Arguments]`
        - Error对象 -> `[object Error]`
        - Math对象 -> `[object Math]`
        - window对象 -> `[object global]`
        - document对象 -> `[object HTMLDocument]`
        - JSON对象 -> `[object JSON]`
        - Map对象 -> `[object Map]`
        - console对象 -> `[object Console]`

- `typeof 值`

- `值 instanceof 值`

- `值 in 值`

### 判断对象、方法是否定义
- 判断对象方法是否可以执行

    ```javascript
    /* 对象已经定义 && 对象不为null && 对象方法存在*/
    if (typeof obj !== "undefined" && obj !== null && typeof obj.func === "function") {
        /* 对象方法已定义 可执行*/
    }
    ```
- 判断全局对象方法是否可以执行

    ```javascript
    /* window的子对象存在 && 对象方法存在*/
    if (window.obj && typeof window.obj.func === "function") {
        /* 对象方法已定义 可执行*/
    }
    ```
- 判断是否需要重新定义

    ```javascript
    /* 对象不存在 || 对象不为null || 对象方法不存在*/
    if (typeof obj === "undefined" || obj === null || typeof obj.func !== "function") {
        /* 对象或对象方法没有定义 需重新定义*/
    }
    ```
- 变量已定义

    ```javascript
    /* 变量已定义（不排除null）*/
    if (typeof a !== 'undefined') {
        /* 对象已定义 可操作*/
    }
    ```

### JS性能
- 平稳退化：当浏览器不支持或禁用了JS功能后，访问者也能完成最基本的内容访问。
    - 为JS代码预留出退路（html标签添加属性链接，用js事件绑定去拦截浏览器默认行为）

        `<a href="真实地址" class="j-func">...</a>`

    - ~~伪协议`javascript:`~~

        `<a href="javascript: func();">...</a>`

    - ~~内嵌事件处理函数~~

        `<a href="#" onclick="func();return false;">...</a>`
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

### DOM加载步骤、jQuery的文档ready事件和js的onload事件顺序
1. 解析Html结构
2. 加载外部脚本和样式表文件
3. 解析并执行脚本代码
4. 构造Html DOM模型 ->完成后执行`$(document).ready(function(){});`
5. 加载图片等外部文件
6. 页面加载完毕 -> 完成后执行`window.onload();`

### web storage、cookie、session
- web storage（localStorage、sessionStorage）
    - 本地保存，字符串形式保存
    - 仅在客户端（即浏览器）中保存，不参与和服务器的通信
    - 除了ie6、ie7外其他浏览器都支持（ie及FF需在web服务器里运行）

        >ie6、ie7可以用它们独有的`UserData`代替使用
    - 拥有方便的api

        ```javascript
        /* 以sessionStorage为例，localStorage有完全同样用法*/
        /* setItem存储value（可以直接用"."和"[]"操作）*/
        sessionStorage.setItem("key1", "value1");
        sessionStorage.key2 = "value2"; /* 或 sessionStorage['key2'] = "value2";*/

        /* getItem获取value（可以直接用"."和"[]"操作）*/
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
            - 持久化本地存储。除非被清除，否则永久保存（因为修改和访问的都是本地文件，因此在一个会话中修改值，同域名下的其他会话的值也变化)
            - 5m
            - 应用场景：所有需要长期本地存储的数据
        2. `sessionStorage`
            - 同源且同会话（tab窗口）下共享
            - 会话级别存储。跳转页面为同源后仍旧有效，关闭浏览器后被清除（一个会话存储一个sessionStorage对象，不同tab的值不共通;关闭tab后恢复此tab可能恢复数据）
            - 5m
            - 应用场景：需要拆分成多个子页面的填写数据
- `cookie`：
    - 本地保存，字符串形式保存
    - 若不设置失效期则存储在内存中；若设置了失效期则存储在硬盘
    - 同源同路径，默认是关闭浏览器后失效，设置失效时间则到期后才失效
    - 始终在http请求中携带
    - 单个cookie保存的数据不超过4k，单个域名有限制数量的cookie（最少20个）
    - 需要程序员自己封装get和set方法，源生的Cookie接口不友好
    - 应用场景：主要判断用户登录，用于辨认不同用户以提供不同个性化服务
- `session`：
    - 服务端保存，对象形式保存
    - 无状态值（无法区分请求地址），需要借助本地cookie进行操作

### jQuery的`.on()`绑定效率
`$(event handler).on(event,selector,function(){})`

1. 执行`on`方法的时刻，把所有满足条件的DOM对象安装指定的内容，成为**event handler**。有且仅有这些event handler绑定成功；之后动态生成的也满足条件的对象不再安装；对已生效的event handler处理DOM也不会使绑定内容失效（除非删除）；在event handler内动态增删的**selector**都可以由条件判定是否生效绑定内容。
2. 绑定的event handler距离selector越近，效率越高。因此把selector都绑定在`$(document)``上是低效的。

### 自执行匿名函数
- `(function () {/* code*/}());`推荐
- `(function () {/* code*/})();`

### prototype
prototype属性是js函数的继承机制，是构造函数的属性，作用是为实例共享属性（或方法），`构造函数.prototype`和`实例对象.__proto__`（已弃用）指向同一个原型链。

由同一个构造函数实例化的不同对象，各自有不共享的属性和方法副本，改变一个实例内容不会影响其他实例；但共同引用的prototype对象则共享其中内容，修改了prototype对象就会影响所有该构造函数的实例。

对于构造函数`function Fun(){}`：

1. 覆盖原型链

    ```javascript
    Func.prototype = {
        fun2: function () {
            console.log('add fucntion fun1');
        },
        fun3: function () {
            console.log('add fucntion fun2');
        }
    };
    ```
2. 不覆盖，在原型链上添加

    ```javascript
    Func.prototype.fun2 = function () {
        console.log('add fucntion fun2');
    };
    Func.prototype.fun3 = function () {
        console.log('add fucntion fun3');
    };
    ```

### 注意点
- `var a = b = 1;   /* b没有var的声明*/`

    在function中用如上写法，第二个以后的变量自动变成没有var定义的状态，意味着如果之前没有声明，那么就转化为全局变量的声明。
- `if(var a = 1, b = 2, c = 3, false){ /* 不执行*/}`

    逗号运算符，从左往右依次执行，逻辑结果取最后一个值。
- html5的`audio`标签有自动播放属性`autoplay`，但ios系统是无法自动播放，可以设置触屏的时候开始播放

    ```html
    <audio src="1.mp3" controls="controls" autoplay="autoplay" id="audio">
        您的浏览器不支持 audio 标签
    </audio>

    <script>
        window.ontouchstart = function () {
            document.getElementById('audio').play();
            window.ontouchstart = null;
        }
    </script>
    ```
- 实例化（new）一个构造函数，得到的对象拥有构造函数内用`this`定义的属性（或方法），在构造函数内`var`的变量和`function`无法被这个对象使用，只能在构造函数里使用（类似私有变量）。

    相对于单全局变量，构造函数更加灵活，可以生成多个对象进行互相独立的操作。
- `this`：调用函数的那个对象

    ```javascript
    /* 函数作为某个对象的方法调用，this指向上级对象*/
    function test() {
        console.log(this.x);
    }

    x = 1;
    test(); /* 1 等价于window.test*/

    var obj = {};
    obj.x = 2;
    obj.func = test;
    obj.func(); /* 2*/


    /* apply或call调用，传入对象代替this调用*/
    var obj2 = {x: 3};
    obj.func.call(obj2);    /* 3*/


    /* 作为构造函数生成一个新对象，this指向这个新对象*/
    function Test2() {
        this.x = 4;
    }
    var obj3 = new Test2();
    console.log(obj3.x);    /* 4*/
    ```

### js代码风格规范（style guideline）
- 变量声明

    无论语句在何处，无论是否会真正执行到，所有的`var`语句的声明都提前到包含这段逻辑的函数的顶部执行。

    >建议：总是把所有变量声明都放在函数顶部，而不是散落在各个角落
- 函数声明

    也会被js引擎提前声明，因此代码中函数的调用可以出现在函数声明之前（变量命名法必须先声明：`var a = function(){...};`）。
    函数声明不应当出现在语句块之内（如条件语句等），语句块的函数也会提前声明，导致语义不清容易出错。

    >建议：先声明函数再使用。可以把函数声明紧接着放在变量声明之后
- 严格模式`use strict`

    可用于全局，也可以用于局部（如函数内）。

    >建议：不推荐用在全局作用域中，因为当有js文件合并时，一个文件的全局严格模式会导致整个文件都是严格模式。
    >全局可以用`(function(){'use strict'; /* 执行内容*/}());`匿名函数使用。
- 当要比较的两个值的类型不同时，`==`和`!=`都会强制类型转换;用`===`和`!==`则不会。（`switch`语句比较值是全等模式比较）

    >建议：都用`===`或`!==`进行比较
- 三元运算符应当仅仅用在条件赋值语句中，而不要作为if语句的替代。
    - ~~`condition ? func1() : func2();`~~
    - `var a = condition ? '1' : '2';`

- 命名
    - 变量命名的前缀应当是**名词**，函数命名的前缀应当是**动词**
    - 约定函数名：
        - `can`、`has`、`is`开头的返回值是布尔型
        - `get`开头的返回是非布尔型
        - `set`开头的执行保存动作
    - 常量用大写字母和下划线分割，如`MAX_COUNT`
    - 构造函数用大驼峰命名法（Pascal Case），首字母大写（以非动词开头），单词首字母大写。这样对于首字母大写的函数即可认定为构造函数，否则为普通函数。

        - `var a = new Person();    /* 构造函数*/`
        - `var b = getPerson();    /* 普通函数*/`
    - 不要用多行的字符串写法

        ```javascript
        /* 不提倡的多行写法*/
        var a = 'abc\
        def';

        /* 一般写法*/
        var b = 'abc' + 'def';
        ```
    - 直接量
        - 对象直接量

            用直接量代替`Object`构造函数
            ```javascript
            /* 不提倡的构造函数写法*/
            var a = new Object();
            a.attr1 = '...';

            /* 直接量*/
            var b = {attr1: '...'};
            ```
        - 数组直接量

            用直接量代替`Array`构造函数
            ```javascript
            /* 不提倡的构造函数写法*/
            var arr1 = new Array("a", "b");

            /* 直接量*/
            var arr2 = ["a", "b"];
            ```
    - 对象的属性、方法，与变量、方法命名规则相同，若属性、方法是私有的，应当在之前加一个下划线`_`

### jQuery或Zepto相关
- 长字符串连使用`.join()`：

    ```javascript
    var arr = [],
        i;

    for (i = 0; i < 100; i++) {
        arr[i] = '字符串' + i + '字符串';
    }

    $('body').text(arr.join(''));
    ```

    而不使用`+`：
     ```javascript
    var text = '',
        i;

    for (i = 0; i < 100; i++) {
        text = text + '字符串' + i + '字符串';
    }

    $('body').text(text);
    ```
- 判断是否加载成功，不成功则执行载入本地文件

    ```html
    <script>
        window.jQuery || document.write('<script src="本地地址"><\/script>');
    </script>
    ```
- 当变量是jQuery或Zepto对象是，可以用`$`作为开头命名，利于区别与普通变量的区别

    ```javascript
    var a = 1;
    var $a = $('a');
    ```
- 选择器
    1. `$('子','父') === $('父').find('子')`

        找到所有父级，若子级在此父级后面，则选择。
    2. ~~`$('父 子')`~~

        找到所有子级，然后向前找出有父级的，则选择（性能差）。

### 移动端相关
- 移动端或者Zepto的`tap事件`点透bug解决
>移动端触摸事件顺序：touchstart->touchmove->touchend->click，tap事件发生后300ms才触发click事件。
>在使用Zepto框架的tap相关方法时，若绑定tap方法的dom元素在tap方法触发后会隐藏、css3 transfer移走、requestAnimationFrame移走等，而“隐藏、移走”后，
>它底下同一位置正好有一个dom元素绑定了click的事件、或者有浏览器认为可以被点击有交互反应的dom元素（默认），则会出现“点透”现象。

    1. 使用`fastclick.js`后用`click`代替tap
    2. 使用缓动动画，过度300ms延迟
    3. 中间增加一层接受这个点透事件，然后去除此层
