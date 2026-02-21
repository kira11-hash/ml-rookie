# ML验证期学习日志

## 总规则
- 优先级：`IC > ML`
- 当前主线：`搜广推（Search/Recommendation/Ads）`
- 并行补充：`LLM相关能力（以推荐结合为主）`
- 2026.02-2026.07 每周ML目标投入：`5-10小时`
- 预备周验收标准（2026-02-17 到 2026-02-21）：
  - 完成 5 个 `.py` 文件
  - 总学习时长 >= 8 小时
  - 独立解决 >= 2 个报错
  - Python自评 >= 4/10

---

## 2026-02-17（预备周 Day 1）

### 今日计划
- [x] 完成 `everyday_learning/day1/day1_handwrite.py`
- [x] 理解变量 / if判断 / print输出
- [x] 完成 `grade_level` 和 `BMI` 两段逻辑
- [x] 至少运行脚本 3 次

### 时间记录
- 开始时间：2026-02-17 23:00
- 结束时间：2026-02-18 00:00
- 专注时长（分钟）：60

### 今日完成
- [x] Day1 手写脚本跑通（断言通过）
- [x] 理解 `if / elif / else` 的执行顺序
- [x] 理解缩进决定代码块层级
- [x] 理解 BMI 公式中括号和 `**` 的作用

### 今日报错与修复
- 报错1：`NameError`（变量名拼写不一致）
  - 原因：变量名前后不统一
  - 修复：统一变量名并重跑
- 报错2：`AssertionError`（成绩分段逻辑错误）
  - 原因：分段阈值误写（如 `>=700`）
  - 修复：改成正确分段并重跑通过

### 自检
- 我能解释 `if / elif / else`：是
- 我能独立写一个简单函数：是
- Python自评（1-10）：8

---

## 2026-02-18（预备周 Day 2）

### 今日计划
- [x] 完成 `everyday_learning/day2/day2_handwrite.py`
- [x] 理解 `list / dict / for / enumerate` 基础语法
- [x] 完成 `top10_word_frequency(text)` 函数（清洗 + 统计 + 排序）
- [x] 运行脚本并通过全部断言
- [x] 独立修复至少 1 个真实报错

### 时间记录
- 开始时间：2026-02-18 19:50
- 结束时间：2026-02-18 21:50
- 专注时长（分钟）：120

### 今日完成
- [x] 列表练习：`append` / `sort` / `pop` 理解
- [x] 词频函数跑通：`lower -> 清洗 -> join -> split -> dict统计 -> sorted`
- [x] 断言通过，终端输出 `Day2 手写练习通过。`
- [x] 完成关键概念问答（`lambda`、`key`、`enumerate`、`join/split` 等）

### 易错语法提醒（Day2）
- [x] `for` / `if` / `elif` 行末必须有冒号 `:`
- [x] 缩进统一 4 空格，同一层级缩进必须一致
- [x] 用 `elif`，不要写 `else if`
- [x] `else` 后面不能加条件
- [x] `freq[word]` 里的 `word` 是变量，不要写成 `"word"`
- [x] `freq[word] = freq.get(word, 0) + 1`，避免 `KeyError`
- [x] `sort()` 是原地修改；`sorted()` 返回新列表
- [x] `enumerate(words, start=1)` 的 `start=1` 是排名从 1 开始

### 今日报错与修复
- 报错1：`SyntaxError`（把 `freq[w]` 写成 `freq(w)`）
  - 报错信息（原文）：invalid syntax
  - 原因定位：字典索引应使用 `[]`，`()` 是函数调用
  - 修复动作：改为 `freq[w] = freq.get(w, 0) + 1`
  - 修复后结果：词频统计可正常执行
- 报错2：`AttributeError: 'list' object has no attribute 'split'`
  - 原因定位：对列表调用了字符串方法 `split()`
  - 修复动作：先 `clean_text = "".join(clean_chars)` 再 `split()`
  - 修复后结果：`words` 正常生成

### 关键代码/结果记录
- 总词数（`total_words`）：32
- 去重词数（`unique_words`）：25
- Top10 前3项：
  1. `('is', 4)`
  2. `('learning', 3)`
  3. `('machine', 2)`
- 终端最终输出是否包含：`Day2 手写练习通过。`：是

### 自检（Day2）
- 我能解释 `freq.get(word, 0) + 1` 的含义：是
- 我能解释 `enumerate(words, start=1)` 的作用：是
- 我能解释 `sorted(..., key=lambda x: (-x[1], x[0]))`：是
- 我能独立口述词频任务 5 步流程：是
- Python自评（1-10）：6

