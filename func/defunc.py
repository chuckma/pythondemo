#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/11 下午8:33
# @Author  : Lucas Ma
# @File    : defunc


# 自定义函数
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-9))


# 如果想定义一个什么事也不做的空函数，可以用pass语句：为了不使语法报错， 可以使用pass ，如果你还没有想好怎么写函数的代码，
# 可以先放一个pass，

def nop():
    pass


import math


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

res = move(100, 100, 60, math.pi / 6)
print(res)