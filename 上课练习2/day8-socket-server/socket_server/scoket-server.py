#!/usr/bin/env python
#-*-conding:utf-8-*-

import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        while True:
            print("new conn:",self.client_address)
            date = self.request.recv(1024)
            if not date:break
            print("client says:",date.decode())
            self.request.send(date)

if __name__ =='__main__':
    HOST,PORT = "localhost",50007

    
    server = socketserver.TCPServer((HOST,PORT),MyTCPHandler)
    server.serve_forever()


