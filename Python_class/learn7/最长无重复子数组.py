#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-05-18 21:19 
# @Author : huff 
# @File : 最长无重复子数组.py 
# @Software: PyCharm

# alist = [2,3,4,5]
# blist = []
#
# # print(alist[:0:1])
# # print(alist[:1:1])
# # print(alist[:2:1])
#
#
# for i in range(len(alist)):
#     blist.append(1)
#     temp = alist[:i]
#     if i == 0:
#         continue
#     if alist[i] not in temp:
#         blist[i] = blist[i-1]+1
#     else:
#         blist[i] = blist[i-1]
# print(blist)
# print(max(blist))

#不满足运行时间要求
class Solution:
    def maxLength(self , arr ):
        alist = arr
        blist = [1]
        for i in range(1,len(alist)):
            temp = alist[:i]
            if i == 0:
                continue
            elif alist[i] not in temp:
                blist.append(blist[i-1]+1)
            else:
                blist.append(blist[i-1])
        return max(blist)

if __name__ == '__main__':
    s = Solution()
    arr = [1,2,3,1,2,3,2,2]
    print(s.maxLength(arr))
    print(type(min(3,4)))