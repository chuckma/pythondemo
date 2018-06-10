#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/10 上午11:09
# @Author  : Lucas Ma
# @File    : hello

' a test module'

__author__ = 'Lucas Ma'

import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')


if __name__ == '__main__':
    test()
