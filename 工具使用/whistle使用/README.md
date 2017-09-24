# [whistle](https://github.com/avwo/whistle)使用（还有很多问题）

>因为实现原理和`vConsole`冲突，因此开启`whistle`后无法再在`vConsole`获取信息。但是可以选择**在页面开头注入html**中带着`vConsole`，查看交互操作前的问题。

1. 启动

    ```bash
    whistle start   # 启动
    whistle stop    # 停止
    whistle restart # 重启
    ```
2. 调试移动端

    >默认代理端口为`8899`。

    1. 移动端HTTP代理：`电脑ip:8899`
    2. 电脑Chrome打开：`127.0.0.1:8899`
3. **Rules**

    1. 设置hosts、请求转发

        ```bash
        域名1 域名2
        ```
    2. 本地替换

        ```bash
        域名 file:///User/username/test   # Mac、Linux
        域名 file://E:\xx\test            # Windows的路径分隔符可以用 \ 或者 /
        ```
    4. 在页面末尾注入html、js、css

        ```bash
        # Mac、Linux
        域名 html:///User/xxx/test/test.html
        域名 js:///User/xxx/test/test.js
        域名 css:///User/xxx/test/test.css
        
        # Windows的路径分隔符可以用 \ 或者 /
        域名 html://E:\xx\test\test.html
        域名 js://E:\xx\test\test.js
        域名 css://E:\xx\test\test.css
        ```
    5. 在页面开头注入html（可以注入`<script>`、`<link>`）

        ```bash
        域名 resPrepend://{变量名}
        ```

        在**Values**设置的'变量名'为html内容，可以写入：文本、`<script>`作为JS、<link>作为CSS。

        >外部链接的地址最好使用外网CDN，不要使用本地服务器地址。
    6. **Weinre**查看页面结构

        ```bash
        域名 weinre://变量名
        ```
    7. log信息

        ```bash
        # 在Values设置的'变量名'作为log内容
        域名 log://{变量名}

        # 本地js脚本
        域名 log://E:\xx\test\test.js
        域名 log:///User/xxx/test/test.js
        ```
4. **Values**

    配置log协议中添加的`变量名`的js脚本。
5. **Network**

    查看右边`log->console`抓取的页面console信息（不需要设置任何Rules即可抓取）。