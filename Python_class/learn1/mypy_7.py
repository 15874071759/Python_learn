#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-03-17 22:14 
# @Author : huff 
# @File : mypy_7.py
# @Software: PyCharm

# for i in range(5):
#     for j in range(5):
#         print(i,end='\t')
#     print('\n')

# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{0}*{1}={2}'.format(i,j,i*j),end='\t')
#     print()


# r1 = dict(name='高小一', age=18, salary=30000)
# r2 = dict(name='高小二', age=19, salary=30000)
# r3 = dict(name='高小三', age=20, salary=10000)
# tb = [r1, r2, r3]
#
# for i in tb:
#     if i.get('salary') > 15000:
#         print(i)

# while True:
#     x = input("请输入：")
#     if x == 'O':
#         print("结束")
#         break
#     else:
#         print('输入为：{0}'.format(x))

# 员工数
count = 0
salary_sum = 0
salary = []
for i in range(4):
    x = input("请输入工资：")
    if x == 'Q':
        break
    if float(x)<0 :
        continue
    count +=1
    print(count)
    salary_sum +=float(x)
    salary.append(float(x))
else:
    print("共录入4名员工工资")
print('员工数：{0}，录入薪资：{1}，平均薪资{2}'.format(count,salary,salary_sum/i))
