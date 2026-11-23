### 离线包差量更新方案
>离线包管理系统：离线包生成、配置（差量包对应旧版本、上/下线状态、灰度、白名单、等）、监控统计，线上服务。

0. 客户端后台起个服务执行以下逻辑（一般是客户端SDK实现，也可以是前端调用bridge实现）
1. 方案一

    >利用[bsdiff/bspatch](https://github.com/mendsley/bsdiff)。

    1. 素材：①本地资源旧包A、②差量资源包B（利用bsdiff由A和最新资源包C对比产生）、③经发布方签名验证的清单，包含目标版本和C的 SHA-256 摘要。
    2. 步骤：

        1. 确认A是B支持的基线版本，用bspatch将A和B合并为临时包D，计算D的 SHA-256 摘要。
        2. 若摘要与清单一致，则原子切换到D。
        3. 若合并或校验失败，下载全量包C，通过同样的校验后再切换；下载中断或校验失败时继续使用A。
2. 方案二（类似[HMR](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/webpack学习笔记/README.md#热更新hot-module-replacementhmr模块热替换)）

    确认基线版本后，根据已验签的 manifest.json 下载有变化的文件。先在新版本目录补齐并校验整组资源，再切换入口，避免更新中断时混用两个版本。
