# webpack学习笔记

## 目录
1. [总结](#总结)
1. [`webpack.config.js`](#webpackconfigjs)

---
### 总结
>webpack: module building system.

1. 能使用各种方式表达依赖关系

    CommonJS、ES6 module、AMD、CSS的`@import`、样式的`url()`、HTML的`<img src="">`。都被转化为CommonJS规范的实现（各种方式引入效果相同）。

    >```javascript
    >import list from './list';
    >// 等价于：
    >var list = require('./list');
    >```
2. 所有文件都当作是**模块（module）**：`脚本（js、jsx、tsx、coffee）`、`样式（css、scss、sass、less）`、`模版（html、tpl）`、`JSON`、`图片`、`字体`。

    webpack自身只理解JS，使用`loader`把所有类型的文件（链式）转换为模块。
3. 从入口起点（`entry`）开始进入文件进行解析，递归地构建一个依赖图（dependency graph），这个依赖图包含着应用程序所需的每个模块，模块通过`加载器`解析完毕，之后经过`插件`二次处理，最终将所有这些模块打包为少量的bundle由浏览器加载。
4. 概念

    1. chunk
    
        （中间过程的）代码块，块的名字在`entry`设置，数字是id。
        
        >每次修改一个模块时，webpack会生成两部分：`manifest.json`（新的编译hash和所有的待更新chunks目录）；更新后的chunks（.js）。
    2. vendor
    
        >使用`SplitChunksPlugin`进行自动化选择某些资源避免重复依赖。
        
        独立于经常改动的业务代码，额外提取出chunk成为单独的bundle用于用户缓存。每次构建时都需要进行构建。
    3. dll
    
        >`DLLPlugin`和`DLLReferencePlugin`配合设置动态链接库（还需要在html中插入），指定资源避免重复依赖。
        
        独立于经常改动的业务代码，额外提取出chunk成为单独的bundle用于用户缓存。在打包时额外提取出dll的chunk，之后的构建过程不需要进行dll引用内容的构建，直到改动了dll引用内容才需要再对dll进行一次构建。
    
    >vendor和dll二选一即可。
    
    4. bundle
    
        多个chunk的最终合并产出物。

### `webpack.config.js`
1. 关键点
    1. `entry`：定义整个编译过程的起点
    2. `output`：定义整个编译过程的终点
    3. `module`：加载器定义模块（文件）的处理方式
    4. `plugin`：插件对编译完成后的内容（加载器处理之后）进行二度加工
    5. `resolve.alias`：定义路径的别名
2. `webpack-dev-server`的热更新配置：`devServer.hot: true`（需要插件`new webpack.HotModuleReplacementPlugin()`配合）

    利用websocket实现，websocket-server识别到html、css和js的改变，就向websocket-client发送一个消息，websocket-client判断如果是html和css就操作dom，实现局部刷新，如果是js就整体刷新。
3. 插件`DefinePlugin`在构建结束后向项目代码中注入变量：`new webpack.DefinePlugin({键-值})`

    若项目代码中要使用的Node的环境变量，建议都用此方式注入后再使用，而不要直接使用由webpack额外处理的Node环境变量。
4. 可以导出数组，分别进行配置，串行执行多个webpack任务（如前后端同构任务）

    ```javascript
    module.exports = [配置1, 配置2]
    ```
