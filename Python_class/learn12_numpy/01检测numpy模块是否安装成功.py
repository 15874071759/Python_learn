#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-06-25 23:15 
# @Author : huff 
# @File : test-numpy.py 
# @Software: PyCharm

#导入numpy
import numpy as np
import math
#创建数组
a=np.arange(10)
print(a)
print(type(a))

#对ndarray对象类型进行向量处理
print(np.sqrt(a))


#对列表中的元素开平方
b = [3,4,9]
#定义存储开平方结果的列表
result = []

#遍历列表
for i in b:
    result.append(math.sqrt(i))
print(result)