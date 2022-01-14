#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-07-13 23:22 
# @Author : huff 
# @File : 02高阶函数map将数字转化为字符串.py 
# @Software: PyCharm

a = 10
#将10转换为字符串
s = str(a)
print(type(s))

a = [1,2,3,4,5,6,7,8,9] #将列表中每个元素转换成字符串
L = map(str,a)
print(list(L))