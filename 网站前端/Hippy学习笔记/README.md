# Hippy学习笔记

## 目录
1. [Hippy](#hippy)
1. [hippy-react](#hippy-react)

---
### [Hippy](https://github.com/Tencent/Hippy)
![hippy图](./images/hippy-1.png)

1. 运行demo、调试

    >来自：[前端调试](https://hippyjs.org/#/guide/debug)。

    1. （可选）使用官网的发布版本（Latest release），不要用master分支代码跑demo
    2. 根目录执行`npm run build`
    3. 客户端demo运行

        1. iOS

            直接可以根据文档运行Xcode
        2. Android

            参考：[Hippy/issues/39](https://github.com/Tencent/Hippy/issues/39)。

            1. Android Studio安装SDK

                1. 当提示 ToolChain 需要更新时全部选择拒绝（Gradle等）。
                2. 选择安装制定版本的SDK Tools：

                    1. Android SDK Build-Tools：28.0.3
                    2. CMake：3.6.4111459
            2. 配置自己sdk里面的cmake到环境变量
            3. Android Studio右上角的Project Structure（command + ;） -> SDK Location -> Android NDK location 设置ndk位置
    4. 运行Hippy demo项目

        `npm run hippy:dev`、`npm run hippy:debug`

        1. Android调试（按步骤）：

            1. `adb reverse tcp:38989 tcp:38989`
            2. App点击：本地调试 -> 点击调试
            3. `chrome://inspect/#devices`打开Hippy debug tools for V8
        2. iOS调试（按步骤）：

            1. 打开Safari，勾选：开发 -> 模拟器 xxx -> ️自动显示JSContext的网页检查器
            2. App点击：本地调试 -> 点击调试

                >若Safari没有调试信息，则重启App
2. 前端使用：

    1. 构建工具

        webpack
    2. 网络请求

        1. `fetch`
        2. `WebSocket`
        3. `cookie`（NetworkModule）
    3. 定时器

        `setTimeout`、`clearTimeout`、`setInterval`、`clearInterval`
    4. 日志

        `console.log/warn/error`

        - `console`日志会输出到iOS和Android系统日志中。
    5. 自定义字体

        `fontFamily`

### hippy-react
![hippy-react图](./images/hippy-react-1.png)

1. 组件

    >[组件文档](https://hippyjs.org/#/hippy-react/components)比较简单，更详细的用法在[demo](https://github.com/Tencent/Hippy/tree/master/examples/hippy-react-demo/src/components)或[源码](https://github.com/Tencent/Hippy/tree/master/packages/hippy-react/src/components)中。

    `<Image>`、`<ListView>`、`<Modal>`、`<Navigator>`、`<RefreshWrapper>`、`<ScrollView>`、`<TextInput>`、`<Text>`、`<View>`、`<ViewPager>`

    >组件功能需要完全按照文档描述来使用，不像前端标签那么灵活。如：`<View>`和`<ScrollView>`不能混用，`<ScrollView>`文档只有`contentContainerStyle`而没有 ~~`style`~~。

    - 客户端都是**单屏**视口（可以理解为外层包裹着一个高宽等于视口的flex父级容器），借助某些组件的内部滚动来实现多屏效果。

        >所有滚动都是：组件内部滚动。

        1. `<ScrollView>`

            支持：横向 或 竖向滚动（`horizontal`只能选择其一，不能同时横向、竖向滚动）。

            1. 组件宽度/高度优先等于子组件总共的宽度/高度（就不用滚动）；若显式设置的宽度/高度小于子组件总共的宽度/高度则滚动。
            2. `<ScrollView>`内可嵌套所有组件（包括：`<ScrollView>`、`<ListView>`、`<ViewPager>`）。
        2. `<ListView>`

            支持：竖向滚动。

        3. `<RefreshWrapper>`

            包裹一个`<ListView>`后支持：下滑刷新。
        4. `<ViewPager>`

            支持：横向切换（类似Swiper）。

        - 其他组件都没有组件内部滚动功能（`overflow`只有`hidden/visible`2个属性值）。

    - 注意点

        1. `<Image>`

            1. 若设置`position: 'absolute'`，则需要显示设置`width`和`height`。
        2. `<ScrollView>`

            1. 不要用 ~~`style`~~，用文档要求的`contentContainerStyle`。
        3. `<Text>`

            1. Android:

                1. `ellipsizeMode`仅支持`tail`。
                2. 截断中有特殊字符（如一些标点符号）时，截断会提前，不会在内容结尾处正常截断。
2. 模块

    >[模块文档](https://hippyjs.org/#/hippy-react/modules)比较简单，更详细的用法在[demo](https://github.com/Tencent/Hippy/tree/master/examples/hippy-react-demo/src/modules)或[源码](https://github.com/Tencent/Hippy/tree/master/packages/hippy-react/src/modules)中。

    `Animation`、`AnimationSet`、`AsyncStorage`、`BackAndroid`、`Clipboard`、`Dimensions`、`NetInfo`、`NetworkModule`、`PixelRatio`、`Platform`、`Stylesheet`

    - 引入base64

        >默认情况下，webpack会针对小于某KB的图标进行转base64，所以一般情况不需要显式使用这个。

        `!!url-loader?modules!路径`，如：`import defaultSource from '!!url-loader?modules!./defaultSource.jpg';`

3. 自定义组件、自定义模块

    1. 自定义组件

        `import { UIManagerModule } from "@hippy/react"`
    2. 自定义模块

        `import { callNative, callNativeWithPromise } from "@hippy/react"`
3. 手势系统（点击事件、触屏事件）

    所有组件（或自定义组件）均支持监听手势系统（点击事件、触屏事件）。

    1. 点击事件

        1. `onClick`：点击
        2. `onPressIn`：开始触屏
        3. `onPressOut`：结束触屏
        4. `onLongClick`：长按

        - 回调参数：

            ```javascript
            {
              name: 「事件名」,
              id: 「控件的id」,
              target: 「控件的id」
            }
            ```
    2. 触屏事件

        1. `onTouchDown`：开始触屏
        2. `onTouchMove`：移动手指（持续触发回调）
        3. `onTouchEnd`：结束触屏
        4. `onTouchCancel`：被中断触屏

            若触发`onTouchCancel`则不触发`onTouchEnd`。

        - 回调参数：

            ```javascript
            {
              name: 「事件名」,
              id: 「控件的id」,
              target: 「控件的id」,
              page_x: 「触屏点相对于根元素的横坐标」,
              page_y: 「触屏点相对于根元素的轴坐标」
            }
            ```

    - 事件冒泡

        点击事件、触屏事件均支持事件冒泡，由最上层组件往根元素冒泡触发事件回调。

        1. 若事件回调返回`false`，则冒泡。
        2. 若事件回调返回`true`或不返回值，则不再冒泡。
    - 事件拦截

        父级组件拦截或中断子级组件的事件触发。所有触发在子级组件的事件都仅触发在父级组件。

        1. `onInterceptTouchEvent`：

            1. `true`：

                1. 拦截所有手势事件（点击事件+触屏事件）。
                2. 若父级组件在设置`onInterceptTouchEvent`为`true`之前，子级组件已经在处理触屏事件，则子级组件将收到一次`onTouchCancel`回调（如果子控件有注册该函数）。
            2. `false`（默认）：不拦截
        2. `onInterceptPullUpEvent`（貌似还未实现？）
4. 终端事件

    ```jsx
    import { HippyEventEmitter } from '@hippy/react';
    const hippyEventEmitter = new HippyEventEmitter();

    # 发送rotate事件并监听回调
    this.call = hippyEventEmitter.addListener('rotate', evt => console.log(evt.result));


    # 事件卸载
    this.call.remove();
    ```
5. 样式

    >1. Hippy的还原设计稿方案，与客户端的方案基本一致：[各端还原设计稿方案响应式方案](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/还原设计稿/README.md#各端还原设计稿方案响应式方案)。
    >2. [React Native样式](https://reactnative.dev/docs/style)的子级。
    >3. 注意属性值要求是`Number`还是`String`，要严格遵守，不能互换。

    1. 长度单位

        无单位、数值型（`Number`）。含义是dp或pt。不支持：~~百分比~~、~~任何单位（`px`、`em`、`rem`、`vw`、`vh`）~~。

    >属性名的方向：`left === start`、`right === end`。但貌似未实现 ~~`start`~~ 或 ~~`end`~~。

    2. 盒模型

        >类型CSS的`box-sizing: border-box;`（布局所占宽度 = width = content + padding左右 + border左右。高度同理）。

        1. `width`
        2. `height`
        3. `border`

            1. 宽度（`Number`）

                1. `borderWidth`

                    >仅能设置为相同数值。
                2. `borderTopWidth`
                3. `borderRightWidth`
                4. `borderBottomWidth`
                5. `borderLeftWidth`
            2. 颜色

                属性值为颜色字符串。

                1. `borderColor`
                1. `borderTopColor`
                1. `borderRightColor`
                1. `borderBottomColor`
                1. `borderLeftColor`
            3. `borderStyle`

                1. `'solid'`（默认）
                1. `'dotted'`
                1. `'dashed'`
        4. `padding`（`Number`）

            1. `padding`

                >仅能设置为相同数值。
            2. `paddingVertical`

                >仅能设置为相同数值。
            3. `paddingHorizontal`

                >仅能设置为相同数值。
            4. `paddingTop`
            5. `paddingRight`
            6. `paddingBottom`
            7. `paddingLeft`
        5. `margin`（`Number`）

            1. `margin`

                >仅能设置为相同数值。
            2. `marginVertical`

                >仅能设置为相同数值。
            3. `marginHorizontal`

                >仅能设置为相同数值。
            4. `marginTop`
            5. `marginRight`
            6. `marginBottom`
            7. `marginLeft`
    3. 布局（flex）

        仅支持flex（，所以省略 ~~`display: flex`~~，所有组件全都只能是`flex`）。

        >与CSS的[flex](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/HTML+CSS学习笔记/弹性盒子.md#flex语法)略有不同。

        1. Flex容器

            1. `flexDirection`：决定主轴的方向。

                1. `'row'`：水平方向，起点在左端。
                2. `'column'`（默认）：垂直方向，起点在上沿。
            2. `flexWrap`：一条主轴排不下的情况，如何换行。

                >与CSS的`flex-wrap`表现一致。

                1. `alignContent`：多根主轴（一条主轴排不下，有换行）的对齐方式（不换行则该属性不起作用）。

                    1. `flex-start`（默认）
            3. `justifyContent`：子项在主轴上的对齐方式（与轴的方向有关）。

                >与CSS的`justify-Content`表现一致。
            4. `alignItems`：子项在侧轴上的对齐方式（与轴的方向有关）。

                1. `stretch`（默认）

                >与CSS的`align-Items`表现一致。
        2. Flex子项

            >都在主轴方向上。

            1. `flex`：占用容器中剩余空间的大小。

                1. `0`（默认）：元素没有弹性，不管父级容器空间，仅使用自身原本宽度/高度占据空间。
                2. `「正整数」`：元素有弹性，`每个元素占用的剩余空间 = 自己的 flex 数值 / 所有同一级子容器的 flex 数字之和`。

                    >此时`flex: 「正整数」`等价于`flexGrow: 「正整数」`。

                3. `-1`：若空间不足则缩小到最小的宽度/高度。若空间没有不足，则使用自身原本宽度/高度占据空间。
            2. `flexGrow`：伸缩项目扩展的能力。

                >与CSS的`flex-grow`表现一致。
            3. `flexShrink`：伸缩项目收缩的能力。

                >与CSS的`flex-shrink`表现一致。
            4. `flexBasis`：伸缩基准值。

                >与CSS的`flex-basis`表现一致。
            5. `alignSelf`：单个子项覆盖父元素的`alignItems`。

                >与CSS的`align-self`表现一致。
    4. 颜色

        1. rgb

            e.g. `'#f0f'`、`'#ff00ff'`、`'rgb(255, 0, 255)'`
        2. rgba

            e.g. `'#f0ff'`、`'#ff00ff40'`、`'rgba(255, 0, 255, 0.5)'`
        4. hsl

            e.g. `'hsl(0, 33%, 69%)'`
        5. hsla

            e.g. `'hsla(0, 33%, 69%, 0.5)'`
        6. `'transparent'`
        7. 颜色名字
    5. 字体

        1. `fontSize`
        2. `lineHeight`
        3. `color`
        4. `fontWeight`
    6. `transform: [{ 属性1: 值1 }, {属性2: 值2}]`

        >属性值是`object[]`。
    7. `backfaceVisibility`

        元素背面朝向观察者时是否可见。

        1. `'visible'`（默认）
        2. `'hidden'`
    8. 定位

        1. `position`

            1. `'relative'`（默认）
            2. `'absolute'`
        2. `top`
        3. `right`
        4. `bottom`
        5. `left`
    9. `zIndex`

        1. `0`（默认）

            >（与CSS的[层叠上下文](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/HTML+CSS学习笔记/README.md#层叠上下文stacking-context)略有不同）可以理解为：Hippy中任何一个组件，都形成层叠上下文且默认层叠顺序为`0`。因此层叠顺序仅在兄弟节点就确定了，不是兄弟节点无法改变堆叠顺序。
        2. `「整数」`
    10. `overflow`

        >`overflow`只有2个属性值，没有CSS的 ~~`scroll`~~，除了拥有滚动效果的组件（`<ScrollView>`、`<ListView>`、`<RefreshWrapper>`、`<ViewPager>`）之外，其他组件都不支持组件内滚动。

        子元素超过父容器的宽度/高度后的显示情况。

        1. `'visible'`（默认）
        2. `'hidden'`
    11. 背景

        1. `backgroundImage`

            >url不能缩写。不能用 ~~<https://placeholder.com/>~~？

            e.g. `backgroundImage: "https://图片地址"`
        2. `backgroundPositionX`
        2. `backgroundPositionY`
    12. 外边框圆角（`Number`）

        1. `borderRadius`

            >仅能设置为相同数值。
        1. `borderTopLeftRadius`
        1. `borderTopRightRadius`
        1. `borderBottomRightRadius`
        1. `borderBottomLeftRadius`
    13. `opacity`

    - 样式写法

        1. 内联样式

            e.g. `<View style={{ width: 100, height: 100, backgroundColor: 'red' }}/>`。
        2. 外部样式

            <details>
            <summary>e.g.</summary>

            ```jsx
            // 定义样式
            import { StyleSheet } from '@hippy/react'
            const styles = StyleSheet.create({
              itemStyle: {
                width: 100,
                height: 100,
                lineHeight: 100,
                borderWidth: 1,
                borderColor: '#4c9afa',
                fontSize: 80,
                margin: 20,
                color: '#4c9afa',
                textAlign: 'center'
              },
              verticalScrollView: {
                height: 300,
                width: 140,
                margin: 20,
                borderColor: '#eee',
                borderWidth: 1
              },
            });


            // 使用
            <Text style={styles.itemStyle}/>
            <Text style={styles.verticalScrollView}/>
            ```
            </details>