---

## 易错语法错题本（持续更新）

### Day1 典型坑
- `=` 是赋值，`==` 才是比较
- Python 用缩进表示代码块层级
- `return tier` 不能写成 `return "tier"`
- BMI 公式必须写成 `weight / (height ** 2)`

### Day2 典型坑
- 字典取值/赋值用 `[]`，不是 `()`
- `split()` 只能用于字符串，不能用于列表
- `sort()` 修改原列表并返回 `None`
- `sorted(..., key=...)` 里的 `key` 是排序规则，不是字典的 key
- `word`（变量）和 `"word"`（固定字符串）含义完全不同
- `enumerate(..., start=1)` 让排名从 1 开始

### Day3 典型坑
- `.strip` 是方法对象，`.strip()` 才会执行
- `re.sub(r"\s+", "", text)` 会删光空白，不是归一化；应替换成 `" "` 再 `strip()`
- 去非字母字符时建议替换成空格 `" "`，避免单词粘连
- 先 `join` 形成字符串，再 `split` 切词
- `r"..."` 是原始字符串，写正则时建议固定使用

---

## 2026-02-19（预备周 Day 3）

### 今日计划
- [x] 完成 `everyday_learning/day3/day3_handwrite.py`
- [x] 理解函数拆分：`normalize_spaces` + `clean_text`
- [x] 理解字符串处理：`lower / split / join / strip`
- [x] 理解正则清洗：`re.sub`（去 URL、去非字母）
- [x] 运行脚本并通过全部断言
- [x] 独立修复至少 1 个真实报错

### 时间记录
- 开始时间：2026-02-19 11:00
- 结束时间：2026-02-19 11:52
- 专注时长（分钟）：52

### 今日完成
- [x] Day3 手写脚本跑通（终端输出 `Day3 手写练习通过。`）
- [x] 掌握 `import re`、`re.sub`、`r"..."` 的基本语义
- [x] 掌握空白归一化：`" ".join(text.split())` / `re.sub(...).strip()`
- [x] 完成正则清洗流程：小写 -> 去 URL -> 去非字母 -> 归一化空白

### 今日报错与修复
- 报错1：`AssertionError: 空白归一化失败`
  - 原因定位：`normalize_spaces` 中把空白替换成了空字符串 `""`，导致单词被粘连
  - 修复动作：改为 `re.sub(r"\s+", " ", text).strip()`
  - 修复后结果：`normalize_spaces("a   b\tc\n d") == "a b c d"` 通过
- 报错2：方法对象误用
  - 报错信息（现象）：写成 `.strip`（无括号）导致未执行
  - 原因定位：`.strip` 是方法对象，`.strip()` 才是调用
  - 修复动作：补上 `()`
  - 修复后结果：空白清洗逻辑恢复正常

### 关键代码/结果记录
- 清洗前样例：`Hello!!!  ML is FUN. Visit https://example.com now, 100% sure.`
- 清洗后结果：`hello ml is fun visit now sure`
- `normalize_spaces("a   b\\tc\\n d")` 结果：`a b c d`
- 终端最终输出是否包含：`Day3 手写练习通过。`：是

### 今日提问与答案（Day3，一一对应）
1. 问：`import re` 是什么？是否类似 C 的 `include`？  
答：`import re` 是导入 Python 标准库正则模块；作用上接近“引入库”，但机制不是 C 的预处理展开。

2. 问：正则为什么能做文本匹配/替换？是否需要联网？  
答：正则是“模式匹配语言”；`re` 在本地执行匹配和替换，不需要联网。

3. 问：`r"https?://\\S+|www\\.\\S+"` 逐段什么意思？  
答：匹配两类 URL。前半段是 `http/https://...`，后半段是 `www....`，`|` 表示“或”。

4. 问：`+`（量词）是什么意思？  
答：前一个模式出现 1 次或多次，例如 `\\S+` 表示一个或多个连续非空白字符。

5. 问：`r"..."` 和不加 `r` 有什么区别？  
答：`r"..."` 是原始字符串，反斜杠按字面处理；不加 `r` 时通常要多写转义，容易错。

6. 问：`r"[^a-z\\s]"` 为什么要 `[]`，`^` 是什么作用？  
答：`[]` 是字符集合；`^` 在集合开头表示取反，所以这句匹配“不是小写字母或空白”的字符。

7. 问：两次 `re.sub` 各做什么？  
答：第一步去 URL，第二步去非字母字符；分步写更容易理解和排错。

