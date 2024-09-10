# 集合的定义与操作

# 集合不支持重复元素，自带去重功能，并且内容无序

# 定义
my_set = {"大连海事大学","信息学院","计算机科学与技术","内容是无序不重复的","大连海事大学","信息学院","计算机科学与技术"}
my_set_empty = set()
print(f"my_set的内容是：{my_set}，类型是：{type(my_set)}")
print(f"my_set_empty的内容是：{my_set_empty}，类型是：{type(my_set_empty)}")

# 集合是无序的，所以不支持下标索引，但支持修改

# 添加新元素
my_set.add("python")
my_set.add("大连海事大学")  # 去重所以不会添加成功
print(f"my_set添加元素后的结果是：{my_set}")

# 移除元素
my_set.remove("python")
print(f"my_set移除元素后的结果是：{my_set}")

# 随机取出一个元素
element = my_set.pop()
print(f"集合被取出元素：{element}，my_set取出元素后的结果是：{my_set}")

# 清空集合
my_set.clear()
print(f"my_set清空后的结果是：{my_set}")

# 取出两个集合的差集，集合1有而集合2没有的
# 得到一个新的集合，原来的集合1和集合2不变
set1 = {1, 2, 3}
set2 = {1, 4, 5}
set3 = set1.difference(set2)
print(f"取出差集后的结果是；{set3}")
print(f"取出差集后原有set1；{set1}")
print(f"取出差集后原有set2；{set2}")

# 消除两个集合的差集
# 在集合1内删除和集合2相同的元素
# 结果：集合1内的元素被修改，集合2不变
set1.difference_update(set2)
print(f"消除差集后set1结果；{set1}")
print(f"消除差集后set2结果；{set2}")

# 两个集合合并
# 将集合1和集合2组合成新集合
# 结果：得到新集合，集合1和集合2不变
set1 = {1, 2, 3}
set2 = {1, 4, 5}
set3 = set1.union(set2)
print(f"两集合合并后set3的结果；{set3}")  # 去重，所以不会出现两个1
print(f"合并后set1；{set1}")
print(f"合并后set2；{set2}")

# 统计集合元素数量
num = len(set1)
print(f"集合内元素有:{num}个")

# 集合的遍历
# 集合不支持下标索引，所以不可以用while循环
# 可以用for循环
for element in set1:
    print(f"集合的元素有：{element}")