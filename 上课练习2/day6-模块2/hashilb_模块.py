#!/usr/bin/env python
#-*-conding:utf-8-*-

import hashlib,hmac


# m = hashlib.md5()
# m.update(b"Hello word")
# m.update(b"It's me")
# print(m.digest())


h = hmac.new('wueiqi')
h.update('hellowo')
print(h.hexdigest())
