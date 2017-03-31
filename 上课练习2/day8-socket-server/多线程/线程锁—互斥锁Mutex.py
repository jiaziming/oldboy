#!/usr/bin/env python
#-*-conding:utf-8-*-

import threading,time

def addNUM():
    global num  #在每个线程都获取这个全局变量
    print('--get num:',num)
    time.sleep(1)
    lock.acquire()
    num -= 1    #对公共变量进行-1操作
    lock.release()

lock =threading.Lock()
num = 100   #设置一个公共变量
thread_list = []
for i in range(100):
    t = threading.Thread(target=addNUM)
    t.start()
    thread_list.append(t)

for i in thread_list:   #等待所有线程直线完毕
    t.join()

print('final num:',num)