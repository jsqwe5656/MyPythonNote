# -*- coding: utf-8 -*-

import os,sqlite3

db_file = os.path.join(os.path.dirname(__file__),'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

# 初始数据:
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()
#返回这个区间的名字并从高到低排列
def get_score_in(low, high):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    values = None
    result_list = []
    try:
        cursor.execute('select * from user where score between ? and ? order by score',(low,high))
        #获得查询结果集
        values = cursor.fetchall()
        #注意循环的是values里的个数 所以输出的是一个一个的tuple
        for i in values:
            print(i)
            result_list.append((i[1]))
        #print(result_list)
    except Exception as err:
        print(err)
    finally:
        cursor.close()
        conn.close()
    #print(values)
    return result_list

assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)

print('pass')




