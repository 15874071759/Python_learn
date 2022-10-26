#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-06-19 18:23 
# @Author : huff 
# @File : 递归算法2.py 
# @Software: PyCharm

#递归打印所有的目录和文件

import os

allfiles = []
def getAllFiles(path,level):
    childFiles = os.listdir(path)
    for file in childFiles:
        filepath = os.path.join(path,file)
        if os.path.isdir(filepath):
            getAllFiles(filepath,level+1)
        allfiles.append("\t"*level+filepath)

getAllFiles("../learn8",0)

for f in reversed(allfiles):
    print(f)

