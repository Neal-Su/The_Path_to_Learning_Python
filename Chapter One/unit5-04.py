student_age = [21,25,21,23,22,20]
new_list = [29,33,30]
student_age.append(31)
print(f"追加一个数字31到列表尾部，结果是：{student_age}")
student_age.extend(new_list)
print(f"追加一个新列表到列表尾部，结果是：{student_age}")
element1 = student_age[0]
print(f"取出第一个元素，取出的元素是{element1}，列表是：{student_age}")
element2 = student_age[-1]
print(f"取出最后一个元素，取出的元素是{element2}，列表是：{student_age}")
index1 = student_age.index(31)
print(f"查找元素31在列表中下标的位置，位置是{index1}")

# 列表的常用操作课后练习
