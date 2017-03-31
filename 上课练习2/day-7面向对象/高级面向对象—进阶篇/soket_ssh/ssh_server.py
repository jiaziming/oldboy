#!/usr/bin/env python
#-*-conding:utf-8-*-

import socket
import subprocess

ip_port = ("127.0.0.1",9998)

sk = socket.socket()
sk.bind(ip_port)
sk.listen(5)

while True:
    print("server wating.....")
    conn,addr = sk.accept()
    while True:
        client_date = conn.recv(1024)
        if not client_date:break
        print("recv:",str(client_date,'utf8'))
        cmd = str(client_date,"utf8").strip()
        cmd_retsult =subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
        conn.send(cmd_retsult.stdout.read())

    conn.close()
