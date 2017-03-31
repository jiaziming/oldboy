#!/usr/bin/env python
#-*-conding:utf-8-*-

class Foo:

    def __init__(self):
        pass
        self.n = 3
        #print('__init')

    def __call__(self, *args, **kwargs):

        print('__call__')


obj = Foo() # 执行 __init__
obj()       # 执行 __call__

print(obj.__dict__)

print(type(obj))