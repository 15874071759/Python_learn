#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-07-19 22:17 
# @Author : huff 
# @File : 07 边界字符的使用.py 
# @Software: PyCharm

import re
#匹配QQ邮箱5-10数字

qq='865677@qq.com'
qq='865677@qq.com.cn'
qq='865677@qq.com.cn.126.com'

pattern = r'[1-9]\d{4,9}@qq.com$'
o= re.match(pattern,qq)
print(o)

print('-----^开始-----')
s='hello world'
s='hepython'
pattern = r'^hello.*'
o = re.match(pattern,s)
print(o)

print('-----\\b匹配单词左边界-----')
pattern = r'.*\bab'
s='12345 abc'
o=re.match(pattern,s)
print(o)

print('-----\\b匹配单词右边界-----')
pattern = r'.*ab\b'
s='12345 abc'
s='12345 ab'
o=re.match(pattern,s)
print(o)

print('-----\\B匹配非单词右边界-----')
pattern = r'.*ab\B'
s='12345 abc'
s='12345 abc'
o=re.match(pattern,s)
print(o)