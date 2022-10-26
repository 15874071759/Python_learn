#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-07-20 22:27 
# @Author : huff 
# @File : 09 匹配多个字符.py 
# @Software: PyCharm

import re

pattern = 'aa|bb|cc'
s = 'aa'
o = re.match(pattern,s)
print(o)

s = 'bb'
o = re.match(pattern,s)
print(o)

s = 'my name is cc'
o = re.search(pattern,s)
o = re.match(pattern,s)
print(o)

#匹配0-100之间所有的数字 0-99｜100
pattern = r'[1-9]?\d$|100$'
s = '1'
s = '11'
s = '99'
s = '100'
s = '1000'
o = re.match(pattern,s)
print(o)


