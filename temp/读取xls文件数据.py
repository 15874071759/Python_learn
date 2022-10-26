#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2/24/22 3:26 PM 
# @Author : huff 
# @File : 读取xls文件数据.py 
# @Software: PyCharm

import xlrd

def solution():
    wb = xlrd.open_workbook("testAccount.xls")
    sh = wb.sheet_by_name("Sheet1")
    data = {}
    data_list = []
    for i in range(1,sh.nrows):
        print(sh.row_values(i)[3])
        data_list.append(sh.row_values(i)[3])
    print(data_list)
    max_count = 1
    max_data = ""
    for j in data_list:
        if data_list.count(j) > max_count:
            max_count = data_list.count(j)
            max_data = j
    return max_data,max_count
        # for j in range(sh.ncols):
        #     data[sh.row_values(0)[j]] = sh.row_values(i)[j]
        # data_temp = data.copy()
        # data_list.append(data_temp)
    # print(data_list)




if __name__ == '__main__':
    re = solution()
    print(re)