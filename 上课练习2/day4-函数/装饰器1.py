#!/usr/bin/env python
#-*-conding:utf-8-*-


def login(func):
        print("passed user verification")
        #func()
        return  func
    #return inner
#def home(name):
#    print("Welcome [%s] to home page" %name)


def Tv():
    print("Welcome [%s] to Tv page")

#def moive(name):
 #   print("Welcome [%s] to moive page" %name)

Tv = login(Tv)
Tv()
