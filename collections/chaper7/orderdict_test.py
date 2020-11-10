#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :  17:42 
# @Author  :  Administrator
# @Site    : 
# @File    :  orderdict_test
# @Software: PyCharm

from collections import OrderedDict

'''
    OrderedDict 是有序的， 按照添加的顺序加入 dict
    1. python3 里 dict 默认是有序的。python2 一下 dict 不是有序的。
    2. 既然py3 里 dict 已经是有序的了，还有必要使用 OrderedDict 吗，答案是有必要。 OrderedDict 还有一些其他的方法 
'''
user_dict = OrderedDict()

user_dict["a"] = "userA"
user_dict["c"] = "userC"
user_dict["b"] = "userB"
print(user_dict.move_to_end("a"))  # 移动指定元素到末尾
print(user_dict)
print(user_dict.pop("c"))  # 删除dict指定的key值 并返回值
print(user_dict.popitem())  # 删除末尾的 元素
print(user_dict)
