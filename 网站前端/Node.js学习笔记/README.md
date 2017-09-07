# Node.js学习笔记

### nvm更新Node.js版本
1. macOS或Linux的[nvm](https://github.com/creationix/nvm)：

    ```bash
    nvm list-remote
    nvm install v新版本号
    nvm use v新版本号
    nvm alias default v新版本号

    nvm list
    nvm uninstall v旧版本号
    ```
2. Windows的[nvm-windows](https://github.com/coreybutler/nvm-windows)：

    ```bash
    nvm node_mirror https://npm.taobao.org/mirrors/node/    #设置node源：
    nvm npm_mirror https://npm.taobao.org/mirrors/npm/      #设置npm源：

    nvm list available
    nvm install v新版本号
    nvm use v新版本号

    nvm list
    nvm uninstall v旧版本号
    ```

>切换版本之后需重装Node.js模块包。

### npm
1. 命令

    1. 登录

        `npm login`
    2. 初始化`package.json`

        `npm init --yes`
    3. 发布

        `npm publish`
2. 安装包

    1. 作用域

        1. 本地：在本地被`require`引入后使用。
        2. 全局：在命令行中使用。
    2. 安装方式

        1. `package.json`（`npm install`）

            >`主版本号.次版本号.补丁号`，详细定义查看[Semantic](http://semver.org/lang/zh-CN/)。

            安装时自动选择相对最新版本号。

            1. 最新（主版本号最新）：

                `*`、`x`
            2. 次版本号最新：

                `1`、`1.x`、`^1.2.3`
            3. 补丁号最新：

                `1.2`、`1.2.x`、`~1.2.3`
            4. 确定的版本：

                `1.2.3`
        2. `npm install 包`

            1. 没有后缀，则最新版
            2. `@版本`

                1. 具体版本号
                2. `latest`
                3. 版本范围：`>`、`>=`、`<`、`<=` + 版本号
3. `package.json`

    1. `dependencies`

        生产环境依赖。
    2. `devDependencies`

        开发、测试依赖。
4. 包的制作-使用

    1. 制作：
    
        按照`CommonJS`规范制作
    2. 使用：
    
        1. 在Node.js环境下使用（`require`）

            >如`vue-cli`。
        2. 在浏览器环境下使用

            用打包工具（webpack等）打包成能够在浏览器运行的JS代码、或直接制作可兼容在浏览器环境运行的代码。

            >如`Vue.js`。