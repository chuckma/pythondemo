#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/14 21:30
# @Author  : Lucas Ma
# @File    : tcp_ip_test

import socket

# 创建一个 socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 连接服务器
s.connect(('www.zhihu.com', 80))
# 发送数据 要求返回首页内容
s.send(b'GET / HTTP/1.1\r\nHost: www.zhihu.com\r\nConnection: close\r\n\r\n')

# 接收数据:
buffer = []
while True:
    # 每次最多接收1k字节:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
s.close()
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 接收的数据写入文件
with open('zhihu.html', 'wb') as f:
    f.write(html)
