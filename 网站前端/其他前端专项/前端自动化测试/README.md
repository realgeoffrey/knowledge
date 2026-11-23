### 前端自动化测试

单元测试验证独立逻辑，组件测试验证界面交互和状态，端到端测试（E2E）验证浏览器内的完整流程及真实接口集成。根据改动可能引起的故障选择测试层级。

单元测试可以用 [Jest](https://github.com/jestjs/jest) 或 [Mocha](https://github.com/mochajs/mocha)。组件测试可以用 [React Testing Library](https://github.com/testing-library/react-testing-library)、[Vue Test Utils](https://github.com/vuejs/test-utils) 或 [Storybook 交互测试](https://storybook.js.org/docs/writing-tests/interaction-testing)。按角色、名称或标签找控件，异步结果等到它实际出现再断言；一并检查 [表单的键盘和读屏操作](../无障碍/README.md)。[Testing Library 查询说明](https://testing-library.com/docs/queries/about/)

[Cypress](https://github.com/cypress-io/cypress) 和 [Puppeteer](https://pptr.dev/) 都能驱动浏览器。拦截请求并返回固定数据可验证交互和渲染。验证接口集成时，让浏览器连接测试环境中的真实接口。

#### 看覆盖率时查什么

[nyc](https://github.com/istanbuljs/nyc) 可统计实际执行到的语句（Statements）、分支（Branches）、函数（Functions）和行（Lines）。早期工具见 ~~[istanbul](https://github.com/gotwarlost/istanbul)~~。查看覆盖率时，也要确认关键分支有相应断言。更多例子见[单元测试与测试规范要点](../../../全栈/单元测试与测试规范要点/README.md)。
