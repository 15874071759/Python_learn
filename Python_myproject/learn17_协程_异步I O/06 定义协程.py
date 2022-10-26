#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-07-22 22:17 
# @Author : huff 
# @File : 06 定义协程.py 
# @Software: PyCharm

import asyncio,time
now = lambda :time.time()
#使用async来修饰一个函数，则该函数就称为一个协程对象
async def do_work(x):
    print('waiting:',x)

#调用协程
start = now()
#1.创建事件循环
loop = asyncio.get_event_loop()
#2.将协程对象加入到事件循环中
loop.run_until_complete(do_work(3))
print('TIME:',now()-start)