8. 问：两步清洗能不能合成一步？  
答：可以，但可读性和可调试性会下降，当前阶段不建议。

9. 问：`.strip()` 的作用是什么？  
答：去掉字符串首尾空白，不会改动中间空白。

10. 问：什么叫“归一化空白”？  
答：把多个空格/Tab/换行统一成单个空格，并去掉首尾空白，让文本格式稳定。

11. 问：`re.sub` 返回的是什么？  
答：返回一个新字符串，不是字符列表。

12. 问：为什么还要 `" ".join(text.split())`？  
答：用于统一各种空白并消除多空格，是最稳妥的空白规范化方式之一。

13. 问：`re.sub(...).strip()` 和 `" ".join(text.split())` 是什么关系？  
答：都能做空白规整；前者更可控，后者更简洁。

14. 问：`""` 和 `" "` 在替换里差异是什么？  
答：替换成 `""` 会把单词粘在一起；替换成 `" "` 会保留词边界。

15. 问：`.strip` 和 `.strip()` 差异是什么？  
答：`.strip` 是方法对象；`.strip()` 才是实际执行调用。

16. 问：Git/GitHub 什么时候开始？  
答：Day5 先做本地 Git 最小闭环（`init/add/commit/log`），GitHub 放到有完整小项目后再上。

17. 问：LeetCode 当前怎么安排？  
答：先 Hot100，语言选 Python3；现在按 Day 任务推进，不抢跑。

18. 问：MiniGPT / CS336 是否在计划里？  
答：在后续冲刺期里，当前 Day3 不作为主任务。

19. 问：牛客现在要不要用？  
答：暂时不用，后期投递与面试阶段再用。

20. 问：当前学习路线优先级是什么？  
答：先完成 Day3 handwrite 与断言，再进入 Day4/Day5，保证学习链条连续。

### 自检（Day3）
- 我能口述 `clean_text` 的 4 步流程：是
- 我能解释去 URL 的正则语句含义：是
- 我能解释去非字母字符的正则语句含义：是
- 我能解释为什么要做空白归一化：是
- Python自评（1-10）：7

### 明日任务（2026-02-20 Day 4）
- 文件IO / 异常处理（try-except）
- 完成 `everyday_learning/day4/day4_handwrite.py`（已创建，待完成）

---

## 2026-02-20（预备周 Day 4）

### 今日计划
- [x] 完成 `everyday_learning/day4/day4_handwrite.py` 第一版
- [x] 理解 `with open(..., mode, encoding="utf-8")` 的标准写法
- [x] 理解 `try-except`：专门异常 + 兜底异常
- [ ] 实现 `clean_file(input_path, output_path)` 并通过全部断言
- [x] 独立定位并修复至少 1 个真实报错

### 时间记录
- 开始时间：2026-02-20 15:30
- 结束时间：2026-02-20 16:30
- 专注时长（分钟）：60

### 今日完成
- [x] 完成 Day4 手写文件主流程（`write_demo_file` / `clean_line` / `clean_file`）
- [x] 搞清文件读写三种常用读取方式：`read` / `readline` / `readlines`
- [x] 搞清 `f.write(c + "\n")`、`"w"` 与 `"a"` 的区别
- [x] 完成 Git/GitHub 连通并成功 `push` 到远程
- [x] 搞清 `Exception as e`、`__file__`、`Path(...).resolve().parent`、`pass`

### 易错语法提醒（Day4）
- [x] 写文件用 `"w"` 会覆盖原文件，追加要用 `"a"`
- [x] `write()` 不会自动换行，需要手动加 `\n`
- [x] `\s` 与 `\S` 含义相反：前者空白，后者非空白
- [x] `"\n"` 和 `"\\n"` 含义不同（真换行 vs 字面字符）
- [x] `except Exception as e` 中 `e` 是“异常对象变量名”，可自定义
- [x] `with open(...) as f` 会自动关闭文件
- [x] `clean_file` 里不要写死文件名，要用 `input_path/output_path`

### 今日报错与修复
- 报错1：
  - 报错信息（原文）：`AssertionError: clean_line 规则有误`
  - 原因定位：`clean_line` 用了 `re.sub(r"\S+", " ", line)`，把非空白字符都替换掉了；且未正确压缩空白。
  - 修复动作：改思路为压缩空白（`" ".join(line.split())`）或用 `re.sub(r"\s+", " ", line)`。
  - 修复后结果：定位完成，准备按最终版本改到断言通过。
