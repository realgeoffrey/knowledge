### SVN环境配置（CentOS）

>历史环境记录：CentOS Linux 已停止维护，新环境请使用仍受支持的发行版；SVN 本身仍可用，但新项目也可优先评估 Git。

1. 安装 Subversion（历史命令需要可用的 CentOS 软件源）

    ```shell
    sudo yum install subversion
    ```
2. 创建仓库

    由管理员准备专用的非 root 系统账户，用作仓库所有者并运行 svnserve。确保该账户可写 /home/svn，并以此账户创建两个仓库（目录名尚未使用）：

    ```shell
    umask 077
    svnadmin create /home/svn/one
    svnadmin create /home/svn/two
    ```
    「*/home/svn/two*」 、「*/home/svn/one*」 为所创建仓库的2个路径。

3. 配置仓库

    针对每个仓库单独配置，分别修改每个仓库conf目录下面的三个配置文件（**authz**、**passwd**、**svnserve.conf**）
    1. 修改**authz**文件，这个配置文件里面可以设置用户组和用户目录权限

        ```ini
        [groups]
        # harry_and_sally = harry,sally
        # harry_sally_and_joe = harry,sally,&joe
        admin = user1,user2
        # [/foo/bar]
        # harry = rw
        # &joe = r
        # *=
        [/]
        @admin = rw
        *  =
        ```

        >前面是配置一个用户组admin 有成员user1,user2两个；
        >后面开始配置目录权限，设置admin组（前面加@符号）的权限为读写权限，其他成员没有权限（* = ）
    2. 修改**passwd**文件，设置访问当前仓库的用户和密码。将两个占位符分别替换为独立的强密码。该文件保存明文，权限设为 600，由运行 svnserve 的账户持有。

        ```ini
        [users]
        user1 = <user1 的密码>
        user2 = <user2 的密码>
        ```
    3. 修改**svnserve.conf**文件，开启权限控制等功能

        在已有的 `[general]` 节中启用以下配置项，注释说明保留行首的 `#`。

        ```text
        [general]
        ### These options control access to the repository for unauthenticated
        ### and authenticated users.  Valid values are "write", "read",
        ### and "none".
        #匿名访问的权限，可以是read,write,none,默认为read
        anon-access = none
        #使授权用户有写权限
        auth-access = write
        ### The password-db option controls the location of the password
        ### database file.  Unless you specify a path starting with a /,
        ### the file's location is relative to the directory containing
        ### this configuration file.
        ### If SASL is enabled (see below), this file will NOT be used.
        ### Uncomment the line below to use the default password file.
        #密码数据库的路径
        password-db = passwd
        ### The authz-db option controls the location of the authorization
        ### rules for path-based access control.  Unless you specify a path
        ### starting with a /, the file's location is relative to the the
        ### directory containing this file.  If you don't specify an
        ### authz-db, no path-based access control is done.
        ### Uncomment the line below to use the default authorization file.
        #访问控制文件
        authz-db = authz
        ### This option specifies the authentication realm of the repository.
        ### If two repositories have the same authentication realm, they should
        ### have the same password database, and vice versa.  The default realm
        ### is repository's uuid.
        #认证命名空间，subversion会在认证提示里显示，并且作为凭证缓存的关键字
        # 此处保留默认 realm（仓库 UUID），两个仓库各用自己的密码文件。
        ```

        >节名和配置项从行首开始写，避免缩进被当作上一项的续行。
4. 启动和关闭服务

    1. 启动服务

        ```shell
        svnserve -d --foreground -r /home/svn
        ```

        以仓库所有者身份执行，终端保持打开。参数 `-r` 指定两个仓库的父目录，与启动时所在目录无关。服务默认监听 TCP 3690，远程访问需要客户端能连接此端口。
    2. 停止服务

        在启动服务的终端按 Ctrl+C 即可停止本次启动的实例。
5. 访问仓库项目

    将下面的 IP地址 替换为服务器地址，两个仓库分别为 `svn://IP地址/one` 和 `svn://IP地址/two`。
6. SVN客户端操作

    在客户端选一个可写目录，检出工作副本，按提示输入对应密码：

    ```shell
    svn checkout --username user1 svn://IP地址/one abc
    cd abc
    ```

    以下命令按需使用，将文件名替换为实际路径。先用 `svn status` 核对待提交的改动：

    ```shell
    svn add 新建的文件
    svn delete 已受版本控制的文件
    svn status
    svn commit -m "信息" .
    svn update
    ```

    更新到指定版本时使用 `svn update -r 版本号`。

参考：[Subversion 手册：svnserve 配置](https://svnbook.red-bean.com/en/1.7/svn.serverconfig.svnserve.html)、[svnserve 启动选项](https://svnbook.red-bean.com/en/1.7/svn.ref.svnserve.html)。
