# 常见的类内置方法(魔术方法)


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 字符串方法__str__
    # 控制类转换为字符串
    def __str__(self):
        return f"Student类对象，name：{self.name}, age:{self.age}"

    # __lt__魔术方法
    # 类对象比较大小，只能用于<和>
    def __lt__(self, other):
        return self.age < other.age

    # __le__魔术方法
    # 类对象比较大小，能用于<=和>=
    def __le__(self, other):
        return self.age <= other.age

    # __eq__魔术方法
    # 类对象比较运算符，能用于==，不使用__eq__魔术方法直接==比较，默认比较的是内存地址
    def __eq__(self, other):
        return self.age == other.age

stu = Student("周杰伦", 31)
print(stu)       # 这两个位置直接输出的都会是内存地址,但提供__str__魔术方法之后就可以由我们自己决定输出什么
print(str(stu))  # 这两个位置直接输出的都会是内存地址,但提供__str__魔术方法之后就可以由我们自己决定输出什么


stu1 = Student("周杰伦", 31)
stu2 = Student("林俊杰", 36)
print(stu1 < stu2)
print(stu1 > stu2)

stu1 = Student("周杰伦", 36)
stu2 = Student("林俊杰", 36)
print(stu1 <= stu2)
print(stu1 >= stu2)

print(stu1 == stu2)
