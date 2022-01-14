#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-04-18 21:30 
# @Author : huff 
# @File : algo1.py 
# @Software: PyCharm
# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        self.n = n
        if self.n == 0:
            return 0
        if self.n == 1:
            return 1
        sum = self.Fibonacci(n-1) + self.Fibonacci(n-2)
        return sum
if __name__ == '__main__':

    s = Solution()
    print(s.Fibonacci(5))