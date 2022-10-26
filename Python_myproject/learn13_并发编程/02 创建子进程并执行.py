#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-07-01 21:34 
# @Author : huff 
# @File : 02 创建子进程并执行.py 
# @Software: PyCharm

from multiprocessing import Process

def run_test():
    print('....test....')

if __name__ == '__main__':
    print('主进程执行')
    #创建子进程 target接收执行的任务
    p = Process(target=run_test)
    #调用子进程
    p.start()