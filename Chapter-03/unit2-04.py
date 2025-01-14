# 获取进程编号

import os
# 获取当前进程编号:
#               os.getpid()
# 获取当前父进程编号:
#               os.getppid()

import time
import multiprocessing

def sing(num, name):
    print("唱歌进程的pid：", os.getpid())
    print("唱歌进程父进程的pid：", os.getppid())
    for i in range(num):
        print(name)
        print("唱歌")
        time.sleep(0.5)

def dance(num, name):
    print("跳舞进程的pid：", os.getpid())
    print("跳舞进程父进程的pid：", os.getppid())
    for i in range(num):
        print(name)
        print("跳舞")
        time.sleep(0.5)


# 主进程(唱歌跳舞进程的父进程)
if __name__ == '__main__':
    print("主进程的pid：", os.getpid())
    # 创建子进程对象并指定执行的任务名
    sing_process = multiprocessing.Process(target=sing, args=(3, "小明"))
    dance_process = multiprocessing.Process(target=dance, kwargs={"name": "小红", "num": 2})
    # 启动子进程并执行任务
    sing_process.start()
    dance_process.start()