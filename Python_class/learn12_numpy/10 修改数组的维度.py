#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-06-29 22:08 
# @Author : huff 
# @File : 10 修改数组的维度.py 
# @Software: PyCharm

#导入模块
import numpy as np

#通过reshape将一维数组修改成二维，三维数组

#创建一个一维数组
a = np.arange(1,25)
print(a)

#将一维修改成二维 (2,12)(12,2)(4,6)(3,8)
#b = a.reshape(4,6)
b = a.reshape((3,8))
print(b)

#将一维修改为三维 （2，3，4）
c = a.reshape((2,3,4))
print(c)

#通过np.reshape()进行修改
#bb = np.reshape(a,(3,8)) #将一维修改为二维
bb = np.reshape(a,(4,3,2)) #将一维修改为三维
print(bb)

print('****')
#将多维数组修改为一维数组
#a = bb.reshape(24)
a = bb.reshape(-1)
print(a)

#通过ravel,flatten函数将多维数组转换为一维数组
#ravel
a = bb.ravel()
print(a)

#flatten
a = bb.flatten()
print(a)

