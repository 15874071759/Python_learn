#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-03-28 15:57 
# @Author : huff 
# @File : myoo_03.py 
# @Software: PyCharm

#测试@property的用法

class Employee:

    def __init__(self,name,salary):
        self.__name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self,salary):
        if 1000 < salary < 30000:
            self.__salary = salary
        else:
            print("录入错误")


emp1 = Employee("hufangfang",30000)

emp1.salary = 2000
print(emp1.salary)

# emp1.set_salary(2000)
# print(emp1.get_salary())
