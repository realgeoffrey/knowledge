# 命令行备忘

### 验证文件的数字签名
1. MD5

    ```bash
    md5sum 文件
    ```
2. SHA1

    ```bash
    sha1sum 文件
    ```

### [NVM](https://github.com/creationix/nvm)更新Node.js版本
```bash
nvm install v新版本号
nvm use v新版本号
nvm alias default v新版本号

nvm list
nvm uninstall v旧版本号
```
>需重装Node.js模块包。

### 远程拷贝文件
```bash
scp -P 端口号 远程用户名@远程地址:远程地址路径 本地存放路径
```