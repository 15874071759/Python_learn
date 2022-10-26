#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-07-26 22:13 
# @Author : huff 
# @File : 10 asyncio实现并发.py 
# @Software: PyCharm

import asyncio,time

async def do_work(x):
    print('waiting:',x)
    await asyncio.sleep(x)
    return 'Done after {}s'.format(x)

start = time.time()
#创建多个协程对象
coroutine1 = do_work(1)
coroutine2 = do_work(2)
coroutine3 = do_work(4)

#创建任务列表
tasks = [
    asyncio.ensure_future(coroutine1),
    asyncio.ensure_future(coroutine2),
    asyncio.ensure_future(coroutine3)
]

#将任务列表注册到事件循环中
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

#获取返回的结果
for task in tasks:
    print('Task reslut: ',task.result())
print('TIME:',time.time()-start)


