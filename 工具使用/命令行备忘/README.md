# 命令行备忘

### 验证文件的数字签名
1. MD5

    ```bash
    md5 文件  #或md5sum
    ```
2. SHA1

    ```bash
    shasum 文件  #或sha1sum
    ```

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

### 其他命令
1. ping地址测试

    ```bash
    ping IP地址
    ```
2. ssh登录

    ```bash
    ssh 用户名@地址 -p 端口号
    ```
3. 远程拷贝文件

    ```bash
    scp -P 端口号 远程用户名@远程地址:远程地址路径 本地存放路径
    ```

    >注意本机（目录权限）和远程主机的权限（文件权限）。
4. 改密码

    ```bash
    passwd
    ```
5. 指令在PATH变量的路径

    ```bash
    which 指令
    ```