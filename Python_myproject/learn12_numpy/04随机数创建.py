#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-06-27 22:23 
# @Author : huff 
# @File : 04随机数创建.py 
# @Software: PyCharm

#导入模块
import numpy as np

def randomtest():
    #使用random创建一维数组[0.0,1.0]
    a = np.random.random(size=5)
    print(a)
    print(type(a))

    #创建二维数组
    b = np.random.random(size=(3,4))
    print(b)

    #创建三维数组
    c = np.random.random(size=(2,3,4))
    print(c)

#随机整数
def randomintTest():
    #生成0-5之间的随机整数 一纬
    a = np.random.randint(6,size=10)
    print(a)
    print(type(a))

    #生成5-10之间的随机整数 二纬
    b = np.random.randint(5,11,size=(4,3)) #4行 3列
    print(b)

    #生成5-10之间的随机整数 三维
    c = np.random.randint(5,11,size=(2,4,3))
    print(c)

    #dtype的使用
    d = np.random.randint(10,size=5,dtype=np.int64)
    print('默认的dtype',d.dtype)

#创建标准的正太分布
def randnTest():
    a = np.random.randn(4)
    print(a)

    #创建二维
    b = np.random.randn(2,3)
    print(b)

    #创建三纬的数组
    c = np.random.randn(2,3)
    print(c)

#创建指定期望和方差的正太分布
def normalTest():
    a = np.random.normal(size=5) #默认的期望是loc=0.0 方差scale=1.0
    print(a)

    #指定期望和方差
    b = np.random.normal(loc=2,scale=3,size=(3,4))
    print(b)

#调用
#randomtest()
#randomintTest()
#randnTest()
normalTest()