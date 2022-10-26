#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-07-22 21:22 
# @Author : huff 
# @File : 02 使用yield实现协程.py 
# @Software: PyCharm

import time

def A():
    while True:
        print('--------A---------')
        yield
        time.sleep(0.5)

def B(c):
    while True:
        print('-------B--------')
        c.__next__()
        time.sleep(0.5)

a = A() #生成一个生成器对象
B(a)
