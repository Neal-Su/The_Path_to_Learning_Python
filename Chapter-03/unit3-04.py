# 线程的注意点(线程结束顺序)

# 1.主线程会等待所有的子线程执行结束再结束

import threading
import time

def work():
    for i in range(10):
        print("工作中...")
        time.sleep(0.2)


if __name__ == '__main__':
    work_thread = threading.Thread(target=work)
    work_thread.start()

    # 主线程睡眠一秒
    time.sleep(1)
    print("主线程执行完毕")

# 2.设置守护主线程(一旦主线程结束，所有子线程立即都销毁，不再执行子线程中的代码)


def work():
    for i in range(10):
        print("工作中...")
        time.sleep(0.2)


if __name__ == '__main__':
    work_thread = threading.Thread(target=work)
    work_thread.daemon = True
    work_thread.start()

    # 主线程睡眠一秒
    time.sleep(1)
    print("主线程执行完毕")


