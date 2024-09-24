# 异常的捕获

# 基本的捕获语法 (捕获所有异常)
try:
    f = open("E:/abc.txt", "r", encoding="UTF-8")  # r模式找不到文件会报错
except:
    print("出现异常了，因为文件不存在，我将open的模式，改为w模式打开")
    f = open("E:/abc.txt", "w", encoding="UTF-8")

# 捕获指定的异常
try:
    print(name)
except NameError as e:
    print("出现了变量未定义的异常")

# 捕获多个异常，和异常else
try:
    1 / 0
except (NameError,ZeroDivisionError) as e:
    print("出现了变量未定义 或 除以0 的异常")

# 另一种捕获所有异常
try:
    f = open("E:/abc.txt", "r", encoding="UTF-8")  # r模式找不到文件会报错
except Exception as e:
    print("出现了异常")
else:
    print("没有异常")
# finally表示无论是否异常都要执行的代码，例如关闭文件
finally:
    f.close()