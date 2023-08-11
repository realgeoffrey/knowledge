### 水印合成
>参考：[谈谈前端水印实现的几种方式](https://developer.aliyun.com/article/859086)、[从破解某设计网站谈前端水印(详细教程)](https://juejin.cn/post/6900713052270755847)

1. 前端合成水印图

    - 优势

        1. 不占用服务器资源，完全依赖客户端的计算能力，减少服务端压力。
        2. 速度快，无论哪种前端的实现方式，性能都优于后端。
        3. 实现方式简单。

    1. 在目标区域 上或下 额外覆盖水印图或水印DOM（注意：透明度+点击穿透+文本不被选中），或在目标区域DOM加水印图background

        水印图可以用后台返回、canvas生成、svg生成。

        - 可以监听水印节点的`MutationObserver`进行重新复原防删除

            ><details>
            ><summary>破解</summary>
            >
            >1. 开发者工具 -> 设置 -> 偏好设置 -> 调试程序 -> 停用 JavaScript。
            >2. 或 复制`<body>`后查看（不包含监听代码）。
            >3. 或 代理前端代码，找到水印相关代码删除。
            ></details>
    2. 或通过canvas，把原图和水印内容合成后导出base64替换原图展示（注意：canvas操作原图的跨域限制、导出不支持gif）
2. 后端返回水印图

    - 优势

        安全性高。

    >Node.js图片处理库：[gm](https://github.com/aheckmann/gm)、[images](https://github.com/zhangyuanwei/node-images)、[jimp](https://github.com/jimp-dev/jimp)

- 暗水印/隐水印

    通过某种加密算法，把图片的每个像素点进行肉眼无法分辨的修改，再把泄露的图进行这种解密算法，从而获得加密写入的额外信息。
