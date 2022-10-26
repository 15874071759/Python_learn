#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-03-16 22:15 
# @Author : huff 
# @File : mypy_4.py 
# @Software: PyCharm

#测试if语句

# a = input("please input：")
# if int(a)<10:
#     print(a)
# b = []
#if b == 5:
# if b:
#
#     print("非空")
# else:
#     print("空")

# b = input("please input：")
# print(b if int(b)<10 else '小于10数字')

# score = int(input("请输入："))
# grade = ""
# if score<60:
#     grade = "不及格"
# elif score<80:
#     score = "及格"
# elif score <= 89:
#     grade = "良好"
# else:
#     grade = '优秀'
# print("分数是:{0},等级是:{1}".format(score, grade))

#测试选择结构嵌套
# score = int(input("输入分数："))
# grade = ''
# if score >100 or score<0:
#     score = int(input("输入错误，请重新输入："))
# else:
#     if score >= 90:
#         grade = 'A'
#     elif score >= 80:
#         grade = 'B'
#     elif score >= 70:
#         grade = 'C'
#     elif score >= 60:
#         grade = 'D'
#     else:
#         grade = 'E'
#     print("分数为{0},等级是{1}".format(score, grade))
#
# num =0
# while num<10:
#     print(num,end='\t')
#     num += 1

#计算1-100之间数字累计和
# num = 1
# sum = 0
# while num <= 100:
#     sum += num
#     num += 1
# print("总和:{0}".format(sum))

a = [10, 20, 30]
for i in a:
    print(i)

for j in range(len(a)):
    print(a[j])

for j in range(5):
    print(j,end='\t')

for x in 'shjfdhsg':
    print(x)

d = {'name': 'tom', 'age':18, 'job': '程序员'}
for i in d.keys():
    print(i)
for i in d.values():
    print(i)
for i in d.items():
    print(i)

#计算累加和
sum_all = 0
sum_even = 0
sum_odd = 0
for i in range(101):
    sum_all +=i
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i
print(sum_all , sum_odd, sum_even)