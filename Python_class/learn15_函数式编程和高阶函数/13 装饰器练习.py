#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-07-18 13:15 
# @Author : huff 
# @File : 13 装饰器练习.py 
# @Software: PyCharm

#给foo函数，新增功能

#在调用foo函数前，输出'I am foo'

def funcOut(func):
    def funcIn():
        print('I am foo')
        func()
    return funcIn

@funcOut
def foo():
    print('foo函数正在运行')


#使用闭包
#foo = funcOut(foo)

foo()