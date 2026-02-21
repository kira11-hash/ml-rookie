# Python 语法讲义（超详细版，纯讲义）

> 适用对象：零基础  
> 讲义目标：让你在 Day1/Day2 不靠死记硬背，真正理解并能手写通过

---

## 目录与使用路线（新版）

按“当天任务”只看对应章节，避免信息过载：
1. Day1：看 `##2`
2. Day2：看 `##3`
3. Day3：看 `##8`
4. Day4：看 `##9`
5. Day5：看 `##10`
6. Day6（基础语法）：先看 `##11`
7. Day6（完整MNIST任务）：再看 `##12`

本讲义统一格式：
1. 先讲概念
2. 再讲语法
3. 再给例子
4. 最后给 TODO 对照和常见误区

---

## 0. 讲义使用方法（先看这个）

### 0.1 你每天的固定学习顺序
1. 先读本讲义里“当天对应章节”（15-25分钟）。
2. 再写 `dayN/dayN_handwrite.py`（45-90分钟）。
3. 同一报错卡住超过10分钟，再来问我。
4. 当天更新 `ml_learning_log.md`。

### 0.2 你必须坚持的原则
1. 先手写，再看答案。
2. 先理解“为什么错”，再改代码。
3. 每天至少独立修复1个报错。

### 0.3 你会遇到的正常现象
1. 看懂代码但写不出来：正常，靠手写次数解决。
2. 一直报 `SyntaxError`：正常，Python对格式很严格。
3. 写得慢：正常，早期速度不是核心指标。

---

## 1. Python 入门总图（先建立脑图）

Python 初学可以分成四层：
1. 数据：变量、字符串、数字、列表、字典。
2. 逻辑：if 判断、for 循环、函数封装。
3. 工程：文件读写、异常处理、模块调用。
4. 任务：把上面三层拼成可运行脚本。

Day1 对应第1层和第2层最基础部分。  
Day2 重点是“容器 + 循环 + 统计任务”。

---

## 2. Day1 讲义：变量 / print / if / 函数 / BMI

## 2.1 变量（Variable）到底是什么

变量可以理解为“给一段数据起一个名字”。

```python
name = "Qingan"
age = 22
height = 1.75
```
想让 Python 把它当“值本身”，就用该类型的字面量语法。
字符串的字面量语法就是加引号。

不加引号时，Qingan 会被当成变量名。
这个变量通常没定义，会报 NameError。
字符串字面量必须加引号（单引号或双引号都行）

上面三行含义：
1. `name` 存了字符串 `"Qingan"`。
2. `age` 存了整数 `22`。
3. `height` 存了浮点数 `1.75`。

### 2.1.1 `=` 不是数学里的“等于”
在编程里 `=` 是“赋值”：把右边的值交给左边变量。

```python
x = 3
x = x + 2
```

最终 `x` 是 `5`，不是“矛盾式子”。

### 2.1.2 常见类型
1. `int`：整数，例如 `3`、`100`、`-5`
2. `float`：小数，例如 `3.14`、`1.75`
3. `str`：字符串，必须有引号，例如 `"hello"`
4. `bool`：布尔值，只能是 `True` 或 `False`

### 2.1.3 命名规则（非常重要）
1. 只能用字母、数字、下划线。
2. 不能以数字开头。
3. 区分大小写（`score` 和 `Score` 是两个变量）。
4. 不要用中文、空格、特殊符号。

建议命名风格：`snake_case`，例如 `score_value`、`user_height`。

---

## 2.2 输出：`print()`

`print()` 作用：把信息显示到终端，便于观察程序是否正确。

```python
name = "Qingan"
age = 22
print("姓名:", name)
print("年龄:", age)
```

### 2.2.1 为什么初学要大量 `print`
1. 它是最简单的调试工具。
2. 每一步结果都可见，能快速定位错误。
3. 在你还没学调试器前，`print` 是第一生产力。

### 2.2.2 三种常见写法
```python
print("分数:", 95)                  # 逗号分隔
print("分数是 " + str(95))          # 字符串拼接（需要类型转换）
score = 95
print(f"分数是 {score}")            # f-string，推荐

```

这三种写法都能打印结果，但语法逻辑不同：
1. `print("分数:", 95)`：
   - `print` 接受多个参数。
   - 参数之间自动加空格。
2. `print("分数是 " + str(95))`：
   - `+` 在这里表示字符串拼接。
   - 左右两边都必须是字符串，所以要先 `str(95)`。
3. `print(f"分数是 {score}")`：
   - `f` 是 format（格式化）的意思。
   - 花括号 `{}` 内可直接放变量或表达式，最推荐。

f-string 常见写法：
```python
name = "Qingan"
score = 95
bmi = 21.554

print(f"你好，{name}")
print(f"分数是 {score}")
print(f"BMI 保留两位小数：{bmi:.2f}")   # 21.55
print(f"明年年龄：{22 + 1}")            # 花括号里可写表达式
```

f-string 常见错误：
1. 忘记加前缀 `f`，变量不会被替换。
2. 花括号没配对，会 `SyntaxError`。
3. 想输出字面量 `{` 或 `}`，要写 `{{` 或 `}}`。

### 2.2.3 `[]`、`()`、`{}` 的异同点

先记最常用含义：
1. `[]`：列表（list），有序、可重复、可修改。
2. `()`：元组（tuple）或函数调用参数。
3. `{}`：字典（dict）或集合（set，非空时）。

例子：
```python
# [] -> list
nums = [3, 1, 2]
nums.append(4)
print(nums[0])
# 下标从 0 开始，所以 nums[0] 是第一个元素（这里是 3）

# () -> tuple
point = (10, 20)
# point[0] = 99  # 报错：tuple 不可改

# () -> 函数调用
print(len(nums))

# {} -> dict
student = {"name": "Qingan", "age": 22}
print(student["name"])

# {} -> set（非空）
seen = {1, 2, 3}

# 空字典 vs 空集合
empty_dict = {}
empty_set = set()
```

快速选择规则：
1. 存一串会变化的数据：`list`（`[]`）。
2. 存一组固定值：`tuple`（`()`）。
3. 做 key-value 映射：`dict`（`{}`）。
4. 做去重/查存在：`set`（`{...}` 或 `set()`）。

---

## 2.3 输入：`input()` 和类型转换

`input()` 默认返回字符串（`str`），哪怕你输入的是数字。

```python
x = input("请输入一个数字: ")
print(type(x))  # <class 'str'>
```

要做数值计算，必须转类型：

```python
weight = float(input("请输入体重(kg): "))
height = float(input("请输入身高(m): "))
```
`float(...)` 是 Python 内置函数，作用是“把值转换为浮点数（小数）”。
1. 语法：`float(x)`
2. 常见输入：`x` 可以是数字或数字字符串（如 `"66"`、`"1.75"`）
3. 常见用途：`input()` 返回 `str`，做数值计算前通常先 `float(...)`
4. 示例：`float("66") -> 66.0`，`float(10) -> 10.0`

### 2.3.1 常见错误
```python
age = input("年龄: ")
print(age + 1)   # TypeError，str 不能直接 + int
```

修复：
```python
age = int(input("年龄: "))
print(age + 1)
```

---

## 2.4 条件判断：`if / elif / else`

语法模板：

```python
if 条件1:
    代码块1
elif 条件2:
    代码块2
else:
    代码块3
```

执行逻辑：
1. 先判断 `if`。
2. 如果 `if` 不成立，按顺序判断 `elif`。
3. 都不成立，走 `else`。

### 2.4.1 条件表达式
常见比较运算符：
1. `>` 大于
2. `<` 小于
3. `>=` 大于等于
4. `<=` 小于等于
5. `==` 等于（注意是两个等号）
6. `!=` 不等于

### 2.4.2 例子：成绩分档
```python
score = 83
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print("等级:", grade)
```

### 2.4.3 顺序为什么重要
如果你先写 `if score >= 60`，那 `95` 也会被提前拦截，后面的 A 档永远到不了。  
所以区间判断一般从大到小写。

---

## 2.5 函数：`def`

函数本质：把一段“可复用逻辑”封装成一个名字。

```python
def grade_level(score_value):
    if score_value >= 90:
        return "A"
    elif score_value >= 80:
        return "B"
    else:
        return "C"
```

### 2.5.1 关键概念
1. `def`：定义函数。
2. `score_value`：参数（输入）。
3. `return`：返回结果（输出）。

### 2.5.2 函数调用
```python
g = grade_level(95)
print(g)  # A
```

### 2.5.3 `return` 和 `print` 的区别
1. `print`：只显示，不把值交给外部。
2. `return`：把结果“返回给调用者”，后续可继续使用。

错误示例：
```python
def f(x):
    print(x + 1)

y = f(1)
print(y)   # None，因为函数没 return
```

---

## 2.6 Day1 任务讲透：`grade_level` + `BMI`

### 2.6.1 `grade_level(score)`
目标：输入分数，输出等级。

推荐规则：
1. `>= 90` -> A
2. `>= 80` -> B
3. `>= 70` -> C
4. `>= 60` -> D
5. 其他 -> F

### 2.6.2 BMI 公式
公式：`BMI = 体重(kg) / 身高(m)^2`

```python
def bmi_value(weight_kg, height_m):
    return weight_kg / (height_m ** 2)
```

### 2.6.3 BMI 分级（你现在使用的版本）
1. `< 18.5`：偏瘦
2. `< 24`：正常
3. `< 28`：偏胖
4. `>= 28`：肥胖

---

## 2.7 Day1 常见报错总表

1. `SyntaxError`  
典型原因：漏冒号、括号不闭合。

2. `IndentationError`  
典型原因：缩进混乱（Python 用缩进表示代码块）。

3. `NameError`  
典型原因：变量名拼错，如 `scroe` 写成 `score`。

4. `TypeError`  
典型原因：字符串和数字直接相加。

5. `AssertionError`  
典型原因：你的函数逻辑和断言预期不一致。

---

## 3. Day2 讲义：list / dict / for / 词频 Top10

## 3.1 Day2 你到底在做什么（先看目标）

Day2 的核心不是“背语法”，而是完成一个小工程任务：  
输入一段英文文本，输出词频 Top10。

这件事需要四个语法能力：
1. 用 `list` 存一组数据。
2. 用 `dict` 做“单词 -> 次数”统计。
3. 用 `for` 循环反复处理每个元素。
4. 用 `sorted` 排序得到 Top10。

你可以把 Day2 看成“第一次把语法拼成任务”。

---

## 3.2 列表 `list`（把一组数据放在一起）

### 3.2.1 列表是什么
列表是“有顺序、可修改”的容器。  
类比：一个按顺序排好的抽屉。

```python
scores = [88, 92, 76]
```

