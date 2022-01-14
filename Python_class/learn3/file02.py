#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-04-03 18:02 
# @Author : huff 
# @File : file02.py 
# @Software: PyCharm

with open(r'./b.txt','r',encoding='utf-8') as f:
    #f.write('dfjhskgkhgkhf')
    #s = f.read()
    #s = f.read(3)
    for a in f:
        print(a,end='')