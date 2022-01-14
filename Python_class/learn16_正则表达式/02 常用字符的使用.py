#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-07-19 21:18 
# @Author : huff 
# @File : 02 常用字符的使用.py 
# @Software: PyCharm

import re
print('-------.的使用-------')
s='a'
s='A'
s='8'
s='_'
s='\n'
pattern = '.'
o = re.match(pattern,s)
print(o)
print('-------\d的使用-------')
s='0'
s='5'
s='9'
s='a'
s='\n'
pattern = '\d'
o = re.match(pattern,s)
print(o)

print('-------\D的使用-------')
s='0'
s='5'
s='9'
s='a'
s='\n'
pattern = '\D'
o = re.match(pattern,s)
print(o)

print('-------\s的使用-------')
s=' '
s='\n'
s='\t'
s='_'
pattern = '\s'
o = re.match(pattern,s)
print(o)

print('-------\S的使用-------')
s=' '
s='\n'
s='\t'
s='_'
pattern = '\S'
o = re.match(pattern,s)
print(o)

print('-------\w的使用-------')
s='z'
s='A'
s='8'
s='_'
s='#'
pattern = '\w'
o = re.match(pattern,s)
print(o)

print('-------\W的使用-------')
s='z'
s='A'
s='8'
s='_'
s='#'
s='+'
pattern = '\W'
o = re.match(pattern,s)
print(o)

print('-------[]的使用-------')
s='2'
s='3'
s='4'
pattern = '[2468]'
o = re.match(pattern,s)
print(o)