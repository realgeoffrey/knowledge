# ICU与国际化（i18n）

## 目录
1. [ICU的国际化技术栈](#icu的国际化技术栈)
1. [intl-messageformat](#intl-messageformat)
1. [vue-i18n](#vue-i18n)
1. [`Intl`例子](#intl例子)
1. [翻译内容中包含HTML标签](#翻译内容中包含html标签)

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

    >Chrome (V8)、Safari (JavaScriptCore) 等浏览器引擎内部都嵌入了 ICU 库（暴露接口`Intl`）。对于前端开发者来说，ICU 和 JS 的关系其实是 “底层引擎” 和 “表层接口” 的关系。我们不需要“安装”ICU 的 JS 代码，因为我们所处的环境（浏览器或 Node.js）已经帮我们内置好了（完整的ICU代码量在百万行级别，编译后的数据包通常在20MB - 30MB）。
4.  Intl API——JS接口

    作用：浏览器提供的JS API，封装 ICU 功能。

    >调用`new Intl.DateTimeFormat()`等 API 时，底层实际调用 ICU 引擎，查询 CLDR 数据，返回格式化结果。
- intl-messageformat——封装实现

    作用：Intl API 的封装，实现 ICU MessageFormat 标准。

### [intl-messageformat](https://formatjs.github.io/docs/intl-messageformat)
是一个 JS 库，它的核心作用是解析和格式化遵循行业标准 [ICU MessageFormat](https://unicode-org.github.io/icu/userguide/format_parse/messages/) 的字符串。它主要解决的是 “如何根据变量（如：**数量、性别、状态**等）动态生成符合特定语言语法的句子” 这一难题。

>ICU MessageFormat的核心思想是将 数据逻辑 与 语言表现 分离。

1. 占位符语法

    1. 语法定界符：`{`、`}`、`'`、`#`、`<标签>`（不被逃逸标志`'`覆盖）
    1. `{key, type, format}`

        1. `key`：替换的对象属性名
        1. `type`：类型，决定如何处理该值

            1. `number`：数字格式化（依赖 CLDR 数字规则）
            1. `date`：日期格式化（依赖 CLDR 日期规则）
            1. `time`：时间格式化（依赖 CLDR 时间规则）
            1. `select`：基于值的分支选择（不依赖语言规则，完全依赖字符串匹配）
            1. `plural`：基于数量的复数规则（依赖 CLDR 复数规则）
            1. `selectordinal`：基于序数的复数规则（依赖 CLDR 序数规则）
        1. `format`：格式化选项，根据`type`不同而不同
    1. `{数字}`替换的数组下标
    1. 支持[部分 HTML/XHTML/XML 规范](https://formatjs.github.io/docs/intl-messageformat#formatvalues-method)

        1. HTML标签上的任何属性会被忽略（报错）
        2. 不支持自闭标签，其被视为字符串字面量
        3. 所有标签都必须在`format`有对应的值（否则报错）

            >e.g. `new IntlMessageFormat('我是 <em>{name1}</em>', 'en-US').format({ name1: 1, em: (chunks) => '<em>' + chunks + '</em>' })`
    >变量`{key}`里应该只放动态数据（如：人名、数字、文件名），不要放句子结构的一部分（如：动词、名词），否则句子被分割，导致语序被破坏
2. 逃逸标志`'`（以`'`结尾 或 覆盖到句子最后）

    主要转义`{`、`}`、`'`、`#`、`<标签>`。若需要输出单引号，则需要2个单引号`''`。

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

1. vue-i18n默认的消息模式：支持部分 ICU Message 格式，有自己特殊的[语法规则](https://vue-i18n.intlify.dev/guide/essentials/syntax.html)：

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
    1. 需要转义的字符`@`、`|`、`{`（转义：`{'@'}`、`{'|'}`、`{'{'}`）
    1. 不支持 HTML/XHTML/XML 规范（当做普通字符）
1. vue-i18n@9.3+的`messageCompiler`（[Custom Message Format](https://vue-i18n.intlify.dev/guide/advanced/format)）、vue-i18n@8的`formatter`（[自定义格式](https://kazupon.github.io/vue-i18n/zh/guide/formatting.html#自定义格式)）可以配置自定义消息模式，设置为ICU Message语法

### `Intl`例子
1. `Intl.ListFormat`

    列表格式化。

    >避免用`.join(固定分隔符)`。

    ```js
    function formatList (list) {
      const formatter = new Intl.ListFormat('zh-CN', { style: 'long', type: 'conjunction' });
      return formatter.format(list);
    };

    formatList(['jpg', 'png'])   // -> jpg和png
    ```
2. `Intl.Collator`

    字符串比较。
3. `Intl.DateTimeFormat`

    日期、时间格式化。
4. `Intl.DisplayNames`

    针对 `语言、地区、脚本、日历、、货币、日期时间字段` 显示名称的一致翻译。
5. `Intl.DurationFormat`

    时长格式化。
6. `Intl.NumberFormat`

    数字格式化（货币符号、百分比、科学计数法、单位）。
7. `Intl.PluralRules`

    复数格式化。
8. `Intl.RelativeTimeFormat`

    相对时间格式化。
9. `Intl.Segmenter`

    文本分割，允许将一个字符串分割成有意义的片段（字、词、句），专门用于处理像中文、日文这种没有空格分隔词语的语言。

### 翻译内容中包含HTML标签
>1. 以下用字符串`replace` 简化表示 ICU MessageFormat；假设`$t`是翻译方法
>2. 插入HTML（`innerHTML`）会导致XSS，应尽量避免
>3. 方案的关注点：①是否让翻译人员看到完整句子？②是否会破坏语言语序、是否分割完整句子？③是否会带来XSS风险？④是否会让机翻或人译误处理占位符或HTML标签？

e.g. 针对一行文字中间插入了HTML标签的情况，如：`将文件拖到此处，或<em>点击上传</em>`

<details>

<summary>几种方式分析</summary>

1. 不依赖组件库方式：

    1. ⍻XSS风险高

        1. **（直接翻译）`$t('将文件拖到此处，或<em>点击上传</em>')`**

            翻译维护性差（若需修改HTML标签内容，则会新生成需要翻译的文案）

            >若是机翻，则可能对HTML标签、占位符符号处理不好；若是经过培训的人工翻译，则能够解决翻译内容中包含HTML标签、占位符符号的情况。
    1. ×XSS风险低（还是有），但翻译质量堪忧，不能针对所有语言

        1. `$t('将文件拖到此处，或{0}点击上传{1}').解决xss().replace('{0}', '<em>').replace('{1}', '</em>')`

            占位符作为HTML标签语义不明，不适用于从右至左书写的语言
        1. `$t('将文件拖到此处，或{0}').解决xss().replace('{0}', "<em>{{ $t('点击上传') }}</em>")`

            句子被分割，语序被破坏，翻得不自然。不适用于语序变化强烈的语言
        1. `$t('将文件拖到此处，或{0}点击上传').解决xss().split('{0}')[0]` + `<em>` +`$t('将文件拖到此处，或{0}点击上传').解决xss().split('{0}')[1]` + `</em>`

            码可读性差，占位符作为分隔符语义不明。不适用于语序变化强烈的语言
    1. <details>

        <summary>AI完整方案过于复杂</summary>

        ![HTML标签翻译方案](./images/i18n.jpg)
        </details>
1. ⍻依赖组件库方式（无XSS风险，解耦翻译和结构，但写法复杂）：

    1. [react-i18next](https://github.com/i18next/react-i18next)的`<Trans>` 或 [react-intl](https://formatjs.github.io/docs/react-intl)的`<FormattedMessage>`
    2. [vue-i18n](https://github.com/intlify/vue-i18n)的`<i18n-t>`

</details>

><details>
><summary>e.g. 以Vue3的vue-i18n为例</summary>
>
>1. ⍻直接翻译包含HTML标签字符串，再innerHTML插入（可以使用[DOMPurify](https://github.com/cure53/DOMPurify)、[vue-dompurify-html](https://github.com/LeSuisse/vue-dompurify-html)降低XSS风险）：
>
>
>    ```vue
>    // 翻译内容
>    createI18n({
>      locale: 'zh',
>      messages: {
>        zh: {
>          message: {
>            welcomeHTML1: '你好，<em style="color: red;">{name1}</em>，我是 <em style="color: blue;">{name2}</em>。拉或<em>上传</em>', // × 原文中包含标签，不推荐。应该要分离内容和样式
>            welcomeHTML2: '你好，{name1}，我是 {name2}。拉或{upload}'  // ⍻ 变量`{key}`里应该只放动态数据（如：人名、数字、文件名），不要放句子结构的一部分（如：动词、名词）
>          },
>        },
>      },
>    })
>
>    <p v-dompurify-html="$t('message.welcomeHTML1', { name1: 'Jack', name2: 'Geo' })"/>
>    <p v-dompurify-html="$t('message.welcomeHTML2', { name1: `<em style='color: red;'>Jack</em>`, name2: `<em style='color: blue;'>Geo</em>`, upload: '<em>上传</em>' })"/>
>    <!-- 输出：
>      <p>你好，<em style="color: red;">Jack</em>，我是 <em style="color: blue;">Geo</em>。拉或<em>上传</em></p>
>    -->
>
>    dompurify.sanitize(t('message.welcomeHTML1', { name1: 'Jack', name2: 'Geo' }))  // 输出字符串
>    dompurify.sanitize(t('message.welcomeHTML2', { name1: `<em style='color: red;'>Jack</em>`, name2: `<em style='color: blue;'>Geo</em>`, upload: '<em>上传</em>' }))  // 输出字符串
>    ```
>2. ⎷利用`<i18n-t>`组件
>
>    ```vue
>    // 翻译内容
>    createI18n({
>      locale: 'zh',
>      messages: {
>        zh: {
>          message: {
>            welcome: '你好，{name1}，我是 {name2}。拉或{upload}',
>            upload: '上传'
>          },
>        },
>      },
>    })
>
>    <i18n-t keypath="message.welcome" tag="p"><!-- 若是Vue2的vue-i18n，则仅修改这里为`<i18n path="message.welcome" tag="p">` -->
>      <template #name1>
>        <em style="color: red;">{{ data.yourName }}</em>
>      </template>
>      <template #name2>
>        <em style="color: blue;">{{ data.myName }}</em>
>      </template>
>      <template #upload>
>        <em>{{ $t('message.upload') }}</em>
>      </template>
>    </i18n-t>
>    <!-- 输出：
>      <p>你好，<em style="color: red;">{{ data.yourName }}</em>，我是 <em style="color: blue;">{{ data.myName }}</em>。拉或<em>{{ $t('message.upload') }}</em></p>
>    -->
>    ```
></details>

- 总结（按`vue-i18n`默认的消息模式举例）：

    1. ×翻译内容包含HTML标签：XSS风险，内容和样式未分离，翻译维护性差（若需修改HTML标签内容，则会新生成需要翻译的文案）

        e.g. `你好，<em style="color: red;">{name1}</em>，我是 <em style="color: blue;">{name2}</em>。拉或<em>上传</em>`, `{ name1: 'Jack', name2: 'Geo' }`
    2. ⍻翻译内容分割句子结构：变量`{key}`里应该只放动态数据（如：人名、数字、文件名），不要放句子结构的一部分（如：动词、名词），否则句子被分割、语序被破坏

        e.g. `你好，{name1}，我是 {name2}。拉或{upload}`, `{ name1: "<em style='color: red;'>Jack</em>", name2: "<em style='color: blue;'>Geo</em>", upload: '<em>上传</em>' }`
    3. ⎷利用`<i18n-t>`等组件实现：仅支持组件展示（无法仅输出字符串），稍微麻烦一些，其他没有问题
