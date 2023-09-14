# 微信生态相关

## 目录
1. [概念](#概念)
1. [微信调试开发](#微信调试开发)

    1. [`WeixinJSBridge`](#weixinjsbridge)
    1. [微信外部链接](#微信外部链接)
    1. [微信内访问第三方页面的网页授权](#微信内访问第三方页面的网页授权)
1. [小程序相关](#小程序相关)

    1. [taro](#taro)

---

### 概念
1. 微信[开放平台](https://open.weixin.qq.com/)：

    `（微信内外的）h5、app等`与`微信app`进行第三方功能（登录、支付、分享、[打开其他APP](https://developers.weixin.qq.com/doc/oplatform/Mobile_App/WeChat_H5_Launch_APP.html)、等）。

>1. 开放平台是基础，APP、小程序、web、公众号 可以选择绑定到开放平台，由开放平台统一管理（如：开放平台提供统一的UnionID判断用户，达到多平台用户信息统一的作用）。
>2. 微信公众平台 处理 微信APP内部交互，微信开放平台 处理 外部应用与微信APP的交互。

2. 微信[公众平台](https://mp.weixin.qq.com/)：

    公众号（服务号、订阅号）、小程序、小游戏、企业微信。

    1. 微信[JSSDK](https://developers.weixin.qq.com/doc/offiaccount/OA_Web_Apps/JS-SDK.html)：

        微信内部的H5与微信app功能（原生硬件能力、微信app功能）的交互功能。
    2. 小程序、小游戏：

        怎么开发这些功能。
3. 多端（如：uni-app）：

    按照小程序为基础，扁平化开发，可能用到 开放平台、JSSDK 等功能。

- 字段概念

    >来自：[小程序登录](https://developers.weixin.qq.com/minigame/dev/guide/open-ability/login.html)。

    1. AppID

        公众号或小程序或微信开放平台等的标记账户的唯一id

        >微信开放平台的AppID无法用在微信公众号登录，只能作为客户端第三方登录使用。

        - AppSecret

            小程序密钥（账号设置生成后保存）
    2. OpenID

        用户唯一标识，一个用户id（uid）针对某个AppID生成的唯一且不变化的id
    3. session_key（或openkey、access_token）

        会话密钥，每次登录会变化且一定时间会过期无效。与OpenID一起确定某个用户id的登录态

        >后台获得并保存。涉及签名校验以及数据加解密，因此不要把它发还给前端。

        >e.g. 前端调用接口返回`rawData`和`signature`（`signature = sha1( rawData + session_key )`），只有后台有session_key，因此后台收到前端发来的2个值能校验真伪。
    4. UnionID

        （需要应用先绑定到微信开放平台帐号才存在，）一个用户id（uid）针对微信开放平台帐号生成的唯一且不变化的id

        >同一用户，对同一个微信开放平台下的不同应用（用微信开放平台登录的app、h5，用微信开放平台绑定的公众帐号、小程序、小游戏），UnionID是相同的。

---
## 微信调试开发
1. 检查域名是否在接口调用权限安全域名内。

    1. 某个域名，能请求通就是有权限，不能请求通（根据错误码信息）就是没有权限。
    2. 基本权限，公众号申请appid之后就可以获得。高级权限，仅有内部app才可以申请获得。

    如：`WeixinJSBridge`。

    >一般不会有外部接口查询哪些域名支持哪些接口。
2. 在微信内调用需要引入对应的sdk文件。
3. 重要的流程，调用`wx.config`的方法进行相关的权限配置。
4. 清理微信WebView的缓存或cookie等，貌似现在最佳的方案只能是退出-重新登录微信账号。

    >现代版本Android微信也不是~~x5~~内核，而转用系统内置WebView内核。
5. 微信支付等提示`签名参数构造错`，尝试关闭代理后再试。
6. 若自定义CA证书有问题，则微信里可能就会拦截从而不发起请求（在其他APP可能只是提示证书有问题）。

    可能是操作系统问题或APP本身问题，尝试升级至最新版本。
7. 直接打开在聊天界面的URL，会有诸多限制，如：无法拉起APP、分享的URL不是卡片而是纯文本 等。

    打开 分享的卡片、二维码扫描 的网址，才有更多页面权限。

### `WeixinJSBridge`
>`WeixinJSBridge`是底层的接口，建议使用官方封装的[JSSDK](https://developers.weixin.qq.com/doc/offiaccount/OA_Web_Apps/JS-SDK.html)。

1. `WeixinJSBridge.invoke("API名称", 参数对象, 回调函数)`
2. `WeixinJSBridge.on("事件名称", 回调函数)`

### 微信外部链接
遵守[《微信外部链接内容管理规范》](https://weixin.qq.com/cgi-bin/readtemplate?t=weixin_external_links_content_management_specification)，避免被封禁。

### 微信内访问第三方页面的网页授权
授权流程根据[《微信网页开发/网页授权》](https://developers.weixin.qq.com/doc/offiaccount/OA_Web_Apps/Wechat_webpage_authorization.html)进行。

>针对`A域名`发起微信登录授权到`B域名`，h5跳转登录授权页会弹出提示（iOS）——h5跳转`open.weixin.qq.com`前 iOS会拦截进行弹窗，可以用Node.js跳转登录授权页来去除弹出提示（iOS）。

---
## 小程序相关
1. 注意模拟器和真机有区别，部分限制和设置效果在模拟器不起作用。

    开发者工具仅供调试使用，最终的表现以客户端为准。

### [taro](https://github.com/NervJS/taro)
1. 组件库

    1. `<Button>`的`hoverClass`要在没有`className`时才起作用（`<View>`的不受此限制）。
    2. `<Swiper>`动态改变配置会导致渲染错误（属性、内部滑块？），因此配置只能用固定不变的值。
2. 其他

    1. 有些样式写在`.scss`里会被框架删除，需要添加到`.tsx`模板上。

        e.g. `-webkit-box-orient: vertical;`
