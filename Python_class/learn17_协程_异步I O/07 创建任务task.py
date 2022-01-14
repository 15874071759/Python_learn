#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-07-22 22:34 
# @Author : huff 
# @File : 07 创建任务task.py 
# @Software: PyCharm

import asyncio,time
async def do_work(x):
    print('waiting:',x)

#获取协程对象
coroutine = do_work(3)
#创建事件循环对象
loop = asyncio.get_event_loop()
#创建任务
#task = asyncio.ensure_future(coroutine)
task = loop.create_task(coroutine)
print(task)
print('task是否是future的子类',isinstance(task,asyncio.Future))
#将协程对象注册到事件循环中
loop.run_until_complete(task)
print(task)