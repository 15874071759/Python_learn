#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-07-15 21:53 
# @Author : huff 
# @File : 04 高阶函数reduce.py 
# @Software: PyCharm

from functools import reduce

#计算一个序列的求和
a=[1,2,3,4,5,6,7,8,9,10]

sum =0
for i in a:
    sum +=i

print('累加和：',sum)

def sumTest(x,y):
    return x+y

sum = reduce(sumTest,a)
print('reduce计算列表求和：',sum)