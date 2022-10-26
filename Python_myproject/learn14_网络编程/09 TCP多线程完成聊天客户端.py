#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-07-10 17:32 
# @Author : huff 
# @File : 09 TCP多线程完成聊天客户端.py 
# @Software: PyCharm

from socket import *
from threading import Thread

def readMsg(client_socket):
    while True:
        recv_data = client_socket.recv(1024)
        print('收到：',recv_data.decode('utf-8'))

def wirteMsg(client_socket):
    while True:
        msg = input('>')
        msg = user_name+'说：'+msg
        client_socket.send(msg.encode('utf-8'))

#创建客户端套接字对象
client_socket = socket(AF_INET,SOCK_STREAM)
#调用connect连接服务器
client_socket.connect(('192.168.31.184',18878))
user_name = input('请输入用户名:')
#开启一个线程处理当前客户端的读取消息
t = Thread(target=readMsg,args=(client_socket,))
t.start()
#开启一个线程处理客户端的发送消息
t = Thread(target=wirteMsg,args=(client_socket,))
t.start()














