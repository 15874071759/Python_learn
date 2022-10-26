#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-07-19 21:38 
# @Author : huff 
# @File : 04 重复数量号码.py 
# @Software: PyCharm

import re

print('------*的使用------')
pattern = '\d*'
s = '123456qwe'
s = '123456789qwe'
s='qwe'
o = re.match(pattern,s)
print(o)

print('------+的使用------')
pattern = '\d+'
s = '123456qwe'
s = '123456789qwe'
s='qwe'
o = re.match(pattern,s)
print(o)

print('------?的使用------')
pattern = '\d?'
s = '1qwe'
s = '123456789qwe'
s='qwe'
o = re.match(pattern,s)
print(o)

print('------{m}的使用------')
pattern = '\d{2}'
pattern = '\d{4}'
s = '123qwe'
# s = '123456789qwe'
# s='qwe'
o = re.match(pattern,s)
print(o)

print('------{m,n}的使用------')
pattern = '\d{2,5}'
s = '123456qwe'
# s = '123456789qwe'
s='qwe'
o = re.match(pattern,s)
print(o)


print('------{m,}的使用------')
pattern = '\d{2,}'
s = '12qwe'
# s = '123456789qwe'
#s='qwe'
o = re.match(pattern,s)
print(o)