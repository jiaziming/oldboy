#!/usr/bin/env python
#-*-conding:utf-8-*-

from multiprocessing import Process,Pipe


def f(conn):
    conn.send([42,None,'hello'])
    conn.close()

if __name__ == '__main__':
    parent_conn,child_conn = Pipe()
    p = Process(target=f,args=(child_conn,))
    p1 = Process(target=f,args=(child_conn,))
    
    p.start()
    p1.start()
    print(parent_conn.recv())
    print(parent_conn.recv())  #print"[42,None,'hello']"
    p.join()



