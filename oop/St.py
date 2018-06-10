#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/10 下午12:05
# @Author  : Lucas Ma
# @File    : St


from student import Student

student = Student()
student.print_file()
student.set_name('dggdgagdasg')

# 私有变量无法访问
# print(student.__name)
# 设置get 方法访问
print(student.get_age())
print('改变后的 name：' + student.get_name())

# __name 双下换线开头的实例变量不是一定不能从外部访问 ，python解释器只是将 __name 改变成了 _Student__name
print(student._Student__name)
