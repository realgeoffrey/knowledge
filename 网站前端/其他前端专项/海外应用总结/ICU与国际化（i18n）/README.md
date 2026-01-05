# ICU与国际化（i18n）

## 目录
1. [ICU的国际化技术栈](#icu的国际化技术栈)
1. [intl-messageformat](#intl-messageformat)
1. [vue-i18n](#vue-i18n)
1. [`Intl`例子](#intl例子)
1. [翻译内容中包含HTML标签](#翻译内容中包含html标签)
1. [翻译输入输出case问题](#翻译输入输出case问题)

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
        1. `type`（可选）：类型，决定如何处理该值

            1. `number`：数字格式化（依赖 CLDR 数字规则）
            1. `date`：日期格式化（依赖 CLDR 日期规则）
            1. `time`：时间格式化（依赖 CLDR 时间规则）
            1. `select`：基于值的分支选择（不依赖语言规则，完全依赖字符串匹配）
            1. `plural`：基于数量的复数规则（依赖 CLDR 复数规则）
            1. `selectordinal`：基于序数的复数规则（依赖 CLDR 序数规则）
        1. `format`（可选）：格式化选项，根据`type`不同而不同
    1. `{数字}`替换的数组下标
    1. 支持[部分 HTML/XHTML/XML 规范](https://formatjs.github.io/docs/intl-messageformat#formatvalues-method)

        1. HTML标签上的任何属性会被忽略（报错）
        2. 不支持自闭标签，其被视为字符串字面量
        3. 所有标签都必须在`format`有对应的值（否则报错）

            >e.g. `new IntlMessageFormat('我是 <em>{name1}</em>', 'en-US').format({ name1: 1, em: (chunks) => '<em>' + chunks + '</em>' })`
    >变量`{key}`里应该只放动态数据（如：人名、数字、文件名），不要放句子结构的一部分（注意：名词若不是动态数据，也是句子结构），否则句子被分割，导致语序被破坏
    >
    >1. 如何判断{key}是句子结构的一部分：①{key}需要被翻译吗？若不需要翻译则是动态数据，若需要翻译则是句子结构；②{key}能不能在不改变句子其他部分的情况下，随意替换？如会变格的名词、法语中的动词。若能随意替换则是动态数据，若替换了要修改翻译则是句子结构。
    >2. ICU 的职责是：在 message 内部，统一处理语言结构。{key} 的职责是：传入语言无关的数据。一旦 {key} 本身需要翻译 或 会导致message变化，就说明它是语言的一部分，而不是数据。
2. 逃逸标志`'`（以`'`结尾 或 覆盖到句子最后）

    主要转义`{`、`}`、`'`、`#`、`<标签>`。若需要输出单引号，则需要2个单引号`''`。

    >e.g. `...'{param1}`、`...'{param1}'`、`...'{param1}' {param2}` ：param1 都不是key

><details>
><summary>e.g. 6种可选的type</summary>
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
        // key: "值1 | 值2 | 值3" // 2个值：singular | plural。或 3个值： zero | one | other
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

    >注意：配置ICU MessageFormat后，原有的vue-i18n默认语法（如管道符`|`、`@:`引用）可能不再工作，需要统一使用ICU语法。建议在项目初期就决定使用哪种模式，避免后期迁移成本。

### `Intl`例子
1. `Intl.ListFormat`

    列表格式化，根据语言地区自动选择合适的连接词和格式。

    >避免用`.join(固定分隔符)`，因为不同语言的列表连接方式不同（中文用"和"，英文用"and"，有些语言用逗号等）。

    ```js
    function formatList (list, options) {
        const formatter = new Intl.ListFormat('zh-CN'/* 语言地区 */, {
            style: 'long',  // 'long' | 'short' | 'narrow'
            type: 'conjunction',  // 'conjunction'（和） | 'disjunction'（或） | 'unit'
            ...options
        });
        return formatter.format(list);
    };

    formatList(['jpg', 'png'])   // -> jpg和png
    ```
2. `Intl.Collator`

    字符串比较，根据语言地区的排序规则进行比较。

    ```js
    const collator = new Intl.Collator('sv'/* 语言地区 */);

    ['z', 'ö'].sort(collator.compare)  // ['z', 'ö']
    ```
3. `Intl.DateTimeFormat`

    日期、时间格式化，根据语言地区自动选择合适的格式。

    ```js
    const dateFormatter = new Intl.DateTimeFormat('zh-CN', {
        dateStyle: 'medium',  // 'full' | 'long' | 'medium' | 'short'
        timeStyle: 'short',
        timeZone: 'Asia/Shanghai'
    });

    dateFormatter.format(new Date())  // '2024年1月12日 09:52'
    ```

4. `Intl.DisplayNames`

    针对`语言、地区、脚本、日历、、货币、日期时间字段`显示名称的一致翻译。

    ```js
    const displayNames = new Intl.DisplayNames('zh-CN', { type: 'region' });

    displayNames.of('US')  // '美国'
    displayNames.of('GB')  // '英国'
    ```

5. `Intl.DurationFormat`

    时长格式化。

    ```js
    const durationFormatter = new Intl.DurationFormat('zh-CN', {
        style: 'long'
    });

    durationFormatter.format({ hours: 2, minutes: 30 })  // '2小时30分钟'
    ```

6. `Intl.NumberFormat`

    数字格式化（货币符号、百分比、科学计数法、单位）。

    ```js
    const numberFormatter = new Intl.NumberFormat('zh-CN', {
        style: 'currency',
        currency: 'CNY',
        minimumFractionDigits: 2,
        maximumFractionDigits: 2
    });

    numberFormatter.format(1000)  // '¥1,000.00'
    ```
7. `Intl.PluralRules`

    复数格式化，根据数字值返回对应的复数类别。

    ```js
    const pluralRules = new Intl.PluralRules('ru');  // 俄语

    pluralRules.select(1)   // 'one'
    pluralRules.select(2)   // 'few'
    pluralRules.select(5)   // 'many'
    ```
8. `Intl.RelativeTimeFormat`

    相对时间格式化，生成"2小时前"、"3天后"等相对时间表达。

    ```js
    const rtf = new Intl.RelativeTimeFormat('zh-CN', {
        numeric: 'auto',  // 'always' | 'auto'
        style: 'long'     // 'long' | 'short' | 'narrow'
    });

    rtf.format(-2, 'hour')  // '2小时前'
    rtf.format(3, 'day')    // '3天后'
    ```

9. `Intl.Segmenter`

    文本分割，允许将一个字符串分割成有意义的片段（字、词、句），专门用于处理像中文、日文这种没有空格分隔词语的语言。

    ```js
    const segmenter = new Intl.Segmenter('zh-CN', { granularity: 'word' });
    const segments = segmenter.segment('你好世界');

    Array.from(segments).map(s => s.segment)  // ['你好', '世界']
    ```

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
>            welcomeHTML2: '你好，{name1}，我是 {name2}。拉或{upload}'  // ⍻ 变量`{key}`里应该只放动态数据（如：人名、数字、文件名），不要放句子结构的一部分
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
    2. ⍻翻译内容分割句子结构：变量`{key}`里应该只放动态数据（如：人名、数字、文件名），不要放句子结构的一部分，否则句子被分割、语序被破坏

        e.g. `你好，{name1}，我是 {name2}。拉或{upload}`, `{ name1: "<em style='color: red;'>Jack</em>", name2: "<em style='color: blue;'>Geo</em>", upload: '<em>上传</em>' }`
    3. ⎷利用`<i18n-t>`等组件实现：仅支持组件展示（无法仅输出字符串），稍微麻烦一些，其他没有问题

### 翻译输入输出case问题
在使用 ICU MessageFormat（或类似的现代 i18n 标准）之前，开发者经常会犯一些"硬编码逻辑"的错误。这些写法最大的问题在于：它们假设了所有语言的语法结构、语序和标点习惯都和英语（或中文）一样。

1. "拼积木"式拼接

    开发者试图通过代码把词拼成句子，但**不同语言的语序不同**（主谓宾顺序）、书写顺序也不同。一句话分割后分别翻译也导致翻译**上下文丢失**。

    ```js
    // ❌ 错误示例
    const msg = $t('删除') + ' ' + itemName;    // 还有多余空格问题
    const msg2 = $t('共') + count + $t('条');   // 语序问题：阿拉伯语是"条共3"

    // ✅ 正确示例
    $t('删除{itemName}', { itemName: x })
    $t('共{count}条', { count: x })
    ```

    >解决方案：避免任何形式的拼接，将完整句子作为翻译单元。翻译时提供完整上下文，让翻译人员根据目标语言的语序调整。
2. 肢解句子

    1. 为了在句子中间插入 HTML 标签（如链接、加粗），强行把一个完整的句子切碎。

        除了导致"拼积木"式拼接问题外，还引入**XSS风险**。

        ```js
        // ❌ 错误示例
        $t('点击{action}查看详情', { action: '<a href="...">这里</a>' })  // XSS风险，语序破坏

        // ⚠️ 示例（使用ICU的HTML标签功能）
        $t('点击<action>这里</action>查看详情', { action: (chunks) => `<a href="...">${chunks}</a>` })   // 语序ok，但依然有XSS风险

        // ✅ 正确示例（使用vue-i18n的<i18n-t>组件）
        // 翻译：'点击{action}查看详情'
        // <i18n-t keypath="message.clickToView" tag="span">
        //   <template #action>
        //     <a href="...">{{$t('这里')}}</a> /* ⚠️ 这里嵌套翻译了，也有问题 */
        //   </template>
        // </i18n-t>
        ```

        >解决方案：尽量避免句子中间插入 HTML 标签，若实在无法避免，查看[翻译内容中包含HTML标签](#翻译内容中包含html标签)。

    2. 占位符不仅是动态数据，还错误地包含句子结构的一部分。

        ```js
        // ❌ 错误示例（连词不是“动态数据”，而是“句子结构”的一部分）
        $t(`{conjunction, select, when {当} and {且}}我来了`, { conjunction: 'when或and' })

        // ✅ 正确示例（若变量是句子结构的一部分，则只能包含完整句子）
        $t(`{conjunction, select,
          when {当我来了}
          and  {且我来了}
        }`, { conjunction: 'when或and' })
        // ✅ 正确示例（再包含动态数据）
        $t(`{conjunction, select,
          when {当{name}来了}
          and  {且{name}来了}
        }`, { conjunction: 'when或and', name: '雷锋' })
        ```

        >解决方案：若一旦存在`结构`变量，则翻译必须**拥有整句控制权**。
3. 嵌套翻译（在占位符中又包含翻译）

    1. **变格问题**：在很多语言（德语、俄语、波兰语、芬兰语等）中，名词的形式取决于它在句子中的位置（主语、宾语、属格等）——变格。

        ```js
        // ❌ 错误示例（俄语）
        $t('删除{fileName}', { fileName: $t('文件') })
        // 问题：俄语中"文件"作为宾语需要变格，但嵌套翻译无法处理

        // ✅ 正确示例
        $t('删除文件{fileName}', { fileName: 'document.pdf' })
        // 翻译人员可以在完整句子中正确处理变格
        ```

    2. **性别/阴阳性问题**：在法语中，"删除"(supprimé / supprimée) 这个词的拼写需要根据宾语的词性变化。

        ```js
        // ❌ 错误示例（法语）
        $t('{action}成功', { action: $t('删除') })
        // 问题：法语中"删除"需要根据宾语性别变化，但嵌套无法传递上下文

        // ✅ 正确示例
        $t('删除{fileName}成功', { fileName: 'document.pdf' })
        // 翻译人员可以在完整句子中正确处理性别变化
        ```

    >解决方案：尽量避免，改造为翻译一句完整的话。如果这个`$t()`的结果在任何语言里"可能需要改写"（变格、性别、语序等），就禁止嵌套。使用ICU的`select`处理性别等分支逻辑。
4. 硬编码标点符号

    1. 代码写死冒号，会导致英文界面出现全角冒号，或中文界面出现半角冒号，不专业。
    2. 语序：某些语言（如法语）在冒号前需要加空格。
    3. 特殊标点：西班牙语的疑问句前面有一个倒问号`¿`。

    ```js
    // ❌ 错误示例
    $t('名称') + ':' + value
    $t('确认删除') + '?'

    // ✅ 正确示例
    $t('名称：{value}', { value })
    $t('确认删除？')
    ```

    <details>
    <summary>e.g. 列表连接的多语言实现</summary>

    ```js
    function formatList (list, options) {	// formatList(['jpg', 'png'])   // -> jpg和png（取决于浏览器实现）
        const formatter = new Intl.ListFormat('zh-CN'/* 语言地区 */, { style: 'long', type: 'conjunction', ...options });
        return formatter.format(list);
    };

    $t('仅支持上传{typeList}类型文件', { typeList: formatList(typeList) })
    ```
    </details>

    >解决方案：把标点符号包含进完整的翻译句子，让翻译人员根据目标语言的标点习惯调整。或使用`Intl.ListFormat`等标准API。
5. 手动 Replace 占位符

    通过`String.prototype.replace`而非ICU的替换语法，无法处理复杂格式化需求（如：数字格式化、日期格式化、复数规则等）。

    >解决方案：改用ICU占位符语法解决。ICU支持嵌套占位符、格式化选项、复数规则等复杂场景。
6. 占位符key的命名未语义化

    ```js
    // ✅ 正确示例
    $t('你好，{cityName}', { cityName: '厦门' })
    $t('共{totalCount}条记录，已选择{selectedCount}条', { totalCount: 10, selectedCount: 3 })

    // 👎🏻 错误示例
    $t('你好，{0}', ['厦门'])                    // 数字索引不语义化
    $t('你好，{item}', { item: '厦门' })         // 通用名称不明确
    $t('共{count1}条记录，已选择{count2}条', { count1: 10, count2: 3 })  // 命名不清晰
    ```

    >解决方案：ICU的key尽量语义化，提高可读性和维护性。翻译人员也能更好地理解上下文。
7. 忽略ICU的格式化能力

    1. 不使用ICU的`number`、`date`、`time`格式化，手动处理数字、日期格式，导致格式不符合目标语言习惯。

        >解决方案：充分利用ICU的格式化能力，让数字、日期、时间格式自动适配目标语言地区。
    2. 逻辑里写复数

        1. 复杂复数规则：英语、中文仅有单复数；俄语、波兰语有 3 种复数形式（1个、2-4个、5个以上不同）；阿拉伯语有 6 种形式（零、单数、双数、3-10、11-99等）。
        2. 代码无法维护：不可能在代码里为每种语言写一套if/else。

        >解决方案：使用ICU语法`{count, plural, ...}`解决。同理，6种类型的占位符type（plural、select、number、date、time、selectordinal），都是必要的功能，未使用或自实现一套一定会有遗漏。

- 使用建议（要求）

    1. 完整句子原则：将完整句子作为翻译单元，避免拆分拼接
    2. 具名占位符：使用`{name}`而非 ~~`{0}`~~
    3. 动态数据原则：占位符只放动态数据（数字、人名、文件名等），不放句子结构
    4. 变量仅承载“数据值”，不得承载句法角色（句子结构）

        若变量用于区分句式、语序或从句结构（如 `when`、`if`、`and`、`or`），必须使用`select`ICU占位符语法，且 `select`的每个分支必须是完整、可独立翻译的句法单元。
    4. 避免嵌套：不在占位符值中调用`$t`
    5. 利用 ICU 能力：使用 plural、select、number、date、time、selectordinal 等格式
    6. HTML标签处理：使用`<i18n-t>`组件或ICU的HTML标签功能 而非字符串拼接，避免XSS风险并保持语序正确

    >核心原则：永远把一整句话作为一个翻译单元（Translation Unit），不要在代码里拆解它。充分利用ICU的格式化能力，让翻译人员专注于语言表达，而非技术实现（关注点分离）。
