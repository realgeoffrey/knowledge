# JS学习笔记

## 目录
1. [性能原理](#性能原理)

    1. [函数](#函数)
    1. [变量、`this`](#变量this)
    1. [闭包（closure）](#闭包closure)
    1. [动态执行JS脚本（执行字符串）](#动态执行js脚本执行字符串)
    1. [欺骗JS词法作用域](#欺骗js词法作用域)
    1. [原型](#原型)
    1. [继承](#继承)
    1. [内存机制](#内存机制)
    1. [内存泄漏](#内存泄漏)
    1. [深复制（深拷贝）实现思路](#深复制深拷贝实现思路)
    1. [数据类型转换](#数据类型转换)
    1. [`||`和`&&`和`??`](#和和)
    1. [浏览器的`事件循环（event loop）`](#浏览器的事件循环event-loop)
    1. [定时器 && 重绘函数](#定时器--重绘函数)
1. [功能归纳](#功能归纳)

    1. [判断数据类型](#判断数据类型)
    1. [循环遍历](#循环遍历)
    1. [异步循环遍历](#异步循环遍历)
    1. [跨域请求](#跨域请求)
    1. [浏览器文档间的数据交互（文档与`<iframe>`、文档与`window.open()`的新窗口）](#浏览器文档间的数据交互文档与iframe文档与windowopen的新窗口)
    1. [Web Storage && cookie && IndexedDB](#web-storage--cookie--indexeddb)
    1. [错误处理机制](#错误处理机制)
    1. [预加载](#预加载)
    1. [判断对象、方法是否定义](#判断对象方法是否定义)
    1. [浏览器缓存](#浏览器缓存)
    1. [JS压缩细节](#js压缩细节)
    1. [JS混淆（加密）细节](#js混淆加密细节)
1. [编程技巧](#编程技巧)

    1. [JS代码风格规范（coding style guide）](#js代码风格规范coding-style-guide)
    1. [编程实践（programming practices）](#编程实践programming-practices)
    1. [函数防抖、函数节流](#函数防抖函数节流)
    1. [自执行匿名函数（拉姆达，λ，lambda）](#自执行匿名函数拉姆达λlambda)
    1. [Tips](#tips)
1. [事件相关](#事件相关)

    1. [事件绑定](#事件绑定)
    1. [事件流（event flow）](#事件流event-flow)
    1. [WAP端相关](#wap端相关)
1. [DOM操作](#dom操作)

    1. [获取位置信息](#获取位置信息)
    1. [节点与视口距离关系](#节点与视口距离关系)
    1. [节点是否在首屏](#节点是否在首屏)
    1. [判断滚动定位](#判断滚动定位)
    1. [进行文档滚动](#进行文档滚动)
    1. [DOM相对位置](#dom相对位置)
    1. [DOM修改](#dom修改)
    1. [`Node`与`Element`](#node与element)
    1. [`attribute`与`property`](#attribute与property)
    1. [jQuery相关](#jquery相关)

---
## 性能原理

### 函数
1. 每个函数都是一个`Function`对象，像普通对象一样拥有**属性**和**方法**。

    1. 函数拥有

        1. `length`：希望接收的命名参数个数（计数到`默认参数`或`剩余参数`之前的形参）
        2. `name`：函数名
        3. `prototype`：（函数独有）指向函数的原型对象

            箭头函数、`bind`生成的函数，没有 ~~`prototype`~~，不能作为 ~~类`extends`的基类~~。
    2. ES6不推荐使用（部分情况下导致报错）：

        1. 函数体内的`arguments.callee`是一个指针：其指向拥有`arguments`对象的函数（函数自身）。
        2. `函数对象.caller`：保存调用当前函数的函数（嵌套的外一层函数）的引用。
        3. 函数体内的`arguments.caller`（值为`undefined`，仅为分清`arguments.caller`和`函数对象.caller`）。
2. 函数总有返回值。

    1. 执行函数：默认返回`undefined`。
    2. 实例化（`new`）：默认返回`this`。
3. 创建函数的方式：

    >无论函数是如何创建的，函数都是一个值。

    1. 函数声明（函数语句）

        `function 名字 (多个参数) {/* 函数体 */}`

        >函数名绑定在所在作用域。

    >若`function`（或箭头函数的`()`）是声明中的第一个词，则是函数声明，否则是函数表达式。

    2. 函数表达式（function expression）

        1. `var 名字 = function 内部名字 (多个参数) {/* 函数体 */}`（或`var 名字 = (多个参数) => {/* 函数体 */}`）
        2. `(function 内部名字 (多个参数) {/* 函数体 */}())`（或`((多个参数) => {/* 函数体 */})()`）

        >函数名绑定在函数表达式内部函数体中。

    >1. 通过**函数声明**、**函数表达式**创建的函数，在加载脚本时和其他代码一起解析（编译时），但只有函数声明会被赋值，函数表达式不会被赋值、仅`var`声明变量；通过**构造函数**定义的函数，在构造函数被执行时（运行时）才解析函数体字符串。
    >2. 不推荐通过~~构造函数~~创建函数，因为作为字符串的函数体可能会阻止一些JS引擎优化，也会引起其他问题。

    3. ~~构造函数~~

        `var 名字 = new Function([多个参数, ]函数体字符串);`

        >直接调用`Function`（不使用`new`操作符）的效果与调用构造函数一样，区别是`this`指向`window`。
4. [匿名函数](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/JS学习笔记/README.md#自执行匿名函数拉姆达λlambda)、[箭头函数](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/前端内容/标准库文档.md#箭头函数)

    只能提供给其他变量引用、或自执行。

    ><details>
    ><summary>匿名函数：可以添加仅在匿名函数内部才能使用的函数名字，主要用于在执行栈中标记匿名函数的函数名（主要针对：自执行匿名函数），而不只是显示<code>anonymous</code></summary>
    >
    >e.g.
    >
    > ```js
    > var func1 = function func2() { // 其中函数名`func2`只能在函数体内部使用。
    >    console.log(typeof func1);  // => function
    >    console.log(typeof func2);  // => function
    > };
    >
    > func1();
    >
    > console.log(typeof func1);     // => function
    > console.log(typeof func2);     // => undefined
    > ```
    ></details>
5. 实例化（`new`）一个构造函数

    >1. 相对于单全局变量，构造函数更加灵活，可以生成多个对象进行互相独立的操作。
    >2. 构造函数，其实就是一个普通函数，没有任何特殊。

    1. `new`得到的实例对象（若构造函数不是返回一个引用数据类型），拥有构造函数体内使用`this`定义的属性和方法，且拥有构造函数的原型对象上的属性和方法（因为实例的`[[Prototype]]`指向`构造函数.prototype`）；在构造函数体内`var`的变量和`function`无法被这个对象使用，只能在构造函数里使用（类似私有变量）。
    2. <details>

        <summary>若构造函数返回值不是这个构造函数的实例时，则<code>new 构造函数() instanceof 构造函数 === false</code></summary>

        ```js
        class Foo {
          constructor () {
            return Object.create(null)
          }
        }
        console.log(new Foo() instanceof Foo)   // => false


        function Foo2 () {
          return {}
        }
        console.log(new Foo2() instanceof Foo2) // => false
        ```
        </details>

    >1. `new Func`等价于：`new Func()`。
    >2. `new Obj().func()`等价于：`(new Obj()).func()`（先新建实例，再调用实例的方法/原型链上方法）。
    >3. `new Obj.func()`等价于：`new (Obj.func)()`、`new (Obj.func)`、`new Obj.func`（新建实例）。

    - <details>

        <summary><code>new</code>一个构造函数执行的步骤</summary>

        e.g. `var newObj = new Func(para1, para2);`

        1. 创建一个空对象（假设为obj）：

            `var obj = {};`
        2. 设置obj的`[[Prototype]]`指向构造函数的原型对象：

            `obj.__proto__ = Func.prototype;`（或`Object.setPrototypeOf(obj, Func.prototype);`）

        >第一、二步骤也可以用`var obj = Object.create(Func.prototype);`代替。

        3. 使用obj作为上下文调用构造函数，并传入参数：

            `Func.apply(obj, arguments);`
        4. newObj赋值

            1. 若Func返回**引用数据类型**，则这个引用数据类型的值赋值给newObj。
            2. 若Func返回基本数据类型或返回this或无返回，则obj赋值给newObj。
        </details>
6. <a name="函数-参数"></a>参数

    1. 参数变量在函数体内是默认声明的（传递进函数体），所以不能在函数体内用`let`或`const`再次声明同名参数（`var`可以）。
    2. 使用**参数默认值**时的特殊情况：

        1. 调用函数时，根据传参为`undefined`或不传，才进行参数默认值的表达式值计算（惰性求值），默认值是运行时执行而不是~~定义时执行~~（若默认值是调用其他函数，则当且仅当传参为`undefined`或不传参时才执行其他函数）。
        2. 调用函数时，所有参数会形成一个单独作用域（context）进行初始化，初始化结束则作用域消失。此作用域中的参数进行类似`let`定义，因此函数不能有同名参数。

            ><details>
            ><summary>e.g.</summary>
            >
            >```js
            >function f1(y1 = x1) {     // 形成短暂的单独作用域，x1没有定义，向父级作用域取值，取不到则报错
            >  let x1 = 'x1'
            >  console.log(y1)
            >}
            >f1()                       // ReferenceError: x1 is not defined
            >
            >
            >let x2 = 'outer x2'
            >function f2(y2 = x2) {     // 形成短暂的单独作用域，x2没有定义，向父级作用域取值
            >  let x2 = 'x2'
            >  console.log(y2)
            >}
            >f2()                       // => 'outer x2'
            >
            >
            >let x3 = 'outer x3'
            >function f3(x3, y3 = x3) { // 形成短暂的单独作用域，x3是传参定义的值，不向父级作用域取值
            >  console.log(y3)
            >}
            >f3()                       // => undefined
            >f3(3)                      // => 3
            >
            >
            >let x4 = 'outer x4'
            >function f4(x4 = x4) {     // 形成短暂的单独作用域，实际执行类似let x = x，暂时性死区导致报错
            >
            >}
            >f4()                       // ReferenceError: x is not defined
            >```
            ></details>
        3. 不能~~在参数默认值中调用函数体内的方法~~（参数默认值总是被首先执行，而函数体内的函数声明之后生效）。
    3. 建议参数都用对象形式传递，且形参设置为解构赋值+默认参数。

        >e.g. `function func ({ para1 = 'default', para2 } = {}) {}`
    4. 参数的数量有限制，如：有些JS引擎限制在`Math.pow(2, 16)`。

    - 设计函数的参数时，有2种方式：①多参数；②单参数是对象。

        可选的参数最好设计成对象形式，方便将来扩展。

        ```js
        // 方便扩展
        function func1 (必填1, 必填2, { 可选1 = '默认值1' } = {}) {}
        function func2 ({ 必填1, 必填2, 可选1 = '默认值1' } = {}) {}

        // 不方便扩展
        function func3 (必填1, 必填2, 可选1 = '默认值1') {}
        ```
7. [变量、`this`](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/JS学习笔记/README.md#变量this)的取值

- 复制一个函数：[动态执行JS脚本（执行字符串）](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/JS学习笔记/README.md#动态执行js脚本执行字符串)

- 其他函数相关概念

    1. 函数防抖、函数节流。

        e.g. [防抖函数、节流函数](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/JS方法积累/手写代码/README.md#防抖函数节流函数)
    2. 柯里化（currying）

        把接受多个参数的函数变换成接受单一参数（最初函数的第一个参数）的函数，并且返回接受余下参数的新函数。e.g. [柯里化](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/JS方法积累/手写代码/README.md#柯里化)
    3. 惰性函数（Lazy Function）

        一种在第一次调用时初始化并替换自身的函数。这种技术通常用于优化那些根据特定条件执行不同逻辑的函数，特别是当这些条件在函数第一次调用时就已经确定的情况下。
    4. 仅执行一次函数

        ```js
        // e.g.
        function a(func) {
          let called = false;   // 利用闭包
          return function () {
            if (!called) { called = true; func.apply(this, arguments); }
          };
        }
        ```

### 变量、`this`
1. `变量`（[词法作用域](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/程序员的自我修养/README.md#词法作用域动态作用域)）

    1. <details>

        <summary>由声明函数时，变量处在哪一个函数作用域（或块级作用域）唯一决定；</summary>

        1. ES5

            函数声明是唯一拥有自身作用域的结构。

            >1. 若`function`或`箭头函数`**声明**出现，则在父级作用域中新增一个子级作用域。
            >2. 父级不能访问子级作用域，子级能完全使用父级作用域。
        2. ES6

            在ES5的基础上，增加块级作用域概念（[`let`、`const`](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/前端内容/标准库文档.md#letconst)）。
        </details>

        >与~~调用函数时所在的作用域、时机、以何种方式被调用~~无关（函数赋值给任何变量或属性也不改变变量取值）。
    2. 遍历嵌套作用域链，在当前执行的作用域开始（函数声明处），向上遍历查找直到全局作用域或找到；

        >1. 对于`变量 = 值`赋值（LHS），若直到全局作用域也没查找到变量，则创建一个全局变量，用`值`赋值给这个新建的全局变量。
        >2. 对于`变量`引用（RHS），若直到全局作用域也没查找到变量，则报错`ReferenceError: 变量 is not defined`。
    3. 多层的嵌套作用域中，可以定义同名的标识符（变量、函数），遮蔽效应使内部的标识符「遮蔽」外部的标识符（若查找到第一个匹配的标识符则停止再向上查找）。

        >`window.某变量`可以访问被同名变量`某变量`遮蔽的全局变量。
    4. 产生[闭包](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/JS学习笔记/README.md#闭包closure)

        <details>
        <summary>e.g. 词法作用域</summary>

        ```js
        function foo () {
          console.log(a)
        }

        function bar () {
          var a = 2
          foo()
        }

        var a = 1
        bar() // => 1

        // JS是词法作用域的流程：执行 foo 函数，先从 foo 函数内部查找是否有局部变量 value，如果没有，就根据书写的位置（声明位置），查找上面一层的代码，也就是 value 等于 1，所以结果会打印 1。
        // 其他语言是动态作用域的流程：执行 foo 函数，依然是从 foo 函数内部查找是否有局部变量 value。如果没有，就从调用函数的作用域，也就是 bar 函数内部查找 value 变量，所以结果会打印 2。
        ```
        </details>

        回调函数里的变量，也满足词法作用域：声明函数时，变量处在哪一个函数作用域（或块级作用域）唯一决定。
    5. 声明

        >在[JS的预编译](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/前端内容/基础知识.md#js的预编译)阶段进行提升（hoisting）。

        0. [`let`、`const`](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/前端内容/标准库文档.md#letconst)
        1. 变量声明（`var`）

            无论语句在何处，无论是否会真正执行到，所有的`var`语句的**声明**都提升到作用域（函数体内或全局）顶部执行，但具体**赋值**不会被提前。

            ><details>
            ><summary>e.g.</summary>
            >
            >```js
            >(function () {
            >    console.log(a);    // undefined
            >    var a = 2;
            >    console.log(a);    // 2
            >})();
            >
            >// 等价于：
            >(function () {
            >    var a;
            >    console.log(a);    // undefined
            >    a = 2;
            >    console.log(a);    // 2
            >})();
            >```
            ></details>

            1. 声明变量是所在上下文环境的不可配置属性；非声明变量是可配置的。
            2. 相同作用域中，对同一个变量进行多次声明，则忽略第一次之后的声明（会执行变量赋值）。

            >建议：总是把所有变量声明都放在函数顶部，而不是散落在各个角落。
        2. 函数声明

            1. 也会被JS引擎提升到当前执行的作用域顶部声明（函数声明就等同于赋值），因此代码中函数的调用可以出现在函数声明之前。
            2. 函数声明不应当出现在~~语句块~~内（如：条件语句），块内函数声明的行为很奇怪，请勿使用它们。

                >在非严格模式下，语句块的函数也会提前声明，导致语义不清容易出错；在严格模式下，块内函数声明仅在块内作用域中（或不允许在语句块中使用函数声明）。
        3. 函数表达式（Function expressions）声明

            必须先声明：`var a = function () {...};`才可以使用，`a`声明会被提前，但`a`赋值不会被提前。

            ><details>
            ><summary>e.g.</summary>
            >
            >```js
            >foo() // TypeError: foo is not a function
            >bar() // ReferenceError: bar is not defined
            >
            >var foo = function bar () {}
            >```
            ></details>
        4. 同名的变量声明和函数声明（不是函数表达式）

            同时声明的情况下（顺序不影响结果）：

            1. 变量仅声明不赋值：被赋值为函数。
            2. 变量赋值：被赋值为变量。

            - 原因：

                1. 函数、变量都在编译时提升，变量的赋值在运行时进行，函数的声明等同于赋值。

                    因此：所有函数声明会提升到所有变量声明赋值之前。
                2. 可以重复声明，重复声明的变量`var`被忽略，重复声明的函数`function`会覆盖之前同名的函数声明。

            ><details>
            ><summary>e.g.</summary>
            >
            >```js
            >var a1 = 1;
            >function a1() {}
            >console.log(a1);    // 1
            >
            >function b2() {}
            >var b2 = 1;
            >console.log(b2);    // 1
            >
            >var c3;
            >function c3() {}
            >console.log(c3);    // function
            >
            >function d4() {}
            >var d4;
            >console.log(d4);    // function
            >```
            ></details>

        >建议：先声明再使用；把函数声明紧接着放在变量声明之后。

    - 变量命名规范（包含：方法名、类名等所有变量名）

        1. 只能由`字母`、`数字`、`_`、`$`，不能~~以数字开头~~

            >允许非英文字母，但不推荐。
        2. 不能使用~~关键字~~、~~保留字~~

            - `undefined`不是保留关键字。

                全局属性`undefined`不能被重写（`window.undefined`、`global.undefined`），但是要注意局部变量名可以声明为`undefined`，从而优先被引用的问题。可以用`void 运算符`永远返回的`undefined`代替值`undefined`。

            >[MDN：关键字](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Lexical_grammar#关键字)。
        3. 区分大小写
        >一般推荐的多个单词隔断方式：小驼峰、大驼峰；（表示常数：）全大写+单词用`_`分割。
2. `this`（函数调用方式）

    >Node.js的`this`指向全局变量的情况不太一样。

    1. 非箭头函数

        >`this`取值类似于[动态作用域](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/程序员的自我修养/README.md#词法作用域动态作用域)。

        `this`：调用函数的那个对象（与在什么作用域无关）；`this`的值：在函数被调用时才会指定。

        1. 直接函数调用（如：`alert()`）、立即调用的函数表达式（如：`(function () {}())`）

            `this`：全局对象

            >严格模式：`undefined`
        2. 对象的方法调用（如：`obj1.obj2.func()`）

            `this`：最后一层对象（`obj2`）
        3. 间接调用（如：`alert.call/apply/bind(传入的值)`等[this替代](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/前端内容/标准库文档.md#this替代)）

            `this`：传入的值

            >1. 非严格模式，传入的值：
            >
            >    1. 若是引用数据类型，则传入什么给`this`，函数的`this`就是什么。
            >    2. 若是基本数据类型
            >
            >        1. 则`this`成为那个值的基本包装类型（除了`undefined/null`之外）；
            >        2. 若不传或传入`undefined/null`，则`this`为全局对象。
            >2. 严格模式，传入的值：
            >
            >    传入什么给`this`，函数的`this`就是什么。
        4. 构造函数实例化（如：`new RegExp()`）

            `this`：新实例对象

            >`new (func.bind(传入的值))()`的`this`是新实例对象，而不是 ~~`bind`传入的值~~。

        以上规则实施顺序（优先->其次）：构造函数实例化 -> 间接调用 -> 对象的方法调用 -> 直接函数调用。

        <details>
        <summary>e.g.</summary>

        ```js
        var x = "global";

        function windowTest() {
          console.log(this.x);
          console.log(_test());
          console.log(
            (function () {
              return this.x;
            })(),
          );

          function _test() {
            return this.x;
          }
        }

        /* window：方法没有对象调用（直接函数调用、立即调用的函数表达式，且与作用域无关） */
        windowTest(); // => global => global => global
        console.log("------------------");
        var obj1 = {
          x: 1,
          test1: function () {
            var that = this;

            return function () {
              console.log(this.x);
              console.log(that.x);
            };
          },
          test2: function () {
            console.log(this.x);
          },
        };
        obj1.test1()(); // => global => 1
        console.log("------------------");

        var { test1 } = obj1;
        test1()(); // => global|global
        console.log("------------------");

        setTimeout(obj1.test1(), 0); // => global => 1
        setTimeout(obj1.test2, 0); // => global

        /* 上级对象：函数作为某个对象的方法调用 */
        var obj2 = {};
        obj2.x = 2;
        obj2.func = windowTest;
        obj2.func(); // => 2 => global => global
        console.log("------------------");

        /* 新实例对象：构造函数 */
        function Test() {
          this.x = 3;
          console.log(this.x);
          console.log(_test());
          console.log(
            (function () {
              return this.x;
            })(),
          );

          function _test() {
            return this.x;
          }
        }

        var obj3 = new Test(); // => 3 => global => global
        console.log("------------------");

        /* 传入的指定对象：apply或call调用 */
        var obj4 = { x: 4 };
        obj2.func.call(obj4); // => 4 => global => global
        console.log("------------------");
        ```
        </details>

        ><details>
        ><summary>某些挂在<code>window</code>下的方法，内部实现有使用到<code>this</code>，且<code>this</code>需要指向特殊对象（如：必须指向<code>window</code>或<code>null</code>），因此当新建对象指向某方法时，注意this。</summary>
        >
        >```js
        >// e.g.
        >const a = {
        >  b: window.open
        >}
        >
        >a.b()           // TypeError: Illegal invocation
        >a.b.call({})    // TypeError: Illegal invocation
        >a.b.call(null)  // 正常
        >```
        ></details>
    2. 箭头函数

        不会创建自己的`this`（所以不会使用非箭头函数的规则），根据[词法作用域](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/程序员的自我修养/README.md#词法作用域动态作用域)向上遍历查找直到非箭头函数定义的`this`或全局对象（严格模式为undefined）；若找到`this`，则再根据非箭头函数的方式决定取值。

        >看上去就像：使用封闭执行上下文最近（**就近原则**）的一个`this`值。

        ><details>
        ><summary>e.g.</summary>
        >
        >```js
        >var a = {
        >  foo: () => { // 箭头函数
        >    return () => {
        >      console.log(this)
        >    }
        >  },
        >  bar () {     // 非箭头函数（简写的方法）
        >    return () => {
        >      console.log(this)
        >    }
        >  }
        >}
        >
        >a.foo()()        // => 全局对象
        >a.bar()()        // => a
        >
        >var b = a.bar
        >b()()            // => 全局对象
        >
        >
        >var foo1 = () => {console.log(this)}       // 箭头函数
        >var foo2 = function () {console.log(this)} // 非箭头函数
        >
        >var obj2 = {
        >  foo1: foo1,
        >  foo2: foo2
        >}
        >
        >var obj1 = {
        >  obj2: obj2
        >}
        >
        >obj1.obj2.foo1() // => 全局对象
        >obj1.obj2.foo2() // => obj2
        >
        >
        >var c = {
        >  d: {
        >    e: () => {
        >      console.log(this)
        >    }
        >  }
        >}
        >
        >c.d.e()          // => 全局对象
        >```
        ></details>

    - 回调函数里的`this`

        1. 回调函数是非箭头函数：取决于回调函数在代码实现逻辑里如何被调用。

            大部分是直接函数调用，如：`setTimeout(回调)`，回调内的this指向全局对象。
        2. 回调函数是箭头函数：与箭头函数一致。

<details>
<summary>e.g.</summary>

```js
function F() {
  this.func = function () {
    console.log("1");
  };

  func = function () {
    console.log("2");
  };

  return;
}

F.func = function () {
  console.log("3");
};
F.prototype.func = function () {
  console.log("4");
};

var func = function () {
  console.log("5");
};

function func() {
  console.log("6");
}

func(); // => 5
var a = new F();
a.func(); // => 1
func(); // => 2
new F.func(); // => 3
new F().func(); // => 1
new new F().func(); // => 1  === new (new F()).func();
```
</details>

### 闭包（closure）
>因为JS是[词法作用域](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/程序员的自我修养/README.md#词法作用域动态作用域)，所以产生了闭包效果。

1. 当函数体内定义了其他函数时，就创建了闭包。内部函数总是可以访问其所在的外部函数中声明的内容（链式作用域），即使外部函数执行完毕（寿命终结）之后。

    >有了[`let`、`const`](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/前端内容/标准库文档.md#letconst)之后，闭包应该改为：内部函数总是可以访问其所在的外部作用域中声明的内容。
2. 无论通过何种手段将内部函数传递到它所在的词法作用域以外，函数都会持有对原始定义作用域的引用（函数记住并访问它原始所在的词法作用域），无论在何处执行这个函数都会使用闭包。
3. 闭包通常用来创建私有变量或方法，使得这些内容不被外部访问，同时又可以通过指定的闭包函数访问。

- 产生效果：

    1. 可以操作函数体内的私有内容（特权方法）。
    2. 让被操作的私有内容始终保持在内存中不被垃圾回收。
    3. 占用较多的内存。

><details>
><summary>e.g.</summary>
>
>`var`只有全局作用域、函数作用域；`let`、`const`有全局作用域、函数作用域、块级作用域。
>
>```js
>for (var i = 0; i < 3; i++) {
>    // 不用匿名函数
>    setTimeout(function () {
>        console.log(i);         // => 3 => 3 => 3（闭包作用：每个结果都同一个值）
>    }, 0);
>}
>
>for (var i = 0; i < 3; i++) {
>    // 匿名函数
>    (function (para) {
>        setTimeout(function () {
>            console.log(para);  // => 0 => 1 => 2（结果是传入进匿名函数的参数）
>        }, 0);
>    }(i));
>}
>
>for (var i = 0; i < 3; i++) {
>    // ES6的块级作用域（ES6拥有了块级作用域之后，不再需要~~自执行匿名函数~~）
>    let num = i;
>    setTimeout(function () {
>        console.log(num);       // => 0 => 1 => 2
>    }, 0);
>}
>
> // ES6的块级作用域（ES6拥有了块级作用域之后，不再需要~~自执行匿名函数~~）
>for (let i = 0; i < 3; i++) {
>    setTimeout(function () {
>        console.log(i);        // => 0 => 1 => 2
>    }, 0);
>}
>
> // 块级作用域保证i每次都是新值，但var num又提升到函数作用域了，因此最后取num都是取同一个值
>for (let i = 0; i < 3; i++) {
>    var num = i;
>    setTimeout(function () {
>        console.log(num);        // => 2 => 2 => 2
>    }, 0);
>}
>
> // 局部变量用的是向上查找到的i
>let i; // 或`var i`
>for (i = 0; i < 3; i++) {
>    setTimeout(function () {
>        console.log(i);        // => 3 => 3 => 3
>    }, 0);
>}
>```
></details>

### 动态执行JS脚本（执行字符串）
1. 字符串转换为执行的JS代码：

    1. 浏览器：`eval`、`new Function`、`setTimeout/setInterval`
    2. Node.js：`eval`、`new Function`、`vm`模块

    ```js
    // 全部都极度不安全，不建议使用

    var a = 'console.log("aa")';
    var b = 'console.log("bb")';
    var c = 'console.log("cc")';
    var d = 'console.log("dd")';

    // 以下均会执行字符串内容
    eval(a);
    new Function(b)();
    setTimeout(c, 0);   // Node.js已不支持第一个参数传字符串
    setInterval(d, 0);  // 需要clearInterval。Node.js已不支持第一个参数传字符串
    ```

    ```js
    // Node.js

    var e = 'console.log("ee")';
    const vm = require("node:vm");
    const script = new vm.Script(e);
    script.runInThisContext();
    ```
2. 复制一个函数：`` eval(`(${func.toString()})`) ``或`new Function("return " + func.toString())()`

    >仅根据`func.toString()`创建，不包含`func`额外添加的属性。

    ```js
    function cloneFunction(func) {
      const funcStr = func.toString();
      try {
        // 或：return new Function("return " + funcStr)();
        return eval("(" + funcStr + ")"); // 不支持：`a={b(){}};`中`a.b`方法（以及后面catch还报错的）
      } catch {
        try {
          // 或：return new Function("return function " + funcStr)();
          return eval("(function " + funcStr + ")"); // 不支持：任何native code方法（包括.bind新创建的函数）
        } catch {
          return func; // 暂不处理、直接返回：任何native code方法（包括.bind新创建的函数）
        }
      }
    }
    ```

### 欺骗JS词法作用域
通过`eval`、`with`，能在JS运行期修改或创建书写期就确定的词法作用域。

>运行期修改或创建词法作用域，会导致JS无法进行JIT优化（当JS引擎遇到这些代码时，只能谨慎地不进行JIT优化，因此可能导致**所有**优化都失效）。且极度不安全，最好不要使用。

1. `eval`

    接受一个字符串作为参数，将其中的内容视为好像在书写时就存在于程序中这个位置的代码（用程序动态生成代码并运行，好像代码是写在这个位置一样）。

    ```js
    // e.g.
    function foo (str, a) {
      eval(str)         // 改变词法作用域
      console.log(a, b)
    }

    var b = 2
    foo('var b = 3', 1) // => 1 3
    ```

    - 类似的有：`setTimeout/setInterval`的第一个参数是字符串、`new Function`的最后一个字符串参数，都能动态生成代码，都能在运行期修改书写期的词法作用域。
2. `with`

    ```js
    // e.g.
    function foo (obj) {
      with (obj) { // 为形参obj创建作用域
        a = 2      // 作用域中查找变量a并赋值（若查找不到则向上查找，顶层也找不到则创建一个全局变量）
      }
    }

    var o1 = { a: 1 }
    foo(o1)
    console.log(o1.a)    // => 2

    var o2 = {}
    foo(o2)
    console.log(o2.a, a) // => undefined 2
    ```

### 原型
1. 构造函数、原型对象、实例、原型链

    1. 只有函数有`prototype`属性，指向函数的原型对象。

        互相连接：函数拥有`prototype`属性指向其原型对象，原型对象拥有`constructor`属性指向函数。

        >构造函数通过`prototype`为实例存储要共享的属性和方法，可设置`prototype`指向其他对象来继承其他对象。
    2. 当构造函数实例化（`new`），该实例拥有`[[Prototype]]`属性，指向**构造函数的原型对象**。

        >访问对象的`[[Prototype]]`属性：（非标准）`对象.__proto__`、`Object.getPrototypeOf(对象)/Object.setPrototypeOf(对象, 原型对象)`。

        1. 连接存在于**实例**与**构造函数的原型对象**之间，而不直接存在于~~实例与构造函数~~之间。
        2. 内置构造函数的原型上有各种方法和属性，实例对象通过原型链进行调用。
    3. 每个引用数据类型都有`[[Prototype]]`属性，指向`自己的构造函数.prototype`（原型对象）。

        >每个引用数据类型都显式或隐式由某个构造函数创建。
    4. 不断向上的`[[Prototype]]`属性，构成了原型链。

        >访问一个引用数据类型的属性：若这个属性在对象自身中不存在，则向上查找其`[[Prototype]]`指向的对象；若依然找不到，则继续向上查找（其`[[Prototype]]`指向的对象的）`[[Prototype]]`指向的对象，直到原型终点。

        原型链终点是`null`，倒数第二是`Object.prototype`。

        ```js
        Object或Function或任意函数.__proto_ === Function.prototype
        Function.prototype.__proto__ === Object.prototype
        Object.prototype.__proto__ === null
        ```

    <details>
    <summary>e.g.</summary>

    ```js
    var A = function () {};
    var a = new A();

    console.log('原型与构造函数：', A.prototype.constructor === A)
    console.log('实例与原型：', a.__proto__ === A.prototype)
    console.log('实例与构造函数:', a.__proto__.constructor === A)

    /*
     若a.constructor无定义，则向上查找a.__proto__.constructor；
     若依然没有定义，则继续向上查找a.__proto__.__proto__.constructor；
     ...
     直到原型链终点。
    */

    console.log(a.__proto__.__proto__ === Object.prototype)
    console.log(a.__proto__.__proto__.__proto__ === null)
    ```
    </details>
2. 若重写原型的值（不是添加），可以给原型添加`constructor`属性并指向**构造函数**

    ```js
    var A = function () {};

    A.prototype = {
        other: '...'
    };

    if (typeof Object.defineProperty === 'function') {

        // 使属性：不可以改变描述符、不可以删除、不可以枚举、不可以被赋值运算符改变
        Object.defineProperty(A.prototype, 'constructor', {
            value: A
        });
    } else {
        A.prototype.constructor = A;
    }
    ```
3. 通过**原型链**实现**继承**

- 纯粹的空对象（没有继承`Object.prototype`的空对象，原子空对象）：

    `Object.create(null)`或`Object.setPrototypeOf({}, null)`

    >`{}`等价于：`Object.create(Object.prototype)`

### 继承
1. 继承原理

    1. 子类继承父类属性：在子类构造函数体内调用父类构造函数。
    2. 子类继承父类原型链：

        1. 将父类构造函数的实例赋值给子类构造函数的原型，或ES6`Son.prototype = Object.create(Father.prototype)`
        2. 使用ES6的`class-extends`则自动实现
2. 继承方式

    1. ES6：`class-extends`

        **能够继承原生构造函数**：先新建父类的实例对象`this`，然后再用子类的构造函数修饰`this`，使得父类的所有行为都可以继承。

        ```js
        class Father {
          constructor (...args) {   // 可省略
            // this.
          }

           父类方法 () {}
        }

        class Son extends Father {
          constructor (...args) {   // 可省略
            super(...args)
            // this.
          }

          子类方法 () {}
        }


        /* 使用测试 */
        Son.__proto__  === Father                       // => true
        Son.prototype.__proto__ === Father.prototype    // => true


        var father1 = new Father('父para')
        var son1 = new Son('子para1', '子para2')

        son1.__proto__.__proto__ === father1.__proto__  // => true
        ```
    2. ES5模拟：寄生组合式继承

        **无法继承原生构造函数**：先新建子类的实例对象`this`，再将父类的属性添加到子类上，导致父类的内部属性无法获取。

        ```js
        /* 父类定义： */
        function Father(fatherPara) {
            // 私有属性用let；静态私有属性用const

            /* 父类属性 */
            this.父类属性 = fatherPara;
        }

        /* 父类原型链 */
        Father.prototype.父类原型链方法 = function () {};


        /* 子类定义： */
        function Son(sonPara1, sonPara2) {
            /* 子类继承父类属性 */
            Father.call(this, sonPara1);

            /* 子类属性 */
            this.子类属性 = sonPara2;
        }

        /* 子类继承父类原型链 */
        Son.prototype = new Father();
        Son.prototype.constructor = Son;
        // 或ES6：Son.prototype = Object.create(Father.prototype, {constructor: {value: Son}});

        Son.__proto__  = Father;    // 同步class的实现

        /* 子类原型链 */
        Son.prototype.子类原型链方法 = function () {};


        /* 使用测试 */
        Son.__proto__  === Father;                      // => true
        Son.prototype.__proto__ === Father.prototype;   // => true


        var father1 = new Father('父para');
        var son1 = new Son('子para1', '子para2');

        son1.__proto__.__proto__ === father1.__proto__  // => true
        ```

        ><details>
        ><summary>「子类继承父类原型链」可改为的不使用<code>Object.create</code>方式</summary>
        >
        >```js
        >(function (subType, superType) {
        >    function _object(o) {
        >        function F() {}
        >        F.prototype = o;
        >        return new F();
        >    }
        >
        >    var prototype = _object(superType.prototype);
        >    prototype.constructor = subType;
        >    subType.prototype = prototype;
        >}(Son, Father));
        >```
        ></details>

### 内存机制
1. JS自动完成内存分配、[回收](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/前端内容/基础知识.md#垃圾回收)。
2. [变量](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/前端内容/基础知识.md#js数据类型)在内存中的存储

    1. 栈内存（stack）：

        >先进后出，寄存速度快，栈数据可共享，系统自动分配，数据固定不灵活，空间大小有限制，超出则栈溢出。

        存储内容：变量标识（指向基本数据类型、引用数据类型的地址）、基本数据类型、引用数据类型的地址。
    2. 堆内存（heap）：

        >顺序随意，寄存速度慢，由程序申请，操作简单，存储空间较大（取决于系统有效虚拟内存）。

        存储内容：引用数据类型。
3. 变量的值传递

    变量（包括函数的参数）都是**值传递**（变量指向的值复制给另一个变量去指向）。

    1. 引用数据类型的浅复制

        1. 复制对象A时，对象B将复制A的所有字段。若字段是引用数据类型（内存地址），B将复制地址；若字段是基本数据类型，B将复制其值。
        2. 缺点：若改变了对象B（或A）所指向的内存地址所存储的值，则同时也改变了对象A（或B）指向这个地址所存储的值。
    2. 引用数据类型的深复制

        1. 新开辟一个内存空间，完全复制所有数据至新的空间，新对象指向这个新空间的地址（原对象不变化）。
        2. 优点：B与A不会相互依赖（A，B完全脱离关联）；缺点：复制的速度更慢，代价更大。

    - 数组（对象）的值传递

        >对于数组`arr`或对象`obj`。

        1. 清空数组（对象）

            1. 不改变原始数组（对象）

                `arr = []   // （新赋值一个空数组）`

                >对象：`obj = {}   // （新赋值一个空对象）`
            2. 改变原始数组（对象）

                `arr.length = 0`或`arr.splice(0, arr.length)`

                >对象：遍历属性并`delete`
        2. 改变传入函数的数组（对象），但不改变实参

            >不考虑原型链。

            1. 浅复制：

                1. `arr = [...arr]`（ES6的展开元素）

                    >对象：`obj = {...obj}`
                2. `[...arr] = arr`（ES6的解构赋值的剩余参数）

                    >对象：`({...obj} = obj)`
                3. `arr = arr.slice()`或`arr = arr.concat()`或`arr = Array.from(arr)`

                    >对象：`obj = Object.assign({}, obj)`（不推荐用：~~`obj = Object.create(obj)`~~）
                4. 一层[循环遍历](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/JS学习笔记/README.md#循环遍历)赋值
            2. [深复制](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/JS学习笔记/README.md#深复制深拷贝实现思路)。
4. <details>

    <summary>存储、值传递步骤举例</summary>

    ```js
    // e.g.
    var a = 'test1';            // i
    var b = {'key': 'test1'};   // ii
    var c = a;                  // iii
    c = 'test2';                // iv
    var d = b;                  // v
    d['key'] = 'test2';         // vi
    ```

    1. `var a = 'test1';`步骤：

        1. 声明a：查找栈内存中是否存在a，不存在则创建，不管是已存在还是新创建的a，都指向undefined。
        2. 为a赋值：在栈内存中查找'test1'，无则栈内存中创建'test1'，然后让a指向'test1'。
    2. `var b = {'key': 'test1'};`步骤：

        1. 声明b（同声明a）。
        2. 为b赋值：堆内存中创建{'key': 'test1'}，栈内存中创建其堆地址url_b，让b指向url_b。
    3. `var c = a;`步骤：

        1. 声明c（同声明a）。
        2. 为c赋值：在栈内存中查找a，找不到则抛出错误，找到a则让c指向a所指向的'test1'。
    4. `c = 'test2';`步骤：

        1. 在栈内存中查找c，未找到则声明一个全局变量c。
        2. 为c赋新值：在栈内存中查找'test2'，无则栈内存中创建'test2'，然后让c指向'test2'。
    5. `var d = b;`步骤：

        1. 声明d（同声明a）。
        2. 为d赋值：在栈内存中查找b，找不到则抛出错误，找到b则让d指向b所指向的url_b。
    6. `d['key'] = 'test2'`步骤：

        1. 在栈内存中查找d，找不到则抛出错误，找到d则通过其所指向url_b找到堆内存中的{'key': 'test1'}。
        2. 修改堆内存中的{'key': 'test1'}为{'key': 'test2'}。
    </details>

### 内存泄漏
> 内存泄露：计算机内存逐渐丢失。当某个程序总是无法释放内存时，出现内存泄露。

- 不是内存泄漏，只是不会被垃圾回收：

    1. 全局变量不会被垃圾回收：合理创建全局变量，[严格模式（`"use strict"`）](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/前端内容/标准库文档.md#严格模式)可以避免意外创建全局变量。
    2. 被闭包引用的变量不会被垃圾回收：合理使用闭包。
    3. 被遗忘的定时器或事件监听的回调函数：不使用时及时清除。
    4. `console`打印的`对象`，不会被垃圾回收：生产环境去除`console`日志。

1. DOM清空或删除时事件绑定未清除，引起的内存泄漏：删除DOM前，先移除事件绑定。

    浏览器已优化，原生的事件可以不关注解绑，第三方库的自定义事件要关注解绑。

    >jQuery的`empty`和`remove`会移除元素内部的一切，包括绑定的事件及与该元素相关的jQuery数据（data、promise等所有数据）；`detach`则保留所有jQuery数据。
2. <details>

    <summary>元素引用，引起的内存泄漏：指向DOM（包括后代）的变量，删除DOM后要设为<code>null</code>。</summary>

    ![内存泄漏图](./images/memory-leak-1.gif)

    ```js
    var refA = document.getElementById('refA');
    var refB = document.getElementById('refB');
    document.body.removeChild(refA);  // 尽管删除了，但DOM#refA不能GC回收，因为存在变量refA对它的引用

    refA = null;  // 将变量refA对DOM#refA引用释放，但因为子元素的间接引用，还是无法回收DOM#refA

    // 变量refB对DOM#refA的间接引用(变量refB引用了DOM#refB，而DOM#refB属于DOM#refA)

    refB = null;  // 将变量refB对DOM#refB的引用释放，DOM#refA和DOM#refB就可以被GC回收
    ```

    1. 黄色是指直接被JS变量所引用，在内存里。
    2. 红色是指间接被JS变量所引用，DOM#refA被DOM#refB间接引用，因此即使变量refA被清空，也没DOM被回收。
    3. DOM#refB由于属于parentNode，只要引用它的变量不释放，它所有的父元素（图中红色部分）都不会被删除。
    </details>

>随着JS引擎的更新，原来会导致内存泄漏的bug已经慢慢被修复，因此写代码时不太需要注意内存泄漏问题（误）；Node.js的内存泄漏比较严重、隐蔽、难根除。

- 关于内存优化的重要性

    1. 减少OOM（Out Of Memory，内存不足），提高应用稳定性
    2. 减少卡顿，提高应用流畅度
    3. 减少内存占用，提高应用后台运行时的存活率
    4. 减少异常发生和代码逻辑隐患

fixme: chrome如何查内存和内存泄漏，Node.js如何查隐蔽的内存泄漏和如何规避。`console.profile()和console.profileEnd()`

- 内存泄露的排查

    1. 通过Devtools工具

        - 通过 performance 面板查看内存使用率
        - 通过 Memory 面板查看内存使用情况

            1. 拍取快照，查看 shallow size（对象本身占用内存）、retained size（对象被删除可以释放的内存大小）
            2. 可以拍两个 snapshot，通过数量变化和引用关系，推断出可能出现内存泄露的位置，着重分析
    2. 通过`performance.memory`

### 深复制（深拷贝）实现思路
>参考：[深入剖析JavaScript的深复制](http://jerryzou.com/posts/dive-into-deep-clone-in-javascript/)。

1. 递归赋值（最全面方式）

    >深复制要处理的坑：循环引用、各种引用数据类型、执行性能。
2. 针对**仅能够被JSON直接表示的数据结构（对象、数组、数值、字符串、布尔值、null）**：

    `JSON.parse(JSON.stringify(obj));`
3. [`structuredClone(value[, { transfer }])`](https://developer.mozilla.org/zh-CN/docs/Web/API/structuredClone)

    使用[结构化克隆算法](https://developer.mozilla.org/zh-CN/docs/Web/API/Web_Workers_API/Structured_clone_algorithm)（注意支持的类型，对不支持的类型会导致抛出异常）。

>不考虑原型链。

4. `Proxy`

### 数据类型转换
>参考：[阮一峰：数据类型转换](http://javascript.ruanyifeng.com/grammar/conversion.html)、[ecma-262等于比较](https://262.ecma-international.org/#sec-islooselyequal)。

1. 强制转换

    1. `Number(参数)`

        1. 基本数据类型：

            e.g.

            ```js
            Number('123')       // 123
            Number('123a')      // NaN
            Number('')          // 0

            Number(true)        // 1
            Number(false)       // 0

            Number()            // 0

            Number(undefined)   // NaN

            Number(null)        // 0

            Number(Symbol(123)) // Uncaught TypeError: Cannot convert a Symbol value to a number

            Number(123n)        // 123
            ```

            >`parseInt`与`Number`均忽略字符串前后的不可见字符。`parseInt`从前向后逐个解析字符，只要开头有数字则返回数值；`Number`判断只要有一个字符无法转成数值，则返回`NaN`。
        2. 引用数据类型：

            若参数是**单个数值的数组**、**空数组**、**单个数值为undefined的数组**，则返回`数值`、`0`、`0`；否则返回`NaN`。

            e.g.

            ```js
            Number([5])             // 5
            Number([])              // 0
            Number([undefined])     // 0

            Number([1, 2, 3])       // NaN
            Number({})              // NaN
            ```

            - `Number(对象)`具体规则：

                1. 调用原对象自身的`valueOf`，若返回值是基本数据类型，则再使用`Number`，不再进行后续步骤；
                2. 调用原对象自身的`toString`，若返回值是基本数据类型，则再使用`Number`，不再进行后续步骤；
                3. 若以上返回都还是对象，报错`TypeError: Cannot convert object to primitive value`。
    2. `String(参数)`

        >与`` `${参数}` ``返回效果一致。

        1. 基本数据类型：

            1. 数值：

                转为相应的字符串
            2. 字符串：

                原来的值
            3. 布尔值：

                ```js
                String(true)        // 'true'
                String(false)       // 'false'
                ```
            4. `undefined`：

                `String(undefined)  // 'undefined'`
            5. `null`：

                `String(null)       // 'null'`
            6. `Symbol`：

                ```js
                String(Symbol())    // 'Symbol()'
                String(Symbol(1))   // 'Symbol(1)'
                String(Symbol('a')) // 'Symbol(a)'
                ```
            7. `BigInt`：

                `String(1n)         // '1'`
        2. 引用数据类型：

            若是数组，则返回该数组的字符串形式；否则返回一个类型字符串。

            ```js
            // e.g.
            String([1, 2, 3])                  // '1,2,3'
            String([1, [2], [3, [4, [5, 6]]]]) // '1,2,3,4,5,6'
            String({a: 1})                     // '[object Object]''
            ```

            - `String(对象)`具体规则：

                1. 调用原对象自身的`toString`，若返回值是基本数据类型，则再使用`String`，不再进行后续步骤；
                2. 调用原对象自身的`valueOf`，若返回值是基本数据类型，则再使用`String`，不再进行后续步骤；
                3. 若以上返回都还是对象，报错`TypeError: Cannot convert object to primitive value`。
    3. `Boolean(参数)`

        | 数据类型 | 转换为`true`的值 | 转换为`false`的值 |
        | :--- | :--- | :--- |
        | Undefined | 无 | `undefined` |
        | Boolean | `true` | `false` |
        | Number | 任何非零`Number`类型的值（包括无穷大） | `0`、`-0`、`+0`、（+-）`NaN` |
        | String | 任何非空`String`类型的值 | `''` |
        | Symbol | 任何`Symbol`类型的值 | 无 |
        | BigInt | 任何非零`BigInt`类型的值 | `0n`、`-0n`、`+0n` |
        | Object（引用数据类型） | 任何对象（包括基本包装类型） | `null` |

        >`数组.filter(Boolean)`等价于`数组.filter((item)=>Boolean(item))`简化筛选逻辑。
2. 自动转换

    1. 触发情况：

        1. **运算数的数据类型**与**运算符的预期**不符。
        2. 不同类型的数据互相运算。
        3. 对非布尔值类型的数据求布尔值。
        4. 对非数值类型的数据使用一元运算符（`+`、`-`）

            <details>
            <summary>e.g.</summary>

            ```js
            'a' + + 'a'         // 'a' + (+ 'a') -> 'a' + NaN -> 'aNaN'
            + '123';            // 123
            - [123];            // -123
            1 + undefined       // NaN
            '1' + undefined     // '1undefined'
            ```
            </details>
    2. 行为：

        预期什么类型的值，就调用该类型的转换函数。

        1. 自动转换为`Boolean`：

            1. `if`、`while`、`for`等条件语句。
            2. `条件运算 ? 表达式1 : 表达式2`。
            3. `!!条件运算`。
        2. 自动转换为`String`：

            主要发生在加法运算时：当一个值为字符串，另一个值为非字符串，则后者转为字符串。
        3. 自动转换为`Number`：

            除了~~加法运算符~~有可能把运算数转为字符串，其他运算符都会把运算数自动转成数值（包括一元运算符）。

        - `+`加法运算：

            >`Symbol`不能进行~~加法运算~~；`BigInt`只能和 `BigInt`、字符串、对象 进行加法运算。

            1. 若运算数有对象，先`ToPrimitive(对象)`转换为的基本数据类型，再按照下面方式继续自动转换或运算出结果；
            2. 若运算数有字符串，则都转换为字符串（`String(基本数据类型)`）进行；
            3. 若运算数是数值与布尔值，则布尔值转换为数值（`true` -> 1、`false` -> 0）进行。
3. `==`与`!=`进行的强制类型转换步骤

    1. 运算数若存在`NaN`，则返回`false`；

        >除了`!=`和`!==`，只要对比（`==`、`===`、`>`、`>=`、`<`、`<=`）的操作数有一个是`NaN`，则返回`false`。
    2. 运算数若存在`布尔值`，将布尔转换为数字（`true` -> 1、`false` -> 0）；
    3. 运算数若存在`字符串`, 有三种情况：

        1. 对方是`对象`，则进行`ToPrimitive(对象, 'string')`后进行对比；
        2. 对方是`数字`，字符串转数字；
        3. 对方是`字符串`，直接比较；
        4. 其他返回`false`。
    4. 若运算数是`数字`与`对象`，则对象进行`ToPrimitive(对象, 'number')`，再比较；
    5. 若运算数都是`对象`，则比较它们的`引用值`（若两个运算数指向同一对象，则返回`true`，否则`false`）；
    6. `null`与`undefined`不会进行类型转换, 但相等。

>1. `ToPrimitive`：依次调用对象的`valueOf`、`toString`，将对象转化了基本数据类型。
>2. `{ toString: () => {console.log('toString');return {}}, valueOf: () => {console.log('valueOf');return {}} }`对象来判断先调用哪个属性。

### `||`和`&&`和`??`
1. `expr1 || expr2`：

    1. 赋值操作：若expr1能转换成true（`Boolean(expr1)`）则返回expr1，否则返回expr2。

        若多个`||`，则取第一个为true的值（`Boolean(expr)`）或最后一个值，短路求值。
    2. 在Boolean环境（如：if的条件判断）中使用：两个操作结果中只要有一个为true，返回true；二者操作结果都为false时返回false。
2. `expr1 && expr2`：

    1. 赋值操作：若expr1能转换成false（`Boolean(expr1)`）则返回expr1，否则返回expr2。

        若多个`&&`，则取第一个为false的值（`Boolean(expr)`）或最后一个值，短路求值。
    2. 在Boolean环境（如：if的条件判断）中使用：两个操作结果都为true时返回true，否则返回false。
3. `expr1 ?? expr2`

    1. 赋值操作：若expr1不是`null`或`undefined`则返回expr1，否则返回expr2。

        若多个`??`，则取第一个 不是`null`或`undefined`值 或最后一个值，短路求值。

### 浏览器的`事件循环（event loop）`
>参考：[阮一峰：再谈Event Loop](http://www.ruanyifeng.com/blog/2014/10/event-loop.html)、[Help, I’m stuck in an event-loop.](https://vimeo.com/96425312)、[Tasks, microtasks, queues and schedules](https://jakearchibald.com/2015/tasks-microtasks-queues-and-schedules/)。

>不是在ECMAScript中定义，而是在[HTML Standard](https://html.spec.whatwg.org/#event-loops)中定义。

1. JS的主线程是单线程

    1. 原因：

        1. JS设计初衷是为了与用户互动、操作DOM等简单操作。
        2. 单线程提高效率，多线程会带来复杂的同步问题。
    2. 结果：

        1. 程序在执行时必须排队，且一个程序不能中断另一个程序的执行。
        2. 没有任何代码是立即执行的，但一旦进程空闲则尽快执行。
    3. 弥补单线程计算量太大、事件耗时太久影响浏览器体验：

        1. 新增**Web Worker**标准，但不能~~操作DOM~~，完全受主线程控制。

            >1. Worker与主线程通信，都通过`postMessage`（或`MessageChannel`）传递信息、通过监听`message`事件接受信息，信息通过[结构化克隆算法](https://developer.mozilla.org/zh-CN/docs/Web/API/Web_Workers_API/Structured_clone_algorithm)（一种深复制）复制后传递。
            >2. 在浏览器tab没有被激活时（inactive），定时器间隔的最小值会提升、进程执行会变慢。用`Web Worker`不会受浏览器是否激活的影响。
        2. 多个异步线程分别处理：**网络请求**、**定时器**、**读写文件**、**I/O设备事件**、**页面渲染**等。

            >DOM的变动（尤其是涉及页面重新渲染的部分），通常不会立即执行，而是每16毫秒执行一次。
2. 任务类型

    1. 同步任务（synchronous）：

        在主线程上排队执行的任务。
    2. 异步任务（asynchronous）：

        1. 先挂起到（对应种类的）工作线程等待结果，主线程不会因此阻塞；有结果后，发起通知进入（对应种类的）「任务队列」（task queue）；「执行栈」（execution context stack）为空后会读取并执行「任务队列」的通知对应的回调函数。

            >相同类型的异步工作线程是串行工作；不同类型的异步工作线程互不影响执行。
        2. 异步任务分为两种类型：

            1. macrotask（task，宏任务）一般包括:

                1. I/O、UI交互

                    监听的事件。
                2. `setTimeout`、`setInterval`、`setImmediate`

                    在当前「任务队列」的尾部，添加事件。
                3. AJAX、`fetch`
                4. `新的<script>`
            2. microtask（job，微任务）一般包括:

                1. `Promise`（`Promise.prototype.then/catch/finally(回调)`的回调）

                    `new Promise(回调)`的回调、`Promise.all/race/any/allSettled([回调])`的回调、`Promise.resolve/reject()`，都是同步任务。
                2. `async-await`（只有`await`是异步）

                    >生成器（generators）是中断-恢复同步运行-中断，不是异步任务。

                    `await`后若是方法则同步执行该方法，执行结果交给`await`后才是microtask（无论结果如何）。

                    ><details>
                    ><summary>e.g.</summary>
                    >
                    >```js
                    >async function func () {
                    >  await // 同步执行，执行完无论未完成/完成/失败，都异步microtask执行后面代码
                    >    new Promise((resolve) => {
                    >        console.log('a')       // 同步
                    >        resolve()
                    >    })
                    >    .then(() => {console.log('then1')}) // 异步microtask
                    >    .then(() => {console.log('then2')}) // 异步microtask
                    >
                    >    console.log('b')     // 等待await完成（microtask）
                    >}
                    >
                    >func()
                    >console.log('c')
                    >// => a c then1 then2 b
                    >```
                    >
                    >```js
                    >var obj = {
                    >  a () {
                    >    console.log('a')
                    >    return obj
                    >  },
                    >  b () {
                    >    console.log('b')
                    >  }
                    >}
                    >
                    >async function func () {
                    >  await // 同步执行，执行完无论未完成/完成/失败，都异步microtask执行后面代码
                    >    obj.a() // 同步
                    >      .b()  // 同步
                    >
                    >  console.log('d')  // 等待await完成（microtask）
                    >}
                    >
                    >func()
                    >console.log('c')
                    >// =>a b c d
                    >```
                    >
                    >```js
                    >var obj = {
                    >  a () {
                    >    console.log('a')
                    >    return obj
                    >  },
                    >  b () {
                    >    console.log('b')
                    >    return Promise.resolve()
                    >  }
                    >}
                    >
                    >async function func () {
                    >  await // 同步执行，执行完无论未完成/完成/失败，都异步microtask执行后面代码
                    >    obj.a() // 同步
                    >      .b()  // 同步
                    >      .then(() => {console.log('then1')}) // 异步microtask
                    >      .then(() => {console.log('then2')}) // 异步microtask
                    >
                    >  console.log('d')  // 等待await完成（microtask）
                    >}
                    >
                    >func()
                    >console.log('c')
                    >// =>a b c then1 then2 d
                    >```
                    ></details>
                3. `for-await-of`的方法体执行和迭代器遍历
                4. `MutationObserver`
                5. `queueMicrotask`

    3. 浏览器渲染相关的异步任务

        1. 渲染前执行

            `requestAnimationFrame` -> `IntersectionObserver`
        2. 渲染后若还有空闲时间：

            `requestIdleCallback`
3. JS的事件循环运行机制：

    1. 「执行栈」进行：

        1. 所有同步任务都在主线程上执行，形成一个「执行栈」，串行执行直到「执行栈」为空（只有前一个任务执行完毕，才能执行后一个任务）。
        2. 主线程之外，还存在「任务队列」。「执行栈」遇到异步任务则把其挂起到异步线程，只要异步线程有了运行结果，就在「任务队列」之中放置通知。
    2. 一旦「执行栈」中的所有同步任务执行完毕，系统就会（按照macrotask、microtask的事件循环运行机制）读取「任务队列」，把**一个**通知对应的回调函数加入执行栈。跳回步骤1（「执行栈」又有内容可以执行）。

        - macrotask、microtask的事件循环运行机制：

            1. 检查macrotask队列：

                1. 选择最早加入的任务X，设置为「目前运行的任务」并进入「执行栈」；若macrotask队列为空，则跳到第4步；

                    >最初时刻：「执行栈」为空，`<script>`作为第一个macrotask被运行。
                2. 「执行栈」运行任务X（运行对应的回调函数）；
                3. 设置「目前运行的任务」为`null`，从macrotask队列中移除任务X；
                4. 跳出macrotask队列、进行：检查microtask队列。
            2. 检查microtask队列：

                1. 选择最早加入的任务a，设置为「目前运行的任务」并进入「执行栈」；若microtask队列为空，则跳到第5步；
                2. 「执行栈」运行任务a（运行对应的回调函数）；
                3. 设置「目前运行的任务」为`null`，从microtask队列中移除任务a；
                4. 跳到第1步（检查下一个最早加入的microtask任务）；
                5. 跳出microtask队列、进行：检查macrotask队列 或 浏览器渲染。
            3. 浏览器渲染（根据屏幕刷新率、浏览器performance策略，如：每16.6ms才会触发一次）。

            >macrotask和microtast选择：若想让一个任务立即执行，则把它设置为microtask，除此之外都用macrotask。因为虽然JS是异步非阻塞，但在一个事件循环中，microtask的执行方式基本上是用同步的。

    ![事件循环图](./images/event-loop-1.png)
4. 由于异步函数是立刻返回，异步事务中发生的错误是无法通过外层的：`try-catch`、`Promise`、`async-await`来捕捉（但可以捕获`await`的`reject`）。

    每个事件循环都是一个独立的调用栈，不同调用栈之间无法互相`try-catch`错误，所以新的事件循环不会被原调用栈捕获错误，导致向上抛出错误（若新的事件循环内没有在自己的调用栈上设置`try-catch`）。

    ```js
    try {
      setTimeout(()=>{
        错误                                  // 异步的无法捕获，错误会向全局抛
      })
    } catch (e) {}


    try {
      Promise.resolve().then(() => { 错误 })  // 异步的无法捕获，错误抛给Promise变成未捕获的失败Promise实例，再向全局抛出
    } catch (e) {}


    new Promise((resolve, reject) => {
      Promise.resolve().then(() => { 错误 }) // 异步的无法捕获，错误抛给Promise变成未捕获的失败Promise实例，再向全局抛出
    }).catch(()=>{})


    async function func1 () {
      Promise.resolve().then(() => { 错误 }) // 异步的无法捕获，错误抛给Promise变成未捕获的失败Promise实例，再向全局抛出
    }
    func1().catch(()=>{})


    async function func2 () {
      await Promise.resolve().then(() => { 错误 }) // 错误可以被func2捕获
    }
    func2().catch(()=>{})
    ```

    - 解决办法：可以在异步回调内部再包一层`try-catch`，或Promise实例后添加`.catch`
5. JS的异步编程方式：

    1. 回调函数（可能产生回调地狱）
    2. 事件监听（观察者模式）
    3. Promise
    4. Generator
    5. async-await

### 定时器 && 重绘函数
1. 定时器（`setInterval`、`setTimeout`）

    >不适合制作动画。

    定时器触发后，会把**定时器处理程序（回调函数）**插入至等待执行的**任务队列**最后面。`setInterval`和`setTimeout`的内部运行机制完全一致。

    1. `setInterval/clearInterval`：

        1. 同一个被setInterval执行的函数只能插入一个**定时器处理程序**到**任务队列**。
        2. setInterval是间隔时间去尝试执行函数，不关注上一次是何时执行。
        3. 若setInterval触发时已有它的**定时器处理程序**在**任务队列**中，则忽略此次触发。直到没有它的**定时器处理程序**在**任务队列**后才可以再次插入（正在执行的不算在**任务队列**中）。
        4. 相邻的2次**定时器处理程序**可能小于或大于（或等于）设定的间隔时间。无法确定**定时器处理程序**何时执行。
    2. `setTimeout/clearTimeout`:

        [用setTimeout模拟setInterval](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/JS方法积累/实用方法/README.md#原生js用settimeout模拟setinterval)，可以提高性能（上一次执行完毕后延迟时间再执行下一次，而不是固定间隔时间都尝试执行），并且可以确保每次**定时器处理程序**执行间隔一定大于（或等于）设置的间隔时间。

    - `setImmediate/clearImmediate`：

        >主流浏览器不支持，仅ie10+、Node.js支持。

        大致类似于：`setTimeout(func, 0)`。

    >`setInterval`、`setTimeout`有最短延迟时间、最长延迟时间：
    >
    >1. 最短延迟时间大概是>4ms（从其他地方调用`setInterval`，或在嵌套函数达到特定深度时调用`setTimeout`）。浏览器和Node.js等的最短时间不同。
    >2. 若处于未激活窗口，则最短延迟时间可能扩大到>1000ms。
    >3. 有最大延迟时间，若延迟时间设置>`Math.pow(2, 31) - 1`ms，则延时溢出导致立即执行回调函数。
2. 重绘函数（`requestAnimationFrame/cancelAnimationFrame`）

    >[递归调用](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/JS方法积累/实用方法/README.md#原生jsrequestanimationframe的递归)。

    1. 浏览器重绘之前，进行一次：发起通知进入「任务队列」，等待「执行栈」调用。

        大部分浏览器是1秒钟60帧，也就是16.67ms进行一帧重绘。
    2. 替代执行时机无法保证的`setTimeout`、`setInterval`进行动画操作，提升渲染性能：

        1. 把每一帧中的所有DOM操作集中起来，在一次重绘或重排中完成动画，且时间间隔紧随浏览器的刷新频率。
        2. 仅仅绘制用户可见的动画。这意味着没把CPU或电池寿命浪费在绘制处于背景标签，最小化窗口，或页面隐藏区域的动画上。
        3. 当浏览器准备好绘制时（空闲时），才绘制一帧，此时没有等待中的帧。意味着其绘制动画不可能出现多个排队的回调函数，或阻塞浏览器。因此动画更平滑，CPU和电池使用被进一步优化。

- 空闲函数（`requestIdleCallback`、`cancelIdleCallback`）

    在浏览器空闲时期依次调用函数。

    >1. 只有当前帧的运行时间小于16.66ms时，回调函数才会执行。否则，就推迟到下一帧，若下一帧也没有空闲时间，则推迟到下下一帧，以此类推。
    >2. 第二个参数表示指定的毫秒数。若在指定的这段时间之内，每一帧都没有空闲时间，那么回调函数将会强制执行。

---
## 功能归纳

### 判断数据类型
1. `Object.prototype.toString.call(值);`（或`apply`）

    1. 没有跨帧问题。
    2. 放入**内置对象**，返回`'[object 构造函数的名称]'`的字符串

        >特例：自定义类型返回`'[object Object]'`，`undefined/null`返回对应名字。

        1. `undefined` 或 不填 -> `'[object Undefined]'`
        2. `null` -> `'[object Null]'`
        3. Boolean实例（包括：基本包装类型） -> `'[object Boolean]'`
        4. Number实例（包括：基本包装类型） -> `'[object Number]'`
        5. String实例（包括：基本包装类型） -> `'[object String]'`
        6. Symbol实例（包括：基本包装类型） -> `'[object Symbol]'`
        7. BigInt实例（包括：基本包装类型） -> `'[object BigInt]'`
        8. Object实例 -> `'[object Object]'`
        9. 自定义类型实例 -> `'[object Object]'`
        10. Array实例 -> `'[object Array]'`
        11. Function实例（包括：类） -> `'[object Function]'`
        12. Date实例 -> `'[object Date]'`
        13. RegExp实例 -> `'[object RegExp]'`
        14. <details>

            <summary>Error类型实例 -> <code>'[object Error]'</code></summary>

            `Error`、`EvalError`、`RangeError`、`ReferenceError`、`SyntaxError`、`TypeError`、`URIError`
            </details>
        15. Map实例 -> `'[object Map]'`
        16. Set实例 -> `'[object Set]'`
        17. WeakMap实例 -> `'[object WeakMap]'`
        18. WeakSet实例 -> `'[object WeakSet]'`
        19. Promise实例 -> `'[object Promise]'`
        20. 生成器实例 -> `'[object GeneratorFunction]'`
        21. `window` -> `'[object Window]'`
        22. `document` -> `'[object HTMLDocument]'`

            >参考：[MDN：HTML 元素接口](https://developer.mozilla.org/zh-CN/docs/Web/API/Document_Object_Model#HTML_元素接口)。

            继承`document`的各种DOM，返回`'[object HTML继承类Element]'`。
        23. HTMLCollection实例（DOM集合） -> `'[object HTMLCollection]'`
        24. NodeList实例（`DOM.childNodes`或`document.querySelectorAll`等返回） -> `'[object NodeList]'`
        25. `arguments` -> `'[object Arguments]'`
        26. `Math` -> `'[object Math]'`
        27. `JSON` -> `'[object JSON]'`
        28. `WebAssembly` -> `'[object WebAssembly]'`
        29. <details>

            <summary>「TypedArrays」实例 -> <code>'[object 构造函数名]'</code></summary>

            Int8Array、Uint8Array、Uint8ClampedArray、Int16Array、Uint16Array、Int32Array、Uint32Array、Float32Array、Float64Array
            </details>
        30. ArrayBuffer实例 -> `'[object ArrayBuffer]'`
        31. DataView实例 -> `'[object DataView]'`

        ><details>
        ><summary>对于没有声明的变量，直接使用会报<strong>引用不存在变量</strong>的错误，可以用<code>typeof</code>来使代码健壮</summary>
        >
        >`if (typeof 变量 !== 'undefined' && Object.prototype.toString.call(变量) === '[object 某]') {}`
        ></details>
2. `typeof 值`

    1. 没有跨帧问题。
    2. 返回一个表示值类型的字符串。

        1. 字符型 -> `'string'`
        2. 布尔型 -> `'boolean'`
        3. 数值型 -> `'number'`
        4. Symbol型 -> `'symbol'`
        5. BigInt型 -> `'bigint'`
        6. `undefined` -> `'undefined'`
        7. 函数 -> `'function'`

            >包括：类。
        8. 引用对象型 -> `'object'`

            >所有基本包装类型都返回`'object'`。
        9. `null` -> `'object'`

        >1. 因为`typeof null`返回`'object'`，因此要特别判断一下null。
        >2. ~~ie8-的DOM节点的方法返回不是function，而是`object`，因此只能用`方法名 in DOM`检测DOM是否拥有某方法。~~
3. `对象 instanceof 构造函数或类`

    >可用`构造函数或类.prototype.isPrototypeOf(对象)`（不能跨帧）代替。

    1. 不能跨帧（`<iframe>`、`window.open()`的新窗口）。

        >```js
        >/* 跨帧：浏览器的帧（frame）里的对象传入到另一个帧中，两个帧都定义了相同的构造函数或类 */
        >A实例 instanceof A构造函数或类; // true
        >A实例 instanceof B构造函数或类; // false
        >```
    2. 判断`构造函数或类.prototype`是否存在于对象的整条原型链（`[[Prototype]]`）上。

        若`构造函数或类.prototype === 对象.__proto__/对象.__proto__.__proto__/.../Object.prototype`，则返回`true`。否则返回`false`。
        >e.g. `new Number() instanceof Object; // true`
    3. （`instanceof`、`Object.prototype.isPrototypeOf`）**检测自定义类型的唯一方法。**
4. `属性名 in 对象`

    判断对象或对象的整条原型链（`[[Prototype]]`）上是否拥有属性名，不读取属性值。

    >1. `对象.hasOwnProperty(属性名)`仅检查在当前实例对象，不检测其原型链。
    >
    >    `对象.hasOwnProperty(属性名)`建议替代用：`Object.prototype.hasOwnProperty.call(对象, 属性名)`。
    >2. ie8-的DOM对象并非继承自Object对象，因此没有hasOwnProperty方法。

- Chrome的DevTools的控制台执行`queryObjects(构造函数)`，返回当前执行环境的构造函数创建的所有实例。

### 循环遍历
><details>
><summary>约定</summary>
>
>`obj`为对象实例，`arr`为数组实例。
></details>

>1. `continue`应用在循环（`while`、`do-while`、`for`、`for-in`、`for-of`），表示跳过当次循环；`break`应用在循环、`switch-case`，表示跳出整个循环。
>
>    不支持在 三元运算符 带上`continue`或`break`，会报错（请用`if-else`代替），e.g. `(i > 5) ? alert(i) : continue // 报错`。
>2. `forEach`、`map`、`filter`、`some`、`every`无法中止循环（`return`只结束回调函数）。
>3. `$.each/$dom.each`跳出循环用`return true`（功能等价于：`continue`）、`return false`（功能等价于：`break`）。

- 尽量不要在`for-in`、`for-of`、Array遍历方法中改变原数组项或值

    1. 若仅是删减项，则可以用`Array.prototype.filter`。
    2. 若是更复杂的情况，则可以用`Array.prototype.reduce`（最方便）或`for`（需要创建一个新变量保存结果，可能性能好些）。

1. 原生JS

    - 遍历对象的属性

        `Object.entries/values/keys/getOwnPropertyNames/getOwnPropertySymbols`、`for-in`、`JSON.stringify`、`Reflect.ownKeys`可以获得属性描述（数据属性、访问器属性）。

        ><details>
        ><summary>e.g.</summary>
        >
        >```js
        >const obj = {
        >  a: 'obj\'s a',
        >  [Symbol('b')]: 'obj\'s b'
        >}
        >Object.defineProperties(obj, {
        >  c: {
        >    value: 'obj\'s c',
        >    enumerable: true
        >  },
        >  d: {
        >    value: 'obj\'s d',
        >    enumerable: false
        >  },
        >  [Symbol('e')]: {
        >    value: 'obj\'s e',
        >    enumerable: true
        >  },
        >  [Symbol('f')]: {
        >    value: 'obj\'s f',
        >    enumerable: false
        >  }
        >})
        >
        >const arr = ['arr\'s a']
        >arr[Symbol('b')] = 'arr\'s b'
        >Object.defineProperties(arr, {
        >  c: {
        >    value: 'arr\'s c',
        >    enumerable: true
        >  },
        >  d: {
        >    value: 'arr\'s d',
        >    enumerable: false
        >  },
        >  [Symbol('e')]: {
        >    value: 'arr\'s e',
        >    enumerable: true
        >  },
        >  [Symbol('f')]: {
        >    value: 'arr\'s f',
        >    enumerable: false
        >  }
        >})
        >
        >
        >// 输出：可枚举 && !属性名是Symbol类型
        >console.info('\n for-in')  // for-in还会遍历整条原型链上的属性：可枚举 && !属性名是Symbol类型。
        >for (const i in obj) {
        >  console.log(i, obj[i])
        >}
        >for (const i in arr) {
        >  console.log(i, arr[i])
        >}
        >
        >console.info('\n Object.entries')
        >console.log(Object.entries(obj))
        >console.log(Object.entries(arr))
        >
        >console.info('\n Object.values')
        >console.log(Object.values(obj))
        >console.log(Object.values(arr))
        >
        >console.info('\n Object.keys')
        >console.log(Object.keys(obj))
        >console.log(Object.keys(arr))
        >
        >
        >// 输出：(可枚举 || 不可枚举) && !属性名是Symbol类型
        >console.info('\n Object.getOwnPropertyNames')
        >console.log(Object.getOwnPropertyNames(obj))
        >console.log(Object.getOwnPropertyNames(arr))
        >
        >
        >// 输出：属性名是Symbol类型
        >console.info('\n Object.getOwnPropertySymbols')
        >console.log(Object.getOwnPropertySymbols(obj))
        >console.log(Object.getOwnPropertySymbols(arr))
        >
        >
        >console.info('\n JSON.stringify')
        >// 输出：可枚举 && !属性名是Symbol类型
        >console.log(JSON.stringify(obj))
        >// 输出：数组的项（当做对象添加的属性不返回）
        >console.log(JSON.stringify(arr))
        >
        >
        >console.info('\n ...展开')
        >// 输出：可枚举
        >console.log({ ...obj })
        >// 输出：数组的项（当做对象添加的属性不返回）
        >console.log([...arr])
        >
        >
        >// 输出：所有键名
        >console.info('\n Reflect.ownKeys')
        >console.log(Reflect.ownKeys(obj))
        >console.log(Reflect.ownKeys(arr))
        >
        >
        >console.info('\n Map数据类型的遍历')
        >// 输出：Map的所有项
        >for (const i of new Map([['a', 'Map\'s a'], [Symbol('b'), 'Map\'s b']])) {
        >  console.log(i)
        >}
        >```
        ></details>

    1. <details>

        <summary><code>while</code>、<code>do-while</code></summary>

        ```js
        while (跳出判断) {

        }
        ```

        ```js
        do {

        } while (跳出判断);
        ```
        </details>
    2. <details>

        <summary><code>for</code></summary>

        ```js
        for (执行一次; 跳出判断; 每执行一次后执行) {

        }
        ```
        </details>
    3. <details>

        <summary><code>for-in</code></summary>

        遍历对象自身和整条原型链（`[[Prototype]]`）上的可枚举属性。

        ```js
        /* i为数组当前项的索引或对象当前项的属性名 */
        for (var i in obj或arr) {

        }
        ```

        >在`for-in`时，需要遍历的key值和顺序预先确定。若遍历到某个key，此key不存在（被删了或移出了），则会跳过不执行当前key。若在`for-in`内部新增的key，不会被遍历执行。且任何时候直接使用原对象/原数组会展示修改后的当前值。
        >
        >e.g.
        >```js
        >var originObj1 = { a: "aa", b: "bb" };
        >for (const key in originObj1) {
        >  originObj1[key + key] = originObj1[key] + originObj1[key];
        >  console.log(key, originObj1); // => 'a' {a: "aa", b: "bb", aa: "aaaa"} => 'b' {a: "aa", b: "bb", aa: "aaaa", bb: "bbbb"}
        >}
        >
        >var originObj2 = { a: "aa", b: "bb", c: "cc" };
        >for (const key in originObj2) {
        >  delete originObj2[key];
        >  console.log(key, originObj2); // => 'a' {b: "bb", c: "cc"} => 'b' {c: "cc"} => 'c' {}
        >}
        >
        >var originObj3 = { a: "aa", b: "bb", c: "cc" };
        >for (const key in originObj3) {
        >  delete originObj3.b;
        >  console.log(key, originObj3); // => 'a' {a: "aa", c: "cc"} => 'c' {a: "aa", c: "cc"}
        >}
        >
        >
        >const originArr1 = ["a", "b"];
        >for (const key in originArr1) {
        >  originArr1.unshift(key + "<-" + key);
        >  originArr1.push(key + "->" + key);
        >  console.log(key, originArr1); // => 0 ["0<-0", "a", "b", "0->0"] => 1 ["1<-1", "0<-0", "a", "b", "0->0", "1->1"]
        >}
        >
        >const originArr2 = ["a", "b", "c"];
        >for (const key in originArr2) {
        >  originArr2.splice(1, 1);
        >  console.log(key, originArr2); // => 0 ["a", "c"] => 1 ["a"]
        >}
        >```
        </details>
    4. <details>

        <summary><code>for-of</code></summary>

        遍历可迭代对象自身的项。

        ```js
        /* i为迭代对象的属性值 */
        for (let i of 可迭代对象) {

        }
        ```

        >若在`for-of`中改变原数组，则会影响遍历的项和顺序。且任何时候直接使用原数组会展示修改后的当前值。
        >
        >```js
        >// e.g.
        >var originArr = ['a', 'b', 'c']
        >for (let item of originArr) {
        >  originArr.pop()
        >  console.log(item, originArr) // => 'a' ['a', 'b'] => 'b' ['a']
        >}
        >```
        </details>
    5. Array方法

        ><details>
        ><summary>若在Array遍历的回调函数中改变原数组，则会影响遍历的项和顺序。且任何时候直接使用原数组会展示修改后的当前值</summary>
        >
        >```js
        >// e.g.
        >var originArr = ['a', 'b', 'c']
        >originArr.forEach((item, index, arr) => {   // 或其他所有Array.prototype.遍历方法
        >  originArr.pop()
        >  console.log(index, arr, originArr)   // => 0 ['a', 'b'] ['a', 'b'] => 1 ['a'] ['a']
        >})
        >```
        ></details>

        参数均为：`回调函数(当前值, 索引, 数组整体)[, this替代]`。

        1. `Array.prototype.forEach()`

            对数组的每个元素执行一次提供的函数。
        2. `Array.prototype.map()`

            数组中的每个元素调用提供的函数，组成新的数组。
        3. `Array.prototype.filter()`

            使用提供的函数测试所有元素，并创建包含所有通过测试的元素的新数组。
        4. `Array.prototype.every()`

            测试数组中是否所有元素都通过提供的函数。
        5. `Array.prototype.some()`

            测试数组中是否有一个元素通过提供的函数。
        6. `Array.prototype.find()`

            查找数组中通过提供的函数的第一个元素。
        7. `Array.prototype.findIndex()`

            查找数组中通过提供的函数的第一个元素的索引。

        >- 向后/向前对数组应用提供的函数，累计处理返回最后一个结果
        >
        >    1. `Array.prototype.reduce(回调函数(上一次调用返回的值, 当前值, 索引, 数组整体)[, 第一次调用回调函数的第一个参数])`
        >    2. `Array.prototype.reduceRight(回调函数(上一次调用返回的值, 当前值, 索引, 数组整体)[, 第一次调用回调函数的第一个参数])`
2. jQuery

    1. <details>

        <summary><code>$.each</code></summary>

        ```js
        /* index为数组当前项的索引或对象当前项的属性名或jQuery对象的索引，item为当前项的值（不是jQuery对象，是DOM对象，与this相同） */
        $.each(obj或arr或$dom, function (index, item) {

        });
        ```
        </details>
    2. <details>

        <summary><code>$dom.each</code></summary>

        ```js
        /* index为jQuery对象的索引，item为当前项的值（不是jQuery对象，是DOM对象，与this相同） */
        $dom.each(function (index, item) {

        });
        ```
    3. `$.grep`

        类似`Array.prototype.filter`

### 异步循环遍历
尝试 串联异步任务 循环遍历（一个任务完成才执行下一个任务）。

1. `while`、`do-while`、`for`、`for-in`、`for-of`配合`async-await`可以保证内部、外部的执行顺序按照预想结果进行

    <details>
    <summary>e.g. </summary>

    ```js
    var asyncFunc = (ms = 1000) => new Promise((resolve) => setTimeout(resolve, ms)) // 模拟异步操作

    async function func () {
      console.log('start')

      for (const i of [1, 2]) {   // while、do-while、for、for-in、for-of 同理
        await asyncFunc()    // 一项完成才会进行下一项，全部完成才会执行for之后代码。
        console.log(i)
      }

      console.log('end')
    }

    func()

    console.log('outside')

    // => start => outside =>（异步） => 1 => 2 => end
    ```
    </details>
2. Array方法配合`async-await`（或`Promise`）的执行顺序：

    1. 无效：回调函数内部加`async`（e.g. `arr.map(async()=>{})`）

        Array遍历方法内的每一项按项的顺序执行但不互相依赖（后面的项不会等前面的执行完毕才开始执行），`async-await`只能处理每一项自己方法内的执行顺序，不影响外部和其他项。

        <details>
        <summary>e.g. </summary>

        ```js
        var asyncFunc = (ms = 1000) => new Promise((resolve) => setTimeout(resolve, ms)) // 模拟异步操作

        function func () {
          console.log('start');

          ([1, 2]).forEach(async (item) => {  // forEach、map、filter、every 同理
            console.log('array start', item)
            await asyncFunc()
            console.log('array end', item)
          })

          console.log('end')
        }

        func()

        console.log('outside')

        // => start => array start 1 => array start 2 => end => outside =>（异步：） array end 1 => array end 2
        ```
        </details>
    2. 无效：方法外部加`await`（e.g. `await arr.map(()=>{})`）：

        Array遍历方法没有返回Promise实例，因此直接在外部加上`await`也是同步执行、无法达到预期效果。
    3. 利用`Array.prototype.reduce`实现

        ```js
        const chainingAsyncRun = (callbackArr) => {
          callbackArr.reduce(async (prevPromise, currentCallback) => {
            try {
              await prevPromise;
            } catch (e) {
              console.error(e);
            }
            return currentCallback();
          }, null);
        };
        ```
        <details>
        <summary>使用测试</summary>

        ```js
        /* 使用测试 */
        var funcArr = [
          () => {
            return new Promise((resolve, reject) => {
              setTimeout(() => {
                console.log(1);
                resolve(1);
              }, 500);
            });
          },

          () => {
            console.log(2);
          },
          () => {
            return new Promise((resolve, reject) => {
              setTimeout(() => {
                console.log(3);
                reject(new Error(3));
              }, 1000);
            });
          },
          () => {
            return new Promise((resolve, reject) => {
              setTimeout(() => {
                console.log(4);
                resolve(4);
              }, 1000);
            });
          },
          () => {
            console.log(5);
          },
        ];

        chainingAsyncRun(funcArr);
        ```
        </details>

    - 改用`while`、`do-while`、`for`、`for-in`、`for-of`等实现异步效果。
    - 使用第三方库，能够控制每一项之间的执行细节（并行、串行、等）：[async](https://github.com/caolan/async)、[bluebird](https://github.com/petkaantonov/bluebird)。

- 实现一个同时只能执行1个任务的[调度器](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/JS方法积累/手写代码/README.md#调度器任务并发单任务插入)

### 跨域请求
><details>
><summary>浏览器同源策略（协议、域名、端口号，必须完全相同）限制</summary>
>
>- 当一个资源从非同源中请求资源时，资源会发起一个跨域HTTP请求。出于安全原因，**浏览器**限制：从**脚本**内发起的跨源HTTP请求 或 拦截跨域HTTP响应。
>
>1. 跨域请求（XMLHttpRequest、Fetch等）不一定是浏览器限制了发起跨站请求，也可能是跨站请求可以正常发起，但返回结果被浏览器拦截。
>2. 现代浏览器会进行CORS处理，发起请求并与服务器协商（特例：有些浏览器不允许从HTTPS跨域访问HTTP，在请求还未发出时就拦截请求）。低版本浏览器可能不会发起跨域请求，直接拒绝发起请求。
></details>

1. [CORS](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/HTTP相关/README.md#corscross-origin-resource-sharing跨域资源共享)（服务端需要支持）

    >1. 不受同源政策限制。
    >2. ie9-的jQuery的非JSONP的AJAX跨域，要添加`jQuery.support.cors = true`。
2. JSONP（json with padding）（服务端需要支持）

    >1. 不受同源政策限制。
    >2. 只支持**GET**请求。

    网页通过添加一个`<script>`，向服务器发起文档请求（不受同源政策限制）；服务器收到请求后，将数据放在一个指定名字的回调函数里传回网页直接执行。

    ><details>
    ><summary>jQuery在它的<code>AJAX</code>方法中封装了<code>JSONP</code>功能</summary>
    >
    >```js
    >$.ajax({
    >    url: '接口地址',
    >    dataType: 'jsonp',
    >    jsonp: '与服务端约定的支持JSONP方法',  // 前端唯一需要额外添加的内容
    >    data: {},
    >    success: function (data) {
    >        // data为跨域请求获得的服务端返回数据
    >    }
    >})
    >```
    ></details>
3. websocket作为中转服务

    >1. 不受同源政策限制。
4. 其他方式

    1. 图片地址

        只能发送GET请求，无法访问服务器的响应文本。只能浏览器向服务器单向通信。常用来[统计](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/JS方法积累/实用方法/README.md#原生js用请求图片作log统计)。
    2. 通过代理服务器转发请求

        通过成功访问代理服务器（统一解决了跨域问题），利用代理服务器转发请求获得数据后（同源策略仅限于浏览器）再返回给浏览器。
    3. 通过[浏览器文档间的数据交互](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/JS学习笔记/README.md#浏览器文档间的数据交互文档与iframe文档与windowopen的新窗口)

        >e.g. A页面不存在同源策略问题，B页面存在同源策略问题，可通过A页面传递信息给B页面。

>解决浏览器显示`Script error`错误：①引用资源添加`<script src="CDN地址" crossorigin="anonymous"></script>` 且 ②CDN地址资源响应头包含`Access-Control-Allow-Origin: 请求头的Origin值 或 *`。

### 浏览器文档间的数据交互（文档与`<iframe>`、文档与`window.open()`的新窗口）
>若是完全独立、不存在父子关系的文档间，则只能通过后台服务或宿主环境服务进行通讯，`SharedWorker`支持同源的文档共同使用。

1. `document.domain`相同则可以文档间互相操作

    ><details>
    ><summary>不同源的文档间不能进行JS交互操作</summary>
    >
    >1. 可以获取window对象，但无法进一步获取相应的属性、方法。
    >2. 无法获取DOM、`cookie`、`Web Storage`、`IndexDB`。仅允许调用部分方法（白名单）。
    ></details>

    把不同文档的`document.domain`设置为一致的值，即可双向通信、互相操作（`cookie`可以直接操作；`localStorage`、`IndexDB`只能通过`postMessage`或`MessageChannel`通信）。

    ><details>
    ><summary><code>document.domain</code>使用限制</summary>
    >
    >1. `document.domain = `仅允许设置为当前域名或向上N级域，e.g. 域名为`a.b.c.com`的文档仅允许设置`document.domain`为：`a.b.c.com`或`b.c.com`或`c.com`。
    >2. `document.domain`（类似`location.hostname`）不包含端口号，意味着不同端口号的相同域名，默认`document.domain`相同，e.g. `http://localhost:3000`与`http://localhost:8899`默认的`document.domain`都是`localhost`。
    >3. 现代浏览器禁止修改`document.domain`解决办法：
    >
    >    1. 方案一：目标文档响应头包含`Origin-Agent-Cluster: ?0`，可允许浏览器在当前文档修改`document.domain`。
    >    2. 方案二：使用`postMessage`（或`MessageChannel`）传递信息的方案，代替相同`document.domain`共用cookie
    的方案。
    ></details>

    1. 与`<iframe>`通信：

        ```js
        // 父窗口调用`<iframe>`的window对象
        var newIframe = document.getElementById('new-iframe').contentWindow;    // 或：window.frames[0]


        // `<iframe>`调用父窗口的window对象
        var father = parent;
        ```
    2. 与`window.open()`的新窗口通信：

        ```js
        // 父窗口调用新打开窗口的window对象
        var newWin = window.open('某URL');


        // 新打开窗口调用父窗口的window对象
        var father = window.opener;
        ```
2. `postMessage`（或`MessageChannel`）文档间通信

    >1. 不受同源政策限制。
    >2. ie8、ie9仅支持与`<iframe>`，ie10+支持与`<iframe>`、`window.open()`的新窗口。

    ```js
    // 发送方（允许自己发给自己接受）
    目标window对象.postMessage(信息内容, '目标源地址或*');


    // 监听的文档
    window.addEventListener('message', function (e) {...}, false) // e.data === 信息内容
    ```
3. 其他方式

    1. 父窗口改变`<iframe>`的hash，`<iframe>`通过监听hash变化的`hashchange`事件获取父窗口信息

        >1. 不受同源政策限制。
        >2. ie8+支持。若只改变hash值，页面不会重新刷新。

        ```js
        // 父窗口改变`<iframe>`的hash值
        document.getElementById('new-iframe').src = '除了hash值，url不变';


        // `<iframe>`窗口监听hash变化，以hash变化当做信息的传递
        window.onhashchange = function () {
            var message = window.location.hash;
            // ...
        };
        ```
    2. 通过监听`window.name`传递信息

        >同会话（tab窗口）前后跳转的页面都可以读取、设置同一个`window.name`值。

        1. 父窗口打开一个子窗口，载入一个不同源的网页，该网页将信息写入`window.name`属性。
        2. 子窗口跳回一个与主窗口同域的网址（文档间访问`window.name`遵循同源策略）。
        3. 主窗口可以读取子窗口的`window.name`值作为信息的传递。

### Web Storage && cookie && IndexedDB
>1. 因为HTTP请求都会携带cookie，因此cookie最好仅用于服务端判定状态。
>2. 浏览器数据存储方式：变量、cookie、Web Storage、IndexedDB、~~Web SQL~~、~~`<html>`的Manifest~~、Service Workers。

1. Web Storage（`localStorage`、`sessionStorage`）

    1. 客户端保存，不参与服务器通信。
    2. 对象形式，键-值的内容都会转换为字符串（若不是字符串则它的`toString`方法）。
    3. ie8+支持（ie及FF需在web服务器里运行）。

        >ie6/7可以用它们独有的`UserData`替代使用。
    4. 单个对象数据大小5M+（或2.5MB~10MB）。
    5. 拥有方便的API

        同步。

        1. 调用`localStorage`、`sessionStorage`对象会为每个源（每个tab）创建独立的`Storage`对象，每个对象都拥有：

            `setItem`、`getItem`、`removeItem`、`clear`、`key`方法，`length`属性。没有~~索引功能~~。
        2. `window`的`storage`事件，会在其他tab的同源页面修改`localStorage`值时触发（增、删、改，`setItem`相同值时不触发）。
    6. 区别

        1. `localStorage`

            1. 同源共享。
            2. 持久化本地存储（关闭浏览器后继续保存；除非被清除，否则永久保存）。
            3. 应用场景：所有需要长期本地存储的数据。
        2. `sessionStorage`

            1. 同源且同会话（tab窗口）共享。
            2. 会话级别存储。跳转页面为同源后仍旧有效（不同tab不共通），关闭浏览器后被清除（重新加载或关闭后恢复，任然存在）。
            3. 应用场景：需要拆分成多个子页面分别存储的数据。
2. cookie

    1. 客户端保存（JS添加或响应头设置），始终在HTTP请求中携带（同源同路径，或父域名、父路径），明文传递，服务端接收、操作客户端cookie。

        >1. cookie中的`domain`（默认：当前域名），可设置为父域名或当前域名，不能设置为其他域名（设置失效）。
        >2. 当前域名可以访问`domain`为当前域名或父域名的cookie；浏览器发起HTTP请求时会向请求地址发送与请求域名相同或是其父域名的cookie。
    2. 字符串形式：`名1=值1[; 名2=值2]`。不能包含任何`,`、`;`、` `（使用`encodeURIComponent/decodeURIComponent`处理属性名和属性值）。
    3. 所有浏览器都支持。
    4. 单域名内，cookie保存的数据不超过4k，数量（最少）20个。

        >发送http请求时携带的cookie太多可能会导致nginx等阻绝访问，如返回：`400 Bad Request - request header or cookie too large`。可以设置更大的服务端接受配置 或 减少请求携带的cookie。
    5. 源生的cookie接口不友好，需要自己[封装操作cookie](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/JS方法积累/废弃代码/README.md#原生js操作cookie)。

        同步。

        1. JS的`document.cookie`：

            1. 新建或更新cookie（一条命令只能设置一条cookie）类似于服务端`Set-Cookie`响应头（一条命令可以设置多条cookie）：

                `名=值[; expires=绝对时间（时间戳）][; max-age=相对时间（秒）][; domain=域名][; path=路径][; secure][; samesite=Strict或Lax或None][; priority=low或medium或high]`

                >1. `Set-Cookie`可以额外设置`HttpOnly`属性；客户端的`document.cookie`不能修改、不能查看以及不能任何操作被设置为`HttpOnly`的cookie（获取不到值，也删除不了）。
                >2. 标记为`Secure`的cookie只能通过被HTTPS协议加密过的请求发送给服务端。非安全站点（HTTP）不能在cookie中设置`secure`，若设置，则此条新建或更新cookie无效。
                >3. `SameSite`是否应该限制在跨站点请求中发送。
                >4. `priority`是Chrome的提案。
                >5. 若设置cookie时不设置`expires`和`max-age`，则该cookie的过期时间是`session`或`会话`，表示：在当前的浏览器会话结束之后删除该cookie；若同时设置`expires`和`max-age`，则`max-age`优先级更高、优先生效；部分App会在App非激活状态或息屏状态下删除会话状态下的cookie；不同浏览器对cookie过期时间有不同上限，如：chrome上限400天。
            2. 读取cookie等同于客户端`Cookie`请求头：

                展示所有cookie`名1=值1[; 名2=值2]`（无法查看其他信息）。
            3. cookie的`名称`、`domain`（默认当前完整域名）、`path`（默认当前路由的path）一同唯一确定一个cookie，因此删除cookie项，需要关注这3个属性。
        2. 没有~~改变`cookie`的事件通知~~，只能轮询检测。
    6. 同源同路径，或父域名、父路径 共享。

        >子域名可以访问（获取/修改/删除）主域名的cookie。e.g. `a.b.c.com`可以获取`a.b.c.com`、`b.c.com`、`c.com`的cookie，但无法获取`d.a.b.c.com`或`d.com`的cookie。
    7. 默认：关闭浏览器后失效（存储在内存）；设置失效时间则到期后失效（存储在硬盘）。
    8. 应用场景：服务端确定请求是否来自于同一个客户端（cookie的session_id与服务端session配合），以确认、保持用户状态。

    ><details>
    ><summary>僵尸cookie（<a href="https://en.wikipedia.org/wiki/Zombie_cookie">zombie cookie</a>）</summary>
    >是指那些删不掉的，删掉会自动重建的cookie。僵尸cookie是依赖于其他的本地存储方法（如：Flash的share object、HTML5的local storages等），当用户删除cookie后，自动从其他本地存储里读取出cookie的备份，并重新种植。
    ></details>
3. IndexedDB

    1. 客户端保存，不参与服务器通信。
    2. 所有类型的数据都可以直接存入。

        1. 不属于~~关系型数据库~~（不支持~~SQL查询语句~~），更接近NoSQL数据库。
        2. 对象仓库中，数据以"键-值"的形式保存，每一个数据记录都有对应的主键，主键是独一无二的，不能有重复，否则会抛出一个错误。
        3. IndexedDB不仅可以储存字符串，还可以储存二进制数据（ArrayBuffer实例和Blob实例）。
    3. ie10+。
    4. 单个库储存空间250MB+。
    5. 异步。支持事务。

        复杂的API。
    6. 同源共享。
    7. 持久化本地存储。

>隐身模式策略：存储API仍然可用，并且看起来功能齐全，只是无法真正储存（如：分配储存空间为0）。

### 错误处理机制
>1. 当JS出现错误时，JS引擎会根据JS调用栈逐级寻找对应的`catch`（每个异步任务会创建各自独立的调用栈，不同调用栈之间不能互相`catch`），若**没有找到相应的catch handler**或**catch handler本身又有error**或**又抛出新的error**，则会把这个error抛给全局（浏览器会用各自不同的方式显示错误信息，可以用`window`的`error`进行自定义操作）。
>2. 在某个**JS block**（`<script>`或`try-catch`的`try`语句块）内，第一个错误触发后，当前JS block后面的代码会被自动忽略，不再执行，其他的JS block内代码不被影响。

1. 原生错误类型

    >来自：[MDN：Error](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Error)。

    错误类型：`Error`、`EvalError`、`RangeError`、`ReferenceError`、`SyntaxError`、`TypeError`、`URIError`。

    >代码错误 或 `throw 错误类型`才包含堆栈信息，`throw 非错误类型`不包含堆栈信息。
2. 自定义错误

    ```js
    // ES5
    function MyError(message) {
        this.stack = (Error.call(this, message)).stack;
        this.message = message || '默认信息';
        this.name = 'MyError';
    }
    MyError.prototype = Object.create(Error.prototype, {constructor: {value: MyError}});


    // ES6的class-extends
    class MyError extends Error{}
    ```
3. 手动抛出错误

    ```js
    throw 'Error'                  // 抛出字符串
    throw 100                      // 抛出数值
    throw true                     // 抛出布尔值
    throw { message: 'An Error' }  // 抛出对象
    throw new Error('An Error')    // 抛出Error类型错误，参数是字符串
    ```
4. 处理代码中抛出的错误

    >语法错误无法被各种方式捕获，e.g. `const a.c.`。

    1. `try-catch-finally`

        1. 必须`try-catch`或`try-finally`或`try-catch-finally`同时出现。
        2. 若有`catch`，则一旦`try`中抛出错误以后就先执行`catch`中的代码，然后执行`finally`中的代码。
        3. 若没有`catch`，`try`中的代码抛出错误后，则先执行`finally`中的语句，然后将`try`中抛出的错误往上抛。
        4. 若`try`中代码是以`return`、`continue`或`break`终止的，则必须先执行完`finally`中的语句后再执行相应的`try`中的返回语句。
        5. 在`catch`中接收的错误，不会再向上提交给浏览器。
        - `try-catch`能捕获其中所有同步代码，同步调用外部的方法也包含。

        >`try { setTimeout(() => { 错误 }, 0) } catch (e) {}`不会捕获异步操作中的错误（同理，在`Promise`或`async-await`等语法中的异步错误也无法被捕获，但可以捕获`await`的`reject`）。可以在异步回调内部再包一层`try-catch`、或用`window`的`error`事件捕获。

        ><details>
        >
        ><summary>注意：<code>finally</code>块总是在控制流退出<code>try-catch-finally</code>结构之前执行。它总是执行，无论是否抛出或捕获异常。</summary>
        >
        >1. 在`try`块正常执行完成后立即执行`finally`；
        >2. 在`catch`块正常执行完成后立即执行`finally`；
        >3. 在`try`块（无`catch`时）或`catch`块中将要执行控制流语句（`return`、`throw`、`break`、`continue`）退出块之前立即执行`finally`。
        >
        >    1. 如果`try`块中抛出异常，即使没有`catch`块来处理异常，`finally`块仍然执行，在这种情况下，异常仍然会在`finally`块正常执行完成后立即抛出。
        >    2. 在`finally`块中的控制流语句（`return`、`throw`、`break`、`continue`）将“覆盖”`try`块或`catch`块的控制流语句（`return`、`throw`、`break`、`continue`）。
        >
        >        ```js
        >        try {
        >          throw new Error("哦豁");
        >        } catch (ex) {
        >          console.error("内层", ex.message);
        >          // 退出之前先去执行finally，但是finally又使用控制流，因此“覆盖”下一行控制流不会执行
        >          throw ex; // 或 return 等
        >        } finally {
        >          console.log("最终");
        >          return;   // 或 throw 等
        >        }
        >
        >        // => 内层, 哦豁, 最终 （不会抛出错误）
        >        ```
        ></details>

    2. `window`的`error`事件

        1. 没有经过`try-catch`处理的错误都会触发`window`的`error`事件。
        2. 传参

            1. `window.onerror`方法会传入多个参数：`message`、`fileName`、`lineNumber`、`columnNumber`、`errorObject`。
            2. `window.addEventListener('error', (event) => {})`只会传入一个参数。
        3. 去掉控制台的异常显示

            1. `window.onerror`，若方法返回`true`，则浏览器不再显示错误信息。
            2. `window.addEventListener('error', (event) => {})`，若回调函数调用`event.preventDefault()`，则浏览器不再显示错误信息。

        - 无法捕获：~~语法错误~~、~~接口异常~~。

        >控制台输入的同步错误代码无法被`window`的`error`事件捕获，代码中、控制台输入的异步错误代码可以被捕获。

        ```js
        window.addEventListener('error', (event) => {
          /* code */

          event.preventDefault() // 浏览器不再显示错误信息
        })


        /**
         * window错误处理
         * @param {String} msg - 错误信息提示
         * @param {String} url - 错误出现url
         * @param {Number} line - 错误出现行数字
         * @param {Number} column - 错误出现列数字
         * @param {Object} error - 错误对象
         * @returns {Boolean} - true：不显示错误信息|false：显示
         */
        window.onerror = function (msg, url, line, column, error) {
          /* code */

          return true            // 浏览器不再显示错误信息
        }
        ```
    3. 资源加载错误的监听

        可以监听各资源的错误情况，包括：`<script>`、`<link>`、`<img>`、媒体资源、等。

        >`<iframe>`需要同源才能够监听事件。

        ```js
        window.addEventListener('error', function (event) { // 包含上面的：没有经过`try-catch`处理的错误都会触发`window`的`error`事件
          // 资源加载报错（event.target：错误资源的DOM）
          if (event.target && (event.target.src || event.target.href)) {
            const log = {
              type: "resourceError",
              fileName: error.target.src || error.target.href, // 哪个资源加载出错
              tagName: error.target.tagName,
            };
            console.log("静态资源加载报错", log); // 进行上报
          }
          // js 执行报错
          else {
            console.log("JS执行报错", event);
          }
        }, true)    // 资源的错误，必须要捕获（捕获是从root到目标元素，因此最外层window可以设置`event.stopPropagation()`阻止捕获继续传递）
        ```
    4. `window`的`unhandledrejection`事件

        若失败的Promise实例未被处理，则触发`window`的`unhandledrejection`事件。

        ```js
        window.addEventListener('unhandledrejection', (event) => {
          /* code */

          event.preventDefault()  // 浏览器不再显示错误信息
        })


        window.onunhandledrejection = function (event) {
          /* code */

          event.preventDefault()  // 浏览器不再显示错误信息。或：return false
        }
        ```
    5. 图像的`onerror`事件

        >1. 只要图像的src属性中的URL不能返回能被识别的图像格式，就会触发图像的`error`事件。
        >2. 错误不会提交到 ~~`window`的`error`~~。
        >3. `Image`实例或`<img>`的`error`事件没有任何参数。

        1. `<img>`的`error`事件

            ```html
            <img src="错误地址" onerror="func();">
            ```
        2. `Image`实例的属性

            ```js
            var img = new Image();  // 或document.createElement('img');

            img.onerror = function () {
                /* code */
            };

            img.src = '错误地址';
            ```
5. 运用策略
    >1. `window`的`error`主要捕获预料之外的错误；`try-catch`则用来在可预见情况下监控特定的错误。两者结合使用更加高效。
    >2. `window`的`unhandledrejection`主要捕获未被处理的 失败的Promise实例；`Promise.prototype.catch或then第二个参数`则用来在可预见情况下处理 失败的Promise实例。

    1. 非客户端页面

        仅需在加载JS之前配置好`window`的`error`。
    2. 客户端内嵌页面

        1. 在加载JS之前配置好`window`的`error`。
        2. 客户端回调函数嵌套一层`try-catch`，提示**哪个方法发生错误等额外信息**。

            >因为Native调用WebView的方法是直接通过函数运行JS代码，抛出错误时`window.onerror`传入的参数仅有第一个`message`参数。
        3. （可选）为了避免**JS代码还未加载完毕客户端就调用回调函数**，需在Native调用JS代码时嵌套一层`try-catch`（服务端代码中添加），提示**哪个方法发生错误等额外信息**。

    >捕获错误的目的在于避免浏览器以默认方式处理它们；而抛出错误的目的在于提供错误发生具体原因的消息。

    - 对于打包压缩的JS，可以用SourceMap进行还原定位错误位置，并且可以把SourceMap放在仅允许特殊IP访问的地方以限制外网人员查看。
    - 尽量避免~~静默错误~~（`try-catch`的`catch`没有任何处理，也没有任何提示）

        若添加`try-catch`捕获了错误，在`catch`中：要不然进行新的逻辑、要不然要把错误暴露出来。如：在`catch`中添加`console`或上报错误或其他方式能让开发者感知到出错了。

### 预加载
预加载，但不影响页面渲染，等待相关资源真正需要被使用时直接使用已预加载的资源 或 更快速的建立连接。

1. `<link>`预加载

    1. `<link rel="preload" href="资源">`

        >高优先级、页面渲染前。

        请求、下载、缓存资源。
    2. 兼容性较差：

        1. `<link rel="prefetch" href="资源">`

            >利用浏览器空闲时间去下载或预取用户在不久的将来可能访问的文档。

            请求、下载、缓存资源。
        2. `<link rel="prerender"  href="域名">`

            就像在后台打开了一个隐藏的tab，下载域名的所有资源、创建DOM、渲染页面、执行JS等等。
        3. `<link rel="dns-prefetch" href="域名">`

            解析DNS。
        4. `<link rel="preconnect" href="域名">`

            解析DNS，建立TCP握手连接、TLS协议。
2. 实现预加载图片

    1. JS

        ```js
        var img = new Image();  // 或document.createElement('img');

        img.src = '图片地址';

        img.onerror = function () {
            console.log('加载失败');
        };

        if (img.complete) {
            console.log('缓存');
        } else {
            img.onload = function () {
                console.log('新加载');
            };
        }
        ```
    2. CSS、HTML

        1. `background-image`

            当不触发页面渲染则不会加载，否则加载。

            >如：`display: none;`不会加载；`opacity: 0;`或`visibility: hidden/collapse;`等，会加载。
        2. `<img>`

            无论CSS设置什么，都会加载。

><details>
><summary>e.g. 预加载字体、图片、音频、视频，并显示进度条</summary>
>
>```vue
><template>
>  <div>
>    loading:{{ completedNumber }}/{{ resourceNumber }}
>
>    <!-- 字体 -->
>    <font>0123456789</font>
>
>    <!-- 图片 -->
>    <img
>      v-for="img of imgArray"
>      :key="img"
>      :src="img"
>      @load="loadHandler"
>    >
>
>    <!-- 音频/视频 （loadeddata、loadedmetadata） -->
>    <audio
>      v-for="audio of audioArray"
>      :key="audio"
>      :src="audio"
>      preload="auto"
>      @loadedmetadata="loadHandler"
>    />
>    <video
>       v-for="video of videoArray"
>       :key="video"
>       :src="video"
>       preload="auto"
>       @loadedmetadata="loadHandler"
>     />
>  </div>
></template>
>
><script>
>import img1 from '@/assets/images/图1.png'
>import img2 from '@/assets/images/图2.png'
>import img3 from '@/assets/images/图3.png'
>import img4 from '@/assets/images/图4.png'
>
>export default {
>  data () {
>    return {
>      imgArray: [
>        img1,
>        img2,
>        img3,
>        img4
>      ],
>
>      audioArray: [
>        '音频地址1',
>        '音频地址2',
>        '音频地址3'
>      ],
>
>      videoArray: [
>        '视频地址1',
>        '视频地址2'
>      ],
>
>      completedNumber: 0
>    }
>  },
>  computed: {
>    resourceNumber () {
>      return this.imgArray.length + this.audioArray.length + this.videoArray.length + 1  // 1：字体
>    }
>  },
>  mounted () {
>    // 字体 加载完毕
>    document.fonts.ready
>      .finally(() => {
>        this.completedNumber = this.completedNumber + 1
>      })
>  },
>  methods: {
>    // 图片、音频、视频 加载完毕
>    loadHandler () {
>      this.completedNumber = this.completedNumber + 1
>    }
>  }
>}
></script>
>
><style scoped>
>  @font-face {
>    font-family: "字体族名";
>    src: url("~@/assets/font/字体族名.woff") format("woff");
>  }
>  font {
>    font-family: 字体族名;
>    visibility: hidden;
>  }
>  img, audio, video {
>    display: none;
>  }
></style>
>```
></details>

### 判断对象、方法是否定义
1. 判断对象方法是否可以执行

    ```js
    /* 对象已经定义 && 对象不等于null && 对象方法存在 */
    if (typeof obj !== 'undefined' && obj !== null && typeof obj.func === 'function') {
        /* 对象方法已定义 可执行 */
    }
    ```
2. 判断全局对象方法是否可以执行

    ```js
    /* window的子对象存在 && 对象方法存在 */
    if (window.obj && typeof window.obj.func === 'function') {
        /* 对象方法已定义 可执行 */
    }
    ```
3. 判断是否需要重新定义

    ```js
    /* 对象不存在 || 对象等于null || 对象方法不存在 */
    if (typeof obj === 'undefined' || obj === null || typeof obj.func !== 'function') {
        /* 对象或对象方法没有定义 需重新定义 */
    }
    ```
4. 变量已定义

    ```js
    /* 变量已定义 && 变量不等于null */
    if (typeof a !== 'undefined' && a !== null) {
        /* 对象已定义 可操作 */
    }
    ```

### 浏览器缓存
>[深入理解浏览器的缓存机制](https://juejin.cn/post/6844904023665934349)。

1. [HTTP定义的缓存机制](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/HTTP相关/README.md#http缓存)
2. 数据缓存

    >因为保存在客户端，因此都不应该保存用户的隐私数据。

    Web Storage（`localStorage`、`sessionStorage`）、cookie、IndexDB、等。
3. 其他缓存机制（不推荐）

    1. HTML的`<meta>`设置缓存情况：

        e.g. 设置不缓存：

        ```html
        <meta http-equiv="pragma" content="no-cache">
        <meta http-equiv="cache-control" content="no-cache">
        <meta http-equiv="expires" content="0">
        ```
    2. `<html>`的`manifest`应用程序缓存：

        ```html
        <html manifest=".manifest文件/.appcache文件">
        ```

### JS压缩细节
>来自：[Javascript代码压缩细节](http://www.airmyth.com/thread-1801-1-1.html)。

>类似[编译器编译原理](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/程序员的自我修养/README.md#编译器编译原理)：parse -> AST -> 转换（压缩逻辑） -> code generate。

试着生成新的代码，对比后输出最短的内容。

1. 去除注释、多余的分隔符与空白符，标识符简写。
2. 压缩表达式

    1. 表达式预计算

        将可预先计算的表达式替换成其计算结果，并比较原来表达式与生成后的结果的大小，取短的。
    2. 优化`true/false`

        1. `true`

            1. 在`==/!=`运算 -> `1`
            2. 其他运算 -> `!0`
        2. `false`

            1. 在`==/!=`运算 -> `0`
            2. 其他运算 -> `!1`
    3. 优化`&&/||`

        1. `true && 表达式` -> `表达式`
        2. `false && 表达式` -> `!1`
        3. `true || 表达式` -> `!0`
        4. `false || 表达式` -> `表达式`
3. 缩短运算符

    1. `===/!==`的两个操作数都是`String`类型或都是`Boolean`类型的，缩短成`==/!=`。
    2. 缩短赋值表达式

        >参考：[MDN：赋值运算符](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators#赋值运算符)。

        对于类似`a = a + b`的赋值表达式（`+` `-` `*` `/` `%` `**` `&&` `||` `??` `>>` `>>>` `<<` `&` `|` `^`），可以缩短成`a += b`。

        >1. 位运算：`>>`符号传播右移、`>>>`无符号右移/零填充右移、`<<`左移、`|`按位或、`&`按位与、`^`按位异或。
        >2. 逻辑复制：逻辑与赋值`x &&= y`运算仅在x为真值时为其赋值；逻辑或赋值`x ||= y`运算仅在x为假值时为其赋值；逻辑空赋值运算符`x ??= y`仅在x是空值`undefined/null`时对其赋值。
    3. `!`操作符的压缩

        对于`!(a>=b)`，若转换后`a<b`得到更短的代码，则转换。
4. 去除没用的声明

    1. 去除重复的指示性字符串，如：`"use strict"`。
    2. 去除没有使用的函数参数。
    3. 去除函数表达式的函数名（若未使用）。
    4. 去除没用的块语句。
    5. 去除没有使用的`break`。
    6. 去除没有引用的`label`。
    7. 去除没有作用的`toString`调用。
5. 压缩`while`

    1. 去除根本不会执行的`while`，如：`while(false){}`。
    5. `while(true){}` -> `for(;;){}`
6. `条件判断 ? 表达式1 : 表达式2`

    1. 若`条件判断`有`!`，则去除`!`且调换表达式前后位置。
    2. 若`条件判断`为常数，则直接缩短为某一个表达式。
7. 压缩语句块

    1. 连续的表达式语句合并成一个逗号表达式`,`。
    2. 多个`var`声明可以压缩成一个`var`声明。
    3. `return`之后的非变量声明、非函数声明可以去除。
    4. 合并块末尾的`return`语句及其前边的多条表达式语句。
8. 优化`if`

    1. 去除没用的、空的`if/else`分支。
    2. 尝试反转`if/else`分支，看看生成代码是否更短。
    3. 若`if`块里边仅有一个`if`语句，且`else`块为空，则可以合并这两个`if`。
    4. 若`if`最后一个语句是跳出控制语句，则可以把`else`块的内容提到`else`外边，然后去掉`else`。
    5. 若`if/else`里各仅有一条`return`语句，则可以合并这两句`return`。
    6. 若`if/else`里各仅有一条语句，则可以转换为三元运算符表达式。
    7. 若`if/else`其中一个块为空，另一个块仅有一条语句，则可以转化成`||/&&`表达式。

### JS混淆（加密）细节
>参考：[JavaScript混淆安全加固](https://github.com/yacan8/blog/blob/master/posts/JavaScript混淆安全加固.md)。

减少加密的成本、增加破解的成本，「当你采用的加密模式，使得攻击者为了破解所付出的代价 远远超过其所获得的利益之时，你的加密方案就是安全的」。

---
## 编程技巧

### JS代码风格规范（coding style guide）
1. 严格模式`use strict`

    可用于全局，也可以用于局部（函数体内）。

    >1. 不推荐在全局作用域中使用，因为当有JS文件合并时，一个文件的全局严格模式会导致整个文件都是严格模式。
    >2. 可以用`(function () {'use strict';/* 执行内容 */}());`匿名函数方式使用严格模式。
2. 全等`===`（不全等`!==`）与等号`==`（不等`!=`）的区别

    >[JS比较表](https://dorey.github.io/JavaScript-Equality-Table/)。

    1. 当比较的两个值的类型不同时，`==`和`!=`都会强制[类型转换](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/JS学习笔记/README.md#数据类型转换)，再进行转换后值的比较。
    2. 用`===`和`!==`则不会转换，若类型不同则直接返回`false`。

        >`NaN`是唯一不全等于自己的值；`+0`和`-0`全等相等。

        使用`===`进行判断的内置方法：`Array.prototype.indexOf/lastIndexOf(查找的元素)`、`「TypedArrays」.prototype.indexOf/lastIndexOf(查找的元素)`、`switch-case`。

    - 通过类似`===`判断是否相同，但额外能判断`NaN === NaN`成立的内置方法：`Array.prototype.includes(查找的元素)`、`「TypedArrays」.prototype.includes(查找的元素)`、`Map`（不重复的键）、`Set`（不重复的值）。

    - `Object.is`与`===`区别：`+0`与`-0`返回`false`；（+-）`NaN`与`NaN`返回`true`。

    >1. 建议：都用`===`或`!==`进行比较。
    >2. `>=`等价于：`== || >`；`<=`等价于：`== || <`。
3. 三元运算符应当仅仅用在条件赋值语句中，而不要作为`if`语句的替代：

    1. `var a = condition ? '1' : '2';`
    2. ~~`condition ? func1() : func2();`~~
4. 命名

    1. 变量命名的前缀应当是**名词**，函数命名的前缀应当是**动词**。
    2. 约定函数名：

        1. `can`、`has`、`is`开头的返回值是布尔型。
        2. `get`开头的返回是非布尔型。
        3. `set`开头的执行保存动作。
    3. 常量用大写字母和下划线分割，如：`MAX_COUNT`。
    4. 构造函数用大驼峰命名法（Pascal Case），首字母大写（以非动词开头），单词首字母大写：

        1. `var a = new Person();   // 构造函数`
        2. `var b = getPerson();    // 普通函数`
    5. 不要用多行的字符串写法

        ><details>
        ><summary>e.g.</summary>
        >
        >```js
        >/* 不提倡的多行写法 */
        >var a = 'abc\
        >def';
        >
        >
        >/* 一般写法 */
        >var b = 'abc' +
        >    'def';
        >```
        ></details>
    6. 对象的属性、方法，与变量、方法命名规则相同。
    7. 若属性、变量、方法在表示其是私有的，可在开头加一个下划线`_`作为区分。
5. 使用字面量替代构造函数（普通函数）的[数据创建方式](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/前端内容/基础知识.md#数据创建方式)

    >好处：
    >1. 代码更少。
    >2. 不需要构造函数的「作用域解析」（scope resolution），提高性能。
    >3. 构造函数可以接收参数，返回的实例不可控、易混淆；字面量简单不出错。

    1. 对象

        e.g.

        ```js
        /* 不提倡的构造函数写法 */
        var a1 = new Object();
        a.attr1 = '...';
        var a2 = new Object({attr1: '...'});


        /* 提倡的字面量写法 */
        var b = {attr1: '...'};
        ```
    2. 数组

        e.g.

        ```js
        /* 不提倡的构造函数写法 */
        var arr1 = new Array('a', 'b');


        /* 提倡的字面量写法 */
        var arr2 = ['a', 'b'];
        ```
    3. 字符串

        e.g.

        ```js
        /* 不提倡的构造函数写法 */
        var str1 = new String('a');


        /* 提倡的字面量写法 */
        var str2 = 'a';
        ```

    - 其他数据类型
6. 注释规范

    1. 单行注释：`//`后不空格

        - 使用场景：

            1. 代码上方独占一行，缩进与备注内容一致，注释前必须空一行。
            2. 代码尾部（至少一个缩进）。
            3. 被注释的大段代码。
    2. 多行注释：`/*`和`*`后空一格

        - 使用场景：

            1. 代码上方独占多行，缩进与备注内容一致，注释前必须空一行。
            2. 作用：

                1. 难以理解的代码。
                2. 可能被误认为错误的代码。
                3. 浏览器特性hack。
    3. 函数注释规范（使用部分[JSDoc](https://jsdoc.app/)）

        >[@param](https://jsdoc.app/tags-param)、[@returns](https://jsdoc.app/tags-returns)。

        ```js
        /**
         * 方法描述
         * @constructor - （是否构造函数）
         * @param {Number} param1 - 参数描述，限制值为：1 描述|2 描述|3 描述
         * @param {Object|String|Boolean|Function|Array} param2 - 参数描述
         * @param {*} [param3] - 任意类型、可选参数
         * @param [param4 = 'default'] - 可选参数拥有默认值
         * @param {Object} param5 - 对象
         * @param {Object|String|Boolean|Function|Array} param5.param5_1 - 对象的属性描述
         * @param {...Number} param6 - 可重复使用参数（不好理解）
         * @returns {Object|Undefined} result - 参数描述
         */
        function func(param1, param2, param3, param4, param5, param6) {
            // param5.param5_1

            return result;
        }
        ```

        >jsdoc中类型的注释，大部分都可以用ts定义。
7. JS编程风格总结（programming style）

    >参考：[阮一峰：JavaScript 编程风格](http://javascript.ruanyifeng.com/grammar/style.html)。

    1. 表示区块起首的大括号，不要另起一行。
    2. 调用函数时，函数名与左括号之间没有空格。
    3. 所有其他语法元素与左括号之间，都有一个空格。
    4. 不要省略句末的分号。
    5. 不要使用`with`语句。
    6. 不要使用「相等」（`==`）运算符，只使用「严格相等」（`===`）运算符（同理仅使用`!==`，不使用`!=`）。
    7. 不要将不同目的的语句，合并成一行。
    8. 所有变量声明都放在函数的头部。
    9. 所有函数都在使用之前定义。
    10. 避免使用全局变量；*若不得不使用，则用大写字母表示变量名。*
    11. 不要使用`new`命令，改用`Object.create()`命令。
    12. 构造函数的函数名，采用首字母大写；其他函数名，一律首字母小写。
    13. 不要使用自增（`++`）和自减（`--`）运算符，用`+= 1`和`-= 1`代替。
    14. 不省略大括号。
8. JS编码规范

    绝大部分同意[fex-team:tyleguide](https://github.com/fex-team/styleguide/blob/master/javascript.md#javascript编码规范)。

    >可以设置为IDEs的**Reformat Code**的排版样式。
9. 用户体验

    1. 平稳退化（优雅降级）：当浏览器不支持或禁用了JS功能后，访问者也能完成最基本的内容访问。

        1. 为JS代码预留出退路（`<a>`添加`href`属性，用JS事件绑定去拦截浏览器默认行为）

            `<a href="真实地址" class="j-func">...</a>`

            >`href="真实地址"`也是为了SEO。
        2. ~~javascript伪协议~~

            `<a href="javascript: func();">...</a>`
        3. ~~内嵌事件处理程序~~

            `<a href="#" onclick="func();return false;">...</a>`
    2. 渐进增强：先完成基本通用功能，再追加额外功能。
    3. 向后兼容：确保老版本浏览器基本可用，使之虽不能支持某些功能，但仍能基本访问。

        1. 能力检测：`if(func){func();}`（最适当方式）。
        2. 怪癖检测：`try-catch`。
        3. 浏览器嗅探技术（用户代理`navigator.userAgent`检测）。
    4. 资源分离：把样式表、脚本分离出HTML。

        1. 使用外部资源。
        2. 不在HTML内嵌：事件处理程序、javascript伪协议。
        3. 对只为DOM增添的内容，转移到外部资源中动态创建。
    5. 性能优化[从URL输入之后](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/前端内容/README.md#页面解析渲染步骤)就开始考虑。

        1. 关于「性能」的写法建议，更多的是一种编程习惯（微优化）：写出更易读、性能更好的代码。
        2. 在解决页面性能瓶颈时，要从URL输入之后就进行[网站性能优化](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/前端内容/README.md#网站性能优化)；避免在处理网页瓶颈时进行~~微优化~~。

### 编程实践（programming practices）
1. UI层的松耦合

    1. 不要~~用JS修改CSS样式~~，JS仅修改class（任何时刻，CSS中的样式都可以修改，而不必更新JS）。

        >特例：根据页面重新定位，可以用JS设定位置（如：`top`、`left`等）。
    2. 将HTML从JS中抽离，避免增加跟踪文本和结构性问题的复杂度。可以使用模板引擎，如：[handlebars.js](https://github.com/wycats/handlebars.js)。
2. 避免使用全局变量

    >任何来自函数外的数据都应当以参数形式传进函数：将函数与其外部环境隔离开。

    1. 单全局变量

        唯一全局对象是独一无二的（不与内置API冲突），并将所有功能代码都挂载到这个全局对象上，因此每个可能的全局变量都成为这个唯一全局对象的属性（或方法）。
    2. 零全局变量（立即调用的函数表达式）

        隔离代码。

        ```js
        (function (win) {
            'use strict';   // 严格模式可以避免创建全局变量

            var doc = win.document;
            /* 代码 */
        }(window));
        ```
3. 事件处理程序

    1. 把事件逻辑（与用户行为相关的代码）与应用逻辑（与应用相关的功能性代码）隔离开。
    2. 不要分发事件：

        让事件处理程序成为接触到`event`对象的唯一函数，在event进入应用逻辑前完成用户相关操作（包括阻止默认事件或阻止冒泡等）。
4. 将配置数据从代码中分离

    配置数据：URL、展示内容、重复的值、设置、任何可能发生变更的值。

### 函数防抖、函数节流
>都是用来限制某个函数在一定时间内执行次数的技巧。

1. 防抖（debounce）

    一个函数被调用后不执行，在间隔时间内没有再次被调用才执行（或一调用就执行，在间隔时间内没有再次被调用才可以进行下一次执行）；若在间隔时间内再次被调用，则刷新等待时间并且继续等待间隔时间结束后才执行。
2. 节流（throttle）

    一个函数无法在间隔时间内连续执行，当上一次函数执行后过了间隔时间后才能进行下一次该函数的调用。

### 自执行匿名函数（拉姆达，λ，lambda）
立即调用的函数表达式（IIFE，Immediately Invoked Function Expression）。

>ES6拥有了块级作用域之后，不再需要~~自执行匿名函数~~。

1. 写法：

    >`function`关键字当作一个**函数声明**的开始，函数声明的后面不能跟圆括号；将函数声明包含在圆括号中，表示**函数表达式**，函数表达式的后面可以跟圆括号，表示执行此函数。

    ```js
    /* 建议方式 */
    ;(function () {}())
    ;(function () {})()
    ;(() => {})()       // 箭头函数

    /* 不推荐方式 */
    ;[function () {}()]

    ~function () {}()
    !function () {}()
    ;+function () {}()
    ;-function () {}()

    delete function () {}()
    typeof function () {}()
    void function () {}()
    new function () {}()
    new function () {}

    var f = function () {}()

    1, function () {}()
    1 ^ function () {}()
    1 > function () {}()
    ```
2. 传值进自执行匿名函数可以避免闭包导致无法记录变量值的问题

    ><details>
    ><summary>e.g.</summary>
    >
    >```js
    >for (var i = 0; i < 3; i++) {
    >    // 不用匿名函数
    >    setTimeout(function () {
    >        console.log(i);         // => 3 => 3 => 3（闭包作用：每个结果都同一个值）
    >    }, 0);
    >}
    >
    >for (var i = 0; i < 3; i++) {
    >    // 匿名函数
    >    (function (para) {
    >        setTimeout(function () {
    >            console.log(para);  // => 0 => 1 => 2（结果是传入进匿名函数的参数）
    >        }, 0);
    >    }(i));
    >}
    >```
    ></details>
3. 可以添加函数名：`(function 内部名字 () { console.log(内部名字); 错误 }())`

    1. 用于在执行栈中标记匿名函数的函数名
    2. 可以在匿名函数内部引用匿名函数本身

- 前端模块化的实现方案之一

### Tips
1. `var a = b = c = 1;/* b、c没有var的声明。等价于：var a = 1; b = 1; c = 1; */`

    第二个以后的变量表示没有~~var~~的赋值。
2. `var a = a || {};`执行顺序：

    <details>
    <summary>等价于：</summary>

    ```js
    /* 不是传参情况 */
    var a;

    if (a === 0 || a === "" || a === false || a === null || a === undefined) {
        a = {};
    }


    /* 传参情况 */
    function func(b) {
        if (b === 0 || b === "" || b === false || b === null || b === undefined) {
            b = {};
        }
    }
    ```
    </details>

    1. 声明提前`var a;`。
    2. 右侧的表达式`a || {}`先执行：根据规则先判断a的值是否为真，若a为真，则返回a；若a不为真，则返回{}。
    3. 最后再将结果赋值给`a`。

    ><details>
    ><summary><code>var a = b || {};</code>与<code>if (c) {}</code>会因为b或c没有定义而报错<code>ReferenceError: b is not defined</code>，可以用<code>typeof</code>来使代码健壮</summary>
    >
    >1. `var a = typeof b !== 'undefined' && b !== null ? b : {};`
    >2. `if (typeof c !== 'undefined' && c !== null) {}`
    ></details>
3. `if`、`while`之类的判断语句中用赋值操作：

    （大部分是误用）赋值的内容Boolean后为假会导致条件判断为假：`if(a = false){/* 不执行 */}`。

    >判断语句内只判断整体返回值是`true`还是`false`，与里面执行内容无关（尽管对其语法有所限制）。
4. 逗号操作符`,`对每个操作对象求值（从左至右），然后返回最后一个操作对象的值。

    1. `(0, obj.func)()`相当于`0; var tmp = obj.func; tmp();`

        ```js
        const obj = {
          func () {
            console.log(this)
          }
        }

        obj.func();     // obj
        (0, obj.func)() // window
        // 返回最后一个操作对象的值，返回一个方法
        ```
    2. `if(var a = 1, b = 2, c = 3, false){/* 不执行 */}`（已语法报错）：

        >`var/let/const`语句中的逗号不是逗号操作符，因为它不存在于一个表达式中。尽管从实际效果来看，那个逗号同逗号运算符的表现很相似。但它是`var/let/const`语句中的一个特殊符号，用于把多个变量声明结合成一个。
    3. `var a = [10, 20, 30, 40][1, 2, 3]; // 40`：

        1. `[10, 20, 30, 40]`被解析为数组；
        2. `[1, 2, 3]`被解析为属性调用，逗号操作符取最后一个值为结果。

        因此结果为数组`[10, 20, 30, 40]`的`[3]`属性值：`40`。
5. `{a: 'b'} + 1; // 1`：

    大括号视为代码块，没有返回值。需要给大括号加上小括号，表明为一个值：`({a: 'b'}) + 1; // [object Object]1`。
6. 判断DOM是否支持某属性：

    若要判定一个属性是否被DOM所支持，新建一个DOM来判断：`if('属性' in document.createElement('某标签')){...}`。

    >在DOM中随意添加一个属性，`此属性 in 此DOM`永远为真，不可以判断是否此DOM存在此属性（或方法）。
7. `eval`（尽量不用`eval`）

    1. `eval`直接执行`function`声明无效，必须用引号把`function`声明包裹起来才有效：

        >`eval`的参数是字符串。

        ```js
        eval(function a() {});   // function a() {}（但没有声明）
        eval('function b() {}'); // undefined（声明成功）
        ```

        >1. `if()`中的代码对于`function`的声明就是用`eval`带入方法做参数，因此虽然返回true，但方法没有被声明。
        >2. `setTimeout`与`setInterval`中第一个参数若使用字符串，也是使用`eval`把字符串转化为代码。
    2. `eval`中的`var`和`函数声明`，会在当前作用域创建变量和方法（非严格模式下）；`eval`中的`let`、`const`（、严格模式下的`var`）不会在当前作用域创建变量（`eval`使用完，下一行JS代码就无法获取里面的变量）

        >[MDN：eval](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval#direct_and_indirect_eval)
8. 获取数组中最大最小值：

    1. `Math.min(...[1, 2, 3])`或`Math.min.apply(null, [1, 2, 3])`
    2. `Math.max(...[1, 2, 3])`或`Math.max.apply(null, [1, 2, 3])`
9. 获取CSS的样式：

    1. `dom.style`：仅`style`内嵌样式。
    2. `window.getComputedStyle(dom[, 伪元素字符串])`：所有样式计算后的最终值。

        >`window.getComputedStyle(dom[, 伪元素字符串])`获取的是只读对象，不允许任何方式设置（包括 ~~`setProperty`~~）。
10. 设置CSS的`style`内嵌样式：

    1. `cssText`（ie8-返回时不包含最后一个`;`）：

        1. 添加：`dom.style.cssText += '; 样式: 属性; 样式: 属性'`
        2. 替换：`dom.style.cssText = '样式: 属性; 样式: 属性'`

        >若赋值错误，则去除无效样式、保留有效的赋值内容。若有相同CSS属性名，则后面的覆盖前面。
    2. 添加某个`style`内嵌样式属性：`dom.style.某属性名 = '值'`或`dom.style.setProperty('某属性名','值')`。
    3. 删除某个`style`内嵌样式属性：`dom.style.某属性名 = ''`或`dom.style.setProperty('某属性名','')`或`dom.style.removeProperty('某属性名')`。

    >若赋值错误，则保持赋值前的值。
11. 文档或一个子资源正在被卸载（关闭、刷新）时先触发`beforeunload`、再触发`unload`：

    >关闭前异步发送数据：`navigator.sendBeacon(地址, 数据)`（`XMLHttpRequest`：异步会被忽略、同步影响体验）。

    1. `beforeunload`(可取消默认行为)

        1. PC：若事件处理程序返回为`真`，则试图弹出对话框让用户选择是否继续操作。
        2. Android：可以执行事件函数但不会弹出对话框。
        3. iOS：无效。

        ```js
        window.onbeforeunload = function (e) {
          // do sth.

          var msg = needConfirm ? '信息' : '';

          (e || window.event).returnValue = msg;

          return msg;
        };
        ```
    2. `unload`

        1. 所有资源仍存在（图片、iframe等）
        2. 对于终端用户所有资源均不可见
        3. 界面交互无效（`window.open`、`alert`、`confirm`等）
        4. 错误不会停止卸载文档的过程
12. 页面的id值会动态地成为`window`的属性（全局变量），值为这个id所在的Element，除非`window`已存在这个属性名。

    ><details>
    ><summary>e.g.</summary>
    >
    >```html
    ><div id="j-dom"></div>
    >
    ><script>
    >  document.getElementById('j-dom') === window['j-dom']  // 当window原本没有j-dom属性时成立
    ></script>
    >```
    ></details>
13. （非打开新窗口的、非`history.pushState/replaceState`改变路由的）页面后退

    `if (document.referrer !== '') { history.back() } else { /* 后退到底的其他行为 */ }`

    >1. 若是新打开的窗口（`target="_blank"`），则会出现`document.referrer`有值，但`history.back()`已后退到底。
    >2. 若是`history.pushState/replaceState`改变路由，则不改变`document.referrer`（可能初始`document.referrer === ''`）。
    >3. 重新请求当前页面链接（如：`location.reload()`、或点击`<a href="当前页面链接">`），会导致`document.referrer === '当前页面链接'`。
14. 使用`encodeURIComponent/decodeURIComponent`仅处理URI中的query属性名和属性值；使用`encodeURI/decodeURI`处理整个URI；不要使用 ~~`escape/unescape`~~（已废弃）

    1. `encodeURIComponent`

        转义除了以下字符之外的所有字符：`字母` `数字` `(` `)` `.` `!` `~` `*` `'` `-` `_`
    2. `encodeURI`

        转义除了以下字符之外的所有字符：`字母` `数字` `(` `)` `.` `!` `~` `*` `'` `-` `_` `;` `,` `/` `?` `:` `@` `&` `=` `+` `$` `#`
15. 当一个`<script>`被执行时，在它之前的标签可以访问，但在它之后的标签无法访问（还不存在、未被解析到）

    ```html
    <!-- document、document.documentElement、document.head 出现 -->
    <html>
      <head></head>
      <body> <!-- document.body出现 -->
        某id的DOM <!-- 某id的DOM出现 -->
      </body>
    </html>
    ```
16. 判断浏览器标签是否在激活状态

    1. `document.hidden`：当前文档是否被隐藏
    2. `document.visibilityState`：当前文档的可见情况（`'visible'`、`'hidden'`、`'prerender'`、`'unloaded'`）
    3. `document`的`visibilitychange`事件：当前文档切换**隐藏/显示**时触发

        >`window`的`focus/blur`事件：当前文档**获得焦点/失去焦点**时触发（并不意味着被浏览器标签是否被隐藏）
    4. `document.hasFocus()`：当前文档是否获得焦点
17. 处理多次引入同个全局对象的冲突

    >参考：[jQuery的防冲突（noConflict）](https://github.com/jquery/jquery/blob/master/src/exports/global.js#L7-L25)。

    1. 先备份全局对象到局部变量；
    2. 再需要时把备份对象赋值回给全局。

    <details>
    <summary>e.g.</summary>

    ```js
    (() => {
      // ①备份原先全局对象到局部变量，用于将来noConflict时覆盖
      var backups = window.myGlobalVariable

      var _myGlobalVariable = {} // 主要功能

      // ②防冲突方法
      // 全局对象回退至上一个版本（若上一个版本未定义，则回退至undefined）
      // 该方法返回当前版本
      _myGlobalVariable.noConflict = function () {
        if (window.myGlobalVariable === _myGlobalVariable) { // 若 全局对象 === 本地变量，则 回退原来的全局对象
          window.myGlobalVariable = backups
        }

        return _myGlobalVariable
      }

      // 定义完对象后写入全局对象
      window.myGlobalVariable = _myGlobalVariable
    })()


    /* 使用测试 */
    // 假设引入2次上面的.js文件（可以是不同版本或相同版本）

    console.log(window.myGlobalVariable)            // 第二次引入的对象

    var a = window.myGlobalVariable.noConflict()
    console.log(a)                                  // 第二次引入的对象
    console.log(window.myGlobalVariable)            // 第一次引入的对象

    var b = window.myGlobalVariable.noConflict()
    console.log(b)                                  // 第一次引入的对象
    console.log(window.myGlobalVariable)            // undefined

    console.log(a)                                  // 第二次引入的对象
    ```
    </details>
18. 对异步加载的功能，可以用`push`的方式处理异步加载问题

    ```html
    <script src="a.js" async></script><!-- 可以在任意地方异步插入 -->

    <script>
    window.a = window.a || []   // 要在插入数据之前执行

    window.a.push({ i: 1 }) // 插入数据1
    window.a.push({ ii: 2 }) // 插入数据2
    </script>
    ```

    ```js
    // a.js
    (() => {
      // 主要功能
      const _a = {
        push (val) {  // 添加要处理的数据：_a.push(数据)
          console.log(val)
        }
      }

      if (window.a instanceof Array) {  // 若是数组，则说明加载.js之前插入了数据，直接处理
        for (let i = 0; i < window.a.length; i++) {
          _a.push(window.a[i])
        }
      }

      // 全局变量赋值
      window.a = _a
    })()
    ```
19. 兼容特殊浏览器、PC与WAP加载不同资源的方案

    1. 不同页面URL入口。
    2. 引入资源前，根据UA判断是否加载特殊资源。

        >1. 引入资源：[同步/异步加载资源](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/JS方法积累/实用方法/README.md#原生js动态添加脚本样式)
        >2. UA判断：[判断所在系统](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/JS方法积累/实用方法/README.md#原生js判断所在系统)、[判断移动平台](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/JS方法积累/实用方法/README.md#原生js判断移动平台)、[判断ie所有版本](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/JS方法积累/实用方法/README.md#原生js判断ie所有版本)
    3. 把特殊资源打包进总体代码，再根据UA判断引入。
    4. 服务端根据HTTP请求的UA判断输出不同页面加载不同资源（BFF层）。
20. 前端无法获取~~电脑文件系统中文件的绝对路径~~

    `<input type="file">`只能获得`C:\fakepath\文件名.文件类型`。

    >`<input>`输出的已加载文件的类型由文件名后缀决定，不会去解析文件而获得真实文件类型；`<input type="file" accept="image/png" />`也只会限制文件名后缀。
21. `dom1.contains(dom2)`判断dom2是否为dom1的后代节点（若`dom1 === dom2`，则返回`true`）。
22. 分享图最好用没有透明度的图，大部分app会在图片后面加上占位颜色

    同一个APP的Android、iOS效果可能不一致，不同APP实现效果更可能不一致。
23. 获取页面内静态资源数量：

    1. [`performance.getEntriesByType("resource")`](https://developer.mozilla.org/en-US/docs/Web/API/Performance/getEntriesByType)获得所有静态资源的`PerformanceResourceTiming`实例

        - 根据每个`PerformanceResourceTiming`实例若干属性判断加载成功/加载失败。
    2. `document.querySelectorAll`请求`<link>`、`<script>`、`<img>`等标签，查看资源DOM数量

        - 若资源的`load`/`error`事件触发则加载完成/加载失败。

    - DevTools的Network面板

---
## 事件相关

>1. 事件：用户或浏览器执行某种动作，如：`click`、`load`。
>2. 事件处理程序（事件处理函数、事件监听器）：当某个事件触发之后响应的函数。
>3. 事件对象：触发DOM事件产生的对象，包含与事件有关的所有信息。

### 事件绑定

><details>
><summary>约定</summary>
>
>1. 以点击事件`click`为例。
>2. `funcAttr`、`func0`、`funcIe`、`func2`为已经定义的方法。
></details>

1. 原生JS

    >参考：[JavaScript 事件绑定机制](http://www.cnblog.me/2016/05/08/javascript-event-binding/)、[理解Javascript中的事件绑定与事件委托](https://segmentfault.com/a/1190000006667581)。

    1. HTML事件处理程序（冒泡）

        `<div onclick="funcAttr()"></div>`（不能同个事件监听多个处理程序）

        <details>
        <summary>移除或修改绑定事件</summary>

        1. 事件处理程序设置为空方法或修改方法：

            `funcAttr = function () {};`、`funcAttr = function () {/* 修改方法 */};`
        2. 移除或修改DOM元素的事件绑定属性：

            `dom.removeAttribute('onclick');`、`dom.setAttribute('onclick', '(function () {/* 修改方法 */} ())');`
        </details>

    >本质上，DOM0级事件处理程序等于HTML事件处理程序。因此可以互相覆盖、移除绑定的事件处理程序。

    2. DOM0级事件处理程序（冒泡）

        `dom.onclick = func0;`（不能同个事件监听多个处理程序）

        <details>
        <summary>移除或修改绑定事件</summary>

        `dom.onclick = null;`、`dom.onclick = function () {/* 修改方法 */};`
        </details>
    3. IE事件处理程序（冒泡）

        `dom.attachEvent('onclick', funcIe);`（可监听多个，按绑定顺序的逆序触发；需参数完全对应才能解绑定；无法解绑匿名函数）

        <details>
        <summary>移除绑定事件</summary>

        `dom.detachEvent('onclick', funcIe);`
        </details>
    4. DOM2级事件处理程序（冒泡、捕获）

        >ie8-不兼容。

        `dom.addEventListener('click', func2, false);`（可监听多个，按绑定顺序触发，需参数完全对应才能解绑定；无法解绑匿名函数）

        <details>
        <summary>移除绑定事件</summary>

        `dom.removeEventListener('click', func2, false);`
        </details>

    - [兼容各浏览器的绑定、解绑事件](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/JS方法积累/实用方法/README.md#原生js绑定解绑事件)
2. jQuery（冒泡）

    >来自：[jQuery:Events](http://api.jquery.com/category/events/)。

    1. `on`（`one`类似）

        >jQuery的事件系统需要DOM元素能够通过元素的属性附加数据，使事件可以被跟踪和传递。因为`<object>`、`<embed>`、`<applet>`不能绑定数据，所以它们不能进行jQuery的事件绑定。

        <details>
        <summary>移除绑定事件</summary>

        `off`
        </details>
    2. <details>

        <summary>其他</summary>

        1. 一系列`on`的事件绑定快捷方法:

            `click`、`dblclick`、`contextmenu`、`keydown`、`keyup`、`keypress`、`mousedown`、`mouseup`、`mousemove`、`mouseenter`、`mouseleave`、`mouseover`、`mouseout`、`hover`、`blur`、`focus`、`focusin`、`focusout`、`select`、`change`、`submit`、`ready`、`resize`、`scroll`
        2. 由`on`或`off`实现的：（废除或不推荐）

            1. 绑定：~~`bind`~~、~~`live`~~、~~`delegate`~~
            2. 解绑：~~`unbind`~~、~~`die`~~、~~`undelegate`~~
        </details>

- 移除绑定：

    `绑定事件接口`将回调函数压入该事件的回调函数队列，当事件发生时，回调函数队列会被遍历，其中的函数会被逐个执行。`解除绑定事件接口`将回调函数从该事件的回调函数队列中移除，当事件发生时，队列中没有该函数，于是该函数便不会执行。

    1. HTML事件处理程序、DOM0级事件处理程序，用赋值覆盖解绑。
    2. `attachEvent/detachEvent`，必须一一对应具体的**handle**进行解绑。**handle**是匿名函数无法解绑。

        ><details>
        ><summary>ie的<strong>handle</strong>中<code>this</code>指向<code>window</code>的兼容方式</summary>
        >
        >1. 处理**handle**（传入方法不改变）
        >
        >    `function () {funcIe.apply(dom, arguments);}`（无法解绑）。
        >2. 修改`funcIe`
        >
        >    1. `funcIe.bind(dom)`（需要`bind`的[polyfill](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/JS方法积累/废弃代码/README.md#原生jsfunctionprototypebind的polyfill)）。
        >    2. 使用`window.event`定义~~this~~
        >
        >        ```js
        >        function funcIe(e) {
        >            e = e || window.event;                 // 事件对象
        >            var _this = e.srcElement || e.target;  // 触发的DOM
        >
        >            /* funcIe代码 */
        >        }
        >        ```
        ></details>
    3. `addEventListener/removeEventListener`，必须一一对应具体的**handle**、**布尔值**进行解绑。**handle**是匿名函数无法解绑。
    4. jQuery的`on/off`（以及其他绑定解绑方法）：

        1. 写具体**handle**时解绑具体**handle**。
        2. 不写**handle**时解绑对象下某事件的所有方法。
        3. 还可以对事件添加**namespace**。
        4. 若要移除元素上所有的代理事件，而不移除任何非代理事件，使用特殊值`'**'`。

            e.g. `$dom.off('click', '**');   // 解绑$dom代理到子节点的click事件，但不解绑$dom自己的click事件`
- JS的自定义事件

    1. 原生JS：

        >来自：[MDN：CustomEvent](https://developer.mozilla.org/zh-CN/docs/Web/API/CustomEvent/CustomEvent)。

        ```js
        // 监听自定义事件
        dom.addEventListener('事件名', function (e) {...}, false) // e.bubbles/cancelable/composed/detail

        // 创建自定义事件
        var event = new CustomEvent('事件名'[, 参数对象]) // 参数对象：bubbles、cancelable、composed、detail（自定义数据）

        // 触发
        dom.dispatchEvent(event)
        ```

        ><details>
        ><summary>或<code>Event</code></summary>
        >
        >来自：[MDN：Event](https://developer.mozilla.org/zh-CN/docs/Web/API/Event/Event)。
        >
        >```js
        >// 监听自定义事件
        >dom.addEventListener('事件名', function (e) {...}, false) // e.bubbles/cancelable/composed
        >
        >// 创建自定义事件
        >var event = new Event('事件名'[, 参数对象])    // 参数对象：bubbles、cancelable、composed。无法传递自定义数据
        >
        >// 触发
        >dom.dispatchEvent(event)
        >```
        ></details>
    2. `jQuery`：

        ```js
        $('选择器').on('自定义事件', function () {})
        $('选择器').trigger('自定义事件')
        ```

### 事件流（event flow）
1. 类型：

    1. 捕获（capture）：

        从外层元素到目标元素的过程，
    2. 冒泡（bubbling）：

        >事件都有`bubbles`属性，判断是否冒泡。W3定义的[DOM-Level-3-Events](https://www.w3.org/TR/DOM-Level-3-Events/)可查冒泡情况：；[media相关事件](https://html.spec.whatwg.org/multipage/media.html#mediaevents)均不冒泡。

        从目标元素到外层元素的过程。
2. DOM标准事件流触发顺序：

    ![事件流图](./images/event-flow-1.png)

    1. 先按**捕获**顺序依次执行节点注册**捕获**的事件。
    2. 处于目标

        1. 依据注册顺序执行事件处理程序，分为捕获、冒泡两种抵达类型。浏览器默认行为：冒泡抵达类型（在捕获、冒泡的事件处理程序执行之后才执行默认行为）。
        2. 可设置不再冒泡（、不再捕获） 或 不执行浏览器默认行为。
        3. 建议仅在**需要在事件到达目标之前截获它的情况**才设置捕获的事件处理程序。

        >DOM2规范要求：实际的目标不接收~~捕获~~事件，仅接收冒泡事件。但浏览器的实现却都让实际目标接收捕获和冒泡事件。
    3. 再按**冒泡**顺序依次执行节点注册**冒泡**的事件。

    >ie10-的DOM事件流只有冒泡，没有~~捕获~~。

### WAP端相关
1. WAP端点透bug

    >1. PC端没有 ~~`touch`~~ 事件。
    >2. WAP端有`touchstart`、`touchmove`、`touchend`、`touchcancel`等`touch`事件。
    >3. Zepto用`touch`一系列事件封装成`tap`事件。

    1. 点透现象：

        使用Zepto的`tap`事件绑定（或原生JS的`touchstart`绑定）后，若此元素在触摸事件发生后离开原始位置（CSS或JS），同一位置正好有一个DOM元素绑定了`click`事件或`<a>`，则会出现「点透」bug（触发底下元素的`click`事件）。
    2. 原因

        >历史原因：WAP端增加快速双击缩放和恢复功能。由于当用户一次点击屏幕之后，浏览器并不能立刻判断用户是单击还是双击操作。因此，就等待300ms左右，以判断用户是否再次点击了屏幕。

        WAP端触摸事件顺序：`touchstart` -> `touchmove` -> `touchend` -> `click`，触摸一瞬间触发`touchstart`，触摸结束后触发Zepto封装的`tap`事件，触摸结束后300ms左右触发`click`事件。
    3. 解决方法：

        1. 使用[fastclick.js](https://github.com/ftlabs/fastclick)消除`click`的延时（最佳方式）

            用`click`代替全部`tap`事件，这样PC端和WAP端都可以一致用`click`事件且不会出现WAP端点透bug。

            >fastclick.js原理：在检测到`touchend`事件时，通过DOM自定义事件立即触发一个模拟`click`事件，并阻止浏览器在300ms之后真正触发的`click`事件。
        2. 禁用缩放，设置`<meta name="viewport" content="initial-scale=1.0, user-scalable=no, minimum-scale=1.0, maximum-scale=1.0">`。
        3. 布局viewport小于等于可视viewport则浏览器禁用双击缩放，设置`<meta name="viewport" content="width=device-width, initial-scale=1.0">`。
        4. CSS属性`touch-action: manipulation;`仅允许在元素上进行触屏操作的平移、缩放，忽略~~双击~~。
        5. 使用缓动动画，过度300ms延迟。
        6. 中间增加一层接受这个点透事件，然后去除此层。
        7. [模拟点击事件](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/JS方法积累/实用方法/README.md#原生js触摸屏模拟点击事件消除延时300毫秒后才触发click事件使点击事件提前触发)代替`click`。
2. WAP端使用`:active`

    1. Android系统的浏览器大部分直接使用CSS伪类即可。
    2. iOS系统的浏览器要添加：`document.body.addEventListener('touchstart', function () {}, true);`。
    3. <details>

        <summary><del>JS添加类的方法模拟</del></summary>

        ```html
        <style>
            .d:active,
            .d.active { }
        </style>

        <script type="text/javascript">
            var selector = '.a,.b .c,.d';   /* 选择器字符串 */

            $(document.body).on('touchstart', selector, function () {
                $(this).addClass('active');
            }).on('touchmove touchend touchcancel', selector, function () {
                $(this).removeClass('active');
            });
        </script>
        ```
        </details>

    - 添加`document.body.addEventListener('touchstart', function () {}, true);`即可满足大部分浏览器使用伪类。
3. WAP端播放

    >大部分`<video>`、`<audio>`同理。

    1. 播放事件

        >参考：[MDN：媒体相关事件](https://developer.mozilla.org/zh-CN/docs/Web/Guide/Events/Media_events)。

        1. 正在播放

            `timeupdate`事件：当`媒体.currentTime`改变（拉动进度或播放中）。

            >iOS手动设置`currentTime`值之后，当播放时，可能会回溯一段时间开始播放。
            >
            >e.g. `dom.currentTime = 10 // currentTime先被设置为10；若开始播放，则倒退至9.n开始播放`
        2. 开始播放

            1. `play`事件：初次播放、暂停后恢复。
            2. `playing`事件：初次播放、暂停后恢复、结束后自动开始（`loop`属性模式）。
        3. 暂停播放

            `pause`事件
        4. 完成一轮播放

            >因为`loop`属性模式无法触发`ended`事件，又`timeupdate`事件触发时间不确定、无法和`媒体.duration`取等判断成功，故无法在`loop`属性模式中判定。

            （非`loop`属性模式下的）`ended`事件（伴随`pause`事件）。

        - 建议只用`timeupdate`、`ended`、`pause`事件处理需求。

        >各机型/浏览器对视频事件、API的处理不同，甚至某些Android机型会要求：只有触发在视频区域内的事件才可执行视频的API。
    2. 自动播放

        1. JS代码模拟

            ```html
            <video id="j-video">
              您的浏览器不支持 video 标签
            </video>

            <script>
              var video = document.getElementById('j-video')

              document.addEventListener('DOMContentLoaded', function () {
                video.setAttribute('src', '视频地址')   // 代替preload="none"
                video.play()
              }, false)

              // 根据需求选用
              window.ontouchstart = function () {
                video.play()
                window.ontouchstart = null
              }
            </script>
            ```
        2. ~~`autoplay`~~ 属性模式

            >兼容性差。
    3. 循环播放

        1. JS代码模拟

            `ended`事件中触发`媒体.play()`。
        2. `loop`属性模式
    4. 内嵌播放

        >因为全屏播放完`<video>`会白屏，故可以在父级添加封面图片背景。

        ```html
        <video id="j-video"
               webkit-playsinline
               playsinline
               x5-video-player-type="h5">
          您的浏览器不支持 video 标签
        </video>

        <script>
          var video = document.getElementById('j-video')

          // QQ浏览器去除 x5-video-player-type 属性
          if (/QQBrowser/.test(window.navigator.userAgent)) {
            video.removeAttribute('x5-video-player-type')
          }
        </script>
        ```
    5. 播放控件（内嵌播放）

        1. `controls`属性模式
        2. <details>

            <summary><del>JS代码模拟</del></summary>

            >兼容性差。

            ```html
            <style>
              .video-wrap {
                position: relative;
                width: 320px;
                height: 500px;
                background: red;
              }
              .video-wrap video {
                max-width: 100%;
                max-height: 100%;
              }
              .icon {
                position: absolute;
                top: 0;
                width: 100%;
                height: 50%;
                background: yellow;
              }
            </style>

            <div id="j-video-wrap" class="video-wrap">
              <video id="j-video"
                     webkit-playsinline
                     playsinline
                     x5-video-player-type="h5"
                     style="width: 1px;height: 1px;">
                您的浏览器不支持 video 标签
              </video>

              <div id="j-start-icon" class="icon">
                封面图（初始点击）
              </div>
              <div id="j-play-icon" class="icon" style="pointer-events: none;display: none;">
                播放按钮
              </div>
            </div>

            <script>
             var video = document.getElementById('j-video')
             var start = document.getElementById('j-start-icon')
             var play = document.getElementById('j-play-icon')

             if (/QQBrowser/.test(window.navigator.userAgent)) { // QQ浏览器去除 x5-video-player-type 属性
               video.removeAttribute('x5-video-player-type')
             }

             function touchstartFunc () {
               start.style.display = 'none'
               video.setAttribute('src', '视频地址')    // 代替preload="none"
               video.removeAttribute('style')
               video.play()

               setTimeout(function () {
                 /* 点击播放 */
                 document.getElementById('j-video-wrap').addEventListener('touchstart', function () {
                   if (video.paused) { // 播放
                     video.play()
                     play.style.display = 'none'
                   } else {  // 暂停
                     video.pause()
                     play.style.display = 'block'
                   }
                 }, false)

                 /* 视频播放结束 */
                 video.addEventListener('ended', function () {
                   // video.play()
                   play.style.display = 'block'
                 }, false)

                 start.removeEventListener('touchstart', touchstartFunc, false)
               }, 0)
             }

             start.addEventListener('touchstart', touchstartFunc, false)
            </script>
            ```
            >[CodePen demo](https://codepen.io/realgeoffrey/pen/mNOavr)
            </details>
    - 播放视频问题：

        1. 无法操作客户端自定义播放控件：

            1. 一般手机有两种播放方式：

                1. 全屏模式
                2. 内联模式（浏览器支持其中一种）：

                    1. `webkit-playsinline playsinline`内联模式。

                        >针对iOS的UC或QQ浏览器，可以添加[iphone-inline-video](https://github.com/bfred-it/iphone-inline-video)。
                    2. `x5-video-player-type="h5"`在底部的全屏内联模式（同层播放）。

                        >[Android的腾讯X5内核WebView](https://x5.tencent.com/tbs/guide/video.html)特有。
            2. 无法操作全屏模式

                1. 无法改变全屏播放方向以及控件内容

                    DOM属性`x5-video-orientation="landscape或portraint"`、`x5-video-player-fullscreen="true"`无法解决。
                2. 有些浏览器在全屏模式中，不触发任何video事件

                    >无法自定义loading。
            3. 关闭`controls`模式，部分浏览器依然出现播放按钮
            4. 无法控制内联模式类型（内联模式/在底部的全屏内联模式）
        2. Android机型播放了`<video>`，会把视频的层级放到最高，暂时没有直接解决方法。
        3. 打开全屏会触发window的`scroll`事件。

            此时的屏幕可能高宽发生切换，页面内的DOM位置信息可能没有变化（如：`getBoundingClientRect`还是在原界面的值，屏幕高宽却变了）。
        4. 播放（`.play()`）是异步行为。

---
## DOM操作
>以纵轴为例。

### 获取位置信息
1. DOM节点

    1. 节点高度：

        1. height+padding：

            `dom.clientHeight`

            >jQuery：`$dom.innerHeight()`
        2. height+padding+border：

            `dom.offsetHeight`（元素的像素高度，包含该元素的垂直内边距和边框，且是一个整数。理解为一个设置的高度）

            >jQuery：`$dom.outerHeight()`
    2. 节点内容高度：

        `dom.scrollHeight`（元素内容高度的度量，包括由于溢出导致的视图中不可见内容。）
    3. 节点内滚动距离：

        `dom.scrollTop`

        >jQuery：`$dom.scrollTop()`
    4. 节点顶部相对视口顶部距离：

        `dom.getBoundingClientRect().top`

        >jQuery：`$dom.offset().top + document.documentElement.clientTop - $(window).scrollTop()`

        >`document.documentElement.clientTop`：`<html>`的`border-top-width`数值。
    5. 节点顶部相对文档顶部距离（不包括~~文档的border~~）：

        `dom.getBoundingClientRect().top + (document.body.scrollTop || document.documentElement.scrollTop) - document.documentElement.clientTop`

        >jQuery：`$dom.offset().top`
2. 文档和视口

    1. 视口高度：

        `window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight`

        >jQuery：`$(window).height()`
    2. 文档内容高度：

        `document.body.scrollHeight`

        >jQuery：`$(document).height()`
    3. 文档滚动高度：

        `document.body.scrollTop || document.documentElement.scrollTop`

        >jQuery：`$(window).scrollTop()`

>1. 还可以使用[`IntersectionObserver`](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/前端内容/标准库文档.md#intersectionobserver)判断节点和视口（或祖先节点）相交程度。
>2. Zepto没有`innerHeight`和`outerHeight`，改为`height`。

### 节点与视口距离关系
1. `getBoundingClientRect`

    ><details>
    ><summary>视口高度</summary>
    >
    >`window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight`
    ></details>

    1. 节点**顶部**在**视口底部**以上

        `dom.getBoundingClientRect().top <= 视口高度`

        >jQuery：`$dom.offset().top <= $(window).scrollTop() + $(window).height()`
    2. 节点**底部**在**视口顶部**以下

        `dom.getBoundingClientRect().bottom >= 0`

        >jQuery：`$dom.offset().top + $dom.outerHeight() >= $(window).scrollTop()`
    3. 节点在视口内

        以上`&&`结合。

        <details>
        <summary>e.g.</summary>

        ```js
        function isInViewport(dom) {
          const viewPortHeight = window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight;
          const viewPortWidth = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;

          const rect = dom.getBoundingClientRect()
          const { top, bottom, left, right } = rect;

          // 只要在视口露一点头就返回true（可以按业务逻辑修改）
          return (
            top <= viewPortHeight &&
            bottom >= 0 &&
            left <= viewPortWidth &&
            right >= 0
          );
        }
        ```
        </details>
2. [`IntersectionObserver`](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/前端内容/标准库文档.md#intersectionobserver)判断节点和视口（或祖先节点）相交程度。

><details>
><summary>某dom跟随屏幕滚动而相对静止</summary>
>
>1. 判断：要处理的节点顶部相对视口顶部距离（`dom.getBoundingClientRect().top`）。
>
>    1. 若≤0，则处理dom（具体实现：[节点跟随屏幕滚动而相对静止](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/JS方法积累/实用方法/README.md#jquery节点跟随屏幕滚动而相对静止)）。
>    2. 若>0，则恢复dom的文档流。
>2. 从文档顶部到要处理的位置用`<div>`包裹，对这个额外包裹的`<div>`进行`IntersectionObserver`处理。
>
>    1. 若消失，则处理dom。
>    1. 若展示，则恢复dom的文档流。
></details>

### 节点是否在首屏
1. 距离文档顶部、左边距离

    ```js
    // 获取距离顶部距离（对fixed处理：当做是浏览器无滚动时的距离）
    function getToTop(dom) {
      let realTop = dom.offsetTop;
      let realLeft = dom.offsetLeft;
      let parent = dom.offsetParent;
      while (parent !== null) {
        realTop += parent.offsetTop;
        realLeft += parent.offsetLeft;
        parent = parent.offsetParent;
      }

      const domHeight = dom.offsetHeight;
      const domWidth = dom.offsetWidth;

      return {
        top: realTop,
        bottom: realTop + domHeight,
        left: realLeft,
        right: realLeft + domWidth,
      };
    }
    ```

    <details>
    <summary><code>getBoundingClientRect</code>实现</summary>

    >2种算法，会有一些对border数值取值的误差。

    ```js
    // 获取距离顶部距离（对fixed处理：加上浏览器滚动距离，就好像fixed内容跟随视口滚动、与视口距离相对不变化）
    function getToTop(dom) {
      const scrollTop = document.body.scrollTop || document.documentElement.scrollTop;
      const scrollLeft = document.body.scrollLeft || document.documentElement.scrollLeft;

      const rect = dom.getBoundingClientRect();
      const { top, bottom, left, right } = rect;

      return {
        top: scrollTop + top,
        bottom: scrollTop + bottom,
        left: scrollLeft + left,
        right: scrollLeft + right,
      };
    }
    ```
2. DOM节点是否在首屏内

    ```js
    function isFirstScreen(dom) {
      const viewPortHeight = window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight;
      const viewPortWidth = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;

      const { top, bottom, left, right } = getToTop(dom);

      // 只要在视口露一点头就返回true（可以按业务逻辑修改）
      return (
        top < viewPortHeight &&
        bottom > 0 &&
        left < viewPortWidth &&
        right > 0
      );
    }
    ```

### 判断滚动定位
>也可以给底部（或顶部）放置一个标记节点，当这个节点的顶部在容器底部以上（或这个节点的底部在容器顶部以下）时为滚动到底部（或顶部）。

1. DOM节点

    1. 内容滚动到底部：

        `dom.offsetHeight + dom.scrollTop >= dom.scrollHeight`
    2. 内容滚动到顶部：

        `dom.scrollTop === 0`
2. 文档

    ><details>
    ><summary>视口高度、文档滚动高度、文档内容高度</summary>
    >
    >1. 视口高度:
    >
    >    `window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight`
    >2. 文档滚动高度：
    >
    >    `document.body.scrollTop || document.documentElement.scrollTop`
    >3. 文档内容高度：
    >
    >    `document.body.scrollHeight`
    ></details>

    1. 滚动到底部：

        `视口高度 + 文档滚动高度 >= 文档内容高度`
    2. 滚动到顶部：

        `文档滚动高度 === 0`

### 进行文档滚动
1. 支持动画过渡效果（smooth）：

    1. 滚动到使DOM进入视口：[`dom.scrollIntoView()`](https://developer.mozilla.org/zh-CN/docs/Web/API/Element/scrollIntoView)
    2. `dom或window.scroll/scrollTo(横轴坐标, 纵轴坐标)` 或 `dom或window.scroll/scrollTo({ left: 横轴坐标, top: 纵轴坐标, behavior: 'smooth'或'auto' })`

        >`dom或window.scrollBy(相对横轴坐标, 相对纵轴坐标)` 或 `dom或window.scrollBy({ left: 相对横轴坐标, top: 相对纵轴坐标, behavior: 'smooth'或'auto' })`
2. 不支持过渡效果、会瞬间定位：

    1. `window.location.href = #锚点`
    2. `dom.scrollTop = 纵轴坐标`

        >`dom.scrollLeft = 横轴坐标`

        - 整个文档滚动：

            `document.body.scrollTop = document.documentElement.scrollTop = 纵轴坐标`

            >`document.body.scrollLeft = document.documentElement.scrollLeft = 横轴坐标`

- dom设置CSS样式`scroll-behavior: smooth;`会强制上面所有滚动效果在dom上都是动画过渡效果（smooth）。

### DOM相对位置
1. DOM点击事件的定位（原生JS）

    1. PC端`MouseEvent`

        `e.`（`e`为传入事件处理程序的第一个参数）或`window.event.`：

        1. `pageX/Y`（ie8-不支持）

            距离文档的左边缘/上边缘。
        2. `clientX/Y`

            距离浏览器窗口。
        3. `screenX/Y`

            距离屏幕。
        4. `offsetX/Y`

            距离目标元素自身填充边界。
        5. `movementX/Y`（ie、Safari不支持）

            （仅针对`mousemove`事件）相对于上一帧鼠标移动距离。
        6. `x/y`

            等价于：`clientX/Y`。
    2. WAP端`TouchEvent`

        `e.touches[0].`（`e`为传入事件处理程序的第一个参数）：

        1. `pageX/Y`
        2. `clientX/Y`
        3. `screenX/Y`
2. <details>

    <summary>相对偏移（jQuery）</summary>

    1. `$dom.offset()`

        返回：相对于文档的距离（可以设置）。
    2. `$dom.position()`

        返回：相对于**距离该元素最近（就近原则）的且被定位过的祖先元素**的距离。
    3. `$dom.offsetParent()`

        返回：相对于**距离该元素最近（就近原则）的且被定位过的祖先元素**的jQuery对象。
    4. `$dom.scrollLeft/Top()`

        返回：当前滚动条的位置（可以设置）。
    </details>

### DOM修改
1. 用HTML文本覆盖：

    `dom.innerHTML/outerHTML/innerText/textContent = HTML文本`
2. 用新的DOM插入或覆盖旧的DOM：

    >若要被添加的DOM（newDom）已存在于页面上，则会移动该DOM到目标容器元素下。

    1. 插入：

        `parentNode.append/prepend/appendChild(newDom)`、`parentNode.insertBefore(newDom, oldDom)`、`oldDom.before(newDom)`
    2. 替换：

        `oldDom.replaceWith(newDom)`、`parentNode.replaceChild(newDom, oldDom)`
3. 删除DOM：

    `parentNode.removeChild(oldDom)`、`oldDom.remove()`
4. 创建DOM：

    `document.createElement(标签名)`

### `Node`与`Element`

- Node根据`nodeType`属性区分节点类型：

    1. `1 === Node.ELEMENT_NODE`

        `Element`

        >`Element`继承了`Node`。
    2. `3 === Node.TEXT_NODE`

        `Element`的`文本`或`属性`
    3. `7 === Node.PROCESSING_INSTRUCTION_NODE`
    4. `8 === Node.COMMENT_NODE`

        注释
    5. `9 === Node.DOCUMENT_NODE`

        `document`
    6. `10 === Node.DOCUMENT_TYPE_NODE`

        文档类型节点，如：`<!DOCTYPE html>`
    7. `11 === Node.DOCUMENT_FRAGMENT_NODE`

        `DocumentFragment`
- [判断是否为`Node`、是否为`Element`](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/JS方法积累/实用方法/README.md#原生js判断是否为node是否为element)

### `attribute`与`property`
1. 在HTML标签里定义标签的`attributes`，一旦浏览器解析后，所有DOM节点会被创建成对象，每个DOM对象就拥有`properties`，因此：

    1. `attributes`：HTML标签的属性（打开浏览器检查能够看见标签上的属性）。

        >1. `.attributes`展示此DOM对象的所有`attribute`
        >2. `.getAttribute/setAttribute/removeAttribute/hasAttribute/toggleAttribute`操作`attribute`
    2. `properties`：DOM对象的属性。

    >浏览器的 前进/后退/重新打开关闭的标签页（~~刷新~~不行），会进行：重新下载HTML后进行常规的[解析HTML-加载资源-渲染](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/前端内容/README.md#页面解析渲染步骤)，但会尝试恢复之前页面的`properties`（包括页面滚动、每个DOM对象的`properties`、等）。仅针对文档对象模型（DOM构造），不包括`attributes`；仅针对新加载出来页面能匹配之前页面的部分，新增的DOM没有匹配。
2. 当一个DOM节点为某个HTML标签所创建时，其大多数`properties`与对应`attributes`拥有相同或相近的名字，但并非一对一的关系：

    >浏览器在加载页面之后会对页面中的标签进行解析，并生成与之相符的DOM对象，每个标签中都可能包含一些属性。若这些属性是[标准属性](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Attributes)，则解析生成的DOM对象中也会包含与之对应的属性。

    1. 某些`property`值等于`attribute`值，修改其中之一另一个也随之改变：

        1. 有几个`property`是直接反映`attribute`，如：`rel`、`id`
        2. 有一些用稍微不同的名字也是直接映射，如：`htmlFor`映射`for`，`className`映射`class`，`dataset`映射`data-`集合
    2. 很多`property`所映射的`attribute`是带有**限制**或**变动**

        1. `type`的值被限制在已知值（即`<input>`的合法类型，如：`text`、`checkbox`等）。
        2. `href/src`的`property`值会计算出最终完整路由，它的`attribute`只是HTML标签上显示的路径。
        3. 部分动态属性（如：`checked`、`selected`、`disabled`、`value`、`muted`等）遵循下面规则：

            1. 若没有设置`property`：页面展示跟随`attribute`，`property`值跟随`attribute`。
            2. 若设置过`property`：页面展示跟随`property`，`property`与`attribute`值不互通。
            - 操作页面展示，修改的是`property`，`attribute`不会随之变化。操作页面展示时，也就设置了`property`。

- 判断一个标签的动态属性（DOM对象的`property`）

    >以`<input>`的`checked`为例，类似的特性还有`selected`、`disabled`、`value`、`muted`等。

    ```html
    <input type="checkbox" checked="checked" id="j-input">

    <script>
      var $dom = $('#j-input');
      var dom = $dom.get(0);

      // ①
      // 共通的值，存储在jQuery内部
      // 获取：真实效果的值
      // 设置：可以改变页面上显示效果、不会改变HTML上属性的值
      dom.checked; // 设置 dom.checked = true/false
      $dom.prop('checked'); // 设置 $dom.prop('checked', true/false);

      // ②
      // 获取：HTML上属性的值
      // 设置：若没有使用①设置值，则可以控制①结果、可以改变页面上显示效果；
      //    若使用①设置过，则仅设置HTML上属性的值、不会真的改变显示效果
      $dom.attr('checked'); // 设置 $dom.attr('checked', true/false);

      // ③
      // 获取：HTML上属性的值
      // 设置：若没有使用①设置值，则可以仅把关闭设置为打开、无法把打开设置为关闭（removeAttribute可以关闭）；
      //    若使用①设置过，则仅设置HTML上属性的值、不会真的改变显示效果
      dom.getAttribute('checked'); // 设置 dom.setAttribute('checked', 值)；去除 dom.removeAttribute('checked')
    </script>
    ```

    - 若要判断、获取或设置，建议仅使用：

        1. 判断、获取：`dom.checked`，设置：`dom.checked = true/false`。
        2. 判断、获取：`$dom.prop('checked')`，设置：`$dom.prop('checked', true/false)`。
        3. 判断、获取：`$dom.is(':checked')`。

><details>
><summary>约定</summary>
>
>1. `dom`为JS对象，`$dom`为jQuery（或Zepto）对象。
>2. 大部分情况下，jQuery内容适用于Zepto。
></details>

### jQuery相关
1. 当变量是jQuery对象时，可用`$`作为开头命名，利于与普通变量区分

    ```js
    // e.g.
    var num = 1;
    var dom = $('div').get();
    var $dom = $('div');
    ```
2. 选择器
    1. `$('子','父') === $('父').find('子')`

        找到所有父级，若子级在此父级后面，则选择。
    2. ~~`$('父 子')`~~（效率低）

        找到所有子级，然后向前找出有父级的，则选择（与CSS相同的查询方式）。
3. 判断选择器选择到空内容

    选择器选取的内容返回数组（空内容返回`[]`），所以`if($(...)) {}`永远成立。因此用以下方法：

    1. `if($(...).length > 0) {}    // 若无则为0`
    2. `if($(...)[0]) {}    // 若无则为undefined`
4. `on`绑定效率（事件代理、事件委托）

    >1. 事件代理：把原本需要绑定的事件委托给祖先元素，让祖先元素担当事件监听的职务。
    >
    >    1. 原理：DOM元素的事件冒泡。
    >    2. 好处：提高性能，避免~~批量绑定~~。
    >2. `paste`、`reset`不支持事件代理，仅能够直接绑定；事件代理不能用于SVG。

    >e.g. `$(eventHandler).on(event, selector, func);`

    1. 确定绑定内容：

        1. 执行`on`方法的时刻，把所有满足条件的DOM对象安装指定的应用逻辑**func**，成为**eventHandler**；
        2. 有且仅有这些eventHandler绑定成功；之后动态生成的且满足条件的DOM不再安装；对已生效的eventHandler操作DOM（如：增删类名）不会使绑定内容失效（除非删除DOM或解绑事件）；
        3. 在eventHandler内动态增删的**selector**都可以由条件判定是否生效绑定内容（因为事件是绑定在eventHandler上，而不是selector上）。
    2. 绑定的eventHandler距离selector越近，效率越高。因此虽然把selector都绑定在`$(document)`上能够避免增删节点对事件绑定造成的影响，但效率会下降。

        >每次触发事件，jQuery会比较从目标元素（`target`）到eventHandler路径中每一个元素上所有该类型的事件（冒泡）。
5. 判断是否加载成功，不成功则加载其他文件地址

    ```html
    <script>
        window.jQuery || document.write('<script src="其他文件地址"><\/script>');
    </script>
    ```
6. `$dom.focus()`

    1. 直接调用，光标停留在文本开头或上一次光标停留的地方（Windows和macOS或不同浏览器效果不同）。
    2. 先清空文本再`focus`然后再添加文本，光标停留在文本结尾。

    [CodePen demo](https://codepen.io/realgeoffrey/pen/pMNqqV)
7. `$dom.data()`仅在第一次使用后（获取或设置）获取HTML上的值或设置到jQuery内部（不会改变HTML上属性的值），之后不再因为HTML改变而改变，也无法修改HTML上属性的值。

    `$dom.removeData()`删除绑定的数据后，再使用`$dom.data()`则重新获取HTML上的值或设置到jQuery内部。

    >因为`<object>`、`<embed>`、`<applet>`不能绑定数据，所以它们不能使用`.data()`。
8. jQuery操作CSS样式：

    1. 设置大部分CSS样式时，不写单位默认：`px`；对于`px`单位的样式可以设置相对值`'+=数字'`或`'-=数字'`：

        `.css()`、`.width()`、`.height()`、`.animate()`。

        >`jQuery.cssNumber`保存着没有默认单位的属性名，可设置为`false`尝试添加默认单位。
    2. 获得样式时，都是换算成`px`（若可以换算）。

        >1. `.height/innerHeight/outerHeight()`返回`数字`。
        >2. `.css('height')`返回带`px`的`字符串`。
9. `$.proxy()`和原生JS的`Function.prototype.bind`类似，返回一个确定了`this`（和参数）的新方法

    >新方法的参数填补在原函数去除已设置参数的后面（与`Function.prototype.bind`一致）。

    - 额外的，jQuery确保即使绑定的函数经过`$.proxy()`处理，依然可以用原先的函数来正确地取消绑定

        <details>
        <summary>e.g.</summary>

        ```js
        var obj = {
          test: function () {
            console.log(this);
            $('#test').off('click', obj.test);  // 可以解绑$.proxy(obj, 'test')
          }
        };

        $('#test').on('click', $.proxy(obj, 'test'));
        ```
        </details>
