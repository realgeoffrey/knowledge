# Vue.js学习笔记

### jQuery与Vue.js对比
1. 做的事情

    1. jQuery

        （旧时代到现在）相对于原生JS，更好的API，兼容性极好的DOM、AJAX操作。
    1. Vue.js

        实现MVVM的数据双向绑定，实现自己的组件系统。
2. 优劣势对比

    1. jQuery

        1. 兼容性好，兼容基本所有当今浏览器；出现早，学习、使用成本低。
        2. 程序员关注DOM，频繁操作DOM；代码量较多且不好维护，当页面需求变化之后代码改动难度大。
    2. Vue.js

        1. 程序员关注数据，DOM的操作交给框架；代码清晰，利于维护；有自己的组件系统。
        2. 不兼容旧版本浏览器；需要一些学习成本。

### [Vue官方教材](https://cn.vuejs.org/v2/guide/)
1. 单向数据流（实现双向绑定效果），响应式

    编写的代码不关注底层逻辑，只关注因**单向数据流**实现的**双向绑定**效果（Vue实例、组件间都是单向数据流）。

    1. 重用DOM
    
        1. 当没有`key`属性、或`key`属性相同时：最大化DOM重用。
        2. 切换的DOM的`key`属性不同：不重用DOM。
    2. Vue实例代理`data`、`methods`的属性内容，可以直接修改或调用；也有以`$`开头的实例属性（如`$el`、`$data`、`$watch`）。

        只有已经被代理的内容是响应的，值的任何改变会触发视图的重新渲染。

        1. 导致试图更新：

            1. 数组的变异方法：`push`、`pop`、`shift`、`unshift`、`splice`、`sort`、`reverse`。
            2. 数组赋值。
            3. 插值：`Vue.set(数组, 索引, 新值)`。
            4. 改变数组长度：`数组.splice(新长度)`。
        2. 无法检测数组变动：

            1. 直接数组索引赋值。
            2. 直接修改数组长度。
    3. 慎用箭头函数，`this`的指向无法按预期指向Vue实例。
    4. 因为HTML不区分大小写，所以大/小驼峰式命名的JS内容，在HTML使用时要转换为相应的短横线隔开式。

        >不受限制：JS字符串模版、`.vue`组件。
2. 模板插值

    1. 支持JS表达式，不支持~~语句~~、~~流控制~~。

        ```html
        <!-- e.g. -->
        {{ number + 1 }}
        {{ ok ? 'YES' : 'NO' }}
        {{ message.split('').reverse().join('') }}
        <div v-bind:id="'list-' + id"></div>
        ```
    2. 只能访问部分全局内容。
    3. 作用域在所属Vue实例（组件也是Vue实例）中。
    4. `<slot>`用于父级向子组件插入内容。
    5. 所有渲染结果不包含`<template>`
