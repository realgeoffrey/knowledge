# 海外应用总结

## 目录
1. [语言问题（翻译）](#语言问题翻译)
1. [书写顺序](#书写顺序)
1. [翻译系统](#翻译系统)
1. [其他](#其他)
1. [多时区](./多时区/README.md)
1. [ICU与国际化（i18n）](<./ICU与国际化（i18n）/README.md>)

---
### 语言问题（翻译）
1. 文字长短不一、文字高度不一
2. 书写顺序，`ltr`、`rtl`（整个界面布局习惯跟随书写顺序变化，关注用户交互体验）
3. 时间问题：日期显示，时区（偏移量），历法

    >[dayjs](https://github.com/iamkun/dayjs)
4. 数字标点（如：小数分隔符，千位分隔符）
5. 货币单位
6. 字符集
7. 复数规则（zero、one、two、few、many、other）

    >[js-lingui](https://github.com/lingui/js-lingui)
8. 性别问题
9. 序数（1st、2nd、3rd、4th、等）
10. 安全性和敏感性（文化、宗教与民族、地缘政治、节日、手势含义、当地法律法规、颜色含义、数字忌讳）

    >注意，是某地区的所有语言都需要过滤处理。e.g. taiwan地区的简体、繁体、英文，都需要把“国家”替换成“地区”；其他地区的简体、繁体、英文，都不做替换。
11. 词汇的上下文（如：某一个词汇有多重含义）、大小写含义变化的词

| 问题领域 | [ICU](https://github.com/unicode-org/icu)能解决吗？ | 解决方案/备注 |
| :--- | :--- | :--- |
| 日期/时间/时区/历法 | ✅ 完美 | "DateFormat, TimeZone, Calendar" |
| 数字/货币/百分比 | ✅ 完美 | "NumberFormat, Currency" |
| 复数规则/序数 | ✅ 完美 | "PluralRules, MessageFormat" |
| 字符集 | ✅ 完美 | Unicode 支持 |
| 语法性别 (文本内) | ✅ 完美 | MessageFormat (select) |
| 文字长度/高度 | ❌ 不能 | 靠 CSS 弹性布局、UI 设计规范 |
| 书写顺序 (RTL) | ⚠️ 仅数据 | ICU 提供算法，CSS 负责界面翻转 |
| 政治/地缘敏感词 | ❌ 不能 | 靠内容审查、CMS 术语表、自定义业务逻辑 |
| 颜色/禁忌/法律 | ❌ 不能 | 靠设计系统 (Design System) 和 法务合规 |

>[ICU与国际化（i18n）](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/其他前端专项/海外应用总结/ICU与国际化（i18n）/README.md)

### 书写顺序
>阿拉伯文、希伯来文，波斯文 等从右至左的语言文字。

0. HTML全局设置整个DOM

    >功能有限，很多样式问题无法处理到，如：`float`、绝对定位布局，更复杂的一些布局。

    `<html dir="ltr或rtl">`或`html{ direction: ltr或rtl; }`（该属性指定了块的基本书写方向，以及针对 Unicode 双向算法的嵌入和覆盖方向）
1. CSS设置左右翻转（镜像）

    1. 父级整体：`transform: scaleX(-1)`
    2. 子级的文字、某些图标等，再翻转回去：`transform: scaleX(-1)`、`text-align: right`

        可以写一个组件，包裹需要翻转回去的节点。

    ```html
    <!-- e.g. 利用 transform 实现全局镜像（左右颠倒） -->
    <div style="transform: scaleX(-1)">
      <!-- 文字向右对齐，重置镜像 -->
      <p style="transform: scaleX(-1); text-align: right;">
        居右 على الرغم من أن لديه بعض الصعوبات على سبيل المثال
        <br>، بعض الرجل يمكن أن مجرد فتح devtools وإزالة أو تغيير قسم
        'لانغ'. لمنع هذا ، أوصي بوضعه في المتغير.
        </Text>
        </View>
      </p>

      <!-- 镜像（左右颠倒） -->
      <div>
        镜像的内容123
      </div>
    </div>
    ```

    >具体参考：[苹果指南](https://developer.apple.com/cn/design/human-interface-guidelines/right-to-left)、[Material Design 指南](https://www.mdui.org/design/usability/bidirectionality.html)、[微软指南](https://learn.microsoft.com/zh-cn/windows/apps/design/globalizing/design-for-bidi-text)。
2. 劫持创建虚拟DOM的函数，对样式统一镜像修改

    >若是RN等，则可以考虑这一块由客户端SDK完成。

    如：`left/right`、`margin左右`、`padding左右`、`border左右`、`borderRadius左右`等颠倒，flex项的几个CSS属性起始方向`flex-start`和`flex-end`颠倒（实现`direction: rtl;`设置后的默认效果）。类似：[rtlcss](https://github.com/MohammadYounes/rtlcss)。

    >`margin`改成`margin-inline`，`padding`改成`padding-inline`等，TODO

    ```js
    // e.g. React中重写`React.createElement`
    const oldCreateElement = React.createElement;

    export default function rtlReactHook() {
      if (!React._rtlHooked) {
        React.createElement = (type, props) => {
          if (isRtl) {
            // RTL样式统一镜像处理
            props.style = getRTLStyle(props.style);
          }
          return oldCreateElement.apply(null, arguments);
        };
        React._rtlHooked = true;
      }
    }
    ```
3. 细节注意

    1. 动画、绝对定位的数值是否考虑取负值
    2. 方向敏感的图标考虑是否翻转（在RTL下，箭头向右表示后退，向左表示前进），图标库需要重新设计
    3. 留意文字长度（如：阿拉伯文أَبْجَدِيَّة عَرَبِيَّة宽度较长）、留意文字高度（如：泰文อักษรไทย高度较高）

        >有点类似兼容颜文字。

        - 针对文字高度问题，解决方案：

            1. 不要写死`line-height`或`height`（或用`min-height`替代），让高的字体文字自动撑开。

                >无法按照UI设计的确定高度展示，因此处理比较粗糙。
            2. 针对特定的语言（如：泰文），设置更高的行高 或 计算dom.scrollHeight（渲染后的内容高度）大于dom.offsetHeight（设置高度、容器高度）就增加行高。

                - 进阶：先找到font-size和渲染高度的关系（如：确定泰文[音标]影响高度的细节和对应关系），再用上面的进行兜底。
- 双向文本（Bi-directional text）混排问题

    当LTR文、RTL文混在一起时，要解决文字书写顺序问题。最常用来处理双向文字的算法叫做Unicode 双向算法（[Unicode Bidirectional Algorithm](https://unicode.org/reports/tr9/)，Bidi算法）：文字的逻辑顺序（内存中的存储顺序）与显示顺序不是同一个方向。

    - unicode 定义来三种类型的字符，

        1. 强类型：大部分字符，方向确定，并且会影响前后字符的方向性。（ltr 的中英、rtl 的阿拉伯语）
        2. 弱类型：数字和数字相关的符号，方向确定，但不会影响前后字符的方向性。
        3. 中性字符：大部分的标点符号和空格，方向不确定，由上下文的bidi属性来决定其方向。

    ```text
    ar 1 times

    1 ar times // error

    // 强转换 ltr Mark
    U+200E
    ar &lrm; 1 times

    // U+202B direction rtl

    // 隔离 Isolate,避免受到其他字符影响
    // <bdi>
    &#x2066; ar &#x2069; 1 times

    // 覆盖 Override 展示内存方向
    // <bdo>
    // 强制将字符按内存顺序从左向右展示
    &#x202d; ar 1 times
    ```

### 翻译系统
>**国家/地区**：构建时、运行时都区分；**语言**：运行时替换。一个国家/地区 绑定 多个语言（App内的 语言 可以切换，国家/地区 不可以切换。国家/地区 在下载App时确定）。

1. 构建时，通过翻译系统的接口，拉取带翻译的.json文件到本地。
2. 开发时，用文本id（可以直接用文本内容）填入代码，展示时会被替换成翻译好的内容

    >语言包从代码中解藕，代码中只有翻译词条的引用id（id也可以语义化）。

    1. ~~方案一~~

        代码中提取待翻译词条，整理成资源文件或上传翻译平台，翻译完成后，最后下载到应用中。

        >最原始的：.excel搜集整理词条，传递给翻译人员，翻译完毕后再填写.excel内容到代码。
    2. 方案二

        1. 先由需求方总结出所有需要用到的翻译词条，并在翻译平台录入；
        2. 开发人员创建id指向翻译词条，再把各id填入代码业务位置，翻译人员并行在翻译平台逐条翻译词条。

        >优点：开发和翻译流程可以**并行**。缺点：需要和需求方进行词条的沟通，翻译的词条格式不可控（要求：需要需求方了解翻译的格式，或舍弃掉复数、性别等翻译，只实现最基本的变量替换翻译，或像i18next那样，单数和复数的词条分开翻译）。

    >- 翻译系统细节
    >
    >    1. 各角色权限划分：
    >
    >        开发仅关注引用翻译词条的id录入代码、构建、发布、验证；产品/运营仅关注词条罗列到翻译平台、审核角色权限等；翻译人员仅关注词条翻译。
    >    2. 支持词条的复用：
    >
    >        翻译词条 <-多对多-> 页面（需求）
    >    3. 审核词条、翻译机制；敏感词自动化校验
    >    4. 按项目（APP）区分权限，按页面区分权限
    >    5. 不同平台、语言的占位符校验、替换
3. 运行时热更新

    >旧的语言包都随着包发布，作为任何情况的兜底；新的语言包热更新。

    支持APP或H5发版之后，在运行时更新翻译结果（时机，如：重启APP或切换语言等），不需要重新安装APP或重新构建H5。

- 按国家/地区

    1. 构建时生成 根据文件后缀区分国家/地区 的代码文件，如：`.th.tsx/scss/js`

        >id->Indonesia、ms->Malaysia、th->Thailand、ph->Philippines、vi->Vietnam、me->Middle East。

        语言包可以都打包在一起（一般也不会很大）。
    2. 构建时、运行时，通过读取App环境变量（国家/地区或语言），根据代码if-else处理不同国家/地区逻辑

### 其他
1. 海外资源CDN加速，如：<https://www.akamai.com>

    >使用CDN可以显著提升海外用户的访问速度，减少延迟。建议根据目标地区选择合适的CDN服务商。

2. 海外支付体系的建设

    >不同地区有不同的支付习惯，需要接入当地主流的支付方式。如：东南亚的GrabPay、GoPay，欧洲的SEPA，中东的Mada等。
3. 合规性要求

    >不同地区有不同的法律法规要求，如：GDPR（欧盟）、CCPA（加州）、PDPA（新加坡）等。需要确保数据处理、用户隐私保护符合当地法规。
4. 网络环境适配

    >不同地区的网络环境差异较大，需要考虑：

    - 弱网环境下的加载优化
    - 数据压缩和缓存策略
    - 离线功能支持
    - 渐进式加载（Progressive Loading）
5. 性能监控

    >建立针对不同地区的性能监控体系，关注：

    - 页面加载时间
    - API响应时间
    - 错误率统计
    - 用户行为分析
