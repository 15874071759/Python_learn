#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-06-15 22:56 
# @Author : huff 
# @File : file03.py 
# @Software: PyCharm

# a= ["我love u！","尚学堂\n","百战程序员\n"]
# b= enumerate(a)
# print(a)
# print(list(b))


with open("e.txt","r",encoding="utf-8") as f:
    lines = f.readlines()
    lines = [line.rstrip()+" #"+str(index+1)+"\n" for index,line in enumerate(lines)]


with open("e.txt","w",encoding="utf-8") as f:
    f.writelines(lines)

