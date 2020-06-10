# 代码调试相关

## 目录
1. [前端调试方式](#前端调试方式)
1. [服务端调试](#服务端调试)

---

### 前端调试方式
1. JS：

    1. 展示：`console.log/info/warn/error`（`alert`）

        >（Value below was evaluated just now.）`console`引用类型的数据，在点击开来查看的这个时刻才去取引用类型的快照（意味着可以console之后再修改展示内容），打开之后不再关联。

        - 更好的展示：

            1. 缩进：`console.groupCollapsed/group`至`console.groupEnd`
            2. 表格：`console.table`
    2. 调用栈：`console.trace`
    3. 执行时间：`console.time`至`console.timeEnd`
2. PC端

    DevTools

    1. Sources断点（`debugger`、配合SourceMap，通过Call Stack查看调用栈）。
    2. Elements，右键标签可以Break On：子节点修改、attribute修改、Node移除。
    3. 通过Chrome的 <chrome://inspect/#devices>，监听Node.js程序运行`node --inspect 文件`，可使用`debugger`等进行断点调试、`console`打印等。
3. WAP端（真机）

    1. 使用页面模拟调试，如：[eruda](https://github.com/liriliri/eruda)、[vConsole](https://github.com/Tencent/vConsole)。
    2. 针对**已开启调试功能的APP**连接对应的调试工具：

        >最佳方式：连接上电脑后借助DevTools。

        1. Android

            PC端的Chrome的Remote devices（<chrome://inspect/#devices>）可以调试**Android已开启调试功能的APP**的WebView（需要能够访问google，否则首次打开inspect页面会404）。

            - Android已开启调试功能的APP：

                1. Chrome
                2. 用<http://debugx5.qq.com/>打开TBS内核调试功能的[腾讯X5内核WebView](https://x5.tencent.com/)（如：Android的微信、QQ）
                3. 开启调试功能的debug包APP

            >若PC端的Chrome识别不到手机WebView，可以下载[Android Debug Bridge (adb)](https://developer.android.google.cn/studio/releases/platform-tools.html?hl=zh-cn#downloads)并运行（进入文件夹后运行`adb.exe devices`或`./adb devices`连接手机设备）。
        2. iOS

            macOS的Safari的「开发」可以调试**iOS已开启调试功能的APP**的WebView。

            - iOS已开启调试功能的APP：

                1. Safari
                2. 开启调试功能的debug包APP
    3. Android真机调试

        1. 打开「开发者选项」的「显示布局边界」，会展示Native渲染边界，方便区分WebView的H5与Native内容。
        2. 打开其他APP时设置的允许/拒绝信息，可以操作当前APP「清除数据」恢复提醒。
    4. 使用抓包工具查看请求、Map请求，如：[Charles](https://github.com/realgeoffrey/knowledge/blob/master/工具使用/Charles使用/README.md#charles使用)、[whistle](https://github.com/realgeoffrey/knowledge/blob/master/工具使用/whistle使用/README.md#whistle使用)。

- 其他策略

    1. 对于App内不方便查看的信息，可以把需要查看的信息发送HTTP请求、再抓包的方式进行调试。
    2. 上线的页面中藏着某些「后门」调试（如：隐蔽操作开启`console`）

        1. 可以在URL中判断某些特定的`search`值，以开启调试模式。

            >e.g. `xxx?debug=1`开启
        2. WAP端可以用一些隐蔽的手势触发log信息展示。

            ><details>
            ><summary>e.g.</summary>
            >
            >```javascript
            >let consolelogId = 0
            >
            >function wapConsole () {
            >  if (event.touches.length >= 4) {    // 4个触发点以上
            >    consolelogId += 1
            >
            >    if (consolelogId >= 2) {    // 2次以上触发
            >      // 展示隐藏的调试信息
            >      const newScript = document.createElement('script')
            >      const appendPlace = document.getElementsByTagName('body')[0] || document.getElementsByTagName('head')[0]
            >
            >      newScript.onload = function () { // 只能保证加载完成，但不能判断是否执行
            >        eruda.init()   // new VConsole()
            >        newScript.onload = null
            >      }
            >
            >      // onerror表示加载失败
            >
            >      newScript.src = '//unpkg.com/eruda'    // '//unpkg.com/vconsole'
            >
            >      appendPlace.appendChild(newScript)
            >
            >      document.removeEventListener('touchstart', wapConsole, false)
            >    }
            >  }
            >}
            >
            >document.addEventListener('touchstart', wapConsole, false)
            >```
            ></details>

### [服务端调试](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/服务端相关/README.md#接口错误排查)
