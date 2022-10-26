#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 1/18/22 11:15 PM 
# @Author : huff 
# @File : 15操作mysql数据库_LB.py 
# @Software: PyCharm

#导入pymysql
import pymysql

# MySQL
MySQL_HOST = "127.0.0.1"
MySQL_PORT = 15434
DATA_BASE = "portfolio-atm"
USER_NAME = "portfolio_atm"
PASS_WORD = "kDUaL1EKra4pnot3zvnA"

class AtmMysql:
    """mysql类"""
    def __init__(self):
        self.host = MySQL_HOST
        self.port = MySQL_PORT
        self.database = DATA_BASE
        self.username = USER_NAME
        self.password = PASS_WORD
        # 创建连接
        self.con = pymysql.connect(host=self.host, user=self.username, password=self.password,database=self.database, port=self.port)
        # 创建游标对象
        self.cur = self.con.cursor()

    def execute(self, sql, condition):
        try:
            # 执行sql
            self.cur.execute(sql, condition)
            # 处理结果集
            result = self.cur.fetchone()
            # 提交事务
            self.con.commit()
            # print("执行成功")
            return result
        except Exception as e:
            print(e)
            self.con.rollback()
            # print("插入失败")

    def db_close(self):
        # 关闭连接
        self.con.close()

    def query_atm(self):
        pass

if __name__ == '__main__':
    mysql = AtmMysql()
    # sql语句
    #sql = "select * from bank_bills where id='%(id)s'"
    #re = mysql.execute(sql,{"id": 1665})
    sql = "select * from bank_bills where currency=%s "  # member_id='%(member_id)s' and and amount='%(amount)s' and balance='%(balance)s'
    re = mysql.execute(sql,('HKD'))  # "member_id": self.member_id,  "amount": self.amount, "balance": self.balance}
    print(re)
    print(re[5])
    mysql.db_close()
