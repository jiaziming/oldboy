#!/usr/bin/env python
#-*-conding:utf-8-*-

import pickle,json

def login():
    print("hello world")

f = open("test.txt","wb")

info = {
    "alex":"123",
    "jcak":"12345",
    "func":login
}


print(pickle.dumps(info))
f.write(pickle.dumps(info))


f.close()