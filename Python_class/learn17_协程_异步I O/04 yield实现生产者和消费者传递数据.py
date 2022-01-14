#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-07-22 21:46 
# @Author : huff 
# @File : 04 yield实现生产者和消费者传递数据.py 
# @Software: PyCharm

def produce(c):
    for i in range(1,10):
        print('生产者生产产品:%d'%i)
        c.send(str(i))

def consumer():
    while True:
        res = yield
        print('消费者消费产品：',res)

c = consumer() #生成器对象
next(c)
produce(c)