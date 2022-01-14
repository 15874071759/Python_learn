#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-07-13 23:24 
# @Author : huff 
# @File : 03高阶函数map传递两个列表.py 
# @Software: PyCharm

a = [1,2,3,4]
b = [10,20,30]

def f(x,y):
    return x+y

L = map(f,a,b)
print(list(L))