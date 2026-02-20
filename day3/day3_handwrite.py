"""
Day3 手写练习（必须自己填空）
目标：函数进阶 / 字符串处理 / 正则表达式
任务：实现 clean_text(text)
"""

import re

print("=== Day3 手写练习开始 ===")


# 任务1：实现空白归一化函数
# 要求：
# 1) 把多个空格/Tab/换行压成单个空格
# 2) 去掉首尾空格
def normalize_spaces(text):
    # TODO: 在下面补代码
    text = re.sub(r"\s+"," ",text).strip()
    return text



# 任务2：实现 clean_text
# 目标：把原始文本清洗成“只保留英文单词和单空格”的格式
# 推荐步骤：
# 1) 全部转小写
# 2) 去掉 URL（http/https/www 开头）
# 3) 非字母字符替换为空格
# 4) 调用 normalize_spaces 压缩空白
def clean_text(text):
    # TODO 1: 转小写
    text = text.lower()
    # TODO 2: 去 URL
    text = re.sub(r"https?://\S+|www\.\S+", " ", text)
    # TODO 3: 去非字母字符（只留 a-z 和空白）
    text = re.sub(r"[^a-z\s]"," ",text)
    # TODO 4: 归一化空白
    text = " ".join(text.split())
    # TODO 5: return
    return text


sample_text = "Hello!!!  ML is FUN. Visit https://example.com now, 100% sure."
cleaned = clean_text(sample_text)
print("清洗结果:", cleaned)


# 可选输入模式
user_text = input("请输入一段待清洗文本（可直接回车跳过）: ").strip()
if user_text:
    print("你的清洗结果:", clean_text(user_text))
else:
    print("你跳过了自定义输入。")


# 验收（补全后应通过）
assert normalize_spaces("a   b\tc\n d") == "a b c d", "空白归一化失败"
assert clean_text("A!! B?? C...") == "a b c", "标点清洗失败"
assert clean_text("Go to https://abc.com NOW!") == "go to now", "URL 清洗失败"
assert clean_text(sample_text) == "hello ml is fun visit now sure", "综合清洗失败"

print("\nDay3 手写练习通过。")
