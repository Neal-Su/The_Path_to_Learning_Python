num = 200
def test_a():
    print(num)
def test_b():
    global num
    num = 500
    print(num)
test_a()
test_b()
print(num)
# golbal关键字在局部范围内修改全局变量

# 输出结果
200
500
500
