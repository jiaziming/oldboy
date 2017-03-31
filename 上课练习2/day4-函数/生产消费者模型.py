#!/usr/bin/env python
#-*-conding:utf-8-*-

import time

def consumer(name):
    print('%s 准备吃包子了！' %name)
    while True:
        baozi = yield

        print('包子[%s] 来了，被[%s]吃了！'%(baozi,name))


def producer(name):
    c1 = consumer('A')
    c2 = consumer('B')
    c1.__next__()
    c2.__next__()
    print('老子开始做包子了')
    for i in range(1,10):
        time.sleep(1)
        print('做了个包子')
        c1.send(i)
        c2.send(i)

producer("alex")
