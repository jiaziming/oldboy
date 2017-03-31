#!/usr/bin/env python
#-*-conding:utf-8-*-

import sys,socket,time,gevent

from gevent import socket,monkey
monkey.patch_all()

def server(port):
    s = socket.socket()
    s.bind(('0.0.0.0', port))
    s.listen(500)
    while True:
        cli, addr = s.accept()
        gevent.spawn(handle_request, cli)

def handle_request(conn):
    try:
        while True:
            date = conn.recv(1024)
            print('recv:',date)
            conn.send(date)
            if not date:
                conn.shudown(socket.SHUT_WR)
    except Exception as ex:
        print(ex)
    finally:
        conn.close()

if __name__ == "__main__":
    server(8001)