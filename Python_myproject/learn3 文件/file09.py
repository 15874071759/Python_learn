#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-06-19 13:51 
# @Author : huff 
# @File : file09.py 
# @Software: PyCharm

"""测试os.path中关于目录、路径的操作"""

import os
#from os import path
import os.path

###############判断：绝对路径、是否目录、是否文件、文件是否存在#################
print(os.path.isabs("/Users"))
print(os.path.isdir("/Users"))
print(os.path.isfile("/Users"))
print(os.path.exists("/Users"))

###############获得文件基本信息在#################
print(os.path.getsize("file09.py"))
print(os.path.abspath("file09.py"))
print(os.path.dirname("/Users"))

print(os.path.getctime("file09.py")) #返回文件创建时间
print(os.path.getatime("file09.py")) #返回文件最后访问时间
print(os.path.getmtime("file09.py")) #返回文件最后修改时间

###############对路径的操作#################
path = os.path.abspath("file09.py")
print(os.path.split(path))  #路径和文件切割
print(os.path.splitext(path))  #扩展名切割
print(os.path.join("aa","bb","cc"))
