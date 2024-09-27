# 异常-模块-包-综合案例

# 导入包内的两个模块
from my_utils import file_util
from my_utils import str_util

my_str = "大连海事大学信息学院计算机科学与技术"
str_util.str_reverse(my_str)
str_util.substr(my_str, 6, 10)

file = "E:/test.txt"
append_str = "信息学院"
file_util.print_file_info(file)
file_util.append_to_file(file, append_str)
file_util.print_file_info(file)