这里：
1. `scores[0]` 是第一个元素 `88`
2. `scores[1]` 是第二个元素 `92`
3. `scores[2]` 是第三个元素 `76`

### 3.2.2 索引（下标）规则
1. 从 `0` 开始，不是从 `1` 开始。
2. 负数索引从尾部取值：`-1` 表示最后一个。

```python
print(scores[0])   # 88
print(scores[-1])  # 76
```

### 3.2.3 Day2 高频操作
```python
scores = [88, 92, 76]
scores.append(95)      # 末尾追加
print(scores)          # [88, 92, 76, 95]

scores.sort()          # 原地排序（升序）
print(scores)          # [76, 88, 92, 95]

x = scores.pop()       # 删除并返回最后一个元素
print(x)               # 95
print(scores)          # [76, 88, 92]
```

### 3.2.3.1 为什么 `.sort` 后面要加 `()`
核心：`.sort` 是“方法本体”，`.sort()` 才是“执行方法”。

```python
nums = [3, 1, 2]

print(nums.sort)    # 打印的是方法对象（还没执行）
nums.sort()         # 现在才真正执行排序
print(nums)         # [1, 2, 3]
```

你可以把它理解成：
1. `nums.sort`：拿到“工具”本身。
2. `nums.sort()`：按下“工具开关”，开始干活。

同理：
1. `text.lower` vs `text.lower()`
2. `f.read` vs `f.read()`
3. `model.train` vs `model.train()`

什么时候不加 `()`：
1. 你只是想“把函数/方法传给别人”，先不执行。
2. 例子：`key=str.lower`（把函数作为参数传入）。

### 3.2.4 `sort()` 和 `sorted()` 的区别（初学易混）
1. `scores.sort()`：直接修改原列表，返回 `None`。
2. `sorted(scores)`：不改原列表，返回新列表。

示例：
```python
nums = [3, 1, 2]
new_nums = sorted(nums)
print(nums)      # [3, 1, 2]
print(new_nums)  # [1, 2, 3]
```

### 3.2.5 常见错误
1. `IndexError: list index out of range`  
原因：访问了不存在的位置，如 `scores[100]`。

2. `AttributeError: 'str' object has no attribute 'append'`  
原因：把字符串当列表用。

---

## 3.3 字典 `dict`（做统计最关键）

### 3.3.1 字典是什么
字典是“键值对（key-value）”容器。  
类比：通讯录，名字是 key，电话号码是 value。

```python
student = {"name": "Qingan", "major": "IC"}
```

### 3.3.2 访问/新增/修改
```python
print(student["name"])       # 访问
student["city"] = "Hangzhou" # 新增 key
student["major"] = "ML"      # 修改已有 key
print(student)
```

### 3.3.3 为什么词频必须用字典
词频本质是映射关系：
`单词 -> 出现次数`

比如：
```python
freq = {"python": 2, "is": 3, "fun": 1}
```

### 3.3.4 统计词频的标准写法
```python
freq[word] = freq.get(word, 0) + 1
```

拆开理解：
1. `freq.get(word, 0)`：取当前单词已有次数，没有就当 `0`。
2. `+ 1`：出现一次就加一。
3. 写回 `freq[word]`。

### 3.3.5 实际过程演示
```python
words = ["python", "is", "python"]
freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1
    print(f"当前word={word}, freq={freq}")
```

输出过程：
1. 读到 `"python"` -> `{'python': 1}`
2. 读到 `"is"` -> `{'python': 1, 'is': 1}`
3. 再读到 `"python"` -> `{'python': 2, 'is': 1}`

### 3.3.6 为什么 `word` 不加引号
1. `word`（不加引号）是变量，值会变化：`"python"`、`"is"`...
2. `"word"`（加引号）是固定字符串，只会统计到同一个 key。

错误示例：
```python
freq["word"] = freq.get("word", 0) + 1
```
这样最终只会得到：
`{'word': N}`，完全丢失真实词频。

---

## 3.4 循环 `for`（把同一动作重复执行）

### 3.4.1 `for` 的基本模板
```python
for 元素变量 in 可迭代对象:
    重复执行的代码
```

### 3.4.2 遍历列表
```python
scores = [76, 88, 92]
for s in scores:
    print(s)
```

这会依次把 `76/88/92` 放进变量 `s`。

### 3.4.3 `range()` 生成数字序列
```python
for i in range(5):
    print(i)  # 0,1,2,3,4
```

常用写法：
1. `range(n)` -> `0...n-1`
2. `range(a, b)` -> `a...b-1`
3. `range(a, b, step)` -> 带步长

例子：
```python
for i in range(2, 8, 2):
    print(i)  # 2,4,6
```

### 3.4.4 `enumerate()`：遍历时同时拿到序号
```python
words = ["a", "b", "c"]
for idx, w in enumerate(words, start=1):
    print(idx, w)
```

输出：
1. `1 a`
2. `2 b`
3. `3 c`

适用场景：
1. 打印 Top10 排名。
2. 任何“第几项 + 值”的需求。

---

## 3.5 字符串清洗（词频任务的关键步骤）

你在 Day2 的 `top10_word_frequency(text)` 里，推荐固定 5 步：
1. 小写化：`text = text.lower()`
2. 清洗符号：只保留字母和空格
3. 切词：`words = cleaned_text.split()`
4. 统计：用 `dict` 累加
5. 排序：频次降序 + 单词升序

### 3.5.1 `lower()`：统一大小写
```python
text = "Python is GOOD"
print(text.lower())  # python is good
```

如果不转小写，`Python` 和 `python` 会被当成两个词。

### 3.5.2 `isalpha()`：判断是不是字母
```python
print("a".isalpha())  # True
print("1".isalpha())  # False
print(",".isalpha())  # False
```

典型清洗写法：
```python
cleaned_chars = []
for ch in text:
    if ch.isalpha() or ch == " ":
        cleaned_chars.append(ch)
    else:
        cleaned_chars.append(" ")
cleaned_text = "".join(cleaned_chars)
```

为什么要把符号替换为空格而不是删掉？  
为了避免单词粘连。比如 `"hi,python"` 变成 `"hi python"` 更安全。

### 3.5.3 `split()`：按空白切词
```python
s = "i   love   python"
print(s.split())  # ['i', 'love', 'python']
```

`split()` 默认会自动处理多个空格。

---

## 3.6 排序拿 Top10：`sorted(..., key=...)`

词频结果是：
```python
freq = {"python": 2, "is": 4, "ml": 2}
```

先转成键值对列表：
```python
print(freq.items())
# dict_items([('python', 2), ('is', 4), ('ml', 2)])
```

补充：`item()` 和 `items()` 是两件不同的事（高频易混）
1. `items()`（有 s）：
   - 对象：`dict`
   - 作用：返回“所有键值对”（`(key, value)`）
   - 例子：`freq.items()` -> `('python', 2)` 这种对
2. `item()`（无 s）：
   - 常见对象：`torch.Tensor`（单元素张量）
   - 作用：把张量中的单个数取成 Python 普通数值
   - 例子：`loss.item()` -> `0.1234`

快速记忆：
1. `item()`：单数，取“一个值”。
2. `items()`：复数，取“很多键值对”。

排序写法：
```python
sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
```

详细拆解（高频重点）：
1. `sorted(...)` 是 Python 内置排序函数  
   - 语法：`sorted(iterable, key=..., reverse=...)`
   - 作用：对可迭代对象排序，返回“新列表”（不改原对象）
2. `freq.items()` 返回字典的键值对  
   - 例如：`{"python": 2, "is": 4}` -> `("python", 2)`、`("is", 4)`
   - 每个元素都是一个二元组：`(key, value)`，在这里就是 `(word, count)`
3. `key=` 是 `sorted` 的参数名（函数自带）  
   - 含义：告诉 `sorted`“按什么标准比较”
   - `sorted` 会把每个元素喂给 `key` 函数，再比较 `key` 的返回值
4. `lambda x: ...` 是匿名函数  
   - 语法：`lambda 参数: 返回表达式`
   - 这里的 `x` 不是预定义变量，而是“当前元素”的临时名字
5. Python 为什么知道 `x` 是 `(key, value)`  
   - 因为 `sorted` 在遍历 `freq.items()` 时，每次拿到的元素本来就是二元组
   - 所以当元素是 `("python", 2)` 时，`x[0]` 就是 `"python"`，`x[1]` 就是 `2`
6. `(-x[1], x[0])` 是“复合排序键”（元组比较）  
   - 第一关键字：`-x[1]`（频次降序，次数大的排前面）
   - 第二关键字：`x[0]`（次数相同按字母升序）
   - 例子：`("python", 2)` -> 键是 `(-2, "python")`

可读性更强的等价写法（和 lambda 完全等价）：
```python
def sort_key(x):
    return (-x[1], x[0])

sorted_items = sorted(freq.items(), key=sort_key)
```

取 Top10：
```python
top10 = sorted_items[:10]
```

### 3.6.1 小例子
```python
freq = {"b": 2, "a": 2, "c": 5}
print(sorted(freq.items(), key=lambda x: (-x[1], x[0])))
# [('c', 5), ('a', 2), ('b', 2)]
```

---

## 3.7 Day2 任务完整示例（最小可运行）

```python
def top10_word_frequency(text):
    text = text.lower()

    cleaned_chars = []
    for ch in text:
        if ch.isalpha() or ch == " ":
            cleaned_chars.append(ch)
        else:
            cleaned_chars.append(" ")
    cleaned_text = "".join(cleaned_chars)

    words = cleaned_text.split()

    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1

    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items[:10], len(words), len(freq)
```

---

## 3.8 Day2 常见报错总表（更细版）

1. `KeyError`  
场景：`freq[w] += 1` 时 `w` 还不存在。  
修复：改成 `freq[w] = freq.get(w, 0) + 1`。

2. `TypeError`  
场景：把数字当字符串拼接、或把字符串当数字计算。  
修复：用 `str()/int()/float()` 做类型转换，或检查变量来源。

3. `AttributeError`  
场景：对错误类型调方法，例如 `text.append()`。  
修复：先 `print(type(text))` 再决定可用方法。

4. `AssertionError`  
场景：断言失败，多数是清洗或排序步骤漏了。  
修复：打印中间变量：`cleaned_text`、`words[:20]`、`freq`、`top10`。

5. `NameError`  
场景：变量拼写不一致，如 `freq` 写成 `frqe`。  
修复：统一变量名，并让编辑器高亮帮你查错。

6. `IndentationError`  
场景：`for` 或 `if` 的代码块缩进不一致。  
修复：统一 4 空格，别混 Tab。

---

## 3.9 Day2 自检题（你做完任务后口述）

