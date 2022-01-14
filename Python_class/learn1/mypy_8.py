#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-03-17 23:19 
# @Author : huff 
# @File : mypy_8.py 
# @Software: PyCharm

# names = ('tome','lisa','sandy')
# ages = (18, 19, 20, 21)
# jobs = ('teacher', 'dev', 'qa')
#
# for name, age, job in zip(names, ages, jobs):
#     print("{0}--{1}--{2}".format(name, age, job ))

# def test01(x):
#     """输入输出简单测试"""
#     print(x*5)
# help(test01.__doc__)
#
# print(id(test01))
# print(type(test01))
# print(test01)

# assert 1==0,'错误'

# if __name__=='__main__':
#     test01('f')

# def func1():  #函数定义
#     print('sxt')
#
# func1() #函数调用
# c = func1
# c()
# print(id(func1))
# print(id(c))
# print(type(c))

#
# a = 3 #全局变量
#
# def test01():
#     b = 4 #局部变量
#     global a #如果要在函数体内改变全部变量的值，增加global关键字使用
#     print(a)
#     a = 300
#
#     print(locals()) #打印输出局部变量
#     print(globals()) #打印输出全局变量
# test01()
# test01()

#测试局部变量和全局变量的效率

# import math
# import time
#
# def test01():
#     start = time.time()
#     for i in range(10000000):
#         math.sqrt(30)
#     end = time.time()
#     print("耗时：{0}".format((end-start)))
#
# def test02():
#     b = math.sqrt
#     start = time.time()
#     for i in range(10000000):
#         b(30)
#     end = time.time()
#     print("耗时：{0}".format((end-start)))
#
# test01()
# test02()

#测试参数传递
#传递可变对象

a = [10,20]
print(id(a))
print(a)
print('*************')
def test01(m):
    print(id(m))
    m.append(300)
    print(id(m))
    print(m)

test01(a)
print(a)