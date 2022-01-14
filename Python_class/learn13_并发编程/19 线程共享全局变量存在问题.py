#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-07-03 22:49 
# @Author : huff 
# @File : 19 线程共享全局变量存在问题.py 
# @Software: PyCharm

import time
from threading import Thread

num = 0

def test1():
    global num
    for i in range(100000):
        num +=1
    print('执行test1函数num的值：',num)

def test2():
    global num
    for i in range(100000):
        num +=1
    print('执行test2函数num的值：',num)

if __name__ == '__main__':
    t1 = Thread(target=test1)
    t2 = Thread(target=test2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()