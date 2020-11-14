#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/14 12:00
# @Author  : Lucas Ma
# @File    : process_test1

import os

# print('Process (%s) start ...' % os.getppid())
# pid = os.fork()
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

# 注意 windows 下 没有 fork 调用 上段代码无法在 win 下运行


# multiprocessing 模块提供了一个 Process 来代表进程对象 ，下面演示启动一个子进程并等待期结束
from multiprocessing import Process


# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')

# 创建子进程时，只需要传入一个执行函数和函数的参数，创建一个 Process 实例，用 start() 方法启动，这样创建进程比 fork'() 简单
# join 方法可以等待子进程结束后再继续往下运行，通常用于进程之间的同步

# Pool 如果要启动大量的子进程，可以使用 进程池的方式批量创建子进程

