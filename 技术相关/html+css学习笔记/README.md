#html+css学习笔记

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
- 单行文本和多行文本超出显示省略号

    ```css
    .ellipsis {
        _width: 100%;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }
    .multi_ellipsis {
        line-height: 1;
        height: 2em;
        display: block;
        display: -webkit-box;
        *display: block;
        overflow: hidden;
        text-overflow: ellipsis;
        -webkit-box-orient: vertical;
        -webkit-line-clamp: 2;
    }
    ```

- 单词内断字换行
    - ~~默认~~
        若此行放不下则整个单词换行,若下行也放不下则溢出(保持单词不断词)
    - ~~`word-break: break-all;`~~
        若此行放不下则直接断词,不会尝试整个单词换行
    - `word-wrap: break-word;`
        若此行放不下则整个单词先换行,若下行也放不下再断词

- body标签设置min-width属性为项目内容宽度(忽略ie6)

    ```css
    body {
       min-width: ;
    }
    ```

-  块级元素的width
    - `width: auto;`
        默认值,换算具体值为:**本元素width = 父级width - 本元素(margin + padding + border)水平值**

        >当块级width为默认的auto时,设置负的水平margin会使width增加

    - `width: 100%;`
        负值父级的px为自己的px






##HTML + CSS
- 垂直居中

    ```html
    <div class="box">
        <img src=""> or <span>...</span>
    </div>
    ```

    ```css
    .box { /* 此层不能是float或absolute，可以在此层外嵌套*/
       display: table-cell;
       height: 114px; /* height/font-size = 1.14*/
       *font-size: 100px;
       vertical-align: middle; /* 无继承性*/
       text-align: center; /* 有继承性*/
    }
    span { /* 必须是内联元素*/
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