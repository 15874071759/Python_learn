#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-07-21 22:08 
# @Author : huff 
# @File : 11 匹配分组.py 
# @Software: PyCharm

import re
#匹配座机号码 区号{3,4}-电话号码{5,8} 010-43222  0432-447727
print('匹配座机号码')
pattern = r'(\d{3,4})-([1-9]\d{4,7}$)'
#pattern = r'\d{3,4}-[1-9]\d{4,7}$'

s = '010-786545'
o = re.match(pattern,s)
print(o)
print(o.group())
print(o.group(1))
print(o.group(2))
print(o.groups())
print(o.groups()[0])
print(o.groups()[1])

print('匹配网页标签内数据')
pattern = r'<.+><.+>.+</.+></.+>'
pattern = r'<(.+)><(.+)>.+</\2></\1>'
s = '<html><head>head部分</head></html>'
s = '<html><title>head部分</head></body>'
o = re.match(pattern,s)
print(o)

#<body><h1><div><div></div></div></h1></body>
print('(?p<name>) 分别起组名')
pattern = r'<(?P<k_html>.+)><(?P<k_head>.+)>.+</(?P=k_head)></(?P=k_html)>'
s = '<html><head>head部分</head></html>'
s = '<html><title>head部分</head></body>'
o = re.match(pattern,s)
print(o)
