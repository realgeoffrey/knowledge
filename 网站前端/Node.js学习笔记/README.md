# Node.js学习笔记

## 目录
1. [安装](#安装)

    1. [nvm更新Node.js版本](#nvm更新nodejs版本)
    1. [n更新Node.js版本](#n更新nodejs版本)
1. [npm](#npm)
1. [CommonJS规范](#commonjs规范)
1. [原理机制](#原理机制)

    1. [Node.js的运行机制](#nodejs的运行机制)
    1. [特性](#特性)
    1. [Node.js原生模块（需要`require`引入）](#nodejs原生模块需要require引入)
    1. [Node.js全局变量](#nodejs全局变量)
    1. [Tips](#tips)
1. [工具使用](#工具使用)

    1. [Koa](#koa)
    1. [pm2](#pm2)

---
## 安装

### nvm更新Node.js版本
1. macOS或Linux的[nvm](https://github.com/creationix/nvm)：

    ```shell
    nvm list-remote
    nvm install v新版本号
    nvm use v新版本号
    nvm alias default v新版本号

    nvm list
    nvm uninstall v旧版本号     # 若无法删除，则用管理员权限按要求设置文件夹权限，还可以去目录删除 /Users/「用户名」/.nvm/versions/node/v「版本号」
    ```

    >安装的全局软件包位置：`/Users/「用户名」/.nvm/versions/node/v「版本号」/lib/node_modules`
2. Windows的[nvm-windows](https://github.com/coreybutler/nvm-windows)：

    >安装nvm-windows时，需要删除原本安装在电脑上的Node.js。

    ```shell
    nvm node_mirror https://npm.taobao.org/mirrors/node/    # 设置node源
    nvm npm_mirror https://npm.taobao.org/mirrors/npm/      # 设置npm源

    nvm list available
    nvm install 新版本号
    nvm use 新版本号

    nvm list
    nvm uninstall 旧版本号      # 还可以再去目录中删除 C:\Users\「用户名」\AppData\Roaming\nvm\v「版本号」
    ```

>切换版本之后需重装Node.js的全局模块包。

### [n](https://github.com/tj/n)更新Node.js版本
>不支持Windows。

1. 安装

    ```shell
    npm install -g n

    # 或：brew、curl
    ```
2. 切换版本

    ```shell
    n ls


    # 安装最新的长期支持正式发布版本
    n lts

    # 安装最新正式发布版本
    n latest

    # 安装指定版本
    n 新版本号


    # 展示已经安装的版本，并选择使用哪个版本
    n


    # 删除指定版本
    n rm 旧版本号

    # 删除当前版本之外的所有版本
    n prune

    # 删除当前版本安装的node和npm
    n uninstall
    ```

---

### npm
npm（Node Package Manager）。

1. `npm`CI

    >在任意命令后添加`-h`、`--help`查看当前命令的所有参数。

    1. 制作

        1. 登录

            `npm login`
        2. 初始化`package.json`

            `npm init`

            - 修改初始化信息

                ```shell
                npm set init.author.name "名字"
                npm set init.author.email "邮箱"
                npm set init.license "MIT"
                ```

                >初始化信息会存放在`~/.npmrc`文件里。
        3. 调试开发

            `npm link`、`npm unlink`

            1. 仅本地

                1. 引用本地模块的仓库：`npm link 本地模块的路径`

                    - 取消：

                        引用本地模块的仓库：`npm unlink 模块名`
            2. 全局

                1. 本地模块：`npm link`

                    也支持bin。

                    - 取消：

                        本地模块：`npm unlink`
                2. 引用本地模块的仓库：`npm link 模块名`

                    - 取消：

                        引用本地模块的仓库：`npm unlink 模块名`
        4. 发布（默认：发布至`latest`标签）

            `npm publish [--tag <tag>]`

            >1. 除了latest，其他标签都不会默认被安装。最后推送的latest版本会显示在npm官网。
            >2. 注意：设置源为npm的网站（https://registry.npmjs.org/）才可以推送到npm。
        5. 「下线」

            >`npm unpublish [<@scope>/]<pkg>[@<version>]`只能下线24小时内发布的版本。

            `npm deprecate <pkg>[@<version>] <message>`
        6. 打印登录名

            `npm whoami`
        7. 登出

            `npm logout`
    2. 查看信息

        1. 查看模块官方信息

            `npm view [<@scope>/]<pkg>[@<version>] [<field>[.subfield]...]`

            - `npm view <pkg> versions`：展示所有版本
        2. 查看已安装的模块和依赖

            `npm list [[<@scope>/]<pkg> ...]`

            >仅查看顶层依赖：`npm list --depth=0`
        3. 查看已安装模块是否需要升级

            `npm outdated [[<@scope>/]<pkg> ...]`
        4. 查看、添加、删除仓库标签的最后版本

            >每个标签仅保留最后一个版本；latest标签无法删除。

            ```shell
            npm dist-tag ls [<pkg>]
            npm dist-tag add <pkg>@<version> [<tag>]
            npm dist-tag rm <pkg> <tag>
            ```
    3. 安装

        > 改变安装包的顺序会影响安装包的内容和依赖。

        - 手动安装npm自己

            1. 在本地Node.js同目录下创建目录`node_modules\npm`；
            2. 下载并解压<https://github.com/npm/cli/releases>至本地Node.js同目录下的`node_modules\npm`；
            3. 拷贝`node_modules\npm\bin`下面的`npm`、`npm.cmd`（、`npx`、`npx.cmd`）到本地Node.js同目录下。

        1. 安装包

            自动选择范围内最后发布的版本，安装到本地或全局的`node_modules`。全局安装会额外创建系统命令。

            1. 安装方式

                1. `npm install`安装所在目录的`package.json`文件描述内容

                    1. 最新（主版本号最新，第一个数）：

                        `*`、`x`
                    2. 次版本号最新（第二个数）：

                        `1`、`1.x`、`^1.2.3`
                    3. 补丁号最新（第三个数）：

                        `1.2`、`1.2.x`、`~1.2.3`
                    4. 确定的版本：

                        `1.2.3`

                    >`主版本号.次版本号.补丁号`，详细定义查看[Semantic](http://semver.org/lang/zh-CN/)。
                2. `npm install [<@scope>/]<name>[@<tag>]`

                    1. 没有后缀，则最后发布的latest版本。
                    2. `@内容`

                        1. 具体版本号
                        2. 标签
                        3. 版本范围：`>`、`>=`、`<`、`<=` + 版本号。范围中最后发布的版本。

                            >e.g. `npm install npm-devil@">=0.0.1 <0.0.5"`
                3. 参数

                    1. `--force`、`-f`：强制重新安装。

                        >当目录中已经存在指定模块，默认：不会重新安装已经安装的模块。或删除`node_modules`目录再重新安装。
                    2. `--save`、`-S`：安装信息保存到`package.json`的`dependencies`（执行时依赖插件）。
                    3. `--save-dev`、`-D`：安装信息保存到`package.json`的`devDependencies`（开发时依赖插件）。
                    4. `--save-optional`、`-O`：安装信息保存到`package.json`的`optionalDependencies`。
            2. 作用域

                1. 本地：在本地被`require`引入后使用。
                2. 全局：在命令行中使用，或被全局命令引用。
        2. 升级

            `npm update [-g] [<pkg>...]`

            升级成功会把升级版本号自动写入`package.json`。

            >只更新顶层模块，而不更新依赖的依赖。可以使用`npm --depth 9999 update`更新依赖的依赖。

            - 升级npm自己

                1. macOS：`npm install -g npm`
                2. Windows：

                    >来自：[npm-windows-upgrade](https://github.com/felixrieseberg/npm-windows-upgrade)。

                    1. 以管理员身份运行[PowerShell](https://github.com/powershell/powershell)（Windows 7 SP1以上的系统自带）
                    2. 在PowerShell内执行

                        ```shell
                        Set-ExecutionPolicy Unrestricted -Scope CurrentUser -Force
                        npm install -g npm-windows-upgrade
                        npm-windows-upgrade
                        ```
        3. 卸载

            `npm uninstall [<@scope>/]<pkg>[@<version>]... [--save-prod|--save-dev|--save-optional] [--no-save]`
        4. 重装npm

            `curl -L https://www.npmjs.org/install.sh | sh`

            >若还是无法使用npm，建议重装Node.js。
        5. 验证缓存（垃圾收集不需要的数据、验证缓存的完整性）

            `npm cache verify`

            > - 除非回收磁盘空间，否则不要使用以下清空npm缓存
            >
            >    `npm cache clean -f`

        - `package-lock.json`

            更新成功（`npm update`）或第一次安装（`npm install`）时生成，用以记录当前状态下实际安装的各个npm包的具体来源和版本号。在存在此文件的根目录进行`npm install`，会按照完全相同的依赖关系进行安装。

            >1. 若使用lock机制，则应该将`package-lock.json`提交到版本控制。
            >2. 若不使用lock机制，则应该把`package-lock=false`加入`.npmrc`，并把`.npmrc`提交到版本控制。

            1. `version`：版本号
            2. `resolved`：软件包位置
            3. `integrity`：校验码
    4. 执行脚本

        1. `npm run 「package.json中scripts字段的命令」 -- 「添加脚本后面的参数」`

            >非`-`开头的参数可以忽略`--`而传递。e.g. `npm run gulp runCss`等价于：`npm run gulp -- runCss`
        2. [npx](https://github.com/zkat/npx)

            >1. 去`node_modules/.bin`路径检查命令是否存在，找到之后执行；
            >2. 找不到，就去环境变量`$PATH`里，检查命令是否存在，找到之后执行;
            >3. 还是找不到，自动下载一个临时的依赖包最新版本在一个临时目录，然后再运行命令，运行完之后删除，不污染全局环境。
2. [`package.json`](https://docs.npmjs.com/files/package.json)字段

    包描述、说明文件。

    1. `name`

        仓库名。

        >组成：小写、无空格、字母数字下划线中划线。
    2. `version`

        版本号`x.x.x`。

        >`npm version [<newversion> | major | minor | patch | premajor | preminor | prepatch | prerelease | from-git]`更新`version`。
    3. `dependencies`

        生产环境依赖。

        >[node_modules 困境](https://zhuanlan.zhihu.com/p/137535779)。

        1. 安装依赖（`npm install`）是从（项目根目录）最外层往（引用处）最里层安装，若本层已经有同名但不同版本的库文件夹，则往里层尝试安装；
        2. 引用依赖是从（引用处）最里层往（项目根目录）最外层引用，一旦找到库目录就检索完毕。

        <details>
        <summary>e.g.</summary>

        1. 项目依赖逻辑：

            ```text
            .
            └── package.json
                .dependencies
                ├── A.v1
                |   .dependencies
                |   ├── B.v1
                |   ├── C.v1
                |   └── D.v1
                └── B.v2
                    .dependencies
                    ├── A.v2
                    └── C.v2
                        .dependencies
                        ├── A.v3
                        |   .dependencies
                        |   └── D.v1
                        └── D.v2
            ```
        2. `npm install`后的文件结构：

            ```text
            .
            ├── node_modules/
            |   ├── A.v1/
            |   |   └── node_modules/
            |   |       └── B.v1/
            |   ├── B.v2/
            |   |   └── node_modules/
            |   |       ├── A.v2/
            |   |       ├── C.v2/
            |   |       |   └── node_modules/
            |   |       |       └── A.v3/
            |   |       |           └── node_modules/
            |   |       |               └── D.v1/   # 注意，D.v1又安装了一遍
            |   |       └── D.v2/   # 注意，是C.v2引用D.v2，但安装在这里
            |   ├── C.v1/
            |   └── D.v1/
            |
            └── package.json
            ```
        </details>
    4. `devDependencies`

        开发、测试依赖。

        >- 何时不被安装：
        >
        >    1. 项目不会安装依赖库的`devDependencies`。
        >    2. `NODE_ENV`值为`production`时，项目不会安装自己的`devDependencies`。
        >
        >        >`export NODE_ENV=production;`。
        >    3. `npm install --production`不会安装自己的`devDependencies`。
    5. `main`

        代码入口，默认：`index.js`。

        >引用仓库的代码入口，不在引用链路内的仓库文件最终不会被使用到。

        - 其他非官方的代码入口（若不存在则退回`main`）：

            1. `module`：ES6 Module
            2. `unpkg`：`<script>`引用（针对[unpkg.com](https://unpkg.com/)）
            3. `jsdelivr`：`<script>`引用（针对[www.jsdelivr.com](https://www.jsdelivr.com/)）
    6. `scripts`

        可执行脚本，用`npm run 脚本名`执行。

        - `pre脚本名`会在执行`脚本名`之前自动执行。
    7. `files`

        将仓库作为依赖项安装时要包含的路径、文件的数组。
    8. `bin`

        `{ 新增的命令: 对应的可执行文件路径 }`
    9. `engines`

        该仓库在哪个版本的Node.js（、npm、yarn、等）上运行。
    10. `browserslist`

        支持哪些浏览器（及其版本）。
    11. `description`

        描述，也作为在npm官网被搜索的内容。
    12. `repository`

        仓库远程版本控制，可以是github等。

        ><details>
        ><summary>e.g.</summary>
        >
        >```json
        >"repository": {
        >    "type": "git",
        >    "url": "git@github.com:用户名/仓库名.git"
        >}
        >
        >// 针对monorepo：
        >"repository": {
        >  "type": "git",
        >  "url": "https://github.com/用户名/仓库名.git",
        >  "directory": "packages/文件夹名"
        >}
        >```
        ></details>
    13. `keywords`

        在npm官网被搜索的关键字。
    14. `author`

        仓库作者。
    15. `contributors`

        仓库贡献者。
    16. `license`

        证书。
    17. `homepage`

        主页。
    18. `bugs`

        链接到软件包的问题跟踪器，最常用的是GitHub的issues页面。
    19. `private`

        设置为`true`，则无法`npm publish`，用于避免不小心公开项目。
    20. 命令特有的属性

        某些命令特有的（如：ESLint的`eslintConfig`、Babel的`babel`、等），可以在相应的命令/项目文档中找到如何使用它们。
    21. 其他
3. 包的制作-使用

    1. 制作：

        按照[CommonJS规范](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/Node.js学习笔记/README.md#commonjs规范)编写代码。
    2. 使用：

        1. 在Node.js环境下使用（`require`）

            >如：`vue-cli`。
        2. 在浏览器环境下使用

            1. 用打包工具（`webpack`、`browserify`、`rollup`）打包成能够在浏览器运行的JS代码。
            2. 直接制作可兼容在浏览器环境运行的代码。

            >如：`Vue.js`。
    - 作用域的包

        `@scope/project-name`
4. `.npmrc`

    npm的配置文件，手动或用`npm config`进行修改。

    >`npm config ls -l`查看所有已有配置和默认配置。

    - 常用：`package-lock`、`registry`。
    - 注释：`;`或`#`。

>项目中使用某个开源库时，要考虑它的License和文件大小（若使用webpack打包，则可以使用[webpack-bundle-analyzer](https://github.com/webpack-contrib/webpack-bundle-analyzer)进行分析）。

### CommonJS规范
>参考：[阮一峰：require() 源码解读](http://www.ruanyifeng.com/blog/2015/05/require.html)、[CommonJS 详细介绍](https://neveryu.github.io/2017/03/07/commonjs/)、[阮一峰：JavaScript 模块的循环加载](http://www.ruanyifeng.com/blog/2015/11/circular-dependency.html)。

一个模块就是一个Node.js文件。

>主模块：通过命令行参数传递给Node.js以启动程序的模块，负责调度组成整个程序的其它模块完成工作。如：`node 文件名`、`package.json`的`main`。

- 概述

    1. 执行阶段（运行时）进行模块加载：确定模块的依赖关系、输入和输出的变量。

        因为本身就是**动态引入**，`module.exports`和`require`能够在任何位置使用（包括块级作用域）。
    2. 有自己单独作用域，不污染全局作用域，必须`module.exports`才能输出给其他模块。

        >不推荐`window.属性`。
    3. 模块的加载逻辑：

        1. 模块加载的顺序：按照其在代码中出现的顺序、引用则嵌套加载。
        2. 注入`exports`、`require`、`module`三个全局变量。
        3. 执行模块的源码：

            1. `require`第一次加载某模块，执行整个脚本，在内存生成一个缓存对象：

                `{ id: '...', exports: {...}, loaded: true/false, ... }`
            2. a模块执行时出现`require(b)`则进入b模块代码中执行，执行完毕后再回到a模块继续向下执行。
            3. 无论加载多少次，仅在第一次加载时运行，之后再被引用则直接返回已导出内容。

                >除非手动清除系统缓存。
            4. 「循环加载」（circular dependency）

                引用之前已经被引用过的模块b，会直接返回模块b已导出的内容，而不会再进入模块b内执行。

                <details>
                <summary>e.g.</summary>

                ```javascript
                // 按①②③④⑤⑥的顺序执行


                // 入口
                ... // ①
                require('a模块'); // ②③④⑤执行后，②⑤导出a模块的内容2
                ... // ⑥


                // a模块
                ... // ②
                require('b模块'); // ③④执行后，③④导出b模块的内容
                ... // ⑤


                // b模块
                ... // ③
                require('a模块'); // ②导出a模块的内容1（因为a模块已经被引用过，所以直接使用a已经导出的内容，而不继续执行a的剩余代码）
                ... // ④
                ```
                </details>
        4. 将模块的`exports`值输出至缓存，以供其他模块`require`获取（或「循环加载」时，部分已经执行产生的`exports`供其他模块引用）。
        5. 若被`require`的模块没有`exports`，则仅执行一遍模块代码，返回`{}`。
    4. `require(a模块)`返回内存中a模块的`module.exports`指向的值（值传递），`require`的内容可以重新赋值和属性改写（重新赋值将不再使用模块引用；属性改写会改变a模块的缓存值，所有`require(a模块)`都会共享）。

        1. 输出的模块内容是一个被复制的值，这个值缓存起来以便其他模块复制引用，这个缓存值可以被本模块修改。
        2. `require`只是使用缓存起来的内容。已经引用模块后，被引用的模块内部再次修改导出内容，不会影响已经引用过的值（修改属性还是会影响）。

        ><details>
        ><summary>e.g.</summary>
        >
        >```javascript
        >var a = 'a1'
        >module.exports.a = a      // 此时引用则获得`a1`的复制
        >setTimeout(() => {
        >  a = 'a2'                // 不会改变a的输出。此时引用则还是获得`a1`的复制
        >}, 500)
        >
        >
        >module.exports.b = 'b1'   // 此时引用获得`b1`的复制
        >setTimeout(() => {
        >  module.exports.b = 'b2' // 重新输出b。此时引用则获得`b2`的复制
        >}, 500)
        >```
        ></details>
    5. CommonJS是一个单对象输出、单对象加载的模型：

        1. 所有要输出的对象统统挂载在`module.exports`上，然后暴露给外界。
        2. 通过`require`加载别的模块，`require`的返回值就是模块暴露的对象。
1. `module.exports`

    模块提供使用的`exports`值。

    - 允许用两种方式为导出赋值：

        1. `module.exports = 值`
        2. `module.exports.属性 = 值`

        >1. `exports`指向`module.exports`（`exports === module.exports`）。
        >2. 若`exports = 值`或`module.exports = 值`则切断了`exports`与`module.exports`的连接，`exports`将没有导出效果。
2. `require(X)`

    加载模块。读取并执行一个JS文件（`.js`后缀可以省略），返回该模块的`exports`值（没有导出内容则为`{}`）。

    >1. 被引入的内容就可以被各种解构。
    >2. 注意文件名大小写，可能导致引用路径失败（针对：开发时的系统大小写不敏感，上线或其他机器运行时系统大小写又敏感的情况）。

    - <details>

        <summary>查找逻辑</summary>

        >官方解析：[Modules: All together](https://nodejs.org/api/modules.html#all-together)。

        ![Node.js的require流程图](./images/nodejs-require-1.jpg)

        1. 若 X 以（绝对路径）`/`或（相对路径）`./`、`../`开头

            1. 根据 X 所在的父模块，确定 X 的绝对路径。
            2. 将 X 当成**文件**，依次查找下面文件，只要其中有一个存在，就返回该文件，不再继续执行。

                `X`、`X.js`、`X.json`、`X.node`
            3. 将 X 当成**目录**，依次查找下面文件，只要其中有一个存在，就返回该文件，不再继续执行。

                `X/package.json（main字段）`、`X/index.js`、`X/index.json`、`X/index.node`
        2. 若 X 是内置模块，则返回该模块，不再继续执行。

            >e.g. `require('http')`
        3. 若 X 不带路径且不是内置模块

            >当作安装在本地的模块。

            1. 根据 X 所在的父模块，确定 X 可能的安装目录。
            2. 依次在每个目录中，将 X 当成**文件**或**目录**加载。

                若当前目录找不到，向上一层搜索 X。
        4. 抛出`Error: Cannot find module 'X'`。

        ><details>
        ><summary>e.g.</summary>
        >
        >- 在`/home/xx/projects/foo.js`执行了`require('bar')`：
        >
        >    1. 属于不带路径情况，判断不是内置模块，当作安装在本地的模块进行搜索；
        >    2. 依次搜索每一个目录：
        >
        >        ```text
        >        /home/xx/projects/node_modules/
        >        /home/xx/node_modules/
        >        /home/node_modules/
        >        /node_modules/
        >        ```
        >
        >        1. 搜索时，先将`bar`当作文件名，依次在`某某/node_modules/`尝试加载下面文件：
        >
        >            `bar`、`bar.js`、`bar.json`、`bar.node`
        >        2. 若都不成功，则说明`bar`可能是目录名，依次在`某某/node_modules/`尝试加载下面文件：
        >
        >            ```text
        >            bar/package.json（main字段）
        >            bar/index.js
        >            bar/index.json
        >            bar/index.node
        >            ```
        >    3. 都找不到则抛出`Error: Cannot find module 'bar'`。
        >- `require('foo')`，将会按如下顺序查找模块：
        >
        >    1. `./node_modules/foo`
        >    2. `../node_modules/foo`
        >    3. `../../node_modules/foo`
        >    4. 直到系统的根目录
        >- `require('foo/bar')`，将会按如下顺序查找模块：
        >
        >    1. `./node_modules/foo/bar`
        >    2. `../node_modules/foo/bar`
        >    3. `../../node_modules/foo/bar`
        >    4. 直到系统的根目录
        ></details>

        </details>
3. `module`

    - 当前模块对象。拥有以下属性：

        1. `module.id`：模块的识别符，通常是带有绝对路径的模块文件名。
        2. `module.filename`：模块的文件名，带有绝对路径。
        3. `module.loaded`：返回一个布尔值，表示模块是否已经完成加载。
        4. `module.parent`：返回一个对象，表示调用该模块的模块。
        5. `module.children`：返回一个数组，表示该模块要用到的其他模块。
        6. `module.exports`：表示模块对外输出的值。
        7. `module.paths`：返回一个数组，模块文件默认搜索目录（`某某/node_modules/`）。

    >所有模块都是Node.js内部`Module`构建函数的实例。

---
## 原理机制

### Node.js的运行机制
1. V8引擎解析JS脚本。
2. 解析后的代码，调用Node.js的API。
3. [libuv](https://github.com/libuv/libuv)负责Node.js的API的执行。将不同的任务分配给不同的线程，形成一个Event Loop（事件循环），以异步的方式将任务的执行结果返回给V8引擎。
4. V8引擎再将结果返回给用户。

>JS本身的`throw-try-catch`异常处理机制并不会导致内存泄漏，也不会让程序的执行结果出乎意料，但Node.js并不是存粹的JS。Node.js里大量的API内部是由C/C++实现，因此Node.js程序的运行过程中，代码执行路径穿梭于JS引擎内部和外部，而JS的异常抛出机制可能会打断正常的代码执行流程，导致C/C++部分的代码表现异常，进而导致内存泄漏等问题。

![Node.js的事件循环图](./images/nodejs-system-1.png)

### 特性
1. 单线程

    不为单个客户端连接创建一个新的线程，而仅仅使用单一线程支持所有客户端连接。通过非阻塞I/O和事件驱动机制，让Node.js程序宏观上并行。

    1. 优点：没有线程创建、销毁的时间开销；不需维护多个线程耗费的内存，可同时处理更多的客户端连接；运行中的单线程CPU利用率饱和。
    2. 缺点：若单一客户端连接造成线程的阻塞或奔溃，则影响所有客户端连接。

    >Java、PHP或.NET等服务器语言，会为每一个客户端连接创建一个新的线程或使用协程。
2. 非阻塞I/O

    回调函数异步执行，通过事件循环检查已完成的I/O进行依次处理。

    >1. I/O主要指由[libuv](https://github.com/libuv/libuv)支持的，与系统磁盘和网络之间的交互。
    >2. 大多数Node.js核心API所提供的异步方法都遵从惯例：**错误信息优先**的回调模式（Error-first Callback，第一个参数是错误信息，若不报错则其值为`null`）。
    >
    >    `EventEmitter`类事件函数不属于此范畴。
3. 事件驱动

    用事件驱动（事件循环）来完成服务器的任务调度。

>1. Node.js开发应用程序：善于I/O（任务调度），不善于计算。如：长连接的实时交互应用程序。
>2. Node.js服务器：没有根目录概念，没有web容器。URL通过顶层路由设计，呈递静态文件。
>
>只有打通和后端技术的桥梁、实现互联互通，Node.js才能在公司业务中有更长远的发展。

### Node.js[原生模块](http://nodejs.cn/api/)（需要`require`引入）
>核心模块定义在[源代码的lib/目录](https://github.com/nodejs/node/tree/master/lib)。

1. `http`：HTTP请求相关API

    1. 接口永远不会缓冲整个请求或响应，所以用户可以流式地传输数据。
    2. 为了支持所有可能的HTTP应用程序，Node.js的HTTP API都是非常底层的。

        它仅进行流处理和消息解析。它将消息解析为消息头和消息主体，但不会解析具体的消息头或消息主体。

    ><details>
    ><summary>e.g.</summary>
    >
    >1. Node.js原生处理POST请求
    >
    >    ```javascript
    >    const http = require('http')
    >
    >    http.createServer((req, res) => {
    >      if (req.method === 'POST') {
    >        let body = '';
    >        req.on('data', chunk => {
    >          body += chunk.toString();
    >        });
    >        req.on('end', () => {
    >          console.log(body);       // body是POST请求body
    >          // 接受完成，可返回`res.end('ok')`
    >        });
    >      }
    >    })
    >      .listen(3000, '0.0.0.0')
    >    ```
    >2. Node.js原生发起POST请求
    >
    >    ```javascript
    >    const http = require("http");
    >
    >    const req = http.request(
    >      路径,
    >      {
    >        method: "POST",
    >        headers: {
    >          "Content-Type": "application/json; charset=UTF-8",
    >        },
    >      },
    >      (res) => {
    >        res.setEncoding("utf8");
    >        let body = "";
    >        res.on("data", (chunk) => {
    >          body += chunk || "";
    >        });
    >        res.on("end", () => {
    >          console.log(body);       // body是POST请求后返回的响应body
    >          // 返回接受完成
    >        });
    >      }
    >    );
    >
    >    req.on("error", (e) => {
    >      console.warn(e);
    >    });
    >
    >    req.write(JSON.stringify({ a: "发起的请求body" })); // 保证：发起请求的body和请求头匹配
    >    req.end();
    >    ```
    ></details>
2. `http2`
3. `https`
4. `fs`：文件操作API

    提供版本：异步、同步（+`Sync`）、基于Promise（`require("fs").promises`）。

    ><details>
    ><summary>e.g.</summary>
    >
    >```javascript
    >// 异步（结果在回调）
    >require('fs').rename('before.json', 'after.json', err => {
    >  if (err) {
    >    return console.error(err)
    >  }
    >  //完成
    >})
    >
    >
    >// 同步（阻塞线程，直到文件操作结束。结果在执行语句返回）
    >try {
    >  require('fs').renameSync('before.json', 'after.json')
    >  //完成
    >} catch (err) {
    >  console.error(err)
    >}
    >
    >
    >// Promise
    >require("fs").promises
    >  .rename("before.json", "after.json")
    >  .then((data) => {
    >    console.log('succeeded', data);
    >  })
    >  .catch((error) => {
    >    console.error('failed' ,error);
    >  });
    >```
    ></details>

    - 尽量选择使用**流**读写文件的内容

        >（不使用流的）读操作都会在返回数据之前将文件的全部内容读取到内存中，这意味着大文件会对内存的消耗和程序执行的速度产生重大的影响；（不使用流的）写操作都是在将全部内容写入文件之后才会将控制权返回给程序（在异步的版本中，这意味着执行回调）。

        - 导出文件需求：

            1. 后端返回json数据（无法利用流技术，只能完整保存在服务端内存中），前端根据数据生成文件并[创建下载](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/JS方法积累/实用方法/README.md#原生js点击下载)。
            2. 后端直接返回文件，前端请求下载文件（get请求）

                1. 利用流技术，创建并保存文件在服务端；
                2. 利用流技术，把刚刚保存的文件传递给前端进行下载。
5. `events`：事件触发器

    >`EventEmitter`类：`require('events')`

    1. 所有能触发事件的对象都是`EventEmitter`类的实例。
    2. `EventEmitter`以注册的顺序同步地调用所有监听器。
6. `path`：处理文件路径

    >e.g. 当前文件所在目录的相对位置：`require('path').resolve(__dirname, '../../xx/xxx.txt')`
7. `url`：解析URL。
8. `os`：基本的系统操作函数
9. `stream`：数据流

    流是一种以高效的方式处理读/写文件、网络通信、或任何类型的端到端的信息交换。

    >e.g. 在传统的方式中，当告诉程序读取文件或通信时，这会将文件或信息从头到尾读入内存，然后进行处理。若使用流，则可以逐个片段地读取并处理（而无需全部保存在内存中），能够一边读取一边处理更加高效。

    1. 所有的流都是`EventEmitter`类的实例。
    2. Node.js提供了多种流对象（`fs`、`http`、`process`等都有流操作方式），除非要创建新类型的流实例，否则极少需要直接使用`stream`。
    3. 流类型：可读（Readable）、可写（Writable）、可读可写（Duplex）、可修改或转换数据（Transform）。
10. `readline`：用于一次一行地读取可读流中的数据
11. `util`：提供常用函数的集合，用于弥补核心JavaScript的功能过于精简的不足
12. `child_process`：衍生子进程

    衍生的Node.js子进程独立于父进程，但两者之间建立的IPC通信通道除外。每个进程都有自己的内存，带有自己的V8实例。

    >由于需要额外的资源分配，因此不建议衍生大量的Node.js子进程。
13. `cluster`：集群

    创建共享服务器端口的子进程。为了充分利用多核系统，有时需要启用一组Node.js进程去处理负载任务。
14. `worker_threads`：并行地执行JS的线程
15. `dgram`：数据报

    对UDP socket的一层封装。
16. `net`：用于创建基于流的TCP或IPC的服务器（`net.createServer`）与客户端（`net.createConnection`）

    - Experimental功能

        1. `require('net').createQuicSocket`：QUIC（快速UDP网络连接，Quick UDP Internet Connections）
17. `dns`：解析域名
18. `querystring`：解析和格式化URL查询字符串
19. `string_decoder`：字符串解码器
20. `tls`：实现安全传输层（TLS）及安全套接层（SSL）协议，建立在OpenSSL的基础上
21. `module`：模块
22. `perf_hooks`：性能钩子

    实现w3c的Performance API的子类。
23. `assert`：断言
24. `repl`：REPL（交互式解释器）

    - 终端使用Node.js的REPL：

        1. `_`

            打印最后一次操作结果（不执行语句、没有副作用）。
        2. `.help`、`.editor`、`.break`、`.clear`、`.load`、`.save`、`.exit`
        3. 可以直接使用系统模块，不需要`require`引入。e.g. REPL中`http === require('http')`。
25. `tty`：终端
26. `v8`：V8的api
27. `vm`：提供V8虚拟机上下文中进行编译和运行代码
28. `crypto`：加密

     OpenSSL的哈希、HMAC、加密、解密、签名、以及验证功能的一整套封装。

    - Experimental功能

        1. `require('crypto').webcrypto`：实现Web Crypto API规范
29. `zlib`：提供`Gzip、Deflate/Inflate、Brotli`的压缩功能

- Experimental功能

    1. `inspector`：与V8调试器交互
    2. `wasi`：实现WebAssembly系统接口规范
    3. `diagnostics_channel`：诊断
    4. `trace_events`：跟踪事件
    5. `async_hooks`：异步钩子去跟踪异步资源

### Node.js[全局变量](http://nodejs.cn/api/globals.html)
Node.js的全局对象`global`是全局变量的宿主。

1. 仅在模块内有效

    1. `require`
    2. `exports`
    3. `module`
    4. `__filename`：当前正在执行的脚本所在文件夹的绝对路径+文件名。
    5. `__dirname`：当前正在执行的脚本所在文件夹的绝对路径。
2. `process`：描述当前Node.js进程状态的对象，提供了一个与操作系统的简单接口。

    1. `process.cwd()`：运行node命令时所在文件夹的绝对路径。
3. `Buffer`：二进制数据流。

    可以将buffer视为整数数组：数组的每一项都是整数，并代表一个数据字节。
4. `queueMicrotask`

    将微任务放入队列以便调用回调。
5. `MessageChannel`、`MessageEvent`、`MessagePort`
6. `setImmediate/clearImmediate`
7. 其他全局变量（类似于浏览器的全局对象<code>window</code>所包含的全局变量）

    1. `setTimeout/clearTimeout`、`setInterval/clearInterval`
    2. `console`
    3. `URL`、`URLSearchParams`
    4. `Error`

        >若在程序执行过程中引发了**未捕获的异常**或**未捕获的失败Promise实例**，则程序将崩溃。捕获未捕获的异常：
        >
        >1. 捕获未捕获的异常
        >
        >    ```javascript
        >    process.on('uncaughtException', err => {
        >      // 执行逻辑
        >    })
        >    ```
        >2. 捕获未捕获的失败Promise实例
        >
        >    ```javascript
        >    process.on('unhandledRejection', err => {
        >      // 执行逻辑
        >    })
        >    ```
    5. `debugger`

        1. `node inspect 脚本.js`：命令行调试
        2. `node --inspect 脚本.js`：与Chrome配合调试（默认：`--inspect=127.0.0.1:9229`。开启远程调试：`--inspect=「公共IP或0.0.0.0」:9229`）

            >有时因为运行的代码，就算退出了程序也无法关闭占用inspect的9229（默认）端口。需要手动杀死占用端口的进程，e.g. `lsof -i :9229`然后`kill -9 「PID」`。

            - `--debug-brk`：直接从第一行代码开始进行断点调试。
    6. `TextDecoder`、`TextEncoder`
    7. `WebAssembly`

    - Experimental功能

        1. `AbortController`、`AbortSignal`
        2. `Event`、`EventTarget`

### Tips
1. 调试方法：

    1. 控制台输出`console`等。
    2. 通过Chrome的 <chrome://inspect/#devices>，监听Node.js程序运行`node --inspect 文件`，可以使用`debugger`等进行断点调试。

        >[调试指南](https://nodejs.org/zh-cn/docs/guides/debugging-getting-started/)。
2. 服务端开发注意点：

    1. 相对于客户端，服务端要处理大量并发的请求。

        >需要学习服务端的各种 高并发、数据库IO 解决方案。前端处理客户端问题无法接触到这些，需要重新踩服务端的坑。

        虽然Node.js是单线程，但是各种异步的操作（如：数据库IO等）需要按照服务端的技术解决方案处理。
    2. 基本数据库的使用，以及如何在Node.js中使用。

        如：MySQL、Redis、MongoDB、等。
    3. 异常处理、错误报警

        对各种IO要进行异常处理（如：`try-catch`包裹所有IO代码），并需要把错误上报（打日志`console`或借助第三方监控告警）。
3. 与浏览器JS的区别

    除了全局变量、提供的模块、模块系统、API不同之外，在Node.js中，可以控制运行环境：除非构建的是任何人都可以在任何地方部署的开源应用程序，否则开发者知道会在哪个版本的Node.js上运行该应用程序。与浏览器环境（无法选择访客会使用的浏览器）相比起来，这非常方便。
4. Node.js运行环境退出（命令行执行完毕后自动退出）：

    代码运行完毕。包括：执行队列、任务队列、等待加入任务队列的其他线程任务，全都执行完毕，当不会有新的指令需要执行时，就自动退出Node.js的进程。监听系统端口，意味着还有事件需要待执行。
5. 不管任何情况，始终保证要有回包，就算代码运行错误，也要兜底回包（`.end()`）
6. `node 「传递给Node.js的参数，如：--inspect」 「执行文件」 「传递给执行文件的参数，以空格分隔」`

    1. 执行文件之前的是传递给Node.js运行的参数，有特定值，错误参数会报错。
    2. 执行文件之后的是传递进执行文件使用的（`process.argv`），可以输入任意内容。

    - 命令行执行eval字符串并打印：`node -p "「js代码文本」"`
7. 返回的内容的属性值为`undefined`的，可能会把这个属性去除。
8. 抓包Node.js发起的http/https请求

    1. 本机全局代理到抓包软件、或用Proxifier等软件转发到抓包软件
    2. 或 代码设置Node.js发起请求时通过代理转发

        ><details>
        ><summary>e.g.</summary>
        >
        >1. Node.js的`host`和`port`参数
        >
        >    ```javascript
        >    const http = require("http");
        >    const req = http.request(
        >      {
        >        port: "8899",      // 代理端口
        >        host: "127.0.0.1", // 代理地址
        >
        >        path: "http://127.0.0.1:8080/", // 访问地址
        >        method: "POST",
        >        headers: {
        >          "Content-Type": "application/json; charset=UTF-8",
        >        },
        >      },
        >      (res) => {
        >        res.setEncoding("utf8");
        >        let body = "";
        >        res.on("data", (chunk) => {
        >          body += chunk || "";
        >        });
        >        res.on("end", () => {
        >          console.log(body); // body是POST请求后返回的响应body
        >          // 返回接受完成
        >        });
        >      }
        >    );
        >
        >    req.on("error", (e) => {
        >      console.warn(e);
        >    });
        >
        >    req.write(JSON.stringify({ a: "发起的请求body" })); // 保证：发起请求的body和请求头匹配
        >    req.end();
        >    ```
        >2. [axios](https://github.com/axios/axios)的`proxy`参数
        >3. [request](https://github.com/request/request)的`proxy`参数
        ></details>

---
## 工具使用

### [Koa](https://github.com/koajs/koa)
关键点：级联 + 通过上下文在中间件间传递数据 + ctx.body的值为HTTP响应数据。

1. 级联（Cascading）：中间件按顺序执行，随着第二个参数`next`执行进入执行栈

    >为了能够更好的链式调用中间件，要使用`await next()`或`return next()`的方式，否则虽然会`next`进入下一个中间件，但下一个中间件的异步代码会导致请求先返回之后再处理异步后代码。

    ```javascript
    const Koa = require('koa')
    const app = new Koa()

    // 按照①②③④⑤⑥执行后输出

    app.use(async (ctx, next) => {
      // ①
      await next()
      // ⑥
    })

    app.use((ctx, next) => {
      // ②
      return next().then(() => {
        // ⑤
      })
    })

    app.use((ctx, next) => {
      // ③
      return next()
    })

    app.use(async ctx => {
      // ④
    })

    app.use(async ctx => {
      // 前一个中间件没有执行`next`，因此后面的中间件不再被执行
    })

    app.listen(3000)
    ```
2. `const app = new Koa()`实例

    1. `app.context`

        上下文，可以添加新值
    2. `app.env`

        获取`NODE_ENV`的值（默认：`'development'`）
    3. `app.use(async (上下文, next) => {}))`

        使用中间件
    4. `app.callback()`

        返回一个函数，用于`http.createServer()`的第一个参数
    5. `app.listen(数字)`

        创建并返回HTTP服务器

        - <details>

            <summary>语法糖</summary>

            等价于：

            ```javascript
            const http = require('http');
            const Koa = require('koa');
            const app = new Koa();
            http.createServer(app.callback()).listen(数字);
            ```
            </details>
    6. `app.on('error', (err, ctx) => {})`

        >[koa的错误处理](https://github.com/koajs/koa/blob/master/docs/error-handling.md)。

        错误处理，中间件产生的 未捕获的 同步错误（或同步`ctx.throw`）都会捕获到这里

        >未捕获的异步错误用`process.on('uncaughtException', err => {})`捕获；未捕获的失败Promise实例用`process.on('unhandledRejection', err => {})`捕获。
    7. `app.keys = `

        设置签名的 Cookie 密钥

    - 其他

        1. `app.maxIpsCount`

            从代理 ip 消息头读取的最大ip数（默认：`0`，表示无限）
        2. `app.middleware`

            所有用到的中间件的引用（数组）。
        3. `app.proxy = `

            若设置为`true`，则header fields将被信任
        4. `app.proxyIpHeader`

            代理 ip 消息头（默认：`'X-Forwarded-For'`）
        5. `app.subdomainOffset`

            `.subdomains`忽略的偏移量（默认：`2`）
        6. `app.emit(事件名[, ...args])`

            发起一个`EventEmitter`事件。
        7. `app.request`
        8. `app.response`
3. 上下文（context）

    >`app.context`、中间件的第一个参数。

    每一个请求都将创建一个新的上下文（来自`app.context`），并在中间件间引用传递和新赋值。

    - 对上下文的写入和读取

        1. 写入：

            1. 统一写入`app.context.新属性 = 值`
            2. 中间件写入

                ```javascript
                app.use((ctx) => {
                  ctx.新属性 = 值
                })
                ```
        2. 读取：

            ```javascript
            app.use((ctx) => {
              console.log(ctx.新属性)
            })
            ```

    - HTTP响应的内容：所有中间件执行结束之后的`ctx.body`值

    1. `.request`

        Koa的`Request`

        1. `.header` === `.request.header` === `.headers` === `.request.headers`
        1. `.header=` === `.request.header=` === `.headers=` === `.request.headers=`
        1. `.method` === `.request.method`
        1. `.method=` === `.request.method=`
        1. `.request.length`
        1. `.url` === `.request.url`
        1. `.url=` === `.request.url=`
        1. `.originalUrl` === `.request.originalUrl`
        1. `.origin` === `.request.origin`
        1. `.href` === `.request.href`
        1. `.path` === `.request.path`
        1. `.path=` === `.request.path=`
        1. `.query` === `.request.query`
        1. `.query=` === `.request.query=`
        1. `.querystring` === `.request.querystring`
        1. `.querystring=` === `.request.querystring=`
        1. `.request.search`
        1. `.request.search=`
        1. `.host` === `.request.host`
        1. `.hostname` === `.request.hostname`
        1. `.request.URL`
        1. `.request.type`
        1. `.request.charset`
        1. `.fresh` === `.request.fresh`
        1. `.stale` === `.request.stale`
        1. `.socket` === `.request.socket`
        1. `.protocol` === `.request.protocol`
        1. `.secure` === `.request.secure`
        1. `.ip` === `.request.ip`
        1. `.ips` === `.request.ips`
        1. `.subdomains` === `.request.subdomains`
        1. `.is()` === `.request.is()`
        1. `.accepts()` === `.request.accepts()`
        1. `.acceptsEncodings()` === `.request.acceptsEncodings()`
        1. `.acceptsCharsets()` === `.request.acceptsCharsets()`
        1. `.acceptsLanguages()` === `.request.acceptsLanguages()`
        1. `.request.idempotent`
        1. `.get()` === `.request.get()`
    2. `.response`

        Koa的`Response`

        1. `.response.header` === `.response.headers`
        1. `.body` === `.response.body`
        1. `.body=` === `.response.body=`
        1. `.response.socket`
        1. `.status` === `.response.status`
        1. `.status=` === `.response.status=`
        1. `.message` === `.response.message`
        1. `.message=` === `.response.message=`
        1. `.length` === `.response.length`
        1. `.length=` === `.response.length=`
        1. `.type` === `.response.type`
        1. `.type=` === `.response.type=`
        1. `.headerSent` === `.response.headerSent`
        1. `.redirect()` === `.response.redirect()`
        1. `.attachment()` === `.response.attachment()`
        1. `.response.get()`
        1. `.set()` === `.response.set()`
        1. `.append()` === `.response.append()`
        1. `.remove()` === `.response.remove()`
        1. `.lastModified` ≈ `.response.lastModified`
        1. `.lastModified=` === `.response.lastModified=`
        1. `.etag` ≈ `.response.etag`
        1. `.etag=` === `.response.etag=`
        1. `.response.is()`
        1. `.response.vary()`
        1. `.response.flushHeaders()`
    3. `.state`

        推荐的命名空间，用于通过中间件传递信息。

        ```javascript
        // 前面的中间件设置
        ctx.state.属性1 = 值

        // 后面的中间获得
        ctx.state.属性1
        ```
    4. `.app`

        应用程序实例引用（`const app = new Koa()`）。
    5. `.cookies`

        >使用[cookies](https://github.com/pillarjs/cookies)模块。

        1. `.cookies.get(名[, options])`
        2. `.cookies.set(名[, 值 [, options]])`
    6. `.throw([状态[, 信息[, properties]]])`

        抛出错误（可以被`try-catch`捕获处理）
    7. `.assert(值[, status[, 信息[, properties]]])`

        当`值`为`false`时抛出一个类似`.throw`的错误。与Node.js的`assert()`方法类似.

        e.g. `ctx.assert(ctx.state.user, 401, 'User not found. Please login!');`
    8. `.req`

        Node.js的`Request`
    9. `.res`

        Node.js的`Response`

        - 绕过Koa的`Response`处理是不被支持的. 应避免使用以下Node.js属性：

            1. ~~`res.statusCode`~~
            2. ~~`res.writeHead()`~~
            3. ~~`res.write()`~~
            4. ~~`res.end()`~~
    10. ~~`.respond`~~

        是否绕过Koa的`Response`。
4. 调试模式

    运行前添加环境变量：`DEBUG=koa*`

### [pm2](https://github.com/Unitech/pm2)
后台运行、进程管理（自动重启、永保活动状态、不停机重新加载，显示进程信息，配置进程处理条件）、多进程运行、负载均衡、处理log输出。

1. [`pm2`CI](https://pm2.keymetrics.io/docs/usage/pm2-doc-single-page/)

    `pm2` +

    1. `start`、`stop`、`restart`、`startOrRestart`、`delete`、`reload` + 执行文件、进程名/进程id/all、配置脚本（.js、.json、.yml）

        1. `start 执行文件或配置脚本`

            1. `-- 「参数，已空格分隔」`

                传递进执行脚本。只能用在命令行最后，`--`之后的所有内容都将当做是参数。
            2. `--node-args="「参数」"`

                >相同：`--interpreter-args="「参数」"`。

                传递给Node.js的`node`运行命令（不是~~传递进执行脚本~~），如：`--inspect`。
            3. `--log 「out、error脚本路径」`

                1. `--output 「out脚本路径」`
                2. `--error 「error脚本路径」`
            4. `-i 「进程数：max、-1、数字」`

                cluster模式。

                1. `--merge-logs`

                    当多进程使用同一个进程名时，不用进程id区分log文件（同名的多进程写到同一个log文件）。
            5. `--watch`

                监听改动文件后重新执行指令（先kill再重启）

                1. `--ignore-watch="「文件或文件夹」"`
            6. `--interpreter=bash/python/ruby/coffee/php/perl/node`

                需要配置`exec_mode: fork`、`exec_interpreter: 对应语言`。
            7. `--max-memory-restart 「数字」K/M/G`

                达到最大内存就自动重启应用。
            8. `--restart-delay 「数字」ms`
            9. `--time`

                每行log前缀添加时间戳
            10. `--env 「环境名」`

                使用配置脚本中的`env_「环境名」`的环境变量配置。不传则默认使用配置脚本中`env`的环境变量配置。

                ><details>
                ><summary>e.g.</summary>
                >
                >```javascript
                >// 默认使用
                >"env": {
                >  "DEBUG": "this"
                >},
                >// 传`--env xx`时使用
                >"env_xx": {
                >  "DEBUG": "that"
                >}
                >```
                ></details>
            11. `--cron 「cron格式」`

                cron形式的自动重启配置
            12. `--no-daemon`

                不使用pm2自己的守护进程运行。

        2. `stop all或进程名或进程id或执行文件或配置脚本`
        3. `restart all或进程名或进程id或执行文件或配置脚本`
        4. `startOrRestart all或进程名或进程id或执行文件或配置脚本`
        5. `delete all或进程名或进程id或执行文件或配置脚本`
        6. `reload all或进程名或进程id或配置脚本`

            如果是在cluster mode，reload会依序升级重启每一个程序，达到zero downtime升级
        7. `start/stop/restart/startOrRestart/delete/reload 配置脚本 --only 「进程名」`

            仅对某一个进程进行操作。

        >若使用配置脚本，则命令行参数大部分会被忽略（除了部分参数，如：`--env`、`--only`、等）。

        - 命令行参数都可以用配置脚本设置，参考：[pm2: Attributes available](https://pm2.keymetrics.io/docs/usage/application-declaration/#attributes-available)。
    2. `ecosystem/init`

        初始化`ecosystem.config.js`文件。
    3. `list/ls/l/status`
    4. `monit`
    5. `logs`

        1. `「进程名」`
        2. `--json`
        3. `--format`
    6. `reloadLogs`

        重载所有logs。
    7. `flush`

        清空所有logs。
    8. `describe 「进程id或进程名」`
    9. `show 「进程id或进程名」`
    10. `ping`

        判断pm2守护进程正在运行。
    11. `kill`

        杀掉pm2自己，包括所有：pm2程序、pm2运行的进程、等，然后重启pm2。

        >pm2卡死的时候使用。
    12. 系统重启或pm2自己的重启

        >重启信息记录在：`$HOME/.pm2/dump.pm2`。

        1. `startup`
        2. `save`
        3. `unstartup`
        4. `resurrect`
    13. `serve 「文件路径，默认：./」 「端口号，默认：8080」`

        静态服务。
    14. `install 「模块名」`

        1. `pm2 install typescript` -> `pm2 start app.ts --watch`
    15. `update`

        更新在内存中运行的pm2。

        >先在全局更新`npm install pm2@latest -g`，然后再更新在内存中运行的pm2。
    16. `deploy`

        部署、发布。
