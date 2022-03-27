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
        2. `bin`、`list`（打印已安装的packages）、`dir`（打印packages安装的目录）

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
    9. 其他

        1. `yarn config` + `set`、`get`、`delete`、`list`

            `--global`或`-g`
        2. `yarn autoclean`
        3. `yarn bin`
        4. `yarn cache clean`
        5. `yarn check`
        6. `yarn generate-lock-entry`
        7. `yarn import`
        8. `yarn info`
        9. `yarn licenses`
        10. `yarn link`、`yarn unlink`
        11. `yarn list或ls [--depth=「数字」]`
        12. `yarn owner` + `list`、`add`、`remove`
        13. `yarn pack`

            创建依赖包的一个gzip压缩文件。
        14. `yarn tag`
        15. `yarn team`
        16. `yarn version`
        17. `yarn versions`
        18. `yarn why`
        19. `yarn workspace`
        20. `yarn workspaces`
        21. `yarn login`、`yarn publish`、`yarn logout`

            发布相关。
        22. `yarn help`
