### [whistle](https://github.com/avwo/whistle)使用
1. 启动

    ```shell
    whistle run     # 前台启动

    whistle start   # 后台启动
    whistle stop    # 后台停止
    whistle restart # 后台重启
    whistle status  # 后台运行信息展示

    # w2是whistle命令的简写

    # 运行参数
    -p 「端口号数字，默认8899」
    -t
    ```
2. 配置原则

    1. 相同协议规则的默认优先级从上到下，即前面的规则优先级匹配高于后面。

        >与传统的hosts配置优先级相反。
    2. 一些属于不同协议，但功能有冲突的规则，按常用优先级为`rule`>`host`>`proxy`。
    3. 部分相同协议会匹配及合并所有可以匹配的规则。
    4. 建议：

        ```text
        127.0.0.1 xxx.com/dev node.xxx.com/dev xxx.com/node/dev

        proxy://127.0.0.1:12639 xxx.com/gtimg/

        htmlPrepend://路径 xxx.com

        10.175.102.200 xxx.com excludeFilter://*/gtimg/

        proxy://127.0.0.1:12639?host=9.68.155.53 xxx.com

        # 因为优先级的原因，若要低优先级的先匹配，则可以把高优先级的规则改为与低优先级一致的规则
        proxy://127.0.0.1:12639?host=9.97.141.32 xxx.com/proxy?g_tk
        # 127.0.0.1 xxx.com # host优先级高于proxy，此行规则会优先于上一行
        proxy://127.0.0.1:12639?host=127.0.0.1 xxx.com # 同一种规则，越上面的越优先
        ```
3. **Rules**

    >`#`为注释符号。

    1. 设置hosts、代理转发

        ```text
        # 不带IP地址
        请求域名 指向域名

        # 带IP地址（IP地址均为指向地址）
        请求域名 指向的IP地址:端口号
        指向的IP地址:端口号 请求域名
        ```
    2. 代理转发

        ```text
        URL proxy://127.0.0.1:「端口号」?host=「IP地址」    # URL通过 本地映射「端口号」的应用 去转发「IP地址」
        ```
    3. 本地替换

        ```text
        URL file:///User/username/test   # macOS、Linux
        URL file://E:\xx\test            # Windows的路径分隔符可以用 \ 或者 /
        ```
    4. 往`content-type`为`html`的响应内容的前面或后面添加文本内容

        ```text
        URL htmlPrepend://文件路径
        URL htmlAppend://文件路径
        ```
    5. 在页面**末尾**注入内容HTML、JS、CSS内容

        ```text
        # macOS、Linux
        URL html:///User/xxx/test/test.html
        URL js:///User/xxx/test/test.js
        URL css:///User/xxx/test/test.css

        # Windows的路径分隔符可以用 \ 或者 /
        URL html://E:\xx\test\test.html
        URL js://E:\xx\test\test.js
        URL css://E:\xx\test\test.css
        ```
    6. 在响应的body**开头**或**末尾**注入HTML内容（可以注入`<script>`、`<link>`）

        >因为是插入至响应的body，因此URL要具体到某一个html文件才行，否则会导致所有请求都添加一遍HTML内容。

        1. 开头

            ```text
            URL resPrepend://{变量名}
            ```
        2. 末尾

            ```text
            URL resAppend://{变量名}
            ```

        在**Values**设置的`变量名`为HTML内容，可以写入：HTML文本、`<script>`作为JS、`<link>`作为CSS。

        >外部链接的地址最好使用外网CDN，不要使用本地服务器地址。

        ><details>
        ><summary>e.g.</summary>
        >
        >```html
        ><!--在Values中写入vconsole-->
        ><script src="//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/vconsole/3.0.0/vconsole.min.js"></script>
        ><script>new VConsole()</script>
        >
        ><!--在Values中写入eruda-->
        ><script src="//cdn.jsdelivr.net/npm/eruda"></script>
        ><script>eruda.init()</script>
        >
        ><!--在Values中写入style-->
        ><style>
        >a {color: red;}
        ></style>
        >
        ><!--在Values中写入HTML内容-->
        ><p>这是whistle插入内容</p>
        >```
        ></details>
    7. log信息

        >开启后会阻止把错误信息输入到vconsole和eruda。

        1. 获取页面的`console`和错误信息

            ```text
            URL log://
            ```
        2. 加载完毕后运行脚本（并且获取页面的`console`和错误信息）

            ```text
            # 在Values设置的'变量名'作为加载完成后输出的JS内容
            URL log://{变量名}

            # 本地JS脚本
            URL log://E:\xx\test\test.js
            URL log:///User/xxx/test/test.js
            ```
    8. **Weinre**查看页面结构

        >开启后会阻止把`console`输入到vconsole和eruda。

        ```text
        域名 weinre://变量名
        ```
    9. excludeFilter

        前面的规则，排除一下路径。

        ```text
        URL 匹配规则 excludeFilter://*/xx/xxx/  # 匹配的规则，排除后面的路径
        ```

    - 所有协议均支持以下匹配方式

        1. 域名（端口号、请求协议）
        2. 路径
        3. 正则
        4. 精确匹配（`$`开头）
        5. 通配符匹配（`^`、`$`、`*`）

            支持`$0`到`$9`获取通配符。
3. **Values**

    配置resPrepend、log等协议中添加的`{变量名}`的HTML内容或JS脚本。
4. **Network**

    查看右边`log->console`抓取的页面console信息（需要设置**Rules**的log协议）。
