# [yarn](https://github.com/yarnpkg/yarn)+[Lerna](https://github.com/lerna/lerna)学习笔记

## 目录
1. [yarn](#yarn)
1. [Lerna](#lerna)

---
### yarn
1. [`.yarnrc`](https://classic.yarnpkg.com/zh-Hans/docs/yarnrc)

    ```text
    registry "https://mirrors.tencent.com/npm/"
    ```
2. [`yarn`CI](https://classic.yarnpkg.com/zh-Hans/docs/cli/)

    1. `yarn init`

        初始化`package.json`。

    >新增或更新或删除等，都会同步更新`yarn.lock`，大部分会同步更新`package.json`（`upgrade`不会）。

    2. `yarn add 「包名」[@「version或tag」]`

        新增或更新某个依赖包。

        >默认加入dependencies。

        1. `--dev`或`-D`加入devDependencies
        2. `--peer`或`-P`加入peerDependencies

            peerDependencies的目的是提示宿主环境去安装满足插件peerDependencies所指定依赖的包，然后在插件`import`或`require`所依赖的包时，永远都是引用宿主环境统一安装的npm包，最终解决插件与所依赖包不一致的问题。
        3. `--optional`或`-O`加入optionalDependencies

        >默认安装主版本下的最新版（1.x.y）。

        4. `--tilde`或`-T`安装急精确次要版本（1.2.x）
        5. `--exact`或`-E`安装精确版本（1.2.3）

        - 安装指定不同路径的包

            1. `yarn add 「file:/path/to/local/folder或.tgz」`从本地文件系统安装
            2. `yarn add 「git路径」`
            2. `yarn add 「http路径」`
    3. `yarn remove 「包名」`

        移除某个依赖包。
    4. `yarn upgrade [「包名」[@「version或tag」]]`

        >不更新`package.json`。

        更新某个或所有依赖包。

        - 更新依赖包并更新`package.json`、`yarn.lock`

            >使用[syncyarnlock](https://github.com/vasilevich/sync-yarnlock-into-packagejson)。

            ```shell
            yarn global add syncyarnlock          // install syncyarnlock globally
            yarn upgrade [「包名」[@「version或tag」]] // update dependencies, updates yarn.lock
            syncyarnlock -s -k                    // updates package.json with versions installed from yarn.lock
            yarn install                          // updates yarn.lock with current version constraint from package.json
            ```

        - `yarn upgrade-interactive`

            交互式更新。
    5. `yarn global` +

        1. `add`、`remove`、`upgrade`、`upgrade-interactive`
        2. `bin`（打印bin安装的目录）、`dir`（打印packages安装的目录）
        3. `list`（打印已安装的packages）

        全局操作。
    6. `yarn outdated`

        检查过时的包依赖。
    7. `yarn`或`yarn install`

        >[yarn: install](https://classic.yarnpkg.com/zh-Hans/docs/cli/install)。

        （按照`yarn.lock`）安装`package.json`的所有依赖包。

        1. `--force`强制重新下载。
        2. `--flat`安装所有依赖，但每个依赖只允许有一个版本存在。
        3. `--production`只安装生产环境依赖。

        - 其他

            1. `yarn run env`列出脚本运行时可用的环境变量
            2. `yarn run`列出包里所有可运行的脚本
    8. `yarn [run]` + `「脚本名」 [「多个参数」]`

        执行`package.json`的`scripts`中的脚本。

        1. `--mutex 「file 或 network」`确保任意给定时间只有一个实例运行（并且避免冲突）。
        2. `--verbose`详细日志
    9. `yarn create 「包名」 [「参数」]`

        >类似`npx`功能。

        1. 先全局安装`create-「包名」`到最新版本；
        2. 再运行`create-「包名」 [「参数」]`（`「包名」`里package.json的`bin`命令）。

        >e.g. `yarn create react-app my-app`等价于`yarn global add create-react-app`+`create-react-app my-app`。
    10. `yarn config` + `set`、`get`、`delete`、`list` + `--global`或`-g`

        设置或查看配置。

        >e.g. `yarn config get registry -g`、`yarn config set registry "https://mirrors.tencent.com/npm/" -g`
    11. 其他

        1. `yarn autoclean`
        2. `yarn bin`
        3. `yarn cache clean`
        4. `yarn check`
        5. `yarn generate-lock-entry`
        6. `yarn import`
        7. `yarn info`
        8. `yarn licenses`
        9. `yarn link`、`yarn unlink`
        10. `yarn list或ls [--depth=「数字」]`
        11. `yarn owner` + `list`、`add`、`remove`
        12. `yarn pack`

            创建依赖包的一个gzip压缩文件。
        13. `yarn tag`
        14. `yarn team`
        15. `yarn version`
        16. `yarn versions`
        17. `yarn why 「包名」`

            显示为什么安装软件包，详细说明哪些其他软件包依赖于它，或者是否明确标记为package.json清单中的依赖项。
        18. `yarn workspace`
        19. `yarn workspaces`
        20. `yarn login`、`yarn publish`、`yarn logout`

            发布相关。
        21. `yarn help`

### Lerna
- 文件结构

    ```text
    .
    ├── packages/
    |   ├── 项目1
    |   └── 项目2
    ├── lerna.json
    └── package.json
    ```

1. `lerna.json`

    ```javascript
    {
      // 当前版本或`independent`
      "version": "1.1.3",

      // 指定运行命令：`npm`（默认）或`yarn`
      "npmClient": "npm",

      "command": {
        "publish": {

          // 通配符的数组，其中的值不会被 lerna changed/publish 包含。
          // 使用它可以防止因更改发布不必要的新版本，如：仅仅修复 README.md 的错误
          "ignoreChanges": ["ignored-file", "*.md"],

          // 执行发布版本更新时的自定义提交消息
          "message": "chore(release): publish",

          // 发布用的registry
          "registry": "https://npm.pkg.github.com"
        },
        "bootstrap": {

          // 运行 lerna bootstrap 时会忽视该字符串数组中的通配符匹配的文件
          "ignore": "component-*",

          // 该字符串数组中的参数将在 lerna bootstrap 命令期间直接传递给 npm install
          "npmClientArgs": ["--no-package-lock"],

          // 该通配符的数组会在 lerna bootstrap 运行时限制影响的范围
          "scope": []
        }
      },

      // 表示包位置的全局变量数组。
      "packages": ["packages/*"]
    }
    ```

>[Lerna中文文档](http://www.febeacon.com/lerna-docs-zh-cn/)

2. 初始化

    1. 固定模式（默认）

        `lerna init`，统一管理版本号。
    2. 独立模式

        `lerna init --independent`，各自独立管理版本号。
3. 发布

    `lerna publish`
4. 其他命令

    1. `lerna version`

        更改自上次发布以来的包版本号
    2. `lerna bootstrap`

        将本地包链接在一起并安装剩余的包依赖项
    3. `lerna list`

        列出本地包
    4. `lerna changed`

        列出自上次标记发布以来发生变化的本地包
    5. `lerna diff`

        自上次发布以来的所有包或单个包的区别
    6. `lerna exec`

        在每个包中执行任意命令
    7. `lerna run`

        在包含该脚本中的每个包中运行npm脚本
    8. `lerna add`

        向匹配的包添加依赖关系

        >建议改成：`yarn workspace 「包内的package.json的name」 add 「依赖库」`
    9. `lerna clean`

        从所有包中删除node_modules目录
    10. `lerna import`

        将一个包导入到带有提交历史记录的monorepo中
    11. `lerna link`

        将所有相互依赖的包符号链接在一起
    12. `lerna create`

        创建一个新的由lerna管理的包
    13. `lerna info`

        打印本地环境信息

- monorepo方案：

    1. ~~Lerna + yarn workspace~~
    2. pnpm
