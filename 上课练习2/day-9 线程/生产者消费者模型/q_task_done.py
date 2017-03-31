#!/usr/bin/env python
#-*-conding:utf-8-*-

import queue,threading,time

def consumer(n):
    while True:
        print("\033[32;1m consumer [%s]\033[0m get task: %s" %(n,q.get()))
        time.sleep(1)
        q.task_done()


def producer(n):
    count = 1
    while True:
        #time.sleep(1)
        #if q.qsize() <3:
        print("prodcer [%s] produced a new task: %s" %(n,count))
        q.put(count)
        count +=1
        q.join()    #queue is emtpy
        print("all taks has been cosumed by consumers")


q = queue.Queue()

c1 = threading.Thread(target=consumer,args=[1,])
c2 = threading.Thread(target=consumer,args=[2,])
c3 = threading.Thread(target=consumer,args=[3,])

p = threading.Thread(target=producer,args=["XiaoYu",])
p1= threading.Thread(target=producer,args=["Liuyao",])

c1.start()
c2.start()
c3.start()

p.start()
p1.start()



