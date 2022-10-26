#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-06-25 23:26 
# @Author : huff 
# @File : 02 array创建数组.py 
# @Software: PyCharm

#导入numpy
import numpy as np

#使用array函数创建一维数组
a = np.array([1,2,3,4])
print(a)
print(type(a))

#使用array创建二维数组
b = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(b)
print(type(b))

#使用array创建三维数组
c=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(c)
print(type(c))

#array函数中dtype的使用
d = np.array([3,4,5],dtype=float)
print(d)
print(type(d))

#array函数中ndim的使用
e=np.array([5,6,7],dtype=float,ndmin=3)
print(e)
print(type(e))