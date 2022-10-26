#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-07-01 23:06 
# @Author : huff 
# @File : 09进程池非阻塞状态使用.py 
# @Software: PyCharm

#导入模块
import multiprocessing
import  time

#定义进程执行的任务函数

def func(msg):
    print('start:',msg)
    time.sleep(3)
    print('end:',msg)

if __name__ == '__main__':
    #创建初始化3的进程池
    pool= multiprocessing.Pool(3)
    #添加任务
    for i in range(1,6):
        msg = '任务%d'%i
        pool.apply_async(func,(msg,))

    #如果进程池不在接收新的请求 调用close
    pool.close()
    #等待子进程结束
    pool.join()