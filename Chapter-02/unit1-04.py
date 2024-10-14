# 演示类的构造方法__init__

# 构造方法的名称：__init__
# 构造方法也是类内置方法(魔术方法)
# 构造方法在构建类对象时候会自动执行
# 构建类对象的传参会传递给构造方法，借此特性可以给成员变量赋值（将参数自动传递给__init__方法使用）
class Student:

    def __init__(self, name, age, tel):
        self.name = name  # 在构造方法内定义成员变量，需要使用self关键字
        self.age = age    # 这里三个是即对成员变量进行声明也进行赋值
        self.tel = tel
        print("Student类创建了一个类对象")

stu  = Student("周杰伦", 31, 18812341234)
print(stu.name)
print(stu.age)
print(stu.tel)
