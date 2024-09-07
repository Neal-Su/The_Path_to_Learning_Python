name = input("请输入您的用户名：")
money = 5000000
opt = None
num = None
flag = 1
def check():
    print("————————————查询余额————————————")
    print(f"{name}您好，您的余额剩余：{money}元")
def infee(num):
    print("————————————存款————————————")
    print(f"{name}您好，您存款{num}元成功")
    print(f"{name}您好，您的余额剩余：{money}元")
def outfee(num):
    print("————————————取款————————————")
    print(f"{name}您好，您取款{num}元成功")
    print(f"{name}您好，您的余额剩余：{money}元")
def menu():
    print("————————————主菜单————————————")
    print(f"{name}，您好，欢迎来到银行ATM，请选择操作：")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    global opt
    opt = input("请输入您的选择：")
while flag:
    menu()
    if opt == "1":
        check()
    elif opt == "2":
        num = int(input("请输入您的存款金额："))
        money += num
        infee(num)
    elif opt == "3":
        num = int(input("请输入您的取款金额："))
        money -= num
        outfee(num)
    else:
        print("退出ATM成功")
        flag = 0
# 函数综合案例







