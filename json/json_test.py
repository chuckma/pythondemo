#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/14 11:29
# @Author  : Lucas Ma
# @File    : json_test


# python 内置的 json 模块提供了非常完善的 python 对象到 json 格式的转换

import json

d = dict(name='李明', age=23, score=99)
print(json.dumps(d))

# dumps 方法返回一个 str 内容是标准的 json

json_str = '{"name": "\u674e\u660e", "age": 23, "score": 99}'
# json 反序列化为 python 对象 用loads() 或者 load()
print(json.loads(json_str))


# dumps 直接 转换 class Student 会错误，注意原因是 Student 对象不是一个可以序列化为 json 的对象
# dumps 除了第一个 obj 参数之外还要一堆的可选参数，这些参数就是让我们自己定制 json 序列化
# 可选参数 default 就是把任意一个对象变成一个可序列化为 json 的对象，我们只需要为示例 class Student 专门写一个转换函数
# 再把函数传进去即可

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


s = Student('Bob', 20, 88)


# print(json.dumps(s))


def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


# student 实例首先被 student2dict() 函数转成 dict，然后再被顺利序列化为 json
print(json.dumps(s, default=student2dict))

# 其实其他的类实例也是无法直接 序列化的，我们可以把任意 class 的实例变成 dict
print(json.dumps(s, default=lambda obj: obj.__dict__))


# 如果要把 JSON 反序列化为一个 Student 实例，loads 先转换出一个 dict 对象，然后传入 object_hook 函数
# 负责吧 dict 转换为 Student 实例
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))
