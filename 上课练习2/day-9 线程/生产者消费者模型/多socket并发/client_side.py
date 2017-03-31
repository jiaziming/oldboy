#!/usr/bin/env python
#-*-conding:utf-8-*-

import socket

HOST = "localhost"
PORT = 8001

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))

while True:
    msg = bytes(input(">>:"),encoding = "utf8")
    if len(msg) ==0:continue
    s.sendall(msg)
    date = s.recv(1024)
    #print(date)

    print('Received',repr(date))

s.close()

    