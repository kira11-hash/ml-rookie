"""
Day4 手写练习（必须自己填空）
目标：文件IO / 异常处理（try-except）
任务：实现 clean_file(input_path, output_path)
"""

import os

print("=== Day4 手写练习开始 ===")


# 任务1：写一个演示输入文件（供后续清洗）
def write_demo_file(path):
    # TODO: 用 with open(..., "w", encoding="utf-8") 写入演示文本
    # 演示文本建议：
    #   "  Python   is FUN  \\n\\n  ML   is practical.  \\n"
    pass


# 任务2：清洗单行文本
# 目标：
# 1) 去首尾空白
# 2) 压缩多个空白为单空格
# 3) 转小写
# 4) 若清洗后为空字符串，返回空字符串
def clean_line(line):
    # TODO: 在下面补代码
    return ""


# 任务3：实现 clean_file
# 要求：
# 1) 读取 input_path
# 2) 对每行调用 clean_line
# 3) 丢掉空行
# 4) 写入 output_path（每行末尾加换行）
# 5) 成功返回 True，异常时返回 False
def clean_file(input_path, output_path):
    # TODO: 用 try-except 包裹文件读写
    # 提示：先 except FileNotFoundError，再 except Exception as e
    return False


input_path = "day4_input_demo.txt"
output_path = "day4_output_demo.txt"

write_demo_file(input_path)
ok = clean_file(input_path, output_path)
print("clean_file 执行结果:", ok)

if ok:
    with open(output_path, "r", encoding="utf-8") as f:
        print("清洗后文件内容:")
        print(repr(f.read()))


# 可选：测试不存在的文件（应返回 False）
missing_ok = clean_file("not_exists_file.txt", "tmp_should_not_exist.txt")
print("不存在文件测试结果(应为False):", missing_ok)


# 验收（补全后应通过）
assert clean_line("  A   B  ") == "a b", "clean_line 规则有误"
assert ok is True, "clean_file 应返回 True"
assert os.path.exists(output_path), "输出文件未生成"
with open(output_path, "r", encoding="utf-8") as f:
    content = f.read()
assert content == "python is fun\nml is practical.\n", "输出文件内容不符合预期"
assert missing_ok is False, "不存在文件时应返回 False"

print("\nDay4 手写练习通过。")
