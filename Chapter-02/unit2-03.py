# SQL语言，数据操纵DML

"""
数据插入：insert into 表(列1, 列2, ..., 列N) values(值1, 值2, ..., 值N), (值1, 值2, ..., 值N),
                    (值1, 值2, ..., 值N), ..., (值1, 值2, ..., 值N);
    例:  insert into student(id, name, age) values(4, '大连海事大学', 20),
        (5, '清华大学深圳', 21), (6, '新加坡国立大学', 22);
        SQL中为字符串提供数据需要单引号包围如：'新加坡国立大学'

数据删除：delete from 表名称 where 条件判断;
        where 条件判断      这段可以没有,代表整张表中的数据全部删除
        条件判断：列 操作符 值
                操作符：= < > <= >= != 等
                例：id = 5
                   id >= 6

数据更新：update 表名 set 列=值 where 条件判断;
        where 条件判断      这段可以没有,表示整张表所有的这个列内的数据都改为这个值
        例：update student set name = '上海交通大学' where id = 5;
"""