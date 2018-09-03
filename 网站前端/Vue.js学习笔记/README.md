# Vue.js学习笔记

## 目录
1. [vue](#vue)

    1. [模板插值](#模板插值)
    1. [指令 && 特殊attribute](#指令--特殊attribute)
    1. [Vue实例的属性](#vue实例的属性)
    1. [组件](#组件)
    1. [单文件组件](#单文件组件)
    1. [过渡/动画](#过渡动画)
    1. [插件](#插件)
    1. [特性](#特性)
    1. [虚拟DOM](#虚拟dom)
    1. [双向绑定](#双向绑定)
1. [vue-router](#vue-router)
1. [vuex](#vuex)
1. [vue-cli](#vue-cli)
1. [nuxt.js](#nuxtjs)
1. [jQuery与Vue.js对比](#jquery与vuejs对比)

---
## [vue](https://github.com/vuejs/vue)
- 心得

    1. 针对不在vue视图内出现的变量：

        >组件的多个实例会共用模块内、组件外的变量（闭包），组件内部的数据则互相独立（类似于`new`实例）。

        1. 若是常量，则可以放在组件外，用`const` + 大写和下划线组成。
        2. 若是会变化的量，则必须放在组件内（`data`或`computed`）。
    2. 注意内存泄漏：

        1. 在Vue实例内部`new`的其他实例或DOM，应放在`data`内进行掌控，当使用完毕后引导垃圾回收。
        2. 在Vue实例内部手动绑定的事件（`addEventListener`）、计时器、http连接、以及任何需要手动关闭的内容，需要在`beforeDestroy`前手动清除（`destroyed`仅自动清除Vue自己定义、绑定的内容）。

### 模板插值
1. 支持JS表达式（单个），不支持~~语句~~、~~流控制~~。

    <details>
    <summary>e.g.</summary>

    ```html
    <!-- 可行 -->
    {{ number + 1 }}
    {{ ok ? 'YES' : 'NO' }}
    {{ Array.from(words).reverse().join('') }}
    <div :id="'list-' + id"/>

    <!--
    是语句，不是表达式
    {{ var a = 1 }}

    流控制不会生效，请使用三元表达式
    {{ if ... }}

    不支持分号，无法添加多个表达式
    {{ message; 1 + 1 }}
    -->
    ```
    </details>
2. 只能访问部分全局变量（白名单）；不允许访问自定义的全局变量（引入的其他库变量仅在JS代码中使用）。
3. 作用域在所属Vue实例范围内。
4. `slot="字符串"`（父级）、`<slot name="字符串">`（子级），用于父级向子组件插入内容。
5. 所有渲染结果不包含`<template>`

### 指令 && 特殊attribute
指令（directives）是带有`v-`前缀的DOM的特殊属性。

>JS表达式的值改变时，将响应式地改变DOM。

1. `:`参数

    用于添加指令后的参数。
2. `v-if`、`v-else`、`v-else-if`

    DOM或组件判定为`false`，则完全销毁（组件会调用`destroyed`）；判定为`true`，则新建。除非使用`<keep-alive>`包裹。
3. `v-for="值/(值, 键)/(值, 键, 索引) in/of JS表达式/整数"`

    ><details>
    ><summary>处于同一节点时，<code>v-for</code>比<code>v-if</code>优先级更高（<code>v-if</code>将分别重复运行于每个<code>v-for</code>循环中）</summary>
    >
    >```html
    ><!-- e.g. -->
    ><li v-for="todo in todos" v-if="!todo.isComplete">
    >  {{ todo }} v-if在v-for循环的每一次都运行判断
    ></li>
    >```
    >
    >避免`v-if`和`v-for`同时用在同一个元素上。
    ></details>

    - 在组件中使用`v-for`时，必须添加`key`属性
    - 尽可能在使用`v-for`时提供`key`属性（除非输出的DOM非常简单，或刻意重用DOM以获取性能提升）

        ```html
        <!-- e.g. -->
        <div v-for="(item, key) in items" :key="key">
          <!-- 内容 -->
        </div>
        ```

        >（相同标签名的DOM切换展示，）没有提供`key`属性：若数据项的顺序被改变，Vue将不会~~移动DOM来匹配数据项的顺序~~；而是保持原DOM尽量不变化，尽量仅修改DOM的属性和内部内容，以确保渲染正确。
4. `v-bind`绑定DOM属性与JS表达式的结果。

    >此DOM属性随表达式最终值改变而改变，直接修改此DOM属性值不改变表达式的值。

    `v-bind:`缩写`:`。

    1. 绑定修饰符：

        1. <details>

            <summary><code>.sync</code></summary>

            >仅为语法糖

            `<my-component :foo.sync="bar"/>`

            等价于：

            `<my-component :foo="bar" @update:foo="val => bar = val"/>`

            - 若要达到效果（同步更新bar），还需要在组件中添加：

                ```javascript
                Vue.component('myComponent', {
                  props: ['foo'],
                  template: '<p @click="doIt">{{foo}}</p>',
                  methods: {
                    doIt () {
                      this.$emit('update:foo', 'new value') // 触发自己的事件（调用父级的回调函数），父级事件改变值，再传入子组件
                    }
                  }
                })
                ```
            </details>
        2. `.prop`（绑定到DOM的`property`而不是HTML标签的 ~~`attribute`~~）
        3. `.camel`（小驼峰式camelCase转换为大驼峰式PascalCase）
    2. 特殊的DOM属性：

        1. 绑定`class`

            1. `:class="{class名: Vue属性[, class名: Vue属性]}"`
            2. `:class="Vue属性对象"`
            3. `:class="[Vue属性[, Vue属性]]"`
            4. `:class="[Vue属性 ? Vue属性 : ''[, Vue属性]]"`
            5. `:class="[{class名: Vue属性}[, Vue属性]]"`
        2. 绑定`style`

            >1. 自动添加样式前缀。
            >2. CSS属性名可以用小驼峰式（camelCase）或短横线隔开式（kebab-case，需用单引号包裹）命名。

            1. `:style="{css属性: Vue属性[, css属性: Vue属性]}"`
            2. `:style="Vue属性对象"`
            3. `:style="[Vue属性[, Vue属性]]"`
            4. 多重值
    3. 传递给子组件DOM属性的值类型

        <details>
        <summary>e.g.</summary>

        ```html
        <!-- 传递字符串 -->
        <my-component some-prop="1">传递字符串'1'</my-component>
        <my-component some-prop="a">传递字符串'a'</my-component>

        <!-- 传递表达式的值 -->
        <my-component :some-prop="1">传递表达式：1（Number）</my-component>
        <my-component :some-prop="'1'">传递表达式：'1'（String）</my-component>
        <my-component :some-prop="a">传递表达式：a（变量是什么类型就是什么类型）</my-component>
        ```
        </details>
    4. 若不带参数的`v-bind="表达式"`，则绑定表达式的所有属性到DOM。

        <details>
        <summary>e.g.</summary>

        ```html
        <div id="test">
          <div v-bind="objs">绑定了title和href属性</div>
          <div v-bind="{alt: 123, href:'https://asd.asd'}">绑定了alt和href属性</div>
        </div>

        <script>
          const vm = new Vue({
            el: '#test',
            data: {
              objs: {
                title: 'My title',
                href: 'http://asd.asd'
              }
            }
          })
        </script>
        ```
        </details>
5. `v-on`事件监听

    `v-on:`缩写`@`。

    1. 事件修饰符：

        1. `.stop`（阻止冒泡）、`.prevent`（阻止默认行为）、`.capture`（捕获事件流）、`.self`（只当事件在该元素本身而不是子元素触发时才触发）、`.once`（事件将只触发一次）、`.passive`（滚动事件的默认滚动行为将立即触发，而不等待~~scroll~~事件完成）
        2. `.enter`、`.tab`、`.delete`、`.esc`、`.space`、`.up`、`.down`、`.left`、`.right`、`.数字键值`、[KeyboardEvent.key的短横线形式](https://developer.mozilla.org/zh-CN/docs/Web/API/KeyboardEvent/key/Key_Values)、`Vue.config.keyCodes`自定义的键位别名

            键盘。
        3. `.left`、`.right`、`.middle`

            鼠标。
        4. `.native`

            监听组件根元素的原生事件，仅在父级引用子组件处添加。
        5. `.exact`

            精确匹配（有其他按键则失败）。

        >- 可同时使用，但改变顺序会产生不同效果。
        >
        >    <details>
        >    <summary>e.g.</summary>
        >
        >    ```html
        >    <!-- Alt + C -->
        >    <input @keyup.alt.67="clear">
        >
        >    <!-- Ctrl + Click -->
        >    <div @click.ctrl="doSomething">...</div>
        >
        >    <!-- 会阻止所有点击的默认行为，该元素点击触发doThat -->
        >    <div @click.prevent.self="doThat">...</div>
        >
        >    <!-- 只会阻止该元素点击的默认行为，该元素点击触发doThat -->
        >    <div @click.self.prevent="doThat">...</div>
        >    ```
        >    </details>
    2. `$event`原生DOM事件的变量，仅能由HTML传入

        <details>
        <summary>e.g.</summary>

        ```html
        <div id="test">
          <a href="#" @click="a($event)">click</a>
        </div>

        <script>
          const vm = new Vue({
            el: '#test',
            methods: {
              a: function (e) {
                console.log(e)
              }
            }
          })
        </script>
        ```
        </details>
    3. 自定义事件

        仅定义在父组件对子组件的引用上，只能由子组件内部`$emit`触发，然后触发父级方法，再通过改变父级属性去改变子组件的`props`（或置换组件）。
    4. 支持不带参数绑定（值为**事件-监听器**的键-值的对象）

        >不支持修饰符。

        e.g. `<button v-on="{ mousedown: doThis, mouseup: doThat }"/>`
6. `v-model`表单

    >忽略表单元素上的`value`、`checked`、`selected`等初始值，而仅通过Vue实例赋值。

    1. 表单修饰符：

        `.lazy`（`change`而不是~~input~~事件触发）、`.number`（输入值转为`Number`类型）、`.trim`（过滤首尾空格）
    2. 仅针对部分元素：`<input>`、`<textarea>`、`<select>`、组件
    3. <details>

        <summary>仅为语法糖</summary>

        1. 普通DOM

            `<input v-model="bar">`

            等价于：

            `<input :value="bar" @input="bar = $event.target.value">`
        2. 组件

            `<my-input v-model="bar"/>`

            等价于（默认：属性绑定为`value`、事件绑定为`input`）：

            `<my-input :value="bar" @input="bar = arguments[0]"/>`

            - 若要达到效果（双向数据绑定），还需要在组件中添加：

                ```javascript
                Vue.component('myInput', {
                  props: ['value'],
                  template: '<input :value="value" @input="updateValue($event)">',
                  methods: {
                    updateValue (e) {
                      this.$emit('input', e.target.value) // 触发自己的事件（调用父级的回调函数），父级事件改变值，再传入子组件
                    }
                  }
                })
                ```
        </details>
    4. 绑定的Vue实例的值：

        1. DOM的`value`属性的值；
        2. 若是`type="checkbox"`，则为`true/false`；
        3. 若要获得Vue实例的动态属性值：

            1. 用`:value="表达式"`；
            2. 若`type="checkbox"`，则用`:true-value="表达式" :false-value="表达式"`。
7. `v-once`一次性插值，不再~~双向绑定~~
8. `v-text`等价于`{{  }}`
9. `v-html`输入真正HTML

    ><details>
    ><summary>与其他插值（如模板插值）的区别</summary>
    >
    >1. `v-html`：`innerHTML`。
    >2. `v-text`、`{{ }}`及其他插值：`innerText`。
    ></details>
10. `v-pre`不编译

    >e.g. `<p v-pre>{{ 不编译 }}</p>`
11. `v-show`

    总是渲染出DOM，根据值切换`display`值。

    >不支持`<template>`、不支持`v-else`。
12. `v-cloak`指令保持在元素上直到关联实例结束编译
13. `.`修饰符

    >用于指出一个指令应该以特殊方式绑定。

    使用在`v-on`、`v-bind`、`v-module`后添加。
14. `|`使用filters过滤器，参数带入函数运行出结果（支持过滤器串联）

    <details>
    <summary>e.g.</summary>

    ```html
    <div id="test">
      <p>{{ 1 | a | b }}</p>    <!-- 3 -->
      <p>{{ num | a | b }}</p>  <!-- 5 -->
    </div>

    <script>
      // 局部
      const vm = new Vue({
        el: '#test',
        data: {
          num: 2
        },
        filters: {
          a: function (e) {
            return e * 2
          },
          b: function (e) {
            return e + 1
          }
        }
      })


      // 全局
      Vue.filter('a', function (e) {})
    </script>
    ```
    </details>
15. 自定义指令（在钩子函数中进行业务）

    `v-自定义指令名`或`v-自定义指令名="表达式"`

    1. 全局

        ```javascript
        // 在全局的模板内使用
        Vue.directive('自定义指令名', 钩子对象)
        ```
    2. 局部

        ```javascript
        new Vue({
          // 在局部的模板内使用
          directives: {
            自定义指令名: 钩子对象,
          }
        })
        ```

    ><details>
    ><summary><code>钩子对象</code></summary>
    >
    >```javascript
    >{
    >  // 只调用一次，指令第一次绑定到元素时调用。在这里可以进行一次性的初始化设置
    >  bind (el, binding, vnode) {},
    >
    >  // 被绑定元素插入父节点时调用 (仅保证父节点存在，但不一定已被插入文档中)
    >  inserted (el, binding, vnode) {},
    >
    >  // 所在组件的 VNode 更新时调用，但是可能发生在其子 VNode 更新之前。指令的值可能发生了改变，也可能没有。但是你可以通过比较更新前后的值来忽略不必要的模板更新 (详细的钩子函数参数见下)
    >  update (el, binding, vnode, oldVnode) {},
    >
    >  // 指令所在组件的 VNode 及其子 VNode 全部更新后调用
    >  componentUpdated (el, binding, vnode, oldVnode) {},
    >
    >  // 只调用一次，指令与元素解绑时调用
    >  unbind (el, binding, vnode) {}
    >}
    >```
    ></details>

- 官方推荐的顺序：[元素特性的顺序](https://cn.vuejs.org/v2/style-guide/#元素特性的顺序-推荐)

### Vue实例的属性
`new Vue(对象)`

1. `el`（字符串）：选择器
2. `methods`（对象）：可调用方法

    >`new`methods里的方法，方法体内的`this`指向这个实例，而非Vue实例。建议不要在methods中添加构造函数，而改用`import`方式引入构造函数。
3. `data`（对象或方法）：数据

    >组件的`data`是方法且返回一个数据对象。
4. `computed`（对象）：依赖其他值（`props`、`data`、`computed`）的改变而执行，最后`return`值

    <details>
    <summary>默认：<code>get</code>（初始化时会调用一次）；显式设置：<code>set</code>（被赋值时执行）和<code>get</code></summary>

    当没有设置`set`时，不能主动去设置`computed`的值（~~`this.计算属性 = 值`~~）；设置了`set`也不能改变自己的值（`set`函数里不能再循环设置自己的值）。

    ```javascript
    // e.g.
    const vm = new Vue({
      data: {
        firstName: 'firstname',
        lastName: 'lastname'
      },
      computed: {
        fullName: {
          // getter
          get: function () { // 初始化和this.firstName或this.lastName改变时调用；this.fullName被赋值时不会直接调用
            return this.firstName + ' ' + this.lastName
          },
          // setter
          set: function (newValue) { // this.fullName被赋值时调用
            const names = newValue.split(' ')
            this.firstName = names[0]
            this.lastName = names[names.length - 1]
            // 不允许`this.fullName = 值`会导致死循环
          }
        }
      }
    })

    // 运行 vm.fullName = 'John Doe' 时，setter 会被调用，vm.firstName 和 vm.lastName 也会相应地被更新
    ```
    </details>

>在（`props`、）`data`、`computed`先定义再使用，而不要对未使用过的变量进行`this.新变量名 = 值`。

5. `watch`（对象）：被watch的（`props`或）`data`或`computed`属性改变而执行（必须是`props`或`data`或`computed`的属性）

    可以设置`immediate`（侦听开始后立即调用一次）和`deep`参数。

>执行顺序是：（`props` -> ）`data` -> `computed` -> `watch`。

6. `filters`（对象）：过滤器方法

    >因为不是Vue实例代理属性，所以可以和Vue实例代理（`props`、`data`、`computed`、`methods`）的属性同名。
7. `components`（对象）：局部注册组件（仅在此Vue实例中可用）
8. 生命周期钩子

    1. `beforeCreate`

    >实例的（`props`、）`data`、`computed`、`watch`等实例内容的创建，在`beforeCreate`之后、`created`之前。

    2. `created`
    3. `beforeMount`
    4. `mounted`

    >页面加载后就要展现的数据，可以在`created`、`beforeMount`、`mounted`进行（`vue-router`等封装了更方便的钩子，可以控制比如在数据加载完毕后再进行跳转）。

    5. `beforeUpdate`
    6. `updated`
    7. `activated`

        >`<keep-alive>`组件特有，内部组件激活时在内部组件调用。
    8. `deactivated`

        >`<keep-alive>`组件特有，内部组件停用时在内部组件调用。
    9. `beforeDestroy`

        >可将大部分内存清理工作放在`beforeDestroy`。
    10. `destroyed`

        >调用后，Vue实例指示的所有东西都会解绑，所有Vue事件监听器会被移除，所有子实例也会被销毁。
    11. `errorCaptured`

    <details>
    <summary>生命周期图示</summary>

    ![vue生命周期图](./images/vue-lifecycle-1.png)
    </details>
9. `mixins`（数组，每一项为Vue实例的属性）：混入

    mixin数组每一项中的属性，都会合并到组件本身的选项（如：mixin的`methods`合并到组件的`methods`、mixin的`data`合并到组件的`data`）。

    1. 钩子函数都会调用：混入对象的钩子优先调用，组件自身的钩子之后调用。
    2. 非钩子函数属性，若有同名内容，则合并之后，组件自身内容覆盖mixin：

        `methods`、`components`、`directives`等，合并为同一个对象；对象内部键名冲突时（如`methods`都有某同名方法），使用组件对象的内容、丢弃mixin的内容。

    - 作用域：

        1. 全局：`Vue.mixin`全局注册，将会影响之后创建的（之前的不受影响）Vue实例，包括第三方模板。
        2. 局部：组件局部注册，仅在本组件内起作用，对子组件无效。

- 官方推荐的顺序：[组件/实例的选项的顺序](https://cn.vuejs.org/v2/style-guide/#组件-实例的选项的顺序-推荐)

### 组件
>所有Vue组件同时也都是Vue实例。

1. 组件属性：

    1. `template`（字符串）：组件的字符串模板

        - 作用域：

            `template`的字符串模板内容为本组件作用域；父级添加的DOM（包括引用子组件）为父级作用域。
        - 内容分发

            子组件使用`<slot>`在内部插入父级引入的内容（`slot="字符串"`）。

            1. 默认

                1. 模板中没有`name`属性的`<slot>`，匹配父级中去除所有`slot="字符串"`引用的内容（没有`slot`或`slot`值为空的DOM）。
                2. 模板中`<slot>`的DOM内容，仅当没有父级匹配时显示。
            2. 具名

                1. 父级引用子组件，在元素内部添加的标签的DOM属性`slot="字符串"`；
                2. 组件模板：`<slot name="字符串">`。
            3. 作用域插槽

                1. 子组件的模板：

                    `<slot 组件属性="字符串">`或`<slot :组件属性="表达式">`
                2. 父级引用子组件元素内部的内容：

                    >`slot-scope`必须在一个父级`slot`定义（默认/具名），在`slot`内部DOM挂载`slot-scope`无效。

                    `<标签或组件名 slot slot-scope="临时变量">{{临时变量.组件属性}}</标签或组件名>`

                    >`<template>`使用`slot-scope`属性时，不要同时使用`v-if`。
    2. `props`（数组或对象）：接受父级传递内容

        1. 数组：接受的DOM属性名
        2. 对象：`{ 接受的DOM属性名: 验证方式, }`

            - 验证方式：

                1. 原生构造器（`String`、`Number`、`Boolean`、`Function`、`Object`、`Array`、`Symbol`）、或`null`（允许任何类型）
                2. 原生构造器的数组
                3. 对象

                    1. `type`：原生构造器、或`null`、或原生构造器的数组
                    2. `required`：是否必须（默认：`false`）
                    3. `default`：基本数据类型的值；对象或数组必须从工厂函数返回默认值（仅当没有传入时才使用或调用）

                    >`required`和`default`二选一。

                    4. `validator`：验证方法（对子组件的任何修改包括`v-show`修改以及自身`default`，都会触发所有prop的验证方法）

                    >props会在一个组件实例创建之前进行验证，所以实例的属性（如：`data`、`computed`、`methods`等）在`default`或`validator`函数中不可用。
    3. `data`（方法）：`return`数据对象

        ```javascript
        data () {   // 组件多个实例间不共享数据对象
          return {
            a: 0,
            b: ''
          }
        }
        ```

        >1. `v-for`循环的每个实例都调用创建一份。
        >2. 仅执行一次，父组件传进来的props改变也不再触发执行。
    4. `model`（对象，包含`prop`、`event`）：修改`v-model`默认使用的属性和事件

    - 其他与Vue实例的属性相同（除了一些根级特有的选项）
2. 注册组件方式：

    >要确保在初始化Vue实例之前注册了组件。

    1. 全局

        `Vue.component('组件元素名', 对象)`
    2. 局部

        ```javascript
        // Vue实例
        new Vue({
            components: {
                '组件元素名': 对象 // 仅在此Vue实例中可用
            }
        })
        ```
3. 组件命名：

    >W3C规定的组件命名要求：小写，且包含一个`-`。

    1. JS注册组件或`props`：

        短横线隔开式（kebab-case）、小驼峰式（camelCase）、大驼峰式（PascalCase）。
    2. HTML中：

        1. 仅能使用短横线隔开式（把大/小驼峰式用`-`隔开并小写单词代替）
        2. 在JS字符串模版、`.vue`组件，可以使用额外方式

            <details>
            <summary>e.g.</summary>

            ```html
            <!-- HTML必须是短横线隔开式 -->
            1. <kebab-cased-component/>
            2. <camel-cased-component/>
            3. <pascal-cased-component/>

            <!-- 在JS字符串模版、.vue组件额外可以使用 -->
            1. 无
            2. <camelCasedComponent/>
            3. <pascalCasedComponent/>
            3. <PascalCasedComponent/>

             <script>
             // 注册的组件
             new Vue({
               components: {
                 'kebab-cased-component': {},
                 camelCasedComponent: {},
                 PascalCasedComponent: {}
               }
             })
             </script>
            ```
            </details>
4. 使用组件：

    1. `<组件名/>`

        >不会导致渲染出错的方式：JS字符串模版、`.vue`组件。
    2. `<有效标签 is="组件名"/>`
    3.  动态组件：`<component :is="表达式"/>`

        >~~`<component is="组件名字符串"/>`~~ 也可执行，只不过写死了某个组件，没有了“动态”的意义。

        ```html
        <div id="test">
          <component :is="current1"/>
          <component :is="current2"/>
        </div>

        <script>
          const vm = new Vue({
            el: '#test',
            data: {
              current1: { template: '<p>111</p>' }, // 对象，则当作组件对象渲染
              current2: 'component2'                // 字符串，则搜索已注册的components
            },
            components: {
              component2: { template: '<p>222</p>' }
            }
          })
        </script>
        ```

        - `<keep-alive>`包裹，保留它的状态或避免重新渲染。
    4. `<keep-alive>`

        `<keep-alive>组件</keep-alive>`，会缓存不活动的组件实例，而不是销毁、重建。当组件在其内被切换时，组件的`activated`、`deactivated`被对应执行。
5. 通信

    >组件（Vue实例）有自己独立的作用域，虽然可以访问到互相依赖关系（`$parent`、`$children`），但是不建议（不允许）通过依赖获取、修改数据。

    1. 父子组件间的通信

        父-`props`->子：传入属性值；子-`$emit`->父：触发外部环境事件；外部事件再改变传进组件的`props`值。

        1. 父->子：通过`props`向下传递初始化数据给子组件实例（不出现在DOM中）

            >添加在DOM上而不在`props`声明，则仅添加到子组件最外层的DOM属性，不传入子组件。其中`class`和`style`属性会合并，其他属性会覆盖。

            1. `props`是单向传递的：当父级的属性变化时，将传导给子组件，不会反过来

                每次父组件更新时，子组件的所有prop都会更新为最新值。
            2. 不应该 ~~在子组件内部改变`props`~~（只能`$emit`到父级再由父级传`props`进子组件来改变）。

                1. 仅展示：直接在模板引用`props`。
                2. 一次性传值（仅首次传值有效，后续传值无法修改`data`）：`props` -> `data`。
                3. 每次对传值内容进行修改后使用：`props` -> `computed`。
                4. 每次根据传值内容进行其他逻辑：`props` -> `watch`。

                <details>
                <summary>e.g.</summary>

                ```javascript
                Vue.component(
                  'myComponent',
                  {
                    props: ['father'], // 可以直接用在子组件内展示
                    data () {
                      return {
                        son1: this.father  // 仅接受首次传值，后续的props变化不再改变
                      }
                    },
                    computed: {
                      son2() {
                        return this.father // 每次对传值内容进行修改后使用
                      }
                    },
                    watch: {
                      father(data) { // 每次根据传值内容进行其他逻辑
                        console.log(data)
                      }
                    },
                    template: '<div>{{ father }}-{{ son1 }}- {{ son2 }}</div>'
                  }
                )
                ```
                </details>

            >注意避免**引用数据类型**导致的子组件改变父级。
        2. 子->父：通过`$emit`向上传递事件、参数

            1. 在父级引用子组件处添加`@自定义事件1="父方法"`监听；

                >若`自定义事件1`是原生事件，可以添加`.native`修饰符，监听组件根元素的原生事件（不再接收子组件的 ~~$emit~~）。
            2. 在子组件方法体内添加`this.$emit('自定义事件1', 参数)`向上传递。
    2. 非父子组件通信

        1. 在简单的场景下，可以使用一个空的Vue实例作为中央事件总线。

            ```javascript
            const bus = new Vue()   // $emit只能向自己的Vue实例发送触发事件通知

            // 触发组件 A 中的事件
            bus.$emit('事件名', 传参)

            // 在组件 B 创建的钩子中监听事件
            bus.$on('事件名', function (para) {})
            ```
        2. 或专门状态管理模式，如[vuex](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/Vue.js学习笔记/README.md#vuex)。
    - 组件的API来自三部分

        `<my-component :子属性="父属性" @父事件="父方法"><标签 slot="名字">内容分发</标签></my-component>`

        1. `props`：允许外部环境传递数据给组件。
        2. `events`：允许从组件内触发外部环境的副作用。
        3. `slots`：允许外部环境将额外的内容组合在组件中。

- 杂项

    1. 父级引用组件时添加属性`ref="字符串"`，可以在Vue实例的`$refs`中访问。
    2. 内联模板：

        引用组件时，添加`inline-template`DOM属性。组件的内容当作模板，而不是分发内容。
    3. `<script type=text/x-template id="id名">`

        ```javascript
        Vue.component('组件名', {
          template: '#id名'
        })
        ```
    4. 当组件中包含大量静态内容时，可以考虑使用`v-once`将渲染结果在组件注册的`template`字段里缓存起来。
    5. 异步组件。
    6. 高级异步组件。
    7. 递归组件。
    8. 循环组件。

### 单文件组件
1. （有导出的）组件内部可以直接引用自身组件（小心无止境的循环引用）
2. 大部分都用局部注册。除非是大范围的统一功能，才用全局方式，才用插件方式。
3. 单文件组件的局部样式

    1. `scoped`（[vue-loader的Scoped CSS](https://vue-loader.vuejs.org/zh/guide/scoped-css.html)）

        1. 使用`scoped`的**单文件组件**内所有Element、**其引用的子组件的根节点**，都会添加自定义`attributes`（如`data-v-2185bf6b`）；非Vue内部生成的节点（手动添加）不会添加自定义`attributes`。
        2. `scoped`方式引用整个样式文件：

            1. 局部：`<style scoped src="@/assets/文件名.css"></style>`
            2. ~~全局~~

                1. `<script>import '@/assets/文件名.css'</script>`
                1. `<style scoped>@import "../assets/文件名.css";</style>`
    2. `module`（[vue-loader的CSS Modules](https://vue-loader.vuejs.org/zh/guide/css-modules.html)）

        在`<style>`添加`module`，即在Vue实例内加入`$style`对象，访问单文件组件内`<style module>`的选择器。
4. <details>

    <summary><del>可以在组件内部（或Vue实例内部）或外部，再创建另一个Vue实例，并且可以互相通信</del></summary>

    主要为了解决：要挂载到不在组件操作范围内的DOM（不建议、反模式）。

    ```javascript
    // 某单文件组件One.vue
    import Vue from 'vue'
    import store from '@/store'
    import router from '@/router'
    import Other from '@/components/Other.vue'

    export default {
      data () {
        return {
          text: '123',
          dom: null
        }
      },
      mounted () {
        // 新建一个Vue实例
        const OtherVue = Vue.extend(Other)  // 创建Vue子类，继续创建Vue实例需要再`new`创建好的子类
        this.dom = new OtherVue({  // 后定义，类似于mixin的合并逻辑（钩子：先定义执行->后定义执行；非钩子：后定义执行、先定义忽略）
          store,  // 共享store
          router, // 共享router
          created () {  // 合并。先定义的钩子先执行，后定义的钩子后执行
            console.log('father created')
          },
          methods: {  // 合并。若属性名相同则后定义的覆盖先定义的
            changeFatherText: () => {
              this.text = Math.random() // this为当前的组件One.vue
            }
          },
          computed: {  // 合并。若属性名相同则后定义的覆盖先定义的
            myText: () => {
              return this.text  // // this为当前的组件One.vue
            }
          }
        }).$mount().$el

        document.getElementById('other').appendChild(this.dom)    // 要挂载到不在组件操作范围内的DOM（若要挂载到组件内，请在组件内的`<template>`进行）
      },
      beforeDestroy () {
        document.getElementById('other').removeChild(this.dom)

        this.dom = null
      }
    }
    ```
    </details>

- 推荐的文件名命名方式：

    1. 两个及以上单词
    2. 大驼峰式（PascalCase）或短横线隔开式（kebab-case）

### 过渡/动画
>此处描述的“帧”是`requestAnimationFrame`（在浏览器下一次重绘之前执行），而不是~~Vue的`nextTick`~~（在Vue控制的DOM下次更新循环结束之后执行）。

- 插入、更新、移除DOM时，提供过渡/动画的操作

    1. 在CSS过渡/动画中自动应用class（可配合使用第三方CSS动画库，如[animate.css](https://github.com/daneden/animate.css)）
    2. 在过渡钩子函数中使用JS直接操作DOM（可配合使用第三方JS动画库，如[velocity](https://github.com/julianshapiro/velocity)）

1. `<transition>`（仅针对第一个子元素）

    >1. 过渡/动画效果仅加在第一个子元素上（子元素内部不会触发）。
    >2. `<transition>`内仅能展示唯一一个子元素（多个元素用`<transition-group>`）。
    >3. 不添加真实的DOM，只有逻辑（`<transition-group>`会添加真实的DOM）。

    提供给包裹的第一个子元素（任何DOM或组件）**进入/离开**的过渡/动画效果。

    1. 触发条件：

        ①在`<transition>`内嵌套子元素，在子元素上进行以下操作；或②引用根节点是`<transition>`的组件，在父级引用上进行以下操作、或在此组件根节点`<transition>`内嵌套的子元素进行以下操作：

        1. `v-if`（`v-else`、`v-else-if`）
        2. `v-show`
        3. `<component :is="表达式"/>`
    2. 触发机制：

        1. 自动嗅探目标元素是否应用了CSS过渡/动画。若是，则在恰当的时机添加/删除CSS类名。
        2. 若`<transition>`添加了过渡钩子，则这些钩子函数在恰当的时机被调用。

        - 若以上都没有，则DOM操作在下一帧执行。
    3. 特殊的props（在`<transition>`组件引用上添加）：

        1. `name`：用于自动生成CSS过渡/动画类名的前缀（默认：`'v'`）

            <details>
            <summary>在进入/离开的过渡/动画中，class切换（若监测到已手动添加了相关类的样式，才会切换）</summary>

            >1. 以`name`默认为`'v'`为例。
            >2. 过渡：CSS的`transition`；动画：CSS的`animation-@keyframes`。

            1. 进入过程

                1. `v-enter`：

                    >定义具体进入过渡的样式（若`v-enter-active`使用`animation-@keyframes`，则可以不设置`v-enter`的样式）。

                    定义进入过渡的开始状态。存在时间：在元素插入之前开始；在元素插入之后的下一帧结束（与此同时`v-enter-to`被添加）。
                2. `v-enter-active`：

                    >定义进入过渡/动画的过程时间、延迟、曲线函数（CSS的`transition`或`animation-@keyframes`）。

                    定义进入过渡/动画的整个状态。存在时间：在`v-enter`存在之后、且元素插入之前开始；在过渡/动画完成之后结束。
                3. `v-enter-to`：

                    >定义元素的初始状态（若和元素本身样式相同，则可以不设置`v-enter-to`的样式）。

                    定义进入过渡的结束状态。存在时间：在元素插入之后下一帧开始 (与此同时`v-enter`被移除)；在过渡/动画完成之后结束。
            2. 离开过程

                1. `v-leave`：

                    >定义元素的初始状态（若和元素本身样式相同，则可以不设置`v-leave`的样式）。

                    定义离开过渡的开始状态。存在时间：在离开过程触发时开始；下一帧结束（与此同时`v-leave-to`被添加）。
                2. `v-leave-active`：

                    >定义离开过渡/动画的过程时间、延迟、曲线函数（CSS的`transition`或`animation-@keyframes`）。

                    定义离开过渡/动画的整个状态。存在时间：在`v-leave`存在之后开始；在过渡/动画完成之后结束。
                3. `v-leave-to`：

                    >定义具体离开过渡的样式（若`v-leave-active`使用`animation-@keyframes`，则可以不设置`v-leave-to`的样式）。

                    定义离开过渡的结束状态。存在时间：在离开过程触发的下一帧开始（与此同时`v-leave`被移除）；在过渡/动画完成之后结束（与此同时元素移除）。
            </details>
        2. 自定义过渡/动画的类名

            >优先级高于普通的类名，主要用于和第三方CSS动画库配合，如[animate.css](https://github.com/daneden/animate.css)。

            1. `enter-class`
            2. `enter-active-class`
            3. `enter-to-class`
            4. `leave-class`
            5. `leave-active-class`
            6. `leave-to-class`
        3. `type`：指定过渡事件类型（`'transition'`或`'animation'`。默认：自动检测出持续时间长的）
        4. `duration`：不根据过渡/动画的JS事件，而手动设置过渡/动画时间（毫秒）

            >e.g. `:duration="1000"`或`:duration="{ enter: 500, leave: 800 }"`
        5. `css`：是否使用CSS过渡/动画的class（默认：`true`。若`false`，则只触发过渡钩子）
        6. 过渡钩子事件：

            >推荐对于仅使用JS过渡的`<transition>`添加`:css="false"`。

            1. 进入过程

                1. `before-enter`
                2. `enter`（与CSS结合使用。当只用JS过渡时，在`enter`中必须调用函数的第二个参数`done`）
                3. `after-enter`
                4. `enter-cancelled`
            2. 离开过程

                1. `before-leave`
                2. `leave`（与CSS结合使用。当只用JS过渡时，在`leave`中必须调用函数的第二个参数`done`）
                3. `after-leave`
                4. `leave-cancelled`
        7. `appear`：是否在初始渲染时使用过渡/动画（默认：`false`）

            - （可选）初始渲染时使用额外的类名、钩子事件（`:appear="true"`）

                1. 初始渲染的自定义过渡/动画的类名：

                    1. `appear-class`
                    2. `appear-active-class`
                    3. `appear-to-class`
                2. 初始渲染的过渡钩子事件：

                    1. `before-appear`
                    2. `appear`
                    3. `after-appear`
                    4. `appear-cancelled`
        8. `mode`：（当有子元素切换时，）控制进入/离开的过渡顺序（`'out-in'`：先离开后进入；`'in-out'`：先进入后离开。默认：同时进行）
    4. `<transition>`内嵌的子元素切换：

        1. 若是**原生**子元素用`v-if`（`v-else`、`v-else-if`）作为切换，则必须在这些子元素上添加`key`属性。
        2. 若是**组件**子元素，则不需要额外添加 ~~`key`~~ 属性。

            1. 用`v-if`（`v-else`、`v-else-if`）作为切换。
            2. 用动态组件`<component :is="表达式"/>`进行切换。
2. `<transition-group>`

    >子元素必须添加`key`属性。

    1. 触发条件、触发机制与`<transition>`类似。
    2. 特殊的props（在`<transition-group>`组件引用上添加）：

        1. `tag`：子级外层嵌套的标签名（默认：`'span'`）
        2. `move-class`：用于自动改变定位时引用的类名（默认：`name`属性的值 + `'-move'`）

        - 除了 ~~`mode`~~ 无效之外，拥有与`<transition>`相同的props

>自制可复用的过渡组件：把`<transition>`或`<transition-group>`作为根组件。

### 插件
```javascript
// 插件是.js文件，应当有一个公开的install方法
MyPlugin.install = function (Vue, options) { // 第一个参数是Vue构造器，第二个参数是Vue.use时传入的可选参数对象
  // 1. 添加全局方法或属性
  Vue.myGlobalMethod = function () {
    // 逻辑...
  }

  // 2. 添加全局资源
  Vue.directive('my-directive', {
    bind (el, binding, vnode, oldVnode) {
      // 逻辑...
    },
  })

  // 3. 注入组件
  Vue.mixin({
    created: function () {
      // 逻辑...
    },
  })

  // 4. 添加实例方法（约定用`$`开头来命名原型自定义属性）
  Vue.prototype.$myMethod = function (methodOptions) {
    // 逻辑...
  }
}


// 在其他地方使用
Vue.use(MyPlugin, { someOption: true })  // Vue.use会自动阻止多次注册相同插件，届时只会注册一次该插件。
```

### 特性
1. 重用DOM（尽量在已存在的DOM上做修改、保持原DOM尽量不变化，而不是~~移除再新建DOM或移动DOM~~）

    >针对：相同标签名的DOM切换展示。

    1. 当没有`key`属性或`key`属性相同时（重复的`key`可能造成渲染错误）：最大化重用DOM。
    2. 切换的DOM的`key`属性不同：不重用DOM。
2. Vue实例代理`props`、`data`、`computed`、`methods`的属性内容（在内部可以`this.名字`访问），可以直接修改或调用，**所有属性名字都不能重复**；也有以`$`开头的Vue实例属性（如`$el`、`$data`、`$watch`）。

    只有已经被代理的内容是响应的（Vue实例被创建时的`props`、`data`、`computed`），值的改变（可能）会触发视图的重新渲染。

    1. 导致视图更新：

        1. 数组的某些mutator方法：`push`、`pop`、`unshift`、`shift`、`reverse`、`sort`、`splice`
        2. 数组赋值
        3. 插值：`Vue.set(数组/对象, 索引/键, 新值)`
    2. 无法检测数组变动：

        1. 直接数组索引赋值。

            >导致视图更新的替代方法：`Vue.set(vm.items, index, value)`或`vm.items.splice(index, 1, value)`。
        2. 直接修改数组长度。

            >导致视图更新的替代方法：`vm.items.splice(newLength)`。
        3. 数组的最新mutator方法：`copyWithin`、`fill`
3. 外层慎用~~箭头函数~~，`this`的指向无法按预期指向Vue实例。
4. 因为HTML不区分大小写，所以大/小驼峰式命名的JS内容，在HTML使用时要转换为相应的短横线隔开式。

    不受限制、不需要转换：JS字符串模版、`.vue`组件。

    >JS字符串模版：`<script type="text/x-template">`、JS内联模板字符串。

### 虚拟DOM
在底层的实现上，Vue将模板编译成虚拟DOM渲染函数。结合响应系统，Vue能够智能地计算出最少需要重新渲染多少组件，并把DOM操作次数减到最少。

### 双向绑定
1. `Object.defineProperty`

    数据劫持。
2. 事件监听

---
### [vue-router](https://github.com/vuejs/vue-router)
1. 初始化

    ```javascript
    new Vue({
      router: new VueRouter({
        mode: 'hash或history或abstract',    // 默认：hash
        base: '/...基路径/',           // 仅在history模式下，设置应用的基路径
        routes: [
          // 普通路由
          {
            path: '路由参数',       // 除了path，其他都是可选
            component: 组件,
            name: '路由名',
            redirect: 路由参数,     // 重定向（URL变化）
            alias: 路由参数,        // 别名（URL不变化）
            props: 布尔或对象或函数, // 传参进组件（布尔值决定$route.params是否被设置为组件属性；对象或函数则传入具体属性）。针对components要再嵌套一层对象
            beforeEnter: 方法,
            meta: '额外信息参数',
            caseSensitive: 布尔值,       // 匹配规则是否大小写敏感（默认：false）
            pathToRegexpOptions: 对象,   // 编译正则的选项
          },

          // 动态路由
          {
            path: ':动态路由',
            component: 组件
          },

          // 命名视图
          {
            path: '路由参数',
            components: {
              'default': 组件,
              '视图名1': 组件,
            },
            props: {
              'default': 布尔或对象或函数,
              '视图名1': 布尔或对象或函数
            }
          },

          // 嵌套路由（可以嵌套所有类型的路由）
          {
            path: '路由参数',
            component: 组件,
            children: [
              路由配置,
            ]
          },
        ],
        linkActiveClass: 'router-link-active',              // 激活<router-link>的CSS类名
        linkExactActiveClass: 'router-link-exact-active',   // 精确激活<router-link>的CSS类名
        scrollBehavior: 方法,
        parseQuery/stringifyQuery: 方法,
        fallback: 方法,
      }),
    })
    ```
2. 内置组件

    1. `<router-link>`：导航

        1. `to`：目标地址
        2. `replace`：（默认：`false`）是否使用`replace`替换~~push~~
        3. `tag`：（默认：`a`）生成其他标签名
        4. `append`：（默认：`false`）是否是相对路径
        5. `exact`：（默认：`false`）：是否精确激活
        6. `event`：（默认：`'click'`）：触发导航的事件
        7. `active-class`：（默认：`'router-link-active'`）：链接激活时使用的CSS类名
        8. `exact-active-class`：（默认：`'router-link-exact-active'`）：被精确匹配的时候应该激活的CSS类名
    2. `<router-view>`：渲染路由匹配的组件（可嵌套）

        `name`：（默认：`'default'`）命名视图的名字
3. 注入后在组件中增加

    1. `$router`：路由器实例对象

        1. `app`：Vue根实例
        2. `mode`：路由模式
        3. `currentRoute`：`$route`
        4. `beforeEach/beforeResolve/afterEach(方法)`：导航守卫
        5. `go(数字)`
        6. `back()`
        7. `forward()`
        8. `push(路由字符串或对象[, 完成回调函数[, 失败回调函数]])`
        9. `replace(路由字符串或对象[, 完成回调函数[, 失败回调函数]])`
        10. `getMatchedComponents(location?)`
        11. `resolve(location, current?, append?)`
        12. `addRoutes(routes)`
        13. `onReady(callback, [errorCallback])`
        14. `onError(callback)`
    2. `$route`：当前激活的路由的状态信息

        1. `path`：绝对路径
        2. `params`：动态路由的路由参数对象
        3. `query`：查询参数对象
        4. `hash`：hash值
        5. `matched`：匹配到的路由数组
        6. `fullPath`：完整路径
        7. `name`：路由名称
        8. `redirectedFrom`：若存在重定向，则为重定向来源的路由名字

        - <details>

            <summary>检测路由变化，可以在组件中<code>watch</code>注入的<code>$route</code>或使用额外的钩子（导航守卫）</summary>

            ```javascript
            new Vue({
              watch: {
                '$route' (to, from) {
                  // 对路由变化作出响应...
                }
              }
            })
            ```
            </details>
    3. 增加钩子：`beforeRouteEnter`、`beforeRouteUpdate`、`beforeRouteLeave`
4. 导航守卫

    ><details>
    ><summary>守卫接收三个参数<code>to, from, next</code></summary>
    >
    >1. `to`：即将进入的目标`$route`
    >2. `from`：正在离开的`$route`
    >3. `next`：`resolve`方法
    ></details>

    1. 全局（通过router对象）

        1. `router.beforeEach((to, from, next) => {})`
        2. `router.beforeResolve((to, from, next) => {})`
        3. `router.afterEach((to, from) => {})`
    2. 路由配置中

        `beforeEnter (to, from, next) {}`
    3. 组件内新增钩子

        1. `beforeRouteEnter (to, from, next) {}`
        2. `beforeRouteUpdate (to, from, next) {}`
        3. `beforeRouteLeave (to, from, next) {}`

    - 完整的导航解析流程

        1. 导航被触发；
        2. 在失活的组件里调用`beforeRouteLeave`守卫；
        3. 调用全局的`beforeEach`守卫；
        4. 在重用的组件里调用`beforeRouteUpdate`守卫；
        5. 在路由配置里调用`beforeEnter`；
        6. 解析异步路由组件；
        7. 在被激活的组件里调用`beforeRouteEnter`；
        8. 调用全局的`beforeResolve`守卫；
        9. 导航被确认；
        10. 调用全局的`afterEach`钩子；
        11. 触发DOM更新；
        12. 用创建好的实例调用`beforeRouteEnter`中的`next`回调函数。
4. 注意

    1. 组件最大限度复用：路由切换时，若两个路由都渲染同个组件，则不会销毁重建，而是直接复用，因此被复用的组件的生命周期钩子不会再被调用。
    2. 匹配优先级：有时候，同一个路径可以匹配多个路由，此时，匹配的优先级就按照路由的定义顺序：谁先定义的，谁的优先级就最高。

### [vuex](https://github.com/vuejs/vuex)
>store的概念：vuex提供的容器，state的集合。

一个专为Vue.js应用程序开发的**状态管理模式**。采用集中式存储管理应用的所有组件的状态（仅一个实例对象就能负责保存整个应用的状态，“唯一数据源”），并以相应的规则保证状态以一种可预测的方式发生变化。vuex的状态存储是**响应式的**，若store中的状态发生变化，则有读取状态的组件（`computed`依赖状态或直接输出状态）也会相应地得到高效更新。

![vuex流程图](./images/vuex-1.png)

1. `state`

    状态（仅能在mutation方法体内改变state）。

    1. 通过store的`state.state名`获取。
    2. 响应规则

        1. 最好提前初始化所需的state（初始化的任何位置都可以被劫持而更新）。
        2. 直接用`=`进行已初始化的state属性更新。
        3. 需要在state或`state.对象`上添加新属性：

            1. `Vue.set(state或state.对象, '新属性名', 值)`
            2. `state.对象 = { ...state.对象, '新属性名': 值 }`

    - <details>

        <summary><code>mapState</code></summary>

        返回对象，用于组件`computed`属性的简写（`data1 () { return this.$store.state.state1 }`）。

        ```javascript
        // 组件中
        import { mapState } from 'vuex'

        new Vue({
          computed: {
            ...mapState({
              // 不需要使用组件属性
              data1: 'state1',  // 等价于：data1: state => state.state1,

              // 需要使用组件属性
              data2 (state) {
                return state.state2 + this.组件属性
              }
            }),
            // 或
            ...mapState([ // computed使用与state属性相同名字可用数组
              'state1',
              'state2'
            ])
          },
        })
        ```
        </details>
2. `getters`

    由state或其他getter派生的值。

    1. 通过store的`getters['getter名']`获取。
    2. 根据方法返回值的依赖而改变（仅能在自己的getter中改变值，不能在其他getter或mutations或actions改变值），store的计算属性。
    3. （就像Vue的`computed`一样，）getter的返回值会根据它的依赖被缓存起来，且只有当它的依赖值发生了改变才会被重新计算；若getter返回一个函数，每次都会去进行调用，而不会缓存结果。

    - <details>

        <summary><code>mapGetters</code></summary>

        返回对象，用于组件`computed`属性的简写（`data1 () { return this.$store.getters['getters1'] }`）。

        ```javascript
        // 组件中
        import { mapGetters } from 'vuex'

        new Vue({
          computed: {
            ...mapGetters({
              data1: 'getters1',
              data2: 'getters2',
            }),
            // 或
            ...mapGetters([ // computed使用与getters属性相同名字可用数组
              'getters1',
              'getters2'
            ])
          }
        })
        ```
        </details>
3. `mutations`

    改变state的唯一方式。

    1. 通过store调用`commit('mutation方法名'[, 参数])`或`commit({ type: 'mutation方法名'[, 参数的项: 值] })`触发。
    2. 必须是同步函数。

    - <details>

        <summary><code>mapMutations</code></summary>

        返回对象，用于组件`methods`方法的简写（`method1 (data) { this.$store.commit('mutate1', data) }`）。

        ```javascript
        // 组件中
        import { mapMutations } from 'vuex'

        new Vue({
          methods: {
            ...mapMutations({ // 方法都可传参数。e.g. this.method1(参数)
              method1: 'mutate1',
              method2: 'mutate2',
            }),
            // 或
            ...mapMutations([ // methods使用与mutations方法相同名字可用数组
              'mutate1',
              'mutate2'
            ])
          }
        })
        ```
        </details>
4. `actions`

    仅触发mutations，而不直接改变~~state~~。

    1. 通过store调用`dispatch('action方法名'[, 参数])`或`dispatch({ type: 'action方法名'[, 参数的项: 值] })`触发。
    2. 可以进行异步操作。
    3. 第一个参数对象包含：`state`、`getters`、`commit`、`dispatch`（，模块模式还有：`rootState`、`rootGetters`）。

    - <details>

        <summary><code>mapActions</code></summary>

        返回对象，用于组件`methods`方法的简写（`method1 (data) { this.$store.dispatch('act1', data) }`）。

        ```javascript
        // 组件中
        import { mapActions } from 'vuex'

        new Vue({
          methods: {
            ...mapActions({ // 方法都可传参数。e.g. this.method1(参数)
              method1: 'act1',
              method2: 'act2',
            }),
            // 或
            ...mapActions([ // methods使用与actions方法相同名字可用数组
              'act1',
              'act2'
            ])
          }
        })
        ```
        </details>

><details>
>
><summary>非模块模式使用vuex</summary>
>
>```javascript
>import Vue from 'vue'
>import Vuex from 'vuex'
>
>Vue.use(Vuex) // 注入
>
>export default new Vuex.Store({ // 导出Vuex实例
>  state: { // 暴露的state数据
>    state1: 0,
>    state2: 0
>  },
>
>  getters: { // 暴露的state计算数据
>    getters1: (state, getters) => { // 第一个参数是state对象，第二个参数是getters对象（只读）
>      return state.state1
>    },
>    getters2: (state, getters) => {
>      return state.state2 + getters['getters1']
>    },
>    getters3: (state, getters) => { // 成员可以返回方法，若返回方法则不缓存，每次都需要调用执行
>      return () => state.state1 * 2
>    }
>  },
>
>  mutations: {  // 暴露的改变state的方法
>    mutate1 (state, 参数) { // 第一个参数是state对象，第二个参数是commit调用方法的第二个参数
>      // 仅同步操作
>      state.state1++
>    }
>  },
>
>  actions: {  // 暴露的触发mutations的方法（可异步操作，也可返回Promise对象，也可使用async-await，还可触发其他actions）
>    act1 (context, 参数) {  // 第一个参数是类似Vuex.Store实例对象（只读），第二个参数是dispatch调用方法的第二个参数
>      return new Promise((resolve, reject) => {
>        setTimeout(() => {
>          context.commit('mutate1', 参数)
>          resolve()
>        }, 0)
>      })
>    },
>    async act2 (context) {
>      await context.dispatch('act1', 123)  // 等待 act1 完成
>    }
>  }
>})
>
>
>// new Vue({ store: 上面导出的内容 })的实例中通过this.$store访问Vuex实例
>this.$store.state.state1            // 输出state
>this.$store.getters['getters1']     // 输出getters
>this.$store.getters['getters3']()   // 输出getters方法的值
>this.$store.commit('mutate1', 参数)  // 触发mutations
>this.$store.dispatch('act1', 参数)   // 触发actions
>```
></details>

5. 模块方式

    1. 模块内部

        >模块vuex对根vuex均是只读。

        1. getters的第三个参数`rootState`是根state、第四个参数`rootGetters`是根getters
        2. actions的第一个参数`context`的：`rootState`属性是根state、`rootGetters`属性是根getters
        3. **（组件使用）** state需要增加路径：store的`state.模块路径.state名`获取。
        4. 命名空间`namespaced`（主要针对getters、mutations、actions）

            1. `false`（默认）

                **（组件使用）** getters、mutations、actions是注册在全局命名空间，与非模块方式调用相同；无法针对某个模块而使用`mapState/mapGetters/mapActions/mapMutations`的第一个参数或`createNamespacedHelpers`。
            2. `true`

                **（组件使用）** getters、mutations、actions调用要在名称中增加路径：`模块路径/名称`；可以针对某个模块而使用`mapState/mapGetters/mapActions/mapMutations`的第一个参数或`createNamespacedHelpers`。

                - actions的定义内部

                    1. 默认的`commit`和`dispatch`只对本模块；
                    2. 添加`{ root: true }`至第三参数，表示针对根vuex：`commit('mutation方法名', 参数, { root: true })`、`dispatch('action方法名', 参数, { root: true })`
    2. 动态注册`registerModule`、动态卸载`unregisterModule`

- 若在`new`Vue实例时，把（已经`Vue.use(Vuex)`的）Vuex.Store实例通过`store`属性注入，则子组件内就能通过`this.$store`访问此Vuex实例。

>- 建议的业务结构：
>
>    1. 在view层（页面.vue）触发`dispatch`（页面创建钩子触发或用户交互触发）。
>    2. 在store模块内引入异步API模块，在actions内请求异步数据。
>    3. 独立的API模块专门进行请求数据异步。

### [vue-cli](https://github.com/vuejs/vue-cli)
快速构建Vue应用的脚手架，可以使用Vue官方或第三方模板来进行Vue应用的配置，主要包括webpack等工具的配置。

1. 任何放置在public文件夹的静态资源都会被简单的复制，而不经过~~webpack~~。需要通过**绝对路径**来引用。

    >1. 绝对路径：`/images/foo.png`、`http://xxx`
    >2. 相对路径：以`.`、`~`、`@`开头。作为一个模块请求被webpack解析。
2. [环境变量](https://cli.vuejs.org/zh/guide/mode-and-env.html)

    1. 构建时：根据命令额外加载环境变量文件

        >构建时，Node.js环境中的`process.env`都会加入（但没有`BASE_URL`）。

        1. 所有情况 加载 `.env`
        2. `vue-cli-service serve` 加载 `.env.development`
        3. `vue-cli-service build` 加载 `.env.production`
    2. 客户端页面：自动添加环境变量文件中以`VUE_APP_`开头的环境变量

        >除了`VUE_APP_`开头的环境变量之外，还有`NODE_ENV`和`BASE_URL`会自动添加到客户端页面。

        1. 在.js访问：`process.env.VUE_APP_名字/NODE_ENV/BASE_URL`
        2. 在public的.html访问：`<%= VUE_APP_名字/NODE_ENV/BASE_URL %>`

### [nuxt.js](https://github.com/nuxt/nuxt.js)
基于Vue的通用应用框架，把webpack、babel、vue-server-renderer、vue-router、vuex、vue-meta等工具整合在一起，并通过自带的`nuxt.config.js`统一配置，不需要对每个工具进行单独配置。

>框架内的Vue组件都是以**Vue单文件组件**的形式，每一个`pages`目录下的组件都是一个页面。

1. 目录结构

    1. `pages`：页面目录

        Vue单文件组件。目录中的`.vue`文件自动生成对应的路由配置和页面。

        <details>
        <summary><code>pages</code>目录下组件新增几个方法（其他目录下无效）</summary>

        1. `asyncData`

            页面组件被初始化前调用（组件还未创建，无法使用`this`引用组件实例）。`return`的数据与`data`方法返回的数据合并后返回当前页面组件。
        2. `fetch`

            在渲染页面前填充状态（store）的数据。
        3. `head`

            覆盖`nuxt.config.js`的`head`属性。
        4. `layout`

            引用`layout`目录的布局文件。
        5. `middleware`

            引用`middleware`目录的中间件文件。
        6. `scrollToTop`

            控制页面渲染前是否滚动至页面顶部。默认：`false`。
        7. `transition`

            Vue的`<transition>`组件配置。
        8. `validate`

            用于校验动态路由参数的有效性。`return false`则自动加载显示404错误页面。
        </details>
    2. `assets`：待编译资源目录

        默认使用webpack的vue-loader、file-loader、url-loader加载器进行编译的资源，如`脚本（js、jsx、tsx、coffee）`、`样式（css、scss、sass、less）`、`模版（html、tpl）`、`JSON`、`图片`、`字体`文件。

        - 引用方式：组件中HTML引用、ES6引用`~/assets/`

        >对于不需要编译的静态资源可以放在`static`目录。
    3. `static`：静态资源目录

        不需要webpack编译的静态资源。该目录下的文件会映射至项目根路径。

        - 引用方式：组件中HTML引用`/`
    4. `components`：组件目录

        Vue单文件组件。提供给项目中所有组件使用。

        - 引用方式：组件中ES6引用`~/components/`

            <details>
            <summary>任意组件引用<code>components</code>目录下组件的方式</summary>

            ```html
            <template>
              <div>
                ...
                <other-component/>
                ...
              </div>
            </template>

            <script>
              import OtherComponent from '~/components/OtherComponent.vue';

              export default {
                components: {
                  OtherComponent
                },
                ...
              };
            </script>
            ```
            </details>
    5. `plugins`：Vue插件目录

        JS文件。在Vue根应用的实例化前需要运行的Vue插件（Vue添加全局功能）。

        - 引用方式：`nuxt.config.js`中加入`plugins`属性

            <details>
            <summary><code>nuxt.config.js</code>文件引用<code>plugins</code>目录下插件的方式</summary>

            ```javascript
            // nuxt.config.js
            module.exports = {
              plugins: [  // 一般也会配置在vendor.bundle.js中
                '~/plugins/插件文件名',
                { src: '~/plugins/插件文件名', ssr: false }  // ssr设置是否也在服务端运行。true（默认）：在服务端和客户端都运行；false：仅在客户端运行
              ],
              ...
            }
            ```
            </details>
    6. `store`：状态目录

        >若`store`目录存在，则：引入`vuex`->增加`vuex`至vendor->设置Vue根实例的`store`属性。

        1. 创建

            1. 普通方式：

                `store/index.js`导出Vuex.Store实例对象，包含`state`、`getters`、`mutations`、`actions`属性。

                <details>
                <summary>e.g.</summary>

                ```javascript
                // store/index.js
                import Vuex from 'vuex';

                export default () => {
                  return new Vuex.Store({
                    state: {
                      state1: 0
                    },

                    getters: {
                      state2(state, getters) {
                        return state.state1;
                      },
                      state3(state, getters) {
                        return state.state1 * getters['state2'];
                      },
                    },

                    mutations: {
                      mutate1(state, data) {
                        state.state1 += data;
                      }
                    },

                    actions: {
                      act1(context, data) {
                        context.commit('mutate1', data);
                      }
                    }
                  });
                };
                ```
                </details>
            2. 模块方式：

                `store`目录下`index.js`为根vuex对象，其他每个`.js`文件被转换为以文件名命名的状态模块（开启`namespaced`）。都导出`state`、`getters`、`mutations`、`actions`变量。

                <details>
                <summary>e.g.</summary>

                ```javascript
                // store/index.js
                export const state = () => ({
                  num: 0
                });

                export const getters = {
                  num2(state, getters) {
                    return state.num;
                  },
                  num3(state, getters) {
                    return state.num * getters['num2'];
                  }
                };

                export const mutations = {
                  mutateNum(state, data) {
                    state.num += data;
                  }
                };

                export const actions = {
                  actNum(context, data) {
                    context.commit('mutateNum', data);
                  }
                };


                // store/module1.js
                export const state = () => ({
                  state1: 0
                });

                export const getters = {
                  state1(state, getters, rootState, rootGetters) {
                    return state.state1 + rootState.num + rootGetters['num2'];
                  }
                };

                export const mutations = {
                  mutateState1(state, data) {
                    state.state1 += data;
                  }
                };

                export const actions = {
                  actState1(context, data) {
                    context.commit('mutateState1', data + context.rootState.num + context.rootGetters['num2']);
                  }
                };
                ```
        2. 使用

            <details>
            <summary>创建并自动设置Vue根实例的<code>store</code>属性后，即可在组件的实例内使用<code>$store</code></summary>

            ```html
            <!--
            .vue组件中使用实例的$store：
            1. 根vuex
            this.$store.state.状态数据、
            this.$store.getters['状态计算数据']、
            this.$store.commit('mutation名', 第二个参数)、
            this.$store.dispatch('action名', 第二个参数)

            2. 模块vuex
            this.$store.state.模块名.状态数据、
            this.$store.getters['模块名/状态计算数据']、
            this.$store.commit('模块名/mutation名', 第二个参数)、
            this.$store.dispatch('模块名/action名', 第二个参数)
            -->
            <template>
              <button @click="func1">{{ $store.state.counter1 }}</button>
              <button @click="func2">{{ $store.getters['num2'] }}</button>

              <button @click="func3">{{ $store.state.module1.counter3 }}</button>
              <button @click="func4">{{ $store.getters['module1/num4'] }}</button>
            </template>

            <script>
              export default {
                methods: {
                  func1() {
                    this.$store.commit('increment1', 1);
                  },
                  func2() {
                    this.$store.dispatch('increment2', 1);
                  },
                  func3() {
                    this.$store.commit('module1/increment3', 1);
                  },
                  func4() {
                    this.$store.dispatch('module1/increment4', 1);
                  }
                }
              };
            </script>
            ```
            </details>
    7. `layouts`：布局目录

        Vue单文件组件。扩展默认布局（`default.vue`、`error.vue`）或新增自定义布局，在布局文件中添加`<nuxt/>`指定页面主体内容。

        - 引用方式：`pages`目录下组件中加入`layout`属性

            <details>
            <summary><code>pages</code>目录下组件引用<code>layouts</code>目录下布局的方式</summary>

            ```html
            <!-- layouts/布局文件名.vue -->
            <template>
              <div>
                ...
                <nuxt/>
                ...
              </div>
            </template>
            ...
            ```

            ```javascript
            // pages/页面名.vue
            export default {
              layout: '布局文件名',
              ...
            }
            ```
            </details>
    8. `middleware`：中间件目录

        JS文件。路由跳转之后，在页面渲染之前运行自定义函数。执行顺序：`nuxt.config.js` -> `layouts` -> `pages`。

        >可以做权限、UA等判断后执行跳转或其他行为。

        - 引用方式：`nuxt.config.js`文件或`layouts`或`pages`目录下组件中加入`middleware`属性

            <details>
            <summary><code>nuxt.config.js</code>文件或<code>layouts</code>或<code>pages</code>目录下组件引用<code>middleware</code>目录下中间件的方式</summary>

            ```javascript
            // middleware/中间件文件名.js
            export default function (context) {
              // 路由跳转之后，且在每页渲染前运行
            }
            ```

            ```javascript
            // nuxt.config.js
            module.exports = {
              router: {
                middleware: ['中间件文件名']
              },
              ...
            }


            // layouts/布局文件名.vue
            module.exports = {
              middleware: ['中间件文件名'],
              ...
            }


            // pages/页面名.vue
            module.exports = {
              middleware: ['中间件文件名'],
              ...
            }
            ```
            </details>
    9. <details>

        <summary><code>nuxt.config.js</code>：配置文件</summary>

        1. `build`

            配置webpack构建。

            1. `build.vendor`：

                添加进公用插件`vendor.bundle.js`，避免每个页面都打包一次插件，以减少项目bundle的体积。

                <details>
                <summary>e.g.</summary>

                ```javascript
                module.exports = {
                  build: {
                    vendor: ['已安装插件名', '~/plugins/插件文件名']
                  },
                  ...
                };
                ```
                </details>
        2. `css`

            配置全局（所有页面都引用）的样式，包括文件、模块、第三方库。
        3. `dev`

            配置开发/生产模式。
        4. `env`

            配置（客户端和服务端）环境变量。
        5. `generate`

            配置每个动态路由的参数，依据这些路由配置生成对应目录结构的HTML。
        6. `head`

            配置HTML的头部信息。

            >`vmid`为`<meta>`的唯一的标识编号，用于覆盖父组件相同标签。
        7. `loading`

            配置加载组件。
        8. `loadingIndicator`
        9. `mode`

            配置nuxt启动的服务器（开发模式、生产模式）是否使用SSR。使用SSR（默认）：`'universal'`；关闭SSR：`'spa'`。
        10. `modules`

            配置需要添加的nuxt模块。
        11. `plugins`

            配置在Vue根应用的实例化前需要运行的JS插件。
        12. `render`
        13. `rootDir`

            配置根目录。
        14. `router`

            配置覆盖默认的`vue-router`配置。

            1. `router.mode`：

                配置路由模式（`history`或`hash`）。

                <details>
                <summary>e.g.</summary>

                ```javascript
                module.exports = {
                  router: {
                    mode: 'hash' // 默认：'history'
                  },
                  ...
                };
                ```
                </details>
            2. `router.middleware`：

                配置全局中间件。

                <details>
                <summary>e.g.</summary>

                ```javascript
                module.exports = {
                  router: {
                    middleware: ['中间件文件名']
                  },
                  ...
                };
                ```
                </details>
        15. `serverMiddleware`
        16. `srcDir`

            配置源码目录。
        17. `transition`

            配置过渡效果属性的默认值。
        18. `watchers`
        </details>

    >10. 根目录中创建自定义文件夹，放置JS模块，提供给其他文件引用
    >11. `.nuxt`：nuxt构建过程资源目录（不要修改、加入.gitignore）

    ><details>
    >
    ><summary>别名</summary>
    >
    >1. `srcDir`：`~`或`@`
    >2. `rootDir`：`~~`或`@@`
    >
    >- 默认的`srcDir`等于`rootDir`
    ></details>
2. 流程

    <details>
    <summary>流程图</summary>

    ![nuxt流程图](./images/nuxt-1.png)
    </details>

    Vue组件的生命周期钩子中，仅有`beforeCreate`、`created`在客户端和服务端均被调用，其他钩子仅在客户端被调用。
3. 路由

    依据`pages`目录结构和文件自动生成`vue-router`模块的路由配置；在`nuxt.config.js`的`generate`和`router`属性中修改默认路由配置。

    1. 动态路由：`.vue`文件或文件夹增加`_`前缀

        ```text
        pages/
        --| users/
        -----| _id.vue         # <- /users/id动态值
        -----| index.vue       # <- /users/
        # 或
        --| _num/
        -----| comments.vue    # <- /num动态值/comments
        -----| index.vue       # <- /num动态值/
        ```

        ><details>
        ><summary>针对动态路由进行静态化（<code>nuxt generate</code>），需要在服务器设置内部重定向</summary>
        >
        >1. nginx：
        >
        >    ```text
        >    location / {
        >      try_files $uri $uri/ /index.html;
        >    }
        >    ```
        ></details>

        - <details>

            <summary>验证动态路由的参数</summary>

            ```javascript
            export default {
              validate({ params }) {
                return /^\d+$/.test(params.userid); // 校验为数字
              },
              ...
            }
            ```
            </details>
    2. 嵌套路由：新增与`.vue`文件（父级）同名的文件夹存放子级，在父级内添加`<nuxt-child\>`展示子级

        >总是显示父级内容，其中`<nuxt-child/>`根据路由选择子级组件。

        ```text
        pages/
        --| users/
        -----| _id.vue         # 若路由为/users/id动态值，则父级内容的<nuxt-child\>指向此组件
        -----| index.vue       # 若路由为/users/，则父级内容的<nuxt-child\>指向此组件
        --| users.vue          # 父级内容
        ```
    3. 动态嵌套路由：动态的父级嵌套动态的子级

    - 在组件中使用`<nuxt-link>`进行路由跳转（与vue-router的`<router-link>`一致）
4. <details>

    <summary>视图</summary>

    1. `layouts`布局目录
    2. `nuxt.config.js`的`head`属性
    3. 定制HTML模板

        在根目录添加`app.html`，可在其中添加任意静态自定义内容

        ```html
        <!DOCTYPE html>
        <html {{ HTML_ATTRS }}>
          <head>
            {{ HEAD }}
          </head>
          <body {{ BODY_ATTRS }}>
            {{ APP }}
          </body>
        </html>
        ```
    </summary>
5. 命令

    1. `nuxt`：以开发模式启动一个基于vue-server-renderer的服务器
    2. `nuxt build`：利用webpack编译应用，压缩JS、CSS（发布用）
    3. `nuxt start`：以生产模式启动一个基于vue-server-renderer的服务器（依赖`nuxt build`生成的资源）
    4. `nuxt generate`：生成静态化文件，用于静态页面发布

    >增加`-h`参数查看nuxt命令可带参数。
6. 输出至生产环境的方案

    1. SSR：服务器渲染（与开发模式的SSR相同）。
    2. 静态化页面

        1. 针对`动态路由`要设置服务器重定向至`index.html`，用`history`路由模式。
        2. 针对**无法修改服务器设置**或**本地文件打开形式的访问（`file://`）**，用`hash`路由模式。

            >服务器是否设置重定向都可行。

### jQuery与Vue.js对比
1. 做的事情

    1. jQuery

        （旧时代到现在）相对于原生JS，更好的API，兼容性极好的DOM、AJAX操作。面向网页元素编程。
    2. Vue.js

        实现MVVM的数据双向绑定，实现自己的组件系统。面向数据编程。
2. 优劣势对比

    1. jQuery

        1. 兼容性好，兼容基本所有当今浏览器；出现早，学习、使用成本低。
        2. 程序员关注DOM，频繁操作DOM；代码量较多且不好维护、扩展，当页面需求变化之后代码改动难度大。
    2. Vue.js

        1. 程序员关注数据，DOM的操作交给框架；代码清晰、强制规范，利于维护；有自己的组件系统。
        2. 不兼容旧版本浏览器；需要一些学习成本。
