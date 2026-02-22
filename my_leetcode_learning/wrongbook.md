# LeetCode 错题本

## 模板（复制使用）
### 题号 + 题名：
- 首次日期：
- 是否独立做出（是/否）：
- 我卡住的位置：
- 正解核心：
- 复杂度：
- 易错语法：
- 报错原文：
- 修复动作：
- 一句话记忆：

---

## 1、两数之和

### 0. LC 1 - Two Sum：Hash 思路（总览）
题意：
1. 给定数组 `nums` 和目标值 `target`
2. 找到两个数之和等于 `target`
3. 返回它们的下标（不是返回数值）

核心直觉：
1. 当你看到当前数 `x` 时，真正想知道的是“补数 `need = target - x` 之前出现过没有”。
2. 所以应该把“之前见过的数”存起来，并且能快速查找。
3. 哈希表（字典）正好适合做：`数值 -> 下标`

思路推导：
1. 准备字典 `mp = {}`，表示 `值 -> 下标`
2. 遍历数组，拿到 `i, x`
3. 计算补数 `need = target - x`
4. 查 `if need in mp`（查的是 key）
5. 如果找到了，直接返回 `[mp[need], i]`
6. 如果没找到，把当前值存入 `mp[x] = i`

为什么“先查再存”：
1. 避免把当前元素和自己配对
2. 逻辑上表示“用当前元素去匹配之前出现过的元素”

参考代码（核心版）：
```python
def two_sum(nums, target):
    mp = {}
    for i, x in enumerate(nums):
        need = target - x
        if need in mp:
            return [mp[need], i]
        mp[x] = i
```

复杂度：
1. 时间复杂度：`O(n)`（字典查找/插入平均 `O(1)`）
2. 空间复杂度：`O(n)`

### A. 时间复杂度速记（刷题必看）

### 1. 定义
时间复杂度描述的是：输入规模 `n` 增大时，算法执行步数如何增长。  
关注增长趋势，不看具体毫秒数。

### 2. 常见级别
- `O(1)`：常数时间
- `O(log n)`：对数时间（每次规模减半）
- `O(n)`：线性时间（单次遍历）
- `O(n log n)`：常见排序级别
- `O(n^2)`：双重循环
- `O(2^n)`：指数增长（通常很慢）

### 3. 计算规则（入门版）
1. 顺序代码：复杂度相加后取最大项。
2. 嵌套循环：复杂度相乘。
3. 忽略常数和低阶项。
   - `3n + 5 -> O(n)`
   - `n^2 + n -> O(n^2)`

### 4. Two Sum 例子
1. 暴力双循环：`O(n^2)`  
   外层 `n` 次，内层近似 `n` 次，总量约 `n*n`。
2. 哈希表一遍扫：`O(n)`  
   遍历 `n` 次，每次字典查找/插入平均 `O(1)`。

### 4.1 Two Sum 暴力法循环边界优化（本次关键收获）
错误直觉：
1. 用两层全范围循环 + `i != j` 判定。
2. 这样会重复比较 `(i, j)` 和 `(j, i)`，还要多写一层判断。

更优写法：
```python
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            return [i, j]
```

为什么更好：
1. `j` 从 `i+1` 开始，天然保证 `i != j`。
2. 每对下标只比较一次，不会重复。
3. 代码更简洁，逻辑更清晰。

### 5. 刷题时必须写
每道题至少写清：
1. 时间复杂度
2. 空间复杂度
3. 你为什么能从慢解法优化到快解法

### B. 类型注解 / 类 / `__init__` / `self` 速记

### 1. 类型注解（Type Hints）
例子：
```python
def twoSum(self, nums: List[int], target: int) -> List[int]:
```
含义：
1. `nums: List[int]`：`nums` 期望是“整数列表”
2. `target: int`：`target` 期望是整数
3. `-> List[int]`：返回值期望是“整数列表”

注意：
1. 类型注解主要是可读性和 IDE 提示
2. Python 默认不会因为注解自动做强类型检查
3. 使用 `List` 通常需要：
```python
from typing import List
```

### 2. 类（class）是什么
`class` 是模板，实例（对象）是模板创建出来的具体实体。  
LeetCode 用 `class Solution:` 是平台约定写法。

### 3. `__init__` 是什么
`__init__` 是初始化方法。  
当你创建对象时会自动调用，用来给对象初始赋值。

