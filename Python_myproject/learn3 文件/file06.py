#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-06-17 23:13 
# @Author : huff 
# @File : file06.py 
# @Software: PyCharm

"""
序列和反序列
"""
import pickle

a1 = "晨光"
a2 = 234
a3 = [10,20,30,40]

with open("data.dat", "wb") as f:
    pickle.dump(a1, f)
    pickle.dump(a2, f)
    pickle.dump(a3, f)

with open("data.dat","rb") as f:
    b1 = pickle.load(f)
    b2 = pickle.load(f)
    b3 = pickle.load(f)
    print(b1);print(b2);print(b3)
    print(id(a1))
    print(id(b1))