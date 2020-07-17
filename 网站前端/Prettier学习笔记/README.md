# [prettier](https://github.com/prettier/prettier)学习笔记

1. CI命令

    ```shell
    prettier --write 「文件（夹）」    # 执行

    prettier --check 「文件（夹）」    # 判断是否已经prettier
    ```
2. 配置文件

    1. `.prettierrc.json`
    2. `.prettierignore`
3. 忽略接下来的语句块

    ```shell
    # JS
    // prettier-ignore

    # JSX
    {/* prettier-ignore */}

    # HTML
    <!-- prettier-ignore -->
    <!-- prettier-ignore-attribute -->
    <!-- prettier-ignore-attribute (mouseup) -->

    # CSS
    /* prettier-ignore */

    # markdown
    <!-- prettier-ignore -->

    <!-- prettier-ignore-start -->
    内容范围
    <!-- prettier-ignore-end -->

    # YAML
    # prettier-ignore

    # GraphQL
    # prettier-ignore

    # Handlebars
    {{! prettier-ignore }}
    ```
