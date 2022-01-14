#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-06-19 17:39 
# @Author : huff 
# @File : my01.py 
# @Software: PyCharm

import shutil

import zipfile

#shutil.copyfile("1.txt","1_copy.txt")
#shutil.copytree("movie/港台","电影")  #"电影目录不存在时才能正常拷贝"
#shutil.copytree("movie/港台","电影",ignore=shutil.ignore_patterns("*.txt","*.html"))

#压缩，解压缩
#shutil.make_archive("电影/abc","zip","movie/港台")

# z1 = zipfile.ZipFile("a.zip","w")
# z1.write("1.txt")
# z1.write("1_copy.txt")
# z1.close()

z2 = zipfile.ZipFile("a.zip","r")
z2.extractall("电影")
z2.close()