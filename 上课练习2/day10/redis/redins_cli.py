#!/usr/bin/env python
#-*-conding:utf-8-*-

import redis


#r =redis.Redis(host='172.21.129.252')  #正常连接方法  默认端口为6379 如为默认端口可以不写

pool = redis.ConnectionPool(host = "172.21.129.252",port=6379) #创建一个连接池的变量
r = redis.Redis(connection_pool=pool)   #连接池

#r.set("Name","JiaZiMing",ex=3)     #ex过期时间（秒） 过期时间为3秒
#r.set("Name","JiaZiMing",px=3)     #px过期时间（毫秒） 过期时间为3毫秒

# r.set("Name","JiaZiMing",nx=True)   #nx，如果设置为True，则只有name不存在时，当前set操作才执行
# print(r.get("Name"))

# r.set("Name","A",xx=True)           #xx，如果设置为True，则只有name存在时，当前set操作才执行
# print(r.get("Name"))

#r.mset(k1= 'v1',k2= 'v2')   #或 r.mset({'k1':'v1','k2':'v2'})  #批量设置值

# r.setbit("uv_count",5,1)
# r.setbit("uv_count",8,1)
# r.setbit("uv_count",3,1)
# print("uv count:",r.bitcount("uv_conunt"))
#
# n = "381"
# r.set("t",n)
#
# for i in n :
#     print(i,ord(i),bin(ord(i)))

# print("res:",r.get("t"))
#
# print(r.keys())


r.incr("count",1)

