#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :  14:04 
# @Author  :  Administrator
# @Site    : 
# @File    :  namedtuple_test
# @Software: PyCharm

from collections import namedtuple

'''
    可以通过 namedtuple 生成一个类
    namedtuple
    优点：
    1. 节省空间
    2. 拥有tuple 好用的特型 
'''
User = namedtuple("User", ["name", "age", "height", "edu"])
user = User("mcg", 24, 170, "ok")
print(user.name, user.age, user.height)
user = User._make(["dsafdas", 12, 178, "hh"])
print(user)

user_tuple = ('zsd', 22, 188)
print(User(*user_tuple, edu="master"))

# 修改对象属性，注意要使用"_replace"方法
user = user._replace(age=22)
print(user)

# 将User对象转换成字典，注意要使用"_asdict"
print(user._asdict())
user1 = user._asdict().copy()
print(user1)
