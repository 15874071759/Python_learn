#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-04-24 20:34 
# @Author : huff 
# @File : 随机数.py 
# @Software: PyCharm
#python生成100个不重复的4位数随机数。

# import random
# a = [a for a in range(1,9)]
# b = [b for b in range(0,9)]
# c = [c for c in range(0,9)]
# d = [d for d in range(0,9)]
# list = []
# count = 0
# while count < 101:
#     aa = random.choice(a)
#     bb = random.choice(b)
#     cc = random.choice(c)
#     dd = random.choice(d)
#     if aa != bb != cc != dd:
#         target = str(aa) + str(bb) + str(cc) + str(dd)
#         list.append(int(target))
#         count +=1
# print(list)

import random
list = [a for a in range(1000,10000)]
target = []
for i in range(100):
    aa = random.choice(list)
    list.remove(aa)
    target.append(aa)
print(target)