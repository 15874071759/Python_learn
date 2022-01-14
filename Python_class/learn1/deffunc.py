#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020-07-09 12:41 
# @Author : huff 
# @File : def_func.py 
# @Software: PyCharm
import math

#算 ax*x-bx+c=0 的两个解
def quadratic(a,b,c):
    x=(-b+math.sqrt(b*b-4*a*c))/(2*a)
    y=(-b-math.sqrt(b*b-4*a*c))/(2*a)
    return x,y

#递归函数
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)

#去除字符串首尾空格
def trim(s):
    while s[:1] == ' ':
        s=s[1:]
    while s[-1:] == ' ':
        s=s[:-1]
    return s

#迭代查找一个list里边最小和最大值，并返回一个tuple
def find_min_and_max(L):
    n = len(L)
    if n == 0:
        return (None,None)
    else:
        min = L[0]
        max = L[0]
        for i in range(n):
            if L[i] < min:
                min = L[i]
            elif L[i] > max:
             max = L[i]
        return (min,max)


#斐波那契数列
def fib(max):
    n,a,b= 0,0,1
    while n<max:
        print(b)
        a,b=b,a+b
        n=n+1
    return 'done'

def isconfirm():
    a=3000
    b=3000
    print(id(a),id(b))
    print("比较值",a is b)