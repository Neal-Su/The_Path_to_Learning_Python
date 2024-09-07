my_list = ["itcast","itheima","python"]
index1 = my_list.index("itheima")
print(f"itheima在列表中的下标索引值是：{index1}")
# index2 = my_list.index("hello")
# print(f"hello在列表中的下标索引值是：{index2}")

my_list[0] = "大连海事"
print(f"列表被修改元素值后，结果是：{my_list}")
my_list.insert(1,"信息学院")
print(f"列表插入元素后，结果是{my_list}")
my_list.append("双学位")
print(f"列表在追加了元素后，结果是{my_list}")
my_list2 = ["计算机科学","人工智能"]
my_list.extend(my_list2)
print(f"列表在追加了一个新的列表后，结果是{my_list}")

del my_list[2]
print(f"列表删除元素后的结果是：{my_list}")
element = my_list.pop(5)
print(f"通过pop方法取出元素后，列表内容：{my_list}，取出的元素内容是：{element}")

my_list.remove("python")
print(f"通过remove方法移除元素后，列表的结果是{my_list}")
# remove是删除某元素在列表中的第一个匹配项，只能删掉一个

count = my_list.count("大连海事")
print(f"列表中大连海事的数量是：{count}")

count = len(my_list)
print(f"列表中元素的数量是：{count}")

my_list.clear()
print(f"列表被清空了，结果是：{my_list}")

# 列表可以容纳不同类型的元素
# 列表是有序存储的（右下标序号）
# 允许重复数据存在
# 可以修改

# 列表的常用操作方法