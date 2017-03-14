# SVN环境配置（CentOS）

1. 安装subversion

    ```shell
    sudo yum install subversion
    ```

2. 创建仓库

	建立文件夹后执行
	```shell
    svnadmin create /home/svn/one
    svnadmin create /home/svn/two
    ```
	“*/home/svn/two*” 、“*/home/svn/one*” 为所创建仓库的2个路径。
	
3. 配置仓库

	针对每个仓库单独配置，分别修改每个仓库conf目录下面的三个配置文件（**authz**、**passwd**、**svnserve.conf**）
	1. 修改**authz**文件，这个配置文件里面可以设置用户组和用户目录权限

	    ```shell
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
	
	2. 修改**passwd**文件，设置访问当前仓库的用户和密码

		```shell
		[users]
		# harry = harryssecret
		# sally = sallyssecret
		user1  = 123456
		user2  = 123456
		```
	
	3. 修改**svnserve.conf**文件，开启权限控制等功能

		找到第一个常规选项[general]，把前面是一个#号的去掉#号，如下是我的demo仓库配置内容
		```text
		[general]
		### These options control access to the repository for unauthenticated
		### and authenticated users.  Valid values are "write", "read",
		### and "none".  The sample settings below are the defaults.
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
		realm = feijie’s svndata
		```

		>所有的行都必须顶格，否则报错。
	
4. 启动和关闭服务

	1. 启动服务

	    ```shell
        svnserve -d -r /home/svn
        ```
		要在SVN根目录下，这样SVN下的多个仓库都可以根据 *svn://ip地址/仓库名* 来进行SVN。
		>不要用sudo权限启动服务，否则无法commit。
		>若无法进行写权限：解决方法：停止SVN服务：`killall svnserve`，在创建版本库的用户下启动`svn ： svnserve -d -r /home/svn`
		
	2. 停止服务

	    ```shell
        killall svnserve
        ```

5. 访问仓库项目

	我们有两个代码仓库 */home/svn/one、/home/svn/two* ，用`svnserve -d -r /home/svn`启动服务后，可以在通过以下地址访问两个项目：
	`svn://ip地址/one, svn://ip地址/two`
	
6. SVN客户端操作

    ```shell
    svn checkout svn://ip地址/one	/var/www/abc/
    ```
	输入user1或user2的账户名和密码
	```shell
    svn add /var/www/abc/*
    svn delete /var/www/abc/某文件
    svn commit -m"信息" /var/www/abc/*
    svn update [-r 版本号] /var/www/abc
    ```