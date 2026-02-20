"""
Day1 手写练习（必须自己填空）
目标：变量 / if / 函数 / print + grade_level + BMI
说明：这个文件故意留空，你需要自己补全 TODO。
"""

print("=== Day1 手写练习开始 ===")

# 任务1：变量与输出
# 要求：
# 1) 定义 name, age, target 三个变量
# 2) 打印三行：姓名、年龄、目标

# TODO: 在下面补代码
name = "Qingan" 
age = 22
target = "find a job in machine learning field"

# 任务2：条件判断
# 要求：
# 1) 定义 score（你自己给一个整数）
# 2) 用 if / elif / else 打印成绩等级（A/B/C/D）

# TODO: 在下面补代码
score = 95

if score > 90:
    print("A")
elif score > 80:
    print("B")
elif score > 70:
    print("C")
else :
    print("D")

# 任务3：实现 grade_level 函数
# 要求：
# 1) 输入 score_value
# 2) 返回 A/B/C/D/F
def grade_level(score_value):
    # TODO: 在下面补代码
    tier = None 

    if score_value >= 90:
        tier = "A"
    elif score_value >= 80:
        tier = "B"
    elif score_value >= 70:
        tier = "C"
    elif score_value >= 60 :
        tier = "D"
    else :
        tier = "F"

    return tier


print("\n=== grade_level 测试 ===")
print("100 -> 等级", grade_level(100))
print("95 -> 等级", grade_level(95))
print("83 -> 等级", grade_level(83))
print("76 -> 等级", grade_level(76))
print("61 -> 等级", grade_level(61))
print("42 -> 等级", grade_level(42))


# 任务4：实现 BMI 计算器
# 要求：
# 1) bmi_value(weight_kg, height_m) 返回 BMI
# 2) bmi_level(bmi) 返回 "偏瘦/正常/偏胖/肥胖"
def bmi_value(weight_kg, height_m):
    # TODO: 在下面补代码
    value = weight_kg/(height_m*height_m)
    return value


def bmi_level(bmi):
    # TODO: 在下面补代码
    level = None
    if bmi <= 18.5:
        level ="偏瘦"
    elif bmi <= 24 :
        level = "正常"
    elif bmi <= 28:
        level = "偏胖"
    else :
        level = "肥胖"
    return level


weight = 65
height = 1.75
bmi = bmi_value(weight, height)
print("\n=== BMI 测试 ===")
print("体重:", weight, "kg")
print("身高:", height, "m")
print("BMI:", round(bmi, 2))
print("BMI等级:", bmi_level(bmi))


# 验收（你补全后，下面断言应该通过）
assert grade_level(95) == "A", "grade_level 规则有误（95 应为 A）"
assert grade_level(42) == "F", "grade_level 规则有误（42 应为 F）"
assert round(bmi_value(65, 1.75), 2) == 21.22, "BMI 公式有误"
assert bmi_level(21.22) == "正常", "BMI 分级规则有误（21.22 应为 正常）"

print("\nDay1 手写练习通过。")
