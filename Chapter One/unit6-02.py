# 函数的多种参数使用形式
def user_info(name, age, gender):
    print(f"姓名是：{name}, 年龄是：{age}, 性别是：{gender}")

# 位置参数
user_info ("小明", 20, "男")

# 关键字参数
# 关键字传入参数可以乱序
# 关键字传参可以与位置传参混用
user_info(name="小王", age=18, gender="女")
user_info(age=19, gender="女", name="小清")
user_info("小紫", gender="女", age=19)

# 缺省参数(默认值)
# 如果设置默认参数必须在参数最后
def user_info(name, age, gender="男"):
    print(f"姓名是：{name}, 年龄是：{age}, 性别是：{gender}")
user_info("小天", 13)
# 默认参数也可以被覆盖
user_info("小安", 13, "女")

# 不定长参数
# 位置传递的不定长，*号
# 不定长定义的形式参数会作为元组存在，接受不定长数量的参数传入
def user_info(*args):
    print(f"args参数的类型是：{type(args)},内容是：{args}")
user_info(1, 2, 3, "男孩", "小明")

# 关键字不定长，**
def user_info(**kwargs):
    print(f"kwargs参数的类型是：{type(kwargs)},内容是：{kwargs}")
user_info(gender = "男孩", name = "小明", addr = "上海")