- 报错2：
  - 报错信息（原文）：`with open(..., "w","encoding = utf-8")` 参数写法错误
  - 原因定位：`encoding` 被写成了字符串位置参数，而不是关键字参数。
  - 修复动作：改为 `with open(..., "w", encoding="utf-8")`
  - 修复后结果：语法问题已修复。
- 报错3：
  - 报错信息（现象）：输出文件内容异常（`' \n'`）
  - 原因定位：`write_demo_file` 内容不符合题目要求且 `clean_line` 逻辑错误导致有效字符被清空。
  - 修复动作：将 demo 文本改为题目指定内容，并按正确清洗规则处理。
  - 修复后结果：问题已定位，下一步完成最终修复并重跑断言。

### 关键代码/结果记录
- 输入文件路径：`/Users/chenqingan/Library/Mobile Documents/com~apple~CloudDocs/ml-rookie/everyday_learning/day4/day4_input_demo.txt`
- 输出文件路径：`/Users/chenqingan/Library/Mobile Documents/com~apple~CloudDocs/ml-rookie/everyday_learning/day4/day4_output_demo.txt`
- 一次运行时 `clean_file` 返回值：`True`
- 一次运行时输出文件内容（repr）：`' \n'`
- 不存在文件测试返回值（应为 False）：`False`
- 终端最终输出是否包含：`Day4 手写练习通过。`：否（当前仍在修复阶段）

### 今日提问与答案（Day4，一一对应）
1. 问：`-m` 是什么意思，`pip` 是什么？  
答：`-m` 是让 Python 运行某个模块；`pip` 是 Python 包管理工具。

2. 问：`mps` 和“解释器”是什么意思？  
答：`mps` 是苹果芯片上的计算加速后端；解释器是执行 Python 源码的程序（如 `/usr/bin/python3`）。

3. 问：`torch` 是谁做的，是否有替代并更快？  
答：PyTorch 由 Meta/社区主导；有很多替代框架，特定场景可更快，但通用生态上 PyTorch 很强。

4. 问：`python3 -m pip install torch` 原理是什么，怎么知道去哪下载？  
答：`pip` 默认从 PyPI 索引解析并下载与你系统匹配的 wheel 包并安装。

5. 问：`readline()` 和 `readlines()` 区别是什么？  
答：`readline()` 读一行字符串；`readlines()` 读所有行并返回列表。

6. 问：`with open(...): data=f.read()` 读完后数据长什么样？  
答：`data` 是一个完整字符串（含 `\n`）。

7. 问：`print(readlines结果)` 会怎样？  
答：会打印列表字面量形式，如 `['a\\n', 'b\\n']`。

8. 问：`readlines` 和 `read` 有啥区别？  
答：前者返回按行列表，后者返回整段字符串。

9. 问：`f.write("hello\\n")` 写到哪里？  
答：取决于模式：`"w"` 覆盖写，`"a"` 末尾追加。

10. 问：`except Exception as e` 里的 `e` 是什么？  
答：`e` 是异常对象变量名，用于拿到具体错误信息，可自定义命名。

11. 问：`def clean_file(input_path, output_path):` 输入和输出分别是什么？  
答：参数 `input_path/output_path` 是输入；函数输出看 `return`（如 True/False）。

12. 问：`for line in lines ... if c: cleaned_lines.append(c)` 是什么意思？  
答：逐行清洗并丢弃空行，只把有效结果加入列表。

13. 问：`f.write(c + "\\n")` 是什么意思？  
答：写入 `c` 再写换行。

14. 问：`+` 是拼接吗？`\\n` 和 `\n` 为什么不同？  
答：`+` 可拼接字符串；`\n` 是换行，`\\n` 是反斜杠+n 的字面字符。

15. 问：如果要写 `cb`，该怎么写？  
答：可写 `f.write("cb\\n")`（固定）或 `f.write(c + b + "\\n")`（变量拼接）。

16. 问：`import os` 和 `from pathlib import Path` 是什么？  
答：导入系统功能库和路径处理类，分别用于系统接口与路径对象化操作。

17. 问：为什么不能默认导入全部模块？  
答：会拖慢启动、增加内存、制造命名冲突并降低可维护性。

18. 问：`BASE_DIR = Path(__file__).resolve().parent` 是什么语法？  
答：用当前脚本路径 `__file__` 计算脚本所在目录，得到稳定基准路径。

19. 问：`pass` 是什么意思？  
答：占位语句，表示先不做任何事但语法完整。

