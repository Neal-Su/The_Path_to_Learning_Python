# 文件的读取课后作业
num = 0
with open("E:/word.txt", "r", encoding="UTF-8") as f:
    for line in f:
        line_list = line.split(" ")
        print(f"{line_list}")
        count = line_list.count("itheima")
        num += count
        count1 = line_list.count("itheima\n")
        print(f"{count1}")
        num += count1
print(f"该文本中itheima出现的次数是：{num}次")


# itheima itcast python
# itheima python itcast
# beijing shanghai itheima
# shenzhen guangzhou itheima
# wuhan hangzhou itheima
# zhengzhou bigdata itheima