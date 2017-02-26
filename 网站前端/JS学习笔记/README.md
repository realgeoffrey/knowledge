# JS学习笔记

## 技巧经验

### 易错点 or Tips
1. `var a = b = 1;   /* b没有var的声明*/`

    在局部作用域中用如上写法，第二个以后的变量自动变成没有var定义的状态，意味着如果之前没有声明，那么就转化为全局变量的声明。
2. `var a = a || {};`

    1. 先声明提前`var a;`；
    2. 接着右侧的表达式`a || {}`先执行：根据规则先判断a的值是否为真，如果a为真，则返回a；如果a不为真，则返回后面的{}；
    3. 最后再将结果赋值给`a`。

    等价于：
    ```javascript
    /* 不是形参情况*/
    var a;

    if (a === 0 || a === "" || a === false || a === null || a === undefined) {
        a = {};
    }

    /* 形参情况*/
    function func(b) {
        if (b === 0 || b === "" || b === false || b === null || b === undefined) {
            b = {};
        }
    }
    ```
    >`var a = b || {};`与`if (c) {}`会因为b或c没有定义而报错，可以用`typeof`来使代码健壮：
    >
    >1. `var a = typeof b !== 'undefined' && b !== null ? b : {};`
    >2. `if (typeof c !== 'undefined' && c !== null) {}`
3. `if(var a = 1, b = 2, c = 3, false){ /* 不执行*/}`

    逗号操作符`,`对每个操作对象求值（从左至右），然后返回最后一个操作对象的值。

    >`var`语句中的逗号不是逗号操作符，因为它不是存在于一个表达式中。尽管从实际效果来看，那个逗号同逗号运算符的表现很相似。但确切地说，它是`var`语句中的一个特殊符号，用于把多个变量声明结合成一个。
4. `var a = [10, 20, 30, 40][1, 2, 3];   /* 40*/`

    1. `[10, 20, 30, 40]`被解析为数组；
    2. `[1, 2, 3]`被解析为属性调用，逗号操作符取最后一个值为结果。

    因此结果为数组`[10, 20, 30, 40]`的`[3]`属性值：`40`。
