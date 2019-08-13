# React学习笔记

## 目录
1. [react](#react)
1. [mobx](#mobx)
1. [taro](#taro)

---

### [react](https://github.com/facebook/react)
1. 组件上两种绑定事件方式

    ```javascript
    this.func.bind(this)

    () => {
      this.func()
    }
    ```
2. `key`的取值和[Vue中`key`的注意点（16.i）](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/Vue.js学习笔记/README.md#指令--特殊attribute)一致

    因为JSX的灵活，只要是能够`切换或条件判断`的都需要考虑`key`。包括`Array`方法、数组、条件判断（`switch`、`if`）等。
3. 模板内的属性

    1. 要在模板内展示的属性，需要放到state中被观测（或放到mobx中被观测），才能在这些值改变时通知视图重新渲染。

        `this.setState({ 属性: '新值' }, () => {/* 更新后的回调 */})`函数是唯一能够更新`this.state.属性`的地方。
    2. 不在模板内展示的值（如：仅作为事件触发修改的状态值、仅在JS逻辑中改变的值），直接放在class中的实例属性中。

    ><details>
    ><summary>e.g.</summary>
    >
    >```jsx
    >class MyComponent extends Component {
    >  constructor (...props) {
    >    super(...props)
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
4. （`class`是保留字，）标签上用`className`代替`class`使用。
5. 组件只能显性接受传入的`props`内容（在外层传`style`、`className`等，需要在组件内接受并处理）。

### [mobx](https://github.com/mobxjs/mobx)
1. computed

    （？某些情况下：）用到才去计算。每一次用到都会跑一遍计算的方法（类似vuex的getters返回一个函数的情况）。

### [taro](https://github.com/NervJS/taro)
1. 组件库

    1. `<Button>`的`hoverClass`要在没有`className`时才起作用（`<View>`的不受此限制）。
    2. `Swiper`动态改变配置会导致渲染错误，因此配置只能用固定不变的值。
2. 其他

    1. 有些样式写在`.scss`里会被框架删除，需要添加到`.tsx`模板上。

        e.g. `-webkit-box-orient: vertical;`
