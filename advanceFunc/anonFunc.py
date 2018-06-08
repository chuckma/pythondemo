#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/8 下午9:27
# @Author  : Lucas Ma
# @File    : anonFunc

# 匿名函数
# Python对匿名函数的支持有限，只有一些简单的情况下可以使用匿名函数。


# 关键字lambda表示匿名函数，冒号前面的x表示函数参数

print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))


# 用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。
# 此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：

f = lambda x:x*x

print(f(3))