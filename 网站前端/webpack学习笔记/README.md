# [webpack](https://github.com/webpack/webpack)学习笔记

## 目录
1. [总结](#总结)
1. [`webpack.config.js`](#webpackconfigjs)
1. [心得](#心得)
1. [Rollup与webpack对比](#rollup与webpack对比)

---
### 总结
>webpack: module building system.

1. 能使用各种方式表达依赖关系

    CommonJS、ES6 Module、AMD、CSS的`@import`、样式的`url()`、HTML的`<img src="">`。都被转化为CommonJS规范的实现（各种方式引入效果相同）。

    >```javascript
    >import list from './list';
    >// 等价于：
    >var list = require('./list');
    >```
2. 所有文件都当作是**模块（module）**：`脚本（js、jsx、tsx、coffee）`、`样式（css、scss、sass、less）`、`模版（html、tpl）`、`JSON`、`图片`、`字体`。

    webpack自身只理解JS和JSON文件，使用`loader（加载器）`把所有类型的文件（链式）转换为模块。
3. 从`入口起点（entry）`开始进入文件进行解析，（动态打包所有依赖、）递归地构建一个依赖图（dependency graph），这个依赖图包含着应用程序所需的每个模块，模块通过`加载器（loader）`解析完毕，之后经过`插件（plugin）`二次处理，最终将所有这些模块打包为一或多个bundle由浏览器加载。
4. 概念

    打包过程过程：chunk -> bundle。vendor、dll是有特殊缓存逻辑的bundle。

    1. chunk

        （中间过程的）代码块，块的名字在`entry`设置，数字是id。

        >每次修改一个模块时，webpack会生成两部分：`manifest.json`（新的编译hash和所有的待更新chunks目录）、更新后的chunks（.js）。
    2. vendor

        >使用`SplitChunksPlugin`进行自动化选择某些资源避免重复依赖。

        第三方库，独立于经常改动的业务代码，额外提取出chunk成为单独的bundle用于用户缓存。每次构建时都需要进行构建。
    3. dll

        >`DLLPlugin`和`DLLReferencePlugin`配合设置动态链接库（还需要在html中插入），指定资源避免重复依赖。

        独立于经常改动的业务代码，额外提取出chunk成为单独的bundle用于用户缓存，只有修改了dll引用的内容才需再次构建dll，提升了构建的速度。

        >Dll这个概念借鉴了Windows系统的动态链接库（Dynamic Link Library，DLL）。一个dll包，仅仅是一个依赖库，它本身不能运行，仅用来给app引用。打包dll时，Webpack会将所有包含的库做一个索引，写在一个manifest文件中，而引用dll的代码（dll user）在打包时，只需读取这个manifest文件即可。

    >vendor和dll二选一即可。

    4. bundle

        多个chunk的最终合并产出物。

### `webpack.config.js`
1. `entry`：定义整个编译过程的起点

    1. 单入口：`string`
    2. 多入口：`Record<string, string>`
2. `output`：定义整个编译过程的终点

    1. 占位符

        >所有输出名字的地方都可以用。

        1. `[name]`：entry名
        2. `[hash]`：hash值
        3. `[ext]`：资源后缀名
        4. `[path]`：路径
3. `module`：加载器定义模块（文件）的处理方式

    1. `.rules`（数组，每一项是一个对象）

        >rules数组执行有顺序之分，数组逆序链式执行。执行完毕一个loader之后，返回的内容再传入下一个loader进行执行。

        loader加载器，接受源文件，返回转化后的模块。处理webpack无法解析的文件。

        1. `.test`：指定匹配规则。

            webpack根据正则表达式，来确定应该查找哪些文件，并将其提供给指定的loader。
        2. `.use`：指定使用的loader、参数。

            >`use`执行有顺序之分，数组逆序链式执行。执行完毕一个loader之后，返回的内容再传入下一个loader进行执行。
4. `plugin`：插件对编译完成后的模块（加载器处理之后）进行二度加工，增强webpack功能

    >每个plugin都会绑定各种webpack生命周期钩子进行执行plugin内某些具体内容，用户一般不用关注各plugins之间执行顺序。

    用于bundle文件的优化、资源管理、环境变量注入。作用于整个构建过程。进行任何loader无法处理的事情。

    1. 插件`DefinePlugin`在构建结束后向项目代码中注入变量：`new webpack.DefinePlugin({键-值})`

        若项目代码中要使用的Node.js的环境变量，建议都用此方式注入后再使用，而不要直接使用由webpack额外处理的Node.js环境变量。
5. `mode`：使用相应环境的内置优化

    `none`、`development`、`production`（默认）
6. 监听文件从而重新构建

    1. `watch`
    2. `watchOptions`：监听参数
7. `devServer`

    [webpack-dev-server](https://github.com/webpack/webpack-dev-server)、webpack-hot-middleware、webpack-dev-middleware，可以写入内存中（而不是写入磁盘、看不见文件）编译并serve资源来提高性能。

    1. `hot`（需要插件`new webpack.HotModuleReplacementPlugin()`配合）：热更新

        >利用websocket实现，websocket-server识别到html、css和js的改变，就向websocket-client发送一个消息，websocket-client判断若是html和css则操作dom，实现局部刷新，若是js则重载页面。
    2. `static`（替代 ~~`contentBase`~~）
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

### 心得
1. 引用仓库

    1. 若引用仓库，则会按照仓库设置好的路径引用仓库文件。
    2. 若引用仓库中某文件，则会按照该文件的引用链路去引用仓库文件。
    3. 仓库中没有被引用到的文件不会打包进最终bundle。

    >e.g. 可以用`import debounce from 'lodash/debounce'`代替`import { debounce } from 'lodash'`，这样最终打包的结果不会引用整个lodash，而只会引用debounce的引用链路文件（可以用[webpack-bundle-analyzer](https://github.com/webpack-contrib/webpack-bundle-analyzer)分析并可视化构建后的打包文件进行对比；也可以直接用[lodash.debounce](https://www.npmjs.com/package/lodash.debounce)单独库代替）。
2. tree shaking

    只支持ES6 Module，不支持CommonJS。
3. 还未找到满足 css和img放置指定地点 且 html和css都有引入图片 的配置方案:)

### [Rollup](https://github.com/rollup/rollup)与webpack对比
1. Rollup：

    1. 文件很小，几乎没多余代码；执行很快；可方便输出CommonJS、ES6 Module、IIFE（用于`<script>`引用）格式。
    2. 必须用ES6 Module格式的代码才可以打包。
2. webpack：

    1. 拥有强大、全面的功能，更好的社区。
    2. 在进行资源打包时会产生很多冗余的代码。

- 总结：App级别的应用——webpack，JS库级别的应用——Rollup。
