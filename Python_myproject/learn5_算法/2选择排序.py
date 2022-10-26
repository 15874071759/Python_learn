#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-05-19 22:19 
# @Author : huff 
# @File : 选择排序.py 
# @Software: PyCharm

def select_sort(alist):
    for i in range(len(alist)-1):
        #剩余列表中最小值索引
        min_index = i
        for j in range(i+1,len(alist)):
            if alist[min_index]>alist[j]:
                min_index=j
        if min_index != i:
            alist[i],alist[min_index] = alist[min_index],alist[i]


alist = [7,5,3,6,44,22,99,11]
print('原数组')
print(alist)
print('排序后数组')
select_sort(alist)
print(alist)
