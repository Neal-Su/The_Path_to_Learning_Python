# 数据容器的通用操作

# 定义5重数据容器
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_str = "abcdefg"
my_set = {1, 2, 3, 4, 5}
my_dict = {"key1": 1, "key2": 2, "key3": 3, "key4": 4, "key5": 5}

# len得出元素个数
print(f"列表 \t元素个数有：{len(my_list)}个")
print(f"元组 \t元素个数有：{len(my_tuple)}个")
print(f"字符串 \t元素个数有：{len(my_str)}个")
print(f"集合 \t元素个数有：{len(my_set)}个")
print(f"字典 \t元素个数有：{len(my_dict)}个")
# max找出最大的元素
print(f"列表 \t最大的元素：{max(my_list)}")
print(f"元组 \t最大的元素：{max(my_tuple)}")
print(f"字符串 \t最大的元素：{max(my_str)}")
print(f"集合 \t最大的元素：{max(my_set)}")
print(f"字典 \t最大的元素：{max(my_dict)}")
# min找出最小的元素
print(f"列表 \t最小的元素：{min(my_list)}")
print(f"元组 \t最小的元素：{min(my_tuple)}")
print(f"字符串 \t最小的元素：{min(my_str)}")
print(f"集合 \t最小的元素：{min(my_set)}")
print(f"字典 \t最小的元素：{min(my_dict)}")
# 容器通用排序
# 排序的结果会都变成列表对象
my_list = [3, 1, 2, 5, 4]
my_tuple = (3, 1, 2, 5, 4)
my_str = "fgadebc"
my_set = {3, 1, 2, 5, 4}
my_dict = {"key3": 1, "key1": 2, "key2": 3, "key5": 4, "key4": 5}
print(f"列表 \t的排序结果：{sorted(my_list)}")
print(f"元组 \t的排序结果：{sorted(my_tuple)}")
print(f"字符串 \t的排序结果：{sorted(my_str)}")
print(f"集合 \t的排序结果：{sorted(my_set)}")
print(f"字典 \t的排序结果：{sorted(my_dict)}")

print(f"列表 \t的反向排序结果：{sorted(my_list, reverse=True)}")
print(f"元组 \t的反向排序结果：{sorted(my_tuple, reverse=True)}")
print(f"字符串 \t的反向排序结果：{sorted(my_str, reverse=True)}")
print(f"集合 \t的反向排序结果：{sorted(my_set, reverse=True)}")
print(f"字典 \t的反向排序结果：{sorted(my_dict, reverse=True)}")

# 扩展列表的sort排序方法对列表进行自定义排序
# 使用方法:
# 列表.sort(key=选择排序依据的函数, reverse=True/False)
# """
# 参数key：    要求传入一个函数，表示将列表的每一个元素都传入函数，返回排序的依据
# 参数reverse：是否反转排序结果，True表示降序，False表示升序
# """

# 如下嵌套列表，排序的依据是内层列表的第二个元素数字
# 以前学习的sorted函数就无法适用了，可以使用列表的sort方法
# 准备列表
my_list = [["a", 33], ["b", 55], ["c", 11]]

# 排序，基于带名函数：
# 定义排序方法函数
def choose_sort_key(element):
    # 这个函数的意思是把每个元素给我传进来
    # 由我这个函数决定按照元素里面的哪一部分取排序
    return element[1]  # 按照每个元素的下标1去排序

my_list.sort(key=choose_sort_key, reverse=True)
print(my_list)

# 排序基于lambda匿名函数
my_list.sort(key=lambda element: element[1], reverse=True)
print(my_list)
