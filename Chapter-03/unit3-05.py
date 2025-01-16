# 线程的执行顺序是无序
import threading
import time

# 获取当前的线程信息
# 通过current_thread方法获取线程对象
#         current_thread = threading.current_thread()
# 通过current_thread对象可以知道线程的相关信息，例如被创建的顺序
#         print(current_thread)


def task():
    time.sleep(1.5)
    # current_thread:获取当前线程的线程对象
    thread = threading.current_thread()
    print(thread)


if __name__ == '__main__':
    for i in range(5):
        sub_thread = threading.Thread(target=task)
        sub_thread.start()