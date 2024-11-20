# python操作mysql数据插入

"""
pymysql在执行数据插入或其他产生数据更改的SQL语句时，默认是需要提交更改的
即，需要通过代码确认这种更改行为
通过链接对象.commit()即可确认这种更改行为

如果不想手动确认，可以在构建链接对象的时候，设置自动commit的属性
conn = Connection(
    host="localhost",        # (主机名)，ip地址也可以，localhost表示自己的电脑
    port=3306,               # 端口号，默认就是3306
    user="root",             # 账户，默认是root，这是mysql数据库的管理员账户
    password="mysql"   # mysql数据库密码，这里因为上传github，密码不是正确的，需要使用记得查询正确密码
    autocommit=True    # 设置自动提交
)
"""

from pymysql import Connection

# 构建到mysql数据库的链接
conn = Connection(
    host="localhost",        # (主机名)，ip地址也可以，localhost表示自己的电脑
    port=3306,               # 端口号，默认就是3306
    user="root",             # 账户，默认是root，这是mysql数据库的管理员账户
    password="mysql"   # mysql数据库密码，这里因为上传github，密码不是正确的，需要使用记得查询正确密码
)

# 获取到游标对象
cursor = conn.cursor()
conn.select_db("world")  # 选择数据库，选择world数据库去操作
cursor.execute("insert into student values(2, '大连海事大学', 19)")  # 执行sql
# 通过commit确认
conn.commit()

# 关闭链接
conn.close()
