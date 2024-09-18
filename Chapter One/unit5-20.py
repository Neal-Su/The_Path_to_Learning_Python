# 字典的常用操作

worker_dict = \
    {
        "王力宏": {"部门": "科技部", "工资": 3000, "级别": 1},
        "周杰伦": {"部门": "市场部", "工资": 5000, "级别": 2},
        "林俊杰": {"部门": "市场部", "工资": 7000, "级别": 3},
        "张学友": {"部门": "科技部", "工资": 4000, "级别": 1},
        "刘德华": {"部门": "市场部", "工资": 6000, "级别": 2}
    }
print(f"全体员工当前信息如下：{worker_dict}")

for name in worker_dict:
    print(f"字典的key是：{name}")
    if worker_dict[name]["级别"] == 1:
        # # 方法一
        # # 获取到员工信息字典
        # information_worker_dict = worker_dict[name]
        # print(f"字典的key是：{information_worker_dict}")
        # information_worker_dict["工资"] += 1000
        # information_worker_dict["级别"] += 1
        # # 将员工信息更新回worker_dict
        # worker_dict[name] = information_worker_dict

        # # 方法二
        worker_dict[name]["级别"] += 1
        worker_dict[name]["工资"] += 1000

print(f"全体级别为1的员工完成升职加薪后，信息如下：{worker_dict}")
