### SCSS使用
>来自：[Sass](https://www.sasscss.com/docs/)。

- 预编译工具

    1. 使用傻瓜式CSS预处理器语言图形编译工具：[Koala](http://koala-app.com/index-zh.html)。
    2. 优先使用 Dart Sass 对应的 [`sass`](https://github.com/sass/dart-sass) 包；~~[node-sass](https://github.com/sass/node-sass)~~ 已 EOL，不建议新项目继续使用。`gulp-sass` 等构建工具也应确认底层实现为 Dart Sass。

1. `变量`、`方法`和`引用`必须在使用前定义，`继承`不需要提前定义；声明相同内容不会报错，只会用最后一次声明复盖之前声明。
2. 变量以`$`开头

    1. 正常使用

        ```scss
        $name: red;

        a {
            color: $name;
        }
        ```
    2. 变量用于**选择器**、**属性名**或**不被计算的基本CSS**时，使用时要`#{}`嵌套`$`

        ```scss
        $name: name;
        $attr: color;
        $font-size: 12px;
        $line-height: 20px;

        a.#{$name} {
            #{$attr}: #fff;
            font: #{$font-size}/#{$line-height} sans-serif;
        }
        ```

    变量有命名空间：全局、局部。
3. 嵌套，引用父级`&`

    1. 正常使用

        ```scss
        .name {
            color: #fff;

            span {
                color: #fff;
            }

            &:hover {
                color: #fff;
            }

            &_suffix {
                color: #fff;
            }
        }
        ```
    2. 嵌套，命名空间`:`

        ```scss
        a {
            color: #f00;

            span {
                color: red;
            }

            font: {
                weight: bold;
                family: fantasy;
            }
        }
        ```
4. `@include`引入`@mixin`

    1. 不带参数

        ```scss
        @mixin a {
            color: red;
        }
        @mixin b {
            .name2 {
                @include a;
            }
        }

        .name1 {
            @include b;
        }
        ```
    2. 带参数

        ```scss
        @mixin c($para1,$para2: 5px) {
            color: $para1;
            font-size: $para2;
        }

        .name3 {
            @include c(#fff);
        }
        .name4 {
            @include c(#fff, 10px);
        }
        ```
    3. 参数数量不定

        ```scss
        @mixin d($para...) {
            box-shadow: $para;
        }

        .name5 {
            @include d(0 4px 5px #666, 2px 6px 10px #999);
        }
        ```
    4. 使用`&`

        ```scss
        @mixin d($para) {
            font-size: $para;

            [data-dpr="2"] & {
                font-size: $para * 2;
            }
        }

        a {
            @include d(10px);
        }
        /*
        a {
            font-size: 10px
        }
        [data-dpr="2"] a {
            font-size: 20px
        }
        */
        ```
5. 继承`@extend`

    查找所有满足`@extend`后的**选择器**的内容，把此选择器替换成使用继承的选择器。

    1. 正常情况

        ```scss
        .clearfix {
            *zoom: 1;
        }
        .clearfix:after {
            content: '';
        }

        .name {
            @extend .clearfix;
        }
        ```
    2. 仅作为被继承，不编译自身`%`

        ```scss
        a%name span {
            color: #fff;
        }

        .abc {
            @extend %name;
        }
        ```
6. 引入文件`@import`

    >Sass `@import` 已废弃，新代码优先使用模块系统 `@use` / `@forward`；以下为旧项目读写方式。

    ```scss
    @import "../css/1.css";     // 写入 @import url(../css/1.css);
    @import "../scss/1.scss";   // 写入 1.scss 文件内容
    ```
7. 算术`+` `-` `*` `/`

    >Sass 中把 `/` 当除法已废弃，新代码用 `math.div()`；`/`更多保留给 CSS 原生斜杠语法。以下为旧写法理解。

    ```scss
    @function func() {
        @return 20px / 2;
    }
    a {
        color: #112233 + #aabbcc;  // #bbddff
        font-size: 20 + px;        // 20px
        width: (20px / 2);         // 10px
        height: func();            // 10px
        line-height: (20px / 2px); // 10
    }
    ```
8. 注释

    ```scss
    // 不出现在.css
    /* 出现在.css */
    ```
    >有中文注释时，要在.scss文件顶部增加`@charset "utf-8";`，否则编译报错。
9. 方法`@function`

    ```scss
    @function func($para) {
        @return $para * 2 + rem;
    }

    .name {
        font-size: func(10);
    }
    ```
10. `unit()`返回单位

    ```scss
    unit(100);       // ""
    unit(100px);     // "px"
    unit(3em);       // "em"
    unit(3rem);      // "rem"
    unit(3vw);       // "vw"
    unit(3vh);       // "vh"
    ```
11. `unitless()`是否没有单位

    ```scss
    unitless(100);   // true
    unitless(100px); // false
    ```
12. `@if` `@for` `@each` `@while`

    ><details>
    ><summary>e.g.</summary>
    >
    >```scss
    >@for $i from 5000 through 5999 {
    >  .s#{$i} {
    >    width: $i * 1%;
    >  }
    >}
    >```
    ></details>