20. 问：学了会忘、频繁查讲义正常吗？  
答：正常；高频查 + 高频用会形成长期记忆。

21. 问：大神是不是也从“没思路”开始？  
答：是；关键在持续练习、复盘与复刷机制。

22. 问：Day4 为什么断言失败，应该改哪里？  
答：核心在 `clean_line`（`\\S+` 用反了）和 demo 输入内容不对，另有路径写死/参数写法问题。

23. 问：`\\s` 和 `\\S` 大小写含义不同吗？  
答：是，二者是反义：`\s` 空白，`\S` 非空白。

24. 问：当前 Day4 还有什么问题？  
答：剩余关键是修正 `write_demo_file` 内容与 `clean_line` 逻辑，使断言全部通过。

### 自检（Day4）
- 我能解释 `with open(...) as f` 为什么更安全：是
- 我能解释 `r / w / a` 三种模式区别：是
- 我能解释 `FileNotFoundError` 与 `Exception as e` 的区别：是
- 我能口述 clean_file 的 6 步流程：是（但实现仍需收口）
- Python自评（1-10）：6

### 明日任务（2026-02-21 Day 5）
- PyTorch 预热（tensor/device/linear）
- LeetCode 2题（两数之和、移动零）
- Git 本地入门（init/add/commit/log）

---

## 2026-02-21（预备周 Day 5）

### 今日计划
- [x] 环境检查通过（PyTorch + MPS 可用性）
- [x] 完成 `everyday_learning/day5/day5_handwrite.py`
- [x] 理解最小训练循环：`forward -> loss -> backward -> step`
- [x] LeetCode：完成 `1. 两数之和`；`283. 移动零` 延后到后续日
- [x] Git 最小闭环：`init/add/commit/log/push`

### 时间记录
- 按本次要求：不记录具体时间

### 环境检查（Day5）
- 命令1：`export PYTORCH_ENABLE_MPS_FALLBACK=1`
- 命令2：`/usr/bin/python3 -c "import torch; print(torch.__version__); print('mps:', torch.backends.mps.is_available())"`
- 可选脚本：`/usr/bin/python3 "/Users/chenqingan/Library/Mobile Documents/com~apple~CloudDocs/ml-rookie/everyday_learning/day5/day5_env_check.py"`
- PyTorch 版本：`2.8.0`
- MPS 可用（True/False）：`True`
- 实际使用设备（`mps/cpu`）：`mps`

### 今日完成
- [x] 完成 Day5 环境搭建与依赖修复（`torch`、`numpy`）
- [x] 跑通 Day5 参考流程并通过断言
- [x] 理解 Tensor / device / Linear / loss / backward / optimizer
- [x] 完成 GitHub SSH 链路与远程 push

### 易错语法提醒（Day5）
- [x] 模型和数据必须在同一个 device（都在 `mps` 或都在 `cpu`）
- [x] 训练三连顺序不能错：`zero_grad -> backward -> step`
- [x] 推理时要用 `with torch.no_grad():`
- [x] `loss.item()` 才是 Python 数值，`loss` 本体是 Tensor
- [x] `nn.Linear` 的 `L` 必须大写（`nn.linear` 会报错）
- [x] `range(epochs)` 的循环次数要先定义好 `epochs`

### 今日报错与修复
- 报错1：
  - 报错信息（原文）：`ModuleNotFoundError: No module named 'torch'`
  - 原因定位：`/usr/bin/python3` 环境里未安装 PyTorch
  - 修复动作：执行 `/usr/bin/python3 -m pip install torch`
  - 修复后结果：可导入 `torch`，MPS 可用
- 报错2：
  - 报错信息（原文）：`UserWarning: Failed to initialize NumPy: No module named 'numpy'`
  - 原因定位：PyTorch 运行时缺少 `numpy`
  - 修复动作：执行 `/usr/bin/python3 -m pip install numpy`
  - 修复后结果：警告消失，环境检查通过
- 报错3：
  - 报错信息（原文）：`AttributeError: module 'torch.nn' has no attribute 'linear'`
  - 原因定位：大小写写错，应为 `nn.Linear`
  - 修复动作：改成 `nn.Linear(1, 1)`
  - 修复后结果：模型创建正常

### 关键结果记录（Day5）
- `day5_handwrite.py` 是否通过：`是`
- 终端最终输出是否包含：`Day5 手写练习通过。`：`是`
- 训练最终 `final_loss`：已达标（`< 0.2`）
- `x=4.0` 的预测值（应接近 9）：已达标（接近 `9`）
- 训练循环是否能口述 5 步：`是`

