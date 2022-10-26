#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-07-13 23:11 
# @Author : huff 
# @File : 01高阶函数map使用.py 
# @Software: PyCharm

#一个函数f(x)=x2,要把这个函数作用在一个list[1,2,3,4,5,6,7,8,9]

a = [1,2,3,4,5,6,7,8,9]

def f(x):
    return x*x

result_list = []

for i in a:
    result_list.append(f(i))
print(result_list)

#使用map实现
it = map(f,a) #返回的it是一个可迭代的对象

#print(type(it))
#判断是否是一个可迭代的对象

from collections import Iterator
print('判断是否是可迭代的：',isinstance(it,Iterator))
print(list(it))