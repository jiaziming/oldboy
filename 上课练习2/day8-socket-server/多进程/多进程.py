#!/usr/bin/env python
#-*-conding:utf-8-*-

from multiprocessing import Process
import time
def f(name):
    time.sleep(2)
    print('hello:', name)

if __name__ == '__main__':
    p = Process(target=f, args=('bob',))
    p1 = Process(target=f,args=('bovov',))

    p.start()
    p1.start()
    p.join()
