# [prettier](https://github.com/prettier/prettier)学习笔记

1. CI命令

    ```shell
    prettier --write 「文件（夹）」    # 执行

    prettier --check 「文件（夹）」    # 判断是否已经prettier
    ```
2. 配置文件

    1. 配置规则：

        1. `package.json`：`prettier`
        2. JSON或YAML：`.prettierrc`
        3. `.prettierrc.json`、`.prettierrc.yml`、`.prettierrc.yaml`
        4. `module.exports`：`.prettierrc.js`、`prettier.config.js`
        5. `.prettierrc.toml`
    2. `.prettierignore`
3. 不对接下来的语句块进行prettier

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
4. 配置规则

    [prettier: options](https://prettier.io/docs/en/options.html)
