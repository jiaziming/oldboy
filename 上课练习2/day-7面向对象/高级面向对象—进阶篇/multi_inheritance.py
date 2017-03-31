#!/usr/bin/env python
#-*-conding:utf-8-*-
import time

class A:
    n = "A"
    def f2(self):
        print("f2 from A")
class B(A):
    n = "B"
    def f1(self):
        print("from B")
    def f2(self):
        print("f2 from B")
class C(A):
    n = "C"
    def f2(self):
        print("form C")

class D(B,C):
    '''test class'''


    def __del__(self):
        print("deleteing the....")

d = D()

d.f1()
d.f2()
print(d.__doc__)
time.sleep(2)

print(d.__module__)

