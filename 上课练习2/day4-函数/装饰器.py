#!/usr/bin/env python
#-*-conding:utf-8-*-

def login(func): #function= TV内存地址
    def inner(arg):
        print("passed user verification")
        func(arg)
        #return  func
    return inner
def home(name):
    print("Welcome [%s] to home page" %name)

@login
def Tv(name):
    print("Welcome [%s] to Tv page"%name)

def moive(name):
    print("Welcome [%s] to moive page" %name)

#Tv = login(Tv) #tv变量 = login（tv内存地址）
Tv("alex")


