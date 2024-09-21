# 文件的写入操作

# open函数在写入时，如果文件不存在，会给我们创建新的文件
f = open("E:/test2.txt", "w", encoding="UTF-8")
# 内容写到内存中
f.write("Hello,world!!!")
# flush刷新
# 将内存中积攒的内容，写入到硬盘的文件中
# f.flush()

f.close() # close方法内置了flush的功能

f = open("E:/test2.txt", "w", encoding="UTF-8")

f.write("大连海事大学")
# w模式，当文件已经存在的时候再写入，会将原来的内容全部清空

f.close()
