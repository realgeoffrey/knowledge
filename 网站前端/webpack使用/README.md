# webpack使用

>webpack: module building system.

1. 能使用各种方式表达依赖关系

    CommonJS、ES module、AMD、CSS的`@import`、样式的`url()`、HTML的`<img src="">`。都被转化为CommonJS规范的实现。

    >```javascript
    >import list from './list';
    >//等价于
    >var list = require('./list');
    >```
2. 所有文件都当作是**模块（module）**：`脚本（js、jsx、tsx、coffee）`、`样式（css、scss、sass、less）`、`模版（html、tpl）`、`JSON`、`图片`、`字体`。

    webpack自身只理解JS，使用`loader`把所有类型的文件（链式）转换为模块。
3. 从入口起点（`entry`）开始进入文件进行解析，递归地构建一个依赖图，这个依赖图包含着应用程序所需的每个模块，然后将所有这些模块打包为少量的bundle（通常只有一个）由浏览器加载。
