# 自定义包

# 导入自定义包中的模块,并使用
import my_package.my_moudule1
import my_package.my_moudule2

my_package.my_moudule1.info_print1()
my_package.my_moudule2.info_print2()

print("——————————————————————————————")

# 另一种导入方式
from my_package import my_moudule1
from my_package import my_moudule2
my_moudule1.info_print1()
my_moudule2.info_print2()

print("——————————————————————————————")

# 又另一种导入方式
from my_package.my_moudule1 import info_print1
from my_package.my_moudule2 import info_print2
info_print1()
info_print2()

# 通过__all__变量，控制import *
# 自定义包中的main在__init__文件中，__all__变量要写在这个__init__文件中
from my_package import *
my_moudule1.info_print1()
# 只能使用my_moudule1，因为__all__变量中只有my_moudule1
