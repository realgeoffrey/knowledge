# knowledge

><details>
><summary>约定</summary>
>
>1. `+`、`-`含义
>
>    1. `ie8+`：包括ie8以及高于ie8的ie浏览器。
>    2. `ie8-`：包括ie8以及低于ie8的ie浏览器。
>2. 变量命名含义
>
>    1. `dom`：`Element`实例（或`document`、`Node`实例）
>    2. `$dom`：jQuery（或Zepto）对象包装的DOM元素
>    3. `obj`：对象实例
>    4. `arr`：数组实例
>3. 浏览器针对的系统环境
>
>    1. `PC`：针对桌面端制作的网页（系统包括：macOS、Windows）。
>    2. `WAP`：针对移动端（手机浏览器或Hybrid App）制作的页面（系统包括：iOS、Android）。
>4. 默认仅针对浏览器的JS运行时环境（JavaScript runtime environment）
>
>    其他JS运行时环境：Node.js、[Deno](https://github.com/denoland/deno)、[Bun](https://github.com/oven-sh/bun)。
>5. 原型链（`[[Prototype]]`）
>
>    （非标准）`对象.__proto__`等价于：`Object.getPrototypeOf(对象)/Object.setPrototypeOf(对象, 原型对象)`
>6. 父子级含义
>
>    广义上可能包含祖先级、孙辈级之间关系，不仅仅是一层父子间关系。
></details>

## 目录
1. 前端内容

    1. [前端概念](./网站前端/前端内容/README.md)
    2. [标准库文档](./网站前端/前端内容/标准库文档.md)
    3. [基础知识](./网站前端/前端内容/基础知识.md)
2. JS

    1. [JS学习笔记](./网站前端/JS学习笔记/README.md)
    2. [JS实用方法](./网站前端/JS方法积累/实用方法/README.md)
    3. [JS正则表达式](./网站前端/JS正则表达式/README.md)
3. HTML+CSS

    1. [HTML+CSS学习笔记](./网站前端/HTML+CSS学习笔记/README.md)
    2. [响应式相关](./网站前端/HTML+CSS学习笔记/响应式相关.md)
    3. [弹性盒子（Flexbox）](./网站前端/HTML+CSS学习笔记/弹性盒子（Flexbox）.md)
    4. [实现具体业务](./网站前端/HTML+CSS学习笔记/实现具体业务.md)

    - <details>

        <summary>其他</summary>

        1. 初始化模板

            1. [cssReset.scss](./网站前端/初始化模板/cssReset.scss)
            2. [init.html](./网站前端/初始化模板/init.html)
        2. [SCSS使用](./网站前端/SCSS使用/README.md)
        </details>
4. [代码调试相关](./网站前端/代码调试相关/README.md)
5. 前端技术栈

    1. [Vue.js学习笔记](./网站前端/Vue.js学习笔记/README.md)
    2. [React学习笔记](./网站前端/React学习笔记/README.md)
6. 大前端

    1. [Hybrid前端开发](./网站前端/Hybrid前端开发/README.md)
    2. [Typescript学习笔记](./网站前端/Typescript学习笔记/README.md)
    3. [Hippy学习笔记](./网站前端/Hippy学习笔记/README.md)
    4. [Node.js学习笔记](./网站前端/Node.js学习笔记/README.md)

        - <details>

            <summary>其他</summary>

            1. [Node.js实用方法](./网站前端/Node.js学习笔记/Node.js实用方法/README.md)
            </details>
    5. [服务端相关](./网站前端/服务端相关/README.md)
    6. [微信生态相关](./网站前端/微信生态相关/README.md)
7. [还原设计稿](./网站前端/还原设计稿/README.md)
8. [HTTP相关](./网站前端/HTTP相关/README.md)
9. [算法](./网站前端/算法/README.md)

    1. [LeetCode记录](./网站前端/算法/LeetCode记录/README.md)
10. [程序员的自我修养](./网站前端/程序员的自我修养/README.md)
11. <details>

    <summary>前端构建工具</summary>

    1. [webpack学习笔记](./网站前端/webpack学习笔记/README.md)
    2. [Babel学习笔记](./网站前端/Babel学习笔记/README.md)
    3. [yarn+Lerna学习笔记](./网站前端/yarn+Lerna学习笔记/README.md)
    4. [ESLint+Prettier学习笔记](./网站前端/ESLint+Prettier学习笔记/README.md)
    5. [Node.js脚手架（TypeScript+pm2或nodemon+--inspect）](./网站前端/Node.js脚手架（TypeScript+pm2或nodemon+--inspect）/README.md)

    - <details>

        <summary>其他</summary>

        1. [我安装的全局仓库](./网站前端/Node.js学习笔记/我安装的全局仓库.md)
        </details>
    </details>
12. [无障碍](./网站前端/无障碍/README.md)
13. [海外应用总结](./网站前端/海外应用总结/README.md)

- <details>

    <summary>其他</summary>

    1. [/工具使用](./工具使用/README.md)
    2. [/环境安装、配置](./环境安装、配置/README.md)
    3. [拓展知识](./网站前端/拓展知识/README.md)
    </details>

><details>
><summary>废弃内容:thumbsdown:</summary>
>
>1. [兼容至ie6](./网站前端/兼容至ie6/README.md)
>2. [JS废弃代码](./网站前端/JS方法积累/废弃代码/README.md)
>3. [原生JS宽高](./网站前端/JS学习笔记/原生JS宽高.md)
>4. [gulp使用](./网站前端/gulp使用/README.md)
></details>

---
><details>
><summary>完美不在于无以复加，而在于无可删减。</summary>
>
>
>[![Star History Chart](https://api.star-history.com/svg?repos=realgeoffrey/knowledge&type=Date)](https://star-history.com/#realgeoffrey/knowledge&Date)
></details>
