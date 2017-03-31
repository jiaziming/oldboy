#!/usr/bin/env python
#-*-conding:utf-8-*-

#不规则数组进行从大到小的顺序进行排序

date = [10,4,33,21,54,3,8,11,5,22,2,1,17,13,6]

# print("before sort:",date)
#
# for j in range(1,len(date)):
#     for i in range(len(date)-j):
#         if date[i]>date[i+1]:
#             tmp = date[i+1]
#             date[i+1] = date[i]
#             date[i] = tmp
#
# print(date)
#
for a in range(1,len(date)):
    for i in range(len(date)-1):
        if date[i] >date[i+1]:
            tmp = date[i+1]
            date[i+1] = date[i]
            date[i] = tmp
    print(date)






