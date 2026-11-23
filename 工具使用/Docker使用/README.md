## 目录
1. [Docker使用](#docker使用)
1. [在k8s中使用](#在k8s中使用)
1. [Docker优势、劣势](#docker优势劣势)

---
### [Docker](https://www.docker.com/)使用
>1. 虚拟机：虚拟出一套硬件，运行一个完整的操作系统，然后在这个系统上安装和运行软件。
>2. 容器：没有自己的内核、没有虚拟出硬件，Linux 容器内应用使用运行 Docker Engine 的 Linux 内核（macOS 上由 Docker Desktop 的 Linux 虚拟机提供）（容器化技术并不是模拟的一个完整操作系统）。

1. 核心概念

    1. 镜像（Image）
    2. 容器（Container）
    3. 仓库（Repository）
2. [Docker命令](https://docs.docker.com/reference)

    >支持传参模式：`--key=value`或`--key value`。

    1. 安装、启动

        ```shell
        # 受支持的 Linux 发行版：开发/测试环境可用此安装脚本。macOS 可安装并启动 Docker Desktop
        curl -fsSL https://get.docker.com/ | sh

        # 使用 systemd 的 Linux 上启动 Docker Engine（需要管理员权限）
        sudo systemctl start docker

        # 安装信息
        docker info
        ```

    - [Daemon配置文件](https://docs.docker.com/engine/reference/commandline/dockerd/)

        1. 地址（默认）：

            1. Linux：`/etc/docker/daemon.json`
            2. Windows：`%programdata%\docker\config\daemon.json`
            3. macOS：Docker Desktop -> Settings -> Docker Engine
        2. 配置项

            1. 镜像源：`"registry-mirrors" : ["镜像源地址"]`

                >`镜像源地址（registry mirrors）` 不等于 `Docker源地址（Docker Registry）`。

    2. 查看、操作镜像

        >联合文件系统（UnionFS），支持分层（layer）。

        ```shell
        # 查看本地镜像
        docker images
        -a      # 显示所有的镜像，包括中间层镜像
        -q      # 仅显示镜像ID


        # 删除镜像（需要此镜像没有在容器中使用）
        docker rmi 「镜像ID或镜像名」
        -f      # 强制删除
        # 删除所有：`docker rmi $(docker images -a -q)`

        # 删除悬空镜像（没有仓库名或标签的镜像，`<none>`）
        docker image prune
        -f      # 不提示确认
        -a      # 删除所有未使用的镜像，而不仅仅是悬空的镜像
        --filter    # 过滤器


        # 搜索镜像，或去网站搜索，如：https://hub.docker.com/
        docker search 「关键字」

        # 拉取远程镜像到本地
        docker pull 「镜像名，如：Docker源地址/用户名/镜像名:tag名」


        # 查看镜像构建历史
        docker history 「镜像名或ID」


        # 使本地镜像增加镜像名、标签
        docker tag 「来源：Docker源地址/用户名/镜像名:tag名」 「目标：Docker源地址/用户名/镜像名:tag名」


        # 保存 镜像 到本地文件
        docker save --output=「地址/文件.tar」 「镜像名或ID」

        # 加载本地文件到镜像
        docker load --input=「地址/文件.tar」


        # 导出 容器的文件系统 到本地文件
        docker export --output=「地址/文件.tar」 「容器ID或容器名」

        # 导入本地文件到镜像
        docker import 「地址/文件.tar 或 URL 或 -」 [「Docker源地址/用户名/镜像名:tag名」]
        ```

        >镜像是 根文件系统更改 和 在容器运行时中使用的相应执行参数 的有序集合。镜像通常包含堆叠在彼此之上的分层文件系统的联合。镜像没有状态，它永远不会改变。
    3. 用镜像启动一个容器

        >用镜像启动一个容器时，会在镜像层顶部新增一个**可写**的容器层。写入挂载路径的数据则保存到对应的挂载中。

        `docker run [「参数」] 「镜像名或ID」 [「命令」 [「命令参数」]]`

        >容器参数必须加在`run`和`镜像名或ID`之间。

        1. `-p=「[宿主机IP:]宿主机端口」:「容器端口」`

            发布端口时，省略宿主机 IP 默认绑定所有接口。仅供本机访问可用 `-p 127.0.0.1:1234:8080`；在 Docker Engine 28.0.0 之前，同一二层网段的其他主机仍可能访问该端口。可以设置多个，e.g. `-p 1234:8080 -p 3333:3000`。[Docker 端口发布说明](https://docs.docker.com/engine/network/port-publishing/)

            ><details>
            ><summary>e.g.</summary>
            >
            >1. 宿主机监听80端口、配置转发xxx.com到1234端口，hosts配置：`127.0.0.1 xxx.com`，Docker 将宿主机1234端口映射到容器内部4321端口（`-p=1234:4321`）。
            >2. 宿主机请求xxx.com：hosts到127.0.0.1:80->端口转发到127.0.0.1:1234->Docker 转发到容器内的4321端口，由容器内的服务处理并返回。
            ></details>

            1. `-P`

                随机宿主机端口:Dockerfile的EXPOSE。

            >相同的宿主机端口，不能被同时启动。
        2. `-d`

            后台方式运行。
        3. `-e 「本地环境变量名」`或`-e 「环境变量名」=「值」`

            设置容器内环境变量。若没有 ~~`=`~~，则使用宿主环境的环境变量值；若没有 ~~`=`~~ 且宿主环境没有这个环境变量值，则不设置。
        4. `-it`

            保持标准输入打开（`-i`）并分配伪终端（`-t`）。以 shell 作为主进程时，退出它会使容器停止。

            >e.g. `docker run -it 「镜像名或ID」 /bin/bash或/bin/sh`
        5. `--rm`

            若容器退出，则自动删除容器。
        6. `-v=[「宿主机目录或文件 或 数据卷名字」:]「容器内目录或文件」`

            宿主机与容器创建数据卷。

            >若`数据卷名字`不存在，则会自动创建一个命名数据卷。
        7. `--volumes-from=「容器ID或容器名」`

            容器间共用数据卷。从另一个容器中挂载已创建好的数据卷。
        8. `--name=「容器名」`

            给运行的容器增加一个容器别名，容器ID和容器名均指向此容器。
        9. `--cidfile=「新文件路径」`

            尝试创建一个新文件，并将容器ID写入它。若文件已存在，将返回一个错误。Docker运行退出时，Docker将关闭此文件。
        10. `--pid=host`或`--pid=container:「容器ID或容器名」`

            进程管理。
        11. `--uts=host`
        12. `--ipc=「none|private|shareable|container:「容器ID或容器名」|host|""（默认）」`
        13. 网络

            1. `--link=「容器ID或容器名」`

                默认 bridge 上的旧式链接会在接收方容器中加入对端的 hosts 映射。使用自定义 bridge 网络时，同一网络内的容器可直接通过容器名或网络别名互访。[Docker 旧式链接说明](https://docs.docker.com/engine/network/links/)
            2. `--dns=`
            3. `--network=「none|bridge（默认）」|host|container:「容器ID或容器名」|「用户自定义」`

                网络连通性。
            4. `--network-alias=`
            5. `--add-host=`
            6. `--mac-address=`
            7. `--ip=`
            8. `--ip6=`
            9. `--link-local-ip=`
        14. `--restart=「no（默认）|on-failure[:max-retries]|always|unless-stopped」`
        15. `--security-opt`
        16. `-w=「容器内路径」`

            设置命令（`CMD`或替换命令）执行的路径（若容器内部不存在设置的路径，则新建）。
        17. `--entrypoint=「值」`

            覆盖镜像的ENTRYPOINT值。
        18. `--cap-add=「值」`、`--cap-drop=「值」`

            增加Linux能力、去除Linux能力。

    - 持久化存储：宿主机中的一个目录或文件。用于容器数据持久化 或 （外部服务与容器内部、容器间）数据同步。

        1. Docker容器中产生的数据 与 宿主机 互相同步。
        2. 一个数据卷可以同时被多个容器同时挂载（容器间数据同步）。
        3. 一个容器也可以被挂载多个数据卷。

        >容器停止后，卷或绑定挂载的源数据仍保留。

        1. 命名数据卷（Named Volumes）

            `docker volume create/ls/inspect/rm/prune`
        2. 绑定挂载（Bind Mounts）

            - 挂载时文件或文件夹覆盖问题：

                1. 文件夹

                    源目录可有内容。源路径不存在时，`-v`会创建目录，`--mount type=bind`默认报错。
                    挂载期间，容器目标目录的原内容被遮住；用同一镜像启动不带挂载的新容器仍可看到它。
                2. 文件

                    先创建宿主机源文件；否则`-v`会创建同名目录。
                    挂载期间，容器的目标路径显示宿主机文件的内容。

        - 对比

            |  | Named Volumes | Bind Mounts |
            | :--- | :--- | :--- |
            | Host Location | Docker chooses | You control |
            | Mount Example (using `-v`) | `「my-volume」:/usr/local/data` | `「/path/to/data」:/usr/local/data` |
            | Populates new volume with container contents | yes | no |
            | Supports Volume Drivers | yes | no |

        3. tmpfs mounts（Linux）
        4. named pipes（Windows）

        >[Docker: storage](https://docs.docker.com/storage/)

    4. 容器操作

        >互相隔离，每个容器都有一个属于自己的文件系统、网络、进程树。

        1. 查看、启动/关闭/删除

            ```shell
            # 获取当前运行的容器信息（PORTS 宿主机端口 -> 容器内端口）
            docker ps
            -a      # 显示所有的容器，包括未运行的
            -q      # 仅显示容器ID


            # 删除容器（不能删除正在运行的容器）
            docker rm 「容器ID或容器名」
            -f      # 强制删除
            # 删除所有：`docker rm $(docker ps -a -q)`

            # 删除所有停止的容器
            docker container prune
            -f      # 不提示确认
            --filter    # 过滤器


            # 启动容器
            docker start 「容器ID或容器名」

            # 停止容器（`-t=「时间 默认10」`：若超时未能关闭则强制kill）
            docker stop 「容器ID或容器名」

            # 强制直接关闭容器
            docker kill 「容器ID或容器名」

            # 关闭容器，内部的文件也不会被清除。除非把容器删除，否则无论容器是否运行，文件都存在，并且文件都可以被宿主机拷贝

            # 重启容器（无论容器是否已启动）
            docker restart 「容器ID或容器名」
            ```
        2. 进入容器shell

            ```shell
            # shell进入容器内（创建新终端进程）
            docker exec -it 「容器ID或容器名」 /bin/bash或/bin/sh

            # 连接到容器主进程的标准输入、输出和错误；若主进程是交互式 shell，exit 会停止容器
            docker attach 「容器ID或容器名」
            ```
        3. 查看：

            1. 容器日志

                ```shell
                docker logs 「容器ID或容器名」
                -t      # 展示时间戳
                -f      # 持续输出容器的新日志
                --tail=「数字」 # 最后n条日志
                ```
            2. 容器底层基础信息

                ```shell
                docker inspect 「容器ID或容器名」
                ```
            3. 容器资源使用情况

                ```shell
                docker stats [「容器ID或容器名」]
                ```
            4. 容器进程信息

                ```shell
                docker top 「容器ID或容器名」
                ```
        4. 拷贝内容

            >容器不运行也可以正常拷贝。

            ```shell
            docker cp 「容器ID或容器名」:「文件路径」 「宿主机保存路径」   # 容器 -> 宿主机
            docker cp 「宿主机文件路径」 「容器ID或容器名」:「保存路径」   # 宿主机 -> 容器
            ```
    5. 容器网络

        >Linux 上默认 bridge 网络通常使用宿主机的 docker0 网桥；Docker Desktop 的 Linux 网桥位于虚拟机内。

        `docker network create/connect/disconnect/inspect/ls/prune/rm`

        1. 默认配置下，同一 bridge 网络内的容器可直接通信；不同 bridge 网络间可通过已发布的宿主机端口通信。
        2. 将容器设置在网络上的两种方法：

            1. 在开始时分配它

                `docker run` + `--network=「网络名」`
            2. 连接现有的容器

                `docker network connect 「网络名」 「容器ID或容器名」`

        >[Docker: network](https://docs.docker.com/network/)。

    - Prune一切

        ```shell
        # all stopped containers
        # all networks not used by at least one container
        # all dangling images
        # all build cache
        docker system prune
        -f      # 不提示确认
        -a      # 删除所有未使用的镜像，而不仅仅是悬空的镜像
        --filter    # 过滤器
        --volumes   # 同时清理未被容器引用的匿名卷
        ```

    6. 新建、提交镜像

        >Docker源：[Docker Hub](https://hub.docker.com/)是Docker公司官方提供的公共容器镜像注册中心；[harbor](https://github.com/goharbor/harbor)是开源的企业级容器镜像注册中心，提供私有的容器镜像仓库解决方案。

        - 登录、登出

            ```shell
            # 登录
            docker login [「Docker源地址」]  # 交互登录；自动化可用 --username 和 --password-stdin

            # 登出
            docker logout [「Docker源地址」]


            # 登录配置文件为 ~/.docker/config.json，可能含凭据，请勿公开其内容。
            ```

        1. 根据容器创建新镜像

            >最好用Dockerfile方式替代。

            ```shell
            # 根据一个已存在的容器创建一个新的镜像（不包括安装在容器内的数据卷中包含的任何数据）
            docker commit 「容器ID或容器名」 [「新的镜像名」[:「tag，如：1.0.0」]]
            -m="「描述信息」"        # Commit message
            -a="「作者」"           # 作者
            -c="「Dockerfile指令」" # Apply Dockerfile instruction to the created image
            ```
        2. 推送镜像到远程仓库

            ```shell
            # （除非是认证的组织）镜像名必须包含用户名的namespace，如：`你的账户名/镜像名`
            docker push 「镜像名，如：Docker源地址/用户名/镜像名:tag名」
            ```

    - Dockerfile

        包含一系列命令的文件，用于自动构建镜像。

        1. `docker build [「参数」] 「路径（如：.） 或 URL 或 -」`

            通过Dockerfile和构建上下文（context）构建镜像；BuildKit 可并行构建互不依赖的阶段。

            1. `-f 「文件路径」`

                设置Dockerfile的文件路径（默认当前目录下的`Dockerfile`）。
            2. `-t 「用户名/镜像名[:「tag，如：1.0.0」]」`

                创建镜像的名字。可以同时添加多个：`-t xx -t xx`。
            3. `--target 「多阶段构建的名字」`

                将指定阶段作为最终镜像。BuildKit 仅构建该阶段及其依赖阶段。
            4. `--build-arg 「名」=「值」`

                传入Dockerfile构建参数。构建时，docker无法获得系统环境变量，需要传入（`ARG`）或者构建文件自己声明（`ENV`）。

            - 构建上下文

                `docker build 「路径」`以该目录为构建上下文；`.dockerignore`排除的文件不供普通 `COPY` 或 `ADD` 使用。
        2. `.dockerignore`

            忽略文件（命令行操作 以及 Dockerfile的`ADD`和`COPY` 时忽略的文件/文件夹）。
        3. 指令书写

            ```shell
            # 解析器指令（Parser directives），需要在文本最前面书写
            # 「`syntax`或`escape`」=「值」

            # 注释会在执行命令前被删除

            # 指令不区分大小写。惯例是将它们大写以更轻松地将它们与参数区分开

            # 同一阶段会保留文件系统变更；单条 RUN 中的 cd 不会改变下一条 RUN 的工作目录，可用 WORKDIR 设置

            # 指令语法：INSTRUCTION arguments

            FROM        # 来源的基础镜像（最基本镜像：scratch） 或 （多阶段构建的）之前阶段
                        # 单个Dockerfile文件可以包含多个FROM指令从而进行多阶段构建
                        # + `as 「名字」`用于指定多阶段构建的某一阶段名字，作用：
                        #   1. `docker build`+`--target=「名字」`设置为最终阶段
                        #   2. `COPY --from=「名字」`指定复制来源为此构建内容
                        #   3. 之后阶段`FROM`之前阶段

            RUN         # 镜像构建的时候需要运行的命令
                        # 是在镜像中进行操作，不是在构建上下文

            LABEL       # 向镜像添加元数据

            EXPOSE      # 声明容器监听的端口；-P 发布声明的端口，-p 可显式发布任意容器端口
                        # 可以设置多个：e.g. `EXPOSE 8080 3000`或多个EXPOSE指令

            ENV         # 构建时，设置环境变量。e.g. `ENV xx=「值」`
                        # 定义后使用：`${变量名}`或`$变量名`。`\`转义的不会去使用变量：`\${xx}`或`\$xx`
                        # 一个ENV命令结束后的下一条才能使用之前设置的环境变量
                        # 构建时存在 且 镜像启动的容器也会保留（环境变量）

            ARG         # `docker build` + `--build-arg 「名」=「值」`传入的键-值
                        # e.g. 定义：ARG key1[=「默认值」]；使用：$key1
                        # 仅构建时存在，不会保留到容器中（不写入环境变量）

            ADD         # 添加文件；默认自动解包可识别的本地 tar 归档（含受支持的压缩格式）

            COPY        # 将文件拷贝到镜像中。从 构建上下文 向 镜像 操作
                        # `--from=「多阶段构建的序号（从0开始）或名字，其他镜像」`：
                        #   用某个多阶段构建的内容 或 其他镜像内容 替代docker build的构建上下文

                        # 不太支持在Dockerfile内进行判断文件（夹）是否存在后进行复制操作，最好是在外部创建构建上下文的时候就确定文件（夹）已经存在：
                        #   https://stackoverflow.com/questions/31528384/conditional-copy-add-in-dockerfile
                        # 添加的同名文件夹会合并，同名文件以之后操作的覆盖之前的

            VOLUME      # 声明容器内的卷挂载点；宿主机源路径在运行时指定

            WORKDIR     # 设置当前工作目录。若提供了相对路径，则相对于前一条WORKDIR指令的路径
                        # 建议仅用绝对路径；建议替代难以维护的`cd`，如：`RUN cd ... && ...`

            ONBUILD     # 其他镜像使用当前镜像时（FROM），触发的指令

            USER

            STOPSIGNAL

            HEALTHCHECK

            SHELL

            CMD         # 指定这个容器启动时运行的命令。运行容器时追加的指令，会覆盖CMD
                        # 为了避免容器一启动运行完命令就停止，需要在最后添加占据前台的命令

            ENTRYPOINT  # 指定这个容器启动时运行的命令。exec 形式会接收运行时参数；shell 形式会忽略 CMD 或运行时追加的参数
            ```

            1. Docker 镜像的文件系统由**只读**层叠加而成。`RUN`、`COPY`等可产生文件系统层，`CMD`等仅改变镜像配置。

                需清理的临时文件应在创建它们的同一条 `RUN` 中删除，避免留在前一层。

                ><details>
                ><summary>e.g.</summary>
                >
                >```dockerfile
                >FROM python:3.13-slim
                >WORKDIR /app
                >COPY . .
                >CMD ["python", "app.py"]
                >```
                ></details>
            2. 当运行一个镜像并生成一个容器时，会在层的顶部添加一个新的**可写**层（“容器层”）。对正在运行的容器所做的所有更改，例如写入新文件、修改现有文件和删除文件，在未挂载的路径下会写入此可写容器层。
        4. 多阶段构建

            多阶段构建时，可将编译产物复制到独立的运行时阶段，让编译器和中间文件留在构建阶段。
        5. 多服务执行

            >为了从Docker中获得最大收益，请避免一个容器负责整个应用程序的多个方面。可以使用用户定义的网络和共享数据卷连接多个容器。

            1. 把多服务放在一个脚本中，用`CMD`运行这个脚本。
            2. 或 使用其他守护进程管理多服务（如：supervisord等），用`CMD`运行这个守护进程。

    7. 扫描镜像

        >使用 [Docker Scout](https://docs.docker.com/scout/quickstart/) 检查镜像中软件包的已知漏洞。

        1. 在已开启 Scout 分析的 Docker Hub 仓库中，推送镜像后会触发分析。
        2. 或 主动运行命令

            ```shell
            # 扫描镜像
            docker scout cves 「镜像名」
            ```

### 在k8s中使用
1. 单个服务打包成docker镜像，可运行在容器内；
2. 每个 Pod 包含一个或多个容器；可配置 HPA 根据 CPU 利用率或自定义指标（如 QPS）调整工作负载的副本数；
3. Pod 通常有集群内 IP，重建后可能变化；Service 为后端 Pod 提供稳定入口；
4. 对外服务可将域名指向负载均衡器，由 Service 将流量转发到就绪的后端 Pod。

- k8s与docker关系

    1. docker

        一种开源的容器化技术，关键概念：镜像、容器、仓库。能提供隔离的容器化服务，方便快速创建和管理容器。
    2. k8s

        用于自动部署、扩展和管理“容器化（containerized）应用程序”的开源系统。提供丰富的功能，如：自动伸缩、服务发现、负载均衡、容器编排等。
    3. pod

        1. pod是k8s调度的最小单元。
        2. 1个pod可以包含1个或多个容器，可以理解为pod是容器集合。
        3. pod相当于逻辑主机；pod内的容器可以共享相同的ip和端口空间。

### Docker优势、劣势
1. 轻量级和快速启动：

    （相比传统虚拟机虚拟一整套硬件和操作系统，再在上面安装和运行软件，）Docker容器共享宿主机的操作系统内核，因此更轻量级、启动速度非常快，通常只需几秒钟就能启动一个容器。

    >1. 性能开销：Docker容器运行在宿主机操作系统上，容器与宿主机共享操作系统内核。这种共享机制可能导致一些性能开销，尤其是在高负载和资源密集型应用的情况下。
    >
    >2. 不适合全虚拟化应用：Docker容器主要适用于应用程序的封装和部署，但对于某些需要完全虚拟化的应用（如某些操作系统级别的任务），容器化方案可能不太适合。
2. 高度可移植性：

    Docker 镜像可在兼容的操作系统内核和 CPU 架构上运行；跨架构可选择多平台镜像或使用模拟。容器化应用程序可以在开发、测试和生产环境之间轻松迁移，减少了因环境差异而引起的问题。
3. 应用程序隔离性：

    每个 Docker 容器运行在独立的用户空间中，相互之间具有良好的应用程序隔离性。资源仍由宿主机共享，一个容器耗尽内存等资源时可能影响其他容器。

    >1. 安全性挑战：尽管Docker容器提供了一定的隔离性，但由于容器共享操作系统内核，容器内部的潜在安全漏洞可能会影响整个宿主机系统。
    >
    >2. 复杂网络配置：在复杂的网络环境下，容器之间的网络配置和通信可能会变得复杂，需要一些额外的配置和管理。
4. 灵活的扩展和分发：

    Docker容器使用镜像作为应用程序的构建和分发单元。镜像是一个可重复构建的、可分享的文件，可以快速部署和复制容器。借助编排系统可根据负载增减容器副本，使应用程序具备弹性和可扩展性。

    >1. 持久化存储管理：Docker容器默认情况下是临时的，容器内部的文件系统和数据通常会随着容器的销毁而消失。对于需要持久化存储的应用程序，需要额外的配置和管理，如：使用数据卷或网络存储解决方案。
5. 依赖管理和版本控制：

    Docker容器明确定义了应用程序及其依赖的版本关系，使得依赖管理和版本控制更加简单。容器化应用程序可以明确指定所需的软件库、工具和配置，确保在不同环境中的一致性运行。
