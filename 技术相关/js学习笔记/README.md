## 技巧经验

### DOM加载步骤、jQuery文档ready事件和js的onload事件顺序
1. 解析Html结构
2. 加载外部脚本和样式表文件
3. 解析并执行脚本代码
4. 构造Html DOM模型 -> 完成后执行`$(document).ready(function(){});`
5. 加载图片等外部文件
6. 页面加载完毕 -> 完成后执行`window.onload();`

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

    在局部作用域中用如上写法，第二个以后的变量自动变成没有var定义的状态，意味着如果之前没有声明，那么就转化为全局变量的声明。
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
- 实例化（new）一个构造函数，得到的对象拥有构造函数内用`this`定义的属性（或方法）以及原型链上的属性（或方法），在构造函数内`var`的变量和`function`无法被这个对象使用，只能在构造函数里使用（类似私有变量）。

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
- 浮点数的计算

    浮点数值计算会产生舍入误差，因此永远不要用条件语句判断某个特定浮点数值，也不要用js进行复杂的计算
- 判断DOM是否支持某属性

    若要判定一个属性是否被DOM所支持，新建一个DOM来判断：`if('属性' in document.creatElement('某标签')){...}`

    >在DOM中随意添加一个属性（DOM所没有的也可以），`此属性 in 此DOM`永远为真，不可以判断是否此DOM存在此属性（或方法）。
- `if`判断中用赋值操作

    （大部分是误用）赋值的内容Boolen后为假会导致条件判断为假：`if(a = false){/* 不执行*/}`。

### Boolean转换
| 数据类型 | 转换为true的值 | 转换为false的值 |
| ------------- | ------------- | ------------- |
| Boolean | true | false |
| String | 任何非空字符串 | ""（空字符串） |
| Number | 任何非零数值（包括无穷大） | 0和NaN |
| Object | 任何对象 | null |
| undefined | n/a | undefined |

>`!!变量`等价于`Boolean(变量)`。

### js代码风格规范（style guideline）
- 声明
    - 变量声明

        无论语句在何处，无论是否会真正执行到，所有的`var`语句的声明都提前到作用域顶部执行。

        >建议：总是把所有变量声明都放在函数顶部，而不是散落在各个角落
    - 函数声明

        也会被js引擎提前声明，因此代码中函数的调用可以出现在函数声明之前（变量命名法必须先声明：`var a = function(){...};`）。
        函数声明不应当出现在语句块之内（如条件语句等），语句块的函数也会提前声明，导致语义不清容易出错。

    >建议：先声明再使用。把函数声明紧接着放在变量声明之后
- 严格模式`use strict`

    可用于全局，也可以用于局部（如函数内）。

    >建议：不推荐用在全局作用域中，因为当有js文件合并时，一个文件的全局严格模式会导致整个文件都是严格模式。
    >全局可以用`(function(){'use strict'; /* 执行内容*/}());`匿名函数方式使用。
