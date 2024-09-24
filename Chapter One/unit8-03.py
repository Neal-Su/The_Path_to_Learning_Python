# 自定义模块并导入

# 导入的自定义模块文件的名字一定要符合命名规则

# 导入的自定义模块内容
# my_module:
# def test(a,b):
#     print(a + b)
# my_module2:
# def test(a,b):
#     print(a * b)

import my_module
my_module.test(2, 3)

# 导入不同模块的同名功能,后用覆盖前面调用的
from my_module import test
from my_module2 import test
test(2, 3)

# __main__变量提供的功能

# my_module:
# def test(a,b):
#     print(a + b)
# test(1, 2)
# 当导入的该模块在那个模块的窗口这样执行没问题，但是如果将该模块导入到其他程序中
# 如from my_module import test这样导入时，导入时就会执行一遍这个test(1, 2)
# 这显然不是我想要的，所以
# my_module:
# def test(a,b):
#     print(a + b)
# if __name__ == "__main__": (__name__是一个内置变量)
#   test(1, 2)
# 这样就只会在那个模块的窗口执行，导入该模块到其他程序时候就不会执行，因为只有这时候就不是main里面了
# if条件就为假了

# __all__变量提供的功能

# my_module:
# def test_a(a,b):
#     print(a + b)
# def test_b(a,b):
#     print(a * b)
# from my_module import *  如果这样导入到一个程序中
# my_module里面的两个函数，这个程序都能用
# 但如果模块中带有__all__变量
# my_module:
# __all__ = ["test_a"]
# def test_a(a,b):
#     print(a + b)
# def test_b(a,b):
#     print(a * b)
# 再将这个模块*模式导入到一个函数中，那这个函数中就不能用test_b了
# 但是from my_module import test_b这样再次导入，就还能用test_b
# 因为__all__是对*生效