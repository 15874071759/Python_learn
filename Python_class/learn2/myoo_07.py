#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-03-28 21:50 
# @Author : huff 
# @File : myoo_07.py 
# @Software: PyCharm

#测试super(),代表父类的定义，而不是代表父类的对象

class A:

    def say(self):
        print("A:",self)


class B(A):

    def say(self):
        #A.say(self)
        super().say()
        print("B:",self)

B().say()