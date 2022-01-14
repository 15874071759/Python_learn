#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-06-24 22:09 
# @Author : huff 
# @File : 07操作mysql数据创建表.py 
# @Software: PyCharm

#导入pymysql
import pymysql

#创建连接
con = pymysql.connect(host="47.98.148.65",user="root",password="Huff@123",database="dbtest",port=3306)
#创建游标对象
cur = con.cursor()
#编写创建表的sql
sql="""
    create table t_student(
    sno int primary key auto_increment,
    sname varchar(30) not null,
    age int(2),
    score float(3,1) 
    )
"""
try:
    #执行创建表的sql
    cur.execute(sql)
except Exception as e:
    print(e)
    print("创建表失败")
finally:
    #关闭连接
    con.close()
    print("创建表成功")