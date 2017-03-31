#!/usr/bin/env python
#-*-conding:utf-8-*-


class Role(object):
    ac = None
    def __init__(self,name,role,weapon,life_value):#初始化方法
        self.name = name
        self.role = role
        self.weapon = weapon
        self.life_vaule = life_value

    def buy_weapon(self,weapon):
        print("%s is buying [%s]" %(self.name,weapon))
        self.weapon = weapon
        #print(self.ac)


#实例 role实例
#把一个抽象的对象变成一个具体的对象的过程 叫实例化

p1 = Role("sanjiang","Police","B10",90)
t1 = Role("chunyun","Terrprist","B11",100)
t2 = Role("t2","Police","B10",90)
t3 = Role("t3","Terrprist","B11",100)


Role.ac = "japanese brand"

p1.buy_weapon("AK47")
t1.buy_weapon("B51")
p1.ac = "china brand"
t1.ac = "US brand"



print("p1:",p1.weapon,)
print("t1:",t1.weapon,t1.ac)
print("t2:",t2.ac)
print("t3:",t3.ac)


