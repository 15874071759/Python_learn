#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-02-22 15:01 
# @Author : huff 
# @File : mypy_2.py 
# @Software: PyCharm
import random


def generateStr():
    SOURCE = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    MY = []
    for i in range(8):
        MY.append(random.choice(SOURCE))

    my_target = "".join(MY)
    return my_target


if __name__ == '__main__':
    str = generateStr()
    print('生成字符串：', str)
