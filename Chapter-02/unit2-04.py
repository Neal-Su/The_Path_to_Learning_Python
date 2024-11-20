# SQL语言，数据查询DQL

"""
在SQL中，通过select关键字开头的SQL语句，来进行数据查询
查询一个库内的某些列
基础语法：select 字段列表 from 表;
     例：select id, name from student;
        select * from 表;  查询所有列
     例：select * from student;

其他语法：select 字段列表/* from 表 where 条件判断;
     例：select name from where student age > 20;

分组聚合：select 字段 聚合函数 from 表 where 条件 group by 列
        where条件为可有可没有
        聚合函数有：
                 sum(列)求和
                 avg(列)求平均值
                 min(列)求最小值
                 max(列)求最大值
                 count(列)求数量
        例：select id, avg(age), sum(age), min(age), max(age), count(*) from student group by id;
        一个SQL中是可以写多个聚合的
        group by 中出现了哪个列，哪个列才能出现在select中的非聚合中

排序和分页：select 列 聚合函数 * from 表
          where ...
          group by ...
          order by ... [asc/desc]
          limit n[,m]
          注：asc升序，desc降序
          例：select * from student where age > 19 order by id desc;
          注：n表示限制展示n条数据 n,m表示跳过n条之后展示m条数据， 1, 2 表示展示第二三条数据
          例：select * from student where age > 19 order by id desc limit 2;
             select * from student where age > 19 order by id desc limit 1, 2;
"""