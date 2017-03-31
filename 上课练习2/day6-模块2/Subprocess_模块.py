#!/usr/bin/env python
#-*-conding:utf-8-*-

import subprocess

a = subprocess.Popen("dir",stdout= subprocess.PIPE)


a.stdout.read()