#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-07-17 20:33 
# @Author : huff 
# @File : 09 闭包的概念.py 
# @Software: PyCharm

#使用闭包，完成两个数的和

def sum(a,b):
    return a+b

def funcOut(num1):
    def funIn(num2):
        #内部函数修改外部函数的变量
        nonlocal num1
        num1 +=100
        return num2+num1
    return funIn

f = funcOut(100)  #调用外部函数，用f变量指向内部函数
print(type(f))
result = f(200)    #调用内部函数
print('两个数的和：',result)