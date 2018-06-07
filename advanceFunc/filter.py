#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/7 下午8:46
# @Author  : Lucas Ma
# @File    : filter


'''
Python内建的filter()函数用于过滤序列。
和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，
filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
比如下面 eg . is_odd 函数
'''


def is_odd(n):
    return n % 2 == 1


# 打印结果 [1, 3, 5, 7, 9]
print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9])))


# 把一个序列中的空字符串删掉，可以这么写
def not_empty(s):
    return s and s.strip()


# 打印结果 ['A', 'B', 'C']
print(list(filter(not_empty, ['A', 'B', None, ' ', 'C'])))

'''
filter()的作用是从一个序列中筛出符合条件的元素。
由于filter()使用了惰性计算，所以只有在取filter()结果的时候，才会真正筛选并每次返回下一个筛出的元素。
'''
