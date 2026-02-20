"""
Day2 手写练习（必须自己填空）
目标：list / dict / for + 词频Top10
说明：这个文件故意留空，你需要自己补全 TODO。
"""

print("=== Day2 手写练习开始 ===")

# 任务1：列表练习
# 要求：
# 1) 创建一个列表 scores，内容是 [88, 92, 76]
# 2) 追加 95
# 3) 排序
# 4) 打印排序后的列表

# TODO: 在下面补代码
scores = [88,92,76]
scores.append(95)
scores.sort()
print(scores)

# 任务2：实现词频函数
# 输入：英文文本 text（字符串）
# 输出：top10（[(word, count), ...]）、总词数、去重词数
def top10_word_frequency(text):
    # TODO 1: 转小写
    text=text.lower()
    # TODO 2: 清洗文本，只保留字母和空格
    clean_chars = []
    for ch in text:
        if ch.isalpha() or ch == " ":
            clean_chars.append(ch)
        else :
            clean_chars.append(" ")
    # TODO 3: split 切词
    clean_text = "".join(clean_chars)
    words = clean_text.split()
    # TODO 4: 用 dict 做词频统计
    freq = {}
    for w in words :
        freq[w] = freq.get(w, 0)+1
    # TODO 5: 排序，频次降序 + 单词升序
    sorted_items = []
    sorted_items = sorted(freq.items(),key = lambda x:(-x[1],x[0]))
    # TODO 6: 返回 top10, 总词数, 去重词数
    return sorted_items[:10], len(words), len(freq)


sample_text = """
Machine learning is fun. Learning by doing is better than only reading.
Python is simple, and machine learning with Python is practical.
If you practice every day, your coding skill will grow.
"""

top10, total_words, unique_words = top10_word_frequency(sample_text)

print("\n总词数:", total_words)
print("去重词数:", unique_words)
print("Top10:")
for i, item in enumerate(top10, start=1):
    print(i, item)


# 验收（你补全后，下面断言应该通过）
assert total_words >= 30, "总词数不对，请检查 split 逻辑"
assert unique_words >= 20, "去重词数偏低，请检查清洗逻辑"
assert len(top10) <= 10, "top10 长度应 <= 10"
assert len(top10) > 0, "top10 为空，说明函数没实现"

print("\nDay2 手写练习通过。")
