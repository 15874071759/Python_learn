#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-07-22 21:43 
# @Author : huff 
# @File : 04 send发送一个参数.py 
# @Software: PyCharm

def foo():
    print('starting')
    while True:
        res = yield 4
        print('res:',res)

g = foo()
print(next(g))
#print(next(g))
print(g.send(10))