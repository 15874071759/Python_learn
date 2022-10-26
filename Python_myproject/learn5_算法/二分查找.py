#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 3/15/22 5:06 PM 
# @File : 二分查找.py 
# @Software: PyCharm

def binary_search(list, target):
    left = 0
    right = len(list) - 1
    while left < right:
        mid = left + (right - left) // 2
        if list[mid] < target:
            left = mid + 1
        else:
            right = mid
    if list[left] == target:
        return left
    else:
        print("未找到")
        return -1

if __name__ == "__main__":
    list = [1, 2, 5, 6, 7, 8, 9]
    res = binary_search(list, 3)
    print("res", res)
