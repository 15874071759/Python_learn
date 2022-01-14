#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-06-29 21:14 
# @Author : huff 
# @File : 07 一维数组的切片和索引.py 
# @Software: PyCharm

#导入numpy
import numpy as np

a = np.arange(10)
print(a)

#正索引访问 从0开始 长度-1

print("索引0处的元素：",a[0])
print("索引5处的元素：",a[5])

#负索引访问 倒数第一个的索引为 -1
print("访问最后一个元素：",a[-1])
print("访问倒数第三个元素：",a[-3])

#切片操作 【start:stop:step】
print(a[:]) #从开始到结尾
print(a[3:]) #从索引3开始到结尾
print(a[3:5]) #从索引3开始到索引4[start,stop)结尾
print(a[1:7:2]) #从索引1开始到索引6，步长是2

#切片中负索引操作
print(a[::-1]) #反向获取
print(a[-5:-2])






