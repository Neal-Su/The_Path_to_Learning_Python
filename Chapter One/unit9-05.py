# 基础地图的使用
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts
# 准备地图对象
map = Map()

# 准备数据
data = [
    ("北京市", 99),
    ("上海市", 199),
    ("湖南省", 299),
    ("台湾省", 399),
    ("广东省", 499)
]
# 添加数据
map.add("测试地图", data, "china")

# 设置全局变量
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,  # 开启手动校准范围
        pieces=[
            {"min": 1, "max": 9, "label": "1-9人", "color": "#CCFFFF"},
            {"min": 10, "max": 99, "label": "10-99人", "color": "#FF6666"},
            {"min": 100, "max": 500, "label": "100-500人", "color": "#990033"},
            # 颜色代码在ab.173网站前端选项里的rgb颜色对照表能查到
        ]
    )
)

# 绘图
map.render()
