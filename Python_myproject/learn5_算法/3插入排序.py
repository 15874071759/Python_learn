#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-05-19 22:52 
# @Author : huff 
# @File : 插入排序.py 
# @Software: PyCharm

#[54,  226,93,17,77,31,44,55,20] #升序排序


#插入排序

def insert_sort(alist):
    for j in range(1,len(alist)):
        i = j
        while i > 0: #和有序列表中每个元素进行比较（从最后一个开始）
            if alist[i]<alist[i-1]: #如果当前元素比前一个元素小，则进行交换
                alist[i],alist[i-1] = alist[i-1],alist[i]
            else: #否则已经是有序列表，则不需要交换，直接推出循环
                break
            i -=1

if __name__ == '__main__':
    alist = [54, 226,93,17,77,31,44,55,20]
    print('原数组')
    print(alist)
    print('排序后')
    insert_sort(alist)
    print(alist)
