def str_reverse(s):
    """
    接受传入字符串，将字符串反转返回
    :param s:传入的字符串
    :return:无返回值
    """
    result = s[::-1]
    print(f"字符串反转后的结果为：{result}")
def substr(s, x, y):
    """
    按照下标x和y对字符串进行切片
    :param s:传入的字符串
    :param x:前下标
    :param y:后下标
    :return:返回切片后的结果
    """
    result = s[x:y:1]
    print(f"切片后的结果为：{result}")
    return result