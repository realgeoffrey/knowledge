cssReset.css

```css
/* CSS reset */
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
ol,ul {list-style:none;}
hr {display:block;height:1px;border:0;border-top:1px solid #ccc;margin:1em 0;padding:0;}
abbr,acronym {border:0;font-variant:normal;}
del {text-decoration:line-through;}
address,caption,cite,code,dfn,th,var,em,i,b,time {font-style:normal;font-weight:500;}
caption,th {text-align:left;}
blockquote,q {quotes:none;}
blockquote:before,blockquote:after,q:before,q:after {content:'';content:none;}
sub,sup {font-size:75%;line-height:0;position:relative;vertical-align:baseline;}
sup {top:-0.5em;}
sub {bottom:-0.25em;}
article,aside,details,figcaption,figure,footer,header,hgroup,menu,nav,section,summary,iframe,main {display:block;}
img {vertical-align:middle;}

html {-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;-webkit-overflow-scrolling:touch;}
img {max-width:100%;}
a,button,input,textarea {-webkit-tap-highlight-color:rgba(63,40,1,.3);}
/*/CSS reset */
/* 全局*/
html, body {
    /*height: 100%;*/
}
body {
    background-color: #fff;
    color: #333;
    min-width: ;
    position: relative;
}
a {
    color: #333;
}
a:hover {

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
    display: block;
    clear: both;
    content: ".";
    visibility: hidden;
    height: 0;
}
.clearfix {
    zoom: 1;
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
/* 手机媒体查询*/
@media (max-width: 374px) {
    html {
        font-size: 10px;
    }
}
@media (min-width: 375px) and (max-width: 639px) {
    html {
        font-size: 15px;
    }
}
@media (min-width: 640px) and (max-width: 736px){
    html {
        font-size: 20px;
    }
}
@media (min-width: 737px) {
    html {
        font-size: 25px;
    }
}
@media (orientation: landscape) {

}
/*/手机媒体查询*/
/* 多大图模式*/
.header {
    background: url() #fff center 0 no-repeat;
    min-width: ;
    height: ;
    overflow: hidden;
}
.main {
    background: url() #fff center 0 no-repeat;
    min-width: ;
    overflow: hidden;
}
.footer {
    background: url() 0 0 repeat-x;
    min-width: ;
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
/* 单大图模式*/
.full_bg {
    background: url() #fff center 0 no-repeat;
    min-width: ;
    overflow: hidden;
}
.header,
.main {
    background: url() center 0 no-repeat;
    width: ;
    margin: 0 auto;
    position: relative;
}
.footer {
    background-color: #fff;
    min-width: ;
}
.footer .wrap {
    width: ;
    margin: 0 auto;
}
/*/单大图模式*/

/* 头像-png24兼容ie6*/
.avatar {
    width: ;
    height: ;
    position: relative;
    cursor: pointer;
}
.avatar img {
    background: url() 0 0 no-repeat; /* 默认图*/
    width: ;
    height: ;
    display: block;
}
.avatar span.hover,
.avatar span.normal {
    width: ;
    height: ;
    position: absolute;
    top: 0;
    left: 0;
}
.avatar span.hover {
    background: url() 0 0 no-repeat;
}
.avatar span.normal {
    background: url() 0 0 no-repeat;
}
/*/头像-png24兼容ie6*/
```