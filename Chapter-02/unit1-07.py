# 封装思想，私有成员变量及方法

# 定义一个类，内含私有成员变量和私有成员方法
# 私有成员变量及方法都是以__开头

class Phone:

    __current_voltage = 0.5  # 当前手机运行电压

    def __keep_single_core(self):
        print("让CPU以单核模式运行")

    def call_by_5g(self):
        if self.__current_voltage >= 1:
            print("5G通话已开启")
        else:
            self.__keep_single_core()
            print("电量不足，无法使用5G通话，并已设置为单核运行进行省电")
    # 私有成员方法及变量都无法直接使用（类对象是没有办法访问私有成员的）
    # 但可以在自己的类里面其他成员可以使用自己的私有成员方法及私有成员变量


phone = Phone()
phone.call_by_5g()
