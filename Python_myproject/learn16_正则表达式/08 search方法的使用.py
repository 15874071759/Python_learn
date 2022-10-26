#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-07-20 22:13 
# @Author : huff 
# @File : 08 search方法的使用.py 
# @Software: PyCharm

import re

pattern = 'hello'
s = 'hello python'
#m = re.search(pattern,s)
m = re.match(pattern,s)
print(m)
print(m.group())

print('-----macth和search的区别-----')
pattern = 'love'
s = 'I love you'
m = re.match(pattern,s)
print('使用match进行匹配',m)

o = re.search(pattern,s)
print('使用search进行匹配',o)

