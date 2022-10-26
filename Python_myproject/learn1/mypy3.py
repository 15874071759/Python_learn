#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-03-11 09:34 
# @Author : huff 
# @File : mypy3.py 
# @Software: PyCharm

r1 = {'name': '高小一', 'age': 18, 'salary': 30000, 'city': '上海'}
r2 = {'name': '高小二', 'age': 19, 'salary': 40000, 'city': '北京'}
r3 = {'name': '高小三', 'age': 20, 'salary': 20000, 'city': '深圳'}
tb = [r1, r2, r3]

# 获得第二行人的薪资
print(r1)

print(tb[1].get('salary'))

# 打印所有人薪资

for i in range(len(tb)):
    print(tb[i].get('salary'))

for j in range(len(tb)):
    print(tb[j].get("name"), tb[j].get("age"), tb[j].get('salary', tb[j].get('city')))
