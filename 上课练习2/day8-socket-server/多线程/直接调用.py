#!/usr/bin/env python
#-*-conding:utf-8-*-
import threading,time

def sayhi(num):

    print("runing on number:%s" %num)

    time.sleep(3)
if __name__ == '__main__':
    '''
    t1 = threading.Thread(target=sayhi,args=(1,))
    t2 = threading.Thread(target=sayhi,args=(2,))

    t1.start()  启动进程
    t2.start()  启动进程
    print(t1.getName())  打印线程名称
    print(t2.getName())  打印线程名称


    t2.join()   #p2.wait()
    print('__main__')'''

    t_list = []

    for i in range(10):
        a = threading.Thread(target=sayhi,args=[i])
        a.start()
        t_list.append(a)
    for i in t_list:
        i.join

    print('____main______')




