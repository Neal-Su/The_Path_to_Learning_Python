# 面向对象编程的思想

# 设计一个闹钟(类)
class Clock:
    id = None     # 序列号
    price = None  # 零售价格

    def ring(self):
        import winsound
        winsound.Beep(2000, 3000)

# 构建两个闹钟对象并让其工作


clock1 = Clock()
clock1.id = "hahaha"
clock1.price = 8.88
print(f"闹钟ID：{clock1.id}，价格：{clock1.price}")
clock1.ring()

clock2 = Clock()
clock2.id = "lalala"
clock2.price = 6.66
print(f"闹钟ID：{clock2.id}，价格：{clock2.price}")
clock2.ring()