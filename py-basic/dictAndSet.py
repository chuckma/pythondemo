#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/10 下午11:26
# @Author  : Lucas Ma
# @File    : discAndSet


d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Bob'])

print(d.get('Michael'))
d.pop('Bob')
print(d)

# 要创建一个set，需要提供一个list作为输入集合 key不能重复
s= set([1,2,3,4])
print(s)

# 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果：
s.add(5)
print(s)

# 通过remove(key)方法可以删除元素：
s.remove(1)
print(s)


# 重复元素在set中自动被过滤：
s = set([1, 1, 2, 2, 3, 3])

print(s)

