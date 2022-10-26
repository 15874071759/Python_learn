#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-05-12 21:55 
# @Author : huff 
# @File : target3.py 
# @Software: PyCharm


# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        curNode = pHead
        temp = curNode
        preNode = None
        while curNode.next != None:
            temp.next = preNode
            preNode = curNode
            curNode = curNode.next
            temp = curNode
        return temp

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        temp = pHead
        preNode = None
        while pHead.next != None:
            temp.next = preNode
            preNode = pHead
            pHead = pHead.next
            temp = pHead
        return temp
