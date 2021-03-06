#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-06-03 21:34 
# @Author : huff 
# @File : 5归并排序.py 
# @Software: PyCharm

def merg_sort(alist):
    #分解
    n = len(alist)
    #递归的出口 分解到最小
    if n <= 1:
        return alist
    mid = n//2
    left_li = merg_sort(alist[0:mid])
    right_li = merg_sort(alist[mid:])

    #合并
    #排序结果列表
    result = []
    left_pointer,right_pointer=0,0
    while left_pointer<len(left_li) and right_pointer<len(right_li):
        if left_li[left_pointer]<right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer+=1
        else:
            result.append(right_li[right_pointer])
            right_pointer+=1
    #退出循环后,将不为空的列表剩余元素添加到result中
    #result += left_li[left_pointer:]
    result.extend(left_li[left_pointer:])
    result += right_li[right_pointer:]

    #将最后排序的结果列表返回
    return result

if __name__ == '__main__':
    alist = [54,26,93,17,77,31,44,55]
    print('原来数组')
    print(alist)
    result = merg_sort(alist)
    print("排序后")
    print(result)




