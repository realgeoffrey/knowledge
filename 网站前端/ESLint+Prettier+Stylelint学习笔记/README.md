# ESLint+Prettier+Stylelint学习笔记

## 目录
1. [ESLint](#eslint)
1. [Prettier](#prettier)
1. [Stylelint](#stylelint)
1. [区别和配合使用](#区别和配合使用)

---
### [ESLint](https://github.com/eslint/eslint)
>eslint@8

1. [CLI命令](https://zh-hans.eslint.org/docs/latest/use/command-line-interface)

    ```shell
    eslint [options] file.js [file.js] [dir]

      --fix
      --ext .xx,.yy
    ```
2. 配置文件

    1. 配置优先级（降序）

        1. 内联配置

            1. `/* eslint-disable */`、`/* eslint-enable */`

                1. 取消之后所有内容的eslint判断：

                    1. `/* eslint-disable */`
                    2. `/* eslint-disable 规则名1[, 规则名2] */`

                - 开启之后所有内容的eslint判断：

                    1. `/* eslint-enable */`
                    2. `/* eslint-enable 规则名1[, 规则名2] */`

                2. 取消当前行的eslint判断：

                    1. `/* eslint-disable-line */` 或 `// eslint-disable-line`
                    2. `/* eslint-disable-line 规则名1[, 规则名2] */` 或 `// eslint-disable-line 规则名1[, 规则名2]`
                3. 取消下一行的eslint判断：

                    1. `/* eslint-disable-next-line */` 或 `// eslint-disable-next-line`
                    2. `/* eslint-disable-next-line 规则名1[, 规则名2] */` 或 `// eslint-disable-next-line 规则名1[, 规则名2]`
            2. `/* global */`
            3. `/* eslint */`
            4. `/* eslint-env */`
        2. 命令行选项

            1. `--global`
            2. `--rule`
            3. `--env`
            4. `-c/--config`（可配合`--no-eslintrc`忽略所有规则默认查找）
        3. 项目级配置

            会在每一个被检查文件的目录中寻找配置文件（不是~~命令执行的目录~~，而是每一个被检查文件的目录，因此不同文件夹的文件都可能有不同的规则配置），并在其直系祖先目录中寻找，直到触发任意停止条件：抵达文件系统的根目录（`/`）或 配置包含 `root: true` ~~或 抵达当前用户的主目录（`~/`）~~。

            - 同一级文件夹内的配置只会使用以下优先级最高的一个文件（降序）：

                1. .eslintrc.js(输出一个配置对象)
                2. .eslintrc.cjs
                3. .eslintrc.yaml
                4. .eslintrc.yml
                5. .eslintrc.json（ESLint的JSON文件允许JavaScript风格的注释）
                6. package.json（在package.json里创建一个eslintConfig属性，在那里定义你的配置）
            - 不同文件夹的规则嵌套覆盖。若未达到停止条件，会一直往上查找并合并配置，相同规则 以 越接近文件的（越先被搜索到的）优先。
    2. 忽略文件

        `.eslintignore`（不会包含.gitignore。指定其他文件作为eslint忽略文件：`--ignore-path .gitignore`）

        >忽略语法和[.gitignore](https://git-scm.com/docs/gitignore#_pattern_format)类似。
    3. 配置内容

        1. `root: true/false`是否不再向上搜索配置文件
        2. `extends: [ 配置名 或 plugin:缩写插件名/插件自定义的配置名 或 文件路径 ]`继承另一个配置文件的所有配置，extends后面的项优先级更高

            1. 可以省略配置名称中的`eslint-config-`前缀，e.g. `airbnb`会被解析为`eslint-config-airbnb`。
            2. 可以是基于配置文件的绝对或相对路径。e.g. `"./node_modules/coding-standard/eslintDefaults.js"`、`require.resolve('仓库名/导出的文件路径')`。
            3. `eslint:recommended`或`eslint:all`。
        3. `plugins: []`添加扩展功能的npm包

            1. 可以省略包名中的`eslint-plugin-`前缀，e.g. `react`是`eslint-plugin-react`的缩写。
            2. 插件作用

                1. 自定义规则，以验证你的代码是否符合某个期望，以及如果不符合该期望该怎么做。
                2. 自定义配置。
                3. 自定义环境。
                4. 自定义处理器，从其他类型的文件中提取JS代码，或在提示前对代码进行预处理。
        4. `overrides: []`针对glob模式进行精细化配置，匹配的文件和规则优先级高于其他配置，overrides后面的项优先级更高

            1. 必须包含`files`字段。
            2. glob在项目级配置中是相对于当前配置文件，在`--config`命令行配置中相对于命令执行目录。
        5. `env: { 环境名 或 缩写插件名/插件自定义的环境名: true/false, }`是否开启环境提供预设的全局变量

            `browser`、`node`、`commonjs`、`shared-node-browser`、`es6`、`es2016~es2024`、`worker`、`amd`、`mocha`、`jasmine`、`jest`、`phantomjs`、`protractor`、`qunit`、`jquery`、`prototypejs`、`shelljs`、`meteor`、`mongo`、`applescript`、`nashorn`、`serviceworker`、`atomtest`、`embertest`、`webextensions`、`greasemonkey`
        6. `globals: { 全局变量名: "writable或readonly或off" }`
        7. `rules: { 规则名 或 缩写插件名/插件自定义的规则名: 值 或 [ 值, 额外选项 ] }`

            "off"===0，"warn"===1，"error"===2（触发时退出代码为1）
        8. `noInlineConfig: true/false`是否禁用所有内联配置注释
        9. `reportUnusedDisableDirectives: true/false`报告不需要的eslint-disable内置注释
        10. `parserOptions`指定解析器选项

            >设置解析器选项有助于 ESLint 确定解析错误是什么。所有的语言选项默认为 `false`。

            1. `.ecmaVersion: 3~15或"latest"`指定要使用的ECMAScript语法的版本
            1. `.sourceType: "script或module"`
            1. `.allowReserved: true/false`允许使用保留字作为标识符
            1. `.ecmaFeatures`想使用哪些额外的语言特性的对象

                1. `.globalReturn: true/false`是否允许全局范围内的return语句
                1. `.impliedStrict: true/false`是否启用全局严格模式
                1. `.jsx: true/false`是否启用jsx
        11. `processor: 处理器名 或 缩写插件名/插件自定义的处理器名`
        12. `parser: 解析器名`

            Esprima、@babel/eslint-parser、@typescript-eslint/parser
        13. `ignorePatterns`忽略文件

            1. glob在项目级配置中是相对于当前配置文件，在`--config`命令行配置中相对于命令执行目录。
            2. 不能在`overrides`属性中使用`ignorePatterns`。
            3. 优先级（降序）：`.eslintignore`文件、`ignorePatterns`配置、`package.json`的`eslintIgnore`
        14. `settings: {}`插件plugins使用来指定应该在其所有规则rules中共享的信息
    4. 缓存文件`.eslintcache`

        >当执行带`cache`的eslint命令时，若原本不存在`.eslintcache`文件，则不会进行仅缓存对比（没有缓存文件）；若存在`.eslintcache`文件，才会进行仅缓存对比。

        - 产生条件：

            1. 命令加了`--cache`（或配置文件包含`cache: true`）

                - 执行一次未包含`--cache`（或配置文件未包含`cache: true`）的命令会删除已有的`.eslintcache`文件
            2. && eslint匹配到了任何文件且没有报错退出
            3. && 输入方式不是 ~~`stdin`~~（e.g. `echo "let a = 1" | eslint --stdin --cache`不会产生/删除`.eslintcache`文件）
            - 注意生成路径（默认在运行命令的目录，可以命令`--cache-location 路径`或配置文件`cacheLocation: '路径'`指定其他位置）

### [Prettier](https://github.com/prettier/prettier)
1. CLI命令

    ```shell
    prettier --write 「文件（夹）」    # 执行

    prettier --check 「文件（夹）」    # 判断是否已经prettier
    ```

    ><details>
    ><summary>不要忘记 glob 周围的引号（<code>'</code>、<code>"</code>）。引号确保 Prettier CLI 扩展 glob 而不是你的 shell，这对于跨平台使用很重要。（对于其他命令同样适用，是该把解析通配符等字符串交给命令，还是交给Shell）</summary>
    >
    >e.g. `prettier "**/*.{vue,js}"`与`prettier **/*.{vue,js}`为什么前者能输出所有.js和.vue，而后者仅输出部分.js和所有.vue？
    >
    >1. Shell看到引号，直接把引号内字符串传递给命令（prettier），命令根据自己的规则（如.prettierignore等）解析这个字符串；
    >1. Shell未看到引号的情况下遇到`**`，触发Shell展开机制，会先解析再传递给命令（prettier）：
    >
    >    >当 Shell 在命令行中遇到特定的保留字符（元字符）且这些字符没有被转义或引用时，才会触发展开机制。具体展开机制略。
    >
    >    1. 展开`**/*.{vue,js}`为`**/*.vue **/*.js`
    >    2. 分别扫描`**/*.vue`与`**/*.js`最终分别输出所有匹配的路径
    >
    >        1. 因为`node_modules`里可能很多.js文件，甚至达到系统限制的ARG_MAX，因此.js的所有文件路径被部分截断，但所有.vue文件路径达不到截断长度因此被完整保留
    >    3. 把扫描出的所有路径传递给命令（prettier）
    ></details>
2. 配置文件

    1. 项目级配置

        会在每一个被检查文件的目录中寻找配置文件（不是~~命令执行的目录~~，而是每一个被检查文件的目录，因此不同文件夹的文件都可能有不同的规则配置），并在其直系祖先目录中寻找，直到触发停止条件：抵达执行prettier命令的目录。

        - 同一级文件夹内的配置只会使用以下优先级最高的一个文件（降序）：

            1. 优先级（降序）

                1. `package.json`：`prettier`
                2. JSON或YAML：`.prettierrc`
                3. `.prettierrc.json`、`.prettierrc.yml`、`.prettierrc.yaml`、`.prettierrc.json5`
                4. `module.exports`：`.prettierrc.js`、`prettier.config.js`
                5. `export default`：`.prettierrc.mjs`、`prettier.config.mjs`
                6. `.prettierrc.toml`

                - 配置简单，导出对象，没有config概念，分享使用通过导出对象进行。
        - 不同文件夹的规则嵌套覆盖。若未达到停止条件，会一直往上查找并合并配置，相同规则 以 越接近文件的（越先被搜索到的）优先。
    2. 忽略文件

        `.prettierignore`（prettier@3会默认加上`.gitignore`的内容；`prettier@2`不会）

        >忽略语法和[.gitignore](https://git-scm.com/docs/gitignore#_pattern_format)一致。

    - 配置规则

        [prettier: options](https://prettier.nodejs.cn/docs/en/options.html`)

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

### [Stylelint](https://github.com/stylelint/stylelint)
1. 配置内容

    - 配置逻辑和eslint类似

        1. 没有嵌套逻辑，以第一个搜索到的配置文件为准。若cli添加`-c/--config 配置路径`，则规则仅以设置的配置路径为准（类似eslint的`-c 配置路径 --no-eslintrc`）。
        2. 没有 ~~`root`~~ 配置（或可理解为`root`含义永远为`true`），每个文件仅会有一个配置。
    1. `extends: [ 配置名 或 文件路径 ]`

        配置。
    2. `overrides`

        覆盖，必须包含`files`。
2. 忽略文件

    `.stylelintignore`（不会包含.gitignore）

    >忽略语法和[.gitignore](https://git-scm.com/docs/gitignore#_pattern_format)一致。
3. [忽略代码](https://stylelint.nodejs.cn/user-guide/ignore-code)

    `stylelint-disable stylelint-enable stylelint-disable-line stylelint-disable-next-line`

### 区别和配合使用
1. 区别：

    1. ESLint（包括其他一些 lint 工具）的主要功能包含：**代码格式**的校验 + **代码质量**的校验。
    2. Prettier：只是**代码格式**的校验（并格式化代码），不会对~~代码质量~~进行校验。

    >1. 代码格式问题通常指的是：单行代码长度、tab长度、空格、逗号表达式等问题。
    >2. 代码质量问题指的是：未使用变量、三等号、全局变量声明等问题。
2. 配合使用：

    1. 通过`eslint`命令，使用`prettier`+`eslint`功能：[eslint-plugin-prettier](https://github.com/prettier/eslint-plugin-prettier)（使用eslint的忽略文件；可以在eslint的配置文件中配置prettier配置规则；可以完全不添加prettier配置文件和忽略文件）。
    2. 使用[`husky`](https://github.com/typicode/husky)/[`simple-git-hooks`](https://github.com/toplenboren/simple-git-hooks)+[`lint-staged`](https://github.com/okonet/lint-staged)，针对git的staged文件，在git hooks时期，进行lints操作（如：eslint、prettier、等）。

    >[demo](./demo)。
