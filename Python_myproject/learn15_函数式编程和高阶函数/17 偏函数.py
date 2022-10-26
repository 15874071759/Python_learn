#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-07-18 15:30 
# @Author : huff 
# @File : 17 偏函数.py 
# @Software: PyCharm

print(int('12345')) #按照十进制转换成整数
print('转换为八进制：',int('12345',base=8))
print('转换为八进制：',int('12345',base=16))

#将'1010'按二进制转换为整数
print(int('1010',base=2))
print(int('101010',base=2))

#定义函数
def new_int(s):
    return int(s,base=2)

print(new_int('101010'))

from functools import partial
new_int = partial(int,base=2)
print(new_int('1010101'))
print(new_int('101010'))
print(new_int('1010'))