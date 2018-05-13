#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/13 上午11:01
# @Author  : Lucas Ma
# @File    : recurFunc


'''
递归函数
'''

def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)


print(fact(10))
