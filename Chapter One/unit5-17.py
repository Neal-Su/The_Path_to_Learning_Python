# 集合的课后练习

my_list = ["大连海事","信息学院","计算机科学技术","人工智能","信息学院","人工智能","计算机科学技术"]
my_set = set()
for element in my_list:
    print(f"该列表的元素有：{element}")
    my_set.add(element)
print(f"存入集合后结果：{my_set}")