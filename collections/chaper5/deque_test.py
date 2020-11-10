#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :  16:35 
# @Author  :  Administrator
# @Site    : 
# @File    :  deque_test
# @Software: PyCharm

#  双向队列
from collections import deque

# 注意：deque 和 list 尽量保持相同类型的数据
# deque 线程安全 list 线程不安全。
# deque 初始化的时候可以看到 __init__ 函数有个参数 iterable()
# iterable 是可以迭代的对象，那我们就可以使用 tuple or list 来初始化它
user_name = deque(("liming", "wangs"))
user_name1 = deque(["liming", "wangs"])
print(user_name)
print(user_name1)
# 还可以用 dict 初始化它
user_name2 = deque({
    "name1": "tony",
    "name2": "lucas"

})
print(user_name2)

#  deque 常用方法的使用
user_name.append("新增加的")  # 增加到列尾
print(user_name)
user_name.appendleft("增加到 deque 左边了")  # 增加到列头
print(user_name)
print(user_name.count("liming"))  # 统计deque 元素的数量

print(user_name.index("新增加的", 0, 4))  # 查询指定元素的索引位置，从 start - stop 之间查询

user_name.insert(2, "我是插入指定位置的元素")  # i 表示插入到队列的位置，后面的元素依次往后移动
print(user_name)

print(user_name.popleft(), user_name)  # 在 deque 的左边取出一个元素

user_name.remove("liming")  # 移除指定的元素
print(user_name)
user_name.extend(("扩展1", "扩展2", "扩展3"))  # 在 deque 的右边扩展一个迭代对象 可以认为是直接插入一个 迭代对象，这里放了一个 tuple
print(user_name)
user_name.reverse()  # 将队列倒叙输出
print(user_name)

user_name.clear()  # 清空 deque
print(user_name)
