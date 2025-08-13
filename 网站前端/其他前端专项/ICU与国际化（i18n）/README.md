# ICU与国际化（i18n）

## 目录
1. [ICU的国际化技术栈](#icu的国际化技术栈)
1. [intl-messageformat](#intl-messageformat)
1. [vue-i18n](#vue-i18n)

---
>ICU（International Components for Unicode）是一个庞大的底层基础库（C/C++ 和 Java），它主要致力于解决计算机如何正确处理人类语言和文化习惯这一根本问题。包含：1. 文本边界分析 (Text Boundary Analysis) / Break Iterator；2. 排序与检索 (Collation)；3. Unicode 规范化 (Normalization)；4. 音译 (Transliteration)；5. 双向文本算法 (BiDi / Bidi Algorithm)；6. 复杂的日期/数字/列表格式化；7. 多语言文案替换、消息格式化（Message Formatting）。


### [ICU](https://github.com/unicode-org/icu)的国际化技术栈
国际化技术栈的四个层次（自底向上）：

1.  Unicode——字符标准

    作用：定义字符集和编码规则。为世界上几乎所有的字符（中文、Emoji、拉丁文等）分配唯一的码点（Code Point）。只规定字符是什么，不规定如何使用。
2.  CLDR（Common Locale Data Repository）——本地化数据

    作用：提供各语言地区的文化习惯数据（XML 格式）。例如：日期格式（美国`MM/DD/YYYY`，英国`DD/MM/YYYY`）、数字格式（中文用`万`，英文用`Million`）、复数规则等。
3.  ICU（International Components for Unicode）——核心引擎

    定义：它是 C++ 和 Java 的库。ICU 使用 Unicode 的字符，查询 CLDR 的数据，然后通过复杂的算法计算出结果。它是真正干活的代码库。

    >Chrome (V8)、Safari (JavaScriptCore) 等浏览器引擎内部都嵌入了 ICU 库（暴露接口`Intl`）。对于前端开发者来说，ICU 和 JS 的关系其实是 “底层引擎” 和 “表层接口” 的关系。我们不需要“安装”ICU 的 JS 代码，因为我们所处的环境（浏览器或 Node.js）已经帮我们内置好了。
4.  Intl API——JS接口

    作用：浏览器提供的JS API，封装 ICU 功能。

    >调用`new Intl.DateTimeFormat()`等 API 时，底层实际调用 ICU 引擎，查询 CLDR 数据，返回格式化结果。
5. intl-messageformat——封装实现

    作用：Intl API 的封装，实现 ICU MessageFormat 标准

### [intl-messageformat](https://formatjs.github.io/docs/intl-messageformat)
是一个 JS 库，它的核心作用是解析和格式化遵循行业标准 [ICU MessageFormat](https://unicode-org.github.io/icu/userguide/format_parse/messages/) 的字符串。它主要解决的是 “如何根据变量（如：**数量、性别、状态**等）动态生成符合特定语言语法的句子” 这一难题。

>ICU MessageFormat的核心思想是将数据逻辑与语言表现分离。应用程序提供数据（上下文变量），而 MessageFormat 模板字符串（Pattern String）则封装了如何根据这些数据生成最终用户可见文本的逻辑。

1. 占位符语法

    1. 语法定界符：`{`、`}`（不被逃逸标志`'`覆盖）（、`'`、`#`）
    1. `{key, type, format}`

        1. `key`：替换的对象属性名
        1. `type`：类型，决定如何处理该值

            1. `number`：数字格式化（依赖 CLDR 数字规则）
            1. `date`：日期格式化（依赖 CLDR 日期规则）
            1. `time`：时间格式化（依赖 CLDR 时间规则）
            1. `select`：基于值的分支选择（不依赖语言规则）
            1. `plural`：基于数量的复数规则（依赖 CLDR 复数规则）
            1. `selectordinal`：基于序数的复数规则（依赖 CLDR 序数规则）
        1. `format`：格式化选项，根据`type`不同而不同
    1. `{数字}`替换的数组下标
2. 逃逸标志`'`（以`'`结尾 或 覆盖到句子最后）

    主要转义`{`、`}`、`'`、`#`。若需要输出单引号，则需要2个单引号`''`。

    >e.g. `...'{param1}`、`...'{param1}'`、`...'{param1}' {param2}` ：param1 都不是key

><details>
><summary>e.g. </summary>
>
>>可以使用<https://devpal.co/icu-message-editor/>测试。
>
>1. number
>
>    [Number Skeletons](https://unicode-org.github.io/icu/userguide/format_parse/numbers/skeletons.html)（数字骨架）
>
>    格式化结果随语言地区变化。
>
>    ```js
>    new IntlMessageFormat(
>      `Almost {pctBlack, number, ::percent} of them are black.`,
>      '语言地区'
>    ).format({pctBlack: 1000})
>    // -> 'Almost 100,000% of them are black.'
>    ```
>
>    ```js
>    new IntlMessageFormat(
>      `The price of this bagel is {num, number, ::sign-always compact-short currency/GBP}`,
>      '语言地区'
>    ).format({num: 1000})
>    // -> 'The price of this bagel is +£1000'
>    ```
>2. date
>
>    使用预定义格式（`short`、`medium`、`long`、`full`）或自定义格式。
>
>    格式化结果随语言地区变化。
>
>    ```js
>    new IntlMessageFormat(
>      `Sale begins {start, date, medium}`,
>      '语言地区'
>    ).format({start: 1705024329653})
>    // -> 'Sale begins 2024年1月12日'
>    ```
>3. time
>
>    使用预定义格式（`short`、`medium`、`long`、`full`）或自定义格式。
>
>    格式化结果随语言地区变化。
>
>    ```js
>    new IntlMessageFormat(
>      `Coupon expires at {expire, time, short}`,
>      '语言地区'
>    ).format({expire: 1705024329653})
>    // -> 'Coupon expires at 09:52'
>    ```
>4. select
>
>    根据变量值精确匹配分支（如`male`、`female`、`yes`、`no`）。不依赖语言规则，所有语言地区使用相同的分支逻辑。
>
>    分支输出可以是字面字符串，也可以嵌套其他占位符。
>
>    ```yaml
>    # messages_zh.yaml
>    friend_add_image: >
>        您好，您的朋友{friend}现在在线。
>        {gender, select,
>        female {她}
>        male {他}
>        other {他们}}
>        向系统添加了新映像。
>    ```
>
>    ```js
>    format('friend_add_image', { friend: 'Ann', gender: 'female' });
>    ```
>
>    ```js
>    new IntlMessageFormat(
>      `Hello. {gender, select,
>      male {He will respond shortly.}
>      female {She will respond shortly.}
>      other {They will respond shortly.}
>      }`,
>      '语言地区'
>    ).format({gender: 'male'})
>    // -> 'Hello. He will respond shortly.'
>    ```
>
>    ```js
>    // 嵌套参数
>    new IntlMessageFormat(
>      `嵌套信息。{isTaxed, select,
>      yes {An additional {tax, number, percent} tax will be collected.}
>      other {No taxes apply.}
>      }`,
>      '语言地区'
>    ).format({isTaxed: "yes", tax: 0.4})
>    // -> '嵌套信息。An additional 40% tax will be collected.'
>    ```
>5. plural
>
>    根据数字值，使用 CLDR 定义的复数规则选择分支。依赖语言规则，不同语言地区对同一数字可能选择不同分支。e.g. `en`：1->one，其他->other；`zh`：所有->other。
>
>    分支输出可以是字面字符串，也可以嵌套其他占位符。
>
>    `zero`、`one`、`two`、`few`、`many`、`other`（必须）、`=value`（`=value`是精确匹配，优先级最高；`one`等，是CLDR匹配）
>
>    在分支输出中，`#`表示原始数字值的占位符。
>
>    `offset`减去逻辑。
>
>    ```js
>    new IntlMessageFormat(
>      `{numPhotos, plural,
>          =0 {You have no photos.}
>          one {You have one photo.}
>          other {You have # photos.}
>        }`,
>      'en-US'
>    ).format({numPhotos: 1}) // 若是中文，则都会跑到other分支
>    // -> 'You have one photo.'
>    ```
>
>    ```text
>    { count, plural, offset:1
>      =0 {没有人点赞}
>      =1 {你点赞了}
>      one {你和另外 # 人点赞了}
>      other {你和另外 # 个人点赞了}
>    }
>    // 若count传入4：
>    // 1. 首先检查精确匹配（=4）。此时使用的是原始值。
>    // 2. 若没有精确匹配，则从原始值中减去 offset，使用减去后的值来查找 CLDR 类别（one, few, other）。
>    // - 在子消息中，# 代表的是减去后的值（无论是否精确匹配）。
>    // 则输出：你和另外 3 个人点赞了
>    ```
>6. selectordinal
>
>    根据数字值，使用 CLDR 定义的序数规则选择分支（用于生成 1st、2nd、3rd 等序数形式）。依赖语言规则，不同语言地区对同一数字可能选择不同分支。e.g. `en`：1->one，2->two，3->few，其他->other；`zh`：所有->other。
>
>    分支输出可以是字面字符串，也可以嵌套其他占位符。
>
>    `zero`、`one`、`two`、`few`、`many`、`other`（必须）、`=value`（`=value`是精确匹配，优先级最高；`one`等，是CLDR匹配）
>
>    在分支输出中，`#`表示原始数字值的占位符。
>
>    ```js
>    new IntlMessageFormat(
>      `It's my cat's {year, selectordinal,
>        one {#st}
>        two {#nd}
>        few {#rd}
>        other {#th}
>      } birthday!`,
>      'en-US'
>    ).format({year: 1})  // 若是中文，则都会跑到other分支
>    // -> 'It's my cat's 1st birthday!'
>    ```
></details>

3. 库关系

    1. `@formatjs/icu-messageformat-parser`（底层解析器）

        功能：将 ICU Message 字符串解析为抽象语法树（AST）。

        使用场景：库开发者使用，普通开发者无需直接使用。

    2. `intl-messageformat`（核心引擎）

        依赖：`@formatjs/icu-messageformat-parser`

        功能：基于 AST，结合变量数据和格式化规则，生成最终字符串。

        使用场景：纯 JS（无前端框架） 或 Node.js 环境。

    3. `@formatjs/intl`（统一 API 层）

        依赖：`intl-messageformat`

        功能：封装`intl-messageformat`，提供统一的国际化 API（日期、时间、数字、相对时间等）。

        使用场景：非 React 框架（Angular、Svelte、原生 JS）。

    4. `react-intl`（React 适配器）

        依赖：`@formatjs/intl`

        功能：将国际化功能封装为 React 组件（`<FormattedMessage />`）和 Hooks（`useIntl`），处理 Context 传递和重新渲染。

        使用场景：React 项目。

    5. ~~`vue-intl`~~（已废弃）

        说明：FormatJS 团队早期维护的 Vue 适配器，主要用于 Vue 2。Vue 生态更主流的选择是`vue-i18n`（与 FormatJS 无关）。

### vue-i18n
[vue-i18n@8（for Vue 2）](https://github.com/kazupon/vue-i18n)、[vue-i18n@latest（for Vue 3）](https://github.com/intlify/vue-i18n)

1. vue-i18n默认的消息模式：支持部分 ICU Message 格式，有自己特殊的[语法规则](https://vue-i18n.intlify.dev/guide/essentials/syntax.html)

    1. plural

        管道符`|`

        ```js
        // key: "值1 | 值2 | 值3" // singular | plural 或 zero | one | other
        $t('key', 0) // -> 值1
        $t('key', 1) // -> 值2
        $t('key', 5) // -> 值3
        ```
    1. 变量插入

        （除了也支持`{key}`、`{0}`之外，还）支持`@:其他key`专用引用语法（转义：`{'@'}`）
    1. 不支持 ~~select~~、~~selectordinal~~
    1. 只有`{key}`写法，没有 ~~`{key,type,format}`~~ 写法
    1. `'`没有~~逃逸效果~~
    1. 需要转义的字符`@`、`|`、`{`、`$`（转义：`{'@'}`、`{'|'}`、`{'{'}`、`{'$'}`）
2. vue-i18n@9.3+的`messageCompiler`（[Custom Message Format](https://vue-i18n.intlfy.dev/guide/advanced/format)）、vue-i18n@8的`formatter`（[自定义格式](https://kazupon.github.io/vue-i18n/zh/guide/formatting.html#自定义格式)）可以配置自定义消息模式，设置为ICU Message语法