1. 为什么词频统计要用 `dict`，而不是 `list`？
2. `freq.get(word, 0)` 比 `freq[word]` 安全在哪里？
3. 为什么要先 `lower()` 再统计？
4. `sorted(... key=lambda x: (-x[1], x[0]))` 里两个键分别控制什么？
5. 为什么 `enumerate(words, start=1)` 适合打印排名？

---

## 3.10 Day2 问答补充（你今天问过的高频点）

### Q1. `for w in words` 里，`w` 为什么不用提前定义？
A：`w` 是循环变量，`for` 每一轮会自动赋值。  
第一轮 `w=words[0]`，第二轮 `w=words[1]`，依次类推。

### Q2. `start=1` 是什么？
A：`enumerate(words, start=1)` 会让编号从 1 开始（更像排名）。  
不写时默认从 0 开始。

### Q3. `text.lower()` 里的 `.` 和 `()` 各是什么意思？
A：`.` 表示“访问对象的方法/属性”；`()` 表示“调用这个方法”。  
`text.lower()` 就是调用字符串 `text` 的 `lower` 方法。

### Q4. `clean_text.split()` 会不会改掉 `clean_text` 本身？
A：不会。字符串是不可变对象。  
`split()` 返回新列表，原字符串不变。

### Q5. `join` 和 `split` 的顺序为什么是“先 join 后 split”？
A：因为清洗阶段先得到的是“字符列表”，要先用 `join` 拼成字符串，  
再用 `split` 按空白切成“单词列表”。

```python
clean_text = "".join(clean_chars)
words = clean_text.split()
```

### Q6. `len(words)` 和 `len(freq)` 分别是什么？
A：
1. `len(words)`：总词数（含重复）
2. `len(freq)`：去重词数（唯一单词个数）

### Q7. `key=lambda x` 里的 `key` 是字典里的 key 吗？
A：不是。  
这里的 `key=` 是 `sorted()` 的参数，表示“排序规则函数”。

### Q8. `lambda` 是什么？
A：匿名函数（临时小函数）。  
常用于 `sorted/map/filter` 这种“要传函数进去”的场景。

```python
sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
```

### Q9. `()`、`[]`、`{}` 最常见区别
A：
1. `()`：函数调用 / 元组 / 分组
2. `[]`：列表 / 索引 / 切片 / 字典取值键
3. `{}`：字典字面量；非空集合用 `{1,2}`；空集合必须 `set()`

### Q10. `list` 和 `tuple` 区别
A：
1. `list`（`[]`）可变：可增删改
2. `tuple`（`()`）不可变：定义后元素不能改

### Q11. `sort()` 为什么返回 `None`？
A：`sort()` 走“原地修改”模式，直接改原列表，所以不返回新列表。  
要拿新列表，用 `sorted(...)`。

### Q12. 这类报错分别什么意思？
A：
1. `TypeError: list.append() takes exactly one argument (0 given)`：`append()` 少传参数
2. `AttributeError: 'list' object has no attribute 'split'`：对列表误用了字符串方法 `split`
3. `SyntaxError`（如 `freq(w)`）：把字典索引 `[]` 误写成函数调用 `()`

---

## 4. 调试方法（零基础必看）

## 4.1 四步调试法
1. 先读报错最后一行（真正错误类型）。
2. 再看报错指出的文件和行号。
3. 用 `print` 打印中间变量，确认哪一步偏了。
4. 一次只改一个点，改完立刻重跑。

## 4.2 你应该优先检查的5件事
1. 是否漏了冒号 `:`
2. 缩进是否统一（建议4空格）
3. 变量名是否前后一致
4. 输入是否需要 `int()/float()` 转换
5. 函数是否真的 `return` 了结果

## 4.3 问我问题时最有效格式
1. 完整报错（从 `Traceback` 到最后一行）
2. 相关代码片段（至少报错行上下各5行）
3. 你的预期结果（你本来想得到什么）

---

## 5. Day1/Day2 验收标准（执行版）

## 5.1 Day1 验收
1. `everyday_learning/day1/day1_handwrite.py` 跑通并出现 `Day1 手写练习通过。`
2. 至少记录 1 个“报错 -> 原因 -> 修复”
3. 能口述 `if / elif / else` 的执行顺序

## 5.2 Day2 验收
1. `everyday_learning/day2/day2_handwrite.py` 跑通并出现 `Day2 手写练习通过。`
2. 你能解释 `freq.get(word, 0) + 1` 在做什么
3. 你能解释 `sorted(... key=lambda ...)` 为什么能排 Top10

---

## 6. 速查表（写代码前看30秒）

```python
# 变量
x = 10

# 条件
if x > 0:
    print("pos")
elif x == 0:
    print("zero")
else:
    print("neg")

# 函数
def add(a, b):
    return a + b

# 列表
arr = [3, 1, 2]
arr.append(5)
arr.sort()

# 字典词频
freq = {}
for w in ["a", "b", "a"]:
    freq[w] = freq.get(w, 0) + 1

# 循环
for i in range(3):
    print(i)
```

---

## 7. 后续追加规则（我会持续维护）
1. Day3 已补：函数进阶、字符串处理、正则。
2. Day4 已补：文件IO、异常处理、路径。
3. Day5 已补：PyTorch最小概念（tensor、device、forward、loss、backward、optimizer）。

---

## 8. Day3 讲义：函数进阶 / 字符串处理 / 正则 / clean_text

## 8.1 Day3 目标
Day3 你要完成一个核心函数：`clean_text(text)`。  
输入原始脏文本，输出“干净的英文文本”。

推荐清洗目标：
1. 全部小写
2. 去掉 URL
3. 去掉标点/数字（只保留英文字母和空白）
4. 压缩多余空白

---

## 8.2 函数进阶（函数之间互相调用）

Day3 你会写两个函数：
1. `normalize_spaces(text)`：处理空白
2. `clean_text(text)`：主函数，内部调用 `normalize_spaces`

示例：
```python
def normalize_spaces(text):
    return " ".join(text.split())

def clean_text(text):
    text = text.lower()
    text = normalize_spaces(text)
    return text
```

这种“拆函数”方式有两个好处：
1. 每个函数职责单一，调试更容易。
2. 以后复用方便（比如 Day4 文件清洗时可直接复用）。

---

## 8.3 字符串处理高频方法（Day3版）

### 8.3.1 `lower()`
把大写转小写：
```python
"ML Is FUN".lower()  # "ml is fun"
```

### 8.3.2 `strip()`
去掉首尾空白：
```python
"  hello  ".strip()  # "hello"
```

### 8.3.3 `split()`
按空白切词：
```python
"a   b\tc\n".split()  # ["a", "b", "c"]
```

### 8.3.4 `" ".join(...)`
把词列表按单空格拼回字符串：
```python
" ".join(["a", "b", "c"])  # "a b c"
```

空白归一化经典写法：
```python
def normalize_spaces(text):
    return " ".join(text.split())
```

---

## 8.4 正则表达式 `re`（Day3 只学够用版）

先导入：
```python
import re
```

核心函数：
```python
re.sub(模式, 替换字符串, 原文本)
```

意思：把“匹配模式”的内容替换成指定字符串。

### 8.4.1 去 URL
```python
text = re.sub(r"https?://\S+|www\.\S+", " ", text)
```
含义：
1. 匹配 `http://...` 或 `https://...`
2. 也匹配 `www.xxx...`
3. 用空格替换，避免单词粘连

### 8.4.2 去非字母字符
```python
text = re.sub(r"[^a-z\s]", " ", text)
```
含义：
1. `^` 在 `[]` 里表示“非”
2. `a-z` 表示小写字母
3. `\s` 表示空白字符（空格、Tab、换行）
4. 整体表示：不是字母/空白的都替换为空格

---

### 8.4.3 `\s` 和 `\S+` 的区别（正则高频）
1. `\s`：匹配“一个空白字符”  
   - 空格、Tab、换行都算空白  
   - 例子：在 `"a b"` 里，空格能被 `\s` 匹配到
2. `\S`：匹配“一个非空白字符”  
   - 字母、数字、符号都可以
3. `\S+`：匹配“连续 1 个或多个非空白字符”  
   - `+` 的意思是“前面的模式重复 1 次或多次”  
   - 例子：在 `"https://abc.com xyz"` 里，`https://abc.com` 会被 `\S+` 一次性匹配

对比记忆：
1. 小写 `s`（`\s`）看空白  
2. 大写 `S`（`\S`）看非空白  
3. 加 `+`（`\S+`）表示“连续一整段”

## 8.5 clean_text 推荐标准流程（记住这 4 步）

```python
def clean_text(text):
    text = text.lower()
    text = re.sub(r"https?://\S+|www\.\S+", " ", text)
    text = re.sub(r"[^a-z\s]", " ", text)
    text = " ".join(text.split())
    return text
```

输入：
`"Hello!!!  ML is FUN. Visit https://example.com now, 100% sure."`

输出：
`"hello ml is fun visit now sure"`

---

## 8.6 Day3 常见报错

1. `NameError: name 're' is not defined`
原因：忘记 `import re`

2. `TypeError`（传入不是字符串）
原因：`clean_text` 参数不是 `str`

3. `AssertionError`
原因：清洗顺序错了，或漏了某一步

4. `SyntaxError`（正则字符串写错）
原因：括号/引号漏写，或转义符写错

---

## 8.7 Day3 验收标准（执行版）

1. `everyday_learning/day3/day3_handwrite.py` 断言全部通过
2. 你能口述 `clean_text` 的 4 步流程
3. 你能解释 `re.sub` 这两行各在做什么：
   - 去 URL
   - 去非字母字符

---

## 8.8 Day3 手写文件 TODO 对照表（详细）

你写 `day3_handwrite.py` 时，按这个顺序对照：
1. TODO：转小写
   - 写法：`text = text.lower()`
   - 作用：统一词形（`Python` 和 `python` 合并）
2. TODO：去 URL
   - 写法：`re.sub(r"https?://\\S+|www\\.\\S+", " ", text)`
   - 作用：去掉链接，避免污染词频
3. TODO：去非字母字符
   - 写法：`re.sub(r"[^a-z\\s]", " ", text)`
   - 作用：只保留字母和空白
4. TODO：归一化空白
   - 写法：`text = " ".join(text.split())`
   - 作用：把多个空格/Tab/换行折叠成单空格
5. TODO：返回结果
   - 写法：`return text`

---

## 8.9 `clean_text` 逐行运行轨迹（带例子）

输入：
```text
"Hello!!!  ML\\tis FUN. Visit https://example.com now, 100% sure."
```

执行过程：
1. 小写后  
`"hello!!!  ml\\tis fun. visit https://example.com now, 100% sure."`
2. 去 URL 后  
`"hello!!!  ml\\tis fun. visit   now, 100% sure."`
3. 去非字母字符后  
`"hello     ml\\tis fun  visit   now    sure "`
4. 空白归一化后  
`"hello ml is fun visit now sure"`

