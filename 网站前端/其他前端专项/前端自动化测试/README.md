### 前端自动化测试
>1. 前端页面是一种特殊的GUI软件，很可能需要`基于图形用户交互界面测试`多于`接口测试`。
>2. GUI 测试需要处理渲染和用户交互。关键用户流程适合做端到端回归，业务规则的边界值通常可以在单元测试中覆盖。

1. 单元测试（unit testing）

    通过模拟输入和预测输出的方式测试独立的函数或类。

    >前端库：[jest](https://github.com/facebook/jest)、[mocha](https://github.com/mochajs/mocha)
2. 端到端（E2E、end to end）测试（UI测试）

    功能测试，站在用户视角，使用各种功能、各种交互，是用户的真实使用场景的仿真。

    1. 编写脚本，浏览器运行。

        >[cypress](https://github.com/cypress-io/cypress)
    2. 用脚本控制真实浏览器，模拟点击、输入并断言结果；截图可辅助检查视觉效果。

        >[Puppeteer](https://pptr.dev/) 默认以无头模式运行浏览器。

    >集成测试可以只验证几个模块能否配合；端到端测试覆盖从用户入口到可见结果的整条流程。
3. 代码覆盖率（code coverage）测试

    统计测试实际执行了哪些代码，帮助发现未覆盖的分支。覆盖率本身无法说明断言是否验证了正确结果。

    >前端库：[nyc](https://github.com/istanbuljs/nyc)、~~[istanbul](https://github.com/gotwarlost/istanbul)~~

    1. Statements：语句覆盖率，所有语句的执行率
    2. Branches：分支覆盖率，所有代码分支（如：if、三目运算）的执行率
    3. Functions：函数覆盖率，所有函数的被调用率
    4. Lines：行覆盖率，所有有效代码行的执行率，和语句类似，但是计算方式略有差别
4. 组件测试库

    >前端库：[react-testing-library](https://github.com/testing-library/react-testing-library)、[vue-test-utils](https://github.com/vuejs/vue-test-utils)、[storybook](https://github.com/storybookjs/storybook)
