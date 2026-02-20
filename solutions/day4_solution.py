"""
Day4 参考解
主题：文件IO / 异常处理（try-except）
任务：clean_file(input_path, output_path)
"""

import os

print("=== Day4 参考解开始 ===")


def write_demo_file(path):
    demo_text = "  Python   is FUN  \n\n  ML   is practical.  \n"
    with open(path, "w", encoding="utf-8") as f:
        f.write(demo_text)


def clean_line(line):
    line = line.strip()
    if not line:
        return ""
    line = " ".join(line.split())
    return line.lower()


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
        print(f"[错误] 文件不存在: {input_path}")
        return False
    except Exception as e:
        print(f"[错误] 处理文件失败: {e}")
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

missing_ok = clean_file("not_exists_file.txt", "tmp_should_not_exist.txt")
print("不存在文件测试结果(应为False):", missing_ok)


assert clean_line("  A   B  ") == "a b", "clean_line 规则有误"
assert ok is True, "clean_file 应返回 True"
assert os.path.exists(output_path), "输出文件未生成"
with open(output_path, "r", encoding="utf-8") as f:
    content = f.read()
assert content == "python is fun\nml is practical.\n", "输出文件内容不符合预期"
assert missing_ok is False, "不存在文件时应返回 False"

print("\nDay4 参考解通过。")
