#LAMP环境配置（CentOS7.0）

1. 新增用户
	创建一个新用户，并设置密码，增加进root，apache组内：
	`useradd 用户名
	passwd 用户名
	usermod -a -G root,apache 用户名`
	
	>若无法使用**sudo**命令：
	>   1. 进入root模式：
	>		`su root`
	>   2. 添加 */etc/sudoers* 文件的写权限：
	>       `chmod u+w /etc/sudoers`
	>   3. 编辑 */etc/sudoers* 文件：
	>       `vim /etc/sudoers`
	>       找到这一行：**root ALL=(ALL) ALL**在下面添加：
	>       `用户名 ALL=(ALL) ALL`
	>   4. 撤销文件的写权限：
	>       `chmod u-w /etc/sudoers`

2. 安装环境
	安装**apache，php**：
	`sudo yum install httpd
	sudo yum install php`
	
	安装**mysql**：
	1. CentOS 7的yum源中似乎没有正常安装mysql时的mysql-sever文件，需要去官网上下载
		`wget http://dev.mysql.com/get/mysql-community-release-el7-5.noarch.rpm
		sudo rpm -ivh mysql-community-release-el7-5.noarch.rpm
		sudo yum install mysql-community-server`
	2. 成功安装之后重启mysql服务
		`sudo service mysqld restart`
	3. 设置mysql的root账户密码
		`mysql -uroot
		mysql> set password for ‘root’@‘localhost’ = password('密码');
		mysql> exit`
		再次登入时候用命令：`mysql –uroot –p密码`
	4. 安装依赖软件：
		`sudo yum install php-mysql`
		
		>有可能需要：`sudo yum php-ZendFramework-Db-Adapter-Mysqli.noarch`

3. 配置apache（ */etc/httpd/conf/httpd.conf* ）
	*（以下事例，用3个域名a.com、b.com、c.com都指向本服务器，现在配置前两个域名的虚拟主机，使前两个指向各自的文件夹，第三个和其他没有配置的域名都指向默认的文件夹）*
	1. 网站目录
		创建网站文件夹：
		`sudo mkdir /var/www/a.com
		sudo mkdir /var/www/b.com`
		
		修改文件夹所有者：
		`sudo chown -R 用户名:apache /var/www/a.com
		sudo chown -R 用户名:apache /var/www/b.com`
		
		修改文件夹权限：
		`sudo chmod -R 755 /var/www`
		
		新建网站index.php页面，可以添加phpinfo()内容：
		`vi /var/www/a.com/index.php
		vi /var/www/b.com/index.php`
		
	2. 配置apache虚拟主机
		新建虚拟机配置文件夹：
		`sudo mkdir /etc/httpd/sites-available
		sudo mkdir /etc/httpd/sites-enabled`
		
		修改apache配置，新增默认访问路径和包含配置文件夹：
		`sudo vi /etc/httpd/conf/httpd.conf`
		第一行增加：
		```
		<VirtualHost *:80>
			ServerName localhost
			ServerAlias localhost
			DocumentRoot /var/www/html
			ErrorLog /var/www/html/error.log
			CustomLog /var/www/html/requests.log combined
		</VirtualHost>
		```
		最后一行增加：
		`IncludeOptional sites-enabled/*.conf`
		
		添加虚拟主机配置：
		- a.com：
		`sudo vi /etc/httpd/sites-available/a.com.conf`
		添加：
		```
		<VirtualHost *:80>
		    ServerName www.a.com
		    ServerAlias a.com
		    DocumentRoot /var/www/a.com
		    ErrorLog /var/www/a.com/error.log
		    CustomLog /var/www/a.com/requests.log combined
		</VirtualHost>
		```
		
		- b.com：
		`sudo vi /etc/httpd/sites-available/b.com.conf`
		添加：
		```
		<VirtualHost *:80>
		    ServerName www.b.com
		    ServerAlias b.com
		    DocumentRoot /var/www/b.com
		    ErrorLog /var/www/b.com/error.log
		    CustomLog /var/www/b.com/requests.log combined
		</VirtualHost>
		```
		
		链接配置文件：
		`sudo ln –s /etc/httpd/sites-available/a.com.conf /etc/httpd/sites-enabled/a.com.conf
		sudo ln -s /etc/httpd/sites-available/b.com.conf /etc/httpd/sites-enabled/b.com.conf`
		
		重启apache：
		`sudo service httpd restart`

4. 使用phpmyadmin
    下载phpmyadmin（<http://www.phpmyadmin.net>）放在项目文件夹下，即可使用。
