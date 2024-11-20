# SQL语言，数据定义DDL

"""
使用某个表前一定要先use那个库！！！
查看数据库：show databases;
使用数据库：use 数据库名称;
查看当前使用数据库：select database();
创建数据库：create database 数据库名称 charset utf8;
        charset utf8 表示以utf8编码，可以写可以不写，mysql默认编码模式就是utf8
删除数据库：drop database 数据库名称;


查看有哪些表：show tables;
        注意要先选择数据库（先use库）
创建表：create table 表名称(
            列名称 列类型,
            列名称 列类型,
            ...........
            列名称 列类型
       );
        列类型有：
                int             整数
                float           浮点数
                varchar(长度)    文本，长度为数字，做最大长度限制，长度最大可填255
                date            日期类型
                timestamp       时间戳类型

删除表：drop table 表名称;
"""