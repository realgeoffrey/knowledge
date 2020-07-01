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

            1. Android Studio：当提示 ToolChain 需要更新时全部选择拒绝；安装设置里SDK Tools：SDK、NDK、cmake 3.6.4（Show Package Details 可以选择cmake的版本等）。
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

    组件功能需要完全按照文档描述来使用，不像前端标签那么灵活。如：`<View>`和`<ScrollView>`不能混用。
2. 模块

    [模块文档](https://hippyjs.org/#/hippy-react/modules)

- 引入base64

    `!!url-loader?modules!路径`，如：`import defaultSource from '!!url-loader?modules!./defaultSource.jpg';`

3. 样式

    1. 盒模型

        >类型CSS的`box-sizing: border-box;`。

        `width`、`height`、`padding`、`border`、`margin`、`background`
    2. 长度单位

        无单位、数值型（Number）。含义是dp。
    3. 布局（flex）

        仅支持flex（，所以省略 ~~`display: flex`~~）。

        >与CSS3的[flex](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/HTML+CSS学习笔记/弹性盒子.md#flex语法)略有不同。

        todo 试验

        1. Flex容器

            1. `flexDirection`：决定主轴的方向。

                1. `row`：水平方向，起点在左端。
                2. `column`（默认）：垂直方向，起点在上沿。
            2. `alignItems`：子项在侧轴上的对齐方式（与轴的方向有关）。

                1. `stretch`：若子项未设置高度或设为`auto`，则将占满整个容器的高度。
                2. `flex-start`（默认）：起点对齐。
                3. `flex-end`：终点对齐。
                4. `center`：居中。
                5. `baseline`：子项的第一行文字的基线对齐。
            3. `justifyContent`：子项在主轴上的对齐方式（与轴的方向有关）。

                >与CSS3的`justify-Content`一致。
        2. Flex子项

            1. `flex`：占用容器中剩余空间的大小。

                1. `0`（默认）：不占用剩余空间。
                2. `「正整数」`：`每个元素占用的剩余空间 = 自己的 flex 数值 / 所有同一级子容器的 flex 数字之和`
                3. `-1`：默认情况会显示正常宽高。然而，若剩余空间不足的话，此设置了flex: -1的容器将会收缩到其 minWidth 的宽度与 minHeight 的高度来显示。
            2. `flexBasis`：伸缩基准值。

                1. `auto`（默认）
                2. `0`
                3. `「正整数」`
            3. `flexGrow`：伸缩项目扩展的能力。

                1. `0`（默认）
                2. `「正整数」`
            4. `flexShrink`：伸缩项目收缩的能力。

                1. `1`（默认）
                2. `「正整数」`
    4. 写法

        1. 内联样式

            e.g. `<View style={{ width: 100, height: 100, backgroundColor: 'red' }}/>`。
        2. 外部样式

            ```react
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
4. 手势系统

    所有组件（或自定义组件）均支持监听：点击事件、触屏事件。

    1. 点击事件

        1. `onClick`：点击
        2. `onPressIn`：类似`touchstart`
        3. `onPressOut`：类似`touchend`
        4. `onLongClick`：长按

        - 回调参数`{ name: 「事件名」 }`
    2. 触屏事件

        todo continue
5. 终端事件

    ```react
    import { HippyEventEmitter } from '@hippy/react';
    const hippyEventEmitter = new HippyEventEmitter();

    # 发送rotate事件并监听回调
    this.call = hippyEventEmitter.addListener('rotate', evt => console.log(evt.result));


    # 事件卸载
    this.call.remove();
    ```


