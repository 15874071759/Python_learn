#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-03-29 22:01 
# @Author : huff 
# @File : myoo_10.py 
# @Software: PyCharm

#工厂模式

class CarFactory:
    def creat_car(self,brand):
        if brand == '奔驰':
            return Benz()
        elif brand == '宝马':
            return BMW()
        elif brand == '比亚迪':
            return BYD()
        else:
            return "未知品牌，无法创建"

class Benz:
    pass

class BMW:
    pass

class BYD:
    pass

factory = CarFactory()
c1 = factory.creat_car('奔驰')
c2 = factory.creat_car('比亚迪')