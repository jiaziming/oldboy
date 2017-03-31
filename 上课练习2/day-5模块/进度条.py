#!/usr/bin/env python
#-*-conding:utf-8-*-


import sys,time

for i in range(10):
    sys.stdout.write("#")
    sys.stdout.flush()      #强制刷新#
    time.sleep(0.5)