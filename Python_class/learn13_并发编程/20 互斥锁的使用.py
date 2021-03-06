#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-07-03 23:05 
# @Author : huff 
# @File : 20 互斥锁的使用.py 
# @Software: PyCharm

import time
from threading import Thread,Lock

num = 0

#创建一个互斥锁
lock = Lock()


def test1():
    global num
    lock.acquire() #上锁
    for i in range(100000):
        num +=1
    lock.release() #释放锁
    print('执行test1函数num的值：',num)

def test2():
    global num
    lock.acquire() #上锁
    for i in range(100000):
        num +=1
    lock.release() #释放锁

    print('执行test2函数num的值：',num)

if __name__ == '__main__':
    t1 = Thread(target=test1)
    t2 = Thread(target=test2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()