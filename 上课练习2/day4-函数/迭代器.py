#!/usr/bin/env python
#-*-conding:utf-8-*-

# a = iter(['eric','alex','jcak'])
# print(a)
#
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
#
# f = open('jia.py')
# f. read()
# f.readlines()

def cash_out(amount):
    while amount >0:
        amount -= 1
        yield 1
        print("擦、又来取钱了。。。")

ATM = cash_out(5)

print(type(ATM))
print("取到钱 %s 元" %ATM.__next__())
print("取到钱 %s 元" %ATM.__next__())
print('叫了个大保健')

