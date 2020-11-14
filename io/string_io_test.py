#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/14 10:04
# @Author  : Lucas Ma
# @File    : string_io_test


from io import StringIO

# 数据的读写不一定是写文件，也可以在内存中读写
# StringIO 顾名思义就是在内存中读写 Str
# str 写入StringIO 需要先创建一个 StringIO，然后想文件写入一样
# getValue() 方法获取写入后的数据
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world')
print(f.getvalue())

# 读取StringIO 可以用一个 str 初始化 StringIO，然后像读文件一样读取
f = StringIO('Hello!\nHi!\nGoodBye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
