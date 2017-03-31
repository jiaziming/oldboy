#!/usr/bin/env python
#-*-conding:utf-8-*-

event_list = []

def  run():
    for event in event_list():
        obj =event()
        obj.execute()

class BsseHandler(object):
    '''
    用户必须继承该类，从而规范所有类的方法（类似于接口的功能）
    '''

def execute(self):
    raise Exception('you must overite excute')
