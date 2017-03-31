#!/usr/bin/env python
#-*-conding:utf-8-*-

import sys

class WebServer(object):
    def __init__(self,host,port):
        self.host = host
        self.port = port

    def start(self):
        print("server is starting")
    def stop(self):
        print("server is stoping")
    def restart(self):
        self.stop()
        self.port()

if __name__ == '__main__':
    server =WebServer('localhost',333)
    #print(sys.argv[1])
    if hasattr(server,sys.argv[1]):
        func = getattr(server,sys.argv[1]) #获取server.start的内存地址
        func()                             #server.start()



    '''cmd_dic = {
        "start" :server.start,
        "stop":server.stop,
    }'''
    # if sys.argv[1] == 'start':
    #     #server.start()
    #     cmd_dic[sys.argv[1]]()
