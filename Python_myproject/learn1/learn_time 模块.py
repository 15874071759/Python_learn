#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2/11/22 12:25 PM 
# @Author : huff 
# @File : learn_time 模块.py 
# @Software: PyCharm

import time
import copy


def wait_for_time():
    now = int(time.time())
    print(now)
    wait = 60 - now%60 + 1
    print(wait)
    time.sleep(wait)
    print(time.time())
    return True

def except_learn():
    a = [1,2,3]
    try:
        print(a[3])
    except IndexError as e:
        print(e)
        print(a)
    finally:
        print(a[0])
    return a

if __name__ == "__main__":
    #wait_for_time()
    # print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
    # print(time.localtime())
    # print(type(time.localtime()))
    # import copy
    # a = [1, 2, 3, [4,5]]
    # b = copy.deepcopy(a)
    # b.append(5)
    #
    # b[3].append(5)
    # print(a)
    # print(b)
    print(except_learn())