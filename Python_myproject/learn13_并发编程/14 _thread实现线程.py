#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-07-03 16:13 
# @Author : huff 
# @File : 14 _thread实现线程.py 
# @Software: PyCharm

#导入模块
import _thread
import  time

def func1():
    print('开始运行func1')
    time.sleep(4)
    print('运行func1结束')

def func2():
    print('开始运行func2')
    time.sleep(2)
    print('运行func2结束')

if __name__ == '__main__':
    print('开始运行')
    #创建线程
    _thread.start_new_thread(func1,())
    _thread.start_new_thread(func2,())
    time.sleep(7)