# 元组的课后练习

student = ("蔡徐坤", 2.5, ["唱", "跳", "Rap", "篮球"])
index = student.index(2.5)
print(f"学生年龄的下标位置是：{index}")
name = student[0]
print(f"学生的姓名是：{name}")
del student[2][3]
print(f"删除篮球后的元组是：{student}")
student[2].append("篮球")
print(f"增加篮球后的元组是：{student}")
