#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-07-01 21:57 
# @Author : huff 
# @File : 05 join方法中timeout使用.py 
# @Software: PyCharm

#导入模块
from multiprocessing import Process
from time import  sleep

def worker(interval):
    print('work start')
    sleep(interval)
    print('work end')

if __name__ == '__main__':
    print('主进程正在执行')
    #创建子进程
    p =Process(target=worker,args=(5,))
    #掉用子进程
    p.start()
    #希望下面的输出语句，在子进程执行完才输出
    #sleep(4)
    #调用join方法：主进程等待调用join的子进程结束
    p.join(3)
    print('主进程执行完')