- 当要比较的两个值的类型不同时，`==`和`!=`都会强制类型转换；用`===`和`!==`则不会。（`switch`语句比较值是全等模式比较）

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
    - 构造函数用大驼峰命名法（Pascal Case），首字母大写（以非动词开头），单词首字母大写。
        - `var a = new Person();    /* 构造函数*/`
        - `var b = getPerson();    /* 普通函数*/`

        >这样对于首字母大写的函数即可认定为构造函数，否则为普通函数。
    - 不要用多行的字符串写法

        ```javascript
        /* 不提倡的多行写法*/
        var a = 'abc\
        def';

        /* 一般写法*/
        var b = 'abc' +
            'def';
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
    - 对象的属性、方法，与变量、方法命名规则相同
    - 若属性、方法是私有的，应当在之前加一个下划线`_`
- 注释规范
    - 单行注释

        ‘//’后不空格

        - 使用场景

            1. 代码上方独占一行，缩进与备注内容一致，注释前必须空一行
            2. 代码尾部，至少一个缩进（若注释太长则必须挪到代码上方）
            3. 被注释的大段代码
    - 多行注释

        ‘\*’或‘/\*’后空一格

        - 代码上方独占多行，缩进与备注内容一致，注释前必须空一行
        - 使用场景
            1. 难以理解的代码
            2. 可能被误认为错误的代码
            3. 浏览器特性hack
    - 函数注释规范

        ```javascript
        /*
         * 函数说明
         * @param {Object} param1 [1|2|3] 参数描述
         * @param {String|Object} param2 参数描述
         * @param {类型1|类型2} 参数名 [取值1|取值2] 描述
         * @returns {Object} result 参数描述
         */
        function func(param1, param2) {
            /* 代码*/

            return result;
        }
        ```

### 编程实践
- UI层的松耦合
    - 不要用js修改css样式，只修改class（任何时刻，css中的样式都可以修改，而不必更新js）。

        >特例：根据页面重新定位，可以用js设定定位置。
    - 将html从js中抽离，避免增加跟踪文本和结构性问题的复杂度。可以使用一些模板类，如baidu模板。
- 避免使用全局变量

    >任何来自函数外的数据都应当以参数形式传递进函数，这样做可以将函数与其外部环境隔离开来，并且修改不会对程序其他部分造成影响。

    - 单全局变量

        所创建的这个唯一全局对象名是独一无二的（不与内置API冲突），并将你所有的功能代码都挂载到这个全局对象上，因此每个可能的全局变量都成为唯一全局对象的属性（或方法），从而不会创建多个全局变量。
    - 零全局变量

        当不与其他代码产生交互，不需要直接引用任何全局变量，可以使用此法。使用场景有限。例：

        ```javascript
        (function (win) {
            'use strict';
            /* 严格模式可以避免创建全局变量*/

            var doc = win.document;
            /* 代码*/
        }(window));
        ```
- 事件处理
    - 把事件处理（与用户行为相关的代码）与应用逻辑（与应用相关的功能性代码）隔离开。
    - 不要分发事件：

        让事件处理函数成为接触到`event`对象的唯一函数，在event进入应用逻辑前进行包括阻止默认事件或阻止冒泡等操作。
- 将配置数据从代码中分离

    配置数据：URL、展示给用户的字符串、重复的值、设置、任何可能发生变更的值。

### 判断jQuery选择器选择到空内容
无论选择器选取的内容是否为空，都返回数组，所以`if($(...)) {/* 永远执行*/}`永远成立。因此用以下方法：

- `if($(...).length > 0) {/* 代码*/}`
- `if($(...)[]) {/* 代码*/}   /* 若无则为undefined*/`

### 移动端相关
- 移动端或者Zepto的`tap事件`点透bug解决
>移动端触摸事件顺序：touchstart->touchmove->touchend->click，tap事件发生后300ms才触发click事件。
>在使用Zepto框架的tap相关方法时，若绑定tap方法的dom元素在tap方法触发后会隐藏、css3 transfer移走、requestAnimationFrame移走等，而“隐藏、移走”后，
>它底下同一位置正好有一个dom元素绑定了click的事件、或者有浏览器认为可以被点击有交互反应的dom元素（默认），则会出现“点透”现象。

    1. 使用`fastclick.js`后用`click`代替tap
    2. 使用缓动动画，过度300ms延迟
    3. 中间增加一层接受这个点透事件，然后去除此层


## 功能用法

### 判断类型
- `Object.prototype.toString.apply(值);  /* 或call*/`

    - ECMA解释：

        如果this的值为undefined，则返回"[object Undefined]"。

        如果this的值为null，则返回"[object Null]"。

        让O成为调用ToObject(this)的结果。

        让class成为O的内部属性[[Class]]的值。

        返回三个字符串"[object "、class以及"]"连接后的新字符串。

        >[ECMA]When the toString method is called, the following steps are taken:
        >   - If the this value is undefined, return "[object Undefined]".
        >   - If the this value is null, return "[object Null]".
        >   - Let O be the result of calling ToObject passing the this value as the argument.
        >   - Let class be the value of the [[Class]] internal property of O.
        >   - Return the String value that is the result of concatenating the three Strings **"[object ", class, and "]"**.
    - 除了放入*undefined*或*null*外，放入**对象**，返回`"[object 构造函数的名称]"`的字符串

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

    可以跨帧（iframe）。

    返回一个表示值类型的字符串。
    - 字符串 -> `"string"`
    - 布尔型 -> `"boolean"`
    - 数值型 -> `"number"`
    - `undefined` -> `"undefined"`
    - 引用型 -> `"object"`
    - **`null` -> `"object"`**
    - 函数 -> `"function"`

    >因为`typeof null`返回`"object"`，因此typeof不能判断是否是引用类型。
    >
    >ie8-的DOM节点的方法返回不是~~`function`~~，而是`object`，因此只能用`方法名 in DOM`检测DOM是否拥有某方法。

- `对象 instanceof 构造函数`

    不能跨帧（iframe）。

    判断是否是对象的构造函数（判断某个构造函数的prototype属性所指向的对象是否存在于另外一个要检测对象的原型链上）。

    不仅检测对象本身，还检测至原型链。如`new Number() instanceof Object`返回true。

    **检测自定义类型的唯一方法。**
- `属性 in 对象`

    仅判断属性是否存在检测的对象上，不会去读取属性值。

    检测至原型链。

    >`对象.hasOwnProperty(属性)`仅检查在当前实例对象，不检测其原型链。
    >
    >ie8-的DOM对象并非继承自Object对象，因此没有hasOwnProperty方法。

### 循环遍历
>`break`应用在循环（while、do-while、for、for-in）和switch。
>
>`continue`应用在循环。
>
>`$.each/obj.each`跳出循环用`return true`（功能类似于continue）和`return false`（功能类似于break）。

- `for-in`js原生语法

    ```javascript
    for (var i in obj) {

    }
    ```
    - obj为数组或对象，i为数组下标或对象属性名。
- `$.each()`jQuery方法

    ```javascript
    $.each(obj, function (index, element) {

    });
    ```
    - obj为数组或对象（原生或jQuery对象），index为数组下标或对象名，element为值（不是jQuery对象，是DOM对象，与this相同）。
- `obj.each()`jQuery方法

    ```javascript
    obj.each(function (index, element) {

    });
    ```
    - obj为jQuery对象，index为从0开始的下标，element为值（不是jQuery对象，是DOM对象，与this相同）。

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

### 自执行匿名函数
- `(function () {/* code*/}());`推荐
- `(function () {/* code*/})();`


## 性能原理

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

### 垃圾收集
垃圾收集器会按照固定的时间间隔（或代码执行中预定的时间）周期性地执行，找出不再继续使用的变量，然后释放其占用的内存。

垃圾收集器必须跟踪并判断变量是否有用，对于不再有用的变量打上标记，以备将来回收。
- 标记清除（mark-and-sweep）

    垃圾收集器在运行时给存储在内存中的所有变量加上标记；然后，去掉环境中的变量以及被环境中变量引用的变量的标记；最后，对那些带标记的值进行释放。
- 引用计数（reference counting）

    跟踪记录每个值被引用的次数，被引用一次加1，引用取消就减1，当引用次数为0时，则说明没有办法再访问这个值了，当垃圾收集器下次运行时，释放引用次数为0的值所占空间。

    >可能产生一个严重的问题：循环引用，引用次数永远不会是0

### 排版引擎与js引擎
- 排版引擎（layout engine）

    也称为浏览器内核（web browser engine）、页面渲染引擎（rendering engine）或样板引擎，是一种软件组件，负责获取标记式内容（如html、xml以及图像文件等）、整理信息（如css、xsl），并将排版后的内容输出至显示屏或打印机。
    所有网页浏览器、电子邮件客户端以及其他需要根据表示性的标记语言来显示内容的应用程序，都需要排版引擎。

    IE：Trident；Chrome：前WebKit，现Blink；Firefox：Gecko；Safari：WebKit；Opera：前Presto，现Blink；Edge：EdgeHTML。
- js引擎

    一个专门处理js脚本的虚拟机，一般会附带在网页浏览器中。

    JScript：ie8-，ASP；Chakra：ie9+，Edge；V8：Chrome，Opera，Nodejs，MongoDB；SpiderMonkey：Firefox；Nitro：Safari。

### 引用类型与基本类型的变量传递
- 只能给引用类型动态地添加属性和方法，不能给基本类型添加。
- js的变量传递都是**值传递**，都是把变量中存储的值复制一份给另一个变量。
    - 基本类型的复制

        把变量的值复制到新变量分配的位置上，两个变量可以参与任何操作而不会互相影响。
    - 引用类型的复制

        引用类型的变量保存的是指向该对象的指针(指针指向具体内容值)，复制给新变量指针后，两个变量实际上引用同一对象，改变其中一个变量，会影响另一个变量。

    >函数的参数也是同以上两种传递方式一样，区分基本类型或引用类型。

### 错误处理机制
- 原生错误类型

    1. SyntaxError

        解析代码发生语法错误时抛出。
    2. ReferenceError

        引用不存在的变量时抛出；另一种触发场景是，将一个值分配给无法分配的对象，比如对函数的运行结果或者this赋值。
    3. RangeError

        数值超出相应范围时抛出。
        主要有几种情况，一是数组长度为负数，二是Number对象的方法参数超出范围，以及函数堆栈超过最大值。
    4. TypeError

        变量或参数不是预期类型时抛出。
        比如，对字符串、布尔值、数值等原始类型的值使用new命令，就会抛出这种错误，因为new命令的参数应该是一个构造函数。
    5. URIError

        URI相关函数的参数不正确时抛出。
        主要涉及`encodeURI()`、`decodeURI()`、`encodeURIComponent()`、`decodeURIComponent()`、`escape()`和`unescape()`这六个函数。
    6. ~~EvalError~~

       使用`eval()`函数发生异常时抛出。

       >该错误类型已经不再在ES5中出现了，只是为了保证与以前代码兼容，才继续保留。

    >浏览器不会抛出`Error`类型的exception异常，所以如果捕获到`Error`类型的异常，可以确定这个异常是用户代码抛出的，不是浏览器抛出的。浏览器默认只会抛出Error的6个派生类型错误。

- Error对象属性

    Error有两个基本的属性`message`和`name`。
    `message`用来表示异常的详细信息；`name`指的的是Error对象的构造函数。

    此外，不同的js引擎对Error还各自提供了一些扩展属性。

- 代码中出现error

    当javascript代码中出现错误的时候，js引擎就会根据js的调用栈逐级寻找对应的`catch`，如果**没有找到相应的catch handler**或**catch handler本身又有error**或者**又抛出新的error**，就会把这个error交给浏览器，浏览器会用各自不同的方式（IE以黄色三角图案显示在左下角，而firefix会显示在错误控制台中）显示错误信息给访问者，可以用`window.onerror`进行控制。

    在某个**JavaScript block**（`<script>`标签）内，第一个错误触发后，当前Javascript block后面的代码会被自动忽略，不再执行，其他的JavaScript block内代码不被影响。

    - `try-catch-finally`

        `try`必须跟`catch`或`finally`或`catch + finally`同时出现。

        如果有`catch`，一旦`try`中抛出错误以后就先执行`catch`中的代码，然后执行`finally`中的代码；
        如果没有`catch`，`try`中的代码抛出错误后，就会先执行`finally`中的语句，然后将`try`中抛出的错误继续往上抛。

        如果`try`中代码是以`return`、`continue`或`break`终止的，必须先执行完`finally`中的语句后再执行相应的`try`中的返回语句。

        在`catch`中处理的错误，不会再向上提交给浏览器。
    - `window.onerror`

        没有通过`try-catch`处理的错误都会触发`window`对象的`onerror`。

        `window`对象有`onerror`属性，把一个方法赋值给此属性后，但凡这个window中有javascript错误出现，则会调用此方法。

        onerror方法会传入3个参数，分别是**错误信息提示**、**javascript产生错误的document url**和**错误出现的行号**。
        若方法返回`true`，浏览器不再显示错误信息；若返回`false`，浏览器还是会提示错误信息：

        ```javascript
        /*
         * window错误处理
         * @param {String} msg 错误信息提示
         * @param {String} url 错误出现url
         * @param {Number} line 错误出现行号
         * @returns {Boolean} [true|false] 不显示错误信息|显示
         */
        window.onerror = function (msg, url, line) {
            /* code*/

            return true;    /* 浏览器不再显示错误信息*/
        };
        ```
    - 图像的`error`事件

        只要图像的src属性中的URL不能返回可以被识别的图像格式，就会触发图像的error事件。

        - `<img>`标签的`onerror`事件

            ```html
            <img src="asdas" alt="" onerror="func();">
            ```
        - `Image`实例的属性

            ```javascript
            var img = new Image();
            img.onerror = function () {
                /* code*/
            };

            img.src = "错误地址";
            ```

        >不会提交到`window.onerror`。

>捕获错误的目的在于避免浏览器以默认方式处理它们；而抛出错误的目的在于提供错误发生具体原因的消息。

### jQuery的`.on()`绑定效率
`$(event handler).on(event,selector,function(){})`

1. 执行`on`方法的时刻，把所有满足条件的DOM对象安装指定的内容，成为**event handler**。有且仅有这些event handler绑定成功；之后动态生成的也满足条件的对象不再安装；对已生效的event handler处理DOM也不会使绑定内容失效（除非删除）；在event handler内动态增删的**selector**都可以由条件判定是否生效绑定内容。
2. 绑定的event handler距离selector越近，效率越高。因此把selector都绑定在`$(document)``上是低效的。

### jQuery或Zepto相关
- 长字符串连使用`.join()`，而不使用`+`：

    ```javascript
    /* 性能好*/
    var arr = [],
        i;

    for (i = 0; i < 100; i++) {
        arr[i] = '字符串' + i + '字符串';
    }

    $('body').text(arr.join(''));


    /* 性能差*/
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