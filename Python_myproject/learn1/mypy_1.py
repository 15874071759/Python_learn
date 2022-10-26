#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-02-20 22:09 
# @Author : huff 
# @File : mypy_1.py 
# @Software: PyCharm

import time

time01 = time.time()  # 起始时间
a = ''
for i in range(1000000):
    a += 'sxt'
time02 = time.time()  # 终止时间
print("运算时间" + str(time02 - time01))

time03 = time.time()
li = []
for j in range(1000000):
    li.append('sxt')
a = ''.join(li)
time04 = time.time()
print("运算时间" + str(time04 - time03))
