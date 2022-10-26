#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2/24/22 6:59 PM 
# @Author : huff 
# @File : 读取csv文件.py 
# @Software: PyCharm

import csv


def solution():
    with open("./testAccount.csv", "r", encoding="utf-8") as f:
        temp_csv = csv.reader(f)
        temp_list = []
        for row in temp_csv:
            print(row[3])
            temp_list.append(row[3])
        print(temp_list)
        temp_list.remove(temp_list[0])
        print(temp_list)
        max_count = 1
        for i in range(len(temp_list)):
            if temp_list.count(temp_list[i]) > max_count:
                max_count = temp_list.count(temp_list[i])
                max_addr = temp_list[i]
        return max_count,max_addr


if __name__ == "__main__":
    re = solution()
    print(re)
