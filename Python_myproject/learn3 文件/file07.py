#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-06-18 22:42 
# @Author : huff 
# @File : file07.py 
# @Software: PyCharm

import csv

with open("dd.csv","r",encoding="utf-8") as f:
    a_csv = csv.reader(f)
    #print(list(a_csv))
    for row in a_csv:
        print(row)

with open("ee.csv","w") as f:
    b_csv = csv.writer(f)
    b_csv.writerow(["ID","姓名","年龄"])
    b_csv.writerow(["1001","二二","19"])

    c = [["1002","小男","3"],["1003","小小","8"],["1004","大大","19"]]
    b_csv.writerows(c)