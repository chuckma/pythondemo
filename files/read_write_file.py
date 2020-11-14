#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/13 22:54
# @Author  : Lucas Ma
# @File    : read_file

# IO 相关
# 文件读写操作


# 读文件
f = open('/Users/lucasma/PycharmProjects/pythondemo/files/a', 'r')
print(f.read())
f.close()

try:
    f = open('/Users/lucasma/PycharmProjects/pythondemo/files/a', 'r')
    print(f.read())
finally:
    if f:
        f.close()

# 上面的这段代码太繁琐了 python 引入了 with 可以简化上面的写法，而且还不用 f.close()
# 下面这段代码和 上面的 try ... finally 是一样的
with open('/Users/lucasma/PycharmProjects/pythondemo/files/a', 'r') as f:
    print(f.read())

# 写文件，写文件和读文件的相同的是都需要打开文件，但是打开后的操作不一样，读是 'r', 写可以用 'w' or 'wb'
# 像下面的这段代码一样
# with open('/Users/lucasma/PycharmProjects/pythondemo/files/b', 'w') as f:
#     f.write("我是刚刚写入的数据 fff")

# w 这种写入方式会删除已经存在的数据并重新写入，要想不用删除 可以使用 a 的方式 a 是 append 的缩写
# 表示追加到末尾。


with open('/Users/lucasma/PycharmProjects/pythondemo/files/b', 'a') as f:
    f.write("我是刚刚写入的数据 fff")
