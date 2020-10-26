# Node.js脚手架（typescript+pm2或nodemon+inspect）

实现：Node.js服务端开发，使用typescript、改动代码自动重启服务（`pm2`或`nodemon`）、chrome的inspect自动更新

>`pm2`或`nodemon` + `typescript` + `--inspect` + Chrome的inspect自动更新（或Visual Studio Code）

- 文件结构

    ```text
    .
    ├── src/
    |   └── index.ts
    |
    ├── pm2.json 或 nodemon.json
    └── package.json
    ```

1. package.json

    ```json
    {
      "scripts": {
        "dev:pm2": "pm2 start pm2.json",
        "stop:pm2": "pm2 stop pm2.json && pm2 delete pm2.json",

        "dev:nodemon": "nodemon --inspect src/index.ts"
      },
      "devDependencies": {
        "@types/node": "14",
        "nodemon": "2",
        "pm2": "4",
        "ts-node": "9",
        "typescript": "4"
      }
    }
    ```
2. 配置文件

    >推荐用`pm2`（e.g. `pm2 start '「指令」' --watch`），`nodemon`可能无法成功监听改动后重启Node.js服务。

    1. pm2.json

        ```json
        {
          "apps": {
            "name": "xxx",
            "script": "./src/index.ts",
            "interpreter": "./node_modules/.bin/ts-node",
            "watch": true,
            "ignore_watch": [
              "node_modules",
              "logs"
            ],
            "error_file": "./logs/pm2-err.log",
            "out_file": "./logs/pm2-out.log",
            "log_date_format": "YYYY-MM-DD HH:mm Z",
            "env": {
              "NODE_OPTIONS": "--inspect"
            }
          }
        }
        ```
    2. nodemon.json

        ```json
        {
          "restartable": "rs",
          "ignore": [
            ".git",
            "node_modules/**/node_modules"
          ],
          "verbose": true,
          "execMap": {
            "ts": "node --require ts-node/register"
          },
          "watch": [
            "src/"
          ],
          "ext": "js,json,ts"
        }
        ```
3. 安装Chrome插件[NIM](https://github.com/june07/NIM)（Visual Studio Code默认支持）

    >参考：[Stack Overflow: Can I get node --inspect to open Chrome automatically](https://stackoverflow.com/questions/41398970/can-i-get-node-inspect-to-open-chrome-automatically#answer-46262271)。
