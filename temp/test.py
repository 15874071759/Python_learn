#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2/28/22 4:53 PM 
# @Author : huff 
# @File : test.py 
# @Software: PyCharm

from copy import deepcopy
# for  i in range(5):
#     print(i)
#     print(type(range(5)))


# res = lambda x,y: x+y
# print(res(5,6))


v = dict.fromkeys(['k1','k2'],[])
print(v)
v['k1'].append(666)
print(v)
v['k1'] = 777
print(v)

a = [1,2,3,4]
c = deepcopy(a)
print(c)