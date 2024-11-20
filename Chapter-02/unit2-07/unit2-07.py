# 数据库综合案例

"""
案例需求：
使用面向对象章节案例中的数据集，完成使用Python语言，读取数据，并将数据写入MySQL的功能

本次开发我们需要新建一个数据库来使用，数据库名称：py_sql

 以下几句均是在MySQL里输入的
 create database py_sql charset utf8;
 use py_sql;
 基于数据结构，我们得到建表语句：
 create table orders(
             order_data date,
             order_id varchar(255),
             money int,
             province varchar(10)
            );
"""

# 读取数据对象，以及封装数据对象

from file_define import TextFileReader, JsonFileReader
from data_define import Record
from pymysql import Connection


text_file_reader = TextFileReader("E:/B python wenjian/2011年1月销售数据.txt")
json_file_reader = JsonFileReader("E:/B python wenjian/2011年2月销售数据JSON.txt")

jan_data: list[Record] = text_file_reader.read_data()
feb_data: list[Record] = json_file_reader.read_data()

# 将2个月份的数据合并为一个list来存储
all_data: list[Record] = jan_data + feb_data

# 构建MySQL链接对象
conn = Connection(
    host="localhost",  # (主机名)，ip地址也可以，localhost表示自己的电脑
    port=3306,  # 端口号，默认就是3306
    user="root",  # 账户，默认是root，这是mysql数据库的管理员账户
    password="mysql",  # mysql数据库密码，这里因为上传github，密码不是正确的，需要使用记得查询正确密码
    autocommit=True  # 设置自动提交
)
# 获取游标对象
cursor = conn.cursor()
# 选择数据库
conn.select_db("py_sql")
# 组织SQL语句
for record in all_data:
    sql = (f"insert into orders(order_data, order_id, money, province) "
           f"values('{record.data}', '{record.order_id}', {record.money}, '{record.province}')")
    # 执行SQL语句
    cursor.execute(sql)

# 关闭MySQL链接对象
conn.close()
