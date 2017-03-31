 #!/usr/bin/env python
#-*-conding:utf-8-*-

import pymysql

from sqlalchemy import create_engine,and_,or_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,ForeignKey
from  sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_engine("mysql+pymysql://root:jia@1234@172.21.129.252:3306/test",echo=True)

class Host(Base):
    __tablename__ = 'hosts'
    id = Column(Integer,primary_key=True,autoincrement=True)
    hostname = Column(String(64),unique=True,nullable=False)
    ip_addr = Column(String(128),unique=True,nullable=False)
    port = Column(Integer,default=22)
    group_id = Column(Integer,ForeignKey('group.id'))


class Group(Base):
     __tablename__ = 'group'
     id = Column(Integer, primary_key=True)
     name = Column(String(64),unique=True,nullable=False)


Base.metadata.create_all(engine) #创建所有表结构

if __name__ == '__main__':
    sessionCls = sessionmaker(bind=engine) #创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
    session = sessionCls()


    #添加
    #h1 = Host(hostname='localhost',ip_addr='127.0.0.1')
    #h2 =Host(hostname='centos',ip_addr='172.21.129.252',port=10000)
    # session.add_all([h1,h2])
    # session.commit()

    #修改
    # obj = session.query(Host).filter(Host.hostname=='localhost').first()
    # print("---->:",obj)
    # obj.hostname ='tast server'

    #objs = session.query(Host).filter(and_(Host.hostname.like("cen%"),Host.port >20)).all()
    #print(objs)


    session.commit()