#!/usr/bin/env python
#-*-conding:utf-8-*-

import queue

class Foo(object):
    def __init__(self,n):
        self.n = n


q = queue.Queue(maxsize = 3)
q.put([1,2,4,5])
q.put(Foo(1))
#q.get(timeout=3)
date = q.get_nowait()
date2 = q.get_nowait()

print(date,type(date))
print(date2,type(date))

print(q.full())