#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-06-27 23:14 
# @Author : huff 
# @File : 05 ndarray对象属性.py 
# @Software: PyCharm

#导入numpy
import numpy as np

#创建一纬数组
a = np.array([1,2,3,4])
#创建二维数组
b = np.arange(4,10)
print(b)

b=np.random.randint(4,10,size=(2,3))
print(b)

#创建三纬数组
c = np.random.randn(2,3,4)
print(c)

#ndim属性
print('ndim:',a.ndim,b.ndim,c.ndim)
#shape属性
print('shape:',a.shape,b.shape,c.shape)
#dtype属性
print('dtype:',a.dtype,b.dtype,c.dtype)
#size 元素的总个数
print('size:',a.size,b.size,c.size)
#itemsize 每个元素所占的字节
print('itemsize:',a.itemsize,b.itemsize,c.itemsize)