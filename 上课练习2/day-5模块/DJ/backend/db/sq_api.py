#!/usr/bin/env python
#-*-conding:utf-8-*-

import os,sys


from config import settings

def db_auth(configs):
    if configs.DATABASE["user"] == "root" and configs.DATABASE["password"] =="123":
        print("db authentication passwd")
        return True
    else:
        print("db login error-----")

def select(table,column):
    if db_auth(settings):
        if table =="user":
            user_info = {
                "001":["alex","22","enineer"],
                "002":["longge","45","chenf"],
                "003":["xiaoyun","25","baoan"],
                }
            return user_info