最终返回：
```text
hello ml is fun visit now sure
```

---

## 8.10 Day3 常见误区（你容易踩）

1. 忘记 `import re`
2. 写成 `text = text.lower`（少了 `()`，拿到的是方法对象）
3. `[^a-z\\s]` 写成 `[^a-z/s]`（把 `\\s` 写错）
4. 先 `split` 再做正则，导致流程绕、容易错
5. 把 `re.sub(..., "", text)` 用在所有步骤，导致词粘连

---

## 9. Day4 讲义：文件IO / 异常处理 / clean_file

## 9.1 Day4 目标
Day4 的核心是把“字符串清洗”扩展成“文件级清洗”。  
你要做的不是一行文本，而是一个输入文件。

你最终要实现：
1. 从文件读入文本
2. 按行清洗
3. 写回新文件
4. 出错时不崩溃（用 `try-except`）

---

## 9.2 文件IO基础（最常用够用版）

### 9.2.1 打开文件：`open()`
常见形态：
```python
open(path, mode, encoding="utf-8")
```

参数：
1. `path`：文件路径（字符串）
2. `mode`：打开模式
3. `encoding`：编码（文本文件建议固定 `utf-8`）

常用 mode：
1. `"r"`：读文件（文件必须存在）
2. `"w"`：写文件（不存在则创建；存在会覆盖）
3. `"a"`：追加写（写到文件末尾）

### 9.2.2 为什么用 `with open(...) as f`
推荐写法：
```python
with open("a.txt", "r", encoding="utf-8") as f:
    data = f.read()
```
`with open(...) as f` 的意思：

1. `open("a.txt", "r", encoding="utf-8")`：以“读模式”打开文件。  
2. `as f`：把这个打开的文件对象命名为 `f`。  
3. `with`：代码块结束后，自动关闭文件（不用手动 `f.close()`）。

`data = f.read()` 的意思：

1. `f.read()`：把文件全部内容读出来（类型是字符串 `str`）。  
2. `data = ...`：把读到的内容存到变量 `data` 里，后面可继续处理。

所以整体是：  
“打开文件 -> 读全部内容到 `data` -> 自动关文件”。

好处：
1. 用完自动关闭文件
2. 出异常也能自动释放资源
3. 代码更安全、更规范

---

## 9.3 读文件与写文件

### 9.3.1 读文件常见方法
```python
f.read()       # 全部读成一个字符串
f.readline()   # 读一行
f.readlines()  # 读成列表，每个元素是一行
```

Day4 推荐使用 `readlines()`，因为你要逐行清洗。

示例：
```python
with open("in.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
print(lines)
```

### 9.3.2 写文件常见方法
```python
f.write("hello\n")
```

注意：`write()` 不会自动加换行，要你自己写 `\n`。

---

## 9.4 异常处理 `try-except`

模板：
```python
try:
    可能报错的代码
except 某类错误:
    出错后的处理
except Exception as e:
    兜底处理
```

Day4 最常见两类：
1. `FileNotFoundError`：文件不存在
2. 其他未知错误：`Exception as e`

示例：
```python
try:
    with open("not_exists.txt", "r", encoding="utf-8") as f:
        data = f.read()
except FileNotFoundError:
    print("文件不存在")
except Exception as e:
    print("其他错误:", e)
```

补充：`as e` 到底是什么意思（高频）
1. 完整语法：`except 某异常类型 as 变量名:`
2. 含义：当异常发生时，把“异常对象”绑定给这个变量名。
3. `e` 只是变量名，不是关键字；你写成 `err`、`ex` 也可以。
4. 作用：你可以打印异常详情，方便定位问题。

示例：
```python
try:
    x = int("abc")
except Exception as e:
    print(type(e))  # <class 'ValueError'>
    print(e)        # invalid literal for int() with base 10: 'abc'
```

如何理解“异常对象”：
1. `Exception` 像“错误的大类”。
2. 实际抛出的可能是它的子类（比如 `ValueError`、`TypeError`）。
3. `as e` 接到的就是这次真实错误的信息载体。

常见写法建议：
1. 能具体就具体：优先 `except FileNotFoundError as e`。
2. 最后再兜底：`except Exception as e`。
3. 不要只写 `except:`（会把系统中断等也吃掉，不利于排查）。

---

## 9.5 clean_file 推荐实现逻辑（记住这 6 步）

1. `try` 包裹整个读写流程  
2. 读入 `lines`  
3. 对每行执行 `clean_line`  
4. 跳过清洗后为空的行  
5. 写入输出文件（每行补 `\n`）  
6. 成功返回 `True`，失败返回 `False`

参考流程：
```python
def clean_file(input_path, output_path):
    try:
        with open(input_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        cleaned_lines = []
        for line in lines:
            c = clean_line(line)
            if c:
                cleaned_lines.append(c)

        with open(output_path, "w", encoding="utf-8") as f:
            for c in cleaned_lines:
                f.write(c + "\n")

        return True
    except FileNotFoundError:
        return False
    except Exception:
        return False
```

---

## 9.6 Day4 常见报错

1. `FileNotFoundError`
原因：输入文件路径写错或文件不存在。

2. `UnicodeDecodeError`
原因：编码不匹配（没指定 utf-8 或文件实际编码不同）。

3. `PermissionError`
原因：没有写入权限（目录不可写）。

4. `IsADirectoryError`
原因：把目录路径当文件路径打开。

5. 逻辑错误（断言失败）
原因：忘记过滤空行、忘记 `\n`、忘记 `return True/False`。

---

## 9.7 路径与调试建议

1. 路径先用相对路径，保证脚本和文件在同一目录（初学最稳）。  
2. 打印关键中间值：
   - `print(lines)`
   - `print(cleaned_lines)`
   - `print(output_path)`
3. 文件问题先查三件事：
   - 路径对不对
   - 模式对不对（r/w/a）
   - 编码是否 utf-8

---

## 9.8 Day4 验收标准（执行版）

1. `everyday_learning/day4/day4_handwrite.py` 断言全部通过  
2. 你能解释为什么要用 `with open(...)`  
3. 你能解释 `try-except` 里“专门异常 + 兜底异常”的意义  
4. 你能口述 clean_file 的 6 步流程

---

## 9.9 `read / readline / readlines` 对比（详细例子）

假设 `a.txt` 内容是：
```text
hello
ml
rookie
```

三种读取方式：
1. `f.read()`
   - 返回一个完整字符串：`"hello\\nml\\nrookie\\n"`
2. `f.readline()`
   - 每次读一行字符串
   - 第一次：`"hello\\n"`，第二次：`"ml\\n"`
3. `f.readlines()`
   - 返回列表：`["hello\\n", "ml\\n", "rookie\\n"]`

什么时候用：
1. 要整段处理：`read()`
2. 要逐行处理（Day4 常见）：`readlines()` 或 `for line in f`

---

## 9.10 `f.write(...)` 与换行细节

### 9.10.1 基本语法
```python
f.write("hello\\n")
```

含义：
1. 写入字符串 `"hello"`
2. 再写一个换行符 `\n`

### 9.10.2 `\n` 和 `\\n` 区别
1. `"\n"`：真正换行
2. `"\\n"`：两个字符（反斜杠 + n）

### 9.10.3 例子
```python
c = "python"
b = "rocks"
f.write(c + " " + b + "\n")  # 输出一行：python rocks
```

---

## 9.11 Day4 手写文件 TODO 对照表（详细）

1. TODO：写演示输入文件
   - 用 `with open(path, "w", encoding="utf-8")`
2. TODO：`clean_line` 清洗规则
   - 去首尾空白：`strip()`
   - 归一化空白：`" ".join(line.split())`
3. TODO：读文件
   - `readlines()` 拿到行列表
4. TODO：逐行清洗并过滤空行
   - `if c:` 过滤空字符串
5. TODO：写输出文件
   - 每行 `f.write(c + "\\n")`
6. TODO：异常处理
   - `FileNotFoundError` 专门处理
   - `Exception as e` 兜底
7. TODO：返回值
   - 成功 `True`，失败 `False`

---

## 10. Day5 讲义：PyTorch 预热 / Tensor / 训练循环

## 10.1 Day5 目标
Day5 不是做“大模型训练”，而是建立最小训练闭环认知：
1. 会创建 Tensor（数据）
2. 会选择 device（`mps` / `cpu`）
3. 会搭一个线性层 `nn.Linear`
4. 会写完整训练循环：`forward -> loss -> backward -> step`
5. 知道 `zero_grad()`、`no_grad()` 是干嘛的

你今天只要把这条线打通，后面 Week1 才不会卡死。

---

## 10.2 先做环境检查（必须）

在终端先执行：

```bash
export PYTORCH_ENABLE_MPS_FALLBACK=1
/usr/bin/python3 -c "import torch; print(torch.__version__); print('mps:', torch.backends.mps.is_available())"
```

或直接运行你仓库里的检查脚本：

```bash
/usr/bin/python3 "/Users/chenqingan/Library/Mobile Documents/com~apple~CloudDocs/ml-rookie/everyday_learning/day5/day5_env_check.py"
```

解释：
1. `PYTORCH_ENABLE_MPS_FALLBACK=1`：MPS 不支持的算子自动回退 CPU，减少报错中断。
2. `torch.__version__`：确认 PyTorch 已安装。
3. `torch.backends.mps.is_available()`：确认 M4 的 MPS 是否可用。

如果报 `ModuleNotFoundError: No module named 'torch'`，先安装 PyTorch 再继续 Day5。

---

## 10.3 Tensor 是什么

Tensor 可以理解成“可在 GPU/MPS 上计算的多维数组”。  
你可以把它先类比成 `numpy` 数组的 PyTorch 版本。

### 10.3.1 创建 Tensor
```python
import torch

x = torch.tensor([[1.0], [2.0], [3.0]], dtype=torch.float32)
print(x)
```

### 10.3.2 常看三个属性
```python
print(x.shape)   # 形状，如 torch.Size([3, 1])
print(x.dtype)   # 数据类型，如 torch.float32
print(x.device)  # 所在设备，如 cpu 或 mps
```

---

## 10.4 device：为什么要管它

模型和数据必须在同一个 device 上，否则会报错。  
典型报错：`Expected all tensors to be on the same device`

推荐模板：
```python
if torch.backends.mps.is_available():
    device = torch.device("mps")
else:
    device = torch.device("cpu")

x = x.to(device)
model = model.to(device)
```

---

## 10.5 `nn.Linear(1, 1)` 在做什么

线性层本质是：
`y_pred = w * x + b`

```python
import torch.nn as nn

model = nn.Linear(1, 1)
pred = model(x)
```