### ML 相关学习知识（Day5）
1. 训练最小闭环（必须会口述）：
   - `forward -> loss -> zero_grad -> backward -> step`
2. Tensor 三要素：
   - `shape`（形状）、`dtype`（类型）、`device`（设备）
3. 设备一致性：
   - 模型和数据必须在同一个 `device`（`mps` 或 `cpu`），否则会报错
4. 线性层认知：
   - `nn.Linear(1, 1)` 本质是学习 `y = w*x + b`
5. 损失函数：
   - `MSELoss` 衡量预测值与真实值误差平方的平均值
6. 优化器与梯度：
   - `loss.backward()` 计算梯度
   - `optimizer.step()` 根据梯度更新参数
7. 推理模式：
   - `with torch.no_grad():` 只推理、不追踪梯度，省内存且更稳定
8. 训练控制变量：
   - `epoch` 控制重复训练轮数，`batch` 控制每次喂入样本数
9. M4 运行关键设置：
   - `PYTORCH_ENABLE_MPS_FALLBACK=1`，MPS不支持算子可回退CPU，减少中断

### LeetCode 记录（Day5）
- 题1：两数之和（`1. Two Sum`）：
  - 是否独立完成：先写出暴力法，后完成哈希法（在讲解后可独立复现）
  - 是否看题解：有参考思路，但核心代码已自己重写通过
  - 复盘一句话：从 `O(n^2)` 双循环升级到哈希表 `O(n)`，关键是“先查补数，再存当前值”
- 题2：移动零（`283. Move Zeroes`）：
  - 是否独立完成：未在 Day5 当天完成（已顺延）
  - 是否看题解：未执行
  - 复盘一句话：Day5 聚焦 Two Sum + 语法补齐，283 放到下一学习日处理

### LeetCode 相关学习知识（Day5）
1. 时间复杂度基础：
   - 暴力双循环是 `O(n^2)`，哈希表查找平均 `O(1)`，所以 Two Sum 可到 `O(n)`。
2. 哈希表核心模型：
   - `mp = {}` 表示“值 -> 下标”映射；
   - 标准顺序是：`need = target - x` -> `if need in mp` -> `mp[x] = i`。
3. `enumerate` 用法：
   - `for i, x in enumerate(nums):` 同时拿下标和元素；
   - `start=1` 表示下标从 1 开始（默认 0）。
4. 常见语法坑：
   - 判断相等要用 `==`，不能用 `=`；
   - `if/elif/else` 缩进必须同层；
   - 字典查的是 key：`if need in mp`，不是 value。
5. 题目迁移点：
   - 167（有序数组）优先考虑双指针；
   - 217（判重）优先考虑 `set()`。

### Git 最小闭环记录（Day5）
- `git init`：`完成`
- `git add .`：`完成`
- `git commit -m "..."`：`完成`
- `git log --oneline -n 3`：`完成`
- `git push`：`完成`
- 今日结论：Git 没有影响主线学习节奏

### 今日提问与答案（Day5，一一对应）
1. 问：MPS fallback 到 CPU 是什么意思？苹果芯片和 x86 有啥区别？  
答：MPS 不支持的算子会自动在 CPU 执行避免中断；Apple Silicon 是 ARM64 + 统一内存，x86 常见是 CPU/GPU 分离生态。

2. 问：`mps` 是啥？  
答：苹果 `Metal Performance Shaders` 后端，PyTorch 在 Mac 上的 GPU 加速通道。

3. 问：`x = torch.tensor(...)` 输出啥样？背后语法是什么？  
答：会输出 `tensor([[1.],[2.],[3.]])`；本质是“函数调用 + 关键字参数 + 赋值”。

4. 问：为什么是二维列表？如何表示多列？  
答：外层是行、内层是列；例如 `[[1,2],[3,4]]` 是 2x2。

5. 问：`2.0` 必须写小数吗？  
答：不必须；写 `2` 也行，`dtype=torch.float32` 会统一转成浮点。

6. 问：`x = x.to(device)`、`model = model.to(device)` 是啥语法？  
答：调用 `.to(...)` 方法把对象移动到设备并重新赋值。

7. 问：`.to` 到底做什么？  
答：转换目标（设备/数据类型），常用是移到 `mps/cpu`。

8. 问：`torch.nn` 和 `nn` 是啥？  
答：`torch.nn` 是神经网络模块库；`nn` 是 `import torch.nn as nn` 的别名。

