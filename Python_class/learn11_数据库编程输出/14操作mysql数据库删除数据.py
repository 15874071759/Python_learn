#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-06-25 22:38 
# @Author : huff 
# @File : 14操作mysql数据库删除数据.py 
# @Software: PyCharm

#导入pymysql
import pymysql
#创建连接
con = pymysql.connect(host="47.98.148.65",user="root",password="Huff@123",database="dbtest",port=3306)
#创建游标对象
cur = con.cursor()

#编写修改的sql
sql = "delete from t_student where sno=%s"

try:
    #执行sql
    cur.execute(sql,(1))
    con.commit()
    print("删除数据成功")


except Exception as e:
    print(e)
    con.rollback()
    print("删除数据失败")

finally:
    #关闭连接
    con.close()