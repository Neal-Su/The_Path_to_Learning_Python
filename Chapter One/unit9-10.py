# 动态GDP柱状图绘制

from pyecharts.charts import Bar, Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType

# 读取数据
f = open("E:/B python wenjian/1960-2019全球GDP数据.csv", "r", encoding="GB2312")
data_lines = f.readlines()
# 关闭文件
f.close()
# 删除第一条数据
data_lines.pop(0)
# 将数据转换为字典储存，格式为：
# { 年份: [[国家, gdp], [国家, gdp], .......], 年份: [[国家, gdp], [国家, gdp], .......], ...... }
# 先定义一个字典对象
data_dict = {}
for line in data_lines:
    year = int(line.split(",")[0])
    country = line.split(",")[1]
    gdp = float(line.split(",")[2])  # gdp数据，float将原始数据中的特殊的科学计数法也转换成了数字
# 如何判断一个字典里面有没有指定的key呢？
    try:
        data_dict[year].append([country, gdp])
        # 尝试在指定的key(这里是年份如：1960)后面value[]里面追加一个[country, gdp]
        # 如果这个key(这里是年份如：1960)不存在，则会报KeyError错误
    except KeyError:
        data_dict[year] = []
        # 因为key(这里是年份如：1960)不存在报错了，所以添加一个key(这里是年份如：1960)，他的value是一个空的[]
        data_dict[year].append([country, gdp])
        # 在指定的key(这里是年份如：1960)后面value[]里面追加一个[country, gdp]

# 创建一个时间线对象
timeline = Timeline({"theme": ThemeType.DARK})

# 排序年份
# 先把字典里的全部key都取出来再排序
sorted_year_list = sorted(data_dict.keys())
for year in sorted_year_list:
    # 对同一年份所有国家根据gdp进行降序排序
    data_dict[year].sort(key=lambda element: element[1], reverse=True)
    # 取出本年份gdp前8名的国家
    year_data = data_dict[year][0:8]
    x_data = []
    y_data = []
    for country_gdp in year_data:
        x_data.append(country_gdp[0])  # x轴添加国家
        y_data.append(country_gdp[1] / 100000000)  # y轴添加gdp数据

    # 构建柱状图
    bar = Bar()
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP(亿)", y_data, label_opts=LabelOpts(position="right"))
    # 反转x和y轴
    bar.reversal_axis()

    # 设置每一年图表的标题
    bar.set_global_opts(
        title_opts=TitleOpts(title=f"{year}年GDP全球前8数据")
    )

    timeline.add(bar, str(year))

# 设置自动播放
timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=False
)

timeline.render("1960-2019全球GDP前8国家.html")