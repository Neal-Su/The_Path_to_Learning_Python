# 元组的操作

t5 = ((1, 2, 3), (4, 5, 6))

num = t5[1][2]
print(f"从嵌套元组中取出的数据是：{num}")

t6 = ("大连海事", "信息学院", "计算机", "双学位", "信息学院")
index = t6.index("计算机")
print(f"在元组t6中查找计算机的下标是：{index}")

num = t6.count("信息学院")
print(f"在元组t6中统计信息学院的数量有：{num}个")

length = len(t6)
print(f"在元组t6中的元素有：{length}个")

index = 0
while index < len(t6):
    print(f"元组t6中的元素有：{t6[index]}")
    index += 1

for element in t6:
    print(f"for遍历的元组的元素有：{element}")