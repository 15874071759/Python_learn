#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-03-31 21:56 
# @Author : huff 
# @File : file01.py 
# @Software: PyCharm

#测试写入中文

try:
    f = open(r'./a.txt','a',encoding='utf-8')
    strs = ['aa\n','bb\n','cc\n']

    f.writelines(strs)

except BaseException as e:
    print(e)

finally:
    f.close()