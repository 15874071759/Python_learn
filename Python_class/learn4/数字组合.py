#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-04-23 20:44 
# @Author : huff 
# @File : 1.py 
# @Software: PyCharm
'''
程序题有1、2、3、4四个数字，能组成多少个无重复数字的三位数字，计数并把它们打印出来。
'''
list = [1, 2, 3, 4]
count = 0  # 组合计数
for i in range(len(list)):
    x = str(list.pop(i))
    for j in range(len(list)):
        y = str(list.pop(j))
        for k in range(len(list)):
            print(x + y + str(list[k]), end='  ')
            count += 1
        list.insert(j, int(y))
    list.insert(i, int(x))
    print('')
