#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :  17:31 
# @Author  :  Administrator
# @Site    : 
# @File    :  counter_test
# @Software: PyCharm

from collections import Counter

users = ["黎明村", "网吗袜子", "白大华", "二柱子"]
user_counter = Counter(users)  # 统计 list 的 数据，从大到小 Counter 是 dict 的子类
print(user_counter)

str = Counter("sdafasfscxfdsafsf")
str.update("sssssffffff")
print(str)  # 统计字符串
# top n 的问题
print(str.most_common(2))
print(str)
