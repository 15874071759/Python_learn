#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-06-18 23:04 
# @Author : huff 
# @File : file08.py 
# @Software: PyCharm

#测试os模块中，关于文件和目录的操作

import os

#os.system("ping www.baidu.com")

###########获取文件和文件夹相关的信息############
print(os.name)   #windows->nt linux和unix->posix
print(os.sep)   #windows->\ linux和unix->/ 分隔符
print(repr(os.linesep)) #windows->\r\n linux和unix->\n 换行符
print(os.stat("file08.py")) #获取文件信息

###########关于工作目录的操作############

# print(os.getcwd()) #当前工作目录
# print(os.chdir("/Users/hufangfanghu")) #改变当前工作目录
# os.mkdir("书籍")

###########创建目录，创建多级目录，删除############
#os.mkdir("书籍")
#os.rmdir("书籍") #相对路径都是相对于当前的工作目录
#os.makedirs("电影/港台")
#os.removedirs("电影/港台") #只能删除空目录
#os.makedirs("../音乐/香港/刘德华") # ../指上一级目录
#os.rename("电影","movie")

dirs = os.listdir("movie") #列出文件下目录
print(dirs)





