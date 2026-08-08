# 命令行备忘

## 目录
1. [命令花费时间](#命令花费时间)
1. [查找命令](#查找命令)
1. [网络连接测试](#网络连接测试)
1. [IPv6相关命令](#ipv6相关命令)
1. [`ssh`](#ssh)
1. [远程复制文件（夹）](#远程复制文件夹)
1. [同步文件（夹）](#同步文件夹)
1. [图形界面文件上传/下载（lrzsz）](#图形界面文件上传下载lrzsz)
1. [改密码](#改密码)
1. [hosts文件位置](#hosts文件位置)
1. [校验文件哈希](#校验文件哈希)
1. [查看本机 IP](#查看本机-ip)
1. [执行或加载脚本](#执行或加载脚本)
1. [Shell 类型与登录 Shell](#shell-类型与登录-shell)
1. [Shell 启动配置文件](#shell-启动配置文件)
1. [查看端口、网络连接和进程](#查看端口网络连接和进程)
1. [查看磁盘空间占用](#查看磁盘空间占用)
1. [创建文件](#创建文件)
1. [查看文件](#查看文件)
1. [清空文件内容](#清空文件内容)
1. [查看 group、user](#查看-groupuser)
1. [指令的别名](#指令的别名)
1. [`adb`](#adb)
1. [`sleep`](#sleep)
1. [`xargs`](#xargs)
1. [批量删除文件](#批量删除文件)
1. [`mysql`](#mysql)
1. [postgresql](#postgresql)
1. [mongodb](#mongodb)
1. [redis](#redis)
1. [`read`](#read)
1. [`sed`](#sed)
1. [`ln`](#ln)
1. [`vi`](#vi)
1. [Shell环境的运行参数](#shell环境的运行参数)
1. [压缩、解压缩](#压缩解压缩)
1. [macOS命令](#macos命令)

    1. [（macOS）brew更新](#macosbrew更新)
    1. [（macOS）打开文件（夹）](#macos打开文件夹)
    1. [（macOS）钥匙串](#macos钥匙串)
    1. [（macOS）管理配置描述文件](#macos管理配置描述文件)

---
>- 学会在终端中进行命令查询
>
>    1. `「命令」 --help`
>    2. `man 「命令」`
>    3. [`tldr`](https://github.com/tldr-pages/tldr) `「命令」`（安装：`brew install tldr`）
>    4. `info 「命令」`
>    5. `whatis 「命令」`
>
>    >`「命令」`可以是 「命令」+「指令」，如：`docker info`。
>
>    阅读英文文档时，英文水平是痛点，跳着看容易看不懂……

>可阅读：[You-Dont-Need-GUI](https://github.com/you-dont-need/You-Dont-Need-GUI)、[bash-guide](https://github.com/Idnan/bash-guide)。

#### 命令花费时间
```shell
time 「命令」
# e.g. time ls
```
- 使用[hyperfine](https://github.com/sharkdp/hyperfine)（高精度命令行基准测试与性能对比工具）

#### 查找命令
```shell
command -v 「命令」  # 输出将被执行的命令路径或定义
type -a 「命令」     # 列出同名的别名、函数、内建命令和可执行文件
```

#### 网络连接测试

><details>
><summary>e.g. <code>22</code>端口号测试都通过，但一执行git操作就报<code>22</code>端口号问题</summary>
>
>`Connection closed` 或 `Connection reset` 表示 TCP 连接可能已建立，但在 SSH 协议交互期间被关闭：
>
>1. `nc`/`telnet` 只能确认 TCP 端口能否连接，不能证明 SSH 协议交互一定成功。
>2. 防火墙、代理、网关、服务端配置或临时故障都可能中断连接，不能仅凭该错误确定责任方。
>3. 可用 `ssh -T git@github.com` 测试是否能完成 SSH 协议交互。
></details>

1. `ping`

    向域名或 IP 发送 ICMP 回显请求，用于检查可达性、延迟和丢包，不代表实际传输速度。

    >发送的ICMP请求是一个固定的协议，不能设定端口号，因此也不能用`ping`来检测某端口是否可访问。若目标IP不返回ICMP数据包，则也无法ping通。

    ```shell
    ping 「域名或IP」
    ```
2. `curl`

    发起HTTP请求，查看返回信息（HTTP响应）。

    ```shell
    curl "「URL」"                                      # 输出响应体
    curl -i "「URL」"                                   # 输出响应头和响应体
    curl -H '「请求头: 值」' "「URL」"                  # 设置请求头
    curl -X 「请求方法，如 POST」 "「URL」"             # 设置请求方法
    curl -g "「URL」"                                   # 不解析 URL 中的 `{}`、`[]`
    curl -x http://127.0.0.1:8899 "「URL」"              # 通过代理访问
    ```
3. `nc` / `telnet`

    测试 TCP 端口是否可连接。`telnet` 传输明文，不应用于实际远程登录；端口检测优先使用 `nc`。

    ```shell
    nc -vz 「IP/域名」 「端口」
    # macOS 安装 telnet：brew install telnet
    telnet 「IP/域名」 「端口」
    ```
4. `nslookup`

    查询DNS的记录，查看域名解析是否正常，在网络故障的时候用来诊断网络问题。
5. `dig`

    从DNS域名服务器查询主机地址信息。
#### IPv6相关命令
```shell
nslookup -type=AAAA 「域名」

dig 「域名」 AAAA

ping6 「域名」    # macOS
ping -6 「域名」  # Linux
curl -6 "「URL」"
```

#### `ssh`
```shell
ssh -p 「端口号，默认 22」 「用户名@地址」
```

- 确认远程主机密钥确已更换后，删除 `known_hosts` 中该主机的旧记录；不要直接删除整个文件。

    ```shell
    ssh-keygen -R 「地址」
    ssh-keygen -R '[「地址」]:「端口号」'  # 使用非默认端口时
    ```

#### 远程复制文件（夹）
```shell
scp -P 「端口号，默认：22」 「来源文件」 「目标路径」
# 复制目录时加 -r
scp -r -P 「端口号」 「来源目录」 「目标路径」
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
rsync -av --progress 「来源路径」 「目标路径」
```

后续同步仅传输差异内容。源目录末尾有 `/` 表示“同步目录中的内容”，没有 `/` 表示“同步目录本身”。

#### 图形界面文件上传/下载（[lrzsz](https://www.ohse.de/uwe/software/lrzsz.html)）
```shell
rz

sz 「文件路径」
```

>iTerm2 使用 ZMODEM 时需配置 Trigger，参考 [iTerm2 Triggers](https://iterm2.com/documentation-triggers.html) 和其链接的 [iTerm2-zmodem 示例](https://github.com/RobberPhex/iTerm2-zmodem)。脚本中的 `rz`/`sz` 路径应以 `command -v rz` 和 `command -v sz` 的输出为准；脚本只需 `chmod +x 「脚本」`，不要使用 `chmod 777`。

#### 改密码

```shell
passwd
```

#### hosts文件位置
1. macOS、Linux

    `/etc/hosts`
2. Windows

    `C:\Windows\System32\drivers\etc\hosts`

#### 校验文件哈希
>哈希可用于下载完整性校验；MD5、SHA-1 不适合安全签名或抗碰撞场景，安全用途优先使用 SHA-256/SHA-512 等。

1. MD5

    ```shell
    # macOS
    md5 「文件」
    md5 -s 「字符串」    # 或`echo -n 「字符串」 | md5`

    # Linux
    md5sum 「文件」
    echo -n 「字符串」 | md5sum

    # Windows PowerShell / cmd.exe
    certutil -hashfile 「文件」 MD5
    ```

    - Node.js

        ```js
        const crypto = require('node:crypto');
        const md5 = crypto.createHash('md5');
        md5.update('字符串').digest('hex');
        ```
2. SHA

    ```shell
    # macOS、Linux
    shasum 「文件」
    echo -n 「字符串」 | shasum
    # 使用特定算法：`-a, --algorithm   1 (default), 224, 256, 384, 512, 512224, 512256`
    # Linux额外还可以使用特定算法：`sha224sum sha256sum sha384sum sha512sum`

    # Windows PowerShell / cmd.exe
    certutil -hashfile 「文件」 SHA256
    ```
- base64（编码，不是哈希）

    ```shell
    # 字符串
    printf '%s' '字符串' | base64
    printf '%s' '5a2X56ym5LiyCg==' | base64 -d  # Linux
    printf '%s' '5a2X56ym5LiyCg==' | base64 -D  # macOS

    # 文件
    base64 「文件」                 # Linux 编码
    base64 -d 「文件」              # Linux 解码
    base64 -i 「文件」              # macOS 编码
    base64 -D -i 「文件」           # macOS 解码
    ```

    - Node.js

        ```js
        Buffer.from('任意字符串', 'utf-8').toString('base64')               // 编码
        Buffer.from('5Lu75oSP5a2X56ym5Liy', 'base64').toString('utf-8');  // 解码

        // 浏览器也支持
        btoa('单字节字符串')    // 编码（对输入有限制：从 二进制 到 ASCII）
        atob('编码值')         // 解码（对输入有限制：从 ASCII 到 二进制）
        ```

#### 查看本机 IP
```shell
# macOS（en0 通常是 Wi-Fi，实际接口可能不同）
ipconfig getifaddr en0
ifconfig

# Linux
ip -brief address

# Windows
ipconfig
```

>上述命令查看的是本地网络接口地址，不一定是互联网出口的公网 IP。

#### 执行或加载脚本
>路径可能包含空格或特殊字符时，优先用引号包裹整个路径。

```shell
chmod +x "「路径/脚本.sh」"
"「路径/脚本.sh」"       # 在子 Shell 中执行，需要正确的 Shebang 和执行权限
bash "「路径/脚本.sh」"  # 显式使用 Bash，脚本无需执行权限

. "「路径/脚本.sh」"     # 加载到当前 Shell，会影响当前环境
# 等价的 Bash/Zsh 写法：source "「路径/脚本.sh」"
```

#### Shell 类型与登录 Shell
1. 查看系统允许使用的登录 Shell

    ```shell
    cat /etc/shells
    ```
2. 查看当前正在执行的 Shell

    ```shell
    ps -p $$ -o comm=
    ```
3. 查看当前用户的登录 Shell

    ```shell
    printf '%s\n' "$SHELL"
    ```

    >`$SHELL` 记录登录 Shell，不一定是当前正在执行的 Shell。
4. 修改当前用户的登录 Shell

    ```shell
    chsh -s 「Shell 路径，如 /bin/zsh 或 /bin/bash」
    ```

#### Shell 启动配置文件
```shell
# Zsh
vi ~/.zshrc       # 交互式 Shell
vi ~/.zprofile    # 登录 Shell

# Bash
vi ~/.bashrc        # 交互式非登录 Shell
vi ~/.bash_profile  # 登录 Shell

# 修改后立即加载对应文件，也可重新打开 Shell
source "「刚修改的配置文件」"
```

>这些文件在 Shell 启动时加载，不是操作系统开机任务；开机服务应使用 macOS `launchd` 或 Linux `systemd`。

#### 查看端口、网络连接和进程
1. 查看端口和网络连接

    ```shell
    # macOS、Linux：查看监听指定端口的进程
    lsof -nP -iTCP:「端口号」 -sTCP:LISTEN

    # Linux：查看所有监听中的 TCP 端口和进程
    ss -lntp

    # Windows cmd.exe：查看指定端口及 PID
    netstat -aon | findstr 「端口号」
    tasklist | findstr 「PID」
    ```
2. 查看进程

    ```shell
    ps -ef
    pgrep -fl '「命令关键字」'  # macOS、Linux；-f 匹配完整命令行
    ```
3. 结束进程

    ```shell
    # macOS、Linux：先请求进程正常退出
    kill 「PID」
    # 只在进程无法正常退出时强制结束
    kill -9 「PID」
    # 可能匹配多个进程，执行前先用 pgrep -fl 确认
    pkill -f '「命令关键字」'
    killall 「进程名」

    # Windows cmd.exe：先尝试正常结束，必要时再加 /F
    taskkill /T /PID 「PID」
    taskkill /F /T /PID 「PID」
    ```

    >macOS 手势突然失效时，可尝试 `killall Dock`。
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
    find 「路径」 -type f -size +10M
    ```

#### 创建文件
1. `touch 「文件名」`

    >若文件已存在，则更新文件时间为当前系统时间。
2. `vi 「文件名」`

    >编辑文件。若文件不存在，则先创建后编辑。
3. `printf '%s\n' '「内容」' > "「文件名」"`

    >若文件已存在，则替换文件内容。

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

- 查看文件属性

    `ls -lh 「文件名」`

#### 清空文件内容
>以下命令会覆盖原内容且通常无法恢复。先确认文件路径，必要时先执行 `cp "「文件名」" "「文件名」.bak"` 备份。

```shell
: > "「文件名」"             # 清空为 0 字节
printf '\n' > "「文件名」"  # 只保留一个换行符
```

#### 查看 group、user
1. 查看 Linux 组信息

    ```shell
    cat /etc/group  # 组名:密码占位符:GID:附加成员列表
    ```
2. 查看 Linux 用户信息

    ```shell
    cat /etc/passwd # 用户名:密码占位符:UID:GID:备注:主目录:登录 Shell
    ```
3. `groups`

    ```shell
    groups          # 返回当前用户所在的组名

    groups 「用户名」 # 返回「用户名」所在的组名
    ```

#### 指令的别名
```shell
# alias 替换简单命令的第一个词；长路径可封装在 cd 别名中

alias   # 查看已设置的内容

alias 「自定义命令名」='「执行命令1」; 「执行命令2」'   # 新增 别名=执行命令
alias cproj='cd "「很长的路径」"'

alias 「自定义命令名」      # 打印设置的执行命令

# 别名后跟随的参数会追加到替换后的命令；别名内部不能使用 $1 等位置参数

unalias 「自定义命令名」    # 删除 别名
```

>需要在命令中使用位置参数时，定义 Shell 函数：
>
>```shell
>sync-public() {
>  curl --request PUT "https://registry-direct.npmmirror.com/-/package/$1/syncs"
>}
>sync-public fabric-demo
>```

#### `adb`
1. 查看已连接的设备（尝试连接手机）

    ```shell
    adb devices -l
    # List of devices attached
    # 「序列号」       device usb:「？？？」 product:「手机型号」 model:「手机型号」 device:「手机型号」 transport_id:「数字」
    ```
2. 系统消息输出

    ```shell
    adb logcat

    # 或

    adb shell   # 启动交互式Unix shell对设备发起命令
    logcat | grep 「筛选内容」
    ```
3. 端口转发

    1. 手机访问「手机端口号」的流量都会转发到PC的「PC端口号」：

        ```shell
        adb reverse --list  # 打印所有 手机->PC 的端口映射列表

        adb reverse tcp:「手机端口号」 tcp:「PC端口号」 # 新增一个端口映射

        adb reverse --remove tcp:「手机端口号」      # 删除一个端口映射

        adb reverse --remove-all                 # 删除所有端口映射
        ```
    2. PC访问「PC端口号」的流量都会转发到手机的「手机端口号」：

        ```shell
        adb forward --list  # 打印所有 PC->手机 的端口映射列表

        adb forward tcp:「PC端口号」 tcp:「手机端口号」 # 新增一个端口映射

        adb forward --remove tcp:「PC端口号」       # 删除一个端口映射

        adb forward --remove-all                 # 删除所有端口映射
        ```

    >可以混合配置使用，如：手机端口 A -> PC 端口 B -> 手机端口 C。
4. 查看手机中所有安装的包

    ```shell
    adb shell pm list packages
    # package:「包名」
    # e.g. com.tencent.mtt.hippy.example:com.tencent.mtt.hippy.example
    ```
5. 查看界面性能数据

    >来自：[测试界面性能](https://developer.android.com/training/testing/performance)。

    ```shell
    # 需要打开了「GPU呈现模式分析」为「在adb shell dumpsys gfxinfo中」
    adb shell dumpsys gfxinfo 「PACKAGE_NAME」
    adb shell dumpsys gfxinfo 「PACKAGE_NAME」 framestats
    ```
6. 安装本地包

    ```shell
    adb install 「包地址」
    ```

#### `sleep`
```shell
sleep 「秒数」  # 延迟一段时间，再向下继续执行命令
```

#### `xargs`
将标准输入转为命令行参数。

```shell
printf '%s\0' '1.txt' '2.txt' '3.txt' | xargs -0 touch  # -0 可正确处理空格和特殊字符
```

#### 批量删除文件
```shell
# 先预览匹配结果
find . -type f -name "「文件名或通配模式」" -print
# 确认后再删除文件（不匹配目录）
find . -type f -name "「文件名或通配模式」" -delete
```

#### [`mysql`](https://dev.mysql.com/doc/refman/en/)
```shell
# 1. 安装
brew install mysql  # 安装 Homebrew 当前稳定版

# 2. 启动服务
brew services start mysql
brew services stop mysql
brew services restart mysql
brew services info mysql  # 查看服务状态和 PID
brew services list        # 查看 Homebrew 管理的后台服务，如 mysql、postgresql@17、redis
mysql_secure_installation # 首次安装后按需设置 root 密码和安全选项

# 3. 连接服务
# Homebrew 首次安装且尚未设置 root 密码时：
mysql -u root   # 需要密码时：mysql -u root -p
# 通用连接：`-h 主机`；`-P 端口`；`-u 用户名`；`-p` 交互输入密码；`-D` 选择数据库（可省略）
mysql -h 127.0.0.1 -P 3306 -u 「用户名」 -p -D 「数据库名」 --default-character-set=utf8mb4
```

>进入 `mysql>` 后，`「SQL 语句」;` 或 `「SQL 语句」\g` 表示执行；`\?` 查看客户端命令，`HELP 「SQL 语句」;` 查看 SQL 帮助，`\q` 退出。

>`DROP`、`DELETE`、`UPDATE` 等语句会修改或删除数据。执行前先备份并确认当前环境、对象名称和 `WHERE` 条件；授权时遵循最小权限原则，`ALL PRIVILEGES` 仅用于明确需要完全管理权限的场景。

```sql
-- 查看、创建、删除和切换数据库
SHOW DATABASES;
CREATE DATABASE 「数据库名」 DEFAULT CHARACTER SET utf8mb4;
DROP DATABASE 「数据库名」;
SELECT DATABASE();
USE 「数据库名」;

-- 查看和修改表
SHOW TABLES;
DESCRIBE 「表名」;                    -- 等价于 SHOW COLUMNS FROM 「表名」;
SHOW FULL COLUMNS FROM 「表名」;      -- 额外显示权限、注释等信息
CREATE TABLE 「表名」 (「字段」 「类型」);
DROP TABLE 「表名」;
RENAME TABLE 「原表名」 TO 「新表名」;
ALTER TABLE 「表名」 「修改内容」;

-- 增删改查数据
SELECT * FROM 「表名」 WHERE 「条件」;
INSERT INTO 「表名」 (「字段」) VALUES (「值」);
UPDATE 「表名」 SET 「字段」 = 「值」 WHERE 「条件」;
DELETE FROM 「表名」 WHERE 「条件」;

-- 查看、创建、授权和删除用户
SELECT User, Host FROM mysql.user;
SHOW GRANTS;  -- 查看当前用户的权限
CREATE USER '「用户名」'@'「主机」' IDENTIFIED BY '「密码」';
GRANT 「所需最小权限，如 SELECT, UPDATE」 ON 「数据库名 或 *」.「表名 或 *」 TO '「用户名」'@'「主机」';
REVOKE 「要撤销的权限，如 UPDATE」 ON 「数据库名 或 *」.「表名 或 *」 FROM '「用户名」'@'「主机」';
DROP USER '「用户名」'@'「主机」';
```

>MySQL 中 `DATABASE` 与 `SCHEMA` 基本同义；连接后可用 `USE 「数据库名」;` 切换当前数据库。

#### postgresql
```shell
# 1. 安装
brew install postgresql@17  # 安装，版本按需

# 2. 启动服务
brew services start postgresql@17
brew services stop postgresql@17
brew services restart postgresql@17
brew services info postgresql@17  # 查看服务状态和 PID
brew services list                # 查看 Homebrew 管理的后台服务
# 前台运行；数据目录以 Homebrew 实际路径为准
"$(brew --prefix postgresql@17)/bin/postgres" -D "$(brew --prefix)/var/postgresql@17"

# 3. 连接服务
# 连接 postgres 数据库：`-h 主机`；`-p 端口`；`-U 用户名`；`-d 数据库名`
psql -h localhost -p 5432 -U "$(whoami)" -d postgres
```

>进入 psql 交互环境（`数据库名=>` 或 `数据库名=#`）后，`\?` 查看 psql 命令，`\h 「SQL 语句」` 查看 SQL 帮助。SQL 语句以 `;` 结束，psql 元命令（如 `\l`、`\du`）不需要。

>`DROP` 会删除对象，执行前先备份并确认当前环境和对象名称。`SUPERUSER` 可绕过常规权限检查，仅在明确需要时使用；通常应创建普通用户并按需授权。

```text
-- 查看数据库列表
\l
-- 创建数据库；shell 中可用：createdb my_test_db
CREATE DATABASE my_test_db;
-- 删除数据库；shell 中可用：dropdb my_test_db
DROP DATABASE my_test_db;
-- 查看和切换当前数据库
SELECT current_database();
\c my_test_db
-- 模式属于当前数据库，不能通过「数据库名.模式名」跨库创建
CREATE SCHEMA IF NOT EXISTS "模式名";
-- 只能直接删除空模式；若包含对象，需先删除对象或按需使用 CASCADE
DROP SCHEMA "模式名";

-- 查看用户列表；\du+ 额外展示描述
\du
-- 创建普通用户；shell 中可用：createuser -U "$(whoami)" -P 用户名
CREATE USER 用户名 WITH PASSWORD '密码';
-- 创建超级用户；用 \h CREATE USER 查看所有选项
CREATE USER 用户名 WITH SUPERUSER PASSWORD '密码';
-- 删除用户；shell 中可用：dropuser -U "$(whoami)" 用户名
DROP USER 用户名;
```

>1. PostgreSQL 的完整层级是：集群 (Cluster) -> 数据库 (Database) -> 模式 (Schema) -> 表/函数等对象。数据库、角色/用户、表空间等属于集群级对象，被同一 PostgreSQL 实例共享；连接任意已有数据库后，只要权限足够，就可以创建新的数据库或角色。
>2. 每次 `psql` 连接只进入一个数据库；模式、表、视图、函数等属于当前数据库，不能用 `数据库名.模式名.表名` 跨库访问或创建。要给非当前数据库创建模式，需要先 `\c 「数据库名」` 切换连接，或在 shell 中执行 `psql -d 「数据库名」 -c 'CREATE SCHEMA 「模式名」;'`。
>3. Schema 是数据库内的命名空间，用来组织表、视图、函数等对象；不同 Schema 下可以存在同名表。创建或访问对象时若不写 Schema，PostgreSQL 会按 `search_path` 顺序查找或选择目标 Schema；默认通常是 `"$user", public`，即先尝试当前用户名同名 Schema，找不到或不可用时再使用 `public`。可用 `SHOW search_path;` 查看，用 `SET search_path TO 「Schema名」, public;` 临时调整。

#### [mongodb](https://www.mongodb.com/docs/)
```shell
# 1. 安装（macOS）
brew tap mongodb/brew
brew install mongodb-community@8.0

# 2. 管理服务
brew services start mongodb-community@8.0
brew services stop mongodb-community@8.0
brew services restart mongodb-community@8.0
brew services info mongodb-community@8.0

# 3. 连接；本地默认地址为 mongodb://127.0.0.1:27017
mongosh
mongosh 'mongodb://「用户名」:「密码」@「主机」:「端口」/「数据库名」'
```

>进入 `mongosh` 后，`help` 查看帮助，`exit` 退出。`use` 只切换当前数据库；首次写入数据后，不存在的数据库和集合才会被创建。

```javascript
show dbs
use 「数据库名」
db
show collections

db.「集合名」.insertOne({ 「字段名」: 「值」 })
db.「集合名」.find({ 「字段名」: 「值」 }).sort({ 「排序字段」: -1 }).limit(「数量」)
db.「集合名」.countDocuments({ 「字段名」: 「值」 })
db.「集合名」.updateOne({ 「查询条件」 }, { $set: { 「字段名」: 「新值」 } })
db.「集合名」.deleteOne({ 「查询条件」 })
```

>`updateOne()` 和 `deleteOne()` 会修改数据，执行前先用同一查询条件运行 `find()` 确认目标文档。

#### redis
```shell
# 1. 安装
brew install redis      # 安装 Redis

# 2. 启动服务
# 后台运行：start 会立即启动并注册为登录时自动启动；run 只启动本次，不注册为登录时自动启动
brew services start redis
brew services stop redis
brew services restart redis
brew services info redis  # 查看服务状态和 PID
brew services list        # 查看 Homebrew 管理的后台服务
brew services run redis   # 只启动本次，不注册为登录时自动启动

# 前台运行：若后台服务已占用 6379，先执行 brew services stop redis，或用 --port 更换端口
# 不指定配置文件时使用内置默认配置；dir 默认为当前目录，RDB 文件默认为 dump.rdb
redis-server
redis-server "$(brew --prefix)/etc/redis.conf"  # 显式使用与 brew services 一致的配置文件
redis-server "$(brew --prefix)/etc/redis.conf" --port 6380 --dir /tmp  # 命令行参数覆盖配置文件

# 3. 连接服务
# 默认连 127.0.0.1:6379、逻辑库 0；ping 通返回 PONG
redis-cli                      # 进入交互式 REPL。尝试输入>`SCAN 0`
redis-cli ping                 # 单次命令，不进 REPL
redis-cli -h 「地址」 -p 「端口」 -n 「逻辑库序号」 ping
redis-cli -a 「密码」 ping     # 带密码；也可用 -u 见下
# URL 形式：redis://[:密码@]主机:端口[/逻辑库序号]
redis-cli -u 'redis://:「密码」@「地址」:「端口」/「逻辑库序号」' ping
redis-cli INFO server          # 看版本、uptime 等；确认连的是哪台实例
```

>进入 `redis-cli` 后，可直接执行 Redis 命令；`HELP 「命令」` 查看帮助，`QUIT` 退出。

```text
SET 「key」 「value」
SET 「key」 「value」 EX 「秒数」 NX
GET 「key」
DEL 「key1」 「key2」
EXISTS 「key」
TTL 「key」
SCAN 0 MATCH '「匹配模式，如 user:*」' COUNT 「数量」
```

>`NX` 表示仅在 key 不存在时写入，`XX` 表示仅在 key 已存在时写入；`EX` 和 `PX` 分别以秒和毫秒设置过期时间。遍历键时将 `SCAN` 返回的游标传入下一次调用，直到游标再次为 `0`；生产环境避免使用可能长时间阻塞服务的 `KEYS *`。

>Redis 主要在内存中读写数据，也可通过 RDB 快照、AOF 日志或两者组合持久化到磁盘。重启后是否丢失数据，取决于持久化配置和故障时机。

| 常见缓存问题 | 含义 | 常用处理 |
| --- | --- | --- |
| 缓存雪崩 | 大量 key 在短时间内同时失效，请求集中转向数据库 | 错开过期时间并加随机值、缓存预热、限流或降级 |
| 缓存穿透 | 缓存和数据库都没有目标数据，重复请求持续查询数据库 | 参数校验、布隆过滤器、短时间缓存空结果 |
| 缓存击穿 | 某个热点 key 失效时，大量并发请求同时查询数据库 | 互斥更新（只允许一个请求回源）、逻辑过期、提前刷新热点数据 |
| 缓存污染 | 低频或仅访问一次的数据长期占用内存 | 设置合理的 TTL、`maxmemory` 和键淘汰策略 |

#### `read`
>以下是 Bash 语法；Zsh 等 Shell 的部分选项含义不同。通常建议加 `-r`，避免把反斜杠当作转义符。

```shell
# 输入默认按 IFS 拆分后赋给变量；没有变量名时使用 REPLY
read -r 「变量名，默认 REPLY」
read -r -t 「秒数」 「变量名」          # 超时
read -r -p '「提示信息」' 「变量名」  # 显示提示
read -r -a 「数组名」                   # 从索引 0 开始赋值
read -r -n 「字符数」 「变量名」       # 读取指定字符数
read -r -e 「变量名」                  # 启用 Readline
read -r -d '「结束符」' 「变量名」      # 读取到指定结束符
read -r -s 「变量名」                  # 不回显输入，常用于密码
read -r -u 「文件描述符」 「变量名」   # 从指定文件描述符读取
```

- 逐行读取文件

    ```shell
    #!/bin/bash

    filename='「文件绝对路径」'

    while IFS= read -r myline; do
      printf '%s\n' "$myline"
    done < "$filename"
    ```

#### `sed`
`sed` 默认逐行处理输入并把结果输出到标准输出，不会修改原文件；使用 `-i` 才会就地修改。

```shell
# 先预览结果，不修改原文件
sed 's/「匹配内容」/「修改内容」/g' "「原文件」"

# macOS：确认结果后就地修改，默认保留 .bak 备份
sed -i '.bak' 's/「匹配内容」/「修改内容」/g' "「原文件」"
sed -i '' 's/「匹配内容」/「修改内容」/g' "「原文件」"  # 不保留备份

# Linux：确认结果后就地修改，默认保留 .bak 备份
sed -i.bak 's/「匹配内容」/「修改内容」/g' "「原文件」"
sed -i 's/「匹配内容」/「修改内容」/g' "「原文件」"  # 不保留备份

# 匹配内容包含 / 时，可换用 # 作为分隔符
sed "s#abc/def#${变量名}#g" "文件1" > "文件2"
```

#### `ln`
```shell
ln "「源文件」" "「目标文件」"             # 硬链接：新目录项指向同一文件数据，不复制文件内容
ln -s "「源文件/目录」" "「目标链接」"  # 符号链接：保存源路径，源路径移动或删除后可能失效
```

>硬链接不能跨文件系统，且通常不允许指向目录；符号链接可跨文件系统并可指向目录。

#### `vi`
1. `:set nu`设置行号
2. `:行号,$s/内容1/内容2`从「行号」开始到最后一行中，每行的第一个「内容1」替换成「内容2」

    `:行号,$s/内容1/内容2/g`从「行号」开始到最后一行中，每行的所有「内容1」替换成「内容2」

#### Shell环境的运行参数
- `set` 修改当前 Shell 的运行选项；子 Shell 环境会继承当前状态，但新启动的独立 Shell 不一定继承所有选项。

    1. [`set`](https://www.gnu.org/software/bash/manual/html_node/The-Set-Builtin.html) + 配置项

        >e.g. `set -u`
    2. `bash`（或其他Shell） + 配置项 + 脚本

        显式指定解释器时，脚本的 Shebang 解释器和其参数不参与执行。

        >e.g. `bash -u ./脚本`
    3. 脚本Shebang行 + 配置项

        >e.g. `#!/bin/sh -u`

```shell
# 运行参数的配置项：

-u          # 展开未设置变量时报错；非交互式 Shell 通常会退出。或：`-o nounset`
+u          # 默认。取消`-u`的效果。或：`+o nounset`

-x          # 运行结果之前，先输出执行的那一行命令（用`+ 指令内容`的方式输出，环境变量`PS4`的值决定输出符号）。或：`-o xtrace`
+x          # 默认。取消`-x`的效果。或：`+o xtrace`

-e          # 未被条件语句等上下文处理的命令返回非 0 状态时退出；存在多种例外。或：`-o errexit`
+e          # 默认。取消`-e`的效果。`+o errexit`

# 默认使用管道中最后一个命令的退出状态
-o pipefail # 改为只要任一命令失败，管道就返回非 0；是否退出脚本另由 -e 等逻辑决定
+o pipefail # 默认。取消`-o pipefail`效果

-E          # 让 ERR trap 被 Shell 函数、命令替换和子 Shell 环境继承。或：`-o errtrace`
+E          # 默认。取消`-E`的效果

-n          # 不运行命令，只检查语法是否正确。或：`-o noexec`

-f          # 不对通配符进行文件名扩展。或：`-o noglob`
+f          # 默认。取消`-f`的效果。`+o noglob`

-v          # 打印 Shell 接收到的每一行输入。或：`-o verbose`
+v          # 默认。取消`-v`的效果。`+o verbose`
```

#### 压缩、解压缩
1. 压缩文件（夹）

    ```shell
    zip 「归档.zip」 「文件」
    zip -r 「归档.zip」 「源目录」
    zip -er 「归档.zip」 「源目录」  # 交互输入密码
    ```
2. 解压缩

    ```shell
    unzip 「x.zip」
    ```
- 其他压缩/解压缩

    - `lzip`（`brew install lzip`）

        用于压缩单个文件；需要处理目录时，先用 `tar` 归档。对 `.zip`、`.gz` 等已压缩文件再压缩通常收益很小。

        ```shell
        lzip 「文件」           # 压缩

        lzip -d 「文件.lz」     # 解压缩
        ```
    - `gzip`、`gunzip`，`bzip2`、`bunzip2`

- 归档`tar`

    | 特性 | Gzip | Tar |
    |------|------|-----|
    | 主要功能 | 压缩（减小文件大小） | 归档（合并多个文件/目录为一个文件） |
    | 处理对象 | 单个文件 | 多个文件和目录结构 |
    | 保留元数据 | 可保留原文件名和时间等有限信息 | 可保留权限、所有者和时间戳等 |
    | 文件扩展名 | .gz | .tar |
    | 典型用途 | 压缩单个大文件 | 打包多个文件为一个文件 |
    | 压缩能力 | 有（使用DEFLATE算法） | 无（仅打包） |
    | 处理目录 | 不能直接处理目录 | 可以处理整个目录结构 |

---
### macOS命令

#### （macOS）brew更新
```shell
brew update && brew upgrade
# update 更新 Homebrew 和仓库元数据；upgrade 升级已安装的 formula 和 cask
```

>`brew install --cask 「软件名」` 可安装 Homebrew Cask 提供的 macOS 应用；先用 `brew search 「软件名」` 搜索。

#### （macOS）打开文件（夹）
```shell
open 「路径/文件」
open -t 「文件」  # 使用默认文本编辑器打开
```

>安装 [duti](https://github.com/moretension/duti)（`brew install duti`）后，可设置文件类型的默认应用：
>
>```shell
>duti -s com.sublimetext.4 public.plain-text all  # Sublime Text
>duti -s com.apple.TextEdit public.plain-text all # TextEdit
>```

#### （macOS）钥匙串
`钥匙串访问`应用可查看和管理 macOS 及部分应用保存的密码、密钥和证书。

#### （macOS）管理配置描述文件
1. 打开「系统设置 -> 通用 -> 设备管理」。
2. 选择配置描述文件，点击移除。

>若移除按钮不可用，该 Mac 可能由公司或学校管理，应联系系统管理员。不要手动删除 `/var/db/ConfigurationProfiles` 等系统目录。参考 [Apple 官方说明](https://support.apple.com/guide/mac-help/change-device-management-settings-mh35474/mac)。