9. 问：`nn.Linear(1,1)` 和 `pred = model(x)` 是啥？  
答：建立 1 输入 1 输出线性层；后者做前向推理得到预测。

10. 问：MSE 是什么？  
答：`(预测-真实)^2` 后求平均。

11. 问：`optimizer` 和 `loss` 分别是什么实体？  
答：`optimizer` 是更新参数的优化器对象；`loss` 是损失 Tensor。

12. 问：反向传播+更新可否给实际数字例子？  
答：已用 `y=2x+1` 单样本演示 `backward` 得梯度、`step` 更新 `w,b` 后 loss 下降。

13. 问：SGD 是不是反向传播？全称是啥？  
答：不是；反向传播算梯度，SGD 用梯度更新参数；全称 `Stochastic Gradient Descent`。

14. 问：`epoch` 和 `batch` 是什么？  
答：`epoch` 是全量数据过一遍；`batch` 是一次喂入的小批量。

15. 问：`for epoch in range(epochs)` 里 `range` 干啥？  
答：生成循环次数，控制训练重复执行多少轮。

16. 问：`epochs` 要自己设吗？  
答：要，属于超参数。

17. 问：`raise SystemExit(1)` 是啥？  
答：立即退出程序，退出码 1 表示异常退出。

18. 问：`torch.backends.mps` 常用属性有哪些？  
答：常用 `is_available()`、`is_built()`。

19. 问：`final_loss = float(loss.item())` 是啥语法？  
答：从标量 Tensor 取 Python 数值并转为 `float` 后赋值。

20. 问：`loss.backward(); optimizer.step()` 各做什么？  
答：`backward` 计算梯度；`step` 按梯度更新参数。

21. 问：`predict_one(...)` 函数每行在做什么？  
答：构造 `(1,1)` 输入、`no_grad` 推理、提取浮点返回。

22. 问：`nn.linear` 报错为什么？  
答：大小写错误，正确是 `nn.Linear`。

23. 问：Day5 通过后是否可以去 LeetCode？Day6 做啥？  
答：可以；Day6 按复习日策略执行，不上新知识。

24. 问：Hot100 为什么像 300 题、刷题策略怎么定、八股是什么？  
答：你看到的是扩展合集；先做核心高频；八股指 ML/推荐/LLM 工程常问概念体系。

25. 问：做完题若思路不清是否加类似题？  
答：已定策略：思路不清或看题解才做出则加 1 题巩固；思路清楚则下一题。

### 自检（Day5）
- 我能解释 Tensor 的 `shape/dtype/device`：`是`
- 我能解释 `zero_grad()` 的作用：`是`
- 我能解释 `torch.no_grad()` 的作用：`是`
- 我能解释为什么模型和数据要同设备：`是`
- 我能解释 `nn.Linear(1,1)` 的输入输出维度含义：`是`
- Python自评（1-10）：7

### 明日任务（Day 6，MNIST 验收日）
- 只做 MNIST 验收：完成 `everyday_learning/day6/day6_handwrite.py`
- 目标：`phase1 >= 92%`，`phase2 >= 95%`
- 记录：`final loss`、`test acc`、`elapsed sec`

---

## 2026-02-21（Day6：MNIST 验收日）

### 今日计划
- [x] 只做 MNIST 验收（不并行新任务）
- [x] 运行并验证 Day6 训练脚本
- [x] 完成 `everyday_learning/day6/day6_handwrite.py`
- [x] 记录四个指标：`final loss`、`phase1 acc`、`phase2 acc`、`elapsed sec`
- [x] 达标：`phase1 >= 92%`，`phase2 >= 95%`

### 今日产出
- device used：`mps`
- final loss：`0.1933884722709656`
- phase1 test acc（%）：`93.43`
- phase2 test acc（%）：`95.36`
- elapsed sec：`4.7286818749999995`
- 是否通过断言：`是（通过）`

### 今日报错与修复（Day6）
1. 报错信息：`UnboundLocalError: local variable 'transform' referenced before assignment`
   - 原因定位：写成了 `transform = transform.ToTensor`，右侧错误引用了同名局部变量。
   - 修复动作：改为 `transform = transforms.ToTensor()`。
   - 复盘：`ToTensor` 是可调用对象，且这里必须用模块名 `transforms`。

2. 报错信息：`TypeError: __init__() takes 1 positional argument but 2 were given`
   - 原因定位：把 `transforms.ToTensor`（类/构造器）直接传给数据集，没有实例化。
   - 修复动作：补 `()`，即 `transforms.ToTensor()`。
   - 复盘：`transform` 参数需要的是“可调用实例”，不是类本体。

