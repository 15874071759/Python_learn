#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-03-26 20:50 
# @Author : huff 
# @File : my00_01.py 
# @Software: PyCharm

class Student: #类首字母一般大写，多个单词采用驼峰原则

    def __init__(self, name, score):    #self必须位于第一个参数
        self.name = name
        self.score = score

    def say_score(self): #self必须位于第一个参数
        print("{0}的分数是:{1}".format(self.name,self.score))


s1 = Student('hufangfang',99)
s1.say_score()

print(dir(s1))
print(s1.__dict__)
print(isinstance(s1,Student))