# python模块的概念与导入

# 模块的导入语法
# [from 模块名] import [模块 | 类 | 变量 | * ] [as 别名]

# 常用的组合形式：
# import 模块名
# from 模块名 import 类，变量，方法等
# from 模块名 import *
# import 模块名 as 别名
# from 模块名 import 功能名 as 别名

# 导入python内置的time模块 (time.py这个文件)
import time
print("你好")
time.sleep(2)  # 通过.就可以使用模块内部的全部功能(类，变量，函数等)
print("我好")

# 导入某个模块中的一个方法
# 导入time模块中的sleep方法
from time import sleep
print("你好")
sleep(2)  # 通过.就可以使用模块内部的全部功能(类，变量，函数等)
print("我好")

# 使用*导入time全部功能
from time import *
print("你好")
sleep(2)
print("我好")

# as定义别名
# 模块定义别名
# import 模块名 as 别名
# 功能定义别名
# from 模块名 import 功能 as 别名
import time as tt
print("1")
tt.sleep(2)
print("2")

from time import sleep as sl
print("3")
sl(2)
print("4")