这里 `w` 和 `b` 是可训练参数，初始是随机值。  
训练的目标就是不断调整 `w,b`，让预测更接近真值。

---

## 10.6 loss：怎么定义“模型好不好”

今天用 `MSELoss`（均方误差）：
```python
loss_fn = nn.MSELoss()
loss = loss_fn(pred, y)
```

直观理解：预测值和真实值差得越远，loss 越大。  
训练就是让 loss 越来越小。

---

## 10.7 `backward()` 和 `optimizer.step()` 是什么关系

### 10.7.1 你必须记住这三句顺序
```python
optimizer.zero_grad()
loss.backward()
optimizer.step()
```

作用拆解：
1. `zero_grad()`：把上一次梯度清零（避免累积污染）。
2. `backward()`：反向传播，计算参数梯度。
3. `step()`：优化器根据梯度更新参数。

顺序乱了，训练就会异常或效果很差。

---

## 10.8 最小训练循环模板（Day5核心）

```python
for epoch in range(epochs):
    pred = model(x)
    loss = loss_fn(pred, y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
```

你今天要观察的不是“高大上指标”，就两件事：
1. `loss` 是否下降
2. `x=4` 的预测是否接近 `9`（因为 `2*4+1=9`）

---

## 10.9 `torch.no_grad()` 什么时候用

在“只预测，不训练”时用：
```python
with torch.no_grad():
    y_pred = model(x_test)
```

作用：
1. 不记录梯度，省内存
2. 防止误把推理过程混进训练图

---

## 10.10 Day5 常见报错（你大概率会遇到）

1. `ModuleNotFoundError: No module named 'torch'`  
原因：没安装 PyTorch。

2. `Expected all tensors to be on the same device`  
原因：数据在 `cpu`，模型在 `mps`（或反过来）。

3. `RuntimeError: MPS backend out of memory`  
原因：张量/模型太大；Day5 基本不会，后续大模型会遇到。

4. loss 不下降  
常见原因：
   - 忘了 `optimizer.step()`
   - 忘了 `loss.backward()`
   - 学习率太大或太小

5. 断言失败：预测值不在范围内  
原因：训练轮数不够，或训练循环写错。

---

## 10.11 Day5 验收标准（执行版）

1. `everyday_learning/day5/day5_handwrite.py` 断言全部通过
2. 你能口述训练循环 5 步：数据 -> 前向 -> loss -> 反向 -> 更新
3. 你能解释为什么要 `zero_grad()`
4. 你能解释为什么推理要用 `torch.no_grad()`
5. 你能解释 device 一致性的要求（模型和数据必须同设备）

---

## 10.12 Git 在 Day5 要不要做

结论：做，但只做最小集，不超过 20 分钟。  
今天的主线是 Day4 + Day5 Python/PyTorch，不是 Git 深挖。

最小命令：
```bash
git init
git add .
git commit -m "complete day4 day5 handwrite"
git log --oneline -n 3
```

你先建立“我会提交一次本地版本”的肌肉记忆即可。  
GitHub 远程仓库可以晚一点再接。

---

## 10.13 Day5 手写文件 TODO 对照表（详细）

1. TODO：`get_device`
   - `mps` 可用就返回 `torch.device("mps")`
   - 否则返回 `torch.device("cpu")`
2. TODO：`make_data`
   - 构造 `x`（形状 `[N,1]`）
   - 构造 `y = 2*x + 1`
   - `x/y` 都放到 `device`
3. TODO：`train_linear`
   - 定义 `model/loss_fn/optimizer`
   - 写训练三连
   - 返回 `model, final_loss`
4. TODO：`predict_one`
   - 构造测试输入 `[[x_value]]`
   - `with torch.no_grad()` 前向推理
   - 返回 float 结果

---

## 10.14 Day5 三组高频语法（你总问到的）

### 10.14.1 `x = x.to(device)`
含义：
1. 右侧 `x.to(device)` 返回“迁移后张量”
2. 左侧再赋值回 `x`
3. 目的是让数据和模型在同设备

### 10.14.2 `final_loss = float(loss.item())`
含义：
1. `loss` 是 Tensor，不是 Python 数字
2. `loss.item()` 取标量值
3. `float(...)` 转为 Python 浮点数，便于打印/比较

### 10.14.3 `with torch.no_grad():`
含义：
1. 进入“无梯度”上下文
2. 推理时更省内存、更稳定
3. 不会污染训练图

---

## 10.15 Day5 常见误区（补充）

1. `nn.linear` 大小写错误（正确是 `nn.Linear`）
2. 忘记 `optimizer.step()`，loss 不降
3. 忘了把数据和模型放到同一设备
4. 以为 `range(epochs)` 是无限循环（其实是固定轮数）
5. 以为 Day5 就是实战项目（其实是训练闭环预热）

---

## 11. Day6 基础课：DataLoader / mini-batch / 训练循环语法（超详细）

> 这一章只做一件事：把你写 Day6 手写文件时会遇到的“语法和概念坑”全部提前讲清楚。  
> `##11` 是基础语法课，`##12` 是完整任务课。先 11，再 12，写 handwrite 会顺很多。

## 11.1 你为什么会在 Day6 卡住
最常见卡点不是“数学不会”，而是这些语法点没打通：
1. `torch.utils.data` 到底是什么
2. `DataLoader(...)` 各参数在干嘛
3. `for xb, yb in loader` 这句语法到底怎么解包
4. `train/eval/no_grad` 应该放哪
5. batch 训练为什么复杂度仍是 `O(n)`

这章就是把这些点拆开讲。

---

## 11.2 先统一术语（写代码前必须统一口径）

### 11.2.1 sample（样本）
一条数据。  
比如 MNIST 一条样本是：一张数字图 + 一个标签（0~9）。

### 11.2.2 batch（小批）
一次喂给模型的一组样本。  
例如 `batch_size=128`，表示一次处理 128 张图。

### 11.2.3 epoch（轮次）
把整个训练集完整走一遍，叫 1 个 epoch。

### 11.2.4 step / iteration（一步更新）
每处理一个 batch 并执行一次 `optimizer.step()`，叫一步更新。

小例子：
1. 训练集有 60000 条
2. `batch_size=128`
3. 每个 epoch 大约有 `60000/128 ≈ 469` 步更新

---

## 11.3 `torch.utils.data` 是什么（命名也讲清）

你会看到：
```python
from torch.utils.data import DataLoader
```

拆开看：
1. `torch`：PyTorch 顶层包
2. `utils`：utilities，工具模块
3. `data`：数据管道模块

所以 `torch.utils.data` 就是“PyTorch 的数据工具箱”。

命名规则：
1. 模块通常小写（`utils`, `data`）
2. 类通常驼峰（`DataLoader`, `TensorDataset`）
3. 点号表示层级路径（包.子包.模块）

---

## 11.4 `DataLoader(...)` 语法逐项拆解

最常见写法：
```python
train_loader = DataLoader(train_ds, batch_size=128, shuffle=True)
test_loader = DataLoader(test_ds, batch_size=512, shuffle=False)
```

参数解释：
1. 第一个参数 `train_ds/test_ds`：数据集对象（比如 `datasets.MNIST(...)`）
2. `batch_size`：一次取多少条
3. `shuffle`：每个 epoch 开始时是否打乱顺序

`train_ds` / `test_ds` 的完整由来语句（从源头到可用）：
```python
from torchvision import datasets, transforms

transform = transforms.ToTensor()

train_ds = datasets.MNIST(
    root="data",
    train=True,
    transform=transform,
    download=True
)

test_ds = datasets.MNIST(
    root="data",
    train=False,
    transform=transform,
    download=True
)
```

参数逐项细拆（你问的重点）：

1. `root="data"` 到底是什么意思  
   - `root` 是“数据集存放根目录”参数。  
   - 写成 `"data"` 是相对路径，表示当前工作目录下的 `data/` 文件夹。  
   - 如果你在项目根目录运行脚本，它通常对应：`.../ml-rookie/data`。  
   - 更稳的写法（不依赖当前终端位置）：
```python
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
train_ds = datasets.MNIST(root=str(DATA_DIR), train=True, transform=transform, download=True)
```

2. `download=True` 是什么意思  
   - 含义：如果本地没有数据，就自动下载；有了就复用，不会每次都重新下载。  
   - 如果写 `download=False` 且本地没数据，通常会报找不到数据集。  
   - “去哪里下载”不是你手写的，`torchvision.datasets.MNIST` 类内部已经写好镜像地址。  
   - 你本机当前 `MNIST.mirrors` 是：
     - `https://ossci-datasets.s3.amazonaws.com/mnist/`
     - `http://yann.lecun.com/exdb/mnist/`
   - 具体下载文件（类里也写好了）是 4 个 gzip 包（训练图像/训练标签/测试图像/测试标签）。

3. `transform=transform` 是什么意思  
   - 这里传入的是“预处理函数（可调用对象）”。  
   - `transform = transforms.ToTensor()` 的作用：
     - 把图片转成 PyTorch Tensor
     - 把像素从 `0~255` 归一到 `0~1`
     - 对 MNIST（灰度图）输出形状通常是 `[1, 28, 28]`
   - 这个变换不是一次性提前改完所有数据，而是“每次取样本时”自动执行。

4. `train=True/False` 再强调一次  
   - `train=True`：构造训练集对象（约 6 万张）。  
   - `train=False`：构造测试集对象（约 1 万张）。

一句话总流程：
1. 指定数据放哪（`root`）
2. 需要就自动下载（`download=True`）
3. 取样本时做预处理（`transform=ToTensor()`）
4. 根据 `train` 选择训练集或测试集

为什么训练集常 `shuffle=True`：
1. 减少样本顺序带来的偏差
2. 训练更稳定

为什么测试集常 `shuffle=False`：
1. 评估不需要随机性
2. 更便于复现和排查问题

### 11.4.1 DataLoader 本身到底是什么
一句话：`DataLoader` 是“按批次取数据的迭代器对象”。

你可以把它想成“传送带”：
1. `Dataset` 里放的是全量样本（仓库）。
2. `DataLoader` 决定每次搬多少、是否打乱（传送带规则）。
3. `for xb, yb in loader` 时，它每轮给你一批 `(输入, 标签)`。

关系图（文字版）：
1. `Dataset`：我有哪些数据
2. `DataLoader`：我怎么一批一批拿数据
3. 训练循环：我拿到这一批后怎么训练

### 11.4.2 “打包成张量”是什么意思（带例子）
“打包成张量”就是：把多条样本堆叠成一个 batch 的大张量。

先看单条样本（MNIST）：
1. 一张图 `x` 的形状是 `[1, 28, 28]`
2. 一个标签 `y` 是一个整数，比如 `7`

