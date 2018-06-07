#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/7 下午9:07
# @Author  : Lucas Ma
# @File    : retFunc
'''
返回函数
'''


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)

print(f1())
# 每次返回的都是一个新的函数
print(f1 == f2)
print(f1() == f2())
