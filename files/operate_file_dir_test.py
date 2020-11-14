#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/14 10:20
# @Author  : Lucas Ma
# @File    : operate_file_dir_test


# 操作文件和目录
# python 内置的 os 模块可以直接调用操作系统提供的接口函数

import os

# 输出操作系统类型，如果是 posix 说明系统是 Linux，Unix， macOS 如果是 nt 就是 windows
print(os.name)
# 获取详细的系统信息 调用 uname 函数 , uname 函数在 windows 上不提供
print(os.uname())


# 操作文件和目录的函数一部分放在 os 模块中，一部分放在 os.path 中。
# 查看当前目录的绝对路径
print(os.path.abspath('.'))
# 在某个目录下创建一个新的目录，首先吧新目录的完整路径表示出来
# print(os.path.join('/Users/lucasma/PycharmProjects/pythondemo/files', 'testdir'))

# 创建一个 文件夹
# os.mkdir('/Users/lucasma/PycharmProjects/pythondemo/files/testdir')
# 删除一个 文件夹
# os.rmdir('/Users/lucasma/PycharmProjects/pythondemo/files/testdir')


# 拆分路径
print(os.path.split('/Users/lucasma/PycharmProjects/pythondemo/files/a'))
# 获取文件扩展名
print(os.path.splitext('/io/bytes_io_test.py')[1])