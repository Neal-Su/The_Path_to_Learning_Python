for i in range(1,3):
    print("语句一")
    break
    print("语句二")
print("语句三")
# 遇到break这个循环整体结束，只作用于当前循环，对上层循环无效
# break中断循环

# 输出结果
语句一
语句三
