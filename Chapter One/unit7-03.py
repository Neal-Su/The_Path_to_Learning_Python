# 文件的读取课后作业
with (open("E:/word.txt", "r", encoding="UTF-8") as f):
    content = f.read()
    print(f"{content}")
    count = content.count("itheima")
print(f"该文本中itheima出现的次数是：{count}次")

num = 0
with open("E:/word.txt", "r", encoding="UTF-8") as f:
    for line in f:
        line = line.strip()  #去除开头和结尾的空格和换行符
        line_list = line.split(" ")
        print(f"{line_list}")
        count = line_list.count("itheima")
        num += count
print(f"该文本中itheima出现的次数是：{num}次")