如果 `batch_size=4`，DataLoader 一次拿 4 条，会变成：
1. `xb` 形状：`[4, 1, 28, 28]`
2. `yb` 形状：`[4]`，例如 `[7, 2, 1, 9]`

这就叫“把一批样本打包成张量”。

再看最小代码感受：
```python
for xb, yb in train_loader:
    print(xb.shape, yb.shape)
    break
```
可能输出：
```text
torch.Size([128, 1, 28, 28]) torch.Size([128])
```

解释：
1. 前面的 `128` 是 batch 大小。
2. 后面的 `1, 28, 28` 是单张图结构。
3. 标签只有类别编号，所以是 `[128]`。

---

## 11.5 `for xb, yb in loader` 到底是什么语法

这是“解包赋值”语法。

先看通用例子：
```python
pairs = [(1, 10), (2, 20)]
for a, b in pairs:
    print(a, b)
```

`loader` 也是类似：每次吐出一个二元结构 `(inputs, labels)`，所以可以写：
```python
for xb, yb in loader:
    ...
```

含义：
1. `xb`：这一批输入（batch x）
2. `yb`：这一批标签（batch y）

变量名不是固定的，你也可写 `batch_x, batch_y`。

---

## 11.6 在 MNIST 里，`xb/yb` 的形状大概是什么

假设 `batch_size=128`：
1. `xb.shape` 常见是 `[128, 1, 28, 28]`
2. `yb.shape` 常见是 `[128]`

解释：
1. `128`：这一批有 128 张图
2. `1`：灰度通道数
3. `28,28`：图像高宽
4. 标签是一维类别编号列表（每个值 0~9）

---

## 11.7 Day6 训练循环的标准位置关系

```python
for epoch in range(epochs):     # 外层：轮次
    model.train()               # 训练模式

    for xb, yb in train_loader: # 内层：每个 batch
        xb = xb.to(device)
        yb = yb.to(device)

        logits = model(xb)
        loss = loss_fn(logits, yb)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
```

你要死记硬背的顺序：
1. `forward`
2. `loss`
3. `zero_grad`
4. `backward`
5. `step`

---

## 11.8 评估循环为什么和训练循环不同

评估时要写：
```python
model.eval()                               # 1) 切到评估模式：告诉模型“现在不是训练”
correct, total = 0, 0                      # 2) 同时初始化两个计数器：答对数/总样本数
with torch.no_grad():                      # 3) 上下文管理器：评估时关闭梯度计算，省内存更快
    for xb, yb in test_loader:             # 4) for + 解包：每轮从测试集取一批 (输入, 标签)
        xb = xb.to(device)                 # 5) 把这一批输入放到 device（cpu/mps）上
        yb = yb.to(device)                 # 6) 把这一批标签也放到同一 device，避免设备不一致报错
        logits = model(xb)                 # 7) 前向推理：得到每个类别的原始分数 logits
        pred_label = logits.argmax(dim=1)  # 8) 按类别维取最大分数下标 -> 预测类别 id
        correct += (pred_label == yb).sum().item()  # 9) 先比较得到布尔张量(对=True/错=False)；.sum()会把True当1、False当0求和=本批答对个数；.item()把单元素张量转成Python数字，便于与correct(普通整数)相加
        total += yb.size(0)                # 10) yb.size(0) 是本批样本数，累加到总数
        # 例子（对应第 1954-1956 行，step by step）：
        # 假设当前 batch 有 3 张图，model(xb) 得到：
        # logits = [[0.1, 2.3, 0.2], [1.8, 0.2, 0.1], [0.3, 0.4, 0.9]]
        # 第 1955 行 argmax(dim=1) 后：pred_label = [1, 0, 2]
        # 假设真实标签 yb = [1, 2, 2]
        # 比较 (pred_label == yb) 得到：[True, False, True]
        # 第 1956 行 .sum() 后是 2（True 按 1、False 按 0），.item() 把它变成 Python 数字 2
        # 所以这一批会让 correct 增加 2

acc = 100.0 * correct / total              # 11) 准确率公式：答对/总数，再乘 100 变百分比
print("test acc:", acc)                    # 12) 打印最终测试准确率，便于日志记录
```

原因：
1. `model.eval()`：切到评估模式（某些层行为会变）
2. `torch.no_grad()`：不计算梯度，省内存、加速推理

训练和评估要分开，不要混写。

---

## 11.9 为什么 batch 训练仍是 `O(n)`

设：
1. 总样本数 `n`
2. batch 大小 `b`

每个 epoch 的 batch 数约 `n/b`，每个 batch 处理 `b` 条，所以总量：
`(n/b) * b = n`

所以每个 epoch 主阶仍是 `O(n)`。  
batch 改变的是“内存占用和更新频率”，不是主阶复杂度。

---

## 11.10 Day6 手写文件 TODO 对照表（重点）

你写 `day6_handwrite.py` 时，按这个映射：
1. `get_device`：
   - 会写 `torch.device("mps")` 和 `torch.device("cpu")`
2. `build_loaders`：
   - 会写 `datasets.MNIST(...)`
   - 会写 `DataLoader(..., batch_size=..., shuffle=...)`
3. `build_model`：
   - 会写 `nn.Sequential(...)`
4. `train_one_epoch`：
   - 会写 `for xb, yb in train_loader`
   - 会写训练三连
5. `evaluate_acc`：
   - 会写 `model.eval()` + `torch.no_grad()`
   - 会写 `argmax(dim=1)` 统计准确率
6. `train_pipeline`：
   - 会写两阶段训练和指标记录

---

## 11.11 Day6 常见错误（按概率排序）

1. 设备不一致
   - 报错关键词：`Expected all tensors to be on the same device`
   - 处理：检查 `model/xb/yb` 是否都 `.to(device)`

2. `for xb, yb in loader` 写错缩进
   - 处理：保证内层循环在 epoch 循环内部

3. 忘了 `optimizer.zero_grad()`
   - 后果：梯度累积，训练异常

4. 评估阶段忘记 `no_grad`
   - 后果：不必要的显存/内存占用

5. `argmax` 维度写错
   - 分类任务通常是 `argmax(dim=1)`

---

## 11.12 你写代码前先口述这 6 句
1. loader 每次吐的是 `(xb, yb)`
2. 训练集要 shuffle，测试集一般不 shuffle
3. 一个 epoch 是看完全部样本一次
4. batch 训练每个 epoch 复杂度仍是 `O(n)`
5. 训练时 `model.train()`，评估时 `model.eval()`
6. 评估要用 `torch.no_grad()`

---

## 11.13 Day6 和 LeetCode 的关系
Day6 建议顺序：
1. 先做 Day6 手写（ML 主线）
2. 再做 LeetCode 1 题（算法手感）

这样不会只刷题，也不会让 ML 主线断掉。

---

## 12. Day6（Week1 启动）讲义：MNIST baseline（MLP，超详细版）

> 执行以本章节为准。  
> 这一章目标：从“会写训练循环”升级到“会跑完整分类任务（数据->训练->评估->记录）”。

## 12.1 Day6 目标（你要交付什么）
1. 跑通 MNIST 训练脚本（`mps` 优先，失败回退 `cpu`）。
2. 使用 baseline 模型：`Flatten -> Linear -> ReLU -> Linear`。
3. 两阶段指标：
   - Phase1：测试集准确率 `>= 92%`
   - Phase2：测试集准确率 `>= 95%`
4. 记录 4 个结果：
   - `final loss`
   - `phase1 test acc`
   - `phase2 test acc`
   - `elapsed sec`（训练耗时，秒）

---

## 12.2 Day6 你会用到哪些文件
1. 手写：`everyday_learning/day6/day6_handwrite.py`
2. 参考：`everyday_learning/day6/day6_solution.py`
3. 环境检查：`everyday_learning/day6/day6_env_check.py`

学习顺序：
1. 先看本讲义（20-30 分钟）
2. 再写 handwrite
3. 卡住再看 solution

---

## 12.3 先讲语法：`import ...` 到底是什么

你会看到：

```python
import time
from pathlib import Path
```

含义：
1. `import time`：导入 `time` 模块（计时用）。
2. `from pathlib import Path`：从 `pathlib` 模块里导入 `Path` 类（路径处理用）。

为什么不“默认全导入”：
1. 启动慢、内存占用高。
2. 命名冲突风险高。
3. 代码可读性差（你看不出用了哪些能力）。

---

## 12.4 `Path` 与计时语法（Day6 必会）

### 12.4.1 路径语法
```python
base_dir = Path(__file__).resolve().parent
data_dir = base_dir / "data"
data_dir.mkdir(parents=True, exist_ok=True)
```

解释：
1. `__file__` 是什么  
   - `__file__` 是 Python 在“脚本运行模式”下自动提供的变量。  
   - 它保存“当前这个 `.py` 文件”的路径（通常是相对或绝对路径字符串）。  
   - 注意：在交互式终端/某些 notebook 场景里，`__file__` 可能不存在。

2. `Path(__file__)` 是什么  
   - `Path(...)` 把字符串路径包装成 `Path` 对象。  
   - 目的：后续可以用 `.parent`、`.mkdir()`、`/` 拼接等“路径专用方法”，比手写字符串更安全。

3. `.resolve()` 是什么  
   - 作用：把路径“解析成绝对路径”，并规范化 `.`、`..` 等部分。  
   - 例如：`"./everyday_learning/day6/day6_handwrite.py"` 可能被解析成  
     `/Users/chenqingan/Library/Mobile Documents/com~apple~CloudDocs/ml-rookie/everyday_learning/day6/day6_handwrite.py`

4. `.parent` 是什么  
   - `parent` 表示“上一级目录”。  
   - 所以 `Path(__file__).resolve().parent` 的结果就是：当前脚本所在文件夹路径。  
   - 这也是为什么变量名叫 `base_dir`（基础目录）。

5. `base_dir / "data"` 为什么能这样写  
   - 这里的 `/` 不是数学除法，而是 `Path` 对象重载后的“路径拼接运算符”。  
   - 等价于“在 `base_dir` 下再进入一个 `data` 子目录”。  
   - 好处：自动处理不同系统的路径分隔符，比字符串拼接稳定。

6. `mkdir(parents=True, exist_ok=True)` 逐项解释  
   - `mkdir`：创建目录的方法。  
   - `parents=True`：如果上级目录不存在，连上级一起创建（递归创建）。  
   - `exist_ok=True`：如果目录已经存在，不报错，直接继续执行。  
   - 实战意义：脚本可重复运行，不会因为“目录已存在”而中断。

7. 一口气串起来理解这三行  
   - 第 1 行：拿到“当前脚本所在目录”作为 `base_dir`  
   - 第 2 行：在该目录下定义 `data_dir = base_dir/data`  
   - 第 3 行：确保 `data_dir` 这个目录一定存在（不存在就创建）

