#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/14 12:23
# @Author  : Lucas Ma
# @File    : process_test2

# 进程间通信
# multiprocessing 模块包装了底层的机制，提供了 Queue，Pipes 等多种方式来交换数据
# 以Queue 为例，在父进程中创建 2 个子进程，一个往Queue 里写数据，一个从Queue 里读数据
from multiprocessing import Process, Queue
import os, time, random


# 写数据进程执行的代码
def write(q):
    print("进程开始写数据：%s" % os.getpid())
    for value in ['a', 'b', 'c']:
        print('写入 %s 到 queue ...' % value)
        q.put(value)
        time.sleep(random.random())


# 读数据进程执行的代码
def read(q):
    print('进程开始读数据：%s' % os.getpid())
    while True:
        value = q.get(True)
        print('从 queue 获取到 %s' % value)


if __name__ == '__main__':
    # 父进程创建queue，并传给各个子进程
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程 pw 写入
    pw.start()
    # 启动子进程 pr 读取
    pr.start()
    # 等待 pw 结束
    pw.join()
    # pr 进程里是死循环，无法等待期结束，只能强行终止
    pr.terminate()
