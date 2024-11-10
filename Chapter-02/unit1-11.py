# 复写父类成员和调用父类成员

# 复写：子类继承父类的成员属性和成员方法，如果对其不满意，那么可以进行复写
# 即：在子类中重新定义同名的属性或方法即可

class Phone:
    IMEI = 2220222587      # 序列号
    producer = "THU"       # 厂商

    def call_by_5g(self):
        print("5g通话")

# 定义子类，复写父类成员
class MyPhone(Phone):
    producer = "DMU"  # 复写父类的成员属性

    def call_by_5g(self):
        print("开启单核模式，确保通话的时候省电")
        # 在子类中调用父类成员变量和成员方法
        # 方式一
        print(f"父类的厂商是：{Phone.producer}")
        Phone.call_by_5g(self)
        # 方式二
        print(f"父类的序列号是：{super().IMEI}")
        super().call_by_5g()

        print("关闭单核模式")

phone = MyPhone()
phone.call_by_5g()
print(phone.producer)

