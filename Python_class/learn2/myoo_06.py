#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-03-28 21:34 
# @Author : huff 
# @File : myoo_06.py 
# @Software: PyCharm

#测试重写object的__str__()

class Person: #默认继承object类

    def __init__(self,name):
        self.name = name

    def __str__(self):
        return "名字是{0}".format(self.name)

P = Person("hufangfang")
print(P)


