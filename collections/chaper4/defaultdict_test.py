#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :  15:35 
# @Author  :  Administrator
# @Site    : 
# @File    :  defaultdict_test
# @Software: PyCharm


from collections import defaultdict

# dict 字典是另一种可变容器模型，且可存储任意类型对象。

user_dict = {}
users = ['a1', 'b1', 'b1', 'b2', 'a3', 'a4']
# 下面这段代码 循环代码在复杂逻辑下不太好
# for user in users:
#     if user not in user_dict:
#         user_dict[user] = 1
#     else:
#         user_dict[user] += 1
# 上面的代码可以这样写
for user in users:
    user_dict.setdefault(user, 0)
    user_dict[user] += 1
    print(user_dict)

# 上面这段代码还可以用 defaultdict 优化  defaultdict 传递可调用对象
default_dict = defaultdict(int)
users2 = ['a1', 'b1', 'b1', 'b2', 'a3', 'a4']
for user in users2:
    default_dict[user] += 1
pass