### 4. `self` 是什么
`self` 代表“当前这个对象本身”。  
它让你在方法里访问/修改当前对象自己的属性。

例子：
```python
class Student:
    def __init__(self, name):
        self.name = name
```
`self.name = name` 的意思是：把传入的 `name` 存到“这个对象自己的 `name` 属性”里。

### C. 易错语法提醒（本题）
1. 判断相等必须用 `==`，不能用 `=`。
2. `=` 是赋值，`==` 才是布尔比较。

### D. 哈希表（Two Sum 核心）

### 1. 是什么
哈希表在 Python 里就是 `dict`。  
核心作用：用 `key` 快速查找 `value`，平均时间复杂度 `O(1)`。

### 2. 为什么 Two Sum 要用哈希表
暴力法要双重循环，时间 `O(n^2)`。  
哈希表法可以边遍历边查找“补数”（`need = target - x`），时间降为 `O(n)`。

### 3. Two Sum 哈希法模板
```python
def twoSum(nums, target):
    mp = {}  # 值 -> 下标
    for i, x in enumerate(nums):
        need = target - x
        if need in mp:
            return [mp[need], i]
        mp[x] = i
```

### 4. 一句话记忆
哈希表 = 用空间换时间，把“查找某值”从 `O(n)` 降到平均 `O(1)`。

### 5. Two Sum 字典方向（易错点）
在本题常用写法里：
```python
mp[x] = i
```
表示：
1. `key` 是数值 `x`
2. `value` 是下标 `i`

因此：
1. `mp[need]` 取到的是“need 对应的下标”
2. `mp[i]` 不代表“按下标取值”，除非 `i` 正好是某个 key
3. 字典默认是 `key -> value` 单向查询，不能自动 `value -> key`

### E. `enumerate` 速记（刷题高频）

### 1. 是什么
`enumerate` 可以在遍历序列时，同时拿到“下标”和“元素值”。

### 2. 基本写法
```python
for i, x in enumerate(nums):
    ...
```
其中：
1. `i` 是下标
2. `x` 是当前元素值

### 3. 和 `range(len(nums))` 的关系
下面两段逻辑等价：
```python
for i, x in enumerate(nums):
    ...
```
```python
for i in range(len(nums)):
    x = nums[i]
    ...
```
`enumerate` 写法更简洁、更不容易写错。

### 4. `start` 参数
```python
for idx, x in enumerate(nums, start=1):
    ...
```
下标会从 1 开始（默认从 0）。

### F. 首次提交代码复盘（完整）

### 1. 当时提交（错误版）
```python
for i, x in enumerate(nums):
    need = target - x
        if need in nums:
            return [nums[need], i]
```

### 2. 三个核心错误
1. 缩进错误：`if` 比 `need = ...` 多缩进一层，Python 会报缩进异常。
2. 容器用错：`if need in nums` 在列表里查值，和后续字典取值逻辑不一致。
3. 取值语义错：`nums[need]` 把 `need` 当下标，实际 `need` 是数值，不是下标。

### 3. 缩进规则（必须记牢）
1. `if / for / while / def / class / try` 后面必须缩进代码块。
2. 同一层逻辑缩进量必须一致（建议固定 4 空格）。
3. 子代码块比父代码块多一层缩进。

### 4. `mp = {}` / `[]` / `set()` 的含义
1. `{}`：空字典（哈希表）。
2. `[]`：空列表。
3. `set()`：空集合（注意：`{}` 不是空集合）。

### 5. 为什么 `mp[x] = i` 要放在最后
正确顺序是“先查补数，再存当前值”：
```python
for i, x in enumerate(nums):
    need = target - x
    if need in mp:
        return [mp[need], i]
    mp[x] = i
```
原因：避免把当前元素和自己配对，保证用到的是“之前见过的元素”。

### 6. 流程示例（`nums=[2,7,11,15], target=9`）
按“先查补数，再存当前值”走：
1. `i=0, x=2`，`need=7`，`7` 不在 `mp`，存入 `mp[2]=0`
2. `i=1, x=7`，`need=2`，`2` 在 `mp`，返回 `[mp[2], 1] = [0,1]`
3. 立即结束，答案正确

备注：
1. 这个例子里“先存后查”也可能凑巧得到正确结果。
2. 但标准写法仍建议“先查后存”，逻辑更稳、能规避同元素配对风险。

