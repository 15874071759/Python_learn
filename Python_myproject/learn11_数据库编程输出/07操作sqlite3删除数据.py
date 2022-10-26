#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-06-23 22:42 
# @Author : huff 
# @File : 07操作sqlite3删除数据.py 
# @Software: PyCharm

#导入模块
import sqlite3
#创建连接

con = sqlite3.connect("/Users/hufangfanghu/huffPythonSource/python/LB_interface/other/dbFile/demo.db")

#创建游标对象
cur = con.cursor()
#编写删除的sql语句
sql = "delete from  t_person  where pno=?"
#执行sql

try:
    cur.execute(sql,(1,))
    #提交事务
    con.commit()
    print("删除成功")
except Exception as e:
    print(e)
    print("删除失败")
    con.rollback()
finally:

    #关闭连接
    con.close()

