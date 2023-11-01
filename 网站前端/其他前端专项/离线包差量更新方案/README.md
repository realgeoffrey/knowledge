### 离线包差量更新方案
1. 方案一

    >利用[bsdiff/bspatch](https://github.com/mendsley/bsdiff)。

    1. 素材：①本地资源旧包A、②差量资源包B（利用bsdiff由A和最新资源包C对比产生）、③最新全量资源包C的MD5值c_md5
    2. 步骤：

        1. A和B通过bspatch进行差量合并（插入新代码、删除旧代码、修改代码），合并完成后生成新的资源包D，获取D的MD5值d_md5
        2. 若 d_md5 === c_md5，则将D替换A（删除A）
        3. 否则，只能全量更新，下载最新全量资源包C包替换A（删除A）
2. 方案二（类似[HMR](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/webpack学习笔记/README.md#热更新hot-module-replacementhmr模块热替换)）

    todo：细节请教

    根据manifest.json找出需要更新的文件，细粒度下载更新替换文件（相对于全量直接全部更新）
