# -*- coding: utf-8 -*-
#导入mysql驱动
import mysql.connector

conn = mysql.connector.connect(user='root',password='root',database='test')
coursor = conn.cursor()

#在上面连接的test数据库中创建user表
coursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
#在表中插入数据
coursor.execute('insert into user (id,name) values (%s,%s)',['1','zbf'])
#提交事务
conn.commit()
coursor.close()
#运行查询
coursor = conn.cursor()
coursor.execute('select * from user where id=%s',('1',))
values = coursor.fetchall()
print(values)
#关闭游标和数据库连接
coursor.close()
conn.close()









