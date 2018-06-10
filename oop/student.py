#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/10 上午11:51
# @Author  : Lucas Ma
# @File    : student


class Student():
    __name = 'lucas'
    __age = 19

    def print_file(self):
        print('name:' + self.__name)
        print('age:' + str(self.__age))

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name
