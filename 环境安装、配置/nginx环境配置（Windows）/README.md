### nginx环境配置（Windows）

1. 安装

    从[官网下载页](https://nginx.org/en/download.html)下载 Windows 版 ZIP，解压到本地目录（例如 `C:\nginx`）。
2. 配置nginx

    1. 编辑`路径\nginx\conf\nginx.conf`：

        ```text
        worker_processes    1;

        error_log   logs/error.log;

        events {
            worker_connections  1024;
        }

        http {
            include         mime.types;
            default_type    application/octet-stream;

            sendfile        on;

            server_names_hash_bucket_size   64;

            keepalive_timeout   65;

            server {
                listen      127.0.0.1:80;
                server_name localhost;

                location / {
                    root    E:/www;    # 改为实际静态站点目录，路径使用正斜杠
                    index   index.html index.htm;
                    try_files $uri $uri/ =404;
                    # 单页应用可改为 try_files $uri $uri/ /index.html;（须有 index.html）
                }

                error_page  500 502 503 504  /50x.html;
                location = /50x.html {
                    root    html;
                }
            }

            # 创建 conf/servers 并添加站点配置后，取消下一行注释
            # include servers/*.conf;
        }
        ```
    2. 如需虚拟主机，创建 `conf\servers` 文件夹，每个站点单独保存一个 `.conf` 文件。以管理员权限编辑 `%SystemRoot%\System32\drivers\etc\hosts`，添加一行 `127.0.0.1 dev.test proxy.test`。

        1. 虚拟主机

            ```text
            # 路径\nginx\conf\servers\dev.test.conf

            server {
                listen      127.0.0.1:80;
                server_name dev.test;

                location / {
                    root    E:/www/dev.test;    # 改为实际静态站点目录
                }
            }
            ```
        2. 代理转发

            ```text
            # 路径\nginx\conf\servers\proxy.test.conf

            server {
                listen      127.0.0.1:80;
                server_name proxy.test;

                location / {
                    proxy_pass  http://127.0.0.1:8080;    # 改为实际后端地址和端口
                }
            }
            ```
3. 启动nginx

    在 Windows 的 cmd 中执行 `cd /d "C:\nginx"`（替换为实际解压目录）。以下命令均在此目录执行，以便 nginx 找到相对路径下的配置和日志。

    1. 检查配置语法及配置中引用的文件

        `nginx -t`
    2. 启动

        `start nginx`或运行`nginx.exe`

        确保 80 端口可用，并在站点目录放入 `index.html`。启动后在本机打开 `http://127.0.0.1/`，虚拟主机按各自站名访问。静态站点目录只放可公开的静态文件。PHP 需要另行配置 FastCGI。

        若需局域网测试，给目标站点另加一条监听主机局域网 IP 的 `listen`，放行相应防火墙端口，客户端按[目录页](../README.md)设置 hosts。

        >1. 重新加载配置
        >
        >    `nginx -s reload`
        >2. 关闭
        >
        >    `nginx -s quit` 等待当前请求完成后退出，`nginx -s stop` 快速停止。

    [nginx 官方 Windows 使用说明](https://nginx.org/en/docs/windows.html)
