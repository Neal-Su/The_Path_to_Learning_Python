# 线程执行带有参数的任务

# 给我们指定的任务去传递参数
#      参数名：args     以元组的方式给执行任务传参
#      参数名：kwargs   以字典的方式给执行任务传参

# 以元组的方式给函数传参
# 这时候args里面的第一个参数就是函数中的第一个形参，也就是传参顺序要一致，元组必须要加逗号才是元组
# sing_thread = threading.Thread(target=sing, args=(3,))

# 以字典的方式给函数传参
# kwargs字典里的key必须与参数的名字一样
# dance_thread = threading.Thread(target=dance, kwargs={"num": 3})

import time
import threading

# 唱歌
def sing(num, name):
    for i in range(num):
        print(name)
        print("唱歌")
        time.sleep(0.5)


# 跳舞
def dance(count):
    for i in range(count):
        print("跳舞")
        time.sleep(0.5)


if __name__ == '__main__':
    # args:以元组的方式给函数传参
    # kwargs:以字典的方式给函数传参
    sing_thread = threading.Thread(target=sing, args=(3, "小明"))
    dance_thread = threading.Thread(target=dance, kwargs={"count": 1})

    sing_thread.start()
    dance_thread.start()