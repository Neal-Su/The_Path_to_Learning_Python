import random
num = random.randint(1,10)
guess_num = int(input("输入你要猜测的数字:"))
if guess_num == num:
    print("恭喜，第一次就猜中了")
else:
    if guess_num > num:
        print("你猜测的数字大了")
    else:
        print("你猜测的数字小了")
    guess_num = int(input("再次输入你要猜测的数字:"))
    if guess_num == num:
        print("恭喜，第二次猜中了")
    else:
        if guess_num > num:
            print("你猜测的数字大了")
        else:
            print("你猜测的数字小了")
        guess_num = int(input("再次输入你要猜测的数字:"))
        if guess_num == num:
            print("恭喜，第三次猜中了")
        else:
            print("三次机会用完了，没有猜中")
