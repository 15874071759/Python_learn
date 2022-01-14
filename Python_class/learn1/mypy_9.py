#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-03-22 22:15 
# @Author : huff 
# @File : mypy_9.py 
# @Software: PyCharm

import copy

def testCopy():
    """测试浅拷贝"""
    a = [10,20,[5,6]]
    b = copy.copy(a)
    print("a:",a)
    print('b:',b)
    b.append(30)
    b[2].append(7)

    print("浅拷贝......")
    print("a:",a)
    print("b:",b)

def testDeepCopy():
    """测试深拷贝"""
    a = [10, 20, [5, 6]]
    b = copy.deepcopy(a)
    print("a:", a)
    print('b:', b)
    b.append(30)
    b[2].append(7)

    print("深拷贝......")
    print("a:", a)
    print("b:", b)


a = (10,20,[5,6])
print('a:',id(a))
def test01(m):
    print("m:",id(m))
    m[2][0] = 888
    print(m)
    print("m:",id(m))


#测试参数类型，位置参数，默认参数