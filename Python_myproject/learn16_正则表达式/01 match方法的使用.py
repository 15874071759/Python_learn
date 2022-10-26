#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-07-18 22:52 
# @Author : huff 
# @File : 01 match方法的使用.py 
# @Software: PyCharm

import re

s = 'hello python'
pattern = 'hello'
o = re.match(pattern,s)
print(o)
print(dir(o))
print(o.group()) #返回匹配的字符串
print(o.span())
print(o.start())

print('flags参数的使用')
s = 'hello python'
pattern = 'Hello'
o = re.match(pattern,s,flags=re.I)