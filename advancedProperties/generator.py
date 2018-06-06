#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/14 下午10:49
# @Author  : Lucas Ma
# @File    : generator


# 生成器

g = (x * x for x in range(10))

for n in g:
    print(n)