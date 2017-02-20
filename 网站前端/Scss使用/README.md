# Scss使用（part of [it](http://sass-lang.com/documentation/file.SASS_REFERENCE.html#css_extensions)）
>1. 推荐使用傻瓜式前端预处理器语言图形编译工具：[Koala](http://koala-app.com/index-zh.html)。
>2. 或者使用gulp（[gulp-sass](https://github.com/dlmanning/gulp-sass)）等构建工具。

1. `变量`、`方法`和`引用`必须在使用前定义，`继承`不需要提前定义；声明相同内容不会报错，只会用最后一次声明覆盖之前声明。

2. 变量以`$`开头

    1. 正常使用

        ```scss
        $name: red;

        a {
            color: $name;
        }
        ```
    2. 变量用于**选择器**、**属性名**或**不被计算的基本css**时，使用时要`#{}`嵌套`$`

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
    变量有命名空间，全局、局部之分。

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

5. 继承`@extend`

    查找所有满足`@extend`后的**选择器**的内容，把此选择器替换成使用继承的选择器。

    1. 正常情况

        ```scss
        .clearfix {
            zoom: 1;
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

    ```scss
    @import "../css/1";
    ```

7. 算术`+` `-` `*` `/`

    ```scss
    a {
        color: #123 + #abc;
        font-size: (20px / 2);
    }
    ```

8. 注释

    ```scss
    // 不出现在css
    /* 出现在css*/
    ```
    >有中文注释时，要在scss文件顶部增加`@charset "utf-8";`，否则编译报错。

9. 方法`@function`

    ```scss
    @function func($para) {
        @return $para * 2 + rem;
    }

    .name {
        font-size: func(10);
    }
    ```

10. `@if` `@for` `@each` `@while`...