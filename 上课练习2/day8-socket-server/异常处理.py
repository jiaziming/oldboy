#!/usr/bin/env python
#-*-conding:utf-8-*-

# while True:
#     num1 =input('num1:')
#     num2 =input('num2:')
#
#     try:
#         num1 =int(num1)
#         num2 =int(num2)
#         result = num1 + num2
#     #except Exception ,e:
#     except ValueError as e:
#         print('Valu err',e)
#     except Exception as e:
#         print('异常处理，信息如下')
#         print(e)


class WupeiqiException(Exception):

    def __init__(self, msg):
        self.message = msg

    def __str__(self):
        return self.message
a = 1

try:
    assert  a == 1
    raise WupeiqiException('我的异常')
except WupeiqiException as e:
    print(e)
else:
    print("hahah else")

finally:
    print("no  matter right or wrong run this anyway!")