3. 报错信息：`RuntimeError: Tensor for argument input is on cpu but expected on mps`
   - 原因定位：`evaluate_acc` 中 `xb/yb` 未 `.to(device)`，模型在 MPS、数据在 CPU。
   - 修复动作：在评估循环中补齐 `xb = xb.to(device)`、`yb = yb.to(device)`。
   - 复盘：训练与评估都必须保证“模型和数据同设备”。

4. 报错信息：`AttributeError: 'builtin_function_or_method' object has no attribute 'item'`
   - 原因定位：写成了 `.sum.item()`，拿到的是方法对象而不是执行结果。
   - 修复动作：改为 `.sum().item()`。
   - 复盘：凡是方法都要加 `()` 才会执行（`.sum` vs `.sum()`）。

### 今日提问与答案（Day6，一一对应）
1. 问：`train_one_epoch` 里为什么没有 `for epoch in ...`？  
   答：该函数职责是“只训练一个 epoch”；外层 `for epoch in range(...)` 在 `train_pipeline` 控制。

2. 问：`bs = xb.size(0)`、`total_loss += loss.item()*bs`、`total_count += bs` 三行什么意思？  
   答：是在做“按样本数加权的 epoch 平均 loss”，避免最后一个 batch 大小不同导致失真。

3. 问：为什么函数里没定义 batch 大小却能一批一批训练？  
   答：batch 大小在 `DataLoader(..., batch_size=...)` 里定义；函数只从 `train_loader` 取批次。

4. 问：`logits` 是什么？  
   答：模型对每个类别的原始分数（未 softmax），`CrossEntropyLoss` 直接吃 logits。

5. 问：`argmax(dim=1)` 里的 `dim=1` 是什么？  
   答：在 `[batch_size, num_classes]` 里按“类别维”取最大值下标，得到预测类别。

6. 问：`numel()` 是干什么的？  
   答：返回张量元素总数（number of elements），常用于统计样本个数或参数量。

7. 问：`Adam` 和 `model.parameters()` 分别是什么？  
   答：`Adam` 是参数更新优化器；`model.parameters()` 提供模型所有可训练参数给优化器管理。

8. 问：`for _ in range(...)` 里的 `_` 是什么意思？  
   答：占位变量，表示“循环变量本身不需要使用”。

9. 问：为什么 `phase1_acc = evaluate_acc(...)` 在 `for` 外面？  
   答：当前设计是“先训练若干轮，再统一评估一次”，不是每轮都评估。

10. 问：`final_loss` 和 `acc` 没有直接计算关系吗？  
    答：对，代码上无直接依赖；但工程上两者一起看可判断训练是否健康（优化/泛化）。

11. 问：`datasets.MNIST(..., root/download/transform)` 各参数是什么意思？  
    答：`root` 指数据目录，`download=True` 自动下载缺失数据，`transform` 定义取样时预处理规则。

12. 问：`Path(__file__).resolve().parent` 和 `time.perf_counter()` 各在干什么？  
    答：前者用于稳定定位脚本目录并构造路径；后者两次差值用于精确测训练耗时。

13. 问：`transforms.ToTensor()` 做了什么？  
    答：把图像转为 Tensor，常见图像维度从 `HWC` 转 `CHW`，并把像素从 `0~255` 归一到 `0~1`。

### 今日 Day6 总结
- 结果：MNIST baseline 跑通并达标（`phase1 93.43%`，`phase2 95.36%`）。
- 技术收获：打通了 Day6 的完整闭环（数据 -> 训练 -> 评估 -> 指标 -> 断言通过）。
- 主要进步：能独立定位“设备不一致”和“方法对象/方法调用”两类高频报错。
- 后续重点：继续巩固 `DataLoader`、`evaluate_acc`、`loss累计逻辑` 三个最容易混的点。

### Day6 自检
- 我能解释 `DataLoader` 的作用：`是`
- 我能解释 `train()` 和 `eval()` 的区别：`是`
- 我能解释 `argmax(dim=1)` 为什么可用于分类预测：`是`
- 我能解释 `CrossEntropyLoss` 的输入输出要求：`是`
- 我能口述完整训练流程：`是`
- 今日自评（1-10）：`6`

### 明日计划（2026-02-22，复习日）
- 复习 Day1-Day5 + Day6 核心知识，不上新任务。
- 闭卷重写 2 个函数（建议：`top10_word_frequency`、`clean_file`）。
- 复盘本周易错点并更新 `wrongbook.md`。
