# Python学习笔记

## 目录
1. [核心软件](#核心软件)
1. [语法](#语法)
1. [数据类型](#数据类型)
1. [The Zen of Python（Python之禅）](#the-zen-of-pythonpython之禅)
1. [网络数据采集](#网络数据采集)

---
### 核心软件
1. [conda](https://github.com/conda/conda)

    环境、系统包管理器
2. pip

    python包管理器

>使用方式：
>
>1. 首先，为项目安装conda、配置conda环境，然后从conda channel（存放软件包的远程服务器地址）安装需要的所有软件包
>2. 其次，在激活conda的情况下，使用conda附带的pip来安装所需的pip依赖项到项目的conda环境中
>- 建议能用conda安装的优先使用conda，尽量使用conda环境隔离功能，为不同的任务创建不同的环境。如果某个包conda没有，再使用pip安装
>
><details>
><summary>某答案总结的优先级规则</summary>
>
>```py
>def choose_installer(package_name):
>    """选择用pip还是conda"""
>
>    # 科学计算包 -> conda
>    if package_name in ['numpy', 'scipy', 'pandas', 'matplotlib', 'scikit-learn', 'tensorflow', 'pytorch', 'faiss']:
>        return 'conda'
>
>    # 有C/C++扩展 -> conda
>    if has_c_extensions(package_name):
>        return 'conda'
>
>    # 纯Python包 -> pip
>    if is_pure_python(package_name):
>        return 'pip'
>
>    # 不确定 -> 先试conda，没有再用pip
>    return 'conda_then_pip'
>```
></details>
>
>[知乎：pip install 和conda install有什么区别吗？](https://www.zhihu.com/question/395145313)

### 语法
1. 单引号`'`与双引号`"`同时支持，相同效果
1. 范围相关的都遵循：左闭右开，支持步长
1. 换行 或 分号`;`表示语句结束
1. 注释

    1. `#`单行注释
    2. `""" """`或`''' '''`多行注释
1. 变量

    1. <details>

        <summary>变量名通常使用小写英文字母，多个单词用下划线<code>_</code>进行连接</summary>

        Python 变量名规则：

        1. 变量名只能包含字母数字字符和下划线（A-z、0-9 和 _ ）
        1. 变量名必须以字母或下划线字符开头、不能以数字开头
        1. 变量名区分大小写（firstname、Firstname、FirstName 和 FIRSTNAME 是不同的变量）
        </details>
    1. 变量关键字

        1. `global`

            在函数内部声明或定义全局变量（模块级别的变量），要么直接使用现有的全局作用域的变量，要么定义一个变量放到全局作用域。
        2. `nonlocal`

            声明使用嵌套作用域的变量（嵌套作用域必须存在该变量，否则报错）。

        - 最佳实践建议

            1. 尽量避免使用`global`——全局变量会使代码难以维护和理解
            2. ​优先使用函数参数和返回值​——比修改外部变量更清晰
            3. 必要时使用`nonlocal`​——在闭包等场景下是合理的选择

                >类似于JS，Python允许嵌套函数访问外部封闭函数的作用域。 这称为闭包。
            4. ​变量命名要明确​——特别是全局变量，可以用`G_`前缀等标识
1. `del 变量或项`

    删除变量
1. 与JS不同的运算符、语法：

    `:=`（`print`、`if`、`while`等既能输出又能赋值）、`==`、`!=`、`not`（非）、`or`（或）、`and`（且）、`//`（整除）、`is`（是变量相等）、`is not`、`in`（包含）、`not in`、`*变量`（可变参数——元组）、`**变量`（可变参数——字典）
1. `if 「条件」:`（没有小括号 ~~`()`~~ ）、`elif 「条件」:`、`else:`

    2. 支持`值1 <= 变量 < 值2`
1. `for key, value in 列表或元组或集合或字符串或字典或range(参数):`

    `for _ in xx:`不使用索引
1. `for-else`

    若`for`语句未执行到`break`，则执行`else`

    ```py
    for iterator in range(start, end, step):
        do something
    else:
        print('若for内部未执行到 break 则执行')
    ```
1. `pass`不执行任何代码，占位符
1. for、if等可以放在表达式中

    >`for`、`if`、`三元运算`看做是一个断句。

    ```py
    items = [i for i in range(1, 10)]   # [1, 2, 3, 4, 5, 6, 7, 8, 9]
    items = [i for i in range(1, 10) if i % 3 == 0 or i % 5 == 0] # [3, 5, 6, 9]
    items = [i ** 2 for i in range(1, 10) if i % 3 == 0 or i % 5 == 0] # [9, 25, 36, 81]
    # 运行顺序：for -> if -> 产出的i进行 i ** 2计算

    items = [str(i)+'是偶数' if i%2==0 else str(i)+'是奇数' for i in range(1, 10) if i % 3 == 0 or i % 5 == 0] # ['3是奇数', '5是奇数', '6是偶数', '9是奇数']
    # 运行顺序：for -> if -> 产出的i进行 三元运算

    prices = {
        'AAPL': 191.88,
        'GOOG': 1186.96,
        'IBM': 149.24,
        'ORCL': 48.44,
        'ACN': 166.89,
        'FB': 208.09,
        'SYMC': 21.29
    }
    # 用股票价格大于100元的股票构造一个新的字典
    prices2 = {key: value for key, value in prices.items() if value > 100}

    # 支持三元运算符表达式： 值1 if 条件表达式 else 值2
    num = 2
    a = '偶数' if num%2==0 else '奇数'
    b = f'{'偶数' if num%2==0 else '奇数'}'
    ```
1. `break`、`continue`仅针对当前循环
1. Python中没有用花括号 ~~`{}`~~ 来构造代码块，而是使用**缩进**的方式来表示代码的层次结构

    1. 缩进仅在每行代码开头有要求（非开头的空格缩进 多余或缺少都不会报错）
    2. 缩进数量无所谓，1或更多空格都可以
    3. 相同层级的代码（同一个父级层级下的才算相同层级），缩进数量必须一致
    4. 非相同层级的代码，缩进数量不需要一致
1. `match-case`

    1. `case 值1 | 值2 | 值3:`
    2. `case _:`默认匹配
1. [内置函数](https://docs.python.org/zh-cn/3/library/functions.html)：不需要 ~~`import`~~ 就能够直接使用的函数

    >内置函数不是~~保留字或关键字~~，可以被赋值覆盖。查看保留字或关键字：`help('keywords')`。

    1. `input(「描述值或变量」)`

        >e.g. `import math; print(int(input('输出半径，输出周长：')) * 2 * math.pi)`
    1. `print`

        1. `print(值或变量)`
        2. `print(变量 := 10)`既能输出又能赋值（~~`print(变量 = 10)`~~ 报错）
        3. `print(f'\033[样式;前景色;背景色m内容...\033[0m')`

            >1. 前景色：30（黑）、31（红）、32（绿）、33（黄）、34（蓝）等。
            >2. 背景色：40（黑）、41（红）、42（绿）等。
            >3. 样式：0（默认）、1（加粗）、4（下划线）。

            控制输出内容的颜色
    1. `type(变量名或值)`检查类型
    1. `range(多个参数)`产生整数序列

        1. `range(101)`：可以用来产生0到100范围的整数，需要注意的是取不到101
        2. `range(1, 101)`：可以用来产生1到100范围的整数，相当于是**左闭右开**的设定，即[1, 101)
        3. `range(1, 101, 2)`：可以用来产生1到100的奇数，其中2是步长（跨度），即每次递增的值，101取不到
        4. `range(100, 0, -2)`：可以用来产生100到1的偶数，其中-2是步长（跨度），即每次递减的值，0取不到
    1. `len(列表或元组或字符串或序列或集合或字典等)`
    1. `list()`将其他序列变成列表
    1. `dict()`
    1. `id()`
    1. `hash(hashable类型)`

        >传递`unhashable`会报错。
    1. `open`
    1. `zip`
    1. `isinstance(值, 类型)`
1. 需要`import`才能使用的内置模块

    `math`、`random`、`string`、`operator`、`functools`、`time`、`enum`、`json`、`csv`、`re`、`heapq`、`itertools`、`collections`、`threading`、`abc`、`gc`、`glob`、`os`、`concurrent`、`asyncio`、`lxml`
1. `import math`（仅导入了`math`）、`import math as m`（仅导入了`m`）、`from math import factorial`（仅导入了`factorial`）、`from math import factorial as f`（仅导入了`f`）

    1. 同名的后导入 覆盖 同名的前导入
    2. 可以在非顶层结构中导入，导入的变量不会 ~~“提升”到外层作用域~~
    3. `,`可以一个语句导入多个变量：`import a, b`、`import a as A, b as B`、`from a import x1, x2`、`from a import x1 as A1, x2 as A2`
1. 异常处理`try`、`except`、`else`、`finally`、`raise`

    ```py
    file = None
    try:
        file = open('致橡树.txt', 'r', encoding='utf-8')
        print(file.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError as err:
        print(f'读取文件时解码错误! {err}')
    except:
        print('其他异常')
    else:
        print('没有异常')
    finally:
        if file:
            file.close()

    raise BaseException('手动抛出异常')
    ```
1. `with`

    用于上下文管理的语法结构，它简化了资源管理（如：文件操作、数据库连接、线程锁、等）的代码，确保资源被正确释放。

    ```py
    with expression [as variable]:
        # with 代码块
        # 在这里使用资源
    # 离开代码块后自动清理资源
    ```
1. 迭代器、生成器

    1. `__iter__`、`__next__`魔术方法就是迭代器协议。
    2. 生成器是语法简化版的迭代器。`yield`
    3. 生成器进化为协程

        生成器对象可以使用`send()`方法发送数据，发送的数据会成为生成器函数中通过`yield`表达式获得的值。
1. 并发编程：多线程、多进程、异步I/O

### 数据类型
1. 整型`int`

    `0b100 == 4`、`0o100 == 64`、`0x100 == 256`
1. 浮点型`float`

    `123.456 == 1.23456e2`
1. 字符串型`str`

    单引号、双引号，`'''`或`"""`支持换行字符串（`\n`可以用回车换行表示）

    1. `r'字符串'`或`R'字符串'`（也支持`'''`或`"""`）：原始字符串、不会转义（不需要用`\`处理会转义的符号）

        ```py
        print("Hello,\nworld")
        # Hello,
        # world

        print(r"Hello,\nworld")
        # Hello,\nworld

        print(r"""Hello,
        \nworld""")
        # Hello,
        #\nworld
        ```

        主要用于正则表达式。e.g. `import re; print(re.match(r'^[0-9a-zA-Z_]{6,20}$', input('请输入用户名: ')))`
    1. `str()`
    1. 字符串`%`变量：`'浮点数%f' % 变量1`、`'浮点数%.1f 整数%d 字符串%s' % (变量1, 变量2, 变量3)`（占位符`%s`、`%f`、`%.数f`）

        >v2.0-
    1. `字符串.format(顺序传值、索引传值、关键字传值)`或`str.format(字符串, 传值)`（占位符`{}`）

        >v2.6+、v3.0+
    1. f-strings：`f'{变量1}  {变量2:.2f} {变量3 = }'`（格式化`{变量 规则}`）

        >v3.6+

        1. 同时输出变量名：`f'{变量 = }'`
        2. <details>

            <summary>格式化规则：<code>f'{变量 : 格式化规则}'</code></summary>

            | 格式代码| 作用 | 举例代码 | 输出 |
            | ------ | ------ | ------ | ------ |
            | `{变量}` | 绑定变量到输出中 | `age = 18; f'{age}'` | `18` |
            | `{变量:+}` | 正负号 | `num = -18; f'{num:+}'` | `-18` |
            | `{变量:.nf}` | 小数点后保留 n 位 | `price = 123.456; f'{price:.2f}'` | `123.46` |
            | `{变量:<n}` | 左对齐，宽度为 n | `age = 18; f'{age:<10}'` | `18        ` |
            | `{变量:>n}` | 右对齐，宽度为 n | `age = 18; f'{age:>10}'` | `        18` |
            | `{变量:^n}` | 居中对齐，宽度为 n | `age = 18; f'{age:^10}'` | `    18    ` |
            | `{变量:字符^n}` | 居中对齐（^、<、>同理），宽度为 n，用字符补齐 | `age = 18; f'{age:x^10}'` | `xxxx18xxxx` |
            | `{变量:d}` | 以整数输出 | `age = 18; f'{age:d}'` | `18` |
            | `{变量:x}` | 以16进制输出（小写） | `age = 18; f'{age:x}'` | `12` |
            | `{变量:X}` | 以16进制输出（大写） | `age = 18; f'{age:X}'` | `12` |
            | `{变量:b}` | 以2进制输出 | `age = 18; f'{age:b}'` | `10010` |
            | `{变量:e}` | 以科学记数法输出（小写 e） | `price = 123.456; f'{price:e}'` | `1.234560e+02` |
            | `{变量:E}` | 以科学记数法输出（大写 E） | `price = 123.456; f'{price:E}'` | `1.234560E+02` |
            | `{变量:,}` | 每三位数添加逗號分隔 | `price = 12345.67; f'{price:,}'` | `12,345.67` |
            | `{变量:%}` | 以百分数输出（乘100） | `rate = 0.1234; f'{rate:%}'` | `12.340000%` |
            | `{变量:.n%}` | 以百分数输出（乘100），保留n位小数 | `rate = 0.1234; f'{rate:.1%}'` | `12.3%` |
            | `{变量:#x}` | 以16进制输出（包括“0x”前缀） | `age = 18; f'{age:#x}'` | `0x12` |
            | `{变量:#o}` | 以8进制输出（包括“0o”前缀） | `age = 18; f'{age:#o}'` | `0o22` |
            | `{变量:#b}` | 以2进制输出（包括“0b”前缀） | `age = 18; f'{age:#b}'` | `0b10010` |

            可以互相组合使用。
            </details>
1. 布尔型`bool`

    `True`、`False`
1. `None`
1. 列表（list`[值,]`）

    1. 列表是一种**可变**容器
    2. `[多个项]`直接创建字面量列表
    3. 列表支持正向索引、反向索引、切片索引
    4. 两个列表可以做关系运算（`<=`、`<`、`>`、`>=`、`==`、`!=`），逐个按顺序对比每个项
    5. 运算符支持：`列表 + 列表`、`列表 * 整数`
    6. `in`、`not in`
    7. **生成式**（推导式）创建法

        e.g. `items = [i for i in range(1, 100) if i % 3 == 0 or i % 5 == 0]`、`items2 = [num ** 2 for num in items]`

        >使用列表生成式创建列表不仅代码简单优雅，而且性能上也优于使用`for-in`循环和`append`方法向空列表中追加元素的方式。**强烈建议用生成式语法来创建列表**
1. 元组（tuple`(值,)`）

    1. 元组是**不可变**类型
    2. 类似列表的大部分操作
    3. `()`（空元组）、`(值, )`（一元组：必须加逗号，否则是改变运算优先级的圆括号）
    4. 打包、解包

        `*`解包成列表（0或多个元素）
1. 集合（set`{值,}`）

    1. 集合是**可变**类型
    2. 创建

        ><details>
        ><summary>e.g.</summary>
        >
        >```py
        >set1 = {1, 2, 3, 3, 3, 2}  # 至少一个元素，若无元素则是空字典：{}
        >print(set1)   # {1, 2, 3}
        >
        >set2 = {'banana', 'pitaya', 'apple', 'apple', 'banana', 'grape'}
        >print(set2)   # {'banana', 'pitaya', 'grape', 'apple'}
        >
        >set3 = set('hello')
        >print(set3)   # {'l', 'o', 'e', 'h'}
        >
        >set4 = set([1, 2, 2, 3, 3, 3, 2, 1])
        >print(set4)   # {1, 2, 3}
        >
        ># 生成式（推导式）创建
        >set5 = {num for num in range(1, 20) if num % 3 == 0 or num % 7 == 0}
        >print(set5)   # {3, 6, 7, 9, 12, 14, 15, 18}
        >```
        ></details>
    3. 集合中的元素必须是`hashable类型`（不可变类型）

        所谓hashable类型指的是能够计算出哈希码的数据类型，通常**不可变类型**都是hashable类型。可变类型都不是hashable类型（unhashable），因为可变类型无法计算出确定的哈希码，所以它们不能放到集合中。如：我们不能将列表作为集合中的元素；同理，由于 集合 本身也是**可变类型**，所以集合也不能作为集合中的元素。我们可以创建出嵌套列表（列表的元素也是列表），但我们不能创建出嵌套的集合。
    4. `in`、`not in`
    5. 交集（`&`、`set1.intersection(set2)`）、并集（`|`、`set1.union(set2)`）、差集（`-`、`set1.difference(set2)`）、对称差（`^`、`set1.symmetric_difference(set2)`）
    6. 比较运算：`==`、`!=`、`<`、`<=`（`set1.issubset(set2)`）、`>`（`set1.issuperset(set2)`）、`>=`

    - 不可变集合（frozenset、冻结集合）

    >集合的成员运算在性能上要优于列表的成员运算。
1. 字典（dictionary`{键:值,}`）

    1. 字典是**可变**类型
    2. 创建

        ><details>
        ><summary>e.g.</summary>
        >
        >```py
        >empty = {}     # 是 空字典；不是 空集合
        >
        >xinhua = {
        >  '麓': '山脚下',
        >  '路': '道，往来通行的地方；方面，地区：南～货，外～货；种类：他俩是一～人',
        >  '蕗': '甘草的别名',
        >  '潞': '潞水，水名，即今山西省的浊漳河；潞江，水名，即云南省的怒江'
        >}
        >print(xinhua)
        >
        >person = {
        >  'name': '王大锤',
        >  'age': 55,
        >  'height': 168,
        >  'weight': 60,
        >  'addr': '成都市武侯区科华北路62号1栋101',
        >  'tel': '13122334455',
        >  'emergence contact': '13800998877'
        >}
        >print(person)
        >
        ># dict函数(构造器)中的每一组参数就是字典中的一组键值对
        >person = dict(name='王大锤', age=55, height=168, weight=60, addr='成都市武侯区科华北路62号1栋>101')
        >print(person)  # {'name': '王大锤', 'age': 55, 'height': 168, 'weight': 60, 'addr': '成都市武>侯区科华北路62号1栋101'}
        >
        ># 可以通过Python内置函数zip压缩两个序列并创建字典
        >items1 = dict(zip('ABCDE', '12345'))
        >print(items1)  # {'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5'}
        >items2 = dict(zip('ABCDE', range(1, 10)))
        >print(items2)  # {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}
        >
        ># 用字典生成式（推导式）语法创建字典
        >items3 = {x: x ** 3 for x in range(1, 6)}
        >print(items3)  # {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
        >```
        ></details>
    3. 字典中的 键 必须是**不可变**类型

        - 字典中的键必须是唯一的。若尝试使用相同的键添加多个值，后面的值会覆盖前面的值。
        - 注意传递变量不会把变量名作为字符串

            >e.g. `a = '某个值'; { a: 1 } # { '某个值': 1 }`
1. 函数`def`

    1. 位置参数、关键字参数（参数位置可以随意打乱）

        ><details>
        ><summary>e.g.</summary>
        >
        >```py
        >def make_judgement(a, b, c):
        >    """判断三条边的长度能否构成三角形"""
        >    return a + b > c and b + c > a and a + c > b
        >
        ># 位置参数
        >print(make_judgement(1, 2, 3))         # False
        >
        ># 关键字参数
        >print(make_judgement(b=2, c=3, a=1))   # False
        >```
        ></details>

        1. 用`/`设置强制位置参数（positional-only arguments）：`/`前面的参数，只能按照参数位置来接收参数值的参数（否则报错）
        2. 用`*`设置命名关键字参数：`*`后面的参数，只能通过`参数名=参数值`的方式来传递和接收参数（否则报错）

        ><details>
        ><summary>e.g.</summary>
        >
        >```py
        ># `/`前面的参数是强制位置参数
        >def make_judgement(a, b, c, /):
        >    """判断三条边的长度能否构成三角形"""
        >    return a + b > c and b + c > a and a + c > b
        >make_judgement(b=2, c=3, a=1)  # TypeError: make_judgement() got some positional-only arguments passed as keyword arguments: 'a, b, c'
        >
        >
        ># `*`后面的参数是命名关键字参数
        >def make_judgement(*, a, b, c):
        >    """判断三条边的长度能否构成三角形"""
        >    return a + b > c and b + c > a and a + c > b
        >make_judgement(1, 2, 3)        # TypeError: make_judgement() takes 0 positional arguments but 3 were given
        >```
        ></details>
    1. 默认参数`=`、可变参数`*变量`（元组）`**变量`（字典）

        | 参数类型 | 语法 | 顺序规则​ |
        | --- | --- | --- |
        | 普通参数 | a,b | 必须最前 ↓ |
        | 默认参数 | a=1, b=2 | 在普通参数后，在*args前 ↓ |
        | 可变参数-元组 | *args | 在默认参数后，在**kwargs前 ↓ |
        | 仅关键字参数 | *, kw_arg | 在*args后，在**kwargs前 ↓ |
        | 可变参数-字典 | **kwargs | 必须最后 ↓ |

        ><details>
        ><summary>e.g.</summary>
        >
        >```py
        >def process_data(name, age=18, *scores, country="USA", **extra):
        >    print(f'{name=} {age=} {scores=} {country=} {extra=}')
        >
        >
        >process_data('geo',18,100,98,99,country='China',sex='male',level=1)   # => name='geo' age=18 scores=(100, 98, 99) country='China' extra={'sex': 'male', 'level':1}
        >```
        ></details>
    1. `def 方法名(变量名: 类型名, 变量名 = 默认值, 变量名: 类型名 = 默认值) -> 类型名:`

        标注参数的类型、标注函数返回值的类型，*虽然它对代码的执行结果不产生任何影响*，但很好的增强了代码的可读性。
    1. 函数默认返回`None`
    1. Python中的函数是“一等函数”：函数可以赋值给变量，函数可以作为函数的参数，函数也可以作为函数的返回值

        把一个函数作为其他函数的参数或返回值的用法，我们通常称之为“高阶函数”
    1. lambda函数（匿名函数）

        `lambda 参数1, 参数2: 返回值的表达式`

        没有名字的函数；只能有一行代码，代码中的表达式产生的运算结果就是这个匿名函数的返回值。
    1. 装饰器

        >装饰器是一种设计模式，允许用户在不修改对象结构的情况下为其添加新功能。装饰器通常在你想要装饰的函数定义之前调用。

        “用一个函数装饰另外一个函数并为其提供额外的能力”的语法现象。装饰器本身是一个函数，它的参数是被装饰的函数，它的返回值是一个带有装饰功能的函数——是一个高阶函数。

        ><details>
        ><summary>e.g.</summary>
        >
        >```py
        >def wrapper_func(func):
        >    def wrapper(*args, **kwargs):
        >        # ...包裹逻辑
        >        result = func(*args, **kwargs)
        >        # ...包裹逻辑
        >        return result
        >    return wrapper
        >
        >@wrapper_func
        >def real_func(props):   # 方法名可以使用，并且是经过装饰器之后的方法名
        >    print(f'{props}')   # do sth.
        >
        >real_func(1)
        >
        ># 等价于：
        >
        >def wrapper_func(func):
        >    def wrapper(*args, **kwargs):
        >        # ...包裹逻辑
        >        result = func(*args, **kwargs)
        >        # ...包裹逻辑
        >        return result
        >    return wrapper
        >
        >def real_func(props):
        >    print(f'{props}')
        >real_func = wrapper_func(real_func)
        >
        >real_func(1)
        >```
        ></details>

        - 支持多个装饰器用于单个函数
    1. 支持递归调用

        函数自己调用自己称为递归调用。函数调用通过内存中的栈空间来保存现场和恢复现场，栈空间通常都很小，所以递归如果不能迅速收敛，很可能会引发栈溢出错误，从而导致程序的崩溃。
    1. `async-await`
1. 类`class`

    >形参名`self`、`cls`等只是约定俗成，可以改成任意变量名，但是因为可读性原因不建议换其他变量名。

    1. 方法的第一个参数通常都是实例对象self，它代表了接收这个消息的对象本身。

        >若没有第一个参数`self`的方法，则无法通过对象调用（报错），只能通过类调用（不推荐，要么加上`self`，要么显式用`@staticmethod`）。
    2. 自动执行`__init__`方法，完成对内存的初始化操作，也就是把数据放到内存空间中。

    ```py
    class Student:
        属性1=值1 # 支持解构
        def __init__(self, name, age):  # 初始化方法
            self.name = name
            self.age = age
        def study(self, course_name):
            print(f'{self.name}正在学习{course_name}.')


    stu1 = Student('ldh', 50)

    # 方案1. 通过“对象.方法”调用方法
    # .前面的对象就是接收消息的对象
    # 只需要传入第二个参数课程名称
    stu1.study('Python程序设计')             # => ldh正在学习Python程序设计.

    # 方案2. 通过“类.方法”调用方法（不推荐）
    # 第一个参数是接收消息的对象
    # 第二个参数是学习的课程名称
    Student.study(stu1, 'Python程序设计')    # => ldh正在学习Python程序设计.


    # 类的属性（方法）都可以直接通过类访问，不需要借助实例
    Student.属性1
    Student.__init__
    Student.study
    ```
    3. `__name`表示一个私有属性，`_name`表示一个受保护属性

        Python语言并没有从语义上做出最严格的限定，可以用`stu._Student__属性名`的方式访问到私有属性`__属性名`或受保护属性`_属性名`
    4. Python是动态语言，若不希望在使用对象时动态的为对象添加属性，可以使用`__slots__`（若再动态添加其他属性则引发异常）

        ><details>
        ><summary>e.g.</summary>
        >
        >```py
        >class Student:
        >    __slots__ = ('name', 'age')
        >
        >    def __init__(self, name, age):
        >        self.name = name
        >        self.age = age
        >
        >
        >stu = Student('王大锤', 20)
        >
        >stu.sex = '男'     # AttributeError: 'Student' object has no attribute 'sex'
        >```
        ></details>
    5. 类的静态方法`@staticmethod`（第一个参数不能是~~类cls或实例对象self~~）、类方法`@classmethod`（第一个参数必须是类cls）
    6. `@property`指定属性（通过属性获取，经过方法计算）
    7. Python语言允许多重继承；`object类`是Python中的顶级类（所有的类都是它的子类，要么直接继承它，要么间接继承它）

        1. 在子类的初始化方法中，可以通过`super().__init__()`来调用父类初始化方法（MRO）。
        2. 子类继承父类的方法后，还可以对方法进行重写（重新实现该方法），不同的子类可以对父类的同一个方法给出不同的实现版本（多态）。

        ```py
        class Person:   # 默认 class Person(object)
            def __init__(self, name, age):
                self.name = name
                self.age = age
            def study(self, course_name):
                print(f'{self.name}随便学习{course_name}.')

        class Student(Person):  # class Student(父类1, 父类2,) 支持多重继承
            def __init__(self, name, age):
                super().__init__(name, age)     # 按照 MRO 顺序调用下一个类的初始化方法
            def study(self, course_name):       # 重写
                print(f'{self.name}正在努力学习{course_name}.')
        ```
        3. MRO (Method Resolution Order，方法解析顺序)是Python处理多重继承时确定方法调用顺序的规则体系。

            `super().方法()`不是简单地调用父类方法，而是按照 MRO 顺序调用下一个类的方法（可调用包括实例方法和`__init__`）。

            ```
              A
             / \
            B   C
             \ /
              D

            查看D类的MRO：`D.__mro__  # D → B → C → A → object`
            ```
            - 当类继承关系无法满足 C3 算法的单调性原则时，Python会抛出错误：

                >C3算法是Python用于确定多重继承中方法解析顺序（MRO）的核心算法，它解决了多重继承中的方法调用顺序问题，特别是著名的"菱形继承"问题。

                ```py
                class A: pass
                class B(A): pass
                class C(A, B): pass  # TypeError: Cannot create a consistent method resolution


                class A: pass
                class B: pass
                class C(A, B): pass
                class D(B, A): pass
                class E(C, D): pass  # TypeError: Cannot create a consistent method resolution
                ```
    8. 抽象类、抽象方法（需要子类继承父类、重写方法）

        >面向对象三大支柱：封装、继承、多态。

        ```py
        from abc import ABCMeta, abstractmethod

        class Employee(metaclass=ABCMeta):  # 定义抽象基类（该类不能实例化）
            def __init__(self, name):
                self.name = name

            @abstractmethod                 # 标记抽象方法（该方法不能调用，需要子类重写）
            def get_salary(self):
                """要求子类必须实现薪资计算方法"""
                pass                        # 什么也不做，也可以用`...`

        class Manager(Employee):
            def get_salary(self):
                return 15000.0

        class Programmer(Employee):
            def __init__(self, name, working_hour=0):
                self.working_hour = working_hour
                super().__init__(name)

            def get_salary(self):
                return 200.0 * self.working_hour
        ```
    - 枚举

        ```py
        from enum import Enum

        class Color(Enum):
            RED = 1
            GREEN = 2
            BLUE = 3


        print(Color.RED)        # => Color.RED
        print(Color.RED.name)   # => 'RED'
        print(Color.RED.value)  # => 1
        ```
    9. 元类

        `对象`是通过`类`创建，`类`是通过`元类`创建（元类提供了创建类的元信息）。所有的`类`都直接或间接的继承自`object`，所有的`元类`都直接或间接的继承自`type`。

        ```py
        class A(type):          # 元类（继承自type）
            pass

        class B(metaclass=A):   # 指定自定义元类（设置metaclass值）
            pass
        ```
- 各种数据类型都支持**解构**
- 各种数据类型（支持序列索引的）都支持 正向索引、反向索引、**切片索引**（`[start:end:stride]`若start值等于0，则可以省略；若end值等于列表长度，则可以省略；若stride值等于1，则可以省略。支持批量修改切片）

    支持序列索引的数据类型：列表 (list)​、字符串 (str)​、元组 (tuple)​、字节（bytes）、字节数组（bytearray）、range对象​（range）

    - `变量[::-1]`：反转
- 不可变类型、可变类型

    |  | 不可变类型（Immutable Types） | 可变类型（Mutable Types）​ |
    | --- | --- | --- |
    | 定义 | 不可变类型一旦创建，其内容无法被修改。任何修改操作都会生成新对象，原对象保持不变 | 可变类型创建后，其内容可直接修改，内存地址不变 |
    | ​修改行为​ | 创建新对象；若尝试直接修改（如：元组元素赋值），会抛出TypeError | 直接修改原对象 |
    | ​​​内存地址`id()`​ | 修改后变化；内存分配固定，相同值的对象可能共享内存以节省空间（如：小整数池、字符串驻留），频繁修改会导致内存碎片（如：多次拼接大字符串） | 修改后不变；动态调整内存结构（如：列表预分配扩展空间），修改时无需创建新对象，适合频繁操作 |
    | ​线程安全​​​ | 是（无需锁） | 否（需同步控制） |
    | ​​适用场景​​ | 字典键、常量数据 | 动态数据、频繁修改 |
    | 包含类型​​ | 数字类型​：整数（int）、浮点数（float）、复数（complex）<br>字符串（str）<br>​元组（tuple）<br>​冻结集合（frozenset）<br>​布尔值（bool）<br>字节（bytes）<br>None（NoneType） | 列表（list）<br>字典（dict）<br>集合（set）<br>字节数组（bytearray）<br>​自定义对象​​ |
    | 哈希性`hash()`与字典键​ | 具有固定哈希值，可作为字典键或集合元素 | 哈希值可能变化，不可作为字典键 |
    | 函数传参​ | 不可变对象传递的是值副本，函数内修改不影响外部变量 | 可变对象传递的是引用，函数内修改会影响原对象 |

### [The Zen of Python（Python之禅）](https://peps.python.org/pep-0020/)
1. Beautiful is better than ugly. （优美比丑陋好）
2. Explicit is better than implicit.（清晰比晦涩好）
3. Simple is better than complex.（简单比复杂好）
4. Complex is better than complicated.（复杂比错综复杂好）
5. Flat is better than nested.（扁平比嵌套好）
6. Sparse is better than dense.（稀疏比密集好）
7. Readability counts.（可读性很重要）
8. Special cases aren't special enough to break the rules.（特殊情况也不应该违反这些规则）
9. Although practicality beats purity.（但现实往往并不那么完美）
10. Errors should never pass silently.（异常不应该被静默处理）
11. Unless explicitly silenced.（除非你希望如此）
12. In the face of ambiguity, refuse the temptation to guess.（遇到模棱两可的地方，不要胡乱猜测）
13. There should be one-- and preferably only one --obvious way to do it.（肯定有一种通常也是唯一一种最佳的解决方案）
14. Although that way may not be obvious at first unless you're Dutch.（虽然这种方案并不是显而易见的，因为你不是那个荷兰人[这里指的是Python之父Guido]）
15. Now is better than never.（现在开始做比不做好）
16. Although never is often better than *right* now.（不做比盲目去做好[极限编程中的YAGNI原则]）
17. If the implementation is hard to explain, it's a bad idea.（如果一个实现方案难于理解，它就不是一个好的方案）
18. If the implementation is easy to explain, it may be a good idea.（如果一个实现方案易于理解，它很有可能是一个好的方案）
19. Namespaces are one honking great idea -- let's do more of those!（命名空间非常有用，我们应当多加利用）

### 网络数据采集
1. 爬虫（crawler）也经常被称为网络蜘蛛（spider），是按照一定的规则自动浏览网站并获取所需信息的机器人程序（自动化脚本代码），被广泛的应用于互联网搜索引擎和数据采集
2. 域名/robots.txt
3. 一个基本的爬虫通常分为 数据采集（网页下载）、数据处理（网页解析）和数据存储（将有用的信息持久化）三个部分的内容，当然更为高级的爬虫在数据采集和处理时会使用并发编程或分布式技术，这就需要有调度器（安排线程或进程执行对应的任务）、后台管理程序（监控爬虫的工作状态以及检查数据抓取的结果）等的参与

    1. 设定抓取目标（种子页面/起始页面）并获取网页
    2. 当服务器无法访问时，按照指定的重试次数尝试重新下载页面
    3. 在需要的时候设置用户代理（User-Agent）或隐藏真实IP，否则可能无法访问页面
    4. 对获取的页面进行必要的解码操作然后抓取出需要的信息
    5. 在获取的页面中通过某种方式（如正则表达式）抽取出页面中的链接信息
    6. 对链接进行进一步的处理（获取页面并重复上面的动作）
    7. 将有用的信息进行持久化以备后续的处理
4. 解析HTML页面

    | 解析方式 | 对应的模块 | 速度 | 使用难度 |
    | --- | --- | --- | --- |
    | 正则表达式解析 | `re` | 快 | 困难 |
    | XPath 解析 | `lxml` | 快 | 一般 |
    | CSS 选择器解析 | （第三方库） `bs4`或`pyquery` | 不确定 | 简单 |
5. 爬虫是典型的 I/O 密集型任务

    >I/O 密集型任务的特点就是程序会经常性的因为 I/O 操作而进入阻塞状态。
