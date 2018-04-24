# webpack学习笔记

## 目录
1. [总结](#总结)
1. [`webpack.config.js`](#webpackconfigjs)

---
### 总结
>webpack: module building system.

1. 能使用各种方式表达依赖关系

    CommonJS、ES6 module、AMD、CSS的`@import`、样式的`url()`、HTML的`<img src="">`。都被转化为CommonJS规范的实现。

    >```javascript
    >import list from './list';
    >// 等价于：
    >var list = require('./list');
    >```
2. 所有文件都当作是**模块（module）**：`脚本（js、jsx、tsx、coffee）`、`样式（css、scss、sass、less）`、`模版（html、tpl）`、`JSON`、`图片`、`字体`。

    webpack自身只理解JS，使用`loader`把所有类型的文件（链式）转换为模块。
3. 从入口起点（`entry`）开始进入文件进行解析，递归地构建一个依赖图（dependency graph），这个依赖图包含着应用程序所需的每个模块，模块通过`加载器`解析完毕，之后经过`插件`二次处理，最终将所有这些模块打包为少量的bundle（`output`）由浏览器加载。
4. 关键点（`webpack.config.js`）

    1. `entry`：定义整个编译过程的起点
    2. `output`：定义整个编译过程的终点
    3. `module`：加载器定义模块（文件）的处理方式
    4. `plugin`：插件对编译完成后的内容（加载器处理之后）进行二度加工
    5. `resolve.alias`：定义路径的别名

### `webpack.config.js`
1. `webpack-dev-server`的热更新配置：`devServer.hot: true`

    利用websocket实现，websocket-server识别到html、css和js的改变，就向websocket-client发送一个消息，websocket-client判断如果是html和css就操作dom，实现局部刷新，如果是js就整体刷新。
2. 插件`DefinePlugin`在构建结束后向项目代码中注入变量：`new webpack.DefinePlugin({键-值})`

    若项目代码中要使用的Node的环境变量，建议都用此方式注入后再使用，而不要直接使用由webpack额外处理的Node环境变量。
