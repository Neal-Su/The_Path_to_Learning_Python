# 类的构造方法作业

class Student:

    def __init__(self, name, age, add):
        self.name = name  # 在构造方法内定义成员变量，需要使用self关键字
        self.age = age    # 这里三个是即对成员变量进行声明也进行赋值
        self.add = add
        print(f"学生{x}信息录入完成，信息为：【学生姓名：{self.name}，年龄：{self.age}，地址：{self.add}】")


for x in range(1, 11):
    print(f"当前录入第{x}位学生信息，总共需录入10位学生信息")
    stu = Student(input("请输入学生的姓名："), input("请输入学生的年龄："), input("请输入学生的地址："))