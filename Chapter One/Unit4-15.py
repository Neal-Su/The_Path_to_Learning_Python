money = 5000000
name = input("请输入您的姓名:")
def check(show):
    if show:
        print("————————————查询余额————————————")
    print(f"{name}您好，您的余额剩余：{money}元")
def infee(num):
    global money
    money += num
    print("————————————存款————————————")
    print(f"{name}您好，您存款{num}元成功")
    check(False)
def outfee(num):
    global money
    money -= num
    print("————————————取款————————————")
    print(f"{name}您好，您取款{num}元成功")
    check(False)
def menu():
    print("————————————主菜单————————————")
    print(f"{name}，您好，欢迎来到银行ATM，请选择操作：")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    return input("请输入您的选择：")
while True:
    keyboard_input = menu()
    if keyboard_input == "1":
        check(True)
        continue
    elif keyboard_input == "2":
        num = int(input("您想要存多少钱："))
        infee(num)
        continue
    elif keyboard_input == "3":
        num = int(input("您想要取多少钱："))
        outfee(num)
        continue
    else:
        print("退出ATM成功")
        break
# 函数综合案例