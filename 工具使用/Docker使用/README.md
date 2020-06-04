### [Docker](https://github.com/docker/docker-ce)使用
1. 核心概念

    1. 镜像（Image）
    2. 容器（Container）
    3. 仓库（Repository）
2. 使用

    1. 安装、启动

        ```shell
        curl -fsSL https://get.docker.com/ | sh # 安装。或用官网安装方式

        service docker start    # 启动


        docker pull 「镜像名」    # 拉取镜像

        docker run 「镜像名」     # 运行镜像
        ```
    2. 查看、操作容器

        ```shell
        docker ps                # 获取容器信息，包括ID（`-a`：显示所有的容器，包括未运行的）


        docker start 「容器ID」   # 启动容器

        docker stop 「容器ID」    # 停止容器（`-t=「时间 默认10」`：若超时未能关闭则强制kill）
        # 或
        docker kill 「容器ID」    # 直接关闭容器

        docker restart 「容器ID」 # 重启容器（无论容器是否已启动）

        docker rm 「容器ID」      # 删除容器

        docker logs -f 「容器ID」 # 查看容器的日志。流式输出（文件改动后重新输出）
        ```
