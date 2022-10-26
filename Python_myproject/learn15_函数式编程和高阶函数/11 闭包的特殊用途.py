#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-07-17 21:06 
# @Author : huff 
# @File : 11 闭包的特殊用途.py 
# @Software: PyCharm

#闭包的特殊用途：不修改源代码的前提下，添加新的功能
#添加日志输出信息

import time
def writeLog(func):
    try:
        file = open('wirteLog.txt','a',encoding='utf-8')
        #向文件中写入日志信息（访问：方法名 时间：XXXX-XX-XX）
        file.write('访问：')
        file.write(func.__name__)
        file.write('\t')
        file.write('时间：')
        file.write(time.asctime())
        file.write('\n')
    except Exception as e:
        print(e.args)
    finally:
        file.close()

def func1():
    #writeLog(func1)
    print('功能1')

def func2():
    #writeLog(func2)
    print('功能2')

#使用闭包，不修改func1 和 func2的功能代码，添加日志信息
def funcOut(func):
    def funcIn():
        writeLog(func)
        func()
        print('调用',func.__name__,'结束')
    return funcIn

func1 = funcOut(func1)
func1()
func2 = funcOut(func2)
func2()