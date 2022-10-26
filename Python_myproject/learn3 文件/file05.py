#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-06-17 22:55 
# @Author : huff 
# @File : file05.py 
# @Software: PyCharm

with open("e.txt","r",encoding="utf-8") as f:
    print("文件名是：{0}".format(f.name))
    print(f.tell())
    print("读取的内容：{0}".format(str(f.readline())))
    print(f.tell())
    f.seek(3)
    print("读取的内容：{0}".format(str(f.readline())))
