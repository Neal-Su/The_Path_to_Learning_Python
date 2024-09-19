# 函数作为参数传递
# 函数的传入，传入的是代码的执行逻辑

def test_func(compute):
    result = compute(1, 2)
    print(f"compute参数的类型是：{type(compute)})")
    print(f"计算结果是：{result}")

def compute(x, y):
    return x + y

test_func(compute)