#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-07-20 22:44 
# @Author : huff 
# @File : 10 择一匹配符列表使用差异.py 
# @Software: PyCharm

import re

pattern = r'[xyz]'
s = 'y'
o = re.match(pattern,s)
print('使用列表【】：',o)

pattern = r'x|y|z'
s = 'y'
o = re.match(pattern,s)
print('择一匹配符｜：',o)

print('字符集([])和择一匹配符（｜）的用法，及它们的差异')
pattern = r'[ab][cd]'
s = 'ac'
s = 'ab'
o = re.match(pattern,s)
print(o)

pattern = r'ab[cd]'
s = 'ab'
s = 'abc'
s = 'abd'
o = re.match(pattern,s)
print(o)

pattern = r'ab|cd'
s = 'abc'
s = 'abd'
s = 'cd'
s = 'ad'
o = re.match(pattern,s)
print(o)
