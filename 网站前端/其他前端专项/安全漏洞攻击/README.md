### 安全漏洞攻击
>[代码安全指南](https://github.com/Tencent/secguide)。

1. XSS

    跨站脚本（Cross-Site Scripting，XSS）是恶意代码注入网页。利用用户对指定网站的信任。

    1. 攻击方式

        >风险取决于不可信数据最终如何写入页面。作为纯文本展示的内容与被浏览器解析为 HTML 或脚本的内容，需要不同的处理。

        - 通过巧妙的方法注入恶意指令代码（HTML、JS、Flash、`<iframe>`，任何能写url的地方包含`javascript: 可执行代码`）到网页内容，使用户加载并执行恶意程序。

            攻击成功后，能够：盗取用户cookie、破坏页面结构、重定向到其它地址、利用用户机器执行各种非客户意愿的行为（如：发起请求、向其他网站发起DDoS攻击）等。
    2. 防御措施：

        1. 按输出位置处理不可信数据

            纯文本用 `textContent`；业务需要富文本时，用维护中的净化库限制标签、属性和 URL 协议。`encodeURI` 本身无法验证 URL 的协议。[OWASP XSS 防御指南](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)

            >e.g. [js-xss](https://github.com/leizongmin/js-xss)
        2. HttpOnly

            `HttpOnly` 限制脚本通过 `document.cookie` 读取该 Cookie；浏览器仍会在符合条件的请求中携带它。
        3. 开启浏览器CSP（Content-Security-Policy，内容安全策略），设置不允许加载白名单外的域名资源

            >指令细节：[MDN：Content-Security-Policy](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Headers/Content-Security-Policy)。

            1. HTTP响应头：

                `Content-Security-Policy: 具体指令`
            2. `.html`的`<meta>`

                `<meta http-equiv="Content-Security-Policy" content="具体指令">`
            - 脚本策略未放行 `'unsafe-eval'` 时，浏览器会阻止 `eval`、`new Function` 和字符串形式的定时器回调；可以向定时器传入函数。
2. CSRF

    跨站请求伪造（Cross-Site Request Forgery，CSRF）是 第三方网站 挟制用户 在已登录的网页上执行非本意操作。利用网站对用户浏览器的信任。

    1. 攻击方式

        - 当用户已经得到目标网站的认可后，在第三方网站 对 目标网站 进行请求操作。

            潜在影响取决于用户权限、浏览器携带的凭证和服务端对该操作的校验。
    2. 防御措施

        1. 校验来源，限制跨站凭证

            1. 对更改状态的请求，服务端可校验 `Origin`，缺失时再核对 `Referer` 的来源是否匹配受信任源。

                >地址栏直接输入内容不会提供`Referer`。
            2. 同源策略和 CORS 会限制跨源脚本读取响应，但跨站表单仍可发送请求。
            3. 给会话 Cookie 显式设置合适的 `SameSite`。它按「站点」判断；`Lax` 仍允许部分跨站顶层导航携带 Cookie。
        2. 添加校验token

            >同步令牌模式中，服务端为会话生成不可预测的 CSRF token，并在更改状态时校验它。[OWASP CSRF 防御指南](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)

            页面通过表单字段或自定义请求头回传令牌，避免将其写入 URL。
        3. 验证码

            对敏感操作可要求二次确认或重新认证。
        4. `POST`请求替代`GET`请求

            >`GET` 应用于读取。改用 `POST` 表达状态变更后，服务端仍需校验 CSRF token 或采用等效防护。
3. 其他攻击

    1. 注入型劫持

        通过在正常的网页中注入广告代码（JS代码、`<iframe>`、其他标签等），实现页面弹窗提醒或者底部广告等。

        1. 攻击方式

            运营商劫持。
        2. 防御措施

            全链路HTTPS（若使用CDN，则必须CDN请求和回源都是HTTPS）。

            >额外增加劫持难度：前端还可以用[子资源完整性（SRI）](https://developer.mozilla.org/zh-CN/docs/Web/Security/子资源完整性)验证加载文件的哈希摘要。
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

            使用专门的密码哈希算法（如 Argon2id），为每个密码生成独立的随机盐，保存算法参数、盐和结果。[OWASP 密码存储指南](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

            ><details>
            ><summary>加盐</summary>
            >
            >盐可以和结果一起保存。相同密码使用不同的盐会产生不同结果，避免多个账户共用一份预计算结果。常用密码哈希库会代为生成盐并编码参数。
            ></details>
    16. DoS攻击（Denial of Service attack）、服务停止攻击或拒绝服务攻击

        运行中的服务呈停止状态的攻击。

        1. 集中利用访问请求造成资源过载。

            DDoS（Distributed Denial of Service attack）利用多台计算机发起Dos攻击。
        2. 通过攻击安全漏洞使服务停止。
    17. Hash Collision DoS

        >参考：[Wikipedia：Hash flooding](https://en.wikipedia.org/wiki/Hash_flooding)。

        Hash碰撞的拒绝式服务攻击（Hash Collision DoS）是对服务器进行恶意负载。

        1. 攻击方式

            >1. Hash：把任意长度的输入，通过散列算法，输出固定长度的散列值。
            >2. 不同的键可能落入同一个桶。碰撞过多时，插入和查找的开销可能上升，具体影响取决于哈希表如何处理碰撞。
        2. 防御措施

            1. 升级hash算法。
            2. 限制POST参数个数和请求长度。
            3. 防火墙检测异常请求。

- 验证码

    仅能预防机器行为：防止广告机注册、发帖、评论，防止暴力破解密码。

    1. 服务端生成图片，前端根据图片发送请求给服务端验证。
    2. ~~前端生成并验证~~。
