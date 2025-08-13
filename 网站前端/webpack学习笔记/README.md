# [webpack](https://github.com/webpack/webpack)学习笔记

## 目录
1. [webpack性能优化](#webpack性能优化)
1. [原理](#原理)

    1. [流程概括](#流程概括)
    1. [动态加载（按需加载，代码分割，异步组件，路由/组件 懒加载）](#动态加载按需加载代码分割异步组件路由组件-懒加载)
    1. [热更新（hot module replacement，HMR，模块热替换）](#热更新hot-module-replacementhmr模块热替换)
    1. [tree shaking](#tree-shaking)
    1. [scope hoisting（作用域提升）](#scope-hoisting作用域提升)
    1. [文件监听工作原理](#文件监听工作原理)
    1. [webpack-dev-server自动刷新原理](#webpack-dev-server自动刷新原理)
1. [分析输出文件](#分析输出文件)
1. [`webpack.config.js`配置](#webpackconfigjs配置)
1. [Rollup、vite与webpack对比](#rollupvite与webpack对比)

---
### webpack性能优化
0. 升级Node.js、webpack版本
1. 开发优化体验

    1. 多进程多实例：

        1. 构建：

            [thread-loader](https://github.com/webpack-contrib/thread-loader)、~~[happypack](https://github.com/amireh/happypack)~~
        2. 压缩：

            1. [webpack-parallel-uglify-plugin](https://github.com/gdborton/webpack-parallel-uglify-plugin)
            2. 压缩插件（~~[uglifyjs-webpack-plugin](https://github.com/webpack-contrib/uglifyjs-webpack-plugin)~~、[terser-webpack-plugin](https://github.com/webpack-contrib/terser-webpack-plugin)）开启`parallel`参数
    2. 分包

        1. vendor

            优化产物缓存
        2. dll

            优化产物缓存、优化构建缓存。预编译资源模块
    3. 构建缓存

        >提升非首次构建速度。缓存位于：`/node_modules/.cache/`。

        1. loader缓存

            1. [babel-loader](https://github.com/babel/babel-loader)开启`cacheDirectory`缓存参数
            2. webpack的`oneof`配置
        2. 压缩缓存

            ~~[uglifyjs-webpack-plugin](https://github.com/webpack-contrib/uglifyjs-webpack-plugin)~~、[terser-webpack-plugin](https://github.com/webpack-contrib/terser-webpack-plugin)开启`cache`缓存参数（terser-webpack-plugin@5默认强制开启缓存）
        3. plugin缓存

            [hard-source-webpack-plugin](https://github.com/mzgoddard/hard-source-webpack-plugin)
    4. 减少文件搜索范围

        1. 优化`rule.include/exclude`配置（限制loader作用文件夹范围）

            >e.g. 不解析`node_modules`
        2. 优化`resolve.modules`配置（减少模块搜索层级，避免上溯父目录）
        3. 优化`resolve.mainFields`配置（减少依赖库入口文件搜索逻辑）
        4. 优化`resolve.extensions`配置（减少文件后缀搜索范围）
        5. 合理使用`resolve.alias`（减少某些确认依赖库的引用搜索）
        6. 优化`module.noParse`配置（忽略对部分没采用模块化的文件的递归解析处理）
    5. 开启自动刷新

        1. 优化`watchOptions.ignored: /node_modules/`配置（忽略自动刷新的文件监听）
        2. 优化`watchOptions.aggregateTimeout/poll`配置（减少重新构建的频率）
        3. （webpack5删除）`devServer.inline`用`inline`（`<iframe>`）替代默认的websocket
    6. 开启热更新
    7. 开启[Scope Hoisting](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/webpack学习笔记/README.md#scope-hoisting作用域提升)

        webpack.optimize.ModuleConcatenationPlugin
2. 产物优化（自动）

    1. 分包（vendor或dll）

        >HTTP/1考虑分包总量尽量少，有利于减少HTTP排队耗时；HTTP/2+考虑分包尽量细粒度，不太关注数量，有利于更新频率降低和缓存命中。
    2. 压缩JS、CSS
    3. 图片压缩

        [imagemin](https://github.com/imagemin) + [image-webpack-loader](https://github.com/tcoopman/image-webpack-loader)
    4. [tree shaking](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/webpack学习笔记/README.md#tree-shaking)

        1. 无用JS删除（只支持ES6 Module，不支持CommonJS）
        2. 无用CSS删除：

            1. [purgecss](https://github.com/FullHuman/purgecss) + [mini-css-extract-plugin](https://github.com/webpack-contrib/mini-css-extract-plugin)

                >实现原理：通过[jsdom](https://github.com/jsdom/jsdom)加载、[postcss](https://github.com/postcss/postcss)解析所有样式表，通过`document.querySelector`筛选出HTML文件中未找到的选择器。
            2. [uncss](https://github.com/uncss/uncss)

                >实现原理：遍历代码（对所有文件进行匹配），识别已用到的CSS class。
    5. [动态加载](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/webpack学习笔记/README.md#动态加载按需加载代码分割异步组件路由组件-懒加载)
    6. 动态polyfill

        [polyfill-server](https://github.com/Financial-Times/polyfill-service)：根据请求ua返回需要的polyfill

        >其他polyfill的缺点：
        >
        >1. babel-polyfill：200k+，难以单独抽离部分功能
        >2. babel-pligin-trasnform-runtime：不能polyfill原型上方法，不适合业务项目的复杂开发环境
        >3. 自己写：重复造轮子，维护问题

- 分析

    1. 打包速度分析

        1. 粗粒度：webpack的`stats`配置
        2. 细粒度：[speed-measure-webpack-plugin](https://github.com/stephencookdev/speed-measure-webpack-plugin)
    2. 打包产物体积分析：[webpack-bundle-analyzer](https://github.com/webpack-contrib/webpack-bundle-analyzer)

        >分析：包依赖关系、大小占比、gzip开启前后区别。发现解决问题：①依赖同一个库多个版本（考虑依赖升级到相同版本）；②第三方包太大（引入时选型：替换更小的类似库，如：dayjs替换moment；替换成支持tree shaking的库，选择的库需要支持导出es6模块且其依赖库也能导出es6模块，且有sideEffects配置）；③替换没有按需加载的库（引用仅使用到的部分，如：lodash-debounce替换lodash；）；④针对不是每次都要使用的库，考虑动态加载引入（如：`import(xx).then((xx)=>{使用逻辑})`）

---
### 原理
>webpack: module building system.一种基于事件流的编程范例，一系列的插件运行。

1. 所有文件都当作是**模块（module）**：`脚本（js、jsx、tsx、coffee）`、`样式（css、scss、sass、less）`、`模版（html、tpl）`、`JSON`、`图片`、`字体`。

    webpack自身只理解JS和JSON文件，使用`loader（加载器）`，从`entry`出发，递归查找所有类型的文件转换为module。

    - 能使用各种方式表达依赖关系

        CommonJS、ES6 Module、AMD、CSS的`@import`、样式的`url()`、HTML的`<img src="">`。都被转化为CommonJS规范的实现（各种方式引入效果相同）。

        >```js
        >import list from './list';
        >// 等价于：
        >var list = require('./list');
        >```
2. 从`入口起点（entry）`开始进入文件进行解析，（动态打包所有依赖、）递归地构建一个依赖图（dependency graph），这个依赖图包含着应用程序所需的每个module，module通过`loader（加载器）`解析完毕，同时`插件（plugin）`在webpack各生命周期进行额外处理，最终将所有这些module打包为一或多个bundle由浏览器加载。

    1. loader

        模块转换器，一个`输入-输出`函数，用于把module原内容按照需求转换成新内容。递归获得路径所有依赖module，输入给第一个loader，处理完毕输出给下一个loader，直到所有loader链式顺序执行完毕，由最后一个loader输出给Webpack。

        1. 四个阶段：`pre` -> `normal` -> `inline` -> `post`
        2. inline loader跳过其他阶段loader：`!`（跳过`normal`）、`!!`（跳过`pre`、`normal`、`post`）、`-!`（跳过`pre`、`normal`）
        3. 同步loader、异步loader
        4. Webpack会从左到右执行每个loader上的`pitch`方法（如果有）

            `pitch loader`的熔断效果：pitch loader中如果存在非`undefeind`返回值的话，那么上述图中的整个loader chain会发生熔断效果。

        >官网可查看官方各loader的功能和实现原理：[webpack: loaders](https://webpack.docschina.org/loaders/)。
    2. Plugin

        扩展插件，[一个包含`apply`方法的Class（构造函数）](https://github.com/webpack/webpack/blob/main/lib/webpack.js#L71C1-L79)，在Webpack构建流程中的特定时机广播出对应的事件（钩子数：200+），plugin监听事件进行逻辑，在事件处理函数内部进行 `修改上下文属性`或`调用上下文api` 等方式对webpack产生side effect。

        ```js
        class BasicPlugin{
          // 在构造函数中获取用户给该插件传入的配置
          constructor(options){}

          // Webpack 会调用 plugin实例 的 apply 方法传入 compiler 对象
          apply(compiler){
            // 监听 compilation、等各种事件
            compiler.plugin('compilation',function(compilation) {
              // webpack 会将上下文信息以参数或this (compiler 对象) 形式传递给钩子回调，
              // 在回调中可以调用 上下文对象的方法 或 直接修改上下文对象属性，对原定的流程产生 side effect
              // 如：
              //   compilation.addModule：添加模块，可以在原有的 module 构建规则之外，添加自定义模块
              //   compilation.emitAsset：直译是“提交资产”，功能可以理解将内容写入到特定路径
              //   compilation.addEntry：添加入口，功能上与直接定义 entry 配置相同
              //   module.addError：添加编译错误信息
            })
          }
        }

        // 导出 Plugin
        module.exports = BasicPlugin;
        ```

        - Webpack中的plugin机制——compiler，基于[Tapable](https://github.com/webpack/tapable)实现，与打包流程解耦。

            Tapable本质上是提供更方面创建自定义事件和触发自定义事件的库（类似于：[Nodejs的EventEmitter](https://nodejs.org/api/events.html#class-eventemitter)）。
3. 打包后产物

    打包过程：chunk -> bundle。vendor、dll是有特殊缓存逻辑的bundle。

    1. chunk

        是输出的基本单位，默认情况下这些chunks与最终输出的资源一一对应，一个entry会对应打包出一个资源，而通过动态引入语句引入的模块，也对应会打包出相应的资源。块的名字在`entry`设置，数字是id。

        1. entry及entry触达到的模块，组合成一个chunk
        2. 使用动态引入语句引入的模块，各自组合成一个chunk

        >每次修改一个module时，webpack会生成两部分：`manifest.json`（新的编译hash和所有的待更新chunks目录）、更新后的chunks（.js）。
    2. vendor

        >使用`SplitChunksPlugin`进行自动化选择某些资源避免重复依赖。

        独立于经常改动的业务代码，额外提取出chunk成为单独的bundle用于用户缓存（分包）。第三方库。每次构建时都需要进行构建。
    3. dll

        >`DLLPlugin`和`DLLReferencePlugin`配合设置动态链接库（还需要在html中插入），指定资源避免重复依赖。

        独立于经常改动的业务代码，额外提取出chunk成为单独的bundle用于用户缓存（分包）。只有修改了dll引用的内容才需再次构建dll（DllPlugin生成了manifest.json文件，指定需要的依赖，DllReferencePlugin再去引用），缓存了dll分包，提升了构建的速度。

    >vendor和dll二选一即可。

    4. bundle

        多个chunk的最终合并产出物。

        ><details>
        ><summary>引用仓库</summary>
        >
        >1. 若引用仓库，则会按照仓库设置好的路径引用仓库文件（package.json的字段）。
        >2. 若引用仓库中某文件，则会按照该文件的引用链路去引用仓库文件。
        >3. 仓库中没有被引用到的文件不会打包进最终bundle。
        >
        >    e.g. 可以用`import debounce from 'lodash/debounce'`替代`import { debounce } from 'lodash'`，这样最终打包的结果不会引用整个lodash，而只会引用debounce的引用链路文件（可以用[webpack-bundle-analyzer](https://github.com/webpack-contrib/webpack-bundle-analyzer)分析并可视化构建后的打包文件进行对比；也可以直接用[lodash.debounce](https://www.npmjs.com/package/lodash.debounce)单独库替代）。
        ></details>

        <details>
        <summary>bundle中的<code>__webpack_require__</code></summary>

        1. bundle能直接运行在浏览器中的原因在于输出的文件中通过`__webpack_require__`函数定义了一个可以在浏览器中执行的加载函数来模拟Node.js中的`require`语句。
        2. 原来一个个独立的module文件被合并到了一个单独的bundle的原因在于浏览器不能像Node.js那样快速地去本地加载一个个module文件，而必须通过网络请求去加载还未得到的文件。 如果module数量很多，加载时间会很长，因此把所有module都存放在了数组中，执行一次网络加载。
        3. 做了缓存优化：执行加载过的module不会再执行第二次，执行结果会缓存在内存中，当某个module第二次被访问时会直接去内存中读取被缓存的返回值。

        ```js
        // e.g.
        function __webpack_require__(moduleId) {
            // 1.首先会检查模块缓存
            if(installedModules[moduleId]) {
                return installedModules[moduleId].exports;
            }

            // 2. 缓存不存在时，创建并缓存一个新的模块对象，类似Node中的new Module操作
            var module = installedModules[moduleId] = {
                i: moduleId,
                l: false,
                exports: {},
                children: []
            };

            // 3. 执行模块，类似于Node中的：
            // result = compiledWrapper.call(this.exports, this.exports, require, this, filename, dirname);
            modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);

            module.l = true;

            // 4. 返回该module的输出
            return module.exports;
        }
        ```
        </details>
4. 名词解析

    1. Entry：编译入口，webpack编译的起点
    2. Compiler：编译管理器，webpack启动后会创建compiler对象，该对象一直存活直到结束退出

    >1. compiler对象代表了完整的webpack环境配置，启动时一次性建立，配置好所有可操作的设置
    >2. compilation对象代表了一次资源版本构建，当检测到文件变化就触发一个新的compilation

    3. Compilation：单次编辑过程的管理器

        >e.g. `watch: true`时，运行过程中只有一个compiler，但每次文件变更触发重新编译时，都会创建一个新的compilation对象

        Compilation模块会被Compiler用来创建新的编译，Compilation实例负责**处理一次完整的构建过程**，从启动构建到生成输出文件。当Webpack开始一次新的构建时，它会使用已有的Compiler实例创建一个新的Compilation实例。Compilation实例将负责管理和执行构建过程中的所有步骤。每次构建过程生成的所有中间结果，包括依赖关系图、转换过的资源和生成的代码块，都将存储在Compilation对象中，直至最终生成输出文件。

        - 在编译阶段，模块会被：

            1. 加载（loaded）
            2. 封存（sealed）
            3. 优化（optimized）
            4. 分块（chunked）
            5. 哈希（hashed）
            6. 重新创建（restored）
    4. Dependence：依赖对象，webpack基于该类型记录模块间依赖关系
    5. Module：webpack内部所有资源都会以“module”对象形式存在，所有关于资源的操作、转译、合并都是以“module”为基本单位进行的
    6. Chunk：编译完成准备输出时，webpack会将module按特定的规则组织成一个一个的chunk，这些chunk某种程度上跟最终输出一一对应
    7. Loader：资源内容转换器，其实就是实现从内容A转换B的转换器
    8. Plugin：webpack构建过程中，会在特定的时机广播对应的事件，插件监听这些事件，在特定时间点介入编译过程

#### 流程概括
Webpack的运行流程是一个串行的过程，从启动到结束会依次执行以下流程：

1. 初始化参数：

    从配置文件和Shell语句中读取与合并参数，得出最终的参数；
2. 开始编译：

    （用上一步得到的参数初始化Compiler对象，）加载所有配置的`plugin`，执行对象的run方法（开启监听事件），开始执行编译；
3. 确定入口：

    根据配置中的`entry`找出所有的入口文件；
4. 编译模块：

    从入口文件出发，调用所有配置的Loader对module进行翻译，找出该入口module依赖的module，递归直到所有入口依赖的文件都经过Loader处理；最终得到每个module被翻译后的最终内容以及它们之间的依赖关系；

    >遍历AST集合过程中，识别`require/import`之类的导入语句，确定模块对其他资源的依赖关系。
5. 输出资源：

    根据入口和module之间的依赖关系，组装成一个个包含多个module的`Chunk`，再把每个Chunk转换成一个单独的文件加入到输出列表；

    >这步是可以修改输出内容的最后机会。
6. 输出完成：

    根据配置确定输出的路径和文件名，把文件内容写入到文件系统。

- 在以上过程中，Webpack会在特定的生命周期广播出特定的事件，`plugin`在监听到代码编写的事件后会执行特定的逻辑，并且可以调用Webpack提供的API改变Webpack的运行结果。

#### 动态加载（按需加载，代码分割，异步组件，路由/组件 懒加载）
1. 代码使用 ES6 Module的`import()` 或 特别约定的`require` 来告诉webpack支持动态加载

    1. [React通过`<React.Suspense>`、`React.lazy`配合`import()`进行代码分离（动态加载）](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/React学习笔记/README.md#代码分割动态加载)
    2. <details>

        <summary>Vue的异步组件</summary>

        ```js
        Vue.component(
          'async-webpack-example',
          // 这个动态导入会返回一个 `Promise` 对象。
          () => import('./my-async-component')
        )


        Vue.component('async-webpack-example', function (resolve) {
          // 这个特殊的 `require` 语法将会告诉 webpack：
          //   自动将你的构建代码切割成多个包，这些包会通过 Ajax 请求加载
          require(['./my-async-component'], resolve)
        })
        ```
        </details>
    3. 基于路由的动态加载
2. 实现原理

    1. 构建阶段的**代码分离（Code Splitting）**：

        当Webpack构建项目时，它会根据代码分离**配置**将module分组为不同的块（①构建安装使用`@babel/plugin-syntax-dynamic-import`babel配置，②代码遇到`import()`或其他）。每个块都是一个独立的文件，可以被异步加载。
    2. 页面运行至**动态加载**部分时：

        先尝试读取module缓存，若没有，则创建`<scrip>`加载chunk包（JSONP），chunk写入`window.webpackJsonp`并被webpack的module加载体系（`__webpack_require__`）引入执行。返回Promise实例。

        - 动态module的代码存放在`window.webpackJsonp`：

            ```js
            // window.webpackJsonp
            [
              0: [
                ["模块1"],
                {./src/templates/basic/模块1.js: ƒ}
              ],
              1: [
                ["模块2"],
                {./src/templates/basic/模块2.js: ƒ}
              ],
              push: f webpackJsonpCallback(data)
            ]
            ```

        - <details>

            <summary>输出文件中的 实现动态加载方法（JSONP原理）</summary>

            ```js
            var inProgress = {};
            var dataWebpackPrefix = "wepack5-demo:";

            // loadScript function to load a script via script tag
            // url: __webpack_require__.p + __webpack_require__.u(chunkId)
            // done: loading结束方法
            // key: "chunk-" + chunkId
            // chunkId: 路径名、文件名、后缀 组成的字符串
            __webpack_require__.l = (url, done, key, chunkId) => {
              // 使用缓存
              if (inProgress[url]) {
                inProgress[url].push(done);
                return;
              }
              var script, needAttach;
              if (key !== undefined) {
                var scripts = document.getElementsByTagName("script");
                for (var i = 0; i < scripts.length; i++) {
                  var s = scripts[i];
                  if (
                    s.getAttribute("src") == url ||
                    s.getAttribute("data-webpack") == dataWebpackPrefix + key
                  ) {
                    script = s;
                    break;
                  }
                }
              }
              if (!script) {
                needAttach = true;
                script = document.createElement("script");

                script.charset = "utf-8";
                script.timeout = 120;
                if (__webpack_require__.nc) {
                  script.setAttribute("nonce", __webpack_require__.nc);
                }
                script.setAttribute("data-webpack", dataWebpackPrefix + key);
                script.src = url;
              }
              inProgress[url] = [done];
              var onScriptComplete = (prev, event) => {
                // avoid mem leaks in IE.
                script.onerror = script.onload = null;
                clearTimeout(timeout);
                var doneFns = inProgress[url];
                delete inProgress[url];
                script.parentNode && script.parentNode.removeChild(script);
                doneFns && doneFns.forEach((fn) => fn(event));
                if (prev) return prev(event);
              };
              var timeout = setTimeout(
                onScriptComplete.bind(null, undefined, { type: "timeout", target: script }),
                120000,
              );
              script.onerror = onScriptComplete.bind(null, script.onerror);
              script.onload = onScriptComplete.bind(null, script.onload);
              needAttach && document.head.appendChild(script);
            };
            ```
            </details>

#### 热更新（hot module replacement，HMR，模块热替换）
1. 配置

    ```js
    devServer: {
      hot: true,
    },
    plugins: [
      new webpack.HotModuleReplacementPlugin(), // 负责加载热更新清单和chunk，并更新替换模块缓存
    ],
    ```
2. 流程

    1. 服务启动（webpack-dev-server）：

        1. Bundle server（文件服务器，express）
        2. HMR Server（服务端服务，包含websocket）
        3. HMR Runtime（客户端服务，包含websocket）
    2. 浏览器加载页面之后，浏览器端的HMR Runtime 与 服务端的HMR Server 建立websocket连接。
    3. 本地文件变化 -> 通知webpack增量构建，产生：

        1. hash值
        2. manifest.json（包含所有发生变更的module列表）
        3. chunk（.js，增量修改内容）
    4. 产生的hash值通过websocket通知浏览器端的HMR Runtime
    5. 浏览器端的HMR Runtime对比新旧的hash值，若不一致，则ajax获取manifest确定需要改动的module和chunk，再通过JSONP去Bundle server获取最新资源

#### [tree shaking](https://webpack.docschina.org/guides/tree-shaking)
移除JS上下文中的未引用代码（dead-code）行为的术语，最早由rollup实现，后来webpack等广泛跟进实现。

①基于静态分析的原理，通过识别未使用的module、函数、变量等并②打上标记，③然后在压缩阶段利用uglify-js/terser等压缩工具删除这些没有用到的代码（AST裁剪）。

1. 在webpack中开启，必须同时满足：

    1. 针对使用ES6 Module规范编写代码

        ><details>
        ><summary>原因</summary>
        >
        >1. 在CommonJS、AMD、CMD等旧版本的JS模块化方案中，导入导出行为是高度动态，难以预测。
        >2. ES6 Module方案则从规范层面规避这一行为，它要求所有的导入导出语句只能出现在模块顶层，且导入导出的模块名必须为字符串常量（不能修改），所以，ES6 Module下模块之间的依赖关系是高度确定的，与运行状态无关，编译工具只需要对代码做静态分析，就可以从代码字面量中推断出哪些模块值未曾被其它模块使用，这是实现Tree Shaking技术的必要条件。
        ></details>
    2. 配置`optimization.usedExports: true`启动标记功能（**标记哪些`导出`没有被使用**，导出层面，不是模块文件层面）

        >webpack在代码中标记：`/* unused harmony export xxx */`。
    3. 启动代码优化功能（最终由压缩工具删除，如：terser）：

        `mode: 'production'`或`optimization.minimize: true`或`optimization.minimizer: 「数组」`
2. 目标代码

    >虽然Webpack自2.x开始就原生支持Tree Shaking功能，但受限于JS的动态特性与模块的复杂性，直至最新的5.0版本依然没有解决许多代码副作用带来的问题，使得优化效果并不如Tree Shaking原本设想的那么完美，所以需要使用者有意识地优化代码结构，或使用一些补丁技术帮助Webpack更精确地检测无效代码，完成Tree Shaking操作。

    0. 使用ES6 Module规范编写代码

        - 确保代码不会在某些阶段被转换为CommonJS等（babel、TypeScript需要配置产出ES6 Module）。
    1. 通过package.json的`"sideEffects"`标记（`: false`：当前包的所有模块都被标记没有副作用；`[有副作用的文件或文件夹]`：标记有副作用的部分）（**标记若一个导入模块的内容没有被使用，则允许完全跳过这个模块**，整个模块文件层面）

        默认情况下，库的每个模块都是有副作用（默认"sideEffects: true"）。

        >副作用标识（`sideEffects`）比起检测无用的导出（`usedExports`）来说是更有效的优化手段，因为它允许跳过整个子树或者子模块的扫描。
    2. `调用函数`标记无副作用（允许删除这条`调用函数`逻辑）

        1. `/*#__PURE__*/`被放到函数调用之前，用来标记是无副作用的（传到函数中的入参是无法被刚才的注释所标记，需要单独每一个标记才可以）。
        2. webpack开启`optimization.innerGraph: true`
    3. 使用明确表示支持tree shaking的库：

        1. 库提供ES6 Module代码，且其依赖的库也是ES6 Module代码。
        2. 库包含package.json的`"sideEffects"`标记
    4. 构建前不能丢失模块结构

        1. 我们应该保留库产物的模块结构，以便其充分受益于 sideEffects 的优化。
        2. 库产物应该被分割成多个独立的小模块，每个模块只负责一段逻辑。
        3. 在使用代码分割的应用程序中，树摇优化的模块只能在 sideEffects 优化下工作。
        4. 转译库（如：babel、TypeScript）不能丢失模块结构和ES6 Module特性

#### scope hoisting（作用域提升）
分析出模块之间的依赖关系，尽可能的把打散的模块合并到一个函数中去，但前提是不能造成代码冗余。因此只有那些被引用了一次的模块才能被合并。

><details>
><summary>e.g.</summary>
>
>1. 未开启：
>
>    ```js
>    [
>      (function (module, __webpack_exports__, __webpack_require__) {
>        var __WEBPACK_IMPORTED_MODULE_0__util_js__ = __webpack_require__(1);
>        console.log(__WEBPACK_IMPORTED_MODULE_0__util_js__["a"]);
>      }),
>      (function (module, __webpack_exports__, __webpack_require__) {
>        __webpack_exports__["a"] = ('Hello,Webpack');
>      })
>    ]
>    ```
>2. 开启后：
>
>    ```js
>    [
>      (function (module, __webpack_exports__, __webpack_require__) {
>        var util = ('Hello,Webpack');
>        console.log(util);
>      })
>    ]
>    ```
></details>

1. 使用

    1. ES6 Module的静态语法
    2. plugin增加`new require('webpack/lib/optimize/ModuleConcatenationPlugin')()`

#### 文件监听工作原理
1. 定时的去获取**文件的最后编辑时间**，每次都存下最新的最后编辑时间，如果发现当前获取的和最后一次保存的最后编辑时间不一致，就认为该文件发生了变化。配置项中的`watchOptions.poll: 毫秒`用于控制定时检查的周期。

    对于多个文件来说，会对列表中的每一个文件都定时的执行检查（默认情况下Webpack会从配置的Entry文件出发，递归解析出Entry文件所依赖的文件，把这些依赖的文件都加入到监听列表中去）。
2. 当发现某个文件发生了变化时，并不会立刻告诉监听者，而是先缓存起来，收集一段时间的变化后，再一次性告诉监听者。配置项中的`watchOptions.aggregateTimeout: 毫秒` 用于配置这个等待时间。因为我们在编辑代码的过程中可能会高频的输入文字导致文件变化的事件高频的发生，如果每次都重新执行构建就会让构建卡死。

#### webpack-dev-server自动刷新原理
1. （默认）往要开发的网页中注入代理客户端代码（websocket），通过代理客户端去刷新整个页面。

    会为每个chunk中都注入代理客户端的代码（因为不确定页面会加载哪些chunk，索性粗暴解决）。
2. （webpack5删除）把要开发的网页装进一个`<iframe>`中，通过刷新`<iframe>`去看到最新效果。

>其他方法：借助浏览器扩展去通过浏览器提供的接口刷新。

---
### 分析输出文件
1. <details>

    <summary>源文件、配置文件</summary>

    1. `webpack.config.js`

        ```js
        // "webpack": "^5.76.2",
        // "webpack-cli": "^5.0.1"
        module.exports = {
          entry: "./src/index.js",
          output: {
            filename: "main.js",
            path: require("path").resolve(__dirname, "dist"),
          },
          mode: "development",
          module: {},
          plugins: [],
          devtool: false,
        };
        ```
    2. 源文件

        ```js
        // ./src/index.js
        const a = require("./a");

        require("./c");

        console.log("index.js");

        module.exports = function Index() {
          return a;
        };
        ```

        ```js
        // ./src/a.js
        const b = require("./b");
        console.log(b);

        const d = require("./d");
        console.log(d);

        module.exports = {
          fileName: "a..js",
        };
        ```

        ```js
        // ./src/b.js
        require("./c");

        console.log("b..js");
        ```

        ```js
        // ./src/c.js
        console.log("i am a not export c..js");
        ```

        ```js
        // ./src/d.js
        console.log("d..js");

        exports.fileName = "d..js";
        ```
    </details>

2. 输出文件

    ```js
    (() => {
      // webpackBootstrap
      var __webpack_modules__ = {
        "./src/a.js": (module, __unused_webpack_exports, __webpack_require__) => {
          const b = __webpack_require__("./src/b.js");
          console.log(b);

          const d = __webpack_require__("./src/d.js");
          console.log(d);

          module.exports = {
            fileName: "a..js",
          };
        },

        "./src/b.js": (
          __unused_webpack_module,
          __unused_webpack_exports,
          __webpack_require__
        ) => {
          __webpack_require__("./src/c.js");

          console.log("b..js");
        },

        "./src/c.js": () => {
          console.log("i am a not export c..js");
        },

        "./src/d.js": (__unused_webpack_module, exports) => {
          console.log("d..js");

          exports.fileName = "d..js";
        },

        "./src/index.js": (
          module,
          __unused_webpack_exports,
          __webpack_require__
        ) => {
          const a = __webpack_require__("./src/a.js");

          __webpack_require__("./src/c.js");

          console.log("index.js");

          module.exports = function Index() {
            return a;
          };
        },
      };

      // The module cache
      var __webpack_module_cache__ = {};

      // The require function
      function __webpack_require__(moduleId) {
        // Check if module is in cache
        var cachedModule = __webpack_module_cache__[moduleId];
        if (cachedModule !== undefined) {
          return cachedModule.exports;
        }
        // Create a new module (and put it into the cache)
        var module = (__webpack_module_cache__[moduleId] = {
          // no module.id needed
          // no module.loaded needed
          exports: {},
        });

        // Execute the module function
        __webpack_modules__[moduleId](module, module.exports, __webpack_require__);

        // Return the exports of the module
        return module.exports;
      }

      // startup
      // Load entry module and return exports
      // This entry module is referenced by other modules so it can't be inlined
      var __webpack_exports__ = __webpack_require__("./src/index.js");
    })();
    ```

### [`webpack.config.js`配置](https://webpack.docschina.org/configuration/)
>只需要大概明白Webpack原理和核心概念去判断选项大致属于哪个大模块下，再去查详细的使用文档。
>
>- 想让源文件加入到构建流程中去被Webpack控制，配置`entry`。
>- 想自定义输出文件的位置和名称，配置`output`。
>- 想自定义寻找依赖模块时的策略，配置`resolve`。
>- 想自定义解析和转换文件的策略，配置`module`，通常是配置`module.rules`里的Loader。
>- 其它的大部分需求可能要通过Plugin去实现，配置`plugin`。

<details>
<summary><del>简单实践的配置</del></summary>

1. `entry`：定义整个编译过程的起点

    1. 单入口：`string`
    2. 多入口：`Record<string, string>`
2. `output`：定义整个编译过程的终点

    1. 占位符（[webpack: Template strings](https://webpack.docschina.org/configuration/output/#template-strings)）

        >所有输出名字的地方都可以用。

        1. `[name]`：entry名
        2. `[hash]`：hash值
        3. `[ext]`：资源后缀名
        4. `[path]`：路径
3. `module`：定义模块（文件）的处理方式

    1. `.rules`（数组，每一项是一个对象）

        >rules数组执行有顺序之分，数组逆序链式执行。执行完毕一个loader之后，返回的内容再传入下一个loader进行执行。

        loader，接受源文件，返回转化后的module。处理webpack无法解析的文件。

        1. `.test`：指定匹配规则。

            webpack根据正则表达式，来确定应该查找哪些文件，并将其提供给指定的loader。
        2. `.use`：指定使用的loader、参数（字符串或数组）。

            >`use`执行有顺序之分，数组逆序链式执行。执行完毕一个loader之后，返回的内容再传入下一个loader进行执行。
4. `plugin`：对编译完成后的module（loader处理之后）进行二度加工，增强webpack功能

    >每个plugin都会绑定各种webpack生命周期钩子进行执行plugin内某些具体内容，用户一般不用关注各plugins之间执行顺序。

    用于bundle文件的优化、资源管理、环境变量注入。作用于整个构建过程。进行任何loader无法处理的事情。

    1. 在构建结束后向项目代码中注入变量：`new webpack.DefinePlugin({键-值})`

        若项目代码中要使用的Node.js的环境变量，建议都用此方式注入后再使用，而不要直接使用由webpack额外处理的Node.js环境变量。
5. `mode`：使用相应环境的内置优化

    `none`、`development`、`production`（默认）
6. 监听文件从而重新构建

    1. `watch`
    2. `watchOptions`：监听参数
7. `devServer`

    [webpack-dev-server](https://github.com/webpack/webpack-dev-server)、webpack-hot-middleware、webpack-dev-middleware，可以写入内存中（而不是写入磁盘、看不见文件）编译并serve资源来提高性能。

    1. `static`（替代 ~~`contentBase`~~）
    2. `hot`（添加`new webpack.HotModuleReplacementPlugin()`配合）：[热更新](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/webpack学习笔记/README.md#热更新hot-module-replacementhmr模块热替换)

        >利用websocket实现，websocket-server识别到html、css和js的改变，就向websocket-client发送一个消息，websocket-client判断若是html和css则操作dom，实现局部刷新，若是js则重载页面。
8. `resolve`

    1. `.alias`：定义路径的别名

        1. 普通别名

            ```js
            // webpack
            alias: {
              xyz: path.resolve(__dirname, 'path/to/file.js')
            }


            // 使用
            import Test1 from 'xyz/file.js'; // 匹配
            import Test2 from '../xyz/file.js'; // 不匹配
            ```
        2. 精准匹配别名（`「名字」$`）

            ```js
            // webpack
            alias: {
              xyz$: path.resolve(__dirname, 'path/to/file.js')
            }


            // 使用
            import Test2 from 'xyz'; // 精确匹配，所以 path/to/file.js 被解析和导入
            import Test3 from 'xyz/file.js'; // 非精确匹配，触发普通解析
            ```
    2. `.extensions`（数组）：能够使用户在引入module时不带扩展，自动查找数组中的后缀（若赋值则覆盖默认数组）

- 可以导出数组，分别进行配置，串行执行多个webpack任务（如：前后端同构任务）

    ```js
    module.exports = [配置1, 配置2]
    ```

>还未找到满足 css和img放置指定地点 且 html和css都能正确引入图片路径 的配置方案。

</details>

### [Rollup](https://github.com/rollup/rollup)、[vite](https://github.com/vitejs/vite)与webpack对比
App级别的应用（开发、打包）——webpack。JS库级别的应用（打包）——Rollup。现代浏览器快速开发体验（开发）——vite。

1. Rollup：

    1. 打包结果文件很小，几乎没多余代码（Tree Shaking）；执行很快；可方便输出CommonJS、ES6 Module、IIFE（用于`<script>`引用）格式。不支持代码分离。
    2. 功能不如webpack完善，配置、使用更加简单。
    3. 原生只支持ES6 Module格式的代码才可以打包（可以用插件[@rollup/plugin-commonjs](https://github.com/rollup/plugins/tree/master/packages/commonjs)导入CommonJS代码）。
    4. 适合纯JS的库或组件。

    - 优点：产物格式极为干净，产物结果对 tree shaking 非常友好。
    - 缺点：产物优化能力薄弱，尤其是缺失 Bundle Splitting 等能力导致业务很难做精细的优化；CommonJS支持不佳（CommonJS转ES6无法做到完全兼容）；不支持HMR，watch表现一般。
2. webpack

    1. 拥有强大、全面的功能、高度可配置，更好的社区。
    2. 针对各种类型的文件（loader支持）。可以处理多个入口文件和复杂的依赖关系。可以高度定制和扩展Webpack的功能。
    3. 在进行资源打包时会产生很多冗余的代码（webpack内部结构、模块化方案、`__webpack_require__`）。
    4. 适合复杂项目。

    - 最大优点：扩展能力极强，能够支持几乎所有的构建场景。
    - 缺点：黑盒化严重，调试能力差，业务碰到构建相关的问题，几乎都很难自行排查；性能问题。
3. vite（`/vit/`）

    1. 目前存在这种开发和构建之间的不一致性

        1. 开发环境中，利用现代浏览器现在已经支持ES6 Module的import能力，遇到import就会发送一个HTTP请求去加载ES6 Module文件，整个过程中没有对文件进行打包编译。在开发环境使用了ESBuild（go）进行预构建（提高页面加载速度、将CommonJS/UMD转换为ESM格式）

            ><details>
            ><summary>Vite通过在一开始将应用中的模块区分为<strong>依赖</strong>和<strong>源码</strong>两类，改进了开发服务器启动时间。</summary>
            >
            >1. 依赖
            >
            >    大多为在开发时不会变动的纯 JavaScript。一些较大的依赖（例如有上百个模块的组件库）处理的代价也很高。依赖也通常会存在多种模块化格式（例如 ESM 或者 CommonJS）。
            >
            >    Vite将会使用`esbuild`预构建依赖。esbuild 使用 Go 编写，并且比以 JavaScript 编写的打包器预构建依赖快 10-100 倍。
            >
            >    利用HTTP头的`Cache-Control: max-age=31536000,immutable`进行强缓存。
            >2. 源码
            >
            >    通常包含一些并非直接是 JavaScript 的文件，需要转换（例如 JSX，CSS 或者 Vue/Svelte 组件），时常会被编辑。同时，并不是所有的源码都需要同时被加载（例如基于路由拆分的代码模块）。
            >
            >    Vite 以 `原生 ESM` 方式提供源码。这实际上是让浏览器接管了打包程序的部分工作：Vite 只需要在浏览器请求源码时进行转换并按需提供源码。根据情景动态导入代码，即只在当前屏幕上实际使用时才会被处理。
            >
            >    利用HTTP的`304 Not Modified`进行协商缓存。
            ></details>

            快速的冷启动能力，提供了快速的开发体验。在开发阶段使用原生ES6 Module直接引入模块，而不需要像Webpack和Rollup一样进行打包，从而提供了更快的热重载和构建速度。
        2. 生产环境中，使用了Rollup打包

            >1. 因为每个模块引用都需要ES6 module的的网络请求，网络请求开销大，所以生成环境还是使用打包的方式。
            >2. 因为Vite目前的插件API与使用esbuild作为打包器并不兼容，尽管esbuild速度更快，所以Vite采用了Rollup灵活的插件API和基础建设
    2. 适用于中小型项目，特别是基于现代浏览器的单页应用（SPA）或中小型网站开发。

    - 缺点：开发模式，每个模块引用都需要ES6 module的的网络请求，网络请求开销大（尤其是HMR时）；目前存在这种开发和构建之间的不一致性。

>4. [esbuild](https://github.com/evanw/esbuild)
>
>    **GoLang**编写的**快速**JS、TS打包器，支持CommonJS（是rollup的很好替代品）。
>5. [Parcel](https://github.com/parcel-bundler/parcel)
>
>    **零配置**的打包工具，适用于小型项目、静态网页或需要快速上手的场景。
>6. [Bun](https://github.com/oven-sh/bun)
>
>    是像Node.js、Deno一样的现代**JS运行时**。旨在无感替代现有的JS运行时（主要替代Node.js）并成为 浏览器外执行JS 的主流环境，为用户带来性能和复杂性的提升的同时，以更好更简单的工具提高开发者的效率。和传统的Node.js这种传统的JS运行时不同，**Bun.js直接内置了打包器、转译器、任务运行器和npm客户端**，这意味着你不再需要安装Webpack/Rollup/esbuild/Snowpack/Parcel/Rome/swc/babel就可以直接运行TypeScript、JSX。另外，Bun.js原生支持了数百个Node.js和Web API。Zig编写。
>7. [Turbopack](https://turbo.build/pack/docs)
>
>    针对JS和TS优化的增量打包器，**Rust**编写。高度优化的机器代码和低级增量计算引擎，可以**缓存**到单个函数的级别。一旦Turbopack执行了一项任务，它就再也不会这样做了。特点是快。
>8. Rspack
>
>    **Rust**编写的Web构建工具，意在用更快、更直接的方式取代Webpack。
>9. ~~Grunt~~
>
>    是一个任务执行者（和npm中`package.json`的`scripts`类似，相当于其进化版，弥补其不足），大量现成的插件封装了常见的任务，也能管理任务之间的依赖关系，自动化执行依赖的任务，每个任务的具体执行代码和依赖关系写在配置文件`Gruntfile.js`。
>
>    >缺点是集成度不高，要写很多配置后才可以用，无法做到开箱即用。
>9. ~~gulp~~
>
>    基于流的自动化构建工具（是Grunt的加强版，增加了监听文件、读写文件、流式处理的功能）。
>
>    >缺点是和Grunt类似，集成度不高，要写很多配置后才可以用，无法做到开箱即用。
>9. ~~Fis3~~
>
>    集成了Web开发中的常用构建功能，一个完整解决方案。
>
>    >已不再更新维护，不支持新版本Node.js。
>9. ~~Browserify~~
>
>    模块打包工具，把CommonJS模块化代码打包成浏览器能运行的代码。
