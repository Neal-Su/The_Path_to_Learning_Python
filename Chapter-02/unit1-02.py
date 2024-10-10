# 面向对象类中的成员方法定义和使用

# self关键字是成员方法定义的时候，必须填写的
# 它用来表示类对象自身的意思
# 在方法内部，想要访问类的成员变量，必须使用self

# 定义一个带有成员方法的类
class Student:
    name = None

    def say_hi(self):
        print(f"大家好，我是{self.name}，请大家多多关照")
        # 在方法内部，想要访问类的成员变量，必须使用self

    def say_hi2(self, msg):
        print(f"大家好，我是{self.name}，{msg}")
        # 访问外部传入的变量时候，直接用就行

stu = Student()
stu.name = "周杰伦"
stu.say_hi()  # self在调用时，可以当它不存在

stu2 = Student()
stu2.name = "林俊杰"
stu2.say_hi()