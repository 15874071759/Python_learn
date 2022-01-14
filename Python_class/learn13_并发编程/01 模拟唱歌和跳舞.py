#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-07-01 21:22 
# @Author : huff 
# @File : 01 模拟唱歌和跳舞.py 
# @Software: PyCharm

from time import sleep

def sing():
    for i in range(3):
        print('正在唱歌。。。%d'%i)
        dance()
        sleep(1)

def dance():
    for i in range(3):
        print('正在跳舞。。。%d'%i)

if __name__ == '__main__':
    sing()
    dance()