3. 指令

    指令（Directives）是带有`v-`前缀的DOM的特殊属性。

    1. `:`参数

        指令后的参数用`:`指明。
    2. `v-if`、`v-else`、`v-else-if`
    3. `v-for="(值, 键, 索引) in/of Vue属性/整数"`

        >比`v-if`优先级更高。

        - 在组件中使用`v-for`时，必须添加`key`属性。
    4. `v-bind`绑定DOM属性与表达式的结果。

        >此DOM属性随表达式最终值改变而改变，直接修改此DOM属性值不改变表达式的值。

        `v-bind:`缩写`:`。

        1. 绑定修饰符：
        
            1. `.sync`
        
                - 仅为语法糖：
                
                    `<my-component :foo.sync="bar"></my-component>`
                
                    等价于
                    
                    `<my-component :foo="bar" @update:foo="val => bar = val"></my-component>`
                    
                    - 若要达到效果（同步更新bar），还需要在组件中添加：
                    
                        ```javascript
                        Vue.component('myComponent', {
                          props: ['foo'],
                          template: '<p v-on:click="doIt">{{foo}}</p>',
                          methods: {
                            doIt () {
                              this.$emit('update:foo', 'new value') // 触发父级事件，父级事件改变值，再传入子组件
                            }
                          }
                        })
                        ```
        2. 特殊的DOM属性：
        
            1. 绑定`class`
    
                1. `v-bind:class="{class名: Vue属性[, class名: Vue属性]}"`
                2. `v-bind:class="Vue属性"`
                3. `v-bind:class="[Vue属性[, Vue属性]]"`
                4. `v-bind:class="[Vue属性 ? Vue属性 : ''[, Vue属性]]"`
                5. `v-bind:class="[{class名: Vue属性}[, Vue属性]]"`
            2. 绑定`style`
    
                >自动添加样式前缀。
    
                1. `v-bind:style="{css属性: Vue属性[, css属性: Vue属性]}"`
                2. `v-bind:style="Vue属性"`
                3. `v-bind:style="[Vue属性[, Vue属性]]"`
                4. 多重值
        3. 传递给子组件DOM属性的值类型
        
            ```html
            <!-- 传递字符串 -->
            <my-component some-prop="1">传递字符串'1'</my-component>
            <my-component some-prop="a">传递字符串'a'</my-component>

            <!-- 传递表达式的值 -->
            <my-component v-bind:some-prop="1">传递表达式：1（Number）</my-component>
            <my-component v-bind:some-prop="'1'">传递表达式：'1'（String）</my-component>
            <my-component v-bind:some-prop="a">传递表达式：a（变量是什么类型就是什么类型）</my-component>
            ```
    5. `v-on`事件处理

        `v-on:`缩写`@`。

        1. 事件修饰符：

            可同时使用，但改变顺序会产生不同效果。
            
            1. `.stop`、`.prevent`、`.capture`、`.self`、`.once`
            2. `.enter`、`.tab`、`.delete`、`.esc`、`.space`、`.up`、`.down`、`.left`、`.right`、`.ctrl`、`.alt`、`.shift`、`.meta`、`.数字`
            3. `.left`、`.right`、`.middle`
            4. `.native`

                组件监听原生事件。
        2. `$event`事件变量
        3. 自定义事件
        
            仅定义在子组件引用上，只能由子组件内部`$emit`触发，然后调用父级方法，再通过改变父级属性去改变子组件的`props`或置换组件。
    6. `v-model`表单

        >忽略表单元素上的`value`、`checked`、`selected`等初始值，而仅通过Vue实例赋值。

        1. 表单修饰符：
        
            `.lazy`、`.number`、`.trim`
        2. 仅针对部分元素：`<input>`、`<textarea>`、`<select>`、组件
        3. 仅为语法糖：

            1. 普通DOM

                `<input v-model="bar">`

                等价于

                `<input v-bind:value="bar" v-on:input="bar = $event.target.value">`
            2. 组件

                `<my-input v-model="bar"></my-input>`

                等价于（默认：属性绑定为`value`、事件绑定为`input`）

                `<my-input v-bind:value="bar" v-on:input="bar = arguments[0]"></my-input>`

                - 若要达到效果（双向数据绑定），还需要在组件中添加：

                    ```javascript
                    Vue.component('myInput', {
                      props: ['value'],
                      template: '<input v-bind:value="value" v-on:input="updateValue($event)">',
                      methods: {
                        updateValue (e) {
                          this.$emit('input', e.target.value) // 触发父级事件，父级事件改变值，再传入子组件
                        }
                      }
                    })
                    ```
    7. `v-once`一次性插值，不再双向绑定数据
    8. `v-html`输入真正HTML

        - 与其他插值（如模板插值）的区别：

            1. `v-html`是`innerHTML`。
            2. 其他是`innerText`。
    9. `.`修饰符

        使用在`v-on`、`v-bind`、`v-module`后面。
    10. `|`过滤器，参数带入函数运行出结果

        >在实例中用`filters`定义，支持过滤器串联。
    11. `v-show`

        总是渲染出DOM，根据值切换`display`值。

        >不支持`<template>`、不支持`v-else`。
4. Vue实例的属性：

    `new Vue(对象)`

    1. `el`（字符串）：选择器
    2. `data`（对象）：数据
    3. `methods`（对象）：可调用方法
    4. `computed`（对象）：自动依赖而计算

        默认是`getter`，也可以设置`getter`+`setter`。
    5. `watch`（对象）：被watch的属性改变而执行
    6. `filters`（对象）：过滤器
    7. `components`（对象）：局部注册组件
    8. 生命周期钩子

        1. `beforeCreate`
        2. `created`
        3. `beforeMount`
        4. `mounted`
        5. `beforeUpdate`
        6. `updated`
        7. `activated`
        8. `deactivated`
        9. `beforeDestroy`
        10. `destroyed`
