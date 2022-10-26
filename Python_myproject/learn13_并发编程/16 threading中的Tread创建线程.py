#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-07-03 16:34 
# @Author : huff 
# @File : 16 threading中的Tread创建线程.py 
# @Software: PyCharm

#导入模块
import threading
import time

def func1(thread_name,delay):
    print('线程{}开始执行func1'.format(thread_name))
    time.sleep(delay)
    print('线程{}运行func1结束'.format(thread_name))

def func2(thread_name,delay):
    print('线程{}开始执行func2'.format(thread_name))
    time.sleep(delay)
    print('线程{}运行func2结束'.format(thread_name))

if __name__ == '__main__':
    print('开始运行')
    #创建线程
    t1 = threading.Thread(target=func1,args=('thread-1',2))
    t2 = threading.Thread(target=func2,args=('thread-2',3))
    #启动线程
    t1.start()
    t2.start()
    t1.join()
    t2.join()


