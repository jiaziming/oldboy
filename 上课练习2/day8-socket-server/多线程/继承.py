#!/usr/bin/env python
#-*-conding:utf-8-*-

import threading,time

class MYThread(threading.Thread):
    def __init__(self,num):
        threading.Thread.__init__(self)
        self.num = num


    def run(self):
        print("runing on unmber:%s" %self.num)

        time.sleep(3)

if __name__ =='__main__':

    t1 = MYThread(1)
    t2 = MYThread(2)

    t1.start()
    t2.start()