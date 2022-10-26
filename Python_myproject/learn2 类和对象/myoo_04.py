#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021-03-28 16:16
# @Author : huff
# @File : myoo_04.py
# @Software: PyCharm


#测试继承的基本使用

class Person:
    def __init__(self,name,age):
        self.name = name
        self.__age = age #私有属性

    def say_age(self):
        print("年龄，年龄我也不知道")

class Student(Person):
    def __init__(self,name,age,score):
        Person.__init__(self,name,age) #必须显式的调用父类的初始化方法，不然解释器不会去调用
        self.score = score

#Student->Person-Object

print(Student.mro())

s = Student("胡芳芳",18,90)
s.say_age()
print(s.name)
#print(s.age)
print(dir(s))
print(s._Person__age)