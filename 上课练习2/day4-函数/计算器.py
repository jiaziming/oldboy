#!/usr/bin/env python
#-*-conding:utf-8-*-

'''
1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )
'''

#1/先计算括号中的括号算出来 正则表达式找到最中间的括号

import re
def mutilpy_and_divdend(formula):
    print("运算结果：",formula)
    cllist = re.split("[+-]",formula)

    print(cllist)
def calc(formla):
    parenthese_flag = True
    while parenthese_flag:
        m = re.search("\([^()]+\)",formula)
        if m:
            print(m.group())
            sub_formula = m.group().strip("()")
            sub_res =mutilpy_and_divdend(sub_formula)

        break


if __name__ =="__main__":
    formula = "1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"
    res =calc(formula)

