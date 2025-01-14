# 使用多进程实现多任务

# 1导入进程包

import time
import multiprocessing


# 唱歌
def sing():
    for i in range(3):
        print("唱歌")
        time.sleep(0.5)


# 跳舞
def dance():
    for i in range(3):
        print("跳舞")
        time.sleep(0.5)


if __name__ == '__main__':
    # 2使用进程类创建进程对象
    # target：需要指定进程执行的函数名
    sing_process = multiprocessing.Process(target=sing)
    dance_process = multiprocessing.Process(target=dance)

    # 3使用进程对象启动进程执行指定任务
    sing_process.start()
    dance_process.start()
