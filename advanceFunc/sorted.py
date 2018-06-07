#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/7 下午8:58
# @Author  : Lucas Ma
# @File    : sorted

'''
排序算法
'''

# eg.
print(sorted([36, 5, -12, 9, -21]))

# 此外，sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：

print(sorted([36, 5, -12, 9, -21], key=abs))

print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))