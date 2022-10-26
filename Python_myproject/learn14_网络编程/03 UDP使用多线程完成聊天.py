#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-07-04 16:24 
# @Author : huff 
# @File : 03 UDP使用多线程完成聊天.py 
# @Software: PyCharm

#导入模块
from  socket import *
from threading import Thread

#创建套接字对象
udp_socket = socket(AF_INET,SOCK_DGRAM)

#绑定本机和端口
udp_socket.bind(('',8990))

#接收
def recv_fun():
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print('>>%s:%s'%(recv_data[1],recv_data[0].decode('gb2312')))

#发送
def send_fun():
    while True:
        addr = ('192.168.121.1',8080)
        data = input('<<:')
        udp_socket.sendto(data.encode('gb2312'),addr)

if __name__ == '__main__':
    #创建两个线程
    t1 = Thread(target=send_fun)
    t2 = Thread(target=recv_fun)
    t1.start()
    t2.start()
    t1.join()
    t2.join()