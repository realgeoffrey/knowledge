# 前端概念

## 目录
1. [前端涉及内容](#前端涉及内容)
1. [前端工程化](#前端工程化)
1. [页面加载解析步骤](#页面加载解析步骤)
1. [浏览器缓存](#浏览器缓存)
1. [前端“增量”原则](#前端增量原则)
1. [网站性能优化](#网站性能优化)
1. [静态资源使用额外域名（domain hash）的原因](#静态资源使用额外域名domain-hash的原因)
1. [安全漏洞攻击](#安全漏洞攻击)
1. [JS压缩细节](#js压缩细节)
1. [垃圾回收](#垃圾回收)
1. [兼容特殊浏览器、PC与WAP加载不同资源的方案](#兼容特殊浏览器pc与wap加载不同资源的方案)
1. [前端与服务端配合方式](#前端与服务端配合方式)
1. [JavaScript范围](#javascript范围)
1. [JS模块化方案](#js模块化方案)

### 前端涉及内容
![前端涉及内容图1](./images/fe-tech-1.png)

>更详细线路图：[developer-roadmap](https://github.com/kamranahmedse/developer-roadmap/blob/master/README.md#-front-end-roadmap)。

1. 从本质上讲，所有Web应用都是一种运行在网页浏览器中的软件，这些软件的GUI（Graphical User Interface，图形用户界面）即为前端。
2. 服务端Node与各种终端的涌现，让前端进入了大前端范畴，这时的前端，已远远不只是浏览器端的页面实现技术，而是后端服务与人机界面的连接器。

    ![前端涉及内容图2](./images/fe-tech-2.png)

### 前端工程化
>参考[张云龙：前端工程——基础篇](https://github.com/fouber/blog/issues/10)。

1. 第一阶段：库/框架选型

    >提升开发效率。（使用自动化工具也能够提升开发效率，如浏览器自动刷新、IDE）
2. 第二阶段：简单构建优化

    >提升运行性能。

    对代码进行压缩、校验，以页面为单位进行简单的资源合并。
3. 第三阶段：JS/CSS模块化开发

    >提升维护效率。

    **分而治之**
    1. [JS模块化方案](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/前端内容/README.md#js模块化方案)：

        CommonJS/AMD/CMD/ES6 Module/UMD
    2. CSS模块化方案：

        sass/less/stylus等预处理器的import、mixin特性支持实现。
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

        解决思路：
        1. 静态资源管理系统 = 资源表 + 资源加载框架
        2. [大公司的静态资源优化方案](https://github.com/fouber/blog/issues/6)：

            1. 配置超长时间的本地缓存 —— 节省带宽，提高性能
            2. 采用内容摘要（MD5）作为缓存更新依据 —— 精确的缓存控制
            3. 静态资源CDN部署 —— 优化网络请求
            4. 非覆盖式更新资源 —— 平滑升级

### 页面加载解析步骤
1. DOM构造解析步骤

    >参考[全方位提升网站打开速度：前端、后端、新的技术](https://github.com/xitu/gold-miner/blob/master/TODO/building-a-shop-with-sub-second-page-loads-lessons-learned.md#前端性能)。
    
    ![页面解析步骤图](./images/load-html-1.png)
    
    1. 增量式生成一个文档对象模型（DOM），解析页面内容（HTML标签）。
    
        1. 加载DOM中所有CSS，生成一个CSS对象模型（CSSOM），描述对页面内容如何设置样式。
    
            加载CSS并构造完整的CSSOM之前，**阻塞渲染**（Render Tree渲染被暂停）。
        2. 加载DOM中所有JS，对DOM和CSSOM进行访问和更改。
    
            1. HTML中出现JS，**阻塞解析**（DOM构造被暂停）。
            2. 下载外部脚本或内嵌脚本不用下载。
            3. 等待所有CSS被提取且CSSOM被构造完毕。
            4. 执行脚本，访问、更改DOM和CSSOM。
            5. DOM构造继续进行。
    
            ><details>
            ><summary><code><script></code>的加载、执行</summary>
            >
            >1. 没有`defer`或`async`：立即加载并执行（同步），阻塞解析。
            >2. `defer`：异步加载，在DOM解析完成后、`DOMContentLoaded`触发前执行，顺序执行。
            >
            >    >多个`defer`脚本不一定按照顺序执行，也不一定会在`DOMContentLoaded`事件触发前执行，因此最好只包含一个延迟脚本。
            >3. `async`：异步加载，加载完马上执行。
            >
            >    乱序执行，仅适用于不考虑依赖、不操作DOM的脚本。
            >4. 模块化属性（在JS内部`import`的同级资源是并行、依赖资源是串行）：
            >
            >    1. `type="module"`：与`defer`相同。
            >    2. `type="module" async`：与`async`相同。
            >
            >![JS脚本加载图](./images/js-load-1.png)
    2. DOM（parse HTML）和CSSOM（recalculate style）构造完成后，进行渲染：
    
        Render Tree（渲染树）：Layout -> Paint -> Composite
    
        >1. 一定要等待外链资源加载完毕（包括加载失败）才可以继续构建DOM或CSSOM。
        >2. 只有可见的元素才会进入渲染树。
        >3. DOM不存在伪元素（CSSOM中才有定义），伪元素存在render tree中。
    
    >无论阻塞渲染还是阻塞解析，资源文件会不间断按顺序加载。
2. 事件完成顺序

    1. 解析DOM；
    2. 执行同步的JS和CSS

        1. 加载外部JS（和CSS）；
        2. （CSSOM先构造完毕）解析并执行JS；
    3. 构造DOM完毕（同步的JS会暂停DOM解析，CSSOM的构建会暂停JS执行）；
        
        完毕后触发：JS的`document.addEventListener('DOMContentLoaded', function(){}, false)` 或 jQuery的`$(document).ready(function(){})`。
    4. 加载图片、媒体资源等外部文件；
    5. 资源加载完毕。
    
        完毕后触发：JS的`window.addEventListener('load', function(){}, false)`。

- 判断JS、CSS文件是否加载完毕：

    1. JS

        1. 监听文件的`load`事件，触发则加载完成。
        2. 监听JS文件的`readystatechange`事件，当文件的`readyState`值为`loaded/complete`则JS加载完成。
    2. CSS

        1. 监听文件的`load`事件，触发则加载完成。
        2. 轮询CSS文件的`cssRules`属性是否存在，当存在则CSS加载完成。
        3. 写一个特殊样式，轮询判断这个样式是否出现，来判断CSS加载完成。

### 浏览器缓存
1. [HTTP定义的缓存机制](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/HTTP相关/README.md#http缓存)
2. 其他缓存机制（不建议方式）

    1. HTML的`<meta>`设置缓存情况：

        e.g. 设置不缓存：

        ```html
        <meta http-equiv="pragma" content="no-cache">
        <meta http-equiv="cache-control" content="no-cache">
        <meta http-equiv="expires" content="0">
        ```
    2. `<html>`的`manifest`应用程序缓存：

        ```html
        <html manifest=".manifest文件/.appcache文件">
        ```

### 前端“增量”原则
1. “增量”原则：

    >“增量下载”是前端在工程上有别于客户端GUI软件的根本原因。

    前端应用没有安装过程，其所需程序资源都部署在远程服务器，用户使用浏览器访问不同的页面来加载不同的资源，随着页面访问的增加，渐进式地将整个程序下载到本地运行。
2. 由“增量”原则引申出的前端优化技巧几乎成为了**性能优化**的核心：

    1. 加载相关：延迟加载、AJAX加载、按需加载、预加载、请求合并压缩等策略。
    2. 缓存相关：缓存更新、缓存共享、非覆盖式更新资源等方案。
    3. 复杂的BigRender、BigPipe、Quickling、PageCache等技术。

### 网站性能优化
1. 从输入URL到页面完成的具体优化：

    >性能优化是一个[工程](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/前端内容/README.md#前端工程化)问题。

    1. URL输入：

        服务端对HTTP请求、资源发布和缓存、服务器配置的优化。

        1. 服务器开启gzip。

            >前端查看Response头是否有：`Content-Encoding: gzip`。
        2. 减少DNS查找，设置合适的TTL值，避免重定向。
        3. 使用CDN。
        4. [静态资源和API分开域名放置](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/前端内容/README.md#静态资源使用额外域名domain-hash的原因)，减少cookie。
        5. 对资源进行缓存：

            1. 减少~~内嵌JS、CSS~~，使用外部JS、CSS。
            2. 使用[缓存相关HTTP头](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/HTTP相关/README.md#http缓存)：`Expires` `Cache-Control` `Last-Modified/If-Modified-Since` `ETag/If-None-Match`。
            3. 配置超长时间的本地缓存，采用内容摘要（MD5）作为缓存更新依据。
        6. [非覆盖式更新资源](https://github.com/fouber/blog/issues/6)。
    2. [载入页面](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/前端内容/README.md#页面加载解析步骤)：

        前端对具体代码性能、CRP（Critical Rendering Path，关键渲染路径，优先显示与用户操作有关内容）的优化。

        1. 优化CRP：

            1. 减少关键资源、减少HTTP请求：

                1. 资源合并、去重。
                2. 非首屏资源延迟异步加载：

                    1. 增量加载资源：

                        1. [图片的延迟加载](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/JS方法积累/实用方法/README.md#jquery图片延时加载)。
                        2. AJAX加载（如：[滚动加载](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/JS方法积累/实用方法/README.md#jquery滚动加载)）。
                        3. 功能文件按需加载（模块化、组件化）。
                    2. 使AJAX可缓存（当用GET方式时添加缓存HTTP头：`Expires` `Cache-Control` `Last-Modified/If-Modified-Since`）。
                3. 利用空闲时间[预加载](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/JS学习笔记/README.md#预加载)。
                4. 第三方资源异步加载（`<script>`添加`defer/async`属性、动态创建或修改`<script>`）。
                5. 避免使用空链接的`<img>`、`<link>`、`<script>`、`<iframe>`（老版本浏览器依旧会请求）。
            2. 最小化字节：

                1. 压缩资源。
                2. 图片优化

                    1. 压缩。
                    2. 小图合并雪碧图。

                        >大图切小图：单个大文件需要多次HTTP请求获取。
                    3. 合理使用Base64、使用WebP、使用`srcset`属性。
            3. 缩短CRP长度：

                CSS放在HTML顶部，JS放在HTML底部。
        2. 技术上优化：

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
                4. 高频事件（如`scroll`、`mousemove`、`touchmove`）使用[函数防抖、函数节流](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/JS学习笔记/README.md#函数防抖函数节流)，避免在高频事件中进行运行时间长的代码。
                5. 避免强制同步布局、避免布局抖动。
                6. 使用`Web Worker`处理复杂的计算。
                7. 正则表达式尽可能准确地匹配目标字符串，以减少不必要的回溯。
            3. HTML：

                1. 减少层级嵌套。
                2. 在拥有`target="_blank"`的`<a>`中添加`rel="noopener"`。

>优先优化对性能影响大、导致瓶颈的部分。

2. 网络应用的生命期建议：

    1. load

        1000ms内完成CRP。
    2. idle

        进行50ms内的空闲时期预加载，包括图片、多媒体文件、后续内容（如评论）。
    3. animations

        保证16ms/f的浏览器渲染时间。
    4. response

        100ms内对用户的操作做出响应。

### 静态资源使用额外域名（domain hash）的原因
1. cookie free

    cookie是同源（且同路径），不同域名可以避免~~某些静态资源携带不必要的cookie而占用带宽~~。
2. 浏览器对同一域名有HTTP并发数限制

    1. 客户端：PC端口数量有限（65536个）、线程切换开销大。
    2. 服务端：服务器的负载、并发接收限制。
3. 动静分离，静态资源方便做CDN

    将网站静态资源（HTML、JS、CSS、图片、字体、多媒体资源等）与后台应用（API）分开部署。

    1. 缺点：

        1. 需要处理[跨域请求](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/JS学习笔记/README.md#跨域请求)。
        2. 不利于SEO。
        3. 开发量大。
    2. 优点

        1. cookie free和HTTP并发限制的需要。
        2. API更加便利、易维护。
        3. 前后端分离开发。
        4. 减轻API服务端压力。

### 安全漏洞攻击
1. XSS

    跨站脚本（Cross-Site Scripting，XSS）是恶意代码注入网页。利用用户对指定网站的信任。

    1. 攻击方式

        >所有可输入的地方，若没有对输入数据进行处理的话，则都存在XSS漏洞。

        - 通过巧妙的方法注入恶意指令代码（HTML、JS或Java，VBScript，ActiveX，Flash）到网页内容，使用户加载并执行恶意程序。

            攻击成功后，能够：盗取用户cookie、破坏页面结构、重定向到其它地址等。
    2. 防御措施：

        1. 过滤用户输入（白名单）。
        2. HttpOnly

            cookie设置为HttpOnly不能在客户端使用~~document.cookie~~访问。
        3. 过滤技术：浏览器的XSS Auditor、W3C的Content-Security-Policy。

        >flash的安全沙盒机制配置跨域传输：crossdomian.xml
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

            操作请求需要提供额外的**不保存在浏览器上、保存在页面表单中**的随机校验码。可以放进请求参数、或自定义HTTP请求头。
3. 其他攻击

    1. DNS攻击

        使域名指往不正确的IP地址。

        1. 攻击方式

            1. 针对DNS服务器：DDoS攻击。
            2. 针对用户：DNS欺骗或劫持（访问恶意DNS服务器）、DNS缓存服务器投毒或污染、本机劫持（hosts文件篡改、本机DNS劫持、SPI链注入、DHO插件）。
        2. 防御措施

            1. 使用安全的DNS服务器。
            2. VPN或域名远程解析。
            3. 查杀病毒，清空DNS缓存。
    2. SQL注入（SQL Injection）

        运行非法的SQL。
    3. OS命令注入攻击（OS Command Injection）

        通过Web应用，执行非法的操作系统命令。
    4. HTTP头部注入攻击（HTTP Header Injection）

        通过在响应头部字段内插入换行，添加任意响应头部或主体。
    5. 邮件头部注入攻击（Mail Header Injection）

        向邮件头部To或Subject内任意添加非法内容，可对任意邮件地址发送广告邮件或病毒邮件。
    6. 目录遍历攻击（Directory Traversal，Path Traversal）

        对本无意公开的文件目录，通过非法截断其目录路径后，达成访问目的。
    7. 远程文件包含漏洞（Remote File Inclusion）

        当部分脚本内容需要从其他文件读入时，利用指定外部服务器的URL充当依赖文件，让脚本读取之后，就可运行任意脚本。
    8. 强制浏览（Forced Browsing）

        从安置在Web服务器的公开目录下的文件中，浏览那些原本非自愿公开的文件。
    9. 不正确的错误消息处理（Error Handling Vulnerability）

        Web应用的错误信息内包含对攻击者有用的信息。
    10. 开放重定向（Open Redirect）

        假如指定的重定向URL到某个具有恶意的Web网站，那么用户就会被诱导至那个Web网站。
    11. 会话劫持（Session Hijack）

        通过某种手段拿到了用户的会话ID，并非法使用此会话ID伪装成用户。
    12. 会话固定攻击（Session Fixation）

        强制用户使用攻击者指定的会话ID。
    13. 点击劫持（ClickJacking）、界面伪装（UI Redressing）

        利用透明的按钮或链接做成陷阱，覆盖在Web页面上。然后诱使用户在不知情的情况下，点击那个链接访问内容。
    14. 密码破解（Password Cracking）

        1. 穷举法（Brute-force Attack，暴力破解法）

            对所有密钥集合构成的密钥空间（Keyspace）进行穷举。即，用所有可行的候选密码对目标的密码系统试错。
        2. 字典攻击

            利用事先收集好的候选密码（经过各种组合方式后存入字典），枚举字典中的密码。

            >如生日日期数值化。

        - 一种安全的服务端存储密码方式：

            先利用给密码加盐（salt）的方式增加额外信息，再使用散列（hash）函数计算出散列值后保存。

            ><details>
            ><summary>加盐</summary>
            >
            >由服务器随机生成的一个字符串，保证长度足够长，且是真正随机生成。然后把它和密码字符串相连接（前后都可以）生成散列值。当两个用户使用了同一个密码时，由于随机生成的salt值不同，对应的散列值也将不同。这样一来，很大程度上减少了密码特征，攻击者也就很难利用自己手中的密码特征库进行破解。
            ></details>
    15. DoS攻击（Denial of Service attack）、服务停止攻击或拒绝服务攻击

        运行中的服务呈停止状态的攻击。

        1. 集中利用访问请求造成资源过载。

            DDoS（Distributed Denial of Service attack）利用多台计算机发起Dos攻击。
        2. 通过攻击安全漏洞使服务停止。
    16. Hash Collision DoS

        >参考[HASH COLLISION DOS 问题](http://coolshell.cn/articles/6424.html)。

        Hash碰撞的拒绝式服务攻击（Hash Collision DoS）是对服务器进行恶意负载。

        1. 攻击方式

            >1. Hash：把任意长度的输入，通过散列算法，输出固定长度的散列值。
            >2. Hash Collision DoS：利用各语言Hash算法的“非随机性”，制造出无数value不同、key相同的数据，让Hash表成为一张单向链表，而导致整个网站的运行性能下降。

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

### JS压缩细节
>来自[Javascript代码压缩细节](http://div.io/topic/447)。

试着生成新的代码，对比后输出最短的内容。

1. 去除注释、多余的分隔符与空白符，标识符简写。
2. 压缩表达式

    1. 表达式预计算

        将可预先计算的表达式替换成其计算结果，并比较原来表达式与生成后的结果的大小，取短的。
    2. 优化`true/false`

        1. `true`

            1. 在`==/!=`运算 -> `1`
            2. 其他运算 -> `!0`
        2. `false`

            1. 在`==/!=`运算 -> `0`
            2. 其他运算 -> `!1`
    3. 优化`&&/||`

        1. `true && 表达式` -> `表达式`
        2. `false && 表达式` -> `!1`
        3. `true || 表达式` -> `!0`
        4. `false || 表达式` -> `表达式`
3. 缩短运算符

    1. `===/!==`的两个操作数都是`String`类型或都是`Boolean`类型的，缩短成`==/!=`。
    2. 缩短赋值表达式

        对于类似`a = a + b`这样的赋值表达式（`+` `-` `*` `/` `%` `>>` `<<` `>>>` `|` `&` `^`），可以缩短成`a += b`。
    3. `!`操作符的压缩

        对于`!(a>=b)`，若转换后`a<b`得到更短的代码，则转换。
4. 去除没用的声明

    1. 去除重复的指示性字符串，如`"use strict"`。
    2. 去除没有使用的函数参数。
    3. 去除函数表达式的函数名（如果没有引用）。
    4. 去除没用的块语句。
    5. 去除没有使用的`break`。
    6. 去除没有引用的`label`。
5. 压缩`while`

    1. 去除根本不会执行的`while`（`while(false){}`）。
    5. `while(true){}` -> `for(;;){}`
6. `条件判断 ? 表达式1 : 表达式2`

    1. 若`条件判断`有`!`，则去除`!`且调换表达式前后位置。
    2. 若`条件判断`为常数，则直接缩短为某一个表达式。
7. 压缩语句块

    1. 连续的表达式语句合并成一个逗号表达式`,`。
    2. 多个`var`声明可以压缩成一个`var`声明。
    3. `return`之后的非变量声明、非函数声明可以去除。
    4. 合并块末尾的`return`语句及其前边的多条表达式语句。
8. 优化`if`

    1. 去除没用的、空的`if/else`分支
    2. 尝试反转`if/else`分支，看看生成代码是否更短。
    3. 如果`if`块里边仅有一个`if`语句，且`else`块为空，那么可以合并这两个`if`。
    4. 如果`if`最后一个语句是跳出控制语句，那么可以把`else`块的内容提到`else`外边，然后去掉`else`。
    5. 如果`if/else`里各仅有一条`return`语句，则可以合并这两句`return`。
    6. 如果`if/else`里各仅有一条语句，则可以转换为三元运算符表达式。
    7. 如果`if/else`其中一个块为空，另一个块仅有一条语句，则可以转化成`||/&&`表达式。

>[移动时代的前端加密](http://div.io/topic/1220)。

### 垃圾回收
>垃圾回收器会按照固定的时间间隔（或代码执行中预定的时间）周期性地执行，找出不再继续使用的变量，然后释放其占用的内存。

垃圾回收器必须跟踪并判断变量是否有用，对于不再有用的变量打上标记，以备将来回收。

1. **标记清除（mark-and-sweep）**（现代浏览器使用方式）

    垃圾回收器在运行时给存储在内存中的所有变量加上标记；然后，去掉环境中的变量以及被环境中变量引用的变量的标记；最后，对那些带标记的值进行释放。
2. 引用计数（reference counting）

    跟踪记录每个值被引用的次数，被引用一次加1，引用取消就减1，当引用次数为0时，则说明没有办法再访问这个值了，当垃圾回收器下次运行时，释放引用次数为0的值所占空间。

    >可能产生一个严重的问题：循环引用，引用次数永远不会是0。

>用`变量 = null;`等方法，让变量成为零引用，从而进行清除元素、垃圾回收（导致内存泄露的情况除外）。

### 兼容特殊浏览器、PC与WAP加载不同资源的方案
1. 不同页面URL入口。
2. 引入资源前，根据UA判断是否加载特殊资源。

    >1. 引入资源：[同步/异步加载资源](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/JS方法积累/实用方法/README.md#原生js动态添加脚本样式)
    >2. UA判断：[判断所在系统](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/JS方法积累/实用方法/README.md#原生js判断所在系统)、[判断移动平台](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/JS方法积累/实用方法/README.md#原生js判断移动平台)、[判断ie所有版本](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/JS方法积累/实用方法/README.md#原生js判断ie所有版本)
3. 把特殊资源打包进总体代码，再根据UA判断引入。
4. 服务端根据HTTP请求的UA判断输出不同页面加载不同资源（BFF层）。

### 前端与服务端配合方式
1. 并行（优先）：

    1. 先与服务端对接预期API，服务端产出API文档；
    2. 前端根据文档通过Mock方式开发；
    3. 当服务端API开发完毕后再用真实API加入前端页面（仅关闭Mock即可）。
2. 串行：

    服务端比前端提前一个版本，交付的内容包括API+文档。

- API文档确定的字段，就算为空，也必须按照文档要求返回` `或`[]`或`{}`，不允许返回内容丢失字段。

### JavaScript范围
>ECMAScript是JavaScript的标准，狭义的JavaScript指ECMAScript。浏览器、Node.js都是JavaScript的运行环境。

JavaScript ＝ ECMAScript + 宿主环境提供的API。

1. 浏览器（web应用）的JavaScript包括：

    1. ECMAScript：描述该语言的语法和基本对象。
    2. Web API：

        1. 文档对象模型（DOM）：描述处理网页内容的方法和接口。
        2. 浏览器对象模型（BOM）：描述与浏览器进行交互的方法和接口。
2. Node.js的JavaScript包括：

    1. ECMAScript：描述该语言的语法和基本对象。
    2. 操作系统的API：

        1. 操作系统（OS）。
        2. 文件系统（file）。
        3. 网络系统（net）。
        4. 数据库（database）。

### JS模块化方案
>参考[关于AMD,CMD,CommonJS及UMD规范](http://blog.gejiawen.com/2015/11/03/what-is-amd-cmd-commonjs-umd/)。

![JS模块化方案图](./images/js-module-1.png)

1. [CommonJS规范](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/Node.js学习笔记/README.md#commonjs规范)。
2. [ES6 Module](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/前端内容/标准库文档.md#ecmascript-2015es6新增)的14。