### 7. 为什么 key 用数值、value 用下标
在 Two Sum 里我们查的是“补数是否出现过”，所以数值要作为 key：
1. `mp[x] = i`：数值 `x` -> 下标 `i`
2. `if need in mp`：按补数快速查
3. `mp[need]`：直接拿补数对应下标

补充：
1. `mp[need]` 能拿到下标。
2. `mp[i]` 不一定有意义，除非 `i` 本身是一个 key。
3. 字典默认只支持 `key -> value`，不能自动 `value -> key`。
4. `if need in mp` 默认查的是“字典 key”，不是 value。
5. `if need in nums` 是在列表里查“元素值是否存在”，不是查下标映射。

### 8. 为什么 Two Sum 不直接用 `nums` 做 `in`
1. `nums` 是列表，`if need in nums` 只能判断“有没有这个值”，平均要线性扫描 `O(n)`。
2. 列表查到值后还需要再找下标，逻辑更绕、复杂度更高。
3. `mp`（字典）能同时做到：
   - `if need in mp`：平均 `O(1)` 查补数
   - `mp[need]`：直接拿到补数对应下标
4. 所以 Two Sum 标准解用哈希表，而不是直接用列表做成员判断。

---

## 2、存在重复元素（217）

### 0. LC 217 - Contains Duplicate：Set 思路（总览）
题意：
1. 判断数组里是否存在重复元素
2. 只需要返回 `True/False`
3. 不需要下标，也不需要顺序

核心直觉：
1. 每看到一个数，只要判断“它是否已经出现过”
2. 这本质是“成员查询”问题，不是排序问题
3. `set` 最适合做“去重 + 快速查询”

思路推导：
1. 建一个空集合 `seen = set()`
2. 遍历数组中的每个值 `x`
3. 如果 `x in seen`，说明重复，立刻返回 `True`
4. 否则把 `x` 加入集合：`seen.add(x)`
5. 全部遍历完还没命中，返回 `False`

为什么 `set` 比 `list` 更好：
1. `x in list` 平均/最坏都要扫一遍（`O(n)`）
2. `x in set` 平均 `O(1)`
3. 所以整体从可能 `O(n^2)` 降到 `O(n)`

参考代码（核心版）：
```python
def contains_duplicate(nums):
    seen = set()
    for x in nums:
        if x in seen:
            return True
        seen.add(x)
    return False
```

复杂度：
1. 时间复杂度：`O(n)`
2. 空间复杂度：`O(n)`

### A. 题目核心
给定数组 `nums`，只判断“是否有重复值”：
1. 有重复 -> `True`
2. 全不重复 -> `False`

这题不需要返回下标，也不需要保序。

### B. 集合（set）是什么
集合是“不重复、无顺序”的容器，最适合做：
1. 判重
2. 快速成员查询

常用语法：
```python
seen = set()     # 空集合（注意不是 {}）
seen.add(3)      # 加元素
3 in seen        # 查是否存在
```

### C. set 和 list 的区别（高频）
1. 重复性：
   - `list` 允许重复
   - `set` 自动去重
2. 顺序性：
   - `list` 有顺序，可按下标访问
   - `set` 无固定顺序，不能按下标访问
3. 查询复杂度（平均）：
   - `x in list` -> `O(n)`
   - `x in set` -> `O(1)`

### D. 为什么 217 推荐 set 而不是 list
1. 217 只关心“出现过没”，不关心位置。
2. 用 `set` 查重更快，整体 `O(n)`。
3. 如果用 `list` 做 `in`，每次都要线性查找，最坏 `O(n^2)`。

### E. 217 标准模板
```python
def containsDuplicate(nums):
    seen = set()
    for x in nums:
        if x in seen:
            return True
        seen.add(x)
    return False
```

### F. 易错点
1. 空集合是 `set()`，不是 `{}`（`{}` 是空字典）。
2. `set` 不能按下标取值（如 `seen[0]` 会报错）。
3. 这题用 `dict` 也能做，但 `set` 更简洁。
4. `for x in nums` 遍历的是列表元素值，不存在 key/value 概念。
5. `for i, x in enumerate(nums)` 是“下标 + 元素值”二元组解包，也不是 key/value。
6. key/value 只属于字典：
   - `for k in d` 默认遍历 key
   - `for k, v in d.items()` 同时拿 key 和 value
