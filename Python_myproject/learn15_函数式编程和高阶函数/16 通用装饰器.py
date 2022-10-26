#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-07-18 15:24 
# @Author : huff 
# @File : 16 通用装饰器.py 
# @Software: PyCharm

import time

def funcOut(func):
    def funcIn(*args,**kwargs):
        wirteLog(func)
        return func(*args,**kwargs)
    return funcIn

def wirteLog(func):
    print('访问方法名：',func.__name__,'\t时间',time.asctime())

@funcOut
def sum(a,b):
    return a+b

@funcOut
def add(a,b,c):
    return a+b+c

result = sum(10,20)
print('两个数的和：',result)
result = add(10,20,30)
print('三个数的和：',result)

