# 文件操作的综合案例
f = open("E:/bill.txt", "r", encoding="UTF-8")
g = open("E:/bill2.txt.", "w", encoding="UTF-8")
for line in f:
    line = line.strip()
    line_list = line.split("，")
    count = line_list.count("正式")
    if count == 1:
        g.write(f"{line}\n")
f.close()
g.close()

# 周杰轮，2022—01—01，100000，消费，正式
# 周杰轮，2022—01—02，300000，收入，正式
# 周杰轮，2022—01—03，100000，消费，测试
# 林俊节，2022—01—01，300000，收入，正式
# 林俊节，2022—01—02，100000，消费，测试
# 林俊节，2022—01—03，100000，消费，正式
# 林俊节，2022—01—04，100000，消费，测试
# 林俊节，2022—01—05，500000，收入，正式
# 张学油，2022—01—01，100000，消费，正式
# 张学油，2022—01—02，500000，收入，正式
# 张学油，2022—01—03，900000，收入，测试
# 王力鸿，2022—01—01，500000，消费，正式
# 王力鸿，2022—01—02，300000，消费，测试
# 王力鸿，2022—01—03，950000，收入，正式
# 刘德滑，2022—01—01，300000，消费，测试
# 刘德滑，2022—01—02，100000，消费，正式
# 刘德滑，2022—01—03，300000，消费，正式