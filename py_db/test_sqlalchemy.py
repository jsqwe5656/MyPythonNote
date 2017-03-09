#-*- coding: utf-8 -*-

from sqlalchemy import Column,String,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#创建对象的基类
Base = declarative_base()

#定义准备实体化的User对象
class User(Base):
    #表的名字
    __tablename__ = 'user'
    #表的结构
    id = Column(String(20),primary_key=True)
    name = Column(String(20))

#初始化数据库连接 '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/test')
#创建DBSession类型
DBSession = sessionmaker(bind=engine)

#创建session对象
session = DBSession()
#创建新的User对象
new_user = User(id='3',name='bff')
#将user对象添加到session中
session.add(new_user)
#提交（即保存到数据库）
session.commit()
#关闭session
session.close()

#创建Session
session = DBSession()
#创建Query查询，filter是where条件,最后调用one()返回唯一行，如果调用all()则返回所有行
user = session.query(User).filter(User.id=='2').one()
#打印类型和对象的nmae属性
print('type:',type(user))
print("name:",user.name)
#关闭session
session.close()




