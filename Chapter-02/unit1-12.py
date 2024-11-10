# 变量的类型注解
import json
import random

# 基础数据类型注解
var_1: int = 10
var_2: str = "DMU"
var_3: bool = True
var_4: float = 3.1415
# 类对象类型注解


class Student:
    pass


stu: Student = Student()

# 基础容器类型注解
my_list: list = [1, 2, 3]
my_tuple: tuple = (1, 2, 3)
my_set: set = {1, 2, 3}
my_dict: dict = {"大连海事大学": 2220222587}
my_str: str = "信息技术学院"
# 容器类型详细注解
my_list: list[int] = [1, 2, 3]
my_tuple: tuple[int, str, bool] = (1, "DMU", True)
my_set: set[int] = {1, 2, 3}
my_dict: dict[str, int] = {"大连海事大学": 2220222587}

# 在注释中进行类型注解，语法：# type：类型
var_1 = random.randint(1,10)  # type: int
var_2 = json.loads('{"name": "zhangsan"}')  # type: dict[str, str]


def func():
    return 10


var_3 = func()  # type: int

# 类型注解仅仅只是个备注，不会影响到程序的运行，标记错了也无所谓，如下
var_4: int = "DMU"
