# 容器的通用转换操作

# 定义5重数据容器
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_str = "abcdefg"
my_set = {1, 2, 3, 4, 5}
my_dict = {"key1": 1, "key2": 2, "key3": 3, "key4": 4, "key5": 5}

# 容器转列表
print(f"列表 \t转列表的结果是：{list(my_list)}")
print(f"元组 \t转列表的结果是：{list(my_tuple)}")
print(f"字符串 \t转列表的结果是：{list(my_str)}")
print(f"集合 \t转列表的结果是：{list(my_set)}")
print(f"字典 \t转列表的结果是：{list(my_dict)}")
# 容器转元组
print(f"列表 \t转元组的结果是：{tuple(my_list)}")
print(f"元组 \t转元组的结果是：{tuple(my_tuple)}")
print(f"字符串 \t转元组的结果是：{tuple(my_str)}")
print(f"集合 \t转元组的结果是：{tuple(my_set)}")
print(f"字典 \t转元组的结果是：{tuple(my_dict)}")
# 容器转字符串
print(f"列表 \t转字符串的结果是：{str(my_list)}")
# 实质上是"[1, 2, 3, 4, 5]"
print(f"元组 \t转字符串的结果是：{str(my_tuple)}")
# 实质上是"(1, 2, 3, 4, 5)"
print(f"字符串 \t转字符串的结果是：{str(my_str)}")
print(f"集合 \t转字符串的结果是：{str(my_set)}")
print(f"字典 \t转字符串的结果是：{str(my_dict)}")
# 容器转集合
print(f"列表 \t转集合的结果是：{set(my_list)}")
print(f"元组 \t转集合的结果是：{set(my_tuple)}")
print(f"字符串 \t转集合的结果是：{set(my_str)}")
print(f"集合 \t转集合的结果是：{set(my_set)}")
print(f"字典 \t转集合的结果是：{set(my_dict)}")