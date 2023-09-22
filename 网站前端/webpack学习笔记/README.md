# [webpack](https://github.com/webpack/webpack)学习笔记

## 目录
1. [`webpack.config.js`配置](#webpackconfigjs配置)
1. [webpack构建优化](#webpack构建优化)
1. [总结](#总结)

    1. [原理](#原理)
1. [分析输出文件](#分析输出文件)
1. [动态加载](#动态加载)
1. [热更新（hot module replacement，HMR，模块热替换）](#热更新hot-module-replacementhmr模块热替换)
1. [tree shaking](#tree-shaking)
1. [Rollup、vite与webpack对比](#rollupvite与webpack对比)

---

### `webpack.config.js`配置
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

        loader，接受源文件，返回转化后的模块。处理webpack无法解析的文件。

        1. `.test`：指定匹配规则。

            webpack根据正则表达式，来确定应该查找哪些文件，并将其提供给指定的loader。
        2. `.use`：指定使用的loader、参数（字符串或数组）。

            >`use`执行有顺序之分，数组逆序链式执行。执行完毕一个loader之后，返回的内容再传入下一个loader进行执行。
4. `plugin`：对编译完成后的模块（loader处理之后）进行二度加工，增强webpack功能

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

            ```javascript
            // webpack
            alias: {
              xyz: path.resolve(__dirname, 'path/to/file.js')
            }


            // 使用
            import Test1 from 'xyz/file.js'; // 匹配
            import Test2 from '../xyz/file.js'; // 不匹配
            ```
        2. 精准匹配别名（`「名字」$`）

            ```javascript
            // webpack
            alias: {
              xyz$: path.resolve(__dirname, 'path/to/file.js')
            }


            // 使用
            import Test2 from 'xyz'; // 精确匹配，所以 path/to/file.js 被解析和导入
            import Test3 from 'xyz/file.js'; // 非精确匹配，触发普通解析
            ```
    2. `.extensions`（数组）：能够使用户在引入模块时不带扩展，自动查找数组中的后缀（若赋值则覆盖默认数组）

- 可以导出数组，分别进行配置，串行执行多个webpack任务（如：前后端同构任务）

    ```javascript
    module.exports = [配置1, 配置2]
    ```

>还未找到满足 css和img放置指定地点 且 html和css都能正确引入图片路径 的配置方案。

### webpack构建优化
1. 打包速度分析

    1. 粗粒度：webpack的`stats`配置
    2. 细粒度：[speed-measure-webpack-plugin](https://github.com/stephencookdev/speed-measure-webpack-plugin)
2. 打包产物体积分析：[webpack-bundle-analyzer](https://github.com/webpack-contrib/webpack-bundle-analyzer)
3. 构建优化

    1. 升级Node.js、webpack版本
    2. 多进程多实例：

        1. 构建：

            [thread-loader](https://github.com/webpack-contrib/thread-loader)
        2. 压缩：

            1. [webpack-parallel-uglify-plugin](https://github.com/gdborton/webpack-parallel-uglify-plugin)
            2. 压缩插件（~~[uglifyjs-webpack-plugin](https://github.com/webpack-contrib/uglifyjs-webpack-plugin)~~、[terser-webpack-plugin](https://github.com/webpack-contrib/terser-webpack-plugin)）开启`parallel`参数
    3. 分包

        1. vendor

            优化产物缓存
        2. dll

            优化产物缓存、优化构建缓存。预编译资源模块
    4. 构建缓存

        >提升非首次构建速度。缓存位于：`/node_modules/.cache/`。

        1. loader缓存

            1. [babel-loader](https://github.com/babel/babel-loader)开启`cacheDirectory`缓存参数
            2. webpack的`oneof`配置
        2. 压缩缓存

            ~~[uglifyjs-webpack-plugin](https://github.com/webpack-contrib/uglifyjs-webpack-plugin)~~、[terser-webpack-plugin](https://github.com/webpack-contrib/terser-webpack-plugin)开启`cache`缓存参数（terser-webpack-plugin@5默认强制开启缓存）
        3. plugin缓存

            [hard-source-webpack-plugin](https://github.com/mzgoddard/hard-source-webpack-plugin)
    5. 缩小构建目标

        1. 优化`rule.include/exclude`配置（限制loader作用文件夹范围）

            >e.g. 不解析`node_modules`
        2. 减少文件搜索范围

            1. 优化`resolve.modules`配置（减少模块搜索层级，避免上溯父目录）
            2. 优化`resolve.mainFields`配置（减少依赖库入口文件搜索逻辑）
            3. 优化`resolve.extensions`配置（减少文件后缀搜索范围）
            4. 合理使用`resolve.alias`（减少某些确认依赖库的引用搜索）
    6. 产物优化（自动）

        1. 分包（vendor或dll）
        2. 图片压缩

            [imagemin](https://github.com/imagemin) + [image-webpack-loader](https://github.com/tcoopman/image-webpack-loader)
        3. [tree shaking](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/webpack学习笔记/README.md#tree-shaking)

            1. 无用JS删除（只支持ES6 Module，不支持CommonJS）
            2. 无用CSS删除：

                1. [purgecss](https://github.com/FullHuman/purgecss) + [mini-css-extract-plugin](https://github.com/webpack-contrib/mini-css-extract-plugin)

                    >实现原理：通过[jsdom](https://github.com/jsdom/jsdom)加载、[postcss](https://github.com/postcss/postcss)解析所有样式表，通过`document.querySelector`筛选出HTML文件中未找到的选择器。
                2. [uncss](https://github.com/uncss/uncss)

                    >实现原理：遍历代码（对所有文件进行匹配），识别已用到的CSS class。
        4. 动态polyfill

            [polyfill-server](https://github.com/Financial-Times/polyfill-service)：根据请求ua返回需要的polyfill

            >其他polyfill的缺点：
            >
            >1. babel-polyfill：200k+，难以单独抽离部分功能
            >2. babel-pligin-trasnform-runtime：不能polyfill原型上方法，不适合业务项目的复杂开发环境
            >3. 自己写：重复造轮子，维护问题

---
### 总结
>webpack: module building system.一种基于事件流的编程范例，一系列的插件运行。

1. 能使用各种方式表达依赖关系

    CommonJS、ES6 Module、AMD、CSS的`@import`、样式的`url()`、HTML的`<img src="">`。都被转化为CommonJS规范的实现（各种方式引入效果相同）。

    >```javascript
    >import list from './list';
    >// 等价于：
    >var list = require('./list');
    >```
2. 所有文件都当作是**模块（module）**：`脚本（js、jsx、tsx、coffee）`、`样式（css、scss、sass、less）`、`模版（html、tpl）`、`JSON`、`图片`、`字体`。

    webpack自身只理解JS和JSON文件，使用`loader（加载器）`把所有类型的文件（链式）转换为模块。
3. 从`入口起点（entry）`开始进入文件进行解析，（动态打包所有依赖、）递归地构建一个依赖图（dependency graph），这个依赖图包含着应用程序所需的每个模块，模块通过`loader（加载器）`解析完毕，之后经过`插件（plugin）`二次处理，最终将所有这些模块打包为一或多个bundle由浏览器加载。
4. 打包后产物

    打包过程过程：chunk -> bundle。vendor、dll是有特殊缓存逻辑的bundle。

    1. chunk

        （中间过程的）代码块，块的名字在`entry`设置，数字是id。

        >每次修改一个模块时，webpack会生成两部分：`manifest.json`（新的编译hash和所有的待更新chunks目录）、更新后的chunks（.js）。
    2. vendor

        >使用`SplitChunksPlugin`进行自动化选择某些资源避免重复依赖。

        独立于经常改动的业务代码，额外提取出chunk成为单独的bundle用于用户缓存（分包）。第三方库。每次构建时都需要进行构建。
    3. dll

        >`DLLPlugin`和`DLLReferencePlugin`配合设置动态链接库（还需要在html中插入），指定资源避免重复依赖。

        独立于经常改动的业务代码，额外提取出chunk成为单独的bundle用于用户缓存（分包）。只有修改了dll引用的内容才需再次构建dll（DllPlugin生成了manifest.json文件，指定需要的依赖，DllReferencePlugin再去引用），缓存了dll分包，提升了构建的速度。

        >Dll这个概念借鉴了Windows系统的动态链接库（Dynamic Link Library，DLL）。一个dll包，仅仅是一个依赖库，它本身不能运行，仅用来给app引用。打包dll时，Webpack会将所有包含的库做一个索引，写在一个manifest文件中，而引用dll的代码（dll user）在打包时，只需读取这个manifest文件即可。

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
        >>e.g. 可以用`import debounce from 'lodash/debounce'`替代`import { debounce } from 'lodash'`，这样最终打包的结果不会引用整个lodash，而只会引用debounce的引用链路文件（可以用[webpack-bundle-analyzer](https://github.com/webpack-contrib/webpack-bundle-analyzer)分析并可视化构建后的打包文件进行对比；也可以直接用[lodash.debounce](https://www.npmjs.com/package/lodash.debounce)单独库代替）。
        ></details>

#### 原理
1. loader（加载器）

    本质是一个函数。webpack中通过compilation对象进行模块编译时，会首先进行匹配loader处理文件得到结果(string/buffer)，之后才会输出给webpack进行编译。通过它我们可以在webpack处理我们的特定资源(文件)之前进行提前处理。
2. plugin插件

    1. [Tapable](https://github.com/webpack/tapable)

        Tapable本质上是提供更方面创建自定义事件和触发自定义事件的库（类似于：[Nodejs的EventEmitter](https://nodejs.org/api/events.html#class-eventemitter)），Webpack中的插件机制就是基于Tapable实现与打包流程解耦，插件的所有形式都是基于Tapable实现。
    2. 本质上在Webpack编译阶段会为各个编译对象初始化不同的Hook（tapable），开发者可以在自己编写的Plugin中监听到这些Hook，在打包的某个特定时间段触发对应Hook注入特定的逻辑从而实现自己的行为。
    3. 实现一个自定义plugin

        ```javascript
        class DonePlugin {
          apply(compiler) {

            // 调用 Compiler Hook 注册额外逻辑
            compiler.hooks.done.tap('Plugin Done', () => {
              console.log('compilation done');
            });
          }
        }

        module.exports = DonePlugin;
        ```
- Compiler：对象主要用于控制打包过程的整个流程

    1. run：开始启动编译过程
    2. make：进行编译
    3. seal：编译完成，形成chunk
    4. emit：输出文件

    - compilation对象代表在这个打包过程中的打包产物，用于记录打包过程中的内容，如dependencies/modules/chunks等等。
    - plugin插件则是监听打包过程中的某一个或多个过程，然后对compilation等内容进行加工处理，最终得到打包好的内容。

---
### 分析输出文件
1. <details>

    <summary>源文件、配置文件</summary>

    1. `webpack.config.js`

        ```javascript
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

        ```javascript
        // ./src/index.js
        const a = require("./a");

        require("./c");

        console.log("index.js");

        module.exports = function Index() {
          return a;
        };
        ```

        ```javascript
        // ./src/a.js
        const b = require("./b");
        console.log(b);

        const d = require("./d");
        console.log(d);

        module.exports = {
          fileName: "a..js",
        };
        ```

        ```javascript
        // ./src/b.js
        require("./c");

        console.log("b..js");
        ```

        ```javascript
        // ./src/c.js
        console.log("i am a not export c..js");
        ```

        ```javascript
        // ./src/d.js
        console.log("d..js");

        exports.fileName = "d..js";
        ```
    </details>

2. 输出文件

    ```javascript
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

### 动态加载
1. 代码使用 ES6 Module的`import()` 或 特别约定的`require` 来告诉webpack支持代码分离

    1. [React通过`<React.Suspense>`、`React.lazy`配合`import()`进行代码分离（动态加载）](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/React学习笔记/README.md#代码分割动态加载)
    2. <details>

        <summary>Vue的异步组件</summary>

        ```javascript
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
    3. 基于路由的代码分离
2. 实现原理

    1. 构建阶段的代码分离（Code Splitting）：

        当Webpack构建项目时，它会根据代码分离配置将模块分组为不同的块（安装使用`@babel/plugin-syntax-dynamic-import`babel配置，代码遇到`import()`或其他）。每个块都是一个独立的文件，可以被异步加载。
    2. 执行代码到动态加载部分时：

        先尝试读取模块缓存，若没有，则创建`<scrip>`加载chunk包（JSONP），chunk写入`window.webpackJsonp`并被webpack的模块加载体系（`__webpack_require__`）引入执行。

        - 动态模块的代码存放在`window.webpackJsonp`：

            ```javascript
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

        - 输出的实现动态加载方法（JSONP原理）：

            ```javascript
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

### 热更新（hot module replacement，HMR，模块热替换）
1. 配置

    ```javascript
    devServer: {
      hot: true,
    },
    plugins: [
      new webpack.HotModuleReplacementPlugin(),
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
        2. manifest（.json，包含所有发生变更的模块列表）
        3. chunk（.js，增量修改内容）
    4. 产生的hash值通过websocket通知HMR Runtime
    5. HMR Runtime对比新旧的hash值，若不一致，则ajax获取manifest确定需要改动的module和chunk，再通过JSONP去Bundle server获取最新资源

### [tree shaking](https://webpack.docschina.org/guides/tree-shaking)
基于静态分析的原理，通过识别未使用的模块、函数、变量等并打上标记，然后在压缩阶段利用uglify-js/terser等压缩工具删除这些没有用到的代码（AST裁剪）。

1. 在webpack中开启，必须同时满足：

    1. 使用ES6 Module规范编写代码

        ><details>
        ><summary>原因</summary>
        >
        >1. 在CommonJs、AMD、CMD等旧版本的JS模块化方案中，导入导出行为是高度动态，难以预测。
        >2. ES6 Module方案则从规范层面规避这一行为，它要求所有的导入导出语句只能出现在模块顶层，且导入导出的模块名必须为字符串常量（不能修改），所以，ES6 Module下模块之间的依赖关系是高度确定的，与运行状态无关，编译工具只需要对代码做静态分析，就可以从代码字面量中推断出哪些模块值未曾被其它模块使用，这是实现Tree Shaking技术的必要条件。
        ></details>

        - 确保代码不会在某些阶段被转换为CommonJS等（在使用babel时避免`compilerOptions.module`设置为非ES6 Module）
    2. 配置`optimization.usedExports: true`启动标记功能
    3. 启动代码优化功能：`mode: 'production'`或`optimization.minimize: true`或`optimization.minimizer: 「数组」`

### [Rollup](https://github.com/rollup/rollup)、[vite](https://github.com/vitejs/vite)与webpack对比
1. Rollup：

    1. 打包结果文件很小，几乎没多余代码（Tree Shaking）；执行很快；可方便输出CommonJS、ES6 Module、IIFE（用于`<script>`引用）格式。
    2. 必须用ES6 Module格式的代码才可以打包。
    3. 适合纯JS的库或组件。
2. webpack

    1. 拥有强大、全面的功能、高度可配置，更好的社区。
    2. 针对各种类型的文件（loader支持）。可以处理多个入口文件和复杂的依赖关系。通过配置文件和加载器，可以高度定制和扩展Webpack的功能。
    3. 在进行资源打包时会产生很多冗余的代码（webpack内部结构、模块化方案、`__webpack_require__`）。
    4. 适合复杂项目。
3. vite

    1. 核心原理：利用现代浏览器现在已经支持ES6 Module的import能力，遇到import就会发送一个HTTP请求去加载ES6 Module文件。整个过程中没有对文件进行打包编译。
    2. 快速的冷启动能力，提供了快速的开发体验。在开发阶段使用原生ES6 Module直接引入模块，而不需要像Webpack和Rollup一样进行打包，从而提供了更快的热重载和构建速度。
    3. 适用于中小型项目，特别是基于现代浏览器的单页应用（SPA）或中小型网站开发。

- 总结：App级别的应用（开发、打包）——webpack，JS库级别的应用（打包）——Rollup，现代浏览器快读开发体验（开发）——vite。
