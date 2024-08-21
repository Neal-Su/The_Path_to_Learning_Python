num = 4
if int(input("请输入第一次猜想的数字（1-5）：")) == num:
    print(f"第一次就猜对了，就是{num}")
elif int(input("不对，再猜一次：")) == num:
    print(f"猜对了就是{num}")
elif int(input("不对，再猜最后一次：")) == num:
    print(f"最后一次机会你猜对了，就是{num}")
else:
    print(f"Sorry,全部猜错啦，我想的是：{num}")

