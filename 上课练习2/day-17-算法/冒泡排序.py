#!/usr/bin/env python
#-*-conding:utf-8-*-
import  random


'''
def bubble_sort(array):
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[j-1] > array[j] : #exchange i and j
                tmp = array[j-1]
                array[j-1] = array[j]
                array[j] = tmp
'''


def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array)-1-i,):
            if array[j] > array[j+1]:
                tmp = array[j]
                array[j] = array[j+1]
                array[j+1] = tmp



if __name__ == '__main__':

    array = [29, 656, 879, 628, 320, 335, 111, 245, 283, 473, 757, 268, 777, 935, 352, 256, 307, 541, 697, 369]
    # for i in range (20):
    #     array.append(random.randrange(1000))
    print(array)

    bubble_sort(array)
    print(array)