5. 组件

    >所有组件都是被扩展的Vue实例：`new (Vue.extend({对象}))()`。

    1. 组件属性：

        1. `template`（字符串）：组件的字符串模板

            - 作用域：

                `template`的字符串模板内容为本组件作用域，父级引用的DOM（包括子组件引用）为父级作用域。
            - 内容分发

                使用`<slot>`可在子组件内部插入父级引入的内容。

                1. 模板的`<slot>`元素内容，仅当父级引用的子组件元素内部为空时才展示。
                2. 具名

                    - 父级引用子组件，在元素内部添加的标签的DOM属性`slot="字符串"`
                    - 组件模板：`<slot name="字符串">`
                3. 作用域插槽

                    - 父级引用子组件元素内部的内容为：`<template scope="临时变量">{{临时变量.组件属性}}</template>`

                        >`<template>`使用`scope`属性时，不要同时使用`v-if`。
                    - 组件模板：`<slot 组件属性="字符串">`或`<slot v-bind:组件属性="表达式">`
        2. `props`

            接受父级传递内容。

            1. （数组）：接受的DOM属性
            2. （对象）：`接受的DOM属性: 验证`

                - 验证：

                    1. 字符串
                    2. 数组
                    3. 对象（type、required、default、validator）
        3. `data`（方法）：`return`数据对象

            >`v-for`循环的每个实例都调用创建一份。
        4. `model`（对象，包含`prop`、`event`）：修改`v-model`默认使用的属性和事件
    2. 注册组件方式：

        >要确保在初始化Vue实例之前注册了组件。

        1. 全局

            `Vue.component('组件元素名', 对象)`
        2. 局部

            ```
            // Vue实例
            new Vue({
                components: {
                    '组件元素名': 对象
                }
            })
            ```
    3. 组件命名：
    
        >W3C规定的组件命名要求：小写，且包含一个`-`。
        
        1. JS注册组件或`props`：
        
            短横线隔开式（kebab-case）、小驼峰式（camelCase）、大驼峰式（PascalCase）。
        2. HTML中：
        
            1. 仅能使用短横线隔开式（把大/小驼峰式用`-`隔开单词代替）。
            2. 在JS字符串模版、`.vue`组件，可以用向下替代。
            
                ```html
                <!-- HTML必须是短横线隔开式 -->
                1. <kebab-cased-component></kebab-cased-component>
                2. <camel-cased-component></camel-cased-component>
                3. <pascal-cased-component></pascal-cased-component>

                <!-- 在JS字符串模版、.vue组件额外可以使用 -->
                1. 无
                2. <camelCasedComponent></camelCasedComponent>
                3. <pascalCasedComponent></pascalCasedComponent>
                3. <PascalCasedComponent></PascalCasedComponent>
                
                 <script>
                 // 注册的组件
                 new Vue({
                   components: {
                     'kebab-cased-component': { /* ... */ },
                     camelCasedComponent: { /* ... */ },
                     PascalCasedComponent: { /* ... */ }
                   }
                 })
                 </script>
                ```
    4. 使用组件：

        1. `<组件名></组件名>`

            >不会导致渲染出错的方式：JS字符串模版、`.vue`组件。
        2. `<标签 is="组件名"></标签>`
        3.  `<component v-bind:is="表达式"></component>`动态组件
        
            `表达式`内容变化去获取Vue实例的`data`的属性值：①值是一个类似局部组件对象；②值是字符串，对应`components`同属性名组件。

            - `<keep-alive>`包裹，保留它的状态或避免重新渲染。
    5. 通信

        1. 父子组件间的通信

            组件有自己独立的作用域：父子组件间、Vue实例间作用域独立，可以访问到互相依赖关系（`$parent`、`$children`），但是不允许通过依赖获取、修改数据。

            1. 父->子：通过`props`向下传递初始化数据给子组件实例（不出现在DOM中）
            
                >仅添加在DOM上而不在`props`声明，则仅添加到子组件最外层的DOM属性，不传入子组件。其中`class`和`style`属性会合并，其他属性会覆盖。

                1. `props`是单向绑定的：当父级的属性变化时，将传导给子组件，不会反过来。
                
                    每次父组件更新时，子组件的所有prop都会更新为最新值。
                2. 不应该在子组件内部改变`props`，定义一个局部变量（`data`），用`props`去初始化并接受子组件的数据变动。
                
                    ```javascript
                    // good
                    Vue.component(
                      'myComponent',
                      {
                        props: ['father'],
                        data () {
                          return { son: this.father }
                        },
                        template: '<div>{{son}}</div>'
                      }
                    )

                    // bad
                    Vue.component(
                      'myComponent',
                      {
                        props: ['father'],
                        template: '<div>{{father}}</div>'
                      }
                    )
                    
                    ```

                >注意避免**引用数据类型**导致的子组件改变父级。
            2. 子->父：通过`$emit`向上传递事件、参数

                1. 在父级引用子组件处添加`v-on:自定义事件1="父方法"`监听。
                2. 在子组件添加`this.$emit('自定义事件1', 参数)`向上传递。
        2. 非父子组件通信

            1. 在简单的场景下，可以使用一个空的Vue实例作为中央事件总线。
            
                ```javascript
                var bus = new Vue()
 
                // 触发组件 A 中的事件
                bus.$emit('事件名', 传参)
 
                // 在组件 B 创建的钩子中监听事件
                bus.$on('事件名', function (para) {/* ... */})
                ```
            2. 或专门状态管理模式，如[vuex](https://github.com/vuejs/vuex)。
        - 组件的API来自三部分

            `<my-component :子属性="父属性" @事件="父方法"><标签 slot="名字">内容</标签></my-component>`

            1. `props`：允许外部环境传递数据给组件。
            2. `events`：允许从外部环境在组件内触发副作用。
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

### vue-router
>使用Charles代理到本地dev环境（map remote），要保证被代理和代理的路径相同，才能让路由正确。