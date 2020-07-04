# React学习笔记

## 目录
1. [react](#react)
1. [redux](#redux)
1. [mobx](#mobx)
1. [react-native](#react-native)

---

### [react](https://github.com/facebook/react)
1. 组件写法注意

    1. `render`函数中事件触发组件方法时传递`this`的两种绑定事件方式：

        ```JSX
        <div
          // handleClick的this指向组件实例
          onClick={this.handleClick.bind(this)}
          onClick={() => {this.handleClick()}}

          // handleClick的this指向undefined
          onClick={this.handleClick}
        />
        ```
    2. `state`初始化：

        ```JSX
        class 组件名 extends React.Component {
          state = {
            value: 0
          }
        }

        // 或

        class 组件名 extends React.Component {
          constructor(props) {
            super(props)
            this.state = {
              value: 0
            }
          }
        }
        ```
2. 组件的特殊属性

    1. `key`的取值和[Vue中`key`的注意点（17.i）](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/Vue.js学习笔记/README.md#指令--特殊attribute)一致

        因为JSX的灵活，只要是能够`切换或条件判断`的都需要考虑`key`。包括`Array`方法、数组、条件判断（`switch`、`if`）等。

        >组件的`key`值并不需要在全局都保证唯一，只需要在当前的同一级元素之前保证唯一即可。
    2. `ref`
3. 模板内的属性

    1. 要在模板内展示的属性，需要放到state中被观测（或放到store中被观测，如：redux、mobx），才能在这些值改变时通知视图重新渲染。

        `this.setState({ 属性: '新值' }, () => {/* 更新后的回调 */})`函数是唯一能够更新`this.state.属性`的方式。
    2. 不在模板内展示的值（如：仅作为事件触发修改的状态值、仅在JS逻辑中改变的值），直接放在class中的实例属性中。

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

    - 不可变性（引用数据类型）

        不直接修改数据（或改变底层数据），而是用新值替换旧值。（对需要修改的`state`内容浅复制一层，对新值进行修改后覆盖原`state`）
4. （`class`是保留字，）标签上用`className`代替`class`使用。
5. 组件只能显性接受传入的`props`内容（在外层传`style`、`className`等，需要在组件内接受并处理）。
6. 通信

    1. 父子组件间的通信

        父级（`props`） -> 子级。其中`props`包括：给子级的初始化数据 + 给子级调用父级的方法。

        <details>
        <summary>e.g.</summary>

        ```jsx
        // 父级
        <子组件
          必要属性1='你好'
          可选方法1={this.父级方法} // 父级方法的参数：子级调用时传入
        />
        ```

        ```jsx
        // 子级
        import React from "react";

        import { View } from "react-native";

        // 可选props
        interface 组件PropsOptional {
          可选属性1?: boolean,
          可选属性2?: number,
          可选方法1?: () => void,
        }

        // +必要props
        interface 组件Props extends 组件PropsOptional {
          必要属性1: string
        }

        // state
        interface 组件State {
          本地属性1: number
        }

        export default class 组件 extends React.Component<组件Props, 组件State> {
          public static defaultProps: 组件PropsOptional = {
            可选属性1: false,
            可选属性2: 123,
          };

          public readonly state: 组件State = {
            本地属性1: this.props.可选属性2 || 0
          };

          public constructor (props: 组件Props) {
            super(props);
          }

          public render () {
            const { 本地属性1 } = this.state;
            const { 必要属性1, 可选属性1, 可选方法1 } = this.props;

            return(
                <View
                  style={styles.son}
                  onClick={() => {
                    this.setState({
                      本地属性1: 本地属性1 + 1
                    });
                    可选方法1 && 可选方法1(子级参数);
                  }}
                >
                  <View>{本地属性1}</View>
                  <View>{必要属性1}</View>
                  <View>{可选属性1 ? '可选属性1: true' : '可选属性1: false'}</View>
                </View>
            );
          }
        }
        ```
        </details>
    2. 非父子组件通信

        1. 祖孙组件间的通信

            1. `props`逐层往下传递
            2. `context`从祖辈向所有孙辈传递
        2. 通用

            1. 状态管理（redux、mobx）
            2. 开发人员维护事件订阅机制
            3. ~~其他能被任意地方调用的全局属性（如：cookie、Web Storage、window、等）~~
7. 函数组件

    若组件仅包含一个`render`方法 && 不包含 ~~`state`~~，则使用函数组件会更简单。

    <details>
    <summary>e.g.</summary>

    ```JSX
    // 函数组件
    function 组件名 (props) {
      return (
        <div className="m-div" onClick={props.onClick}>
          {props.value}
        </div>
      );
    }
    ```
    </details>
8. 命名规范

    1. 事件监听`prop`命名为：`on[Event]`；事件监听处理函数命名为：`handle[Event]`。
9. JSX

    - 为`非构建工具（未使用JSX预处理器）`处理的`<script>`，添加JSX支持：

        1. 添加`<script src="https://unpkg.com/babel-standalone@6/babel.min.js"></script>`；
        2. 在使用JSX的.js文件引用加上`type="text/babel"`。

- 概念

    1. 高阶组件（higher order component，HOC）

        react中对组件逻辑进行重用的高级技术。高阶组件是一个函数，且该函数接受一个组件作为参数，并返回一个新的组件。对比组件将props属性转变成UI，高阶组件则是将一个组件转换成另一个新组件。

### [redux](https://github.com/reduxjs/redux)
1. 设计思想

    1. Web应用是一个状态机，视图与状态是一一对应的。
    2. 所有的状态，保存在一个对象里面。

### [mobx](https://github.com/mobxjs/mobx)
1. computed

    （？某些情况下：）用到才去计算。每一次用到都会跑一遍计算的方法（类似vuex的getters返回一个函数的情况）。

### [react-native](https://github.com/facebook/react-native)
1. 排版引擎：[yoga](https://github.com/facebook/yoga)
