# ESLint+Prettier学习笔记

## 目录
1. [ESLint](#eslint)
1. [Prettier](#prettier)
1. [区别和配合使用](#区别和配合使用)

---

### [ESLint](https://github.com/eslint/eslint)
1. CI命令

    ```shell
    eslint [options] file.js [file.js] [dir]

      --fix
      --ext .xx,.yy
    ```
2. 配置文件

    1. 优先级（降序）

        1. .eslintrc.js(输出一个配置对象)
        2. .eslintrc.yaml
        3. .eslintrc.yml
        4. .eslintrc.json（ESLint的JSON文件允许JavaScript风格的注释）
        5. .eslintrc（可以是JSON也可以是YAML）
        6. package.json（在package.json里创建一个eslintConfig属性，在那里定义你的配置）
    2. 忽略文件

        `.eslintignore`（直接用`.gitignore`文件作为eslint忽略的文件：`--ignore-path .gitignore`）

        >忽略语法和[.gitignore](https://git-scm.com/docs/gitignore#_pattern_format)一致。

    - 配置文件内容

        ```javascript
        {
          //Eslint检测配置文件步骤：
          //1.在要检测的文件同一目录里寻找.eslintrc.*和package.json
          //2.紧接着在父级目录里寻找，一直到文件系统的根目录
          //3.若在前两步发现有root：true的配置，则停止在父级目录中寻找.eslintrc
          //4.若以上步骤都没有找到，则回退到用户主目录~/.eslintrc中自定义的默认配置
          "root": true,

          //ESLint默认使用Espree作为其解析器
          //同时babel-eslint也是用得最多的解析器
          "parser": "babel-eslint",

          //parser解析代码时的参数
          "parserOptions": {
            //指定要使用的ECMAScript版本，默认值5
            "ecmaVersion": 5,
            //设置为script(默认)或module（若你的代码是ECMAScript模块)
            "sourceType": "script",
            //这是个对象，表示你想使用的额外的语言特性,所有选项默认都是false
            "ecmafeatures": {
              //允许在全局作用域下使用return语句
              "globalReturn": false,
              //启用全局strict模式（严格模式）
              "impliedStrict": false,
              //启用JSX
              "jsx": false,
              //启用对实验性的objectRest/spreadProperties的支持
              "experimentalObjectRestSpread": false
            }
          },

          //指定环境，每个环境都有自己预定义的全局变量，可以同时指定多个环境，不矛盾
          "env": {
            //效果同配置项ecmaVersion一样
            "es6": true,
            "browser": true,
            "node": true,
            "commonjs": false,
            "mocha": true,
            "jquery": true,
             //若你想使用来自某个插件的环境时，则确保在plugins数组里指定插件名
             //格式为：插件名/环境名称（插件名不带前缀）
            "react/node": true
          },

          //extends属性值可以是一个字符串或字符串数组
          //数组中每个配置项继承它前面的配置
          //可选的配置项如下
          //1.字符串eslint：recommended，该配置项启用一系列核心规则，这些规则报告一些常见问题，即在(规则页面)中打勾的规则
          //2.一个可以输出配置对象的可共享配置包，如：eslint-config-standard
            //可共享配置包是一个导出配置对象的简单的npm包，包名称以eslint-config-开头，使用前要安装
            //extends属性值可以省略包名的前缀eslint-config-
          //3.一个输出配置规则的插件包，如：eslint-plugin-react
            //一些插件也可以输出一个或多个命名的配置
            //extends属性值为，plugin：包名/配置名称
          //4.一个指向配置文件的相对路径或绝对路径
          //5.字符串eslint：all，启用当前安装的ESLint中所有的核心规则
            //该配置不推荐在产品中使用，因为它随着ESLint版本进行更改。使用的话，请自己承担风险
          "extends": [
            "eslint:recommended",
            "standard",
            "plugin:react/recommended",
            "./node_modules/coding-standard/.eslintrc-es6",
            "eslint:all"
          ],

          //ESLint支持使用第三方插件
          //在使用插件之前，你必须使用npm安装它
          //全局安装的ESLint只能使用全局安装的插件
          //本地安装的ESLint不仅可以使用本地安装的插件还可以使用全局安装的插件
          //plugin与extend的区别：extend提供的是eslint现有规则的一系列预设
          //而plugin则提供除了预设之外的自定义规则，当你在eslint的规则里找不到合适时
          //就可以借用插件来实现了
          "plugins": [
            "eslint-plugin-airbnb",
            //插件名称可以省略eslint-plugin-前缀
            "react"
          ],

          //指定环境为我们提供了预置的全局变量
          //对于那些我们自定义的全局变量，可以用globals指定
          //设置每个变量等于true允许变量被重写，或false不允许被重写
          "globals": {
            "globalVar1": true,
            "globalVar2": false
          },

          //具体规则配置
          //off或0--关闭规则
          //warn或1--开启规则，警告级别(不会导致程序退出)
          //error或2--开启规则，错误级别(当被触发时，程序会退出)
          "rules": {
            "eqeqeq": "warn",
            //你也可以使用对应的数字定义规则严重程度
            "curly": 2,
            //若某条规则有额外的选项，则可以使用数组字面量指定它们
            //选项可以是字符串，也可以是对象
            "quotes": ["error", "double"],
            "one-var": ["error", {
              "var": "always",
              "let": "never",
              "const": "never"
            }],
            //配置插件提供的自定义规则时，格式为：不带前缀插件名/规则ID
            "react/curly": "error"
          },

          //ESLint支持在配置文件添加共享设置
          //你可以添加settings对象到配置文件，它将提供给每一个将被执行的规则
          //若你想添加的自定义规则而且使它们可以访问到相同的信息，则这将会很有用，并且很容易配置
          "settings": {
            "sharedData": "Hello"
          }
        }
        ```
3. 目标文件内的注释开关

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

### [Prettier](https://github.com/prettier/prettier)

1. CI命令

    ```shell
    prettier --write 「文件（夹）」    # 执行

    prettier --check 「文件（夹）」    # 判断是否已经prettier
    ```
2. 配置文件

    1. 优先级（降序）

        1. `package.json`：`prettier`
        2. JSON或YAML：`.prettierrc`
        3. `.prettierrc.json`、`.prettierrc.yml`、`.prettierrc.yaml`
        4. `module.exports`：`.prettierrc.js`、`prettier.config.js`
        5. `.prettierrc.toml`
    2. 忽略文件

        `.prettierignore`

        >忽略语法和[.gitignore](https://git-scm.com/docs/gitignore#_pattern_format)一致。

    - 配置规则

        [prettier: options](https://prettier.io/docs/en/options.html)
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

### 区别和配合使用
1. 区别：

    1. eslint（包括其他一些 lint 工具）的主要功能包含：**代码格式**的校验 + **代码质量**的校验。
    2. Prettier：只是**代码格式**的校验（并格式化代码），不会对~~代码质量~~进行校验。

    >1. 代码格式问题通常指的是：单行代码长度、tab长度、空格、逗号表达式等问题。
    >2. 代码质量问题指的是：未使用变量、三等号、全局变量声明等问题。
2. 配合使用：

    1. 通过`eslint`命令，使用`prettier`+`eslint`功能：[eslint-plugin-prettier](https://github.com/prettier/eslint-plugin-prettier)（使用eslint的忽略文件；可以在eslint的配置文件中配置prettier配置规则；可以完全不添加prettier配置文件和忽略文件）。
    2. 使用[`husky`](https://github.com/typicode/husky)+[`lint-staged`](https://github.com/okonet/lint-staged)，针对git的staged文件，在git hooks时期，进行lints操作（如：eslint、prettier、等）。

    >[demo](./demo)。
