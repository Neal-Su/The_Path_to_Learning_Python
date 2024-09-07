# 列表的循环遍历课后作业
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
oushu_list = []
index = 0
while index < len(my_list):
    if my_list[index] % 2 == 0:
        oushu_list.append(my_list[index])
    index += 1
print(f"{oushu_list}")
oushu_list.clear()
print(f"{oushu_list}")
for element in my_list:
    if element % 2 == 0:
        oushu_list.append(element)
print(f"{oushu_list}")
