### 无障碍

#### 键盘和读屏检查

原生控件自带键盘行为，给每个输入配一个可见标签。点标签文字也能聚焦输入框或勾选复选框。[W3C 表单标签示例](https://www.w3.org/WAI/tutorials/forms/labels/)

1. **只用键盘。** 用 Tab 和 Shift+Tab 检查焦点顺序和焦点样式，再验证控件能通过键盘操作。
2. **打开读屏。** 核对控件的可访问名称、角色和状态。若只听到“按钮”或“编辑框”，先查控件是否有可访问名称。
3. **检查整个页面。** 从页面标题开始检查层级。只含图标的按钮也要能听出用途。图片承载信息时提供等价替代文本，纯装饰的 `<img>` 用空的 `alt=""`。在弹窗、校验失败和结果更新后再走一遍关键操作。[W3C 快速检查](https://www.w3.org/WAI/test-evaluate/easy-checks/)

#### 读屏工具

| 平台 | 工具 |
| --- | --- |
| Android / iOS | TalkBack / VoiceOver（旁白）。手机可设置辅助功能快捷键，方便开发时切换。 |
| Windows | NVDA、JAWS |
| macOS / ChromeOS | VoiceOver（旁白）/ ChromeVox |

Web 开发可查 [MDN 无障碍](https://developer.mozilla.org/zh-CN/docs/Web/Accessibility)、[Vue 无障碍指南](https://cn.vuejs.org/guide/best-practices/accessibility.html)及 [React 输入框与标签](https://react.dev/reference/react-dom/components/input#providing-a-label-for-an-input)。跨端控件见 [React Native 无障碍](https://reactnative.dev/docs/accessibility)和本仓库的 [Hippy React 实践](../../Hippy学习笔记/README.md#hippy-react-无障碍)。
