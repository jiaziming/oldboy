#!/usr/bin/env python
#-*-conding:utf-8-*-

import socket

ip_port = ("127.0.0.1",9999)

sk = socket.socket()
sk.bind(ip_port)
sk.listen(5)

while True:
    print("server wating.....")
    conn,addr = sk.accept()

    client_date = conn.recv(1024)
    print(str(client_date,'utf8'))
    conn.sendall(bytes('不要回答，不要回答，不要回答','utf8'))

    conn.close()