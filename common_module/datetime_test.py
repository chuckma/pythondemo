#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/14 20:59
# @Author  : Lucas Ma
# @File    : datetime_test


# datetime 是 Python 处理日期和时间的标准库

# 获取当前的日期和时间
from datetime import datetime,timedelta

now = datetime.now()
print(now)
print(type(now))

# 获取指定日期和时间
dt = datetime(2020, 11, 14, 20, 30)
print(dt)
# datetime 转换为 timestamp  Python 里timestamp 是一个浮点数
# 整数位表示秒
print(dt.timestamp())

# timestamp 转为 datetime
t = 1605357000.0
print(datetime.fromtimestamp(t))

# str 转为 datetime
cdate = datetime.strptime('2020-11-14 20:30:34', '%Y-%m-%d %H:%M:%S')
print(cdate)
# datetime 转 str
print(datetime.now().strftime('%a, %b %d %H:%M'))

# datetime 加减

