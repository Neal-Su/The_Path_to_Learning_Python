# 多线程基础

# 线程的创建步骤
# 1导入线程包：                   import threading
# 2通过线程类创建进程对象：         线程对象 = threading.Thread(target=任务名)
# 3启动线程执行任务：              进程对象.start()

# 参数名：
#       target  执行的目标任务名，这里指函数名(方法名)
#       name    线程名，一般不用设置
#       group   线程组，目前只能使用None

# 3线程创建与启动的代码：
# 创建子线程：
# sing_thread = threading.Thread(target=sing)
# dance_thread = threading.Thread(target=dance)
# 启动线程：
# sing_thread.start()
# dance_thread.start()
