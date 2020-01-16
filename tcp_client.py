"""
tcp客户端流程
"""
from socket import *
import time
import random

# 默认情况就是tcp套接字
sockfd = socket()

# 连接服务器
server_addr = ('127.0.0.1',8888)
sockfd.connect(server_addr)

# 发收消息
while True:
    time.sleep(random.randint(3,8))
    msg = "客户端错误"
    sockfd.send(msg.encode()) # 要发送字节串


sockfd.close()