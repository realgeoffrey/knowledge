#杂论

##CSS
- 限定布局宽度，让内容决定布局高度。

- z-index用于控制设置了absolute、relative或fixed定位的元素。应该只给有堆叠关系的节点设置此属性，而不要试图通过设定个别元素的z-index来确保元素不重叠。

- 用css创造三角形

    ```css
    div {
        border: 12px solid;
        border-color: transparent #000 transparent transparent;
        height: 0;
        width: 0;
    }
    ```

- 清除浮动：
    - 在父级设置
    
        ```css
        .clearfix:after {
           display: block;
           clear: both;
           content: ".";
           visibility: hidden;
           height: 0;
        }
        .clearfix {
           zoom: 1;
        }
        ```
    - 截断不影响时，在父级设置
    
        ```css
        .father {
            overflow: hidden;
            _width: 100%;
        }
        ```


##HTML + CSS
- 垂直居中

    ```html
    <div class="box">
        <img> or <span>...</span>
    </div>
    ```

    ```css
    .box {  /* 此层不能是float或absolute，可以在此层外嵌套*/
        display: table-cell;
        height: 114px;  /* height/font-size = 1.14*/
        *font-size: 100px;
        vertical-align: middle; /* 无继承性*/
        text-align: center; /* 有继承性*/
    }
    span {  /* 必须是内联元素*/
        display: inline-block;
        vertical-align: middle;
        /* font-size覆盖父级的字体*/
    }
    img {
        vertical-align: middle;
    }
    ```

- 响应式设计之媒体查询
    - css属性：`@media (min-width: 360px) and (max-width: 640px) {...}`
    - html标签：`<link rel="stylesheet" type="text/css" media="(min-width: 360px) and (max-width: 640px)" href="...">`

- 响应式设计三大要素
    - 媒体查询
    - 流式布局：节点用百分比
    - 弹性图片： `img {max-width: 100%;}`
    - wap可以用rem和html的font-size配合


##JavaScript
- if中用赋值（大部分是误用）并非总是返回真值：`if(var = false){...}`中的条件判断为假。

- JS性能
    - 平稳退化：当浏览器不支持或禁用了JS功能后，访问者也能完成最基本的内容访问。
        - ~~伪协议(javascript:)~~
            >`<a href="javascript: func();">...</a>`

        - ~~内嵌事件处理函数~~
            >`<a href="#" onclick="func();return false;">...</a>`
        - 为JS代码预留出退路
            >`<a href="真实地址" class="j-func">...</a>`
