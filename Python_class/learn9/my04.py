#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-06-20 20:02 
# @Author : huff 
# @File : my04.py 
# @Software: PyCharm

"""测试finally"""

try:
    f = open("d:/a.txt","r")
    content = f.readline()
    print(content)
except:
    print("文件未找到")

finally:
    print("run in finally,关闭资源")
    try:
        f.close()
    except BaseException as e:
        print(e)

print("程序执行结束！")
