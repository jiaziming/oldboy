#!/usr/bin/env python
#-*-conding:utf-8-*-

import pymysql
from sqlalchemy import create_engine, Table,select, Column, Integer, String, MetaData, ForeignKey

metadata = MetaData()

user = Table('user', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(20)),
)

color = Table('color', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(20)),
)
engine = create_engine("mysql+pymysql://root:jia@1234@172.21.129.252:3306/test", max_overflow=5)

#metadata.create_all(engine)

conn =engine.connect()          #获取数据库位置

#添加
# sql = user.insert().values(name='wu')  #ID可写可不写 为自增
# sql = user.insert().values(name='a')
# sql = user.insert().values(name='ab')
# conn.execute(sql)
#
# # sql = user.insert().values(name="jia" )
# # conn.execute(sql)
# conn.close()

#删除
# sql = user.delete().where(user.c.name =='wu')
# conn.execute(sql)
# conn.close()

#修改
# sql = user.update().where(user.c.name == 'jack').values(name = 'ed')
#conn.close()

#查询
# sql = select([user.c.id])
# res = conn.execute(sql)
# print(res.fetchall())

