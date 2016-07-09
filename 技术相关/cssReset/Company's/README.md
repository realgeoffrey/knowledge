#cssReset && html template for Company's pc

1. cssReset.css after KS.css

    ```css
    /* 补充KS的reset*/
    html,body,div,span,h1,h2,h3,h4,h5,h6,p,a,img,dl,dt,dd,ul,ol,li,nav,footer,header,
    form,input,textarea,video,audio,iframe,button,pre,code,blockquote,q,
    fieldset,legend,caption,object,article,aside,details,figcaption,figure,hgroup,menu,section {margin:0;padding:0;border:0;font-size:100%;}
    table,tbody,tfoot,thead,tr,th,td {margin:0;padding:0;}
    i,time {font-style:normal;font-weight:500;}
    blockquote,q {quotes:none;}
    blockquote:before,blockquote:after,q:before,q:after {content:'';content:none;}
    hr {display:block;height:1px;border:0;border-top:1px solid #ccc;margin:1em 0;padding:0;}
    button,textarea,:focus {outline:none;}
    img,video,audio {max-width:100%;}
    /*/补充KS的reset*/

    /* 覆盖原框架*/
    .my_topbar {
        position: relative;
        z-index: 1;
    }
    .part_bgcover {
        position: absolute;
        background: url(../images/bg_spread.png) repeat-x;
        left: 0;
        right: 0;
        top: 250px;
        _width: 100%;
        height: 340px;
        z-index: 0;
    }
    /*/覆盖原框架*/
    ```
2. Html template

    ```html
    <!DOCTYPE html>
    <html lang="zh-cmn-Hans">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
        <meta name="renderer" content="webkit">
        <meta name="keywords" content="">
        <meta name="description" content="">
        <title>公司PC项目</title>
        <link href="http://s1.img4399.com/base/css/KS.css" type="text/css" rel="stylesheet">
        <link href="http://s1.img4399.com/base/css/ue_common.css" type="text/css" rel="stylesheet">
        <link href="" type="text/css" rel="stylesheet">
        <script>
            /* 兼容不支持console.log到alert*/
            if (typeof console === "undefined" || console === null || typeof console.log !== "function") {
                console = {};
                console.log = function (msg) {
                    alert(msg);
                };
            }
        </script>
    </head>
    <body>
    <!-- 原框架-->
    <div class="my_topbar">
        <div class="my_wrapper clearfix">
            <div class="my_person">
                <ul class="my_nav">
                    <li class="my_nav_li current">
                        <a class="my_nav_a" href="#" title="首页"><span><i>首页</i></span></a>
                    </li>
                </ul>
                <ul class="my_groupitem">
                    <li class="my_group_li my_dropon">
                        <div class="my_dropmodal my_dropmodal_msg">
                            <ul>
                                <li class="__web-inspector-hide-shortcut__"><a href="#">退出</a></li>
                            </ul>
                        </div>
                    </li>
                </ul>
            </div>
        </div>
    </div>
    <div class="my_ftop">
        <div class="my_fbtm">
            <!-- 插入.full_bg-->
        </div>
    </div>
    <!--/原框架-->


    <div class="full_bg" style="background-image: url(); background-color: #; *background-color: #;">
        <!--<div class="part_bgcover"></div>-->
        <div class="full_wrap" style="background-image: url();">

        </div>
    </div>

    <script type="text/javascript" src=""></script>
    <script type="text/javascript">

    </script>
    </body>
    </html>
    ```