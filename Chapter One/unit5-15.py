# 序列的切片课后作业
str = "术技与学科机算计院学术技息信学大事海连大"
my_str = str[::-1][6:12:1]
print(f"倒序后结果为：{my_str}")

result = str.split("学")[2].replace("术","院学术")[::-1]
print(f"倒序后结果为：{result}")