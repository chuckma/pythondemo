#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :  11:27
# @Author  :  Administrator
# @Site    :
# @File    :  tuple_test
# @Software: PyCharm

name_tuple = ("boy1", "boy2")

#  tuple 拆包
user_tuple = ("bobb1", 24, 170, "杭州",)
# name, age, height = user_tuple
name, *other = user_tuple

print(name, other)


# tuple 的不可变性不是绝对的
# tuple 最好不要放可变的数据对象，下面的这个数组就是可变的
name_tuple = ("boy2", [2,3],)
name_tuple[1].append(4)
print(name_tuple)
