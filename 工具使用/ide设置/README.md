#ideSettings

There'are **webstorm** and **phpstorm** settings. I exported these settings to make sure settings in my workplace and my pc are the same.

>- You should choose the **Scheme** of my name -- *Geoffrey* in preferences in "**Code Style**" and "**Colors & Fonts**".
>- There are two types of keymap in "**Keymap**" named *MyMac* for Mac and *MyWindows* for Windows.
>- There is a template of html in "**File and Code Templates**" in settings of webstorm.

- html

    ```html
    <!DOCTYPE html>
    <html lang="zh-cmn-Hans">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
        <meta name="renderer" content="webkit">
        <!--<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no, minimum-scale=1.0, maximum-scale=1.0">-->
        <!--<meta name="format-detection" content="telephone=no,email=no,address=no">-->
        <!--<link rel="dns-prefetch" href="">-->
        <meta name="keywords" content="">
        <meta name="description" content="">
        <link rel="shortcut icon" type="image/ico" href="favicon.ico">
        <title>#[[$Title$]]#</title>
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
    
    <!-- 多大图模式-->
    <div class="header">
        <div class="wrap">
    
        </div>
    </div>
    <div class="main">
        <div class="wrap">
    
        </div>
    </div>
    <div class="footer">
        <div class="wrap">
    
        </div>
    </div>
    <!--/多大图模式-->
    <!-- 单大图模式-->
    <div class="full_bg">
        <div class="header">
    
        </div>
        <div class="main">
    
        </div>
    </div>
    <div class="footer">
        <div class="wrap">
    
        </div>
    </div>
    <!--/单大图模式-->
    
    <script type="text/javascript" src=""></script>
    <script type="text/javascript">
        $(function () {
    
        });
    </script>
    </body>
    </html>
    ```