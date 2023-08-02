# 海外应用总结

## 目录
1. [语言问题](#语言问题)
1. [书写顺序](#书写顺序)
1. [翻译系统](#翻译系统)

---
### 语言问题
1. 文字长短不一
2. 文字高度不一（颜文字兼容）
3. 书写顺序，`ltr`、`rtl`
4. 时间问题，时间展示，时区

### 书写顺序
>阿拉伯语等从右至左的语言文字。

1. HTML全局设置整个DOM

    `<html dir="ltr或rtl">`
2. CSS设置左右翻转（镜像）

    1. `transform: scaleX(-1)`
    2. `text-align: right`

    - 镜像方案

        ```html
        // 利用 transform 实现全局镜像
        <View style={{ transform: [{ scaleX: -1 }] }}>
          // 文字向右对齐，重置镜像
          <Text
            style={{
              transform: [{ scaleX: -1 }],
              textAlign: 'right',
            }}>
            على الرغم من أن لديه بعض الصعوبات على سبيل المثال ، بعض الرجل يمكن أن مجرد فتح devtools وإزالة أو تغيير قسم 'لانغ'. لمنع هذا ، أوصي بوضعه في المتغير.
          </Text>
        </View>
        ```

        1. 当镜像一个 UI 时，这些元素会发生改变：

            1. **文本框图标**显示在字段的另一侧
            2. **导航按钮**以相反的顺序显示
            3. 表示方向的**图标**会被镜像，如：箭头
            4. **文本**（如果它被翻译为 RTL 语言）右对齐
        2. 这些元素不会被镜像：

            1. 不表示方向的图标，如：相机
            2. 数字，如：时钟、电话号码
            3. 图标和图解
            4. 非RTL文本的段落

        >具体参考：[苹果指南](https://developer.apple.com/cn/design/human-interface-guidelines/right-to-left)、[Material Design 指南](https://www.mdui.org/design/usability/bidirectionality.html)、[微软指南](https://learn.microsoft.com/zh-cn/windows/apps/design/globalizing/design-for-bidi-text)。
3. 注意动画、绝对定位的数值是否考虑取负值

### 翻译系统
