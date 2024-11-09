# 继承的基础语法

# 继承分为单继承和多继承
# 继承表示：将从父类那里继承（复制）来成员变量和成员方法（不含私有）

# 演示单继承
class Phone:
    IMEI = None      # 序列号
    producer = "THU"  # 厂商

    def call_by_4g(self):
        print("4g通话")


class Phone2022(Phone):
    face_id = "10001"  # 面部识别id

    def call_by_5g(self):
        print("2022新功能，5g通话")


phone = Phone2022()
print(phone.producer)
phone.call_by_4g()
phone.call_by_5g()  # 因为Phone2022成功继承了Phone的方法和变量，所以代码才能成功

# 演示多继承


class NFCReader:
    nfc_type = "第五代"
    producer = "DMU"

    def read_card(self):
        print("NFC读卡")

    def write_card(self):
        print("NFC写卡")


class RemoteControl:
    rc_type = "红外遥控"

    def control(self):
        print("红外遥控开启了")


class MyPhone(Phone, NFCReader, RemoteControl):
    pass
    #  pass关键字，当这个类不需要写新的东西的时候
    #  为了语法不报错，使用pass关键字，表示这里是空的


phone = MyPhone()
phone.call_by_4g()
phone.read_card()
phone.write_card()
phone.control()

# 同名成员属性/成员方法，调用时，先继承的优先（左边的优先，这里是Phone优先于NFCReader）
print(phone.producer)