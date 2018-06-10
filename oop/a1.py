#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/10 下午2:21
# @Author  : Lucas Ma
# @File    : a1


class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    print('Dog is barking')

    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')


class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')



