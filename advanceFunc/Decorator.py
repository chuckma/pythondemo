#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/8 下午9:32
# @Author  : Lucas Ma
# @File    : Decorator

# 装饰器
# 在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）


# 打印日志
import time


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper

@log
def now():
    print(time.strftime('%Y-%m-%d', time.localtime(time.time())))


print(now())
