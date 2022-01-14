#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-05-07 22:40 
# @Author : huff 
# @File : target2.py 
# @Software: PyCharm


class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        list_a = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    list_a.append(i)
                    list_a.append(j)
                    break
        return list_a

a = Solution()
print(a.twoSum([2,3,4],6))
