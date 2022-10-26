#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-06-20 23:26 
# @Author : huff 
# @File : Salary.py 
# @Software: PyCharm

"""用于计算公司员工的薪资"""

company = "北京尚学堂"

def yearSalary(monthSalary):
    """根据传入的月薪的值，计算出年薪：monthsalary*12"""
    return monthSalary*12

def daySalary(monthSalary):
    """根据传入的月薪值，计算出1天的薪资。一个月按照22.5天计算"""
    return monthSalary/22.5


if __name__ == "__main__":
    print(yearSalary(20000))