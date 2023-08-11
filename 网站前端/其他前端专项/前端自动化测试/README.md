### 前端自动化测试
>1. 前端页面是一种特殊的GUI软件，很可能需要`基于图形用户交互界面测试`多于`接口测试`。
>2. 接口测试用下面的方法论比较容易实现，但GUI测试比较复杂，目前大部分公司还是通过人工测试（较少自动化测试）。
>3. 因为自动化测试时间人力成本大、又业务需要快速迭代频繁变动，前端业务在自动化测试方面可能较少投入，尤其是UI测试基本都有专人进行人工测试（组件或库进行自动化测试居多）。

1. 单元测试（unit testing）

    通过模拟输入和预测输出的方式测试独立的函数或类。

    >前端库：[jest](https://github.com/facebook/jest)、[mocha](https://github.com/mochajs/mocha)
2. 组件测试库

    >前端库：[testing-library](https://github.com/testing-library)、[storybook](https://github.com/storybookjs/storybook)、[vue-test-utils](https://github.com/vuejs/vue-test-utils)
3. 端到端（E2E、end to end）测试

    功能测试，站在用户视角，使用各种功能、各种交互，是用户的真实使用场景的仿真。

    >集成测试（Integration Test）的一种：在单元测试的基础上，将所有模块按照设计要求组装成为子系统或系统，进行集成测试。
4. 代码覆盖率（code coverage）测试

    通过计算测试过程中被执行的源代码占全部源代码的比例，进而间接度量软件质量的方法。

    >前端库：[nyc](https://github.com/istanbuljs/nyc)、~~[istanbul](https://github.com/gotwarlost/istanbul)~~

    1. Statements：语句覆盖率，所有语句的执行率
    2. Branches：分支覆盖率，所有代码分支（如：if、三目运算）的执行率
    3. Functions：函数覆盖率，所有函数的被调用率
    4. Lines：行覆盖率，所有有效代码行的执行率，和语句类似，但是计算方式略有差别

- UI测试

    大部分手工测试。
