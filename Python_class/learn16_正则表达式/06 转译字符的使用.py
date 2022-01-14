#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-07-19 22:08 
# @Author : huff 
# @File : 06 转译字符的使用.py 
# @Software: PyCharm

print('d:\\a\\b\\c')
print('\\nabc')
print('\\t123')

import re
s='\\t123'
pattern = r'\\t\d*'
o=re.match(pattern,s)
print(o)

s='\\\\t123'
pattern = r'\\\\t\d*'
o=re.match(pattern,s)
print(o)