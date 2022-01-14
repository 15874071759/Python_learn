#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-07-01 22:03 
# @Author : huff 
# @File : 06 Process两个属性的使用.py 
# @Software: PyCharm

#导入模块
import multiprocessing
import time

#定义执行任务的函数
def clock(interval):
    for i in range(3):
        print('当前时间：{}'.format(time.ctime()))
        time.sleep(interval)

if __name__ == '__main__':
    #创建子进程
    p = multiprocessing.Process(target=clock,args=(1,))
    p.start()
    p.join() #等待子进程执行结束再执行后拜年主进程部分
    print('p.id',p.pid)
    print('p.name',p.name)
    print('p.is_alive',p.is_alive())