#!/usr/bin/env python
#-*-conding:utf-8-*-

# def mail():
#     n = 123
#     n += 1
#     print(n)
#     return 123
# ret = mail()
# print(ret)

# def show():
#     print('a')
#     if 1 ==1:
#         return 11111
#     print('b')
#
#
# ret =show()
#


'''
#无参数
# show： -- 》 show()

#一个参数

def show(arg):
    print(arg)
show('1111')
'''


'''
#二个参数

def show(arg,kkkkk):    #可添加多参数     #默认参数必须放在最后
    print(arg,kkkkk)
show(123,789)
'''

'''
#默认参数

def show(a1,a2 = 999):
    print(a1,a2)

#show(123123)
show(1111,0)
'''

'''
#指定参数
def show(a1,a2):
    print(a1,a2)

#show(111,3333)
show(a2 =22222,a1 = 111)

运行结果:111 22222
'''

'''
#直接将参数转换为元组
def show(*arg):
    print(arg,type(arg))

show(11,223,44,55,66)

运行结果:(11, 223, 44, 55, 66) <class 'tuple'>
'''

'''
#直接将参数转换为字典
def show(**arg):
    print(arg,type(arg))

show(n1 = 12,uu =345)

运行结果：{'uu': 345, 'n1': 12} <class 'dict'>
'''


'''
#接受参数为元组、字典
def show(*arg,**karg):
    print(arg,type(arg))
    print(karg,type(karg))

show(11,33,44,55, n=1,m1=12)
运行结果：(11, 33, 44, 55) <class 'tuple'>
        {'n': 1, 'm1': 12} <class 'dict'>
'''


'''
s1 = '{name} is  {erice}'
d = {'name':'alex','erice':'sb'}

restult = s1.format(**d)
print(restult)
'''


#内置函数;

# a = all([0,1,2,3,4,5])
# print(a)

# a = bytearray('贾子明',encoding='utf-8')
# print(a)
#运行结果：bytearray(b'\xe8\xb4\xbe\xe5\xad\x90\xe6\x98\x8e')

# f = lambda x:x+1
# a= f(5)
#
# print(a)
# s = callable(f)
# print(s)


# a =['alex','koa','jia']
# for i,item in enumerate(a,1):
#     print(i,item)
# 运行结果：1 alex
#         2 koa
#         3 jia



# li = [1,2,3,4,5,6,7]
# # new_li = map(lambda x:x +100,li)
# # print(list(new_li))
# new_li = []
# for i in li:
#     print()



#f = open('test.log','r',encoding='utf-8')
# #f.write('asdjioaemqiowdmio')
# ret = f.read(4)
# f.close()
#


#
# # print(ret)
# f.tell()        #查看当前指针位置
# f.seek(1)       #指定当前指针位置
# ret =f.read()   #制定读取位置
#
# f.close()
# print(ret)

#
# f.seek(5)
# print(f.read())
# print(f.truncate())
# f.close()






