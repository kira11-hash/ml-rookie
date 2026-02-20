# Python 语法讲义（超详细版，纯讲义）

> 适用对象：零基础（会一点 Matlab/Mathematica 也算零基础起步）  
> 讲义目标：让你在 Day1/Day2 不靠死记硬背，真正理解并能手写通过

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

排序写法：
```python
sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
```

解释：
1. `x` 是一个元组 `(word, count)`。
2. `x[1]` 是次数，`-x[1]` 表示次数高的排前面。
3. `x[0]` 是单词，次数相同就按字母序。

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
                f.write(c + "\\n")

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
