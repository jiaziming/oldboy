#!/usr/bin/env python
#-*-conding:utf-8-*-

import random,time


def selection(arrary):
    for i in  range(len(arrary)):
        for j in range(i,len(arrary)):
            if arrary[i] > arrary[j]:
                tmp = arrary[i]
                arrary[i] = arrary[j]
                arrary[j] =tmp


if __name__ =='__main__':
    arrary = [29, 656, 879, 628, 320, 335, 111, 245, 283, 473, 757, 268, 777, 935, 352, 256, 307, 541, 697, 369]

    print(arrary)
    time_start = time.time()
    selection(arrary)
    time_end = time.time()