7. `enumerate` 不是“只能用于元组”；它用于可迭代对象（如 list/tuple/string），每轮返回 `(下标, 值)` 元组。

---

## 3、两数之和 II（167）

### 0. LC 167 - Two Sum II：双指针思路（总览）
题意：
1. 数组 `numbers` 已按非递减顺序排列（有序）
2. 找到和为 `target` 的两个数
3. 返回 1-based 下标 `[index1, index2]`

核心直觉：
1. 因为数组有序，所以“和太小/和太大”时，可以确定该移动哪一边
2. 左边增大能让总和变大，右边减小能让总和变小
3. 不需要像 Two Sum(1) 那样用哈希表

思路推导（对撞双指针）：
1. `l = 0`, `r = len(numbers)-1`
2. 当 `l < r` 时循环
3. 计算 `s = numbers[l] + numbers[r]`
4. 若 `s == target`：返回 `[l+1, r+1]`
5. 若 `s < target`：`l += 1`（让和变大）
6. 若 `s > target`：`r -= 1`（让和变小）

为什么不会漏解（关键）：
1. 数组有序，移动方向具有单调性
2. `s < target` 时继续减 `r` 只会更小，所以必须增 `l`
3. `s > target` 时继续增 `l` 只会更大，所以必须减 `r`

参考代码（核心版）：
```python
def two_sum_ii(numbers, target):
    l, r = 0, len(numbers) - 1
    while l < r:
        s = numbers[l] + numbers[r]
        if s == target:
            return [l + 1, r + 1]
        if s < target:
            l += 1
        else:
            r -= 1
```

复杂度：
1. 时间复杂度：`O(n)`
2. 空间复杂度：`O(1)`

### A. 术语：非递减顺序
定义：后一个元素 `>=` 前一个元素，允许相等，不允许变小。

例子：
1. 非递减：`[1, 1, 2, 2, 5]`
2. 非递减：`[-3, -1, 0, 0, 4]`
3. 不是非递减：`[1, 3, 2]`（`3 -> 2` 变小）

### B. 为什么 167 可以用双指针
1. 因为数组已经有序（非递减）。
2. 若当前和太小，左指针右移（增大和）。
3. 若当前和太大，右指针左移（减小和）。
4. 所以整体只需一趟，时间复杂度 `O(n)`。
“》？，
### C. 双指针到底是什么（详细版）
1. 双指针不是新数据结构，本质是两个下标变量。
2. 核心是“有规则地移动两个下标”，而不是“随便移动”。
3. 目标：减少无效比较，把 `O(n^2)` 降到 `O(n)`。

### D. 167 用的是哪一种双指针
1. 167 是“对撞指针”：
   - `l` 从左边开始
   - `r` 从右边开始
2. 循环条件：`while l < r`
3. 每轮计算：`s = numbers[l] + numbers[r]`

### E. 167 的移动规则（必须背下来）
1. `s == target`：找到答案，返回 `[l + 1, r + 1]`  
   注意：题目下标从 `1` 开始。
2. `s < target`：左指针右移 `l += 1`（让和变大）
3. `s > target`：右指针左移 `r -= 1`（让和变小）

### F. 为什么这种移动是正确的（单调性）
1. 数组非递减，意味着右边数字更大或相等，左边数字更小或相等。
2. 当 `s < target` 时，当前左值太小，继续减右值只会更小，因此必须增大左值。
3. 当 `s > target` 时，当前右值太大，继续增左值只会更大，因此必须减小右值。
4. 每次移动都能排除一片不可能区域，所以不会漏解。

### G. 167 模板代码（可直接默写）
```python
def twoSum(numbers, target):
    l, r = 0, len(numbers) - 1
    while l < r:
        s = numbers[l] + numbers[r]
        if s == target:
            return [l + 1, r + 1]
        if s < target:
            l += 1
        else:
            r -= 1
    return []
```

### H. 手动演算例子
`numbers = [2, 7, 11, 15], target = 9`
1. `l=0, r=3`，`s=2+15=17 > 9`，右移 `r=2`
2. `l=0, r=2`，`s=2+11=13 > 9`，右移 `r=1`
3. `l=0, r=1`，`s=2+7=9`，返回 `[1, 2]`

