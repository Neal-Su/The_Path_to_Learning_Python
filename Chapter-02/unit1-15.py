# Union联合类型注解

# Union联合类型注解，在变量注解，函数（方法）形参，返回值，的注解中均可使用
# 使用Union类型必须先导包
from typing import Union

my_list: list[Union[int, str]] = [1, 2, "THU", "DMU"]
# 表示这个list里面存放的元素是int和str类型二选一
my_dict: dict[str, Union[str, int]] = {"THU": "深圳", "DMU": 2220222587}
# 表示value有可能是字符串也有可能是int


# 对函数的形参和返回值进行联合类型注解
def func(data: Union[int, str]) -> Union[int, str]:
    pass
