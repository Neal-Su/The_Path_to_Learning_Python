# 多进程基础

# 进程的创建步骤
# 1导入进程包：                   import multiprocessing
# 2通过进程类创建进程对象：         进程对象 = multiprocessing.Process()
# 3启动进程执行任务：              进程对象.start()

# 2通过进程类创建进程对象：         进程对象 = multiprocessing.Process(target=任务名)
# 参数名：
#       target  执行的目标任务名，这里指函数名(方法名)
#       name    进程名，一般不用设置
#       group   进程组，目前只能使用None

# 3进程创建与启动的代码：
# 创建子进程：
# sing_process = multiprocessing.Process(target=sing)
# dance_process = multiprocessing.Process(target=dance)
# 启动进程：
# sing_process.start()
# dance_process.start()
