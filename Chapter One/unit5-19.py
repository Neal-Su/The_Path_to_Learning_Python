# 字典的常用操作

jiafen_dict = \
    {
        "论文加分": {"A级论文": 60, "B级论文": 40, "C级论文": 20, },
        "竞赛加分": {"国创赛金奖": 80, "国创赛银奖": 60, "A类国一": 40, "A类国二": 20, }
    }
# 新增元素
jiafen_dict["论文加分"]["D级论文"] = 0
print(f"字典经过新增元素后的结果：{jiafen_dict}")
# 更新元素
jiafen_dict["竞赛加分"]["国创赛金奖"] = 100
print(f"字典经过更新元素后的结果：{jiafen_dict}")
# 新增元素和更新元素的语法是一样的，只取决于这个key存不存在

# 删除元素
score = jiafen_dict.pop("论文加分")
print(f"字典中被移除了一个元素，结果是：{jiafen_dict}，论文的加分是：{score}")

# 清空元素
jiafen_dict.clear()
print(f"字典被清空了，结果是：{jiafen_dict}")

# 获取全部的key
jiafen_dict = \
    {
        "论文加分": {"A级论文": 60, "B级论文": 40, "C级论文": 20, },
        "竞赛加分": {"国创赛金奖": 80, "国创赛银奖": 60, "A类国一": 40, "A类国二": 20, }
    }
all_keys = jiafen_dict.keys()
print(f"字典的全部keys，是：{all_keys}")

# 遍历字典
# 方式1，通过获取到全部的key来完成遍历
for key in all_keys:
    print(f"字典的key是：{key}")
    print(f"字典的value是：{jiafen_dict[key]}")
# 方式2，直接对字典进行for循环，每一次循环都是直接得到key
for key in jiafen_dict:
    print(f"方法二字典的key是：{key}")
# 字典不支持下标索引，所以不可以用while循环

# 统计字典的元素数量
num = len(jiafen_dict)
print(f"字典的元素数量有：{num}个")

