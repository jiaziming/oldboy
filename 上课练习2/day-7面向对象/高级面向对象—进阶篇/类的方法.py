#!/usr/bin/env python
#-*-conding:utf-8-*-

class Animal:
    def __init__(self,name,):
        self.name = name
        self.num = None


    hpbbie = "meat"


    @classmethod    #类方法 不能访问实例变量
    def talk(self):
        print("%s is talking....." %self.name)
    @staticmethod   #静态方法，不能访问类变量和实例变量
    def walk(self):
        print("%s is walking....." %self.name)
    @property    #把方法变成属性
    def habit(self):
        print("%s habit xxoo" %self.name)
    @property
    def total_players(self):
        return self.num
    @total_players.setter
    def total_players(self,num):
        self.num =num
        print("total  players:",self,num)





d =Animal("SNAJIANG")
#d.talk()
print(d.total_players)
d.total_players = 3
