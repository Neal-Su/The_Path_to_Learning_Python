# 字符串的定义和操作

# 字符串是无法修改的数据容器

# 通过下标索引取值
my_str = "大连海事大学信息学院"
value1 = my_str[2]
value2 = my_str[-2]
print(f"从字符串{my_str}取下标为2的元素，值为：{value1}")
print(f"从字符串{my_str}取下标为-2的元素，值为：{value2}")

# index查找方法
value3 = my_str.index("海事")
print(f"在字符串{my_str}中查找海事，其起始下标是：{value3}")

# 字符串的替换
# 将字符串内的全部字符串1替换为字符串2
# 注意:不是修改字符串本身，而是得到了一个新字符串
new_my_str = my_str.replace("信息","船舶")
print(f"将字符串{my_str}，进行替换后得到{new_my_str}")

# 字符串的分割
# 按照指定的分隔符字符串，将字符串划分为多个字符串，并存入列表对象中
# 注意：字符串本身不发生变化，而是得到了一个列表对象
my_str = "hello python itheima itcast"
my_str_list = my_str.split(" ")
print(f"将字符串{my_str}进行split切分后得到：{my_str_list}，类型是{type(my_str_list)}")

# strip，字符串的规整
# strip参数为默认值时，去除字符串前后的空格
my_str = "  dalian maritime university  "
new_my_str = my_str.strip()  # 不传入参数，去除首尾空格
# strip有参数时，去除前后指定字符串
# 传入的其实是1和2为内容的两个字符串，后面的21也会移除
print(f"字符串{my_str}被strip后，结果是：{new_my_str}")
my_str = "12dalian maritime university21"
new_my_str = my_str.strip("12")
print(f"字符串{my_str}被strip('12')后，结果是：{new_my_str}")

# 统计字符串中某字符串的出现次数
value4 = my_str.count("it")
print(f"字符串{my_str}中it出现的次数是：{value4}")

# 统计字符串的长度
value5 = len(my_str)
print(f"字符串{my_str}的长度是：{value5}")