### nginx+PHP配置（macOS）

>以下以 Homebrew 安装的 nginx 和 PHP 为例。macOS 从 Monterey（12）起不再预装 PHP。[PHP 手册](https://www.php.net/manual/en/install.macosx.bundled.php)

1. 安装 nginx 和 PHP，PHP-FPM 随 Homebrew 的 `php` 软件包提供。

    ```shell
    brew install nginx php
    brew --prefix        # 配置文件位于此前缀下的 etc/nginx/nginx.conf
    brew --prefix nginx  # nginx 安装位置
    ```
2. PHP

    1. 配置PHP

        查看 `$(brew --prefix)/etc/php/主版本.次版本/php-fpm.d/www.conf` 中的 `listen`。下例使用 `127.0.0.1:9000`；若使用 Unix 套接字，nginx 的 `fastcgi_pass` 也要改为对应的 `unix:/路径`。
    2. 启动php-fpm

        `brew services start php`

        >1. 查看服务状态：`brew services list`
        >2. 关闭 php-fpm：`brew services stop php`
3. nginx

    1. 配置nginx

        1. `vi "$(brew --prefix)/etc/nginx/nginx.conf"`：

            ```text
            worker_processes  1;

            error_log  /tmp/nginx_error.log;

            events {
                worker_connections  1024;
            }

            http {
                include       mime.types;
                default_type  application/octet-stream;

                sendfile        on;

                keepalive_timeout  65;

                server {
                    listen       8080;
                    server_name  localhost;
                    root 文件夹路径;     # 如：/Users/Geoffrey/www

                    location / {
                        index index.php index.html index.htm;
                        try_files $uri $uri/ =404;
                        #try_files $uri $uri/ /index.php?$query_string;
                    }

                    location ~* \.php$ {
                        try_files $uri =404;
                        include fastcgi_params;
                        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
                        fastcgi_pass 127.0.0.1:9000;
                    }

                    error_page   500 502 503 504  /50x.html;
                    location = /50x.html {
                        root   html;
                    }
                }

                include servers/*.conf;
            }
            ```
        2. `vi "$(brew --prefix)/etc/nginx/servers/域名.conf"`：

            1. 静态文件虚拟主机。若还要运行 PHP，将 `root` 放到 `server` 层，并用上例的 PHP 处理块替换下面返回 404 的规则。

                ```text
                # servers/域名1.conf

                server {
                    listen       8080;
                    server_name  域名1;

                    location / {
                        root 文件夹路径;     # 如：/Users/Geoffrey/www/dev.me
                    }
                    location ~* \.php$ { return 404; }
                }
                ```
            2. 代理转发

                ```text
                # servers/域名2.conf

                server {
                    listen       8080;
                    server_name  域名2;

                    location / {
                        proxy_pass http://域名3:端口号;
                    }

                }
                ```
    2. 启动nginx

        1. 检查脚本（语法正确性、配置脚本位置）

            `nginx -t`
        2. 启动

            `brew services start nginx`

            >1. 重载配置
            >
            >    `nginx -t && nginx -s reload`
            >2. 关闭
            >
            >    `brew services stop nginx`
4. 绑定hosts

    `sudo vi /etc/hosts`：添加 `127.0.0.1 域名`，然后访问 `http://域名:8080/`。验证默认站点的 PHP 时，可在其 `root` 目录创建 `check.php`，内容为 `<?php echo 'PHP OK';`；访问 `http://localhost:8080/check.php` 应只显示 `PHP OK`，验证后删除该文件。

- 文件权限根据具体出现的问题调整。
