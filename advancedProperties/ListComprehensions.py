#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/14 下午9:57
# @Author  : Lucas Ma
# @File    : ListComprehensions


# 列表生成式
print(list(range(1,11)))

y = [x * x for x in range(1,11)]
print(y)

import os
xx = [d for d in os.listdir('.')]
print(xx)