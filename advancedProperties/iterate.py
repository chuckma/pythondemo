#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/14 下午9:45
# @Author  : Lucas Ma
# @File    : iterate


d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)

for v in d.values():
    print(v)

# 由于字符串也是可迭代对象，因此，也可以作用于for循环：
for ch in 'abcdefg':
    print(ch)

from collections import Iterable
print(isinstance('abc', Iterable))


for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x,y)
