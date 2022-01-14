#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-06-19 17:59 
# @Author : huff 
# @File : 递归.py 
# @Software: PyCharm

"""测试递归算法"""

"""
num = 1
def a1():
    global num
    num +=1
    print("a1")
    if num<3:
        a1()

def b1():
    print("b1")

a1()
"""

#使用递归计算n的阶乘
def factorial(n):
    if n == 1:
        return n
    else:
        return n*factorial(n-1)
print(factorial(5))

