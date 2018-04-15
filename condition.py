#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/15 21:44
# @Author  : Lucas Ma
# @Site    : 
# @File    : condition.py
# @Software: PyCharm


age = 20
if age >= 18:
    print('your age is', age)
    print('adult')


age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

x = '212'
if x:
    print('True')