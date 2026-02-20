"""
预备周 - 第1天
主题：变量 / if判断 / print输出
任务：成绩等级函数 + BMI计算器
"""

print("=== Day 1 开始 ===")

# ----------------------------
# 第1关：变量 + 输出
# ----------------------------
name = "Qingan"
age = 22
target = "ML实习"
print("姓名:", name)
print("年龄:", age)
print("目标:", target)

# ----------------------------
# 第2关：if / elif / else
# ----------------------------
score = 59
if score >= 90:
    print("当前等级: A")
elif score >= 80:
    print("当前等级: B")
elif score >= 70:
    print("当前等级: C")
else:
    print("当前等级: D")


# ----------------------------
# 第3关：任务1 - grade_level
# ----------------------------
def grade_level(score_value):
    if score_value >= 90:
        return "A"
    elif score_value >= 80:
        return "B"
    elif score_value >= 70:
        return "C"
    elif score_value >= 60:
        return "D"
    else:
        return "F"


print("\n=== grade_level 测试 ===")
print("100 -> 等级", grade_level(100))
print("95 -> 等级", grade_level(95))
print("83 -> 等级", grade_level(83))
print("76 -> 等级", grade_level(76))
print("61 -> 等级", grade_level(61))
print("42 -> 等级", grade_level(42))


# ----------------------------
# 第4关：任务2 - BMI计算器
# ----------------------------
def bmi_value(weight_kg, height_m):
    return weight_kg / (height_m ** 2)


def bmi_level(bmi):
    if bmi < 18.5:
        return "偏瘦"
    elif bmi < 24:
        return "正常"
    elif bmi < 28:
        return "偏胖"
    else:
        return "肥胖"


# 示例数值
weight = 65
height = 1.75
bmi = bmi_value(weight, height)
print("\n=== BMI 测试 ===")
print("体重:", weight, "kg")
print("身高:", height, "m")
print("BMI:", round(bmi, 2))
print("BMI等级:", bmi_level(bmi))


# 可选交互模式
# 如果今天太累，这一部分可以明天再练。
print("\n=== 可选输入模式 ===")
user_weight = float(input("请输入你的体重(kg): "))
user_height = float(input("请输入你的身高(m): "))
user_bmi = bmi_value(user_weight, user_height)
print("你的BMI:", round(user_bmi, 2))
print("你的BMI等级:", bmi_level(user_bmi))
