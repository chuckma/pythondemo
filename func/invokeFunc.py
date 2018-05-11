#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/11 下午8:22
# @Author  : Lucas Ma
# @File    : invokeFunc


# 绝对值函数
print(abs(-20))
print(abs(10))
print(abs(10.22))

# max 函数 返回最大的值
print(max(1, 23, 45))

# Python内置的常用函数还包括数据类型转换函数，比如int()函数可以把其他数据类型转换为整数：
print(int('1231'))
print(int(12.456))
print(float('12.22'))
print(str(12.232))
# 只要不为空， bool 转换就为True
print(bool(1))
print(bool(232))
print(bool(-33242))
print(bool(' '))
# bool 0 或者 空 则为 False
print(bool(0))
print(bool(''))