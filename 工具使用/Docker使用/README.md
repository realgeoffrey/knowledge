### [Docker](https://github.com/docker/docker-ce)使用
>之前只能通过虚拟机安装多系统，现在可以使用Docker高性能、低消耗运行多系统。如：使用[centos镜像](https://hub.docker.com/search?q=centos&type=image)。

1. 核心概念

    1. 镜像（Image）
    2. 容器（Container）
    3. 仓库（Repository）
2. [Docker命令](https://docs.docker.com/reference)

    1. 安装、启动

        ```shell
        curl -fsSL https://get.docker.com/ | sh # 安装。或官网安装（https://www.docker.com/products/docker-desktop）

        service docker start    # 启动

        docker info # 安装信息
        ```
    2. 查看、操作镜像

        ```shell
        docker images           # 查看本地镜像

        docker search 「关键字」   # 搜索镜像，或去网站搜索，如：https://hub.docker.com/

        docker pull 「镜像名」     # 拉取镜像

        docker rmi 「镜像ID」      # 删除镜像（需要此镜像没有在容器中使用）
        -f      # 强制删除
        ```
    3. 用镜像启动一个容器

        ```shell
        docker run -p 宿主机端口:容器端口 「镜像名」
        # e.g. 容器暴露端口（把容器的端口与宿主机的端口关联起来）
        #   宿主机nginx监听80端口、配置转发xxx.com到1234端口，hosts配置：`127.0.0.1 xxx.com`，容器docker监听宿主机1234端口映射到容器内部x端口。
        #   宿主机请求xxx.com：hosts到127.0.0.1:80->nginx端口转发到127.0.0.1:1234->1234端口被docker镜像监听，转发到镜像内的x端口，镜像内处理返回。
        -d      # 后台方式运行
        -it     # 使用交互方式运行，进入容器主shell进程（exit会使容器停止）
        --rm    # 若容器退出，则自动删除容器
        ```
    4. 容器

        1. 查看、启动/关闭/删除

            ```shell
            docker ps               # 获取当前运行的容器信息（PORTS 本地端口 -> 容器内端口）
            -a      # 显示所有的容器，包括未运行的


            docker start 「容器ID」    # 启动容器

            docker stop 「容器ID」     # 停止容器（`-t=「时间 默认10」`：若超时未能关闭则强制kill）
            docker kill 「容器ID」     # 直接关闭容器
            # 关闭容器，内部的文件也不会被清除。除非把容器删除，否则无论容器是否运行，文件都存在，并且文件都可以被宿主机拷贝

            docker restart 「容器ID」  # 重启容器（无论容器是否已启动）

            docker rm 「容器ID」       # 删除容器（不能删除正在运行的容器）
            -f      # 强制删除
            ```
        2. 查看日志、shell操作

            ```shell
            docker logs -f 「容器ID」  # 查看容器的日志。流式输出（文件改动后重新输出）
            -t      # 展示时间戳
            --tail 「数字」 # 展示最后n条日志（新增继续增加）

            docker exec -it 「容器ID」 /bin/bash    # shell进入容器内（创建新终端进程）
            docker attach 「容器ID」                # shell进入容器内（进入容器主shell进程，exit会使容器停止）
            ```
        3. 拷贝

            >容器不运行也可以正常拷贝。

            ```shell
            docker cp 「容器ID」:「文件路径」 「宿主机保存路径」   # 容器 -> 宿主机
            docker cp 「宿主机文件路径」 「容器ID」:「保存路径」   # 宿主机 -> 容器
            ```
        4. 其他

            1. 展示容器进程信息

                ```shell
                docker top 「容器ID」
                ```
            2. 展示容器详情

                ```shell
                docker inspect 「容器ID」
                ```
            3. 展示所有容器资源使用情况

                ```shell
                docker stats
                ```
        5. 新建、提交镜像

            1. 新建镜像（本地）

                ```shell
                docker commit 「已存在的容器ID」 「新的镜像名」:「tag，如：1.0.0」  # （本地）根据一个已存在的容器创建一个新的镜像
                -m="「描述信息」"        # Commit message
                -a="「作者」"           # 作者
                -c="「Dockerfile指令」" # Apply Dockerfile instruction to the created image
                ```
