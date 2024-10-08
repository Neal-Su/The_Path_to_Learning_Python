# 序列的切片
# 序列是指内容连续、有序、可使用下标索引、的一类数据容器
# 列表、元组、字符串、均可视为序列
# 切片:从一个序列中取出一个子序列

# 语法：序列[起始下标：结束下标：步长]
# 表示从序列中，从指定位置开始，依次取出元素，到指定位置结束，得到一个新序列：
# 起始下标表示从何处开始，可以留空，留空视作从头开始
# 结束下标（不含）表示何处结束，可以留空，留空视作截取到结尾
# 步长表示，依次取元素的间隔
# 步长1表示，一个个取元素
# 步长2表示，每次跳过1个元素取
# 步长N表示，每次跳过N—1个元素取
# 步长为负数表示，反向取（注意，起始下标和结束下标也要反向标记）

# 注意：此操作不会影响到序列本身，而会得到一个新的序列

# 对list进行切片
my_list = [0, 1, 2, 3, 4, 5, 6]
result1 = my_list[1:4]  #步长默认是1，所以可以省略不写
print(f"结果1{result1}")

# 对tuple进行切片
my_tuple = (0, 1, 2, 3, 4, 5, 6)
result2 = my_tuple[:]  #起始和结束不写表示从头到尾，步长为1可以省略
print(f"结果2{result2}")

# 对str进行切片
my_str = "01234567"
result3 = my_str[::2]
print(f"结果3为{result3}")

# 反向切片，等同于将序列反转了
my_str = "01234567"
result4 = my_str[::-1]
print(f"结果4为{result4}")

# 对列表切片，从3开始，到1结束，步长为-1
my_list = [0, 1, 2, 3, 4, 5, 6]
result5 = my_list[3:1:-1]
print(f"结果5为{result5}")

# 对元组进行切片，从头开始，到尾结束，步长为-2
my_tuple = (0, 1, 2, 3, 4, 5, 6)
result6 = my_tuple[::-2]
print(f"结果6为{result6}")