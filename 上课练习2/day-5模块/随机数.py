#!/usr/bin/env python
#-*-conding:utf-8-*-

import random

check_code = ""
for i in range(6):
    current = random.randint(0,4)
    if current != i:
        tmp = str(chr(random.randint(65,90)))
    else:
        tmp = random.randint(0,9)
    check_code += str(tmp)


print(check_code)

