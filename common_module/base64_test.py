#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/14 21:12
# @Author  : Lucas Ma
# @File    : base64_test


# Base64 是一种用 64 个字符来表示任意二进制数据的方法

import base64

print(base64.b64encode(b'MVP9060'))
print(base64.b64decode(b'TVZQOTA2MA=='))