#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-06-25 21:59 
# @Author : huff 
# @File : 09操作mysql数据库插入数据.py 
# @Software: PyCharm

#导入pymysql
import pymysql
#创建连接
con = pymysql.connect(host="47.98.148.65",user="root",password="Huff@123",database="dbtest",port=3306)
#创建游标对象
cur = con.cursor()
#编写sql
sql="insert into t_student(sname,age,score) values(%s,%s,%s) "

try:
    #执行sql
    cur.execute(sql,("小强",18,99.9))
    #提交事务
    con.commit()
    print("插入成功")
except Exception as e:
    print(e)
    con.rollback()
    print("插入失败")
finally:
    #关闭连接
    con.close()
