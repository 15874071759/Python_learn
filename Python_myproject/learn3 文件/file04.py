#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-06-17 19:27 
# @Author : huff 
# @File : file04.py 
# @Software: PyCharm

with open("aa.jpg","rb") as f:
    with open("aa_copy.gif","wb") as w:
        for line in f.readlines():
            w.write(line)
print("图片拷贝完成")