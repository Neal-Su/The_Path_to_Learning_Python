# 字符串的操作课后作业

my_str = "itheima itcast boxuegu"
value1 = my_str.count("it")
print(f"字符串{my_str}中有：{value1}个it字符")
new_my_str = my_str.replace(" ","|")
print(f"字符串{my_str}，空格被替换后：{new_my_str}")
my_str_list = new_my_str.split("|")
print(f"字符串{new_my_str}，按照|分割后，得到：{my_str_list}")
