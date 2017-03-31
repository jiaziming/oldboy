#!/usr/bin/env python
#-*-conding:utf-8-*-



def login(func): #func=sayi内存地址
    def weapper():
        print("login.........")
        return func()
    return weapper
#@login

def sayhi():
    print("Hi.......")
    return 9

sayhi = login(sayhi)
sayhi()



# if __name__ == "__main__"
#     print(login())
