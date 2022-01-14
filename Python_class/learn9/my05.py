#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-06-20 20:28 
# @Author : huff 
# @File : my05.py 
# @Software: PyCharm

"""测试with上下文管理（with不是用来取代try...except...finally结构的，只是作为补充。方便我们在文件管理，网络通信时的开发）"""

with open("d:/dd.txt","r") as f:
    content = f.readline()
    print(content)

print("程序执行结束！")