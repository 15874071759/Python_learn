#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-04-18 22:39 
# @Author : huff 
# @File : algo3.py 
# @Software: PyCharm

#如果a+b+c=1000,a^2+b^2=c^2(a,b,c)为自然数，如何求所有a,b,c可能的组合

import time

start_time = time.time()
for a in range(0,1001):
    for b in range(0,1001):
        c = 1000 - a -b
        if a**2+b**2 == c**2:
            print('a:',a,'b:',b,'c:',c)
end_time = time.time()
print('time:',end_time-start_time)