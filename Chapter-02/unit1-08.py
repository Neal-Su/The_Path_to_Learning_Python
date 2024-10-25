# 封装课后作业

# 设计一个类，用来描述手机
class Phone:

    # 设计私有成员变量：__is_5g_enable
    __is_5g_enable = False  # True表示开启5g，False表示关闭5g

    # 设计私有成员方法：__check_5g
    def __check_5g(self):

        if self.__is_5g_enable == 1:
            print("5g开启")
        else:
            print("5g关闭，正在使用4g")

    # 设计公开成员方法：call_by_5g
    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")


phone = Phone()
phone.call_by_5g()
