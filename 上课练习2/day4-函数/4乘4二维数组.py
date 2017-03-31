#!/usr/bin/env python
#-*-conding:utf-8-*-

array=[[col for col in range(4)] for row in range(4)]
'''
[0, 1, 2, 3]
[0, 1, 2, 3]
[0, 1, 2, 3]
[0, 1, 2, 3]
'''
for row in array:
    print(row)
#
# print("----------------")
# for i,row in enumerate(array):
#     for index in range(1,len(row)):
#         tmp = array[index][i]
#         array[index][i] = array[i][index]
#         print(tmp,array[i][index])
#         array[i][index] = tmp
#     for r in array:print(r)
# print('---one big loop ---')








