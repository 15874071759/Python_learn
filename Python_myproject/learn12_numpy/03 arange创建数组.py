#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-06-27 22:14 
# @Author : huff 
# @File : 03 arange创建数组.py 
# @Software: PyCharm

#导入bumpy
import numpy as np

#range的使用 range(start,end,step)
a = list(range(1,10))
print(a)
b = list(range(10)) #默认的从0开始，步长是1
print(b)
c = list(range(1,10,3))
print(c)

#arange创建数组
#使用arange创建1,10的数组
a = np.arange(1,11)
print(a)

#设置step
b = np.arange(1,11,2)
print(b)

#设置dtype
c = np.arange(10,20,2,dtype=float)
print(c)
