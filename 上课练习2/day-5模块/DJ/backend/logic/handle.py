#!/usr/bin/env python
#-*-conding:utf-8-*-

from backend.db.sq_api import select

def home():
    print("welcome to home page")
    q_date = select("user","dddd")
    print("query res:",q_date)

def movie():
    print("welcome to movie page")
def TN():
    print("welcome to Tv page")
