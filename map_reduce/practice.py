# -*- coding: utf-8 -*-
# @author: baiwenhui
# @email: 19241106@bjtu.edu.cn
# @date: 2022/10/27

from functools import *


# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：

def standard(s):
    tmp = ''
    for i in range(len(s)):
        if i == 0:
            tmp += s[i].upper()
        else:
            tmp += s[i].lower()
    return tmp


result = list(map(standard, ['adam', 'LISA', 'barT']))
print(result)


# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积
# [3, 5, 7, 9] 945
def prod(x, y):
    return x * y


result = reduce(prod, [3, 5, 7, 9])
print(result)

# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def fn(x, y):
    return 10 * x + y


def char2num(c):
    return DIGITS[c]


def str2int(s):
    rs = reduce(fn, map(char2num, s))
    return rs


def str2float(s):
    s = s.split('.')
    print(s[0])
    print(s[1])
    rs = str2int(s[0]) + str2int(s[1]) * pow(10, -len(s[1]))
    return rs


print(str2float('123.45678'))