5. HTML5的`audio`标签的自动播放属性`autoplay`

    wap端的部分浏览器无法自动播放，可以设置触屏的时候开始播放：

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
6. 浮点数的计算

    浮点数值计算会产生舍入误差，因此永远不要用条件语句判断某个特定浮点数值，也不要用JS进行复杂的计算。
    >避免浮点数运算误差函数：[用整数进行小数的四则运算](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/JS方法积累/实用方法/README.md#原生js用整数进行小数的四则运算避免浮点数运算误差)。
7. 判断DOM是否支持某属性

    若要判定一个属性是否被DOM所支持，新建一个DOM来判断：`if('属性' in document.creatElement('某标签')){...}`。
    >在DOM中随意添加一个属性（DOM所没有的也可以），`此属性 in 此DOM`永远为真，不可以判断是否此DOM存在此属性（或方法）。
8. `eval`中直接执行`function`声明无效，必须用引号把`function`声明包裹起来才有效（尽量不用`eval`）

    ```javascript
    eval(function a() {});  /* 返回function a() {}，但是没有声明*/
    eval('function b() {}');    /* 返回undefined，声明成功*/
    ```

    >1. `if()`中的代码对于`function`的声明就是用`eval`带入方法当做参数，因此虽然返回true，但是方法没有被声明。
    >2. `setTimeout`与`setInterval`中第一个参数若使用字符串，也是使用`eval`把字符串转化为代码。
9. `if`、`for`以及`while`之类的判断语句中用赋值操作

    （大部分是误用）赋值的内容Boolen后为假会导致条件判断为假：`if(a = false){/* 不执行*/}`。
    >判断语句内只判断整体返回值是`true`还是`false`，与里面执行内容无关（尽管对其语法有所限制）。

### JS和jQuery（Zepto）获取的位置信息（纵轴为例）
1. DOM节点

    > `dom`为JS对象，`$dom`为jQuery（或Zepto）对象。

    1. 节点高度：

        1. 高度+padding：

            `dom.clientHeight` 或 `$dom.innerHeight()`
        2. 高度+padding+border：

            `dom.offsetHeight` 或 `$dom.outerHeight()`
    2. 节点内容高度：

        `dom.scrollHeight`
    3. 节点内滚动距离：

        `dom.scrollTop` 或 `$dom.scrollTop()`
    4. 节点顶部距离屏幕顶部：

        `dom.getBoundingClientRect().top - document.documentElement.clientTop`

        或

        `$dom.offset().top - $(window).scrollTop()`

        > 节点底部距离屏幕顶部：`dom.getBoundingClientRect().bottom`。
    5. 节点顶部距离文档顶部：

        `dom.getBoundingClientRect().top - document.documentElement.clientTop + (document.body.scrollTop || document.documentElement.scrollTop)`

        或

        `$dom.offset().top`
2. 文档和视窗

    1. 视窗高度：

        `window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight`

        或

        `$(window).height()`
    2. 文档内容高度：

        `document.body.scrollHeight` 或 `$(document).height()`
    3. 文档滚动高度：

        `document.body.scrollTop || document.documentElement.scrollTop` 或 `$(window).scrollTop()`

>Zepto没有`innerHeight`和`outerHeight`，改为`height`。

### 节点与屏幕距离关系
1. jQuery或Zepto

    1. 节点**顶部**在**屏幕底部**以上

        `$dom.offset().top <= $(window).scrollTop() + $(window).height()`
    2. 节点**底部**在**屏幕顶部**以下

        `$dom.offset().top + $dom.outerHeight() >= $(window).scrollTop()`
    3. 节点在屏幕内

        以上`&&`结合。
2. 原生JS

    > 屏幕高度 = `window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight` 或 `$(window).height()`。

    1. 节点**顶部**在**屏幕底部**以上

        `dom.getBoundingClientRect().top <= 屏幕高度`
    2. 节点**底部**在**屏幕顶部**以下

        `dom.getBoundingClientRect().bottom >= 0`
    3. 节点在屏幕内

        以上`&&`结合。

### 滚动定位
> 也可以给底部（或顶部）放置一个标记节点，当**这个节点的顶部在容器底部以上（或这个节点的底部在容器顶部以下）**时为滚动到底部（或顶部）。

1. DOM节点

    1. 内容滚动到底部：

        `dom.offsetHeight + dom.scrollTop >= dom.scrollHeight`
    2. 内容滚动到顶部：

        `dom.scrollTop === 0`
2. 文档

    >1. 屏幕高度 = `window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight` 或 `$(window).height()`
    >2. 文档滚动高度 = `document.body.scrollTop || document.documentElement.scrollTop` 或 `$(window).scrollTop()`
    >3. 文档内容高度 = `document.body.scrollHeight` 或 `$(document).height()`

    1. 滚动到底部：

        `屏幕高度 + 文档滚动高度 >= 文档内容高度`
    2. 滚动到顶部：

        `文档滚动高度 === 0`

### 数组的值传递
对于数组`arr`：

1. 清空数组

    1. `arr = [];   /* 不改变原始数组（新赋值一个空数组）*/`
    2. `arr.length = 0; /* 改变原始数组*/`
    3. `arr.splice(0, arr.length);  /* 改变原始数组*/`
2. 操作数组形参，不改变数组实参

    1. 浅复制：`arr = arr.slice(0);`
    2. 深复制：？

### JS代码风格规范（style guideline）
1. 声明

    1. 变量声明

        无论语句在何处，无论是否会真正执行到，所有的`var`语句的**声明**都提前到作用域（函数内部或者全局）顶部执行（hoisting），但是具体**赋值**不会被提前。

        >e.g.
        >```javascript
        >var a = 1;
        >
        >(function () {
        >    console.log(a);    /* undefined*/
        >
        >    var a = 2;
        >
        >    console.log(a);    /* 2*/
        >})();
        >
        >//等效于：
        >var a = 1;
        >
        >(function () {
        >    var a;
        >    console.log(a);    /* undefined*/
        >
        >    a = 2;
        >
        >    console.log(a);    /* 2*/
        >})();

        声明变量是它所在上下文环境的不可配置属性（non-configurable property），非声明变量是可配置的（例如非声明变量可以被`delete`）。

        >建议：总是把所有变量声明都放在函数顶部，而不是散落在各个角落。

        相同作用域中，对同一个变量进行多次声明，则忽略第一次之后的声明（会执行变量赋值）。
    2. 函数声明

        也会被JS引擎提前到作用域顶部声明，因此代码中函数的调用可以出现在函数声明之前。

        >函数声明不应当出现在语句块之内（如条件语句等），语句块的函数也会提前声明，导致语义不清容易出错。
    3. 函数表达式（Function expressions）声明

        必须先声明：`var a = function(){...};`才可以使用，声明会被提前，但赋值不会被提前。
    4. 同名的变量声明和函数声明

        同时声明的情况下（顺序不影响结果）：
        1. 变量仅声明不赋值：被赋值为函数。
        2. 变量赋值：被赋值为变量。

        >e.g.
        >```javascript
        >var a1 = 1;
        >function a1() {}
        >console.log(a1);    /* 1*/
        >
        >
        >function b2() {}
        >var b2 = 1;
        >console.log(b2);    /* 1*/
        >
        >
        >var c3;
        >function c3() {}
        >console.log(c3);    /* function*/
        >
        >
        >function d4() {}
        >var d4;
        >console.log(d4);    /* function*/
        >```

    >建议：先声明再使用。把函数声明紧接着放在变量声明之后。

2. 严格模式`use strict`

    可用于全局，也可以用于局部（如函数内）。

    >不推荐用在全局作用域中，因为当有JS文件合并时，一个文件的全局严格模式会导致整个文件都是严格模式。
    >全局可以用`(function(){'use strict'; /* 执行内容*/}());`匿名函数方式使用。
3. 全等`===`（不全等`!==`）与等号`==`（不等`!=`）区别

    1. 当比较的两个值的类型不同时，`==`和`!=`都会强制类型转换，再进行转换后值的比较；

    2. 用`===`和`!==`则不会转换，直接返回`false`（`switch`语句比较值是全等模式比较）。

    >建议：都用`===`或`!==`进行比较。
4. 等号与不等号进行的强制类型转换步骤

    1. 首先看运算数有没有`NaN`，如果存在`NaN`，一律返回`false`。
    2. 再看运算数有没有`布尔值`，有布尔就将布尔转换为`数字`（`false`是`0`，`true`是`1`）。
    3. 接着看运算数有没有`字符串`, 有三种情况：

        1. 对方是`对象`，对象使用`toString`进行转换；
        2. 对方是`数字`，字符串转数字；
        3. 对方是`字符串`，直接比较；
        4. 其他返回`false`。
    4. 如果是`数字`，对方是`对象`，对象取`valueOf`进行比较, 其他一律返回`false`。
    5. 如果运算数都是`对象`，那么比较的是它们的`引用值`。如果两个运算数指向同一对象，那么返回`true`，否则`false`。
    6. `null`与`undefined`不会进行类型转换, 但它们俩相等。
5. 三元运算符应当仅仅用在条件赋值语句中，而不要作为if语句的替代。

    1. ~~`condition ? func1() : func2();`~~
    2. `var a = condition ? '1' : '2';`
6. 命名

    1. 变量命名的前缀应当是**名词**，函数命名的前缀应当是**动词**。
    2. 约定函数名：

        1. `can`、`has`、`is`开头的返回值是布尔型。
        2. `get`开头的返回是非布尔型。
        3. `set`开头的执行保存动作。
    3. 常量用大写字母和下划线分割，如`MAX_COUNT`。
    4. 构造函数用大驼峰命名法（Pascal Case），首字母大写（以非动词开头），单词首字母大写：

        1. `var a = new Person();    /* 构造函数*/`
        2. `var b = getPerson();    /* 普通函数*/`

        >这样对于首字母大写的函数即可认定为构造函数，否则为普通函数。
    5. 不要用多行的字符串写法

        ```javascript
        /* 不提倡的多行写法*/
        var a = 'abc\
        def';

        /* 一般写法*/
        var b = 'abc' +
            'def';
        ```
    6. 对象的属性、方法，与变量、方法命名规则相同。
    7. 若属性、变量、方法在表示其是私有的，可在之前加一个下划线`_`作为区分。
7. 使用直接量

    1. 对象直接量

        用直接量代替`Object`构造函数：

        ```javascript
        /* 不提倡的构造函数写法*/
        var a = new Object();
        a.attr1 = '...';

        /* 提倡的直接量*/
        var b = {attr1: '...'};
        ```
    2. 数组直接量

        用直接量代替`Array`构造函数：

        ```javascript
        /* 不提倡的构造函数写法*/
        var arr1 = new Array('a', 'b');

        /* 提倡的直接量*/
        var arr2 = ['a', 'b'];
        ```
8. 注释规范

    1. 单行注释

        `//`后不空格

        - 使用场景：

            1. 代码上方独占一行，缩进与备注内容一致，注释前必须空一行。
            2. 代码尾部，至少一个缩进（若注释太长则必须挪到代码上方）。
            3. 被注释的大段代码。
    2. 多行注释

        `/*`和`*`后空一格

        - 代码上方独占多行，缩进与备注内容一致，注释前必须空一行。
        - 使用场景：

            1. 难以理解的代码。
            2. 可能被误认为错误的代码。
            3. 浏览器特性hack。
    3. 函数注释规范（使用部分[JSDoc](http://usejsdoc.org/)）

        ```javascript
        /**
         * 方法描述
         * @constructor - （是否构造函数）
         * @param {Number} param1 - 参数描述，限制值为：1 描述|2 描述|3 描述
         * @param {Object|String|Boolean|Function|Array} param2 - 参数描述
         * @param {*} param3 = 'default' - 拥有默认值
         * @param {*} [param4] - 可选参数
         * @param [param5 = 'default'] - 可选参数拥有默认值
         * @param {...Number} param6 - 可重复使用参数
         * @returns {Object|Undefined} result - 参数描述
         */
        function func(param1, param2, param3, param4, param5, param6) {

            return result;
        }
        ```

9. [JS编程风格总结](http://www.ruanyifeng.com/blog/2012/04/javascript_programming_style.html)（programming style）

    1. 表示区块起首的大括号，不要另起一行。
    2. 调用函数的时候，函数名与左括号之间没有空格。
    3. 函数名与参数序列之间，没有空格。
    4. 所有其他语法元素与左括号之间，都有一个空格。
    5. 不要省略句末的分号。
    6. 不要使用with语句。
    7. 不要使用“相等”（==）运算符，只使用“严格相等”（===）运算符。
    8. 不要将不同目的的语句，合并成一行。
    9. 所有变量声明都放在函数的头部。
    10. 所有函数都在使用之前定义。
    11. 避免使用全局变量；*如果不得不使用，用大写字母表示变量名。*
    12. 不要使用new命令，改用Object.create()命令。
    13. 建构函数的函数名，采用首字母大写；其他函数名，一律首字母小写。
    14. 不要使用自增（++）和自减（--）运算符，用+=和-=代替。
    15. 总是使用大括号表示区块。

### 编程实践
1. UI层的松耦合

    1. 不要~~用JS修改CSS样式~~，JS只修改class（任何时刻，CSS中的样式都可以修改，而不必更新JS）。

        >特例：根据页面重新定位，可以用JS设定定位置（如`top`、`bottom`等）。
    2. 将HTML从JS中抽离，避免增加跟踪文本和结构性问题的复杂度。可以使用模板引擎，如[handlebars.js](https://github.com/wycats/handlebars.js)。
2. 避免使用全局变量

    >任何来自函数外的数据都应当以参数形式传递进函数，这样做可以将函数与其外部环境隔离开来，并且修改不会对程序其他部分造成影响。

    1. 单全局变量

        所创建的这个唯一全局对象名是独一无二的（不与内置API冲突），并将你所有的功能代码都挂载到这个全局对象上，因此每个可能的全局变量都成为唯一全局对象的属性（或方法），从而不会创建多个全局变量。
    2. 零全局变量（匿名函数）

        当不与其他代码产生交互，不需要直接引用任何全局变量，可以使用此法（使用场景有限）。例：

        ```javascript
        (function (win) {
            'use strict';
            /* 严格模式可以避免创建全局变量*/

            var doc = win.document;
            /* 代码*/
        }(window));
        ```
3. 事件处理

    1. 把事件处理（与用户行为相关的代码）与应用逻辑（与应用相关的功能性代码）隔离开。
    2. 不要分发事件：

        让事件处理函数成为接触到`event`对象的唯一函数，在event进入应用逻辑前完成用户相关操作（包括阻止默认事件或阻止冒泡等）。

    >JS的自定义事件建议直接使用jQuery的自定义事件：
    >```javascript
    >$('选择器').on('自定义事件', function () {});
    >$('选择器').trigger('自定义事件');
    >```
4. 将配置数据从代码中分离

    配置数据：URL、展示给用户的字符串、重复的值、设置、任何可能发生变更的值。

### 设计模式
1. 构造函数

    1. 普通版：

        ```javascript
        var oneConstructor = function () {
            /* 私有的内容*/
            var _para = {a: '私有的变量_para'},
                _func = function () {
                    console.log('私有的业务逻辑_func');
                },
                _bindEvent = function () {  /* 绑定事件*/
                    $(document).on('click', function () {
                        console.log(_para);
                    });
                },
                _init = function () {   /* 初始化*/
                    _func();
                    _bindEvent();
                };

            _init();

            for (var _arr = [], _i = 0; _i < arguments.length; _i++) {
                _arr.push(arguments[_i]);
            }

            /* 公开的内容*/
            this.para = _arr;   /* 形参*/
            this.para_1 = {b: '公开的变量para_1（每个实例不共享）'};
            this.func_1 = function () {
                console.log('公开的业务逻辑func_1（每个实例不共享）');
            };
        };
        ```
    2. 拥有原型链内容（所有实例都共享）：

        ```javascript
        var oneConstructor = (function () {
            /* 私有的内容*/
            var _para = {a: '私有的变量_para'},
                _func = function () {
                    console.log('私有的业务逻辑_func');
                },
                _bindEvent = function () {  /* 绑定事件*/
                    $(document).on('click', function () {
                        console.log(_para);
                    });
                },
                _init = function () {   /* 初始化*/
                    _func();
                    _bindEvent();
                };

            function Constructor() {
                _init();

                for (var _arr = [], _i = 0; _i < arguments.length; _i++) {
                    _arr.push(arguments[_i]);
                }

                /* 公开的内容*/
                this.para = _arr;   /* 形参*/
                this.para_1 = {b: '公开的变量para_1（每个实例不共享）'};
                this.func_1 = function () {
                    console.log('公开的业务逻辑func_1（每个实例不共享）');
                };
            }

            /* 原型链上，每个实例共享*/
            Constructor.prototype = {
                para_2: {c: '公开的变量para_2（在原型链上，每个实例共享）'},
                func_2: function () {
                    console.log('公开的业务逻辑func_2（在原型链上，每个实例共享）');
                }
            };

            /* 原型对象添加constructor属性*/
            if (typeof Object.defineProperty === 'function') {

                /* 使属性：不可以改变描述符、不可以删除、不可以枚举、不可以被赋值运算符改变*/
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
        /* 私有变量和私有方法，无法直接访问，只能由return的对象字面量访问*/
        var _para = {a: '私有变量'},
            _func = function () {
                console.log('私有方法');
            };

        /* 单例模式，可以访问私有内容*/
        return {
            get: function () {  /* 特权方法*/
                _func();

                return _para;
            },
            set: function (para) {  /* 特权方法*/
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

### wap端点透bug
>1. pc端没有`touch`一系列事件。
>2. wap端有`touchstart`、`touchmove`、`touchend`、`touchcancel`等`touch`一系列事件。
>3. Zepto用`touch`一系列事件封装了`tap`事件。

- 点透现象：

    使用Zepto的`tap`事件绑定（或直接使用`touchstart`绑定）后，若此元素在触摸事件发生后离开原始位置（CSS或JS方式），底下同一位置正好有一个DOM元素绑定了`click`事件或有一个a标签，则会出现“点透”bug（触发了底下元素的点击事件）。
- 原因：

    wap端触摸事件顺序：`touchstart`->`touchmove`->`touchend`->`click`，触摸一瞬间就触发`touchstart`（触摸结束后瞬间触发Zepto封装的`tap`事件），触摸结束后300ms才触发`click`事件。

    >有可能已经不存在此bug：被浏览器取消`click`事件的延时，或Zepto改变了`tap`事件实现。
- 解决方法：

    1. 最佳实践：

        使用[fastclick.js](https://github.com/ftlabs/fastclick)（消除`click`的延时）后用`click`代替全部`tap`事件，这样pc端和wap端都可以一致用`click`事件并且不会出现wap端点透bug。
    2. 其他方法：

        1. 使用缓动动画，过度300ms延迟。
        2. 中间增加一层接受这个点透事件，然后去除此层。
        3. 使用[模拟点击事件](https://github.com/realgeoffrey/knowledge/tree/master/网站前端/JS方法积累/实用方法#原生js移动端模拟点击事件消除延时300毫秒后才触发click事件使点击事件提前触发)代替`click`。

### [函数防抖](https://github.com/realgeoffrey/knowledge/tree/master/网站前端/JS方法积累/实用方法#原生js防抖函数)、[函数节流](https://github.com/realgeoffrey/knowledge/tree/master/网站前端/JS方法积累/实用方法#原生js节流函数)
>都是用来控制某个函数在一定时间内执行多少次的技巧。

1. 防抖（Debounce）

    一个函数被调用后，在间隔时间内没有再次被调用才执行（或者一调用就执行，在间隔时间内没有再次被调用才可以进行下一次执行）；若在间隔时间内再次被调用，则刷新等待时间并且继续等待间隔时间结束后才执行。
2. 节流（Throttle）

    一个函数无法在间隔时间内连续执行，当上一次函数执行后过了规定的间隔时间后才能进行下一次该函数的调用。
    >可用`requestAnimationFrame`代替*时间设置为一帧的节流函数*：`throttle(func, 16) `。

### jQuery或Zepto相关
1. 判断是否加载成功，不成功则执行载入本地文件

    ```html
    <script>
        window.jQuery || document.write('<script src="本地地址"><\/script>');
    </script>
    ```
2. 当变量是jQuery或Zepto对象是，可以用`$`作为开头命名，利于与普通变量区别

    ```javascript
    var a = 1;
    var $a = $('a');
    ```
3. 选择器
    1. `$('子','父') === $('父').find('子')`

        找到所有父级，若子级在此父级后面，则选择。
    2. ~~`$('父 子')`~~（效率低）

        找到所有子级，然后向前找出有父级的，则选择。
        >与CSS相同的查询方式。
4. 选择器选择到空内容

    无论选择器选取的内容是否为空，都返回数组，所以`if($(...)) {}`永远成立。因此用以下方法：

    1. `if($(...).length > 0) {}    /* 若无则为0*/`
    2. `if($(...)[0]) {}   /* 若无则为undefined*/`
5. `focus`方法

    1. 直接调用，光标停留在文本开头或上一次光标停留的地方。
    2. 先清空文本再`focus`然后再添加文本，光标停留在文本结尾。
    
    [JSFiddle Demo](https://jsfiddle.net/realgeoffrey/zep4cr3p/)

### 跨域请求
>浏览器同源策略限制
>
>1. 不能通过`ajax`去请求不同源中的内容。
>2. 不同源的文档（`iframe`或`window.open`的新窗口）间不能进行JS的交互操作：DOM无法获取（可以获取window对象，但无法再进一步获取相应的属性和方法）；`Cookie`、`LocalStorage`和`IndexDB`无法读取。

1. `document.domain`相同则可以文档间互相操作

    把不同文档的`document.domain`设置为一致的值（仅允许设置为上一级域），即可双向通信、互相操作：对`iframe`、`window.open`的新窗口、`Cookie`起作用（`LocalStorage`和`IndexDB`只能通过`postMessage`通信）。

    1. 与iframe通信：

        ```javascript
        //父窗口调用iframe的window对象
        var newIframe = document.getElementById('new-iframe').contentWindow;    //或：window.frames[0]

        //iframe调用父窗口的window对象
        var father = parent;
        ```
    2. 与`window.open`的新窗口通信：

        ```javascript
        //父窗口调用新打开窗口的window对象
        var newWin = window.open('某URL');

        //新打开窗口调用父窗口的window对象
        var father = window.opener;
        ```
2. `postMessage`跨文档通信

    >ie8、ie9仅支持`iframe`，ie10+支持。不实行同源政策。

    ```javascript
    //发送方
    目标window对象.postMessage(message, '目标源地址或者*');

    //监听的文档
    window.addEventListener('message', function(e) {
      console.log(e);
    },false);
    ```
3. jsonp（服务端需要设置）

    >只支持**GET**请求。

    网页通过添加一个`<script>`元素，向服务器发起文档请求（不受同源政策限制）；服务器收到请求后，将数据放在一个指定名字的回调函数里传回网页直接执行。

    jQuery在`ajax`方法中封装了`jsonp`功能：

    ```javascript
    jQuery.ajax({
        url: '接口地址',
        dataType: 'jsonp',
        jsonp: '与服务端约定的支持jsonp方法',  //前端唯一需要额外添加的内容
        success: function(data) {
            //data为跨域请求获得的服务端返回数据
        }
    })
    ```
4. CORS（服务端需要设置）

    >ie10+支持。

    若服务端配置允许了某些（或所有）域名，就可以进跨域请求（前端不需要进行额外工作）。
5. 父窗口改变iframe的hash，iframe通过监听hash变化的`hashchange`事件获取父窗口信息

    >ie8+支持。若只改变hash值，页面不会重新刷新。

    ```javascript
    //父窗口改变iframe的hash值
    document.getElementById('new-iframe').src = '除了hash值，url不变（父级与iframe不需要同源）';

    //iframe窗口监听hash变化，以hash变化当做信息的传递
    window.onhashchange = function(){
        var message = window.location.hash;
        //...
    };
    ```
6. 通过监听`window.name`传递信息

    >同会话（tab窗口）前后跳转的页面都可以读取和设置同一个`window.name`值。

    1. 父窗口打开一个子窗口，载入一个不同源的网页，该网页将信息写入window.name属性；
    2. 子窗口跳回一个与主窗口同域的网址；
    3. 主窗口可以读取子窗口的window.name值作为信息的传递。

----
## 功能用法

### 判断类型
1. `Object.prototype.toString.apply(值);  /* 或call*/`

    - 没有跨帧问题。
    - 放入**内置对象**，返回`'[object 构造函数的名称]'`的字符串

        >特例：自定义类型返回`'[object Object]'`，*undefined*、*null*返回对应名字。

        1. `undefined` 或 不填 -> `'[object Undefined]'`
        2. `null` -> `'[object Null]'`
        3. `function(){}`（匿名或不匿名） -> `'[object Function]'`
        4. `[]` -> `'[object Array]'`
        5. `{}` -> `'[object Object]'`
        6. 数字 -> `'[object Number]'`
        7. 字符串 -> `'[object String]'`
        8. 布尔型对象 -> `'[object Boolean]'`
        9. Date对象 -> `'[object Date]'`
        10. RegExp对象 -> `'[object RegExp]'`
        11. arguments对象 -> `'[object Arguments]'`
        12. Error对象 -> `'[object Error]'`
        13. Math对象 -> `'[object Math]'`
        14. window对象 -> `'[object global]'`
        15. document对象 -> `'[object HTMLDocument]'`
        16. JSON对象 -> `'[object JSON]'`
        17. Map对象 -> `'[object Map]'`
        18. console对象 -> `'[object Console]'`
        19. Audio对象 -> `'[object HTMLAudioElement]'`
        20. 自定义类型实例 -> `'[object Object]'`

        >对于没有声明的变量，直接使用此行代码会报**引用不存在变量**的错误，因此需要：
        >
        >`if (typeof 变量 !== 'undefined' && Object.prototype.toString.call(变量) === '[object 某]') {}`
2. `typeof 值`

    - 没有跨帧问题。
    - 返回一个表示值类型的字符串。
    
        1. 字符串 -> `'string'`
        2. 布尔型 -> `'boolean'`
        3. 数值型 -> `'number'`
        4. `undefined` -> `'undefined'`
        5. 引用型 -> `'object'`
        6. 函数 -> `'function'`
        7. **`null`** -> **`'object'`**

        >1. 因为`typeof null`返回`'object'`，因此typeof不能判断是否是引用类型。
        >2. ie8-的DOM节点的方法返回不是~~`function`~~，而是`object`，因此只能用`方法名 in DOM`检测DOM是否拥有某方法。

3. `对象 instanceof 构造函数`

    - 不能跨帧（iframe、window.open）。

        >跨帧：假设在一个浏览器的帧（frame A）里的一个对象传入到另外一个帧（frame B）中，两个帧都定义了一个相同构造函数APerson、BPerson，则：
        >
        >```javascript
        >frameAPersonInstance instanceof frameAPerson; //true
        >frameAPersonInstance instanceof frameBPerson; //false
        >```
    - 判断是否是对象的构造函数（判断某个构造函数的prototype属性所指向的对象是否存在于另外一个要检测对象的原型链上）。
    - 不仅检测对象本身，还检测至原型链。如`new Number() instanceof Object`返回true。
    - **检测自定义类型的唯一方法。**
4. `属性 in 对象`

    - 仅判断属性是否存在检测的对象上，不会去读取属性值。
    - 检测至原型链。

    >- `对象.hasOwnProperty(属性)`仅检查在当前实例对象，不检测其原型链。
    >- ie8-的DOM对象并非继承自Object对象，因此没有hasOwnProperty方法。

### 循环遍历
>1. `break`应用在循环（while、do-while、for、for-in）和switch。
>2. `continue`应用在循环。
>3. `$.each/obj.each`跳出循环用`return true`（功能类似于`continue`）和`return false`（功能类似于`break`）。

1. `for-in`JS原生语法

    ```javascript
    /* obj为数组或对象，i为数组下标或对象属性名*/
    for (var i in obj) {

    }
    ```
2. `$.each()`jQuery方法

    ```javascript
    /* obj为数组或对象（原生或jQuery对象），index为数组下标或对象名，element为值（不是jQuery对象，是DOM对象，与this相同）*/
    $.each(obj, function (index, element) {

    });
    ```
3. `obj.each()`jQuery方法

    ```javascript
    /* obj为jQuery对象，index为从0开始的下标，element为值（不是jQuery对象，是DOM对象，与this相同）*/
    obj.each(function (index, element) {

    });
    ```

### 判断对象、方法是否定义
1. 判断对象方法是否可以执行

    ```javascript
    /* 对象已经定义 && 对象不为null && 对象方法存在*/
    if (typeof obj !== 'undefined' && obj !== null && typeof obj.func === 'function') {
        /* 对象方法已定义 可执行*/
    }
    ```
2. 判断全局对象方法是否可以执行

    ```javascript
    /* window的子对象存在 && 对象方法存在*/
    if (window.obj && typeof window.obj.func === 'function') {
        /* 对象方法已定义 可执行*/
    }
    ```
3. 判断是否需要重新定义

    ```javascript
    /* 对象不存在 || 对象不为null || 对象方法不存在*/
    if (typeof obj === 'undefined' || obj === null || typeof obj.func !== 'function') {
        /* 对象或对象方法没有定义 需重新定义*/
    }
    ```
4. 变量已定义

    ```javascript
    /* 变量已定义 && 变量不赋值为null*/
    if (typeof a !== 'undefined' && a !== null) {
        /* 对象已定义 可操作*/
    }
    ```

### Web Storage、cookie、session
1. Web Storage（`localStorage`、`sessionStorage`）

    1. 客户端保存，不参与和服务器的通信。
    2. 对象形式。
    3. 除了ie6、ie7外其他浏览器都支持（ie及FF需在web服务器里运行）。

        >ie6、ie7可以用它们独有的`UserData`代替使用。
    4. 单个对象数据大小5M+。
    5. 拥有方便的api

        调用`localStorage`、`sessionStorage`对象会为每个源创建独立的`Storage`对象，每个对象都拥有：`setItem`、`getItem`、`removeItem`、`clear`、`key`方法，`length`属性。
        
        ```javascript
        /* 以sessionStorage为例，localStorage有完全相同的API*/
 
        /* setItem：设置或更新键值对（可以直接用“.”和“[]”操作）*/
        sessionStorage.setItem('key1', 'value1');
        sessionStorage.key2 = 'value2'; /* 或 sessionStorage['key2'] = 'value2';*/

        /* getItem：获取值（可以直接用“.”和“[]”操作）*/
        var value1 = sessionStorage.getItem('key1');
        var value2 = sessionStorage.key2;   /* 或 var value2 = sessionStorage['key2']*/

        /* removeItem：删除键值对*/
        sessionStorage.removeItem('key1');

        /* clear：清空所有的键值对*/
        sessionStorage.clear();

        /* length：（只读）数据项数量*/
        /* key：返回存储对象第n个数据项的键名*/
        for (var i = 0, key; i < sessionStorage.length; i++) {
            key = sessionStorage.key(i);
            console.log(sessionStorage.getItem(key));
        }
        ```
    6. `localStorage`、`sessionStorage`区别

        1. `localStorage`

            1. 同源共享。
            2. 持久化本地存储（关闭浏览器后继续保存；除非被清除，否则永久保存）。
            3. 应用场景：所有需要长期本地存储的数据。
        2. `sessionStorage`

            1. 同源且同会话（tab窗口）下共享。
            2. 会话级别存储。跳转页面为同源后仍旧有效（不同tab不共通），关闭浏览器后被清除（重新加载tab或关闭tab后恢复，值对任然存在）。
            3. 应用场景：需要拆分成多个子页面的填写数据。
2. `cookie`：

    1. 客户端保存，始终在http请求中携带（亲测chrome显示有些请求没有携带cookie，为何？），服务端接受和操作客户端cookie。
    2. 字符串形式。不能包含任何**逗号**、**分号**或**空格**（可使用`encodeURIComponent`编码，再用`decodeURIComponent`解码）。
    3. 所有浏览器都支持。
    4. 单域名下，cookie保存的数据不超过4k，数量（最少）20个。
    5. 源生的cookie接口不友好，需要程序员自己封装[操作cookie](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/JS方法积累/实用方法/README.md#原生js操作cookie)。
    6. 同源且同路径共享。
    7. 默认（存储在内存）关闭浏览器后失效，设置失效时间（存储在硬盘）则到期后失效。
    8. 应用场景：服务端确定两次请求是否来自于同一个客户端，从而能够确认和保持用户的登录状态（无状态的HTTP协议上记录稳定的状态信息）。

    >僵尸cookie（[Zombie Cookie](https://en.wikipedia.org/wiki/Zombie_cookie)）是指那些删不掉的，删掉会自动重建的cookie。僵尸cookie是依赖于其他的本地存储方法，如flash的share object、html5的local storages等，当用户删除cookie后，自动从其他本地存储里读取出cookie的备份，并重新种植。
3. `session`：

    1. 服务端保存。
    2. 对象形式。
    3. 无状态值（无状态的HTTP协议），需要借助本地cookie进行配合。

>隐身模式策略：（大多数浏览器的策略）存储API仍然可用，并且看起来功能齐全，只是无法真正储存（比如分配储存空间为0）。

### 自执行匿名函数
>匿名函数，也称为**拉姆达（λ，lambda）函数**。

1. `(function () {/* code*/}());    /* 推荐*/`
2. `(function () {/* code*/})();`

>1. `function`关键字当作一个**函数声明**的开始，函数声明的后面不能跟圆括号；
>2. 将函数声明包含在圆括号中，表示**函数表达式**，函数表达式的后面可以跟圆括号，表示执行此函数。

```javascript
//传值进自执行匿名函数可以避免闭包导致无法记录变量值的问题

for (var i = 0; i < 3; i++) {
    //匿名函数
    (function (i) {
        $.ajax({
            url: 'url1',
            dataType: 'json',
            data: {}
        }).done(function (data) {
            console.log(i); //结果是传入进匿名函数的形参
        });
    }(i));
}

for (var i = 0; i < 3; i++) {
    //不用匿名函数
    $.ajax({
        url: 'url1',
        dataType: 'json',
        data: {}
    }).done(function (data) {
        console.log(i); //每个结果都是固定的最后一个值
    });
}
```

### 动态添加样式、脚本
1. 动态添加样式

    1. 添加`style`标签

        ```javascript
        var newStyle = document.createElement('style');

        newStyle.type = 'text/css';

        if (newStyle.styleSheet) {    //for ie
            newStyle.styleSheet.cssText = 'CSS代码';
        } else {
            newStyle.appendChild(document.createTextNode('CSS代码'));
        }

        document.getElementsByTagName('head')[0].appendChild(newStyle);
        ```
    2. 添加`link`标签

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

        oneDom.style.cssText += '; CSS代码'
        ```

    >CSS代码，例如 `div {background-color: yellow;}`。
2. 动态添加脚本

    1. 异步

        1. 直接`document.write`

            ```javascript
            document.write('<script src="JS文件地址"><\/script>');
            ```
        2. 动态改变已有的`script`标签的`src`属性

            ```html
            <script type="text/javascript" id="节点id"></script>

            <script>
                document.getElementById('节点id').src = 'JS文件地址';
            </script>
            ```
        3. 动态创建`script`标签

            ```javascript
            var newScript = document.createElement('script'),
                appendPlace = document.body || document.getElementsByTagName('HEAD').item(0);

            newScript.type = 'text/javascript';

            newScript.src = 'JS文件地址';

            appendPlace.appendChild(newScript);
            ```
    2. 同步

        1. 添加JS代码

            ```javascript
            var newScript = document.createElement('script'),
                appendPlace = document.body || document.getElementsByTagName('HEAD').item(0);

            newScript.type = 'text/javascript';

            try {
                newScript.appendChild(document.createTextNode('JS代码'));
            }
            catch (e) {
                newScript.text = 'JS代码';  /* ie8及以下，Safari老版本*/
            }

            appendPlace.appendChild(newScript);
            ```
        2. 添加`script`标签

            ```javascript
            /**
             * 同步加载JS脚本
             * @param {String} url - JS文件的相对路径或绝对路径
             * @returns {Boolean} - 是否加载成功
             */
            function syncLoadJS(url) {
                var xmlHttp,
                    appendPlace,
                    newScript;

                if (window.ActiveXObject) { /* ie*/
                    try {
                        xmlHttp = new ActiveXObject('Msxml2.XMLHTTP');
                    }
                    catch (e) {
                        xmlHttp = new ActiveXObject('Microsoft.XMLHTTP');
                    }
                } else if (window.XMLHttpRequest) {
                    xmlHttp = new XMLHttpRequest();
                }

                xmlHttp.open('GET', url, false);    /* 采用同步加载*/
                xmlHttp.send(null); /* 发送同步请求，如果浏览器为Chrome或Opera，必须发布后才能运行，不然会报错*/

                /* 4代表数据发送完毕*/
                if (xmlHttp.readyState == 4) {
                    /* 0为访问的本地，200到300代表访问服务器成功，304代表没做修改访问的是缓存*/
                    if ((xmlHttp.status >= 200 && xmlHttp.status < 300) || xmlHttp.status == 0 || xmlHttp.status == 304) {
                        newScript = document.createElement('script');
                        appendPlace = document.body || document.getElementsByTagName('HEAD').item(0);

                        newScript.type = 'text/javascript';

                        try {
                            newScript.appendChild(document.createTextNode(xmlHttp.responseText));
                        }
                        catch (e) {
                            newScript.text = xmlHttp.responseText;
                        }

                        appendPlace.appendChild(newScript);

                        return true;
                    }
                    else {

                        return false;
                    }
                }
                else {

                    return false;
                }
            }
            ```

### 拼接字符串
长字符串拼接使用`Array.prototype.join()`，而不使用`+`

1. `.join()`性能好，推荐：

    ```javascript
    var arr = [],
        i;

    for (i = 0; i < 100; i++) {
        arr[i] = '字符串' + i + '字符串';
    }

    $('body').text(arr.join(''));
    ```
2. ~~`+`性能差，不推荐~~：

    ```javascript
    var text = '',
        i;

    for (i = 0; i < 100; i++) {
        text = text + '字符串' + i + '字符串';
    }

    $('body').text(text);
    ```

### 定时器`setInterval`、`setTimeout` && 重绘函数`requestAnimationFrame`
1. 定时器

    - 运行机制：

        1. JS是单线程的，程序在执行时必须排队，并且一个程序不能中断另一个程序的执行。
        2. 没有任何代码是立即执行的，但一旦进程空闲则尽快执行。
        3. 定时器触发会把*定时器处理程序*插入**等待执行队列**最后面。

    1. `setInterval`：

        1. 同一个被setInterval执行的函数只能插入一个*定时器处理程序*到**等待执行队列**。
        2. setInterval是每隔时间去尝试执行函数，不关注上一次是何时执行。
        3. 若setInterval触发时已经有它的*定时器处理程序*在**等待执行队列**中，则忽略此次触发。直到没有它的*定时器处理程序*在**等待执行队列**后才可以再次插入到**等待执行队列**（正在执行的不算在**等待执行队列**）。
        4. 相邻的2次*定时器处理程序*可能小于或大于（或等于）设定的间隔时间。无法确定*定时器处理程序*什么时候执行。
    2. `setTimeout`:

        [用setTimeout模拟setInterval](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/JS方法积累/实用方法/README.md#原生js用settimeout模拟setinterval)，可以提高性能（上一次执行完毕间隔时间后再执行下一次，而不是固定间隔时间都尝试执行），并且可以确保每次*定时器处理程序*执行间隔一定大于（或等于）设置的间隔时间。
2. 重绘函数`requestAnimationFrame`

    1. 浏览器重绘之前（大部分浏览器是1秒钟60帧，也就是16.67ms进行一帧重绘）调用一次。
    2. 替代*执行时机无法保证的`setTimeout`或`setInterval`*进行动画操作，提升动画性能：

        1. 把每一帧中的所有DOM操作集中起来，在一次重绘或回流中完成动画，并且重绘或回流的时间间隔紧随浏览器的刷新频率。
        2. 仅仅绘制用户可见的动画。这意味着没把CPU或电池寿命浪费在绘制处于背景标签，最小化窗口，或者页面隐藏区域的动画上。
        3. 当浏览器准备好绘制时（空闲时），才绘制一帧，此时没有等待中的帧。意味着其绘制动画不可能出现多个排队的回调函数，或者阻塞浏览器。因此动画更平滑，CPU和电池使用被进一步优化。

    >1. 高级浏览器才有定义此方法，因此需要[Polyfill](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/JS方法积累/实用方法/README.md#原生jsrequestanimationframe和cancelanimationframe的polyfill)。
    >2. 类似`setInterval`实现[递归调用](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/JS方法积累/实用方法/README.md#原生jsrequestanimationframe的递归)。

### jQuery的[`deferred`](http://api.jquery.com/category/deferred-object/)
>参考[阮一峰：jQuery的deferred对象详解](http://www.ruanyifeng.com/blog/2011/08/a_detailed_explanation_of_jquery_deferred_object.html)、[阮一峰：jQuery.Deferred对象](http://javascript.ruanyifeng.com/jquery/deferred.html)。

jQuery根据[CommonJS promise/A](http://wiki.commonjs.org/wiki/Promises/A)标准实现。

1. `Promise对象`是`Deferred对象`的子集。相对于`Deferred对象`，`Promise对象`无法改变执行状态。

    `Promise对象`：

    1. 开放**与改变执行状态无关的方法**：`always`、`catch`、`done`、`fail`、`pipe`、`progress`、`promise`、`state`、`then`
    2. 屏蔽**与改变执行状态有关的方法**：`notify`、`notifyWith`、`reject`、`rejectWith`、`resolve`、`resolveWith`
2. `$.ajax`返回`Promise对象`；允许把所有jQuery对象设置为`Promise对象`（如动画方法后接`.promise().done(方法)`）。

----
## 性能原理

### 函数
1. 每个函数都是一个`Function`对象，像普通对象一样拥有**属性**和**方法**。

    1. 函数默认有`length`（希望接收的命名参数个数）和`prototype`属性。
    2. `函数对象.caller`：保存调用当前函数的函数（嵌套的外一层函数）的引用。
    3. 函数内的`arguments.caller`：`undefined`（仅仅为了分清`arguments.caller`和`函数对象.caller`）。
    4. 函数内的`arguments.callee`是一个指针：其指向拥有`arguments`对象的函数（就是自身）。
    5. 函数继承的`toLocaleString`、`toString`、`valueOf`的返回值为：**经过浏览器处理过的函数代码（因浏览器而异）**。
2. 函数总有返回值。

    1. 执行函数：不显式`return`默认返回`undefined`。
    2. 实例化（`new`）：不显式`return`默认返回`this`。
3. 定义函数方法：

    1. 构造函数

        `new Function(参数);`

        把Function的构造函数当作函数一样调用（不使用new操作符）的效果与作为Function的构造函数调用一样，最明显的区别就是`this`变成`window`对象。
    2. 函数声明（函数语句）

        `function 名字(参数) {};`
    3. 函数表达式（function expression）

        `var 名字 = function(参数) {};`

        >命名函数表达式：`var 名字1 = function 名字2(参数) {};`，其中函数名`名字2`只能在函数体内部使用。
        >
        >例：
        >```javascript
        >var func1 = function func2() {
        >   console.log(typeof func1);  /* function*/
        >   console.log(typeof func2);  /* function*/
        >};
        >
        >func1();
        >
        >console.log(typeof func1);  /* function*/
        >console.log(typeof func2);  /* undefined*/
        >```

    >- 通过函数声明和函数表达式定义的函数只会被解析一次；而构造函数定义的函数在每次构造函数被调用，函数体字符串都要被解析一次。
    >- 不推荐使用Function构造函数创建函数，因为它需要的函数体作为字符串可能会阻止一些JS引擎优化，也会引起其他问题。
4. 实例化（new）一个构造函数

    `new`得到的对象拥有构造函数内用`this`定义的属性（或方法）以及原型链上的属性（或方法），在构造函数内`var`的变量和`function`无法被这个对象使用，只能在构造函数里使用（类似私有变量）。

    >相对于单全局变量，构造函数更加灵活，可以生成多个对象进行互相独立的操作。
5. 函数调用类型
    
    1. 函数调用`alert();`或`(function () {}())`（立即执行函数）
        
        `this`->全局对象`window`
    2. 方法调用`console.log();`
        
        `this`->上级对象
    3. 构造函数调用`new RegExp();`
    
        `this`->新实例对象
    4. 间接调用`alert.call(传入的对象);`（或`apply`）
    
        `this`->传入的对象
6. `this`——调用函数的那个对象

    ```javascript
    var x = 1;
    
    function test() {
        console.log(this.x + '|' + _test() + '|' + (function () {return this.x;}()));
    
        function _test() {
            return this.x;
        }
    }
    
    /* ①方法没有对象调用（包括立即执行函数，并且与作用域无关），this代表全局对象Global（window）*/
    test(); /* 1|1|1*/
    
    
    /* ②函数作为某个对象的方法调用，this指向上级对象*/
    var obj = {};
    obj.x = 2;
    obj.func = test;
    obj.func(); /* 2|1|1*/
    
    
    /* ③作为构造函数生成一个新对象，this指向这个新实例对象*/
    function Test2() {
        this.x = 4;
        console.log(this.x + '|' + _test() + '|' + (function () {return this.x;}()));
    
        function _test() {
            return this.x;
        }
    }
    var obj3 = new Test2(); /* 4|1|1*/
    
    
    /* ④apply或call调用，传入对象代替this调用*/
    var obj2 = {x: 3};
    obj.func.call(obj2);    /* 3|1|1*/
    ```

### 原型
1. 构造函数、原型、实例

    1. 只要创建了一个新函数，就会根据一组特定的规则为该函数创建一个`prototype`属性，指向函数的原型对象；所有原型对象都会自动获得一个`constructor`属性，指向**prototype属性所在函数**。
    
        互相连接：函数拥有一个`prototype`属性指向其原型对象，原型对象拥有一个`constructor`属性指向函数。
    2. 当调用构造函数创建一个新实例后（new），该实例的内部有一个`[[Prototype]]`属性（内部属性、没有标准方式访问，但部分高级浏览器在对象上支持`__proto__`访问），指向**构造函数的原型对象**。
    
        连接存在于实例与**原型对象**之间，而不直接存在于~~实例与构造函数~~之间（**实例**通过`[[Prototype]]`指向**原型对象**再间接与**构造函数**产生关联）。
        
    ```javascript
    var A = function () {
    
    };
    var a = new A();
    
    console.log('原型与构造函数：' + (A.prototype.constructor === A));
    console.log('实例与原型：' + (a.__proto__ === A.prototype));
    console.log('实例与构造函数:' + (a.__proto__.constructor === A));
    ```
2. 如果重写原型的值（不是添加），可以给原型添加`constructor`属性并指向**构造函数**（新对象的原型的`constructor`属性指向`Object`函数）。
    
    ```Javascript
    var A = function () {
        console.log('A');
    };

    A.prototype = {
        other: '...'
    };

    if (typeof Object.defineProperty === 'function') {

        /* 使属性：不可以改变描述符、不可以删除、不可以枚举、不可以被赋值运算符改变*/
        Object.defineProperty(A.prototype, 'constructor', {
            value: A
        });
    } else {
        A.prototype.constructor = A;
    }


    console.log(A.prototype);
    var a = new A();
    console.log(a.__proto__);
    ```
3. 通过**原型链**实现**继承**。

    继承：通过**将一个类型的实例赋值给另一个构造函数的原型**实现。

### 自动插入分号机制（Automatic Semicolon Insertion，ASI）
1. ASI机制不是说在解析过程中解析器自动把分号添加到代码中，而是说解析器除了分号还会以换行为基础按一定的规则作为断句（EOC）的依据，从而保证解析的正确性。
2. 解析器会尽量将新行并入当前行，当且仅当符合ASI规则时才会将新行视为独立的语句：

    1. `;`空语句
    2. `var`语句
    3. 表达式语句（一定会产生一个值）
    4. `do-while`语句（不是`while`）
    5. `continue`语句
    6. `break`语句
    7. `return`语句
    8. `throw`语句

>前置分号策略：只要对行首字符进行token判断是否为：`[` `(` `+` `-` `/`五个符号之一，就在其前面增加分号。

### `Boolean()`转换
| 数据类型 | 转换为true的值 | 转换为false的值 |
| ------------- | ------------- | ------------- |
| Boolean | true | false |
| String | 任何非空字符串 | ""（空字符串） |
| Number | 任何非零数值（包括无穷大） | 0和NaN |
| Object | 任何对象 | null |
| undefined | n/a | undefined |

>`!!变量`等价于`Boolean(变量)`。

### `||`和`&&`
1. `expr1 || expr2`：

    1. 如果expr1能转换成true（`Boolean(expr1)`）则返回expr1，否则返回expr2。
    2. 在Boolean环境（如if的条件判断）中使用时，两个操作结果中只要有一个为true，返回true；二者操作结果都为false时返回false。
2. `expr1 && expr2`：

    1. 如果expr1能转换成false（`Boolean(expr1)`）则返回expr1，否则返回expr2。
    2. 在Boolean环境（如if的条件判断）中使用时，两个操作结果都为true时返回true，否则返回false。

### DOM加载步骤、jQuery文档`ready`事件和JS的`onload`事件顺序
1. 解析Html结构；
2. 加载外部脚本和样式表文件；
3. 解析并执行脚本代码；
4. 构造Html DOM模型 -> 完成后执行`$(document).ready(function(){});`；
5. 加载图片等外部文件；
6. 页面加载完毕 -> 完成后执行`window.onload();`。

### JS性能
1. 平稳退化：当浏览器不支持或禁用了JS功能后，访问者也能完成最基本的内容访问。

    1. 为JS代码预留出退路（a标签添加属性链接，用JS事件绑定去拦截浏览器默认行为）

        `<a href="真实地址" class="j-func">...</a>`

    2. ~~伪协议`javascript:`~~

        `<a href="javascript: func();">...</a>`

    3. ~~内嵌事件处理函数~~

        `<a href="#" onclick="func();return false;">...</a>`
2. 渐进增强：先完成基本通用功能，再追加额外功能。
3. 向后兼容：确保老版本浏览器基本可用，使之虽不能支持某些功能，但仍能基本访问。

    1. **能力检测：`if(func){func();}`**。
    2. 怪癖检测：`try-catch`。
    3. 浏览器嗅探技术（用户代理检测）。
4. 资源分离：把样式表和脚本分离出HTML。

    1. 使用外部资源。
    2. 不在HTML上用事件处理函数。
    3. 对只为DOM增添的内容，转移到外部资源中动态创建。
5. 性能提升。

    1. 减少访问DOM（搜索结果保存在变量中）。
    2. 减少外链请求数量（合并JS、CSS、图片）。
    3. 压缩资源。
    4. 脚本放置在`</body>`前。

### 闭包
1. 当函数内部定义了其他函数时，就创建了闭包。内部函数总是可以访问其所在的外部函数中声明的内容（链式作用域），即使外部函数被返回（寿命终结）之后。
2. 闭包是一种特殊的对象。它由两部分构成：**函数**、创建该函数的**环境**（链式作用域）。
3. 闭包的创建依赖于函数（函数是唯一拥有自身作用域的结构）。闭包通常用来创建私有变量或方法，使得这些内容不被外部随意访问，同时又可以通过指定的闭包函数接口来操作（将函数内部和外部连接起来）。

- 产生效果：
    1. 可以操作函数内部的私有内容（特权方法）。
    2. 让被操作的私有内容始终保持在内存中不被垃圾回收。
    3. 占用较多的内存。

### 垃圾回收
>垃圾回收器会按照固定的时间间隔（或代码执行中预定的时间）周期性地执行，找出不再继续使用的变量，然后释放其占用的内存。

垃圾回收器必须跟踪并判断变量是否有用，对于不再有用的变量打上标记，以备将来回收。

1. **标记清除（mark-and-sweep）**

    垃圾回收器在运行时给存储在内存中的所有变量加上标记；然后，去掉环境中的变量以及被环境中变量引用的变量的标记；最后，对那些带标记的值进行释放。
    >从2012年起，所有现代浏览器都使用了标记-清除垃圾回收算法。
2. 引用计数（reference counting）

    跟踪记录每个值被引用的次数，被引用一次加1，引用取消就减1，当引用次数为0时，则说明没有办法再访问这个值了，当垃圾回收器下次运行时，释放引用次数为0的值所占空间。

    >可能产生一个严重的问题：循环引用，引用次数永远不会是0。

>用`变量 = null;`等方法，让变量成为零引用，从而进行清除元素、垃圾回收（导致内存泄露的情况除外）。

### 内存泄漏
> 内存泄露是指计算机内存逐渐丢失。当某个程序总是无法释放内存时，就会出现内存泄露。JS有内存回收机制（垃圾回收）。

1. 使用chrome的**Profiles**和**Timeline**面板来查看页面占用内存使用和变化。
2. 内存泄漏的原因以及防止建议：

    1. 全局变量不会被垃圾回收。
    2. 被闭包引用的变量不会被垃圾回收。
    3. DOM清空或删除时，事件未清除导致内存泄漏：删除DOM的时候，先移除事件绑定。
    4. 子元素存在引用引起的内存泄漏：

        ![内存泄漏图](./images/memory-leak-1.gif)

        1. 黄色是指直接被 JS变量所引用，在内存里。
        2. 红色是指间接被 JS变量所引用，如上图，refB 被 refA 间接引用，导致即使 refB 变量被清空，也是不会被回收的。
        3. 子元素 refB 由于 parentNode 的间接引用，只要它不被删除，它所有的父元素（图中红色部分）都不会被删除。
    5. 被遗忘的计数器或回调函数：不使用时及时清除。

### 排版引擎与JS引擎
1. 排版引擎（layout engine）

    也称为浏览器内核（web browser engine）、页面渲染引擎（rendering engine）或样板引擎，是一种软件组件，负责获取标记式内容（如HTML、XML以及图像文件等）、整理信息（如CSS、XSL），并将排版后的内容输出至显示屏或打印机。

    所有网页浏览器、电子邮件客户端以及其他需要根据表示性的标记语言来显示内容的应用程序，都需要排版引擎。

    >1. IE：Trident。
    >2. Chrome：前WebKit，现Blink。
    >3. Firefox：Gecko。
    >4. Safari：WebKit。
    >5. Opera：前Presto，现Blink。
    >6. Edge：EdgeHTML。
2. JS引擎

    一个专门处理JS脚本的虚拟机，一般会附带在网页浏览器中。

    >1. JScript：ie8-，ASP。
    >2. Chakra：ie9+，Edge。
    >3. V8：Chrome，Opera，Nodejs，MongoDB。
    >4. SpiderMonkey：Firefox。
    >5. Nitro：Safari。

### 引用类型与基本类型的变量传递
1. 只能给引用类型动态地添加属性和方法，不能给基本类型添加。
2. JS的变量传递都是**值传递**，都是把变量中存储的值复制一份给另一个变量。

    1. 基本类型的复制

        把变量的值复制到新变量分配的位置上，两个变量可以参与任何操作而不会互相影响。
    2. 引用类型的复制

        引用类型的变量保存的是指向该对象内容的指针，复制给新变量指针后，两个变量实际上引用同一对象，改变其中一个引用对象中的属性，会影响另一个。但是如果给其中一个引用对象赋值（不是操作属性），因为值引用改变了引用地址，所以两个变量不再保存同一个指针。

    >所有函数的参数都是按值来传递的。基本类型值的传递和基本类型变量复制一致（采用在栈内新建值），引用类型值的传递和引用类型变量的复制一致（栈内存放的是指针，指向堆中同一对象）。
3. 引用类型的**深、浅复制（拷贝）**

    1. 浅复制

        1. 拷贝对象A时，对象B将拷贝A的所有字段。若字段是内存地址（引用类型），B将拷贝地址；若字段是基本类型，B将复制其值。
        2. 它的缺点是如果你改变了对象B所指向的内存地址，你同时也改变了对象A指向这个地址的字段。
    2. 深复制

        这种方式会完全拷贝所有数据，优点是B与A不会相互依赖（A,B完全脱离关联），缺点是拷贝的速度更慢，代价更大。

### 错误处理机制
1. 原生错误类型

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

    >浏览器不会抛出`Error`类型的错误，所以如果捕获到`Error`类型的错误，可以确定这个异常是用户代码抛出的。浏览器默认只会抛出Error的6个派生类型错误。

2. Error对象属性

    Error实例对象有两个基本的属性`message`和`name`。
    >`message`用来表示异常的详细信息；`name`指的的是Error对象的构造函数。

    此外，不同的JS引擎对Error还各自提供了一些扩展属性。

3. 处理代码中抛出的error

    - 当JS出现错误时，JS引擎就会根据JS调用栈逐级寻找对应的`catch`，如果**没有找到相应的catch handler**或**catch handler本身又有error**或者**又抛出新的error**，就会把这个error交给浏览器，浏览器会用各自不同的方式（IE以黄色三角图案显示在左下角，而firefix会显示在错误控制台中）显示错误信息给访问者，可以用`window.onerror`进行自定义操作。
    - 在某个**JS block**（`<script>`标签或`try-catch`的`try`语句块）内，第一个错误触发后，当前JS block后面的代码会被自动忽略，不再执行，其他的JS block内代码不被影响。

    1. `try-catch-finally`

        1. `try`必须跟`catch`或`finally`或`catch + finally`同时出现。
        2. 如果有`catch`，一旦`try`中抛出错误以后就先执行`catch`中的代码，然后执行`finally`中的代码；
        3. 如果没有`catch`，`try`中的代码抛出错误后，就会先执行`finally`中的语句，然后将`try`中抛出的错误继续往上抛。
        4. 如果`try`中代码是以`return`、`continue`或`break`终止的，必须先执行完`finally`中的语句后再执行相应的`try`中的返回语句。
        5. 在`catch`中接收的错误，不会再向上提交给浏览器。
    2. `window.onerror`

        1. 没有通过`try-catch`处理的错误都会触发`window`对象的`onerror`。
        2. 用方法赋值给`window.onerror`后，但凡这个window中有JS错误出现，则会调用此方法。
        3. onerror方法会传入3个参数（至少），分别是**错误信息提示**、**javascript产生错误的document url**和**错误出现的行号**。
        4. 若方法返回`true`，浏览器不再显示错误信息；若返回`false`，浏览器还是会提示错误信息：

        ```javascript
        /**
         * window错误处理
         * @param {String} msg - 错误信息提示
         * @param {String} url - 错误出现url
         * @param {Number} line - 错误出现行号
         * @returns {Boolean} - true：不显示错误信息|false：显示
         */
        window.onerror = function (msg, url, line) {
            /* code*/

            return true;    /* 浏览器不再显示错误信息*/
        };
        ```
    3. 图像的`onerror`事件

        - 只要图像的src属性中的URL不能返回可以被识别的图像格式，就会触发图像的`onerror`事件。
        - 错误不会提交到`window.onerror`。

        1. `<img>`标签的`onerror`事件

            ```html
            <img src="错误地址" onerror="func();">
            ```
        2. `Image`实例的属性

            ```javascript
            var img = new Image();

            img.onerror = function () {
                /* code*/
            };

            img.src = '错误地址';
            ```

        >与window对象的onerror事件处理函数不同，Image实例对象或img标签的onerror事件没有任何参数。

    - 使用策略

        1. 非客户端页面

            仅需在加载JS之前配置好`window.onerror`。
        2. 客户端内嵌页面

            1. 同样也需要在加载JS之前配置好`window.onerror`，来处理页面内错误。
            2. 客户端回调函数嵌套一层`try-catch`以提供**哪个方法发生错误等额外信息**。

                因为客户端调用前端的方法是直接通过函数运行JS代码，抛出错误时`window.onerror`传入的参数仅有第一个`message`参数（`file`、`line`以及其他参数都没有），所以必须在给客户端调用的JS方法中嵌套`try-catch`并且抛出能标识出所调用方法名字等信息。
            3. （可选）又因为要避免**JS代码还未加载完毕客户端就调用回调函数**，需在客户端调用前端JS回调函数的时候嵌套一层`try-catch`，在`catch`中提供调用哪个方法的信息。

                >仅能获取原始error的`message`信息，无法获取`line`等其他信息，因此还是必须前端在回调函数中嵌套`try-catch`

        >捕获错误的目的在于避免浏览器以默认方式处理它们；而抛出错误的目的在于提供错误发生具体原因的消息。

### jQuery或Zepto的`.on()`绑定效率
>e.g. `$(eventHandler).on(event, selector, func);`

1. 执行`on`方法的时刻，把所有满足条件的DOM对象安装指定的内容，成为**eventHandler**。有且仅有这些eventHandler绑定成功；之后动态生成的也满足条件的对象不再安装；对已生效的eventHandler处理DOM（比如删除类名）也不会使绑定内容失效（除非删除）；在eventHandler内动态增删的**selector**都可以由条件判定是否生效绑定内容。
2. 绑定的eventHandler距离selector越近，效率越高。因此虽然把selector都绑定在`$(document)`上能够避免增删节点对事件绑定造成的影响，但确是低效的。