# [Babel](https://github.com/babel/babel)学习笔记

## 目录
1. [Babel与polyfill的区别](#babel与polyfill的区别)

---
>可阅读：[Babel Handbook](https://github.com/jamiebuilds/babel-handbook)。

### Babel与polyfill的区别
>参考：[Babel polyfill 知多少](https://zhuanlan.zhihu.com/p/29058936)。

1. Babel：（构建时）转译**语法**

    >转译的结果在默认情况下并不包括ES6对运行时的扩展：一般不会造成全局变量污染（修改全局变量）、prototype污染（扩展内建类型的原型方法）。

    当有新语法出现（如：ES6的语法糖），部分浏览器无法支持，就用Babel把新语法转译成老语法（[编译器编译原理](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/程序员的自我修养/README.md#编译器编译原理)）。

    >[`@babel/plugin-transform-runtime`](https://babeljs.io/docs/babel-plugin-transform-runtime) 默认从 `@babel/runtime` 引用转译所需的辅助函数。插件装在开发依赖中，发布的代码若仍引用 `@babel/runtime`，需将它列入运行时依赖。
2. polyfill：（运行时）垫片，判断不支持的API或全局变量进行添加

    >不转换语法。适合开发独立的业务应用，即使全局污染、prototype被修改也影响不大；不适合开发第三方类库。

    1. （全局变量污染）添加内建类型（builtins）

        >如：`Set`、`Map`、`Promise` 等全局对象。`Proxy` 的完整语义需要引擎支持。
    2. （prototype污染）添加内建类型的原型方法

        >如：`Array.prototype.includes`、`String.prototype.padStart`、`Promise.prototype.finally`等。
    3. 添加内建类型的静态方法

        >如：`Array.from`、`Object.assign`等。
    4. 添加Regenerator

        >旧版 Babel 将 `function*`、`async function` 转译后，生成的代码可能需要 `regeneratorRuntime`。语法由编译器转换，运行时负责执行转换后的代码。
