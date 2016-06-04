#cssReset.css

```css
/* CSS reset*/
html,body,div,span,object,iframe,h1,h2,h3,h4,h5,h6,p,a,img,button,
dl,dt,dd,ul,ol,li,table,caption,tbody,tfoot,thead,tr,th,td,
video,audio,footer,header,pre,code,form,fieldset,legend,input,textarea,blockquote,q,
article,aside,details,figcaption,figure,hgroup,menu,nav,section {margin:0;padding:0;border:0;font-size:100%;vertical-align:baseline;}
body,button,input,select,textarea {font:14px/1.4286 "microsoft yahei",simsun,tahoma,arial,sans-serif;}
h1,h2,h3,h4,h5,h6 {font-size:100%;font-weight:500;}
a,ins {text-decoration:none;}
button,input,select,textarea,:focus {outline:none;}
audio,canvas,video {display:inline-block;*display:inline;zoom:1;}
table {border-collapse:collapse;border-spacing:0;}
hr {display:block;height:1px;border:0;border-top:1px solid #ccc;margin:1em 0;padding:0;}
abbr,acronym {border:0;font-variant:normal;}
del {text-decoration:line-through;}
caption,th {text-align:left;}
blockquote,q {quotes:none;}
blockquote:before,blockquote:after,q:before,q:after {content:'';content:none;}
sub,sup {font-size:75%;line-height:0;position:relative;vertical-align:baseline;}
sup {top:-0.5em;}
sub {bottom:-0.25em;}
article,aside,details,figcaption,figure,footer,header,hgroup,menu,nav,section,summary,iframe,main {display:block;}
img {vertical-align:middle;}
address,caption,cite,code,dfn,th,var,em,i,time {font-style:normal;font-weight:500;}
ol,ul {list-style:none;}

/* -wap*/
img,video {max-width:100%;}
html {-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;-webkit-overflow-scrolling:touch;}
a,button,input,textarea {-webkit-tap-highlight-color:rgba(63,40,1,.3);}
html {-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;}
*,*:before,*:after {-webkit-box-sizing:inherit;-moz-box-sizing:inherit;box-sizing:inherit;}
/*/-wap*/

/* -使用富文本需覆盖*/
.rich_text em {
    font-style: italic;
}
.rich_text ol {
    list-style-type: decimal;
    list-style-position: inside;
}
.rich_text ul {
    list-style-type: disc;
    list-style-position: inside;
}
/*/-使用富文本需覆盖*/
/*/CSS reset*/
/* 全局*/
html, body {
    /*height: 100%;*/
}
html {
    _overflow-x: hidden;
}
body {
    background-color: #fff;
    color: #333;
    min-width: 最小宽度;
    position: relative;
}
a {
    color: #333;
}
a:hover {
    text-decoration: none;
}
.left {
    float: left;
    _display: inline;
}
.right {
    float: right;
    _display: inline;
}
.clearfix:after {
    content: "";
    display: table;
    clear: both;
}
.clearfix {
    *zoom: 1;
}
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
/*/全局*/
/* 单大图模式*/
.full_bg {
    background: url() #fff center 0 no-repeat;
    min-width: 最小宽度;
    _width: 100%;
    overflow: hidden;
}
.full_bg .header,
.full_bg .main {
    background: url() center 0 no-repeat;
    width: ;
    margin: 0 auto;
    position: relative;
}
.footer {
    background-color: #fff;
    min-width: 最小宽度;
    _width: 100%;
}
.footer .wrap {
    width: ;
    margin: 0 auto;
}
/*/单大图模式*/
/* 多大图模式*/
.header {
    background: url() #fff center 0 no-repeat;
    min-width: 最小宽度;
    _width: 100%;
    height: ;
    overflow: hidden;
}
.main {
    background: url() #fff center 0 no-repeat;
    min-width: 最小宽度;
    _width: 100%;
    overflow: hidden;
}
.footer {
    background: url() 0 0 repeat-x;
    min-width: 最小宽度;
    _width: 100%;
    overflow: hidden;
}
.header .wrap,
.main .wrap,
.footer .wrap {
    background: url() center 0 no-repeat;
    width: ;
    margin: 0 auto;
    position: relative;
}
/*/多大图模式*/

/* wap媒体查询（320px~640px），最大width:32rem;*/
@media (max-width: 351px) {
    html {
        font-size: 10px;
    }
}
@media (min-width: 352px) and (max-width: 383px) {
    html {
        font-size: 11px;
    }
}
@media (min-width: 384px) and (max-width: 415px) {
    html {
        font-size: 12px;
    }
}
@media (min-width: 416px) and (max-width: 447px) {
    html {
        font-size: 13px;
    }
}
@media (min-width: 448px) and (max-width: 479px) {
    html {
        font-size: 14px;
    }
}
@media (min-width: 480px) and (max-width: 543px) {
    html {
        font-size: 15px;
    }
}
@media (min-width: 544px) and (max-width: 639px) {
    html {
        font-size: 17px;
    }
}
@media (min-width: 640px) {
    html {
        font-size: 20px;
    }
}
@media (orientation: landscape) {

}
/*/wap媒体查询*/
/* pc媒体查询（980px~1920px），最大width:49rem;*/
@media (max-width: 1028px) {
    html {
        font-size: 20px;
    }
}
@media (min-width: 1029px) and (max-width: 1077px) {
    html {
        font-size: 21px;
    }
}
@media (min-width: 1078px) and (max-width: 1126px) {
    html {
        font-size: 22px;
    }
}
@media (min-width: 1127px) and (max-width: 1175px) {
    html {
        font-size: 23px;
    }
}
@media (min-width: 1176px) and (max-width: 1224px) {
    html {
        font-size: 24px;
    }
}
@media (min-width: 1225px) and (max-width: 1273px) {
    html {
        font-size: 25px;
    }
}
@media (min-width: 1274px) and (max-width: 1322px) {
    html {
        font-size: 26px;
    }
}
@media (min-width: 1323px) and (max-width: 1371px) {
    html {
        font-size: 27px;
    }
}
@media (min-width: 1372px) and (max-width: 1420px) {
    html {
        font-size: 28px;
    }
}
@media (min-width: 1421px) and (max-width: 1469px) {
    html {
        font-size: 29px;
    }
}
@media (min-width: 1470px) and (max-width: 1518px) {
    html {
        font-size: 30px;
    }
}
@media (min-width: 1519px) and (max-width: 1567px) {
    html {
        font-size: 31px;
    }
}
@media (min-width: 1568px) and (max-width: 1616px) {
    html {
        font-size: 32px;
    }
}
@media (min-width: 1617px) and (max-width: 1665px) {
    html {
        font-size: 33px;
    }
}
@media (min-width: 1666px) and (max-width: 1714px) {
    html {
        font-size: 34px;
    }
}
@media (min-width: 1715px) and (max-width: 1763px) {
    html {
        font-size: 35px;
    }
}
@media (min-width: 1764px) and (max-width: 1812px) {
    html {
        font-size: 36px;
    }
}
@media (min-width: 1813px) and (max-width: 1861px) {
    html {
        font-size: 37px;
    }
}
@media (min-width: 1862px) and (max-width: 1910px) {
    html {
        font-size: 38px;
    }
}
@media (min-width: 1911px) {
    html {
        font-size: 39px;
    }
}
/*/pc媒体查询*/
```