### 12.4.2 耗时语法
```python
start = time.perf_counter()
# ...训练...
elapsed = time.perf_counter() - start
```
`time.perf_counter()` 是“模块.函数调用”语法。

拆开看：

1. `time`：模块名（你前面 `import time` 导入的）。  
2. `perf_counter`：这个模块里的函数名。  
3. `()`：调用函数执行。  

它返回一个高精度计时值（秒，浮点数），常用于测耗时。

典型写法：

```python
start = time.perf_counter()
# 这里跑训练
elapsed = time.perf_counter() - start
```

所以它在这里属于：  
`赋值语句 + 函数调用 + 浮点运算`。

`elapsed sec` 就是“已耗时（秒）”。
补充：每次调用 `time.perf_counter()`，都会返回“调用当下这一刻”的高精度计时值（单调递增），通常不用看绝对值本身，而是用“两次调用之差”来计算耗时。

---

## 12.5 `torch.device("mps")` 为什么要加引号

示例：
```python
torch.device("mps")
```

`"mps"` 必须是字符串：
1. 加引号：表示文本常量（设备名）。
2. 不加引号：Python 会把 `mps` 当变量名，通常报 `NameError`。

同理：`"cpu"`、`"cuda"` 也都要加引号。

---

## 12.6 MNIST 是什么，为什么用它

MNIST：
1. 训练集 60000 张
2. 测试集 10000 张
3. 图片大小 28x28 灰度图
4. 标签是数字类别 0~9

优点：
1. 数据标准，教程多。
2. MLP 很容易收敛。
3. 适合零基础完成“第一次分类闭环”。

---

## 12.7 `datasets.MNIST(...)` 语法拆解

示例：
```python
from torchvision import datasets, transforms

transform = transforms.ToTensor()
train_ds = datasets.MNIST(root="data", train=True, transform=transform, download=True)
test_ds = datasets.MNIST(root="data", train=False, transform=transform, download=True)
```

先补充：`transforms.ToTensor()` 到底做了哪些预处理（你问的重点）

它通常做 3 件事：
1. 数据类型转换：把图像数据转成 PyTorch 的 `torch.Tensor`。  
2. 维度顺序转换：常见图像从 `H x W x C` 转成 `C x H x W`。  
3. 数值范围归一：若输入是常见 `uint8` 图像（0~255），会除以 255 变成 `0.0~1.0` 的 `float32`。

为什么这么做：
1. 神经网络（尤其 PyTorch 模型）期望输入是 Tensor，而不是 PIL 图片对象。  
2. PyTorch 的卷积层默认用 `C x H x W`。  
3. 把像素缩到 `0~1`，训练更稳定，梯度更健康。

例子 1（灰度像素值变化）：
1. 原像素 `0` -> `0.0`  
2. 原像素 `128` -> `0.5019`（约等于 `128/255`）  
3. 原像素 `255` -> `1.0`

例子 2（MNIST 单张图形状变化）：
1. 原图（灰度）可理解为 `28 x 28`。  
2. `ToTensor()` 后会变成 `1 x 28 x 28`（`1` 是通道数，灰度图只有 1 个通道）。

小提醒（进阶但实用）：
1. `ToTensor()` 只做“转 Tensor + 基础归一”，不做“均值方差标准化”。  
2. 如果后续要标准化，通常再加：`transforms.Normalize(mean, std)`。

这三行逐行拆解：

### 12.7.1 第 1 行：`transform = transforms.ToTensor()`
这行是在“定义预处理规则”。

1. 左边 `transform`：你自己定义的变量名。  
2. 右边 `transforms.ToTensor()`：调用 torchvision 里的函数，返回一个“可调用的预处理对象”。  
3. 后面传 `transform=transform` 时，就会对每个样本自动执行这个预处理。

一句话：先把“图像 -> 张量”的规则存到 `transform` 里，后面复用。

### 12.7.2 第 2 行：`train_ds = datasets.MNIST(...)`
这行是“构造训练集对象”。

参数详细解释：
1. `root="data"`
   - 数据保存目录是 `data` 文件夹（相对当前运行目录）。
   - 如果目录不存在，下载时会自动创建。
2. `train=True`
   - 表示取训练集（60000 张）。
3. `transform=transform`
   - 每次取样本时自动做 `ToTensor`。
   - 所以你拿到的不是 PIL 图像，而是 Tensor。
4. `download=True`
   - 本地没有 MNIST 就下载。
   - 本地已有就直接复用，不重复下载。

### 12.7.3 第 3 行：`test_ds = datasets.MNIST(...)`
这行和训练集构造几乎一样，只改了一个关键参数：

1. `train=False`：取测试集（10000 张）。  
2. 其他参数一致：路径一致、预处理一致、自动下载策略一致。

为什么训练集和测试集都要用同一个 `transform`：
1. 保证输入格式一致（都变成 Tensor）。  
2. 保证数值范围一致（都在 [0,1]）。

### 12.7.4 这三个对象最终是什么
1. `transform`：预处理规则对象（“怎么处理每张图”）。  
2. `train_ds`：训练集 Dataset 对象（可索引）。  
3. `test_ds`：测试集 Dataset 对象（可索引）。

你可以立刻验证：
```python
print(type(train_ds))
print(len(train_ds), len(test_ds))
x0, y0 = train_ds[0]
print(x0.shape, x0.dtype, y0)
```

典型输出含义：
1. `len(train_ds)=60000`，`len(test_ds)=10000`。  
2. `x0.shape` 常见是 `torch.Size([1, 28, 28])`。  
3. `x0.dtype` 常见是 `torch.float32`。  
4. `y0` 是类别编号（0~9 的整数）。

### 12.7.5 常见误区
1. 误区：`root="data"` 是“引入一个必须已存在的目录”。  
   正解：它是“指定保存路径”，不存在会创建。
2. 误区：`download=True` 每次都重新下载。  
   正解：已有数据时不会重复下载。
3. 误区：`train_ds` 里已经是 batch。  
   正解：`train_ds` 是单样本级别，batch 由 `DataLoader` 负责。

---

## 12.7.6 `datasets.MNIST` 的“源头”与调用链（硬件/C 思维版）

你这个问题非常关键：`MNIST` 不是“凭空可用”，它有明确定义源头。

调用链：
1. 你写 `from torchvision import datasets`
2. Python 会加载 `torchvision.datasets` 模块
3. 该模块对外暴露了 `MNIST` 这个类
4. 所以 `datasets.MNIST` 指向的是一个类对象
5. 你写 `datasets.MNIST(...)` 时，本质是在实例化这个类

你当前环境里的真实位置（可验证）：
1. `datasets` 入口模块：
   - `.../site-packages/torchvision/datasets/__init__.py`
2. `MNIST` 类定义文件：
   - `.../site-packages/torchvision/datasets/mnist.py`
3. 类全名：
   - `torchvision.datasets.mnist.MNIST`

和 C 的类比：
1. `datasets` 像“导出符号入口”
2. `mnist.py` 是具体实现
3. `datasets.MNIST(...)` = 通过入口拿到符号并构造实例

你可以自己打印验证：
```python
import inspect
from torchvision import datasets

print(inspect.getfile(datasets))         # datasets 入口文件
print(inspect.getfile(datasets.MNIST))   # MNIST 定义文件
print(datasets.MNIST.__module__)         # 类所属模块
```

---

## 12.8 `transforms.ToTensor()` 在做什么

作用是两步：
1. 把图像对象转成 PyTorch Tensor。
2. 像素值从 `0~255` 归一化到 `0~1`。

例子：
1. 像素 `0 -> 0.0`
2. 像素 `128 -> 0.502...`
3. 像素 `255 -> 1.0`

为什么这么做：
1. 数值范围更稳定。
2. 训练更容易收敛。

---

## 12.9 `DataLoader` 与 batch 语法

示例：
```python
from torch.utils.data import DataLoader

train_loader = DataLoader(train_ds, batch_size=128, shuffle=True)
test_loader = DataLoader(test_ds, batch_size=512, shuffle=False)
```

参数解释：
1. `batch_size=128`：每次喂 128 张图。
2. `shuffle=True`：每个 epoch 打乱训练集顺序。
3. `shuffle=False`：测试集通常不打乱。

为什么 batch 训练仍然是 `O(n)`：
1. 1 个 epoch 仍要看完全部 `n` 个样本。
2. 只是把一次全量喂入改成多次小批喂入。
3. 主阶不变，仍是线性遍历数据。

---

## 12.10 baseline 模型语法：`nn.Sequential(...)`

```python
model = nn.Sequential(
    nn.Flatten(),
    nn.Linear(28 * 28, 128),
    nn.ReLU(),
    nn.Linear(128, 10),
)
```

解释：
1. `nn.Sequential` 不是你自己命名，是官方类。
2. 它把多个模块按顺序串起来。
3. 四个模块里真正有可训练参数的是两层 `Linear`。

逐层理解：
1. `Flatten`：`[B,1,28,28] -> [B,784]`
2. `Linear(784,128)`：全连接层
3. `ReLU`：激活函数
4. `Linear(128,10)`：输出 10 类分数

---

## 12.11 `logits` 是什么

`logits` = 模型最后一层输出的“原始分数”。
1. 不是概率。
2. 可以是负数。
3. 分数最大那一类通常是预测类别。

例子：
`[1.2, -0.5, 3.1]`  
最大是第 3 类，所以预测类是 `2`（从 0 开始计）。

---

## 12.12 为什么这次用 `CrossEntropyLoss`，不用 `MSELoss`

这次是多分类任务（0~9），标准损失是 `CrossEntropyLoss`。

你记住：
1. 输入：`logits`（不手动 softmax）
2. 标签：类别整数（0~9）
3. 作用：正确类别分数越高，loss 越小

而 `MSELoss` 更适合回归（预测连续值），不是分类首选。

一个直觉例子：
1. 真值类别是 2，模型给真值类概率高 -> loss 小。
2. 真值类别概率很低 -> loss 大（惩罚重）。

---

## 12.13 训练循环（Day6 版）

```python
for epoch in range(epochs):
    model.train()
    for xb, yb in train_loader:
        xb = xb.to(device)
        yb = yb.to(device)

        logits = model(xb)
        loss = loss_fn(logits, yb)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
```

逐行核心：
1. `model.train()`：开启训练模式。
2. `for xb, yb in loader`：每轮拿一批数据。
3. `to(device)`：模型和数据设备一致。
4. `zero_grad -> backward -> step`：训练三连。

---

## 12.14 准确率三行代码详细解释

```python
pred_label = logits.argmax(dim=1)
correct += (pred_label == yb).sum().item()
acc = 100.0 * correct / total
```

