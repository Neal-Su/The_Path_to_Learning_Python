# 字典的定义

# 定义字典字面量
# {key: value, key: value, ......， key: value}
# 定义字典变量
# my_dict = {key: value, key: value, ...... key: value}
# 定义空字典
# my_dict = {}   # 空字典定义方式1
# my_dict = dict()  # 空字典定义方式2

# 定义字典
my_dict = {"A级论文": 60, "B级论文": 40, "C级论文": 20, }
# 定义空字典
my_dict2 = {}
my_dict3 = dict()
print(f"字典1的内容是：{my_dict}，类型是：{type(my_dict)}")
print(f"字典1的内容是：{my_dict2}，类型是：{type(my_dict2)}")
print(f"字典1的内容是：{my_dict3}，类型是：{type(my_dict3)}")

# 字典不允许key的重复
my_dict = {"A级论文": 60, "A级论文": 40, "C级论文": 20}
print(f"重复key字典的内容是：{my_dict}")

# 从字典中基于key值获取value
# 字典同集合一样。不可以使用下标索引
# 但是字典可以通过key值来找到对应的value
my_dict = {"A级论文": 60, "B级论文": 40, "C级论文": 20}
value = my_dict["C级论文"]
print(f"一篇C级论文可以加；{value}能力分")

# 字典得嵌套
# 字典的key和value可以是任意数据类型（key不可为字典）
jiafen_dict = \
    {
        "论文加分": {"A级论文": 60, "B级论文": 40, "C级论文": 20, },
        "竞赛加分": {"国创赛金奖": 80, "国创赛银奖": 60, "A类国一": 40, "A类国二": 20, }
    }
print(f"能力分加分规则是：{jiafen_dict}")

# 从嵌套字典中获取数据
value = jiafen_dict["竞赛加分"]["A类国二"]
print(f"A类国二能加：{value}能力分")