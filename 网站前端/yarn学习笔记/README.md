### [yarn](https://github.com/yarnpkg/yarn)学习笔记
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
        17. `yarn why`
        18. `yarn workspace`
        19. `yarn workspaces`
        20. `yarn login`、`yarn publish`、`yarn logout`

            发布相关。
        21. `yarn help`
