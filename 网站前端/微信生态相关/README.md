# 微信生态相关

## 目录
1. [概念](#概念)
1. [小程序相关](#小程序相关)

    1. [taro](#taro)

---
### 概念
1. 微信[开放平台](https://developers.weixin.qq.com/doc/oplatform/Mobile_App/Resource_Center_Homepage.html)：

    （微信内外的）h5与微信app进行第三方功能（登录、支付、等）。
2. 微信[JSSDK](https://developers.weixin.qq.com/doc/offiaccount/OA_Web_Apps/JS-SDK.html)：

    微信内部的H5与微信app功能（原生硬件能力、微信app功能）的交互功能。
3. 小程序、小游戏：

    怎么开发这些功能。
4. 多端（如：uni-app）：

    按照小程序为基础，扁平化开发，可能用到 开放平台、JSSDK 等功能。

---
## 小程序相关

### [taro](https://github.com/NervJS/taro)
1. 组件库

    1. `<Button>`的`hoverClass`要在没有`className`时才起作用（`<View>`的不受此限制）。
    2. `<Swiper>`动态改变配置会导致渲染错误（属性、内部滑块？），因此配置只能用固定不变的值。
2. 其他

    1. 有些样式写在`.scss`里会被框架删除，需要添加到`.tsx`模板上。

        e.g. `-webkit-box-orient: vertical;`
