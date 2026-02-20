"""
预备周 - 第2天
主题：list / dict / for
任务：英文文本词频 Top10
"""

print("=== Day 2 开始：数据结构与循环 ===")

# ----------------------------
# 第1关：list（列表）基础
# ----------------------------
scores = [88, 92, 76]
print("\n[第1关] 初始分数列表:", scores)

scores.append(95)  # 追加元素
print("[第1关] append 后:", scores)

first_score = scores[0]  # 下标访问，第一个元素
print("[第1关] 第一个分数:", first_score)

scores.sort()  # 原地排序（升序）
print("[第1关] sort 后:", scores)


# ----------------------------
# 第2关：dict（字典）基础
# ----------------------------
student = {"name": "Qingan", "major": "IC", "target": "ML"}
print("\n[第2关] 学生信息字典:", student)
print("[第2关] name 字段:", student["name"])

student["city"] = "Hangzhou"  # 新增键值
student["target"] = "ML Internship"  # 修改键值
print("[第2关] 更新后字典:", student)


# ----------------------------
# 第3关：for 循环基础
# ----------------------------
print("\n[第3关] 遍历分数列表:")
for s in scores:
    print("分数:", s)

print("[第3关] range 循环（0到4）:")
for i in range(5):
    print("i =", i)


# ----------------------------
# 第4关：核心任务 - 词频 Top10
# ----------------------------
def top10_word_frequency(text):
    """
    输入：英文文本字符串
    输出：词频前10（列表）
    """
    # 1) 统一小写
    text = text.lower()

    # 2) 仅保留字母和空格，其他符号替换为空格
    cleaned_chars = []
    for ch in text:
        if ch.isalpha() or ch == " ":
            cleaned_chars.append(ch)
        else:
            cleaned_chars.append(" ")

    cleaned_text = "".join(cleaned_chars)

    # 3) 切词
    words = cleaned_text.split()

    # 4) 词频统计（dict）
    freq = {}
    for w in words:
        # get 的写法能避免 KeyError
        freq[w] = freq.get(w, 0) + 1

    # 5) 排序：先按频次降序，再按单词字母序升序
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

    return sorted_items[:10], len(words), len(freq)


sample_text = """
Machine learning is fun. Learning by doing is better than only reading.
Python is simple, and machine learning with Python is practical.
If you practice every day, your coding skill will grow.
"""

top10, total_words, unique_words = top10_word_frequency(sample_text)

print("\n[第4关] 词频统计结果")
print("总词数:", total_words)
print("去重后词数:", unique_words)
print("Top10:")
for idx, (word, count) in enumerate(top10, start=1):
    print(f"{idx:2d}. {word:<10} -> {count}")


# 可选：输入你自己的英文句子测试
print("\n=== 可选输入模式 ===")
user_text = input("请输入一段英文文本（可直接回车跳过）: ").strip()
if user_text:
    user_top10, user_total, user_unique = top10_word_frequency(user_text)
    print("你的总词数:", user_total)
    print("你的去重词数:", user_unique)
    print("你的Top10:")
    for idx, (word, count) in enumerate(user_top10, start=1):
        print(f"{idx:2d}. {word:<10} -> {count}")
else:
    print("你跳过了自定义输入。")
