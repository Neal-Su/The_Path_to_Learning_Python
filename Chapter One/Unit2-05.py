print("欢迎来到黑马动物园")
if int(input("请输入您的身高（cm）：")) < 120:
    print("身高小于120cm，可以免费")
elif int(input("请输入您的vip等级（1-5）：")) > 3:
    print("您是高级VIP，可以免费")
elif int(input("今天几号？")) == 1:
    print("今天是一号免费日，可以免费")
else:
    print("条件都不满足，需要买票10元")
print("祝您游玩愉快。")