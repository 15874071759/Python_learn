#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-07-01 22:22 
# @Author : huff 
# @File : 08 使用继承创建进程.py 
# @Software: PyCharm

#导入模块
from multiprocessing import  Process
from time import  sleep
import time

#定义类
class ClockProcess(Process):
    #重写初始化方法
    def __init__(self,interval):
        Process.__init__(self)
        self.interval =interval

    #重写run方法
    def run(self):
        print('子进程开始执行时间：{}'.format(time.ctime()))
        sleep(self.interval)
        print('子进程结束的时间：{}'.format(time.ctime()))

if __name__ == '__main__':
    #创建子进程
    p = ClockProcess(3)
    #调用子进程
    p.start()
    p.join()
    print('主进程执行完')