# 文件的追加操作
# a模式，文件不存在会创建文件，文件存在会在最后，追加写入文件

f = open("E:/test2.txt", "a", encoding="UTF-8")
f.write("信息学院")
f.write("\n计算机科学与技术") #想要换行写内容，内容前加\n
f.flush()
f.close()
