# 命令行备忘

## 目录
1. [命令花费时间](#命令花费时间)
1. [ping地址测试](#ping地址测试)
1. [ssh登录](#ssh登录)
1. [远程复制文件（夹）](#远程复制文件夹)
1. [同步文件（夹）](#同步文件夹)
1. [改密码](#改密码)
1. [指令在PATH变量的路径](#指令在path变量的路径)
1. [hosts文件位置](#hosts文件位置)
1. [验证文件的数字签名](#验证文件的数字签名)
1. [查看/设置环境变量](#查看设置环境变量)
1. [查看本机IP](#查看本机ip)
1. [执行文件](#执行文件)
1. [（Unix-like）开机自动运行的脚本](#unix-like开机自动运行的脚本)
1. [查看端口占用、网络链接，查看进程](#查看端口占用网络链接查看进程)
1. [查看端口占用，杀掉进程](#查看端口占用杀掉进程)
1. [查看磁盘空间占用](#查看磁盘空间占用)
1. [创建文件](#创建文件)
1. [查看文件](#查看文件)
1. [查看group、user](#查看groupuser)
1. [macOS命令](#macos命令)

    1. [（macOS）brew更新](#macosbrew更新)
    1. [（macOS）打开文件（夹）](#macos打开文件夹)

---

>- 学会在终端中进行命令查询
>
>    1. `「命令」 --help`
>    2. `man 「命令」`
>    3. `info 「命令」`
>    4. `whatis 「命令」`
>
>    >`「命令」`可以是 「命令」+「指令」，如：`docker info`。
>
>    阅读英文文档时，英文水平是痛点，跳着看容易看不懂……

#### 命令花费时间
```shell
time 「命令」
# e.g. time ls
```

#### ping地址测试
```shell
ping 「地址」
```

- IPv6相关

    ```shell
    nslookup -type=AAAA 「域名」

    dig 「域名」 AAAA

    # ping6 「域名」

    # ping -6 「域名」

    # curl -6 「URI」
    ```

#### ssh登录
```shell
ssh 「用户名@地址」 -p 「端口号，默认：22」
```

- 若某远程主机识别已更改，则需删除保存在本机的此IP所有秘钥（删除`known_hosts`保存某ip的秘钥）

    ```shell
    ssh-keygen -R 「地址」
    ```

#### 远程复制文件（夹）
```shell
scp -P 「端口号，默认：22」 「来源文件」 「目标路径」
```

1. 远程 -> 本地

    ```shell
    scp 「远程用户名@远程地址」:「远程文件」 「本地存放路径」
    ```
2. 本地 -> 远程

    ```shell
    scp 「本地文件」 「远程用户名@远程地址」:「远程存放路径」
    ```

>注意：本机和远程主机的目录权限、文件权限。

#### 同步文件（夹）
```shell
rsync 「来源文件」 「目标文件」
```

仅传输有差异内容，性能更好，参数更复杂。

#### 改密码

```shell
passwd
```

#### 指令在PATH变量的路径
```shell
which 「指令」
```

#### hosts文件位置
1. macOS、Linux

    `/etc/hosts`
2. Windows

    `C:\Windows\System32\drivers\etc\hosts`

#### 验证文件的数字签名
1. MD5

    ```shell
    # macOS
    md5 「文件」
    md5 -s 「字符串」    # 或`echo -n 「字符串」 | md5`

    # Linux
    md5sum 「文件」
    echo -n 「字符串」 | md5sum

    # Windows
    md5sum.exe 「文件」
    echo -n 「字符串」 | md5sum.exe
    ```
2. SHA

    ```shell
    # macOS、Linux
    shasum 「文件」
    echo -n 「字符串」 | shasum
    # 使用特定算法：`-a, --algorithm   1 (default), 224, 256, 384, 512, 512224, 512256`
    # Linux额外还可以使用特定算法：`sha224sum sha256sum sha384sum sha512sum`

    # Windows
    sha1sum.exe 「文件」
    echo -n 「字符串」 | sha1sum.exe
    # 使用特定算法：`sha224sum.exe sha256sum.exe sha384sum.exe sha512sum.exe`
    ```

#### 查看/设置环境变量
```shell
echo $「变量」          # 查看变量

export 「变量」=「值」   # 设置变量
```

#### 查看本机IP
```shell
# macOS、Linux
ifconfig    # 查看`en0`的`inet`（IPv4）或`inet6`（IPv6）

# Windows
ipconfig    # 查看`以太网适配器 本地连接 的 IPv4 地址`
```

#### 执行文件
>要对路径名/文件名中的`标点`和`空格`进行`\`转义。

```shell
./「文件名」.sh

. 「路径名/文件名」.sh
```

#### （Unix-like）开机自动运行的脚本
```shell
# macOS、Linux
vi ~/.bash_profile  # bash
vi ~/.zshrc         # zsh

# 如：可以把定义环境变量放在里面`export NODE_ENV=development`

# source 脚本   # 当前运行一遍
```

#### 查看端口占用、网络链接，查看进程
1. 所有端口占用、网络连接情况（Linux）

    ```shell
    # Linux
    netstat -antp
    ```
2. 某端口占用

    ```shell
    # macOS、Linux
    netstat -ant | grep 「端口号」
    lsof -i :「端口号」
    ```
3. 查看进程

    ```shell
    ps -ef
    ```

#### 查看端口占用，杀掉进程
1. macOS、Linux

    ```shell
    lsof -i :「端口号」

    kill 「PID」
    # macOS的「活动监视器」也可以查到「PID」并关闭进程
    ```
2.  Windows（需要在cmd.exe进行）

    ```shell
    netstat -aon | findstr 「端口号」  # 获得某端口号的任务PID

    tasklist | findstr 「PID」          # 获得某PID的任务名
    # 获得任务名之后可以再用`tasklist | findstr 「任务名」`确认是否有多个子任务

    taskkill /F /T /PID 「PID」           # 需要杀死主进程，否则仅杀死的子进程会被主进程再次创建
    # 或`taskkill /F /T /IM 「任务名」`
    # 或去任务管理器结束进程（打开进程->查看->选择列的PID）
    ```

#### 查看磁盘空间占用
1. 以磁盘分区为单位查看文件系统的磁盘空间情况

    ```shell
    df -h
    ```
2. 指定的目录或文件所占用的磁盘空间

    ```shell
    # macOS
    du -h -d1 「路径」

    # Linux
    du -h --max-depth=1 「路径」
    ```
3. 查找超过10M的文件

    ```shell
    find 「路径」 -size +10M
    ```

#### 创建文件
1. `touch 「文件名」`

    >若文件已存在，则更新文件时间为当前系统时间。
2. `vi 「文件名」`

    >编辑文件。若文件不存在，则先创建后编辑。
3. `echo "「内容」" > 「文件名」`

    >若文件已存在，则替换文件内容。
>4. `less/more/cat 「已存在文件」 > 「文件名」`，`cd >/>> 「文件名」`

#### 查看文件
1. `cat`、`nl`
2. `tac`颠倒输出
3. `more`、`less`一页一页输出
4. `tail`查看文件尾部

    ```shell
    tail -n 「行数」 「文件名」
    tail -f 「文件名」        # 流式输出（文件改动后重新输出）
    ```
5. `head`查看文件头部
6. `od`以二进制方式输出

#### 查看group、user
1. 查看所有组

    ```shell
    cat /etc/group  # 返回的每一条是一个组的信息：`组名:密码:组id:组内用户列表`
    ```
2. 查看所有用户

    ```shell
    cat /etc/passwd # 返回的每一条是一个用户的信息：`用户名:密码:用户id:所在组id:备注:用户的home目录:shell命令所在目录`
    ```
3. `groups`

    ```shell
    groups          # 返回当前用户所在的组名

    groups 「用户名」 # 返回「用户名」所在的组名
    ```

---
### macOS命令

#### （macOS）brew更新
```shell
brew update && brew upgrade && brew cask upgrade
```

>brew cask可以安装大部分软件，使用`brew search 「软件名」`进行搜索。

#### （macOS）打开文件（夹）
```shell
open 「路径/文件」
```
