#!/usr/bin/env python
#-*-conding:utf-8-*-

from gevent import monkey; monkey.patch_all()
import gevent
from  urllib.request import urlopen

def f(url):
    print('GET: %s' % url)
    resp = urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))

gevent.joinall([
        gevent.spawn(f, 'https://www.python.org/'),
        gevent.spawn(f, 'https://www.sina.cn/'),
        gevent.spawn(f, 'https://baidu.com/'),
])
