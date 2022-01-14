#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-07-15 22:22 
# @Author : huff 
# @File : 07 高阶函数sorted的使用.py 
# @Software: PyCharm

#对数值进行排序
sort_list = sorted([42,422,4,2,-100,3,-10])
print('默认升序',sort_list)

#逆序排序，给sorted添加reverse参数
sort_list = sorted([42,422,4,2,-100,3,-10],reverse=True)
print('逆序',sort_list)

#对字符串ASCII A:65 a:97
sort_list = sorted(['abc','ad','ABC','D','d','C'])
print('字符串排序',sort_list)


sort_list = sorted(['abc','ad','ABC','D','d','C'],reverse=True)
print('字符串排序',sort_list)

#sorted是高阶函数，还可以接收一个key函数来实现自定义的排序
#对数值列表，按绝对值的大小排序
sort_list = sorted([42,422,4,2,-100,3,-10],key=abs)
print('默认升序',sort_list)

#对字符串列表，忽略大小写
sort_list = sorted(['abc','ad','ABC','D','d','C'],reverse=True,key=str.lower)
print('字符串排序',sort_list)
