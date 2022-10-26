#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-06-20 21:08 
# @Author : huff 
# @File : my08.py
# @Software: PyCharm

#测试调试、断点

def aa():
    print("run in aa() start!")
    print("step1")
    num1 = 3
    num2 = num1 * 4
    num3 = num2 * 5
    print("step2")
    print("run in aa() end!")

if __name__ == "__main__":
    print("main:step1")
    aa()
    print("main:step2")
    print("main:end!!!!")