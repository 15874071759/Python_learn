#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-07-18 13:20 
# @Author : huff 
# @File : 14 多个装饰器.py 
# @Software: PyCharm

#给foo函数，新增功能

#在调用foo函数前，输出'I am foo'

def funcOut(func):
    print('装饰器1')
    def funcIn():
        print('I am foo')
        func()
    return funcIn

def funcOut2(func):
    print('装饰器2')
    def funcIn():
        print('hello')
        func()
    return funcIn


@funcOut2
@funcOut
def foo():
    print('foo函数正在运行')


#使用闭包
#foo = funcOut(foo)

foo()