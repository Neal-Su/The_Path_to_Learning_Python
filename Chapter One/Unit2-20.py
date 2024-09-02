for i in range(1,3):
    print("语句一")
    for j in range(1,3):
        print("语句二")
        continue
        print("语句三")
    print("语句四")
# 遇到continue这次循环结束，如果这个循环还有次数没完成，则继续进行该循环的剩余次数，
# 只作用于当前循环，对上层循环无效
# continue改变循环