#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/10 上午11:51
# @Author  : Lucas Ma
# @File    : Student


class Student():
    name = 'lucas'
    age = 19

    def print_file(self):
        print('name:' + self.name)
        print('age:' + str(self.age))


student = Student()
student.print_file()
