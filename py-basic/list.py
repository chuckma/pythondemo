#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/15 21:17
# @Author  : Lucas Ma
# @Site    : 
# @File    : list.py
# @Software: PyCharm


classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print(len(classmates))
print(classmates[0])
print(classmates[-1])

# 末尾插入
classmates.append('Adam')
print(classmates)

# 指定位置插入
classmates.insert(1, 'Jack')
print(classmates)

# 刪除末尾
classmates.pop()
print(classmates)

# 删除指定位置
classmates.pop(1)
print(classmates)

# 修改指定元素
classmates[1] = 'Sarah'
print(classmates)


# 不同类型

L = ['Apple', 123, True]
print(L)


s = ['python', 'java', ['asp', 'php'], 'scheme']
print(s)



# tuple 元组
classmates = ('Michael', 'Bob', 'Tracy')
print(classmates)

# 空 tuple
t = ()

# 定义只有一个元素的 tuple
a = (1,)
print(a)
print(type(a))