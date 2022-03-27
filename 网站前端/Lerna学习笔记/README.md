### [lerna](https://github.com/lerna/lerna)学习笔记

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
