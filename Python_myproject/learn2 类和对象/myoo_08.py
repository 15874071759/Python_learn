#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-03-28 22:58 
# @Author : huff 
# @File : myoo_08.py 
# @Software: PyCharm

#测试运算符的重载

class Person:
    def __init__(self,name):
        self.name = name

    def __add__(self, other):
        if isinstance(other,Person):
            return "{0}--{1}".format(self.name,other.name)
        else:
            return "不是同类对象，不能相加"

    def __mul__(self, other):
        if isinstance(other,int):
            return self.name*other
        else:
            return "不能相乘"

p1 = Person("xiao")
p2 = Person("yuyu")
x = p1 + p2
print(x)
print(p1*3)

