# 列表的循环遍历

# while循环和for循环，都是循环语句，但细节不同：
# ·在循环控制上：
# ·while循环可以自定循环条件，并自行控制
# ·for循环不可以自定循环条件，只可以一个个从容器内取出数据
# ·在无限循环上：
# ·while循环可以通过条件控制做到无限循环
# ·for循环理论上不可以，因为被遍历的容器容量不是无限的
# ·在使用场景上：
# ·while循环适用于任何想要循环的场景
# ·for循环适用于，遍历数据容器的场景或简单的固定次数循环场景
def list_while_func():
    """
    使用while循环遍历列表的演示函数
    :return:
    """
    my_list = ["大连海事","信息学院","计算机科学与技术","双学位"]
    index = 0
    while index < len(my_list):
        element = my_list[index]
        print(f"列表的元素：{element}")
        index += 1

def list_for_func():
    """
    使用for循环遍历列表的演示函数
    :return:
    """
    my_list = [1, 2, 3, 4, 5]
    for element in my_list:
        print(f"列表的元素有：{element}")

list_while_func()
list_for_func()