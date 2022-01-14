#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-03-23 22:22 
# @Author : huff 
# @File : mypy10.py 
# @Software: PyCharm

# f = lambda a, b, c : a*b*c
# print(f(3,4,5))

# s = "print('dhfkdjg;')"
# eval(s)
#
# a = 10
# b = 20
# c = eval("a+b")
# print(c)
#
#
# dict1 = dict(a=100,b=200)
# d = eval("a+b",dict1)
# print(d)

#使用递归计算阶层，5！=5*4*3*2*1

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n*factorial(n-1)
#
# result = factorial(5)
# print(result)

def outer():
    print("outer running")
    def innner():
        print("innner running")
    innner()
outer()