
def print_file_info(file_name):
    """
    接受传入文件的路径，打印文件的全部内容，如文件不存在则捕获异常
    输出提示信息，通过finally关闭文件对象
    :param file_name:传入文件的路径
    :return:无返回值
    """
    f = None
    try:
        f = open(file_name, "r", encoding="UTF-8")  # r模式找不到文件会报错
        lines = f.readlines()
        print(f"文件的内容是：{lines}")
    except Exception as e:
        print(f"出现异常了，因为文件不存在,原因是{e}")
    else:
        print("没有异常")
    # finally表示无论是否异常都要执行的代码，例如关闭文件
    finally:
        if f:
            f.close()
    # 如果文件不存在没有打开，直接close会报错，所以在前面先赋值None，再在close前判断一下
    # 如果没有打开文件，f依旧是None，则close不会执行，也就不会报错了
def append_to_file(file_name, data):
    """
    接受文件路径以及传入数据，将数据追加写入到文件中
    :param file_name:文件路径
    :param data:追加数据
    :return:
    """
    f = open(file_name, "a", encoding="UTF-8")
    f.write(data)
    f.flush()
    f.close()
    print("追加完成")