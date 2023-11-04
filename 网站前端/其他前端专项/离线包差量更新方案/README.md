### 离线包差量更新方案
>离线包管理系统：离线包生成、配置（差量包对应旧版本、上/下线状态、灰度、白名单、等）、监控统计，线上服务。

0. 客户端后台起个服务执行以下逻辑（一般是客户端SDK实现，也可以是前端调用bridge实现）
1. 方案一

    >利用[bsdiff/bspatch](https://github.com/mendsley/bsdiff)。

    1. 素材：①本地资源旧包A、②差量资源包B（利用bsdiff由A和最新资源包C对比产生）、③最新全量资源包C的MD5值c_md5
    2. 步骤：

        1. （判断A版本号是B支持处理的，）A和B通过bspatch进行差量合并（插入新代码、删除旧代码、修改代码），合并完成后生成新的资源包D，获取D的MD5值d_md5
        2. 若 d_md5 === c_md5，则将D替换A（删除A）
        3. 否则，只能全量更新，下载最新全量资源包C包替换A（删除A）
2. 方案二（类似[HMR](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/webpack学习笔记/README.md#热更新hot-module-replacementhmr模块热替换)）

    （判断旧版本包是支持替换处理的，）根据manifest.json找出需要更新的文件，细粒度下载更新替换文件（相对于全量直接全部更新）