解释：
1. `argmax(dim=1)`：每个样本取分数最大的类别下标。
2. `(pred_label == yb)`：逐个比较对错。
3. `.sum().item()`：统计这一批答对几个。
4. `100.0 * correct / total`：转成百分比准确率。

小例子：
1. `pred=[1,0,2,0]`
2. `label=[1,2,2,0]`
3. 对错是 `[T,F,T,T]`，正确 3/4
4. `acc = 75.0`

---

## 12.15 Day5（整批）和 Day6（小批）区别

1. Day5：整批训练
   - 每个 epoch 常是 1 次更新
2. Day6：小批训练
   - 每个 epoch 多次更新（每个 batch 一次）
3. Day6 更接近真实工程训练流程。

---

## 12.16 两阶段目标怎么跑

Phase1：
1. 训练 1 个 epoch
2. 测试准确率先看 `>= 92%`

Phase2：
1. 在同一模型继续训练 1 个 epoch
2. 测试准确率冲到 `>= 95%`

记录：
1. `final loss`
2. `phase1 acc`
3. `phase2 acc`
4. `elapsed sec`

---

## 12.17 MPS 优先、失败回 CPU（保底策略）

推荐逻辑：
1. 优先 `torch.device("mps")`
2. 若 MPS 训练抛 `RuntimeError`，自动回退 `cpu`

这样能保证“今天一定跑完”。

---

## 12.18 Day6 常见报错与定位

1. `ModuleNotFoundError: No module named 'torchvision'`
   - 解决：`/usr/bin/python3 -m pip install torchvision`
2. 设备不一致错误
   - 检查 `model/xb/yb` 是否都在同一 device
3. 准确率不达标
   - 先检查训练循环顺序
   - 再检查是否确实跑了两阶段
4. 速度慢
   - CPU 慢是正常现象，先求跑通

---

## 12.19 Day6 验收标准（执行版）
1. `everyday_learning/day6/day6_handwrite.py` 断言通过
2. 你能解释：
   - `logits` 是什么
   - `CrossEntropyLoss` 为什么用于分类
   - `argmax(dim=1)` 为什么能拿到预测类别
3. 你能说清：
   - `final loss`
   - `phase1 acc`
   - `phase2 acc`
   - `elapsed sec`

---

## 12.20 Day6 命令（直接跑）

环境检查：
```bash
/usr/bin/python3 "/Users/chenqingan/Library/Mobile Documents/com~apple~CloudDocs/ml-rookie/everyday_learning/day6/day6_env_check.py"
```

手写版：
```bash
/usr/bin/python3 "/Users/chenqingan/Library/Mobile Documents/com~apple~CloudDocs/ml-rookie/everyday_learning/day6/day6_handwrite.py"
```

参考解：
```bash
/usr/bin/python3 "/Users/chenqingan/Library/Mobile Documents/com~apple~CloudDocs/ml-rookie/everyday_learning/day6/day6_solution.py"
```

---

## 13. 注释版附录（按你要求：语法 + 目的 + 为什么 + `.xxx` 功能）

> 这一章专门给你“对照手写文件”用。  
> 每段代码都带详细注释：
> 1. 这行是什么语法
> 2. 为什么这么写
> 3. 目的是什么
> 4. `.xxx` 方法在做什么

## 13.1 先看：`.xxx` 到底是什么语法

在 Python 里，点号 `.` 的作用是“访问对象的属性或方法”。

例子：
1. `text.lower()`
   - `text` 是字符串对象
   - `.lower` 是字符串的方法
   - `()` 表示调用这个方法
2. `x.to(device)`
   - `x` 是张量对象
   - `.to(...)` 是张量的方法
   - 作用是迁移设备/转换类型

你可以把 `对象.方法(参数)` 理解成：
“让这个对象执行某个内置动作”。

---

## 13.2 Day3 注释版：`clean_text`

```python
import re  # 语法：导入模块；目的：使用正则替换 re.sub


def clean_text(text):
    # 语法：函数定义。参数 text 是输入字符串，return 是输出字符串

    # 目的：统一大小写，减少词形分裂（Python/python）
    # .lower()：字符串方法，返回全小写新字符串
    text = text.lower()

    # 目的：去掉 URL，避免链接污染文本
    # re.sub(pattern, repl, string)：把匹配 pattern 的部分替换为 repl
    # r"..." 是原始字符串，避免反斜杠转义干扰
    text = re.sub(r"https?://\S+|www\.\S+", " ", text)

    # 目的：只保留 a-z 和空白，其他符号/数字都替换成空格
    # [^a-z\s]：^ 在 [] 内表示“非”；\s 表示空白字符
    text = re.sub(r"[^a-z\s]", " ", text)

    # 目的：空白归一化，压成单空格
    # .split()：按任意空白切词（多个空格/Tab/换行都会处理）
    # " ".join(list)：把词列表用单空格拼回字符串
    text = " ".join(text.split())

    # 语法：return 返回最终清洗结果
    return text
```

---

## 13.3 Day4 注释版：`clean_file`

```python
def clean_line(line):
    # 目的：把一行文本做最小清洗（去首尾空白 + 归一化空白）
    # .strip()：去掉首尾空白字符
    # .split() + .join()：把内部多空白压成单空格
    return " ".join(line.strip().split())


def clean_file(input_path, output_path):
    # 语法：try-except 异常处理框架；目的：出错时不崩溃
    try:
        # 语法：with open(...) as f，离开代码块自动关闭文件
        with open(input_path, "r", encoding="utf-8") as f:
            # .readlines()：读取所有行，返回列表，每个元素是一行字符串
            lines = f.readlines()

        cleaned_lines = []  # 语法：创建空列表，收集清洗后的行

        # 语法：for 循环遍历每一行
        for line in lines:
            c = clean_line(line)

            # 语法：if c；目的：过滤空行（空字符串在布尔上下文是 False）
            if c:
                # .append(x)：列表方法，把元素追加到末尾
                cleaned_lines.append(c)

        with open(output_path, "w", encoding="utf-8") as f:
            for c in cleaned_lines:
                # .write(str)：写入字符串；不会自动换行，所以手动 + "\n"
                f.write(c + "\n")

        return True  # 成功标记

    except FileNotFoundError:
        # 目的：专门处理文件不存在
        return False

    except Exception as e:
        # e 是异常对象变量，保存具体错误信息
        print("其他错误:", e)
        return False
```

---

## 13.4 Day5 注释版：最小训练循环

```python
import torch
import torch.nn as nn


# 语法：函数定义；目的：确定当前运算设备
# torch.backends.mps.is_available()：检查 MPS 后端是否可用
def get_device():
    if torch.backends.mps.is_available():
        return torch.device("mps")  # "mps" 必须是字符串设备名
    return torch.device("cpu")


# 构造训练数据 y = 2x + 1
def make_data(device):
    # torch.tensor(..., dtype=..., device=...)：创建张量并放到指定设备
    x = torch.tensor([[1.0], [2.0], [3.0], [4.0], [5.0]], dtype=torch.float32, device=device)
    y = 2 * x + 1
    return x, y


def train_linear(x, y, device, epochs=300, lr=0.05):
    # nn.Linear(in_features, out_features)：线性层
    model = nn.Linear(1, 1).to(device)  # .to(device)：把模型参数迁移到设备

    loss_fn = nn.MSELoss()  # 回归任务常用均方误差
    optimizer = torch.optim.SGD(model.parameters(), lr=lr)  # 优化器对象

    final_loss = None
    for epoch in range(epochs):
        pred = model(x)              # 前向计算（forward）
        loss = loss_fn(pred, y)      # 计算损失

        optimizer.zero_grad()        # 清空上一步梯度（梯度默认会累加）
        loss.backward()              # 反向传播，计算当前梯度
        optimizer.step()             # 根据梯度更新参数

        # loss.item()：把标量 Tensor 取成 Python 数值
        final_loss = float(loss.item())

    return model, final_loss


def predict_one(model, device, x_value=4.0):
    x_test = torch.tensor([[x_value]], dtype=torch.float32, device=device)

    # with 语法 + no_grad：进入无梯度上下文，推理更省内存
    with torch.no_grad():
        y_pred = model(x_test)

    return float(y_pred.item())
```

---

## 13.5 Day6 注释版：MNIST 数据 + 训练 + 评估

```python
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms


# 1) 定义预处理规则
# transforms.ToTensor()：把图像转成 Tensor，并把像素从 0~255 归一化到 0~1
transform = transforms.ToTensor()

# 2) 构造训练集 / 测试集对象
# datasets.MNIST(...)：实例化数据集类
# root：数据目录；train=True/False：训练集/测试集；download=True：无数据就下载
train_ds = datasets.MNIST(root="data", train=True, transform=transform, download=True)
test_ds = datasets.MNIST(root="data", train=False, transform=transform, download=True)

# 3) 用 DataLoader 做批量读取
# batch_size：每批样本数；shuffle=True 只建议训练集
train_loader = DataLoader(train_ds, batch_size=128, shuffle=True)
test_loader = DataLoader(test_ds, batch_size=512, shuffle=False)

# 4) 模型定义
# nn.Sequential(...)：顺序组合多个模块
model = nn.Sequential(
    nn.Flatten(),            # 把 [B,1,28,28] 拉平到 [B,784]
    nn.Linear(28 * 28, 128),
    nn.ReLU(),
    nn.Linear(128, 10),      # 输出 10 类 logits（原始分数，不是概率）
)

# 5) 设备与损失/优化器
device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
model = model.to(device)
loss_fn = nn.CrossEntropyLoss()   # 分类任务常用损失
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

# 6) 训练一个 epoch
model.train()  # 训练模式
for xb, yb in train_loader:  # 解包语法：每轮拿一批输入和标签
    xb = xb.to(device)
    yb = yb.to(device)

    logits = model(xb)           # 前向输出 logits
    loss = loss_fn(logits, yb)   # 计算分类损失

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

# 7) 评估准确率
model.eval()  # 评估模式
correct, total = 0, 0
with torch.no_grad():
    for xb, yb in test_loader:
        xb = xb.to(device)
        yb = yb.to(device)

        logits = model(xb)

        # argmax(dim=1)：按“类别维”取最大分数下标 = 预测类别
        pred_label = logits.argmax(dim=1)

        # (pred_label == yb)：逐元素比较对错
        # .sum().item()：统计当前批次答对数量
        correct += (pred_label == yb).sum().item()
        total += yb.size(0)

acc = 100.0 * correct / total  # 测试准确率百分比
print("test acc:", acc)
```

---

## 13.6 你写代码时怎么看注释（实战建议）

1. 先看“目的”注释，知道这段要解决什么。  
2. 再看“语法”注释，确认每行是不是你会写。  
3. 最后看“.xxx 功能”注释，建立方法语义记忆。  
4. 手写时先抄结构，再去掉注释闭卷重写一遍。
