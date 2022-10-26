#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-06-23 22:27 
# @Author : huff 
# @File : 04操作sqlite3查询数据.py 
# @Software: PyCharm

#导入模块
import sqlite3
#创建连接
con = sqlite3.connect("/Users/hufangfanghu/huffPythonSource/python/LB_interface/other/dbFile/demo.db")
#创建游标
cur = con.cursor()
#创建查询sql
sql = "select * from t_person"
try:
    cur.execute(sql)
    #返回结果集
    person_all = cur.fetchall()
    for person in person_all:
        print(person)
except Exception as e:
    print(e)
    print("查询所有数据失败")
finally:
    #关闭游标
    cur.close()
    #关闭连接
    con.close()