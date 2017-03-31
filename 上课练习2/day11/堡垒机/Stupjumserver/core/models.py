#!/usr/bin/env python
#-*-conding:utf-8-*-

import pymysql

from sqlalchemy import create_engine,Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,ForeignKey,UniqueConstraint
from sqlalchemy.orm import relationship
from pyramid_sqlalchemy_utility import ChoiceType,PasswordType
engine = create_engine("mysql+pymysql://root:jia@1234@172.21.129.252:3306/test",echo=True)

Base = declarative_base()   #生成一个sqlORM 基类


HostUser2Group = Table('hostuser_2_group', Base.metadata,
    Column('hostuser_id', ForeignKey('host.id'), primary_key=True),
    Column('host_id', ForeignKey('host.id'), primary_key=True),
)


class Host(Base):
    __tablename__ ='host'
    id = Column(Integer,Primary_key=True,autoincrement=True)
    hostname = Column(String(64),unique=True,nullable=False)
    ip_addr = Column(String(128),unique=True,nullable=False)
    port = Column(Integer,default=22)

    def __repr__(self):
        return "<id=%s,hostname=%s,ip_addr=%s>" %(self.id,
                                                  self.hostname,
                                                  self.ip_addr)

class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True)
    name = Column(String(64),unique=True,nullable=False)

    def __repr__(self):
        return "<id=%s,name=%s>" %(self.id,self.name)


class UserProfile(Base):
    __tablename__ ='user_profile'
    id = Column(Integer,primary_key=True)
    username = Column(String=(64),unique=True,nullable=False)
    password = Column(String=(255),unique=True,nullable=False)

    def __repr__(self):
        return "<id=%s,usname=%s>" %(self.id,self.usname)

class HostUser(Base):
    __tablename__ ='host_user'
    id = Column(Integer,primary_key=True)
    host_id = Column(Integer,ForeignKey('host.id'))
    username = Column(String=(64),unique=True,nullable=False)
    password = Column(String=(255),unique=True,nullable=False)
    groups = relationship('Group',
                          secondary=HostUser2Group,
                          backref='host_list')


    __table_args__ = (UniqueConstraint('host_id', 'username', name='host_username_uc'),)


    def __repr__(self):
        return "<id=%s,host_name=%s>" %(self.id,self.usname)



