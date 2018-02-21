# [whistle](https://github.com/avwo/whistle)使用

1. 启动

    ```bash
    whistle run     # 前台启动
    whistle start   # 后台启动
    whistle stop    # 后台停止
    whistle restart # 后台重启

    # w2是whistle命令的简写
    ```
2. 调试

    >默认代理端口为`8899`。

    1. 被调试的设备设置HTTP代理：`电脑ip:8899`

        >PC可以用系统的HTTP代理设置，也可以用浏览器的代理设置（如SwitchyOmega）。
    2. 电脑Chrome打开查看调试：`127.0.0.1:8899`或`127.0.0.1:8900`
3. **Rules**

    >`#`为注释符号。

    1. 设置hosts、代理转发

        ```bash
        # 不带IP地址
        请求域名 指向域名

        # 带IP地址（IP地址均为指向地址）
        请求域名 指向的IP地址:端口号
        指向的IP地址:端口号 请求域名
        ```
    2. 本地替换

        ```bash
        URL file:///User/username/test   # macOS、Linux
        URL file://E:\xx\test            # Windows的路径分隔符可以用 \ 或者 /
        ```
    4. 在页面**末尾**注入内容HTML、JS、CSS内容

        ```bash
        # macOS、Linux
        URL html:///User/xxx/test/test.html
        URL js:///User/xxx/test/test.js
        URL css:///User/xxx/test/test.css

        # Windows的路径分隔符可以用 \ 或者 /
        URL html://E:\xx\test\test.html
        URL js://E:\xx\test\test.js
        URL css://E:\xx\test\test.css
        ```
    5. 在响应的body**开头**或**末尾**注入HTML内容（可以注入`<script>`、`<link>`）

        >因为是插入至响应的body，因此URL要具体到某一个html文件才行，否则会导致所有请求都添加一遍HTML内容。

        1. 开头

            ```bash
            URL resPrepend://{变量名}
            ```
        2. 末尾

            ```bash
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
    6. log信息

        >开启后会阻止把错误信息输入到vconsole和eruda。

        1. 获取页面的`console`和错误信息

            ```bash
            URL log://
            ```
        2. 加载完毕后运行脚本（并且获取页面的`console`和错误信息）

            ```bash
            # 在Values设置的'变量名'作为加载完成后输出的JS内容
            URL log://{变量名}

            # 本地JS脚本
            URL log://E:\xx\test\test.js
            URL log:///User/xxx/test/test.js
            ```
    7. **Weinre**查看页面结构

        >开启后会阻止把`console`输入到vconsole和eruda。

        ```bash
        域名 weinre://变量名
        ```

    - 所有协议均支持以下匹配方式

        1. 域名（端口号、请求协议）
        2. 路径
        3. 正则
        4. 精确匹配（`$`）
        5. 通配符匹配（`*`、`**`）
        6. 通配路径匹配（`~`）
4. **Values**

    配置resPrepend、log等协议中添加的`{变量名}`的HTML内容或JS脚本。
5. **Network**

    查看右边`log->console`抓取的页面console信息（需要设置**Rules**的log协议）。
