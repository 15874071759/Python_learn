#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-07-15 22:39 
# @Author : huff 
# @File : 08 匿名函数.py 
# @Software: PyCharm

#lambda arg1,arg2,arg3...:表达式
f = lambda a,b,c:a+b+c
print('调用：',f(3,4,5))

#匿名函数作为map高阶函数的参数 f(x)=x*x
L = map(lambda x:x*x,[1,2,3,4,5,6,7,8,9])
print(list(L))

#sorted中使用匿名函数
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

stu1 = Student('zhangsan',21)
stu2 = Student('lisi',25)
stu3 = Student('wangwu',23)
result_list = sorted([stu1,stu2,stu3],key=lambda x:x.age,reverse=True)
#result_list = sorted([stu1,stu2,stu3],key=lambda x:x.name)

for stu in result_list:
    print('name:',stu.name,'age:',stu.age)


