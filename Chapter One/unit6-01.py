# 函数的多返回值

def test_return():
    return 1, "hello", True
x, y, z =test_return()
print(x)
print(y)
print(z)