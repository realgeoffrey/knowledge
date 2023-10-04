# 富文本编辑器
>天坑。

## 目录
1. [富文本编辑器实现方式](#富文本编辑器实现方式)
1. [我的富文本编辑器实现（`contenteditable` + `document.execCommand`）](#我的富文本编辑器实现contenteditable--documentexecCommand)

---
>富文本、纯文本、markdown。

### 富文本编辑器实现方式
>[罗龙浩：富⽂本编辑器的技术演进](https://static001.geekbang.org/con/44/pdf/3673881710/file/富文本编辑器的技术演进-罗龙浩.pdf)

1. `contenteditable` + `document.execCommand`

    如：[wangEditor](https://github.com/wangeditor-team/wangEditor)

>注意`document.execCommand`浏览器兼容性，目前已废弃

2. `contenteditable` + `getSelection` + `Range`
3. DOM实现
4. Canvas

    如：[腾讯文档](https://docs.qq.com/)

难度升序，自由度降序：`contenteditable`+`document.execCommand` < `contenteditable`+`getSelection`+`Range` < DOM实现 ≪ Canvas

### 我的富文本编辑器实现（`contenteditable` + `document.execCommand`）
>富文本编辑器（rich text editor）：一种可内嵌于浏览器，所见即所得（what you see is what you get，WYSIWYG）的文本编辑器。

1. 标签、样式注意：

    1. 除了要检测用户输入标签的闭合性之外，还要注意富文本编辑器的祖先元素不要用`<li>`嵌套。

        因为代码中若有单独的`<li>`（没有嵌套`<ol>`或`<ul>`），则会「越级」到跟祖先级`<li>`同级的内容。
    2. 大部分富文本会用`<em>`、`<ol>`、`<ul>`等标签来表示**斜体**、**有序序列**、**无序序列**，因此若用CSS重置了以上标签的样式后，则要在[富文本内重载开启它们的默认效果](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/初始化模板/cssReset.scss#L63-L79)（或定制效果）。
    3. 大部分富文本会在`<table>`上使用`cellspacing`、`border`、`bordercolor`属性设置表格，又因为设置了`border: 0;`的表格无法重载开启以上属性作用，所以CSS重置时[不要重置`table,tbody,tfoot,thead,tr,th,td`的`border`属性](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/初始化模板/cssReset.scss#L26-L27)。
2. 针对`contenteditable="true"`的DOM内容：

    1. 整个块级元素修改，可用：`document.execCommand('formatBlock', false, '<块级标签名>')`，再设置元素的样式。

        >如：「小字体」的块级内容，就可以用`document.execCommand('formatBlock', false, '<h6>')`，然后设置`h6`的小字体样式。
    2. 内部可以嵌入`contenteditable="false"`的DOM：

        1. 不可编辑此嵌入DOM的文本。
        2. 编辑器的删除功能不方便删除此嵌入DOM，需要额外实现删除此嵌入DOM功能（如：点击删除整个DOM）。
        3. 此嵌入DOM恢复原本逻辑交互（如：若是`<a>`，则可以跳转、hover变成鼠标手型）。
    3. 插入一个不可编辑卡片的方式：

        1. 插入一个`contenteditable="false"`的DOM。
        2. 插入一个动态生成的卡片样子的`<img>`。
3. 实现方式：

    1. 使用原生[`document.execCommand`](https://developer.mozilla.org/zh-CN/docs/Web/API/Document/execCommand)操作`contenteditable="true"`的DOM内容（或`document.designMode === 'on'`的整个文档、`某iframe.contentDocument.designMode === 'on'`的整个`<iframe>`）。

        >如：[pell](https://github.com/jaredreich/pell)。

        大部分是添加`指定的几种标签`和`style`的方式进行展示，因此只需定制富文本内指定的几种标签的样式。

        - <details>

            <summary><code>document.execCommand</code>原生支持添加的标签</summary>

            1. `<b>`或`<strong>`
            2. `<i>`或`<em>`
            3. `<u>`
            4. `<strike>`或`<s>`
            5. `<pre>`、`<blockquote>`、`<h1>`~`<h6>`、`<p>`、等块级标签
            6. `<ul>`、`<ol>`、`<li>`
            7. `<img>`
            8. `<a>`
            9. `<hr>`
            10. `<sub>`、`<sup>`
            11. `<table>`
            12. `<font>`
            13. `<small>`、`<big>`
            </details>

            >若要插入其他标签、或修改HTML属性（`style`、`class`等）、或插入整个DOM，则可以用`document.execCommand('insertHTML', false, 'HTML内容')`。
    2. 修改、插入DOM的方式模拟实现DOM的编辑。

        >如：[quill](https://github.com/quilljs/quill)。

        除了添加标签和`style`之外，还会额外添加`class`和DOM（需自定义样式）。

- 总结：

    1. 支持插入定制的HTML标签；控制标签和属性的白名单，避免xss。
    2. 复制-粘贴监控。
    3. 聚焦点的储存。
    4. 浏览器兼容性。