### I. 复杂度与优势
1. 时间复杂度：`O(n)`（每个指针最多走一遍）
2. 空间复杂度：`O(1)`
3. 对比哈希法：
   - 哈希法也可 `O(n)`，但空间 `O(n)`
   - 167 已有“有序”条件，双指针更省空间

### J. 167 常见错误
1. 忘记题目是 1-based 下标，误返回 `[l, r]`
2. 把 `while l < r` 写成 `<=`，边界容易乱
3. 分支里忘记移动指针，造成死循环
4. 在无序数组上套用这套规则（会错）

---

## 4、移动零（283）

### 0. LC 283 - Move Zeroes：双指针思路（总览）
题意：
1. 把所有 `0` 移到数组末尾
2. 非零元素相对顺序保持不变
3. 必须原地修改（in-place）

核心直觉：
1. 你不需要真的“一个个删 0 再补 0”
2. 只需要把非零元素按顺序收集到前面
3. 所以用两个指针：
   - `fast` 找非零
   - `slow` 放非零

思路推导：
1. 初始化 `slow = 0`
2. 用 `fast` 从左到右扫描整个数组
3. 如果 `nums[fast] != 0`：
   - 把它交换到 `slow` 位置（或覆盖写入）
   - `slow += 1`
4. 扫描结束后，前面是按原顺序排好的非零元素，后面自然是零

为什么能保持相对顺序：
1. `fast` 是从左到右扫描
2. 非零元素是按遇到的先后顺序依次写到 `slow`
3. 所以非零元素之间顺序不变

参考代码（核心版）：
```python
def move_zeroes(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
```

复杂度：
1. 时间复杂度：`O(n)`
2. 空间复杂度：`O(1)`

### A. 已通过代码（双指针）
```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow = slow + 1
```

### B. 题目核心思路
1. `fast`：扫描指针，遍历整个数组。
2. `slow`：指向“下一个非零元素应该放的位置”。
3. 当 `nums[fast] != 0` 时，把当前非零换到前面 `slow` 位置，然后 `slow += 1`。
4. 整个过程原地修改，不需要额外数组。

### C. 今天犯过的错误（必须复习）
1. 写成 `for nums[fast] in nums:`  
   - 错因：`for ... in ...` 左边必须是“变量名”，不能是 `nums[fast]` 这种索引表达式。
   - 改法：`for fast in range(len(nums)):`。
2. 写成 `fast += fast`、`slow += slow`  
   - 错因：这是“加上自己”，会翻倍，不是前进一步。
   - 改法：用 `+= 1`。
3. 误以为 Python 可以写 `fast++`  
   - 错因：Python 没有 `++` 运算符。
   - 改法：`fast += 1`。
4. 纠结 `for x in nums` 能否做双指针  
   - 结论：`for x in nums` 取到的是元素值，不是下标，不适合做本题这种“按下标交换”。
   - 改法：优先 `for fast in range(len(nums))`（或 `enumerate` 取下标）。

### D. 今日问答要点（浓缩）
1. 为什么 `+= fast` 会翻倍：`fast += fast` 等价于 `fast = fast + fast`。
2. 为什么不能 `fast++`：Python 语法不支持 `++`。
3. 为什么 `for x in nums` 不是下标循环：`x` 是值，不是 index。
4. 双指针循环怎么写：`slow=0` + `for fast in range(len(nums))` + 非零时交换。

### E. 复杂度
1. 时间复杂度：`O(n)`（每个元素最多处理一次）。
2. 空间复杂度：`O(1)`（原地修改）。

### F. 一句话记忆
“`fast` 负责找非零，`slow` 负责放非零；遇到非零就交换并推进 `slow`。”

---

## 5、移除元素（27）

### 0. LC 27 - Remove Element：双指针思路（总览）
题意：
1. 原地删除数组中所有等于 `val` 的元素
2. 返回删除后的新长度 `k`
3. 只要求前 `k` 个元素正确（尾部内容不重要）

核心直觉：
1. 这题和 283 很像，本质是“原地筛选”
2. 你要保留的是“`!= val` 的元素”
3. 所以同样用双指针：
   - `fast` 扫描所有元素
   - `slow` 写入保留元素

思路推导：
1. 初始化 `slow = 0`
2. 遍历 `fast in range(len(nums))`
3. 若 `nums[fast] != val`：
   - 把它写到 `nums[slow]`（或交换到 `slow`）
   - `slow += 1`
