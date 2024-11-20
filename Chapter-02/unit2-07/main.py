# 数据分析案例，主文件

# 面向对象，数据分析案例，主业务逻辑代码
"""
1.设计一个类，可以完成数据的封装
2.设计一个抽象类，定义文件读取的相关功能，并使用子类实现具体功能
3.读取文件，生产数据对象
4.进行数据需求的逻辑计算（计算每一天的销售额）
5.通过PyEcharts金星图形绘制
"""

from file_define import TextFileReader, JsonFileReader
from data_define import Record
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType

text_file_reader = TextFileReader("E:/B python wenjian/2011年1月销售数据.txt")
json_file_reader = JsonFileReader("E:/B python wenjian/2011年2月销售数据JSON.txt")

jan_data: list[Record] = text_file_reader.read_data()
feb_data: list[Record] = json_file_reader.read_data()

# 将2个月份的数据合并为一个list来存储
all_data: list[Record] = jan_data + feb_data

# 开始数据计算
data_dict = {}
for record in all_data:
    if record.data in data_dict.keys():
        # 当前日期已经有记录了，所以和老记录做累加即可
        data_dict[record.data] += record.money
    else:
        data_dict[record.data] = record.money

print(data_dict)

# 可视化开发
bar = Bar(init_opts=InitOpts(theme=ThemeType.PURPLE_PASSION))  # 设置主题

bar.add_xaxis(list(data_dict.keys()))  # 添加x轴的数据
bar.add_yaxis("销售额", list(data_dict.values()), label_opts=LabelOpts(is_show=False))  # 添加y轴的数据,并且不显示数字
bar.set_global_opts(
    title_opts=TitleOpts(title="每日销售额")
)
bar.render("每日销售额柱状图.html")