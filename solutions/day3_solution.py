"""
Day3 参考解
主题：函数进阶 / 字符串处理 / 正则表达式
任务：clean_text(text)
"""

import re

print("=== Day3 参考解开始 ===")


def normalize_spaces(text):
    # split() 默认按任意空白切分，再用单空格拼接
    return " ".join(text.split())


def clean_text(text):
    # 1) 小写化
    text = text.lower()

    # 2) 去 URL
    text = re.sub(r"https?://\S+|www\.\S+", " ", text)

    # 3) 非字母替换为空格
    text = re.sub(r"[^a-z\s]", " ", text)

    # 4) 空白归一化
    text = normalize_spaces(text)

    return text


sample_text = "Hello!!!  ML is FUN. Visit https://example.com now, 100% sure."
cleaned = clean_text(sample_text)
print("清洗结果:", cleaned)

user_text = input("请输入一段待清洗文本（可直接回车跳过）: ").strip()
if user_text:
    print("你的清洗结果:", clean_text(user_text))
else:
    print("你跳过了自定义输入。")


assert normalize_spaces("a   b\tc\n d") == "a b c d", "空白归一化失败"
assert clean_text("A!! B?? C...") == "a b c", "标点清洗失败"
assert clean_text("Go to https://abc.com NOW!") == "go to now", "URL 清洗失败"
assert clean_text(sample_text) == "hello ml is fun visit now sure", "综合清洗失败"

print("\nDay3 参考解通过。")