4. 遍历结束后，`slow` 就是新长度
5. （可选）如果本地想把尾部删掉：`del nums[slow:]`

为什么返回 `slow`：
1. `slow` 每增加一次，代表成功保留了一个元素
2. 所以最后 `slow` 正好等于“保留元素总数” = 新长度

参考代码（核心版）：
```python
def remove_element(nums, val):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
    return slow
```

复杂度：
1. 时间复杂度：`O(n)`
2. 空间复杂度：`O(1)`

### A. 题目核心（和 283 是同类题）
1. 原地修改数组 `nums`
2. 删除所有等于 `val` 的元素
3. 返回“新长度” `k`
4. 只需保证前 `k` 个元素正确（LeetCode 不强制真的删尾巴）

### B. 正解核心（双指针）
1. `fast`：扫描整个数组，读每个元素
2. `slow`：指向“下一个保留元素应该写入的位置”
3. 当 `nums[fast] != val` 时：
   - 把 `nums[fast]` 放到 `nums[slow]`
   - `slow += 1`
4. 遍历结束后，`slow` 就是新长度

### C. 你这题问过/踩过的关键点（必须复习）

#### 1. 想在 `for i in range(len(nums))` 里直接 `del nums[i]`
问题：
1. 删除后列表变短，后面的元素左移
2. 原来的下标计划失效，容易跳元素或越界
3. 复杂度也会变差（频繁删除通常是 `O(n)`）

结论：
1. 这类原地筛选题，优先双指针
2. 不要在“按固定下标递增遍历”的同时删除当前元素

#### 2. 返回值写成 `(z, nums)`（元组）是错的
题目要求：
1. 返回值类型是 `int`
2. 返回“新长度”

结论：
1. `return slow`
2. 不要返回整个列表（除非本地调试自己看）

#### 3. `range(1, len(nums))` 的边界理解
你问的点很关键：
1. `range(start, end)` 包含 `start`
2. 不包含 `end`

所以：
1. `range(1, len(nums))` 遍历的是 `1 ... len(nums)-1`
2. 不会遍历到 `len(nums)`

#### 4. `del nums[-3:]` 为什么不对
问题：
1. 这是“固定删最后 3 个”
2. 题目里要删多少个取决于 `val` 出现次数，不是固定值

正确思路：
1. 如果你想把尾部真的删掉，应该按双指针结果删：
   - `del nums[slow:]`
2. 但这一步在 LeetCode 27 里通常是可选的

### D. 你问过的 `list` 删除语法（本题相关）
常用 4 种：
1. `nums.remove(x)`：按值删除第一个匹配项（不存在会报错）
2. `nums.pop(i)`：按下标删除并返回元素
3. `del nums[i]`：按下标删除（不返回）
4. `del nums[a:b]`：切片删除一段（例如 `del nums[slow:]`）

补充：
1. 27 题虽然能用 `del`，但频繁删除不如双指针高效
2. `del nums[slow:]` 是“收尾整理”，不是核心算法步骤

### E. 你最终通过的写法（可复习版）
```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow = slow + 1

        del nums[slow:]
        return slow
```

### F. 进一步优化写法（更直观，常见于题解）
说明：这题不一定需要交换，覆盖写入即可。

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        return slow
```

### G. 一句话记忆
“27 和 283 本质一样：`fast` 负责扫描，`slow` 负责写入保留元素的位置。”

---

## 6、存在重复元素 II（219）

### A. 题目核心（217 的升级版）
题意：
1. 找“是否有重复值”
2. 还要满足重复值的下标距离 `<= k`

所以这题本质是：
1. `217` 的“判重”
2. 再加一个“距离约束”

---

### B. 你的第一版思路（暴力法）是正常的
你先想到的是：
1. 固定 `i`
2. 检查后面最多 `k` 个位置里有没有和 `nums[i]` 相同的值

这个思路非常常见，而且是健康路线：
1. 先保证正确性（暴力法）
2. 再优化复杂度（哈希法）

结论：
1. 不是“只有菜鸟才先想暴力”
2. 很多人也是先暴力，再升级模板

---

### C. 你写过的暴力法（正确版）
```python
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            j = min(i + k, len(nums) - 1)
            for m in range(i + 1, j + 1):
                if nums[m] == nums[i]:
                    return True
        return False
