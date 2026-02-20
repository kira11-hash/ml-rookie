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
- [x] 完成 `day1/day1_handwrite.py`
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
- [x] 完成 `day2/day2_handwrite.py`
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
- [x] 完成 `day3/day3_handwrite.py`
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
- 完成 `day4/day4_handwrite.py`（已创建，待完成）

---

## 2026-02-20（预备周 Day 4）模板

### 今日计划
- [ ] 完成 `day4/day4_handwrite.py`
- [ ] 理解 `with open(..., mode, encoding="utf-8")` 的标准写法
- [ ] 理解 `try-except`：专门异常 + 兜底异常
- [ ] 实现 `clean_file(input_path, output_path)` 并通过断言
- [ ] 独立修复至少 1 个真实报错

### 时间记录
- 开始时间：
- 结束时间：
- 专注时长（分钟）：

### 今日完成
- [ ]
- [ ]
- [ ]
- [ ]

### 易错语法提醒（Day4）
- [ ] 写文件用 `"w"` 会覆盖原文件，注意是否需要备份
- [ ] `write()` 不会自动换行，必要时手动加 `\\n`
- [ ] 记得指定 `encoding="utf-8"`
- [ ] 文件读写优先用 `with open(...)`，不要忘记关闭文件
- [ ] `try` 后至少要有一个 `except`
- [ ] `except FileNotFoundError` 建议写在 `except Exception` 前面
- [ ] 成功/失败路径都要 `return`，避免返回 `None`
- [ ] 先读行列表，再清洗，再写回，避免流程混乱

### 今日报错与修复
- 报错1：
  - 报错信息（原文）：
  - 原因定位：
  - 修复动作：
  - 修复后结果：
- 报错2（可选）：
  - 报错信息（原文）：
  - 原因定位：
  - 修复动作：
  - 修复后结果：

### 关键代码/结果记录
- 输入文件路径：
- 输出文件路径：
- `clean_file` 返回值：
- 输出文件内容（repr）：
- 不存在文件测试返回值（应为 False）：
- 终端最终输出是否包含：`Day4 手写练习通过。`（是/否）

### 自检（Day4）
- 我能解释 `with open(...) as f` 为什么更安全：`是 / 否`
- 我能解释 `r / w / a` 三种模式区别：`是 / 否`
- 我能解释 `FileNotFoundError` 与 `Exception as e` 的区别：`是 / 否`
- 我能口述 clean_file 的 6 步流程：`是 / 否`
- Python自评（1-10）：

### 明日任务（2026-02-21 Day 5）
- PyTorch 预热（tensor/device/linear）
- LeetCode 2题（两数之和、移动零）
- Git 本地入门（init/add/commit/log）

---

## 2026-02-21（预备周 Day 5）模板

### 今日计划
- [ ] 环境检查通过（PyTorch + MPS 可用性）
- [ ] 完成 `day5/day5_handwrite.py`
- [ ] 理解最小训练循环：`forward -> loss -> backward -> step`
- [ ] LeetCode 2题：两数之和、移动零
- [ ] Git 最小闭环：`init/add/commit/log`

### 时间记录
- 开始时间：
- 结束时间：
- 专注时长（分钟）：

### 环境检查（Day5）
- 命令1：`export PYTORCH_ENABLE_MPS_FALLBACK=1`
- 命令2：`/usr/bin/python3 -c "import torch; print(torch.__version__); print('mps:', torch.backends.mps.is_available())"`
- 可选脚本：`/usr/bin/python3 "/Users/chenqingan/Library/Mobile Documents/com~apple~CloudDocs/ml-rookie/day5/day5_env_check.py"`
- PyTorch 版本：
- MPS 可用（True/False）：
- 实际使用设备（`mps/cpu`）：

### 今日完成
- [ ]
- [ ]
- [ ]
- [ ]

### 易错语法提醒（Day5）
- [ ] 模型和数据必须在同一个 device（都在 `mps` 或都在 `cpu`）
- [ ] 训练三连顺序不能错：`zero_grad -> backward -> step`
- [ ] 推理时要用 `with torch.no_grad():`
- [ ] `loss.item()` 才是 Python 数值，`loss` 本体是 Tensor
- [ ] `nn.Linear(1,1)` 输入形状通常是 `[N, 1]`
- [ ] 学习率过大可能不收敛，过小会很慢
- [ ] `torch.manual_seed(...)` 便于复现实验

### 今日报错与修复
- 报错1：
  - 报错信息（原文）：
  - 原因定位：
  - 修复动作：
  - 修复后结果：
- 报错2（可选）：
  - 报错信息（原文）：
  - 原因定位：
  - 修复动作：
  - 修复后结果：

### 关键结果记录（Day5）
- `day5_handwrite.py` 是否通过：`是 / 否`
- 终端最终输出是否包含：`Day5 手写练习通过。`（是/否）
- 训练最终 `final_loss`：
- `x=4.0` 的预测值（应接近 9）：
- 训练循环是否能口述 5 步：`是 / 否`

### LeetCode 记录（Day5）
- 题1：两数之和（`1. Two Sum`）：
  - 是否独立完成：
  - 是否看题解：
  - 复盘一句话：
- 题2：移动零（`283. Move Zeroes`）：
  - 是否独立完成：
  - 是否看题解：
  - 复盘一句话：

### Git 最小闭环记录（Day5）
- `git init`：`完成 / 未完成`
- `git add .`：`完成 / 未完成`
- `git commit -m "..."`：`完成 / 未完成`
- `git log --oneline -n 3`：`完成 / 未完成`
- 今日结论：Git 是否影响主线学习节奏：`是 / 否`

### 今日提问与答案（Day5，一一对应）
1. 问：  
答：
2. 问：  
答：
3. 问：  
答：

### 自检（Day5）
- 我能解释 Tensor 的 `shape/dtype/device`：`是 / 否`
- 我能解释 `zero_grad()` 的作用：`是 / 否`
- 我能解释 `torch.no_grad()` 的作用：`是 / 否`
- 我能解释为什么模型和数据要同设备：`是 / 否`
- Python自评（1-10）：

### 明日任务（Week 1 Day 1）
- 跑通 MNIST 训练循环
- 目标：测试集准确率 > 95%
- LeetCode 继续 1 题
