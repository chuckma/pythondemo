#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/10 下午2:23
# @Author  : Lucas Ma
# @File    : test


from .a1 import Dog, Tortoise

dog = Dog()
dog.run()

tortoise = Tortoise()


def run_twice(animal):
    animal.run()
    animal.run()


run_twice(dog)

run_twice(tortoise)
