#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/14 10:12
# @Author  : Lucas Ma
# @File    : bytes_io_test

# StringIO 操作的只能是 str，如果要操作二进制数据，就需要使用 BytesIO
# BytesIO 实现了在内存中读写 bytes, 创建一个 BytesIO, 写入一些bytes

from io import BytesIO

f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())
# ！！！注意！！！ 写入的不是 str ，而是 经过utf-8 编码的 bytes

# 和 StringIO 类似， BytesIO 的读取也是先用 bytes 初始化一个 BytesIO
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())
