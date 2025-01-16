# 使用多线程实现多任务

import time
import threading

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
    sing_thread = threading.Thread(target=sing)
    dance_thread = threading.Thread(target=dance)

    sing_thread.start()
    dance_thread.start()