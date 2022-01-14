#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-05-05 21:46 
# @Author : huff 
# @File : target1.py 
# @Software: PyCharm

# def target_func(str):
#     alist = str.split()
#     blist = alist[len(alist)-1]
#     return len(blist)
#
# if __name__ == '__main__':
#     str = input("请输入：")
#     slen = target_func(str)
#     print(slen)

# def target_func():
#     astr = input()
#     if len(astr)>500 :
#         print("字符串不符合要求,重新输入：")
#         astr = input()
#     bstr = input()
#     acount = astr.count(bstr)
#     return acount
#
# if __name__ == "__main__":
#     s = target_func()
#     print(s)

import random
def target_fun(alist):
#     alist = []
#     for i in range(n-1):
#         alist.append(random.randint(1, n))
    blist = set(alist)
    clist = sorted(list(blist))
    return clist

if __name__ == "__main__":
    alist = []
    a = input()
    while a != '':
        a = input()
        alist.append(int(a))
    s = target_fun(alist)
    for i in range(len(s)):
        print(s[i])