```

复杂度：
1. 时间复杂度：最坏 `O(n * k)`（当 `k` 接近 `n` 时接近 `O(n^2)`）
2. 空间复杂度：`O(1)`

---

### D. 你在暴力法里犯过的错误（必须复习）

#### 1. 越界错误（最关键）
错误思路：
```python
j = i + k
for m in range(i + 1, j + 1):
    if nums[m] == nums[i]:
        ...
```

问题：
1. 当 `i + k >= len(nums)` 时，`m` 会走到数组外
2. `nums[m]` 触发 `IndexError`

修复：
```python
j = min(i + k, len(nums) - 1)
```

#### 2. `n` 没定义（NameError）
你写过：
```python
j = min(i + k, n - 1)
```
但前面没有：
```python
n = len(nums)
```

修复方式二选一：
1. 提前定义 `n = len(nums)`
2. 直接写 `len(nums) - 1`

---

### E. Claude 给的哈希思路（整理版，值得背）

#### 核心直觉：每个值只需要记“最近一次出现位置”
如果同一个值 `x` 出现在 `i1 < i2 < i3`：
1. `i3 - i2` 一定比 `i3 - i1` 更小（更近）
2. 所以判断当前下标时，保留“最近一次下标”最有用

这就是哈希表的映射：
1. `value -> last_index`

#### 思路推导
遍历 `nums`，对每个 `i, x`：
1. 看 `x` 之前是否出现过（`x in last_seen`）
2. 如果出现过，检查距离：`i - last_seen[x] <= k`
3. 无论是否命中，都更新：`last_seen[x] = i`（覆盖旧下标）

参考代码（Claude思路）：
```python
def containsNearbyDuplicate(nums, k):
    last_seen = {}  # value -> last index
    for i, num in enumerate(nums):
        if num in last_seen and i - last_seen[num] <= k:
            return True
        last_seen[num] = i  # 只保留最新下标
    return False
```

#### 为什么覆盖旧下标是安全的（必须理解）
假设 `nums[i] == nums[j] == nums[m]`，且 `i < j < m`：
1. `m - j < m - i`，说明 `j` 比 `i` 更“有用”（离当前更近）
2. 所以用更近的 `j` 覆盖更旧的 `i` 不会漏答案

---

### F. 你写哈希版时犯过的错误（关键）
你写过（接近正确版）：
```python
mp = {}
for i, x in enumerate(nums):
    if x in mp:
        if i - mp[x] <= k:
            return True
        mp[x] = i
return False
```

问题：
1. `x` 第一次出现时（`x not in mp`），你没有执行 `mp[x] = i`
2. 导致很多值永远不会被记录进字典
3. 后续重复出现时也查不到

正确关键点：
1. `mp[x] = i` 必须每轮都执行（放在 `if` 外面）

正确写法（标准版）：
```python
mp = {}
for i, x in enumerate(nums):
    if x in mp and i - mp[x] <= k:
        return True
    mp[x] = i
return False
```

---

### G. 你问过的关键问题（219相关复习）

#### 1. “这种先暴力再优化的思路常见吗？”
结论：非常常见。
1. 大多数人也是先暴力保证正确
2. 做多了同类题才会更快想到哈希模板

#### 2. `if x in mp:` 在查什么？
结论：查字典的 key。
1. `x in mp` -> 查 key
2. `x in mp.values()` -> 查 value
3. `x in mp.items()` -> 查 `(key, value)` 元组

这也是为什么 219 哈希解法里用：
1. `x in mp`（判断这个值是否出现过）
2. `mp[x]`（取上一次下标）

---

### H. 复杂度总结（要说准确）

#### 哈希版（不主动删旧键）
1. 时间复杂度：`O(n)`
2. 空间复杂度：最坏 `O(n)`

#### 哈希版（如果做滑动窗口并主动删旧元素，另一种写法）
1. 时间复杂度：`O(n)`
2. 空间复杂度：`O(min(n, k))`

说明：
1. 你当前这版“last_seen 字典覆盖最近下标”的写法通常不主动删键
2. 所以空间复杂度说 `O(n)` 更稳妥

---

### I. 一句话记忆
“219 = 217（判重）+ 最近下标；哈希表存 `值 -> 最近出现位置`，每轮先判距离再更新。”
