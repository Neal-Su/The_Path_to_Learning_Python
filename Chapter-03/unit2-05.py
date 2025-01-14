# 进程的注意点(进程结束顺序)
import multiprocessing
import time


# 1.主进程会等待所有的子进程执行结束再结束
def work():
    for i in range(10):
        print("工作中...")
        time.sleep(0.2)


if __name__ == '__main__':
    work_process = multiprocessing.Process(target=work)
    work_process.start()

    # 主进程睡眠一秒
    time.sleep(1)
    print("主进程执行完毕")


# 2.设置守护主进程(一旦主进程结束，所有子进程立即都销毁，不再执行子进程中的代码)

def work():
    for i in range(10):
        print("工作中...")
        time.sleep(0.2)


if __name__ == '__main__':
    work_process = multiprocessing.Process(target=work)
    work_process.daemon = True
    work_process.start()

    # 主进程睡眠一秒
    time.sleep(1)
    print("主进程执行完毕")

