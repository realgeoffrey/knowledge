### [Kubernetes](https://github.com/kubernetes/kubernetes)使用
1. [`kubectl`CLI](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands)

    1. 查看所有信息：

        `kubectl get all -n 「namespace名字」`
    1. 查看所有命名空间：

        `kubectl get namespace`
    2. 查看pod信息：

        ```shell
        kubectl get pod     # 查看所有pod

        kubectl get pod -n 「namespace名字」 | grep 「筛选关键字」 # 查看所有某命名空间的pod

        kubectl describe pod 「pod名字」 # 获取某一个pod详情
        ```
    3. 查看pod内日志：

        ```shell
        kubectl logs 「pod名字」 -n 「namespace名字」 -c 「container名字」  # 查看某一个pod内日志
        -f             # 流式输出（文件改动后重新输出）
        --tail 「数字」   # 最后n条日志
        ```
    3. 用可交互模式执行bash

        `kubectl exec -it 「pod名字」 -n 「namespace名字」 bash`
