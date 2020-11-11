#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/11 21:09
# @Author  : Lucas Ma
# @File    : chain_map_test


from collections import ChainMap

user_dict1 = {
    "a": "李明明",
    "b": "网红",
}

user_dict2 = {
    "c": "三哥",
    "d": "sisal"
}
# ChainMap 可以将 dict 连接起来
new_dict = ChainMap(user_dict1, user_dict2)

for key, value in new_dict.items():
    print(key, value)

print("-------分割线----------")
# 如果是相同的key 就出输出第一个key  比如下面的

user_dict3 = {
    "a": "李明明",
    "b": "网红",
}

user_dict4 = {
    "b": "三哥",
    "d": "sisal"
}
new_dict1 = ChainMap(user_dict3, user_dict4)
for key, value in new_dict1.items():
    print(key, value)

# ChainMap 动态的添加数据,需要注意的是 new_child 不会改变 ChainMap 而是返回一个新的 ChainMap
dict2 = new_dict1.new_child({"aa": "aaaa", "bb": "bbbbb"})
print(dict2)

# ChainMap 的 maps 方法不是 user_dict4 user_dict3  的拷贝，而是指向 它们
# 这里修改它们，元数据也会改变，所以 ChainMap 的好处就是能让我们访问多个 dict 就像访问一个
# dict一样的方便。
print(dict2.maps)
dict2.maps[0]["aa"] = "我改变了吗"
print(dict2)

# for key, value in user_dict1.items():
#     print(key, value)
#
# for key, value in user_dict2.items():
#     print(key, value)
