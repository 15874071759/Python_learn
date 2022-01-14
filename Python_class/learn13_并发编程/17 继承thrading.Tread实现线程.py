#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-07-03 16:43 
# @Author : huff 
# @File : 17 继承thrading.Tread实现线程.py 
# @Software: PyCharm

#导入模块
import threading
import time

def func1(delay):
    print('线程{}执行func1'.format(threading.current_thread().getName()))
    time.sleep(delay)
    print('线程{}执行func1结束'.format(threading.current_thread().getName()))


def func2(delay):
    print('线程{}执行func2'.format(threading.current_thread().getName()))
    time.sleep(delay)
    print('线程{}执行func2结束'.format(threading.current_thread().getName()))

#创建一个类Mythread 继承threading.Tread
class MyThread(threading.Thread):
    #重写构造方法
    def __init__(self,func,name,args):
        super().__init__(target=func,name=name,args=args)

    def run(self):
        self._target(*self._args)


if __name__ == '__main__':
    print('开始运行')
    t1 = MyThread(func1,'thread-1',(2,))
    t2 = MyThread(func2,'thread-2',(4,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
