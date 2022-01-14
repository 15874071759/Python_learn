#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-07-17 22:19 
# @Author : huff 
# @File : 12 装饰器的基本使用.py 
# @Software: PyCharm

#使用装饰器 完成不修改func1() func2()函数的源码，添加输出日志信息
import time

def fun1():
    print('功能1')

def fun2():
    print('功能2')

def wirteLog(func):
    try:
        file = open('log.txt','a',encoding='utf-8')
        file.write('访问：')
        file.write(func.__name__)
        file.write('\t')
        file.write(time.asctime())
        file.write('\n')
    except Exception as e:
        print(e.args)
    finally:
        file.close()

#使用闭包
def funcOut(func):
    def funcIn():
        wirteLog(func)
        func()
    return funcIn

#闭包的调用
func1 = funcOut(fun1)
fun1()

@funcOut #func1 = funcOut(fun1)
def fun1():
    print('功能1')

@funcOut
def fun2():
    print('功能2')

fun1()
fun2()