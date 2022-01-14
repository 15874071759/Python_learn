#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-04-24 23:17 
# @Author : huff 
# @File : 冒泡排序.py 
# @Software: PyCharm

#冒泡排序，对列表进行升序排序

def bubble_sort(alist):
    #相邻两个元素进行比较，如果发现位置错误则进行交换
    for k in range(len(alist)-1):
        for i in range(len(alist)-1-k):
            if alist[i]>alist[i+1]:
                alist[i],alist[i+1]=alist[i+1],alist[i]


#如果传入列表是有序的，则只需要检查一轮，查看是否进行的交换，如果没有进行交换，说明列表就是有序列表，则直接推出循环
def bubble_sort2(alist):
    #相邻两个元素进行比较，如果发现位置错误则进行交换
    for k in range(len(alist)-1):
        count = 0
        for i in range(len(alist)-1-k):
            if alist[i]>alist[i+1]:
                alist[i],alist[i+1]=alist[i+1],alist[i]
                count +=1
        #判断count的值是否等于0，如果等于0说明没有交换
        if count == 0:
            break


alist = [1,44,23,66,78,89,23]
print('原数组:',alist)
bubble_sort(alist)
print('排序数组：',alist)


alist2 = [1,2,23,66,78,89,99]
bubble_sort2(alist)
print('有序列表：',alist)