#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-06-23 22:37 
# @Author : huff 
# @File : 06操作sqlite3数据库修改数据.py 
# @Software: PyCharm

#导入模块
import sqlite3
#创建连接

con = sqlite3.connect("/Users/hufangfanghu/huffPythonSource/python/LB_interface/other/dbFile/demo.db")

#创建游标对象
cur = con.cursor()
#编写修改的sql语句
sql = "update t_person set pname=? where pno=?"
#执行sql

try:
    cur.execute(sql,("小张",1))
    #提交事务
    con.commit()
    print("修改成功")
except Exception as e:
    print(e)
    print("修改失败")
    con.rollback()
finally:

    #关闭连接
    con.close()
