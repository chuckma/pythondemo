#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/11 下午8:33
# @Author  : Lucas Ma
# @File    : defunc


# 自定义函数
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-9))


# 如果想定义一个什么事也不做的空函数，可以用pass语句：为了不使语法报错， 可以使用pass ，如果你还没有想好怎么写函数的代码，
# 可以先放一个pass，

def nop():
    pass


import math


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


res = move(100, 100, 60, math.pi / 6)
print(res)


# 函数的参数

def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(5, 3))


# 计算  a*a + b*b + c*c
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc([1, 2, 3]))

'''
利用可变参数修改上面的函数
定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。
在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数：
'''


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc(1, 2, 4))
print(calc(2))
print(calc())

'''
如果已经有一个list或者tuple，要调用一个可变参数怎么办？可以这样做：
在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去 最常见的写法
'''
nums = [1, 2, 3]
print(calc(*nums))

'''
关键字参数
可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。请看示例：
'''


def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person('lucas', '24')

# 传入人一个关键字参数

person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')

# 和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去：
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])

'''
 命名关键字参数
 对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查。
 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
'''


def person(name, age, *, city, job):
    print(name, age, city, job)


person('Jack', 24, city='Beijing', job='Engineer')


# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def person(name, age, *args, city, job):
    print(name, age, args, city, job)


'''
在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
'''


def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
