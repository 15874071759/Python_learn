#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-06-03 22:43 
# @Author : huff 
# @File : 6顺序查找.py 
# @Software: PyCharm

def sequence_search(alist,v):
    for i in range(len(alist)):
        if alist[i] == v:
            return i
    #没有找到
    return -1

if __name__ == '__main__':
    alist = [4,3,6,7,8,99,1,66]
    index =sequence_search(alist,99)
    if index!=-1:
        print('找到了，索引值为：',index)
    else:
        print('没有找到')