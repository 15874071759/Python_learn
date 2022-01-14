#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-03-29 22:29 
# @Author : huff 
# @File : myoo_12.py 
# @Software: PyCharm

#测试工厂模式和单例模式整合使用
class CarFactory:
    __obj = None #类属性
    __init_flag = True
    def creat_car(self,brand):
        if brand == '奔驰':
            return Benz()
        elif brand == '宝马':
            return BMW()
        elif brand == '比亚迪':
            return BYD()
        else:
            return "未知品牌，无法创建"
    def __new__(cls, *args, **kwargs):
        if cls.__obj == None:
            cls.__obj = object.__new__(cls)
        return cls.__obj
    def __init__(self):
        if CarFactory.__init_flag == True:
            print("init CarFactory....")
            CarFactory.__init_flag = False
class Benz:
    pass
class BMW:
    pass
class BYD:
    pass
factory1 = CarFactory()
c1 = factory1.creat_car('奔驰')
c2 = factory1.creat_car('比亚迪')
print(c1)
print(c2)
factory2 = CarFactory()
print(factory1)
print(factory2)