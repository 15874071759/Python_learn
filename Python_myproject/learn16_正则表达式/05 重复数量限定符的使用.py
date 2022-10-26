#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021-07-19 21:49
# @Author : huff
# @File : 05 重复数量限定符的使用.py
# @Software: PyCharm

import re
#匹配出一个字符串首字母为大写字符，后边都是小写字符，这些小写字母可有可无
print('-----案例1------')
pattern = '[A-Z][a-z]*'
s = 'Hello'
s = 'HEllo'
o = re.match(pattern,s)
print(o)

print('-----案例2------')
#匹配有效的变量名（字母，数字，下划线，而且数字不能开头）

pattern = '[a-zA-Z_][a-zA-Z0-9_]*'
pattern = '[a-zA-Z_]\w*'
s='userName'
s='age'
s='a'
s='3er'
s='_qwe'
o = re.match(pattern,s)
print(o)

print('-----案例3------')
#匹配1-99的数字

pattern = '[1-9]\d?'
s='2'
s='99'
s='100'
s='0'
o = re.match(pattern,s)
print(o)


print('-----案例4------')
#匹配一个随机密码8-20以内（大写字母，小写字母，下划线，数字）

pattern = '\w{8,20}'
s='12345678'
s='abc123qwe_'
s='1234567#'
o = re.match(pattern,s)
print(o)
