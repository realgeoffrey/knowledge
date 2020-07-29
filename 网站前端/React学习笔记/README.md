# React学习笔记

## 目录
1. [react](#react)

    1. [JSX](#jsx)
    1. [元素渲染](#元素渲染)
    1. [组件](#组件)
    1. [代码分割（动态加载）](#代码分割动态加载)
1. [create-react-app](#create-react-app)
1. [redux](#redux)
1. [mobx](#mobx)
1. [react-native](#react-native)

---
### [react](https://github.com/facebook/react)

#### JSX

1. 需要`import React from "react";`才可以使用JSX语法。
2. JSX是一个表达式
3. 若多行，则包裹`(` `)`
4. `{JS表达式}`

    1. `&&`
    2. `condition ? true : false`
    3. `Array`方法
5. 采用小驼峰式（camelCase）定义标签的属性名称，包括：事件名。

    >类似DOM对象的`properties`名。

    1. （`class`是保留字，）`className`代替`class`
    2. `htmlFor`代替`for`

    - 特殊情况用`-`短横线隔开式（kebab-case）的属性名：

        1. 无障碍属性`aria-*`
6. 组件名称必须以大写字母开头。
7. 插入的值都会进行HTML的字符实体（character entity）转义，避免XSS。
8. Babel会把JSX转译成`React.createElement`函数调用，生成React元素

    ><details>
    ><summary>e.g.</summary>
    >
    >```jsx
    >const element = (
    >  <h1 className="greeting">
    >    Hello, world!
    >  </h1>
    >);
    >
    >// 等价于：
    >
    >const element = React.createElement(
    >  'h1',
    >  {className: 'greeting'},
    >  'Hello, world!'
    >);
    >
    >
    >// => 创建React元素
    >const element = {   // 简化后的结构
    >  type: 'h1',
    >  props: {
    >    className: 'greeting',
    >    children: 'Hello, world!'
    >  }
    >};
    >```
    ></details>

- 为`非构建工具（未使用JSX预处理器）`处理的`<script>`，添加JSX支持：

    1. 添加`<script src="https://unpkg.com/babel-standalone@6/babel.min.js"></script>`；
    2. 在使用JSX的.js文件引用加上`type="text/babel"`。

#### 元素渲染
>由`ReactDOM.render`对根DOM组件开始初始化-渲染，随着引入的子组件再以树状结构对子组件进行初始化-渲染。

1. `ReactDOM.render`

    渲染到根DOM。
2. React DOM

    1. 管理根DOM内所有内容。
    2. 将React元素和它的子元素与它们之前的状态进行比较，并只会进行必要的更新来使DOM达到预期的状态。
3. React元素（React elements）

    1. 不可变对象（[immutable](https://zh.wikipedia.org/wiki/不可变对象)）
    2. 创建开销极小的普通对象
4. 组件渲染

    组件渲染完成后返回React元素。

    1. `render`方法（或函数组件）返回`null`，组件会正常运行和执行生命周期函数，只是不渲染出任何DOM（因为渲染空内容）。

#### 组件
组件：它接受任意的入参（Props），并返回用于描述页面展示内容的React元素。

1. 组件类型：

    1. class组件（class components）

        ><details>
        ><summary>e.g.</summary>
        >
        >```jsx
        >class 组件名 extends React.Component {
        >  render() {
        >    return (
        >      <div className="m-div" onClick={this.props.onClick}>
        >        {this.props.value}
        >      </div>
        >    );
        >  }
        >}
        >```
        ></details>
    2. 函数组件（function components）

        不能包含 ~~State~~。

        ><details>
        ><summary>e.g.</summary>
        >
        >```jsx
        >function 组件名 (props) {
        >  // 没有this
        >
        >  function handleClick (e) {
        >    console.log(e, e.preventDefault);
        >  }
        >
        >  return (
        >    <div
        >      onClick={props.onClick}
        >      onClick={(e) => {props.onClick(e);}} // 匿名函数
        >      onClick={handleClick}
        >      onClick={(e) => {handleClick(e);}}   // 匿名函数
        >    >
        >      {props.value}
        >    </div>
        >  );
        >}
        >```
        ></details>
2. 限制

    1. Props不能被修改（只读）。
    2. 组件只能显性接受传入的Props内容（在外层传`style`、`className`等，需要在组件内接受并处理）。
    3. 组件需要以`default`方式导出。
3. State

    State是私有的，并且完全受控于当前组件，其父、子组件均不可见。

    1. 不要~~直接修改State~~，仅用`this.setState`修改
    2. State的更新是异步的（`setState`是异步的）

        `this.props`和`this.state`可能会异步更新。

        ><details>
        ><summary>e.g.</summary>
        >
        >```jsx
        >// Wrong
        >this.setState({
        >  counter: this.state.counter + this.props.increment,
        >});
        >
        >
        >// Correct
        >this.setState((state, props) => ({  // 第一个参数是上一个State，第二个参数是此函数运行时的Props
        >  counter: state.counter + props.increment
        >}));
        >```
        ></details>
    3. 属性值改变的策略

        1. 要在模板内展示的属性，需要放到State中被观测（或放到store中被观测，如：redux、mobx），才能在这些值改变时通知视图重新渲染（`this.setState`）。

            `this.setState(对象或函数, () => {/* 更新后的回调 */})`函数是唯一能够更新`this.state.属性`的方式。

            - 不可变性（引用数据类型）

                不直接修改数据（或改变底层数据），而是用新值替换旧值。（对需要修改的State内容浅复制一层，对新值进行修改后覆盖原State）
        2. 不在模板内展示的值（如：仅作为事件触发修改的状态值 或 仅在JS逻辑中改变的值），直接放在class中的实例属性中。

            - 可以向组件中加入任意不参与数据流的额外字段，但是要在组件生命周期结束前清理（如：在`componentWillUnmount`中处理）。

        ><details>
        ><summary>e.g.</summary>
        >
        >```jsx
        >class MyComponent extends Component {
        >  constructor (props) {
        >    super(props)
        >    this.state = {
        >      current: 0    // 需要放到模板内展示
        >    }
        >  }
        >
        >  componentDidMount () {
        >    this.timerID = setInterval(
        >      () => {},
        >      1000
        >    );
        >  }
        >
        >  componentWillUnmount () {
        >    clearInterval(this.timerID);
        >  }
        >
        >  isLoading = false // 不需要在模板内展示
        >
        >  render () {
        >    return (
        >      <View
        >        onClick={() => {
        >          this.isLoading = !this.isLoading // 直接赋值修改
        >          this.setState({                  // setState修改
        >            current: this.state.current + 1
        >          })
        >        }}
        >      >
        >        {this.state.current}
        >      </View>
        >    )
        >  }
        >}
        >```
        ></details>
4. Props

    >可以把任何东西当做Props传递，如：组件、函数、JS的任意数据类型。

    1. 特殊属性

        1. `key`的取值和[Vue中`key`的注意点（17.i）](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/Vue.js学习笔记/README.md#指令--特殊attribute)一致

            因为JSX的灵活，只要是能够`切换或条件判断`的都需要考虑`key`。包括：`Array`方法、数组、条件判断（`switch`、`if`）等。

            >1. 组件的`key`值并不需要在全局都保证唯一，只需要在当前的同一级元素（兄弟节点）之前保证唯一即可。
            >2. `key`无法 ~~作为Props传递给子组件~~。
        2. `ref`

            ><details>
            ><summary>e.g.</summary>
            >
            >```jsx
            >// father
            >constructor(props) {
            >  super(props);
            >  this.divRef = React.createRef();
            >  this.sonRef = React.createRef();
            >}
            >render() {
            >  return (
            >    <div onClick={() => {console.log(this.divRef, this.sonRef)}}>
            >      <div
            >        ref={this.divRef}
            >      />
            >      <Son
            >        refData={this.sonRef}  // 父组件渲染会导致子组件渲染
            >      />
            >    </div>
            >  );
            >}
            >
            >
            >// Son
            >render() {
            >  return (
            >    <div ref={this.props.refData} />
            >  );
            >}
            >```
            ></details>

            可以从父级传递`React.createRef()`实例，再在子组件赋值子组件节点的`ref`到Props，这样父节点就可以获得子节点的`ref`。

            - `React.forwardRef((props, ref) => {})`

                Refs转发
    2. 把DOM或React元素传入子组件

        1. `children`

            传入子组件内的内容，都会在子组件的`props.children`中。
        2. 传参

        ><details>
        ><summary>e.g.</summary>
        >
        >```jsx
        >export default function Father () {
        >  return (
        >    <Son1
        >      aa={<Son2 />}             // 传参
        >      bb={<p>from Father 2</p>} // 传参
        >    >
        >
        >      {/*children*/}
        >      <p>from Father 3</p>
        >      <Son2 />
        >
        >    </Son1>
        >  );
        >}
        >
        >function Son1 (props) {
        >  return (
        >    <div className="m-son-1">
        >      {props.children}
        >      {props.aa}
        >      {props.bb}
        >    </div>
        >  );
        >}
        >
        >function Son2 (props) {
        >  return (
        >    <div className="m-son-2">Son2</div>
        >  );
        >}
        >```
        ></details>

    - 组合、~~继承~~

        用组合（`import`和Props）的方式、而不是 ~~继承（`extends`）~~ 的方式构建新组件。

        - 特例关系（specialization）

            一个组件是其他组件的特殊实例（special case）。

            ><details>
            ><summary>e.g.</summary>
            >
            >```jsx
            >function Dialog(props) {
            >  return (
            >    <FancyBorder color="blue">
            >      <h1 className="Dialog-title">
            >        {props.title}
            >      </h1>
            >      <p className="Dialog-message">
            >        {props.message}
            >      </p>
            >    </FancyBorder>
            >  );
            >}
            >
            >// WelcomeDialog 可以说是 Dialog 的特殊实例
            >function WelcomeDialog() {
            >  return (
            >    <Dialog
            >      title="Welcome"
            >      message="Thank you for visiting our spacecraft!" />
            >  );
            >}
            >```
            ></details>
5. 书写方式

    1. `render`函数中事件触发组件方法时传递`this`的绑定事件方式：

        1. 仅一次声明（推荐）

            ```jsx
            class 组件名 extends React.Component {
              constructor (props) {
                super(props);

                // 关键代码：
                this.handleClick = this.handleClick.bind(this);
              }

              handleClick (e) {
                console.log(this, e)
              }

              render () {
                return (
                  <button onClick={this.handleClick} />
                );
              }
            }
            ```

            ```jsx
            class 组件 extends React.Component {
              // 关键代码：
              handleClick = (e) => {  // 注意: 这是 *实验性* 语法（默认启用此语法）
                console.log(this, e);
              };

              render () {
                return (
                  <button onClick={this.handleClick} />
                );
              }
            }
            ```
        2. 组件render时会创建不同回调函数（不推荐）

            若这种写法作为Props传入子组件，则父级每次render都会导致传入子组件的这个Props变化，导致子组件重新渲染。

            ><details>
            ><summary>e.g.</summary>
            >
            >```jsx
            >class 组件 extends React.Component {
            >  handleClick (e) {
            >    console.log(this, e);
            >  };
            >
            >  render () {
            >    return (
            >      <button
            >        // handleClick的this指向组件实例
            >        onClick={this.handleClick.bind(this)}
            >        onClick={(e) => {this.handleClick(e);}}
            >
            >        // handleClick的this指向undefined
            >        // onClick={this.handleClick}
            >      />
            >    );
            >  }
            >}
            >```
            ></details>
    2. State初始化：

        ```jsx
        class 组件名 extends React.Component {
          state = {
            value: 0
          }
        }
        ```

        ```jsx
        class 组件名 extends React.Component {
          constructor(props) {
            super(props)
            this.state = {
              value: 0
            }
          }
        }
        ```
6. 通信

    1. 父子组件间的通信（单向数据流/单向绑定）

        父级（Props） -> 子级。其中Props包括：数据（可以是父级的State） + 父级的方法。

        ><details>
        ><summary>e.g.</summary>
        >
        >```jsx
        >// 父级
        ><子组件
        >  必要属性1='你好'
        >  可选方法1={this.父级方法} // 父级方法的参数：子级调用时传入
        >/>
        >```
        >
        >```jsx
        >// 子级
        >import React from "react";
        >
        >import { View } from "react-native";
        >
        >// 可选Props
        >interface 组件PropsOptional {
        >  可选属性1?: boolean,
        >  可选属性2?: number,
        >  可选方法1?: () => void,
        >}
        >
        >// +必要Props
        >interface 组件Props extends 组件PropsOptional {
        >  必要属性1: string
        >}
        >
        >// State
        >interface 组件State {
        >  本地属性1: number
        >}
        >
        >export default class 组件 extends React.Component<组件Props, 组件State> {
        >  public static defaultProps: 组件PropsOptional = {
        >    可选属性1: false,
        >    可选属性2: 123,
        >  };
        >
        >  public readonly state: 组件State = {
        >    本地属性1: this.props.可选属性2 || 0
        >  };
        >
        >  public constructor (props: 组件Props) {
        >    super(props);
        >  }
        >
        >  public render () {
        >    const { 本地属性1 } = this.state;
        >    const { 必要属性1, 可选属性1, 可选方法1 } = this.props;
        >
        >    return(
        >        <View
        >          style={styles.son}
        >          onClick={() => {
        >            this.setState({
        >              本地属性1: 本地属性1 + 1
        >            });
        >            可选方法1 && 可选方法1(子级参数);
        >          }}
        >        >
        >          <View>{本地属性1}</View>
        >          <View>{必要属性1}</View>
        >          <View>{可选属性1 ? '可选属性1: true' : '可选属性1: false'}</View>
        >        </View>
        >    );
        >  }
        >}
        >```
        ></details>
    2. 非父子组件通信

        1. 祖孙组件间的通信

            1. Props逐层往下传递

            2. <details>

                <summary><code>context</code>从祖辈向所有孙辈传递</summary>

                1. `const MyContext = React.createContext(默认值)`
                2. 祖辈组件设置：`<MyContext.Provider value={/* 某个值 */}>`

                    >可以嵌套不同context的Provider。

                    当`Provider`的`value`值发生变化时，它内部所有孙辈节点的`this.context`和`Consumer组件`都会重新渲染。
                3. 孙辈组件使用的2种方式：

                    从组件树中离自身最近匹配`Provider`中读取到当前的`context`值。

                    1. `contextType`

                        - 2种声明方式：

                            1. 组件类的声明之后：`组件.contextType = MyContext`
                            2. 组件类的静态属性：`static contextType = MyContext`

                        孙辈组件中通过`this.context`使用。
                    2. `<MyContext.Consumer>{(data) => { return 组件 }}<MyContext.Consumer>`

                        >`Provider`及其内部`Consumer组件`都不受制于`shouldComponentUpdate`函数，因此当`Consumer组件`在其祖辈组件退出更新的情况下也能更新。

                - `MyContext.displayName = 字符串`

                    React DevTools使用该字符串来确定context要显示的内容。
                </details>
        2. 通用

            1. 状态管理（redux、mobx）
            2. 开发人员维护事件订阅机制
            3. ~~其他能被任意地方调用的全局属性（如：cookie、Web Storage、window、等）~~

    >1. 若多个组件需要反映相同的变化数据，则将共享状态提升到最近的共同父组件中去。
    >
    >    应当依靠自上而下的数据流，而不是尝试在不同组件间同步State。
    >2. 若某些数据可以由Props或State推导得出，则它就不应该存在于State中
7. 事件处理

    1. 小驼峰式（camelCase）定义事件名
    2. 事件处理函数的参数是一个合成事件（`e`）。

        1. 参数只能同步使用，异步不保存。
        2. 阻止默认行为、阻止冒泡，必须显式调用`e.preventDefault/stopPropagation()`
8. 特殊组件

    1. `<React.Fragment>`

        1. 仅支持`key`属性。
        2. 短语法：`<>子节点</>`（不支持所有属性，包括不支持`key`属性）。
    2. 表单

        1. 受控组件（controlled components）

            渲染表单的React组件还控制着用户输入过程中表单发生的操作（表单的`value`、`onChange`受组件控制）。React的State成为表单“唯一数据源”。

            1. `<input>`、`<textarea>`

                ><details>
                ><summary>e.g.</summary>
                >
                >```jsx
                >constructor (props) {
                >  super(props);
                >  this.state = { value: "初始化值" };
                >
                >  this.handleChange = this.handleChange.bind(this);
                >}
                >
                >handleChange (event) {
                >  this.setState({ value: event.target.value });
                >}
                >
                >render () {
                >  return (
                >    <input或textarea type="text" value={this.state.value} onChange={this.handleChange} />
                >  );
                >}
                >```
                ></details>
            2. `<select>`

                ><details>
                ><summary>e.g.</summary>
                >
                >```jsx
                >// 单选
                >constructor (props) {
                >  super(props);
                >  this.state = { value: "coconut" };
                >
                >  this.handleChange = this.handleChange.bind(this);
                >}
                >
                >handleChange (event) {
                >  this.setState({ value: event.target.value });
                >}
                >
                >render () {
                >  return (
                >    <select value={this.state.value} onChange={this.handleChange}>
                >      <option value="grapefruit">葡萄柚</option>
                >      <option value="lime">酸橙</option>
                >      <option value="coconut">椰子</option>
                >      <option value="mango">芒果</option>
                >    </select>
                >  );
                >}
                >```
                >
                >```jsx
                >// 多选
                >constructor (props) {
                >  super(props);
                >  this.state = { value: ["coconut", "mango"] };
                >
                >  this.handleClick = this.handleClick.bind(this);
                >}
                >
                >handleClick (event) {
                >  const value = event.target.value;
                >
                >  this.setState((state) => {
                >    const oldValue = state.value.slice();
                >    if (oldValue.includes(value)) {
                >      oldValue.splice(oldValue.indexOf(value), 1);
                >    } else {
                >      oldValue.push(value);
                >    }
                >    return { value: oldValue };
                >  });
                >
                >}
                >
                >render () {
                >  return (
                >    <select multiple={true} value={this.state.value} onChange={this.handleClick}>
                >      <option value="grapefruit">葡萄柚</option>
                >      <option value="lime">酸橙</option>
                >      <option value="coconut">椰子</option>
                >      <option value="mango">芒果</option>
                >    </select>
                >  );
                >}
                >```
                ></details>

            - 在受控组件上写死`value`会阻止用户输入（除了 ~~`null/undefined`~~）。

                >e.g.
                >
                >1. 无法输入改变表单：`<input value="hi" />`。
                >2. 可以输入改变表单：`<input value={undefined} />`、`<input value={null} />`、`<input />`。
        2. 非受控组件（uncontrolled components）
    3. 错误边界（error boundaries）

        若一个class组件中定义了`static getDerivedStateFromError()`（渲染备用UI）或`componentDidCatch()`（打印错误信息）这两个生命周期方法中的任意一个（或两个）时，则它就变成一个错误边界。可以当做常规组件去使用。

        >任何未被错误边界捕获的错误将会导致整个React组件树被卸载。

        - 无法捕获错误的场景：

            1. 事件处理

                >利用`try-catch`弥补。
            2. 异步代码
            3. 服务端渲染
            4. 它自身抛出的错误

                若一个错误边界无法渲染错误信息，则错误会冒泡至最近的上层错误边界。
    4. 严格模式`<React.StrictMode />`
    5. 高阶组件（higher order component，HOC）

        >是一种设计模式。

        参数为组件，返回值为新组件的函数。

        1. HOC不应该修改传入组件，而应该使用组合的方式，通过将组件包装在容器组件中实现功能。
        2. 是纯函数，没有副作用。
9. 命名规范

    1. 事件监听Props命名为：`on[Event]`；事件监听处理函数命名为：`handle[Event]`。

#### 代码分割（动态加载）
添加一个动态引入，就会新增一个`chunk`、不会~~把动态引入的代码加入`bundle`~~。策略：基于路由进行代码分割。

1. `import()`

    >e.g. `import("./math").then(math => { console.log(math.add(16, 26)); });`
2. `<Suspense>`渲染`React.lazy`

    >不支持服务端渲染。

    ><details>
    ><summary>e.g.</summary>
    >
    >```jsx
    >import React, { Suspense } from 'react';
    >
    >const OtherComponent = React.lazy(() => import('./OtherComponent'));
    >
    >function MyComponent() {
    >  return (
    >    <Suspense fallback={<div>懒加载前展示的组件</div>}>
    >      多个懒加载组件
    >      <OtherComponent />
    >    </Suspense>
    >  );
    >}
    >```
    ></details>

### [create-react-app](https://github.com/facebook/create-react-app)
1. 模板：

    1. 搜索：[cra-template-*](https://www.npmjs.com/search?q=cra-template-*)
    2. 创建：`npx create-react-app 「文件夹名」 --template 「模板名」`

        >e.g. `npx create-react-app my-app --template typescript`
2. 必要文件

    1. `public/index.html`：页面模板

        1. 仅能使用`public/`内的文件。
        2. webpack不会处理`public/`内的文件。
        3. 引用`public/`路径：

            1. `public/`内使用`%PUBLIC_URL%`
            2. `src/`内使用`process.env.PUBLIC_URL`
    2. `src/index.js`：入口文件

        1. 业务文件仅能放到`src/`。
        2. webpack仅处理`src/`内的文件。
3. [`scripts`](https://create-react-app.dev/docs/available-scripts)
4. 模块的导出引入

    1. 支持ES6 Module（推荐）、CommonJS。
    2. 支持`import()`

    - 建议：仅导出单个内容时使用`export default 表达式`。
5. 环境变量

    >若要改变环境变量，则需要重启应用。

    1. 内容：

        1. `NODE_ENV`
        2. 以`REACT_APP_`开头的环境变量（不是以`REACT_APP_`开头的均无法获得）
    2. 使用：

        1. `src/`：`process.env.「名字」`
        2. `public/index.html`：`%「名字」%`

            >只有`public/index.html`可以使用环境变量，`public/`其他文件都不编译解析、直接拷贝到根目录供引用。
    3. 设置：

        1. 根目录下的`.env`等文件
        2. 临时：`REACT_APP_「变量」=「值」 npm start`（macOS）
        3. 设置环境变量：`export 「变量」=「值」`

        - [高级环境配置](https://create-react-app.dev/docs/advanced-configuration/)

            >小部分可以在代码中使用，大部分只是配置、无法在代码中输出。

### [redux](https://github.com/reduxjs/redux)
1. 设计思想

    1. Web应用是一个状态机，视图与状态是一一对应的。
    2. 所有的状态，保存在一个对象里面。

### [mobx](https://github.com/mobxjs/mobx)
1. computed

    （？某些情况下：）用到才去计算。每一次用到都会跑一遍计算的方法（类似vuex的getters返回一个函数的情况）。

### [react-native](https://github.com/facebook/react-native)
1. 排版引擎：[yoga](https://github.com/facebook/yoga)
2. 样式

    [Stack Overflow: flex vs flexGrow vs flexShrink vs flexBasis in React Native?](https://stackoverflow.com/questions/43143258/flex-vs-flexgrow-vs-flexshrink-vs-flexbasis-in-react-native)
