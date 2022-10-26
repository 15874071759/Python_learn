#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-06-25 22:25 
# @Author : huff 
# @File : 12操作mysql数据库查询一条数据.py 
# @Software: PyCharm

#导入pymysql
import pymysql
#创建连接
con = pymysql.connect(host="47.98.148.65",user="root",password="Huff@123",database="dbtest",port=3306)
#创建游标对象
cur = con.cursor()

#编写sql
sql = "select * from t_student"

try:
    #执行sql
    cur.execute(sql)
    #处理结果集
    student = cur.fetchone()
    #for student in students:
        #print(student)
    sno = student[0]
    sname = student[1]
    age = student[2]
    score = student[3]
    print("sno:",sno,"sname:",sname,"age:",age,"score:",score)

except Exception as e:
    print(e)
    print("查询所有数据失败")

finally:
    #关闭连接
    con.close()