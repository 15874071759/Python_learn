#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-07-19 21:33 
# @Author : huff 
# @File : 03 匹配手机号码.py 
# @Software: PyCharm

import re

pattern = '1[35789]\d\d\d\d\d\d\d\d\d'

s='15874071759'

o = re.match(pattern,s)
print(o)

#电话号码 区号-座机号 010-3762266 0342-8776262
