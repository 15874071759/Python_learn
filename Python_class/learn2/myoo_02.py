#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-03-26 21:52 
# @Author : huff 
# @File : myoo_02.py 
# @Software: PyCharm

# class Student: #类首字母一般大写，多个单词采用驼峰原则
#
#     def __init__(self, name, score):    #self必须位于第一个参数
#         self.name = name
#         self.score = score
#
#     def say_score(self): #self必须位于第一个参数
#         print("{0}的分数是:{1}".format(self.name,self.score))
#
# stu2 = Student
# s1 = Student('san',80)
# s2 = stu2('si',99)
#
# s1.say_score()
# s2.say_score()

#测试可调用方法 __call__()

# class SalaryAccount:
#     def __call__(self, salary):
#         print("算工资")
#         yearSalary = salary*12
#         daySalary = salary//22.5
#         return dict(yearSalary=yearSalary,daySalary=daySalary)
#
# s = SalaryAccount()
# print(s(3000))

#测试方法的动态性
# class Person:
#     def work(self):
#         print("努力上班")
#
# def play_game(s):
#     print("{0}在玩游戏".format(s))
#
# def work2(s):
#     print("好好上班hahahhha")
#
# Person.play = play_game
# p = Person()
# p.work()
# p.play() #Person.play(p)
#
# Person.work = work2
# p.work()

#测试私有属性,私有方法
class Employee:

    __company = 'longbridge'
    def __init__(self, name ,age):
        self.name = name
        self.__age = age #私有属性

    def __work(self): #私有方法
        print("siyoufangfa")
        print(self.__age)

        print(Employee.__company)

e =Employee("xiaoxiao",18)
print(e.name)
#print(e.__age)
print(e._Employee__age)
print(dir(e))
print(Employee._Employee__company)

#e.__work()
e._Employee__work()