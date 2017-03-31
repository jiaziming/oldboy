#!/usr/bin/env python
#-*-conding:utf-8-*-

import pickle

def login():
    print("hahaha")

f = open("test.txt","rb")


date = pickle.loads(f.read())
date['func']()

print(date)