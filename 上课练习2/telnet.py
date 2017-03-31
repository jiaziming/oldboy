#!/usr/bin/env python
#-*-conding:utf-8-*-

import telnetlib
def do_telnet(Host, username, password, finish, commands):
    print ('hi')

    '''Telnet远程登录：Windows客户端连接Linux服务器'''

    # 连接Telnet服务器
    tn = telnetlib.Telnet(Host, port=22, timeout=40)


    # 输入登录用户名
    tn.read_until('login: ')
    tn.write(username + '\n')

    print('hi')

    # 输入登录密码
    tn.read_until('Password:')
    tn.write(password + '\n')

    print('hi')

    # 登录完毕后执行命令
    print('hi')
    print(commands)
    tn.write('%s\r\n' %  commands)

    temp = tn.read_all()
    print("%r",temp)


    #执行完毕后，终止Telnet连接（或输入exit退出）


    temp = tn.read_until(finish)
    print("%r",temp)





    tn.close() # tn.write('exit\n')

    print('hi')

if __name__=='__main__':
     # 配置选项
    Host = '172.21.10.2'
    username = 'root'   # 登录用户名
    password = 'limu1992'  # 登录密码
    finish = '~ #>'      # 命令提示符
    commands = 'help'
    do_telnet(Host, username, password, finish, commands)
