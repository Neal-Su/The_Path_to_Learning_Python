# 多态

# 同样的行为（函数），传入不同的对象，得到不同的状态

# 多态常作用于继承关系上
# 比如：
# 函数（方法）形参声明接受父类对象
# 实际传入父类的子类对象进行工作
# 即：
# 以父类做定义声明
# 以子类做实际工作
# 用以获得同一行为，不同状态

class Animal:  # 父类
    def speak(self):
        pass


class Dog(Animal):  # 子类
    def speak(self):
        print("汪汪汪")


class Cat(Animal):  # 子类
    def speak(self):
        print("喵喵喵")

def make_noise(animal:Animal):
    """制造点噪音，需要传入Animal对象"""
    animal.speak()


# 演示多态，构建两个子类对象来调用函数
dog = Dog()
cat = Cat()

make_noise(dog)
make_noise(cat)


# 多态也用于抽象类场景上

# 抽象类：含有抽象方法的类称作抽象类
# 抽象方法：方法体是空实现的(pass)称之为抽象方法

# 抽象类的作用:多用于做顶层设计(设计标准)，以便子类做具体实现
# 也是对子类的一种软性约束，要求子类必须复写(实现)父类的一些方法，并且配合多态去使用，获得不同的工作状态

# 演示抽象类
class AC:  # 抽象类
    def cool_wind(self):  # 抽象方法
        """制冷"""
        pass

    def hot_wind(self):  # 抽象方法
        """制热"""
        pass

    def swing_l_r(self):  # 抽象方法
        """左右摆风"""
        pass

class Midea_AC(AC):
    def cool_wind(self):
        print("美的空调制冷")

    def hot_wind(self):
        print("美的空调制热")

    def swing_l_r(self):
        print("美的空调左右摆风")

class Gree_AC(AC):
    def cool_wind(self):
        print("格力空调制冷")

    def hot_wind(self):
        print("格力空调制热")

    def swing_l_r(self):
        print("格力空调左右摆风")

def make_cool(ac: AC):
    ac.cool_wind()

midea_ac = Midea_AC()
gree_ac = Gree_AC()

make_cool(midea_ac)
make_cool(gree_ac)