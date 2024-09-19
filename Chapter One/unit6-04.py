# lambda匿名函数
# 函数定义中，def定义有名称的函数，lambda可以定义匿名函数
# 有名称的函数可以基于名称重复使用，无名称的匿名函数只可临时使用一次
# lambda匿名函数的函数体只能写一行代码

def test_func(compute):
    result = compute(1, 2)
    print(f"compute参数的类型是：{type(compute)})")
    print(f"计算结果是：{result}")

test_func(lambda x, y: x + y)