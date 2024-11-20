# python操作mysql基础使用

# 演示python pymysql库的基础操作

from pymysql import Connection

# 构建到mysql数据库的链接
conn = Connection(
    host="localhost",        # (主机名)，ip地址也可以，localhost表示自己的电脑
    port=3306,               # 端口号，默认就是3306
    user="root",             # 账户，默认是root，这是mysql数据库的管理员账户
    password="mysql"   # mysql数据库密码，这里因为上传github，密码不是正确的，需要使用记得查询正确密码
)

# 获取mysql数据库基础信息
# print(conn.get_server_info())


# 执行非查询性质的sql语句：

# 获取到游标对象
cursor = conn.cursor()
conn.select_db("test")  # 选择数据库，选择test数据库去操作
# 执行sql
# cursor.execute("create table test_pymysql(id int); ")  # python中执行sql可以不写;分号


# 执行查询性质的sql语句：

conn.select_db("world")  # 选择数据库，选择world数据库去操作
cursor.execute("select * from student")  # 执行sql
# 获取查询结果
results = cursor.fetchall()  # 返回的是元组
print(results)
for r in results:
    print(r)

# 关闭链接
conn.close()
