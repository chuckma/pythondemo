#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/13 上午11:22
# @Author  : Lucas Ma
# @File    : slice
#

# slice demo

# 取一个list或tuple的部分元素是非常常见的操作。比如，一个list如下：
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# 取 L 的前三个元素 0，1，2
print(L[:3])

# 取倒数两个元素
print(L[-2:])

# 取倒数第二个元素

print(L[-2:-1])

# 创建一个0-99 的数列

L1 = list(range(100))
print(L1)

# 取前十
print(L1[:10])

# 取后十个数

print(L1[-10:])

# 取 10 -20

print(L1[10:20])

# 前10个数，每两个取一个：
print(L1[:10:2])

# 所有 每 5个数取一个
print(L1[::5])

# 复制
print(L1[:])


# tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：
print((0, 1, 2, 3, 4, 5)[:3])

print('ABCDEFG'[:3])