#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-06-19 17:19 
# @Author : huff 
# @File : file10.py 
# @Software: PyCharm

"""列出指定目录下所有的.py文件，并输出文件名"""

import os

path = os.getcwd()

file_list = os.listdir(path)

for filename in file_list:
    if filename.endswith("py"):
        print(filename)


print("################################")
file_list2 = [filename for filename in os.listdir(path) if filename.endswith("py")]
for f in file_list2:
    print(f,end="\t")