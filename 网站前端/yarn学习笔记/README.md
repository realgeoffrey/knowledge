# [yarn](https://github.com/yarnpkg/yarn)学习笔记

## 目录
1. [xx](#xx)

---
### xx
1. `.yarnrc`

    ```text
    registry "https://mirrors.tencent.com/npm/"
    ```
1. `yarn add 「包名」 --dev`加入devDependencies
1. 更新

    1. 更新某个包并更新`package.json`、`yarn.lock`

        `yarn add 「包名」`（更新或新增安装）
    2. 更新**所有**包并更新`package.json`、`yarn.lock`

        >使用[syncyarnlock](https://github.com/vasilevich/sync-yarnlock-into-packagejson)。

        ```shell
        yarn global add syncyarnlock // install syncyarnlock globally
        yarn upgrade                 // update dependencies, updates yarn.lock
        syncyarnlock -s -k           // updates package.json with versions installed from yarn.lock
        yarn install                 // updates yarn.lock with current version constraint from package.json
        ```
