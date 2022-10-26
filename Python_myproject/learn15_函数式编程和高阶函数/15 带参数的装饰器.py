#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-07-18 15:10 
# @Author : huff 
# @File : 15 带参数的装饰器.py 
# @Software: PyCharm

# def fun1():
#     print('功能1')
#
# def foo():
#     print('foo函数正在运行')

import time
def wirteLog(func):
    print('访问了方法名：',func.__name__,'\t时间：',time.asctime())

def funcOut(func):
    def funcIn(x,y):
        wirteLog(func)
        return func(x,y)
    return funcIn

@funcOut
def sum(a,b):
    return a+b

result = sum(10,20)
print('两数的和：',result)

def funcOut2(func):
    def funcIn(x,y,z):
        wirteLog(func)
        return func(x,y,z)
    return funcIn

#功能函数三个参数
@funcOut2
def add(a,b,c):
    return a+b+c

result=add(10,20,30)
print('三个数的和：',result)