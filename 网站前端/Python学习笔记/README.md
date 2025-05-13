# Python学习笔记

## 目录
1. [核心软件](#核心软件)
1. [语法](#语法)
1. [The Zen of Python（Python之禅）](#the-zen-of-pythonpython之禅)

---
### 核心软件
1. [conda](https://github.com/conda/conda)

    环境管理、包管理

### 语法
1. 单引号`'`与双引号`"`同时支持，相同效果
1. 范围相关的都遵循：左闭右开，支持步长
1. 换行 或 分号`;`表示语句结束
1. 注释

    1. `#`单行注释
    2. `""" """`或`''' '''`多行注释
1. 数据类型

    1. 整型`int`

        `0b100 == 4`、`0o100 == 64`、`0x100 == 256`
    2. 浮点型`float`

        `123.456 == 1.23456e2`
    3. 字符串型`str`

        单引号、双引号，`'''`或`"""`支持换行字符串（`\n`可以用回车换行表示）

        1. `r'字符串'`或`R'字符串'`（也支持`'''`或`"""`）：原始字符串、不会转义

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
    4. 布尔型`bool`

        `True`、`False`
1. 变量惯例：

    1. 变量名通常使用小写英文字母，多个单词用下划线`_`进行连接
    2. 受保护的变量用单个下划线`_`开头
    3. 私有的变量用两个下划线`__`开头
1. （与JS不同的运算符）`:=`、`==`、`!=`、`not`、`or`、`and`、`//`、`is`、`is not`、`in`、`not in`
1. `if 「条件」:`（没有小括号 ~~`()`~~ ）、`elif 「条件」:`、`else:`

    2. 支持`值1 <= 变量 < 值2`
1. `for 变量 in 列表或元组或集合或字符串或字典或range(参数):`

    `for _ in xx:`不使用索引
1. for、if等可以放在表达式中

    ```py
    items = [i for i in range(1, 10)]   # [1, 2, 3, 4, 5, 6, 7, 8, 9]
    items = [i for i in range(1, 10) if i % 3 == 0 or i % 5 == 0] # [3, 5, 6, 9]
    items = [i ** 2 for i in range(1, 10) if i % 3 == 0 or i % 5 == 0] # [9, 25, 36, 81]
    # 运行顺序：for -> if ->产出的i进行 i ** 2计算
    ```
1. `break`、`continue`仅针对当前循环
1. Python中没有用花括号 ~~`{}`~~ 来构造代码块，而是使用**缩进**的方式来表示代码的层次结构
1. `match-case`

    1. `case 值1 | 值2 | 值3:`
    2. `case _:`默认匹配
1. `内置函数`:不需要 ~~`import`~~ 就能够直接使用的函数

    1. `input(「描述值或变量」)`
    1. `print`

        1. `print(值或变量)`
        1. `print('浮点数%f' % 变量1)`、`print('浮点数%.1f 整数%d 字符串%s' % (变量1, 变量2, 变量3))`
        2. `print(f'{变量1}  {变量2:.2f}')`

            - 同时输出变量名：`print(f'{变量1 = } {变量2 = :.3f}')`
        3. `print(变量 := 10)`既能输出又能赋值（~~`print(变量 = 10)`~~ 报错）
        4. `print(f'\033[样式;前景色;背景色m内容...\033[0m')`

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
1. 需要`import`才能使用的内置模块

    `math`、`random`、`string`、`operator`、`functools`、`time`
1. `import math`（仅导入了`math`）、`import math as m`（仅导入了`m`）、`from math import factorial`（仅导入了`factorial`）、`from math import factorial as f`（仅导入了`f`）

    - 同名的后导入 覆盖 同名的前导入
1. 列表（list）

    1. 列表是一种**可变**容器
    2. `[多个项]`直接创建字面量列表
    3. 列表支持正向索引、反向索引、切片索引（`[start:end:stride]`若start值等于0，则可以省略；若end值等于列表长度，则可以省略；若stride值等于1，则可以省略。支持批量修改切片）
    4. 两个列表可以做关系运算（`<=`、`<`、`>`、`>=`、`==`、`!=`），逐个按顺序对比每个项
    5. 运算符支持：`列表 + 列表`、`列表 * 整数`
    6. `in`、`not in`
    7. **生成式**创建法

        e.g. `items = [i for i in range(1, 100) if i % 3 == 0 or i % 5 == 0]`、`items2 = [num ** 2 for num in items]`

        >使用列表生成式创建列表不仅代码简单优雅，而且性能上也优于使用`for-in`循环和`append`方法向空列表中追加元素的方式。**强烈建议用生成式语法来创建列表**
1. 元组（tuple）

    1. 元组是**不可变**类型
    1. 类似列表的大部分操作
    3. `()`（空元组）、`(值, )`（一元组：必须加逗号，否则是改变运算优先级的圆括号）
    4. 打包、解包

        `*`解包成列表（0或多个元素）
1. 集合（set）

    1. 集合是**可变**类型
    1. 创建

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
        >set5 = {num for num in range(1, 20) if num % 3 == 0 or num % 7 == 0}
        >print(set5)   # {3, 6, 7, 9, 12, 14, 15, 18}
        >```
        ></details>
    1. 集合中的元素必须是`hashable类型`

        所谓hashable类型指的是能够计算出哈希码的数据类型，通常不可变类型都是hashable类型。可变类型都不是hashable类型（unhashable），因为可变类型无法计算出确定的哈希码，所以它们不能放到集合中。如：我们不能将列表作为集合中的元素；同理，由于 集合 本身也是**可变类型**，所以集合也不能作为集合中的元素。我们可以创建出嵌套列表（列表的元素也是列表），但我们不能创建出嵌套的集合。
    3. `in`、`not in`
    4. 交集（`&`、`set1.intersection(set2)`）、并集（`|`、`set1.union(set2)`）、差集（`-`、`set1.difference(set2)`）、对称差（`^`、`set1.symmetric_difference(set2)`）
    5. 比较运算：`==`、`!=`、`<`、`<=`（`set1.issubset(set2)`）、`>`（`set1.issuperset(set2)`）、`>=`

    - 不可变集合（frozenset、冻结集合）

    >集合的成员运算在性能上要优于列表的成员运算。
1. 字典（dictionary）

    1. 字典是**可变**类型
    1. 创建

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
        >'name': '王大锤',
        >'age': 55,
        >'height': 168,
        >'weight': 60,
        >'addr': '成都市武侯区科华北路62号1栋101',
        >'tel': '13122334455',
        >'emergence contact': '13800998877'
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
        ># 用字典生成式语法创建字典
        >items3 = {x: x ** 3 for x in range(1, 6)}
        >print(items3)  # {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
        >```
        ></details>
    2. 字典中的 键 必须是**不可变**类型
1. 不可变类型、可变类型

    |  | 不可变类型（Immutable Types） | 可变类型（Mutable Types）​ |
    | --- | --- | --- |
    | 定义 | 不可变类型一旦创建，其内容无法被修改。任何修改操作都会生成新对象，原对象保持不变 | 可变类型创建后，其内容可直接修改，内存地址不变 |
    | ​修改行为​ | 创建新对象；若尝试直接修改（如：元组元素赋值），会抛出TypeError | 直接修改原对象 |
    | ​​​内存地址`id()`​ | 修改后变化；内存分配固定，相同值的对象可能共享内存以节省空间（如：小整数池、字符串驻留），频繁修改会导致内存碎片（如：多次拼接大字符串） | 修改后不变；动态调整内存结构（如：列表预分配扩展空间），修改时无需创建新对象，适合频繁操作 |
    | ​线程安全​​​ | 是（无需锁） | 否（需同步控制） |
    | ​​适用场景​​ | 字典键、常量数据 | 动态数据、频繁修改 |
    | 包含类型​​ | 数字类型​：整数（int）、浮点数（float）、复数（complex）<br>字符串（str）<br>​元组（tuple）<br>​冻结集合（frozenset）<br>​布尔值（bool）<br>字节（bytes） | 列表（list）<br>字典（dict）<br>集合（set）<br>字节数组（bytearray）<br>​自定义对象​​ |
    | 哈希性`hash()`与字典键​ | 具有固定哈希值，可作为字典键或集合元素 | 哈希值可能变化，不可作为字典键 |
    | 函数传参​ | 不可变对象传递的是值副本，函数内修改不影响外部变量 | 可变对象传递的是引用，函数内修改会影响原对象 |
1. 函数`def`

    1. 位置参数、关键字参数

        ><details>
        ><summary>e.g.</summary>
        >
        >```py
        >def make_judgement(a, b, c):
        >    """判断三条边的长度能否构成三角形"""
        >    return a + b > c and b + c > a and a + c > b
        >
        ># 位置参数
        >print(make_judgement(1, 2, 3))  # False
        >print(make_judgement(4, 5, 6))  # True
        >
        ># 关键字参数
        >print(make_judgement(b=2, c=3, a=1))  # False
        >print(make_judgement(c=6, b=4, a=5))  # True
        >```
        ></details>

        1. 用`/`设置强制位置参数（positional-only arguments）：只能按照参数位置来接收参数值的参数
        2. 用`*`设置命名关键字参数：只能通过`参数名=参数值`的方式来传递和接收参数

        ><details>
        ><summary>e.g.</summary>
        >
        >```py
        ># / 前面的参数是强制位置参数
        >def make_judgement(a, b, c, /):
        >    """判断三条边的长度能否构成三角形"""
        >    return a + b > c and b + c > a and a + c > b
        ># 下面的代码会产生TypeError错误，错误信息提示“强制位置参数是不允许给出参数名的”
        ># TypeError: make_judgement() got some positional-only arguments passed as keyword arguments
        ># print(make_judgement(b=2, c=3, a=1))
        >
        >
        ># * 后面的参数是命名关键字参数
        >def make_judgement(*, a, b, c):
        >    """判断三条边的长度能否构成三角形"""
        >    return a + b > c and b + c > a and a + c > b
        ># 下面的代码会产生TypeError错误，错误信息提示“函数没有位置参数但却给了3个位置参数”
        ># TypeError: make_judgement() takes 0 positional arguments but 3 were given
        ># print(make_judgement(1, 2, 3))
        >```
        ></details>
    2. 默认参数`=`、可变参数`*变量`（元组）`**变量`（字典）
    3. `del 方法名(变量名: 类型名, 变量 = 1) -> 类型名:`

        标注参数的类型、标注函数返回值的类型，*虽然它对代码的执行结果不产生任何影响*，但很好的增强了代码的可读性。
    4. Python中的函数是“一等函数”，所谓“一等函数”指的是：函数可以赋值给变量，函数可以作为函数的参数，函数也可以作为函数的返回值

        把一个函数作为其他函数的参数或返回值的用法，我们通常称之为“高阶函数”
    5. lambda函数（匿名函数）

        `lambda 参数1, 参数2: 返回值的表达式`

        没有名字的函数；只能有一行代码，代码中的表达式产生的运算结果就是这个匿名函数的返回值。
    6. 装饰器

        “用一个函数装饰另外一个函数并为其提供额外的能力”的语法现象。装饰器本身是一个函数，它的参数是被装饰的函数，它的返回值是一个带有装饰功能的函数——是一个高阶函数。

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
