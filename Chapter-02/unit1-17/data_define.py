# 数据分析案例，数据定义的类

"""
1.数据定义的类
"""

class Record:

    def __init__(self, data, order_id, money, province):
        self.data = data          # 订单日期
        self.order_id = order_id  # 订单ID
        self.money = money        # 订单金额
        self.province = province  # 订单省份

    def __str__(self):
        return f"{self.data}, {self.order_id}, {self.money}, {self.province}"