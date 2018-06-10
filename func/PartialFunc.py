#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/10 上午11:00
# @Author  : Lucas Ma
# @File    : PartialFunc

# 偏函数

# 自定义
import functools


def int2(x,base=2):
    return int(x,base)

print(int2('1000000'))


# functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2：

int2 = functools.partial(int,base=2)

print(int2('1000000'))

print(int2('1000000', base=10))



