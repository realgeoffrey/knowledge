# 前端概念

## 目录
1. [前端涉及内容](#前端涉及内容)
1. [前端工程化](#前端工程化)
1. [网站性能优化](#网站性能优化)
1. [页面解析、渲染步骤](#页面解析渲染步骤)
1. [前端「增量」原则](#前端增量原则)
1. [安全漏洞攻击](#安全漏洞攻击)

---
### 前端涉及内容
![前端涉及内容图1](./images/fe-tech-1.png)

>更详细的线路图：[Frontend Roadmap](https://github.com/kamranahmedse/developer-roadmap/blob/master/readme.md#-frontend-roadmap)。

1. 从本质上讲，所有Web应用都是一种运行在网页浏览器中的软件，这些软件的GUI（Graphical User Interface，图形用户界面）即为前端。
2. 服务端Node.js与各种终端的涌现，让前端进入了大前端范畴，这时的前端，已远远不只是浏览器端的页面实现技术，而是后端服务与人机界面的连接器。

    ![前端涉及内容图2](./images/fe-tech-2.png)

### 前端工程化
>参考：[张云龙：前端工程——基础篇](https://github.com/fouber/blog/issues/10)。

1. 第一阶段：库/框架选型

    >提升开发效率。（使用自动化工具也能够提升开发效率，如：浏览器自动刷新、IDEs）
2. 第二阶段：简单构建优化

    >提升运行性能。

    对代码进行压缩、校验，以页面为单位进行简单的资源合并。
3. 第三阶段：JS/CSS模块化开发

    >提升维护效率。

    **分而治之**
    1. [JS模块化方案](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/前端内容/标准库文档.md#js模块化方案)：

        CommonJS/AMD/CMD/ES6 Module/UMD
    2. CSS模块化方案：

        Sass/Less/Stylus等CSS预处理器的`import`、`mixin`特性支持实现。
4. 第四阶段：前端工程化

    >优化部署、开发。

    1. 组件化开发

        >模块化开发的升华。

        1. 页面上的每个**独立的**可视/可交互区域视为一个组件；
        2. 每个组件对应一个**工程目录**，组件所需的各种资源都在这个目录下**就近维护**；
        3. 由于组件具有独立性，因此组件与组件之间可以**自由组合**；
        4. 页面只不过是组件的容器，负责组合组件形成功能完整的界面；
        5. 当不需要某个组件，或想要替换组件时，可以整个目录替换、删除。

    2. 资源管理

        >静态资源加载的技术实现。

        1. 静态资源管理系统 = 资源表 + 资源加载框架
        2. [大公司的静态资源优化方案](https://github.com/fouber/blog/issues/6)：

            1. 配置超长时间的本地缓存 —— 节省带宽，提高性能
            2. 采用文件的数字签名（如：MD5）作为缓存更新依据 —— 精确的缓存控制
            3. 静态资源CDN部署 —— 优化网络请求
            4. 非覆盖式更新资源 —— 平滑升级

### 网站性能优化
>性能优化是一个[工程](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/前端内容/README.md#前端工程化)问题。

页面内容下载速度 -> 页面解析、渲染速度和流畅性 -> 用户交互流畅性 的具体优化。

1. URL输入：

    服务端（运维）对HTTP请求、资源发布和缓存、服务器配置的优化。

    1. 服务器开启gzip（如：nginx）。

        >前端查看Response头是否有：`Content-Encoding: gzip`。
    2. 优先开启使用HTTP/2.0（代替HTTP/1.1、HTTP/1.0）
    3. 减少DNS查找，设置合适的TTL值，避免重定向。
    4. 使用CDN。
    5. [静态资源和API分开域名放置](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/前端内容/基础知识.md#静态资源使用额外域名的原因)，减少cookie。
    6. 对资源进行缓存：

        1. 减少~~内嵌JS、CSS~~，使用外部JS、CSS。
        2. 使用[缓存相关HTTP头](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/HTTP相关/README.md#http缓存)

            `Expires` `Cache-Control` `Last-Modified/If-Modified-Since` `ETag/If-None-Match`
        3. 配置超长时间的本地缓存，采用文件的数字签名（如：MD5）作为缓存更新依据。

            [非覆盖式更新资源](https://github.com/fouber/blog/issues/6)。
2. 载入页面时，优化CRP（Critical Rendering Path，关键渲染路径，优先显示与用户操作有关内容）：

    1. 减少关键资源、减少HTTP请求：

        1. 资源合并、去重。
        2. 首屏资源进行服务端渲染，不要在客户端异步加载并渲染。
        3. 非首屏资源延迟异步加载：

            1. 增量加载资源：

                1. [图片的延迟加载（lazyload）](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/JS方法积累/实用方法/README.md#jquery图片延时加载lazyload)。
                2. AJAX加载。

                    如：[滚动加载](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/JS方法积累/实用方法/README.md#jquery滚动加载)、[IntersectionObserver判断DOM可见再发起异步加载](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/JS方法积累/实用方法/README.md#原生jsdom展示或消失执行方法intersectionobserver)。
                3. 功能文件按需加载（模块化、组件化）。
            2. 使AJAX可缓存。

                当用GET方式时添加缓存HTTP头：`Expires` `Cache-Control` `Last-Modified/If-Modified-Since`。
        4. 使用缓存代替每次请求。

            客户端：localStorage、sessionStorage、cookie等；服务端：Redis等。
        5. 利用空闲时间[预加载](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/JS学习笔记/README.md#预加载)。
        6. 第三方资源异步加载（`<script>`添加`defer/async`属性、动态创建或修改`<script>`）、第三方资源使用统一的CDN服务和设置[`<link>`预加载](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/JS学习笔记/README.md#预加载)。
        7. 避免使用空链接的`<img>`、`<link>`、`<script>`、`<iframe>`（老版本浏览器依旧会请求）。
    2. 最小化字节：

        1. 压缩资源。
        2. 图片优化

            1. 压缩。
            2. 小图合并雪碧图。

                >大图切小图：单个大文件需要多次HTTP请求获取。
            3. 合理使用Base64、WebP（SharpP）、`srcset`属性。

                >1. 服务端（或CDN）处理图片资源，提供返回多种图片类型的接口（如：[七牛](https://developer.qiniu.com/dora/manual/3683/img-directions-for-use)）。
                >2. [判断浏览器是否支持WebP](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/JS方法积累/实用方法/README.md#原生js判断是否支持webp)，对不同浏览器请求不同的图片类型。
                >3. 用`<source>/<img>`的`type`、`srcset`、`sizes`、`media`等属性，让浏览器自动选择使用哪种资源（浏览器自动跳过不支持的资源）。
    3. 缩短CRP长度：

        CSS放在HTML顶部，JS放在HTML底部。
    4. 用户体验：

        >本质上是减弱用户对加载时长的感知，并没有真的提高程序性能。

        1. 骨架屏
        2. lazyload默认图
3. 载入页面后进行的[页面解析、渲染](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/前端内容/README.md#页面解析渲染步骤)、线程执行性能：

    >大部分情况下的浏览器是单线程执行，因此要尽量做到「最小化主线程的责任」，来确保渲染流畅和交互响应及时。

    1. CSS性能：

        1. [CSS选择器性能](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/HTML+CSS学习笔记/README.md#css选择器)。
        2. [渲染性能](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/HTML+CSS学习笔记/README.md#渲染性能rendering-performance)

            1. 样式缩小计算范围、降低复杂度。
            2. 减少重绘和重排。
            3. 动画合理触发GPU加速。
            4. 尽量仅使用`opacity`、`transform: translate/scale/rotate/skew`处理动画。
    2. JS代码性能优化：

        1. 使用性能好的代码方式（微优化）

            1. 字面量创建数据，而不是构造函数。
            2. 缓存DOM的选择、缓存列表.length。
            3. [闭包合理使用](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/JS学习笔记/README.md#闭包closure)。
            4. [避免内存泄漏](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/JS学习笔记/README.md#内存泄漏)。
            5. 长字符串拼接使用`Array.prototype.join()`，而不使用`+`。
        2. 尽量使用事件代理，避免批量绑定事件。
        3. [定时器取舍，合理使用重绘函数代替](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/JS学习笔记/README.md#定时器--重绘函数)。
        4. 高频事件（如：`scroll`、`mousemove`、`touchmove`）使用[函数防抖、函数节流](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/JS学习笔记/README.md#函数防抖函数节流)，避免在高频事件中进行运行时间长的代码。
        5. 避免强制同步布局、避免布局抖动。
        6. 使用`Web Worker`处理复杂的计算。
        7. 正则表达式尽可能准确地匹配目标字符串，以减少不必要的回溯。
        8. 针对在用框架，使用合理的特性实现业务逻辑。

            1. <details>

                <summary>vue</summary>

                1. `key`属性的组件/DOM复用。
                2. `v-once`只渲染元素和组件一次。
                3. 最小限度使用响应式系统。

                    1. 若不需要响绑定到视图的变量

                        1. 不提前注册在`data`或`computed`中，直接this.来创建
                        2. `Object.freeze()`
                4. 注意内存泄漏（全局副作用）：

                    1. 在Vue实例内部`new`的其他实例或DOM，应放在`data`内进行掌控，当使用完毕后引导垃圾回收。
                    2. 在Vue实例内部手动绑定的事件（如：`addEventListener`）、计时器、http连接、以及任何需要手动关闭的内容，需要在`beforeDestroy`前手动清除（`destroyed`仅自动清除Vue自己定义、绑定的内容）。
                </details>
    3. HTML：

        1. 减少层级嵌套。
        2. 在拥有`target="_blank"`的`<a>`中添加`rel="noopener"`。

- [WebView优化](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/Hybrid前端开发/README.md#webview性能)：

    配合客户端开发落地优化方案。

>- <details>
>
>    <summary>优先优化对性能影响大、导致瓶颈的部分</summary>
>
>    1. 在客户端运行[`window.performance`](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/前端内容/标准库文档.md#performance)查看页面从打开到加载完成的时间数据。
>    2. DevTools：
>
>        1. Performance查询运行时导致**帧数**过高的代码。
>        2. Rendering、Layers查看CSS渲染情况。
>        3. Memory、JavaScript Profiler、Performance monitor查询内存占用情况。
>    3. 打开各种分析工具，根据建议逐条对照修改
>
>        1. [lighthouse](https://github.com/GoogleChrome/lighthouse)
>
>            1. DevTools的Audits
>            2. Chrome的扩展程序：[Lighthouse](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk)
>            3. Node.js全局安装[lighthouse](https://www.npmjs.com/package/lighthouse)并执行`lighthouse 域名`
>        2. 分析网站：
>
>            1. google的性能分析[PageSpeed Insights](https://developers.google.com/speed/pagespeed/insights/)
>            2. W3C
>
>                1. [标签验证](https://validator.w3.org/)
>                2. [CSS验证](https://jigsaw.w3.org/css-validator/validator.html.zh-cn)
>                3. [链接测试](https://validator.w3.org/checklink)
>            3. [性能测试](https://gtmetrix.com/)
>    </details>
>- <details>
>
>    <summary>网络应用的生命期建议：</summary>
>
>    1. load
>
>        1000ms内完成CRP。
>    2. idle
>
>        进行50ms内的空闲时期预加载，包括图片、多媒体文件、后续内容（如：评论）。
>    3. animations
>
>        保证16ms/f的浏览器渲染时间。
>    4. response
>
>        100ms内对用户的操作做出响应。
>    </details>

### 页面解析、渲染步骤
>参考：[全方位提升网站打开速度：前端、后端、新的技术](https://github.com/xitu/gold-miner/blob/master/TODO/building-a-shop-with-sub-second-page-loads-lessons-learned.md#前端性能)、[浏览器的工作原理：新式网络浏览器幕后揭秘](https://www.html5rocks.com/zh/tutorials/internals/howbrowserswork/#The_order_of_processing_scripts_and_style_sheets)。

![页面解析步骤图](./images/load-html-1.png)

><details>
><summary>约定</summary>
>
>1. 判断是否DOM构造：打印该DOM。
>2. 判断是否完成新的渲染：查看页面显示的DOM结果（DOM结构和样式效果）。
>3. 可以利用抓包工具（如：Charles），breakpoints静态资源来模拟加载缓慢或加载失败，从而判断是否会影响后面的解析或渲染。
>4. 利用DevTools的Network中的Waterfall判断资源加载的开始时间、是否并行。
></details>

1. 解析HTML（parse HTML）

    获取.html文件后，对文件进行从上到下解析：**增量式**生成一个文档对象模型（DOM构造）、生成CSS对象模型（CSSOM）。

    ><details>
    ><summary>总结</summary>
    >
    >1. 解析HTML基本严格按照HTML内容从上到下进行。
    >2. 渲染引擎通过各种线程并行的措施，尽可能快速解析HTML：
    >
    >    并行进行：DOM构造、生成CSSOM、渲染。
    >
    >    1. 异步脚本（`defer`或`async`的`<script>`）。
    >    2. 执行脚本时可能预解析剩下的HTML。
    >    3. 网络操作：无论何时（包括：阻塞解析HTML、阻塞渲染 时），预加载扫描仪不间断并行下载各种类型资源文件（按优先级和HTML顺序）。
    >3. 从上到下尽可能快地解析HTML时，进程会因为各种情况被阻塞：
    >
    >    1. JS会等待它之前的CSS生成CSSOM之后才执行。
    >    2. JS执行完之前不会继续解析HTML。
    >    3. 除了CSS和JS文件之外，其他资源文件的下载不会影响解析HTML
    >
    >        1. 解析到CSS且这个CSS文件在`<body>`中时，若该文件还在下载，则阻止解析HTML。
    >        2. 解析到JS时，若该文件还在下载，则阻止解析HTML。
    >
    >        - 阻止解析期间，必须等待CSS和JS的外链资源加载完毕（包括加载失败）才会继续解析HTML。
    ></details>

    1. 加载DOM中所有CSS，生成CSSOM（recalculate style），描述对页面内容如何设置样式。

        1. 加载CSS并构造完成当前的CSSOM之前，**阻塞渲染**（Render Tree渲染被暂停）。
        2. 解析到CSS且这个CSS文件在`<body>`中时，若该文件还在下载，则阻止解析HTML，直到下载完成（下载中的CSS文件若在`<head>`中，则不会阻止解析HTML）。

        >异步添加的CSS（JS动态添加样式），不会阻塞渲染、不会阻止解析HTML。

        3. 多个CSS文件可同时进行分析而后再生成CSSOM，也可对已经生成的CSSOM进行增删改查。
        4. 构建生成CSSOM的速度非常快。

        ><details>
        ><summary>已经被提取的CSS（<code>&lt;link></code>、<code><style></code>、<code>style</code>内嵌样式），若再次修改或删除（或新添加），会再次影响CSSOM构造。</summary>
        >
        >以下代码可以实时在页面中编辑样式
        >```html
        ><style contenteditable style="display: block">
        >  a {
        >    color: red;
        >  }
        ></style>
        >
        ><a href="javascript:">a标签</a>
        >```
        ></details>
    2. 加载DOM中所有JS，对DOM和CSSOM进行访问和更改。

        1. 解析到JS，在脚本执行完之前，**阻塞解析HTML**（DOM构造被暂停）。

            >1. 解析到JS时，若该文件还在下载，则保持阻塞解析HTML，直到下载并执行完毕。
            >2. 带有`defer`或`async`的`<script>`是异步加载的JS，不会阻塞解析HTML。
        2. 等待之前已经解析的所有CSS被提取且CSSOM被构造完毕。
        3. 执行脚本，访问、更改DOM和CSSOM。

            ><details>
            ><summary>一个<code><script></code>最多执行一次。</summary>
            >
            >1. 已经执行过的脚本（`<script>`：外部脚本`src`或内嵌脚本），若再次修改或删除，不会再执行，也不会影响执行过的内容。已经执行过的脚本，若删除外部脚本`src`或删除内嵌脚本内容，之后再添加外部脚本`src`或添加内嵌脚本内容，也不会再次执行。
            >2. 没有执行过内容的空脚本`<script></script>`，若添加外部脚本`src`或添加内嵌脚本，会执行一次。
            ></details>
        4. 脚本执行完毕，继续 解析HTML（DOM构造）。

            >[`<script>`的加载和执行时机](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/前端内容/基础知识.md#script的加载和执行时机)。

    - 事件完成顺序

        1. 开始解析HTML；
        2. （额外线程、并行）加载外部资源文件（CSS、JS、图片、媒体、等）；
        3. 执行同步的JS和CSS

            1. 等待外部JS和CSS加载完毕；
            2. CSSOM先构造完毕，再执行JS。
        4. 构造DOM完毕；

            `构造DOM完毕` -> `<script>`的`defer`脚本执行完毕 -> `document`的`DOMContentLoaded`事件触发 或 jQuery的`$(document).ready(function () {})`执行回调
        5. 解析HTML完成、且所有资源加载完毕（包括：`<img>`等资源文件、样式引用的`background`图片、异步加载的JS、动态加载的资源）。

            完毕后触发：`window`的`load`事件。
2. DOM和CSSOM构造完成后（解析HTML完成），进行渲染：

    Render Tree（渲染树）：Layout -> Paint -> Composite

    >1. 只有可见的元素才会进入渲染树。
    >2. DOM不存在伪元素（CSSOM中才有定义），伪元素存在render tree中。

    - 渲染在每一帧都会进行

        >[渲染细节和性能](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/HTML+CSS学习笔记/README.md#渲染性能rendering-performance)。

        页面每一帧刷新时，会使用当前最新解析完成的DOM和CSSOM进行渲染。阶段性生成CSSOM完成之前（生成CSSOM进行时），会阻塞渲染。

### 前端「增量」原则
1. 「增量」原则：

    >「增量下载」是前端在工程上有别于客户端GUI软件的根本原因。

    前端应用没有安装过程，其所需程序资源都部署在远程服务器，用户使用浏览器访问不同的页面来加载不同的资源，随着页面访问的增加，渐进式地将整个程序下载到本地运行。
2. 由「增量」原则引申出的前端优化技巧几乎成为了**性能优化**的核心：

    1. 加载相关：延迟加载、AJAX加载、按需加载、预加载、请求合并压缩等策略。
    2. 缓存相关：缓存更新、缓存共享、非覆盖式更新资源等方案。
    3. 复杂的BigRender、BigPipe、Quickling、PageCache等技术。

### 安全漏洞攻击
1. XSS

    跨站脚本（Cross-Site Scripting，XSS）是恶意代码注入网页。利用用户对指定网站的信任。

    1. 攻击方式

        >所有可输入的地方，若没有对输入数据进行处理的话，则都存在XSS漏洞。

        - 通过巧妙的方法注入恶意指令代码（HTML、JS、Flash）到网页内容，使用户加载并执行恶意程序。

            攻击成功后，能够：盗取用户cookie、破坏页面结构、重定向到其它地址、利用用户机器执行各种非客户意愿的行为（如：发起请求、向其他网站发起DDoS攻击）等。
    2. 防御措施：

        1. 过滤用户输入（白名单）

            >e.g. [js-xss](https://github.com/leizongmin/js-xss)
        2. HttpOnly

            cookie设置为HttpOnly不能在客户端使用~~document.cookie~~访问。
        3. `Content-Security-Policy`设置不允许加载白名单外的域名资源

            >指令细节：[MDN: Content-Security-Policy](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Headers/Content-Security-Policy)。

            1. HTTP响应头：

                `Content-Security-Policy: 具体指令`
            2. `.html`的`<meta>`

                `<meta http-equiv="Content-Security-Policy" content="具体指令">`

        >Flash的安全沙盒机制配置跨域传输：crossdomian.xml
2. CSRF

    跨站请求伪造（Cross-Site Request Forgery，CSRF）是挟制用户在已登录的网页上执行非本意操作。利用网站对用户浏览器的信任。

    1. 攻击方式

        - 当用户已经得到目标网站的认可后，对目标网站进行请求操作。

            攻击成功后，能够：进行所有目标网站的请求操作。
    2. 防御措施

        1. 检查HTTP请求的Referer字段

            Referer：请求来源地址。

            >地址栏直接输入内容不会提供`Referer`。
        2. 添加校验token

            >token：判断用户当前的会话状态是否有效（短时效性）。

            目标网站请求需要额外提供保存在页面中的随机校验码（不保存在cookie即可）。可以放进请求参数、或自定义HTTP请求头。保证用户必须实时在目标网站才能获取到校验token。
        3. 验证码

            保证用户必须和目标网站进行交互后才可以发起请求。
        4. 跨域请求的限制（利用CORS等）
3. 其他攻击

    1. 注入型劫持

        通过在正常的网页中注入广告代码（JS代码、`<iframe>`、其他标签等），实现页面弹窗提醒或者底部广告等。

        1. 攻击方式

            运营商劫持。
        2. 防御措施

            全链路HTTPS（若使用CDN，则必须CDN请求和回源都是HTTPS）。

            >额外增加劫持难度：前端还可以用[子资源完整性（SRI）](https://developer.mozilla.org/zh-CN/docs/Web/Security/子资源完整性)验证加载文件的数字签名。
    2. DNS攻击

        使域名指往不正确的IP地址。

        1. 攻击方式

            1. 针对DNS服务器：DDoS攻击。
            2. 针对用户：DNS欺骗或劫持（访问恶意DNS服务器）、DNS缓存服务器投毒或污染、本机劫持（hosts文件篡改、本机DNS劫持、SPI链注入、DHO插件）。
        2. 防御措施

            1. 使用安全的DNS服务器。
            2. VPN或域名远程解析。
            3. 查杀病毒，清空DNS缓存。
    3. SQL注入（SQL Injection）

        运行非法的SQL。
    4. OS命令注入攻击（OS Command Injection）

        通过Web应用，执行非法的操作系统命令。
    5. HTTP头部注入攻击（HTTP Header Injection）

        通过在响应头部字段内插入换行，添加任意响应头部或主体。
    6. 邮件头部注入攻击（Mail Header Injection）

        向邮件头部To或Subject内任意添加非法内容，可对任意邮件地址发送广告邮件或病毒邮件。
    7. 目录遍历攻击（Directory Traversal，Path Traversal）

        对本无意公开的文件目录，通过非法截断其目录路径后，达成访问目的。
    8. 远程文件包含漏洞（Remote File Inclusion）

        当部分脚本内容需要从其他文件读入时，利用指定外部服务器的URL充当依赖文件，让脚本读取之后，就可运行任意脚本。
    9. 强制浏览（Forced Browsing）

        从安置在Web服务器的公开目录下的文件中，浏览那些原本非自愿公开的文件。
    10. 不正确的错误消息处理（Error Handling Vulnerability）

        Web应用的错误信息内包含对攻击者有用的信息。
    11. 开放重定向（Open Redirect）

        假如指定的重定向URL到某个具有恶意的Web网站，那么用户就会被诱导至那个Web网站。
    12. 会话劫持（Session Hijack）

        通过某种手段拿到了用户的会话ID，并非法使用此会话ID伪装成用户。
    13. 会话固定攻击（Session Fixation）

        强制用户使用攻击者指定的会话ID。
    14. 点击劫持（ClickJacking）、界面伪装（UI Redressing）

        利用透明的按钮或链接做成陷阱，覆盖在Web页面上。然后诱使用户在不知情的情况下，点击那个链接访问内容。
    15. 密码破解（Password Cracking）

        1. 穷举法（Brute-force Attack，暴力破解法）

            对所有密钥集合构成的密钥空间（Keyspace）进行穷举。即，用所有可行的候选密码对目标的密码系统试错。
        2. 字典攻击

            利用事先收集好的候选密码（经过各种组合方式后存入字典），枚举字典中的密码。

            >如：生日日期数值化。

        - 一种安全的服务端存储密码方式：

            先利用给密码加盐（salt）的方式增加额外信息，再使用散列（hash）函数计算出散列值后保存。

            ><details>
            ><summary>加盐</summary>
            >
            >由服务器随机生成的一个字符串，保证长度足够长，且是真正随机生成。然后把它和密码字符串相连接（前后都可以）生成散列值。当两个用户使用了同一个密码时，由于随机生成的salt值不同，对应的散列值也将不同。这样一来，很大程度上减少了密码特征，攻击者也就很难利用自己手中的密码特征库进行破解。
            ></details>
    16. DoS攻击（Denial of Service attack）、服务停止攻击或拒绝服务攻击

        运行中的服务呈停止状态的攻击。

        1. 集中利用访问请求造成资源过载。

            DDoS（Distributed Denial of Service attack）利用多台计算机发起Dos攻击。
        2. 通过攻击安全漏洞使服务停止。
    17. Hash Collision DoS

        >参考：[HASH COLLISION DOS 问题](http://coolshell.cn/articles/6424.html)。

        Hash碰撞的拒绝式服务攻击（Hash Collision DoS）是对服务器进行恶意负载。

        1. 攻击方式

            >1. Hash：把任意长度的输入，通过散列算法，输出固定长度的散列值。
            >2. Hash Collision DoS：利用各语言Hash算法的「非随机性」，制造出无数value不同、key相同的数据，让Hash表成为一张单向链表，而导致整个网站的运行性能下降。

            - 找到hash算法漏洞，不断提交服务器请求导致无数hash碰撞，进而形成类似单向链表的存储结构。

                攻击成功后，能够：hash堆积、查询缓慢、服务器CPU高负荷、服务器内存溢出。
        2. 防御措施

            1. 升级hash算法。
            2. 限制POST参数个数和请求长度。
            3. 防火墙检测异常请求。

- 验证码

    仅能预防机器行为：防止广告机注册、发帖、评论，防止暴力破解密码。

    1. 服务端生成图片，前端根据图片发送请求给服务端验证。
    2. ~~前端生成并验证~~。
