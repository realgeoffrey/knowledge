### 前端自动化测试

以“输入工单号、勾选只看待处理、点击查询”为例。先想这次改动可能把哪一步弄坏，再选能看见这个错误的测试层级。

| 想验证什么 | 在哪一层测 | 断言什么 |
| --- | --- | --- |
| 工单号会去掉首尾空格 | 单元测试，直接调用构建查询参数的函数 | 输入 `' A-42 '` 得到 `'A-42'`，空白输入按接口约定处理。 |
| 勾选后页面能否正确提交并展示结果 | 组件测试，渲染查询表单，用可控的响应代替服务端 | 通过“只看待处理”和“查询”操作控件。断言请求带上 `status=pending`，返回的工单出现在列表；再覆盖一次空结果或失败提示。 |
| 页面和真实接口对参数、身份及数据的理解是否一致 | 端到端测试（E2E），浏览器连接测试环境 | 为测试账号准备一张待处理工单和一张已完成工单，按状态查询后只看到待处理的那张。 |

单元测试可以用 [Jest](https://github.com/jestjs/jest) 或 [Mocha](https://github.com/mochajs/mocha)。组件测试可以用 [React Testing Library](https://github.com/testing-library/react-testing-library)、[Vue Test Utils](https://github.com/vuejs/test-utils) 或 [Storybook 交互测试](https://storybook.js.org/docs/writing-tests/interaction-testing)。按角色、名称或标签找控件，异步结果等到它实际出现再断言；一并检查 [表单的键盘和读屏操作](../无障碍/README.md)。[Testing Library 查询说明](https://testing-library.com/docs/queries/about/)

[Cypress](https://github.com/cypress-io/cypress) 和 [Puppeteer](https://pptr.dev/) 都能驱动浏览器。若查询接口被拦截并返回固定数据，这个用例能验证浏览器里的交互和渲染；前后端联调还要实际经过接口。截图适合发现布局变化，查询结果要核对工单号和状态。

#### 看覆盖率时查什么

[nyc](https://github.com/istanbuljs/nyc) 可统计实际执行到的语句（Statements）、分支（Branches）、函数（Functions）和行（Lines）。早期工具见 ~~[istanbul](https://github.com/gotwarlost/istanbul)~~。即使查询函数的每一行都执行过，也值得查一眼“未勾选时省略状态参数”这条分支有没有断言。更多例子见[单元测试与测试规范要点](../../../全栈/单元测试与测试规范要点/README.md)。
