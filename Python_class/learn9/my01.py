#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-06-20 17:48 
# @Author : huff 
# @File : my01.py 
# @Software: PyCharm

print("step0")
try:
    print("step1")
    a=3/2
    print("step2")
except BaseException as e:
    print("step3")
    print(e)
    print(type(e))
print("end!!!")