# -*- coding: utf-8 -*-
# @author: baiwenhui
# @email: 19241106@bjtu.edu.cn
# @date: 2022/10/27

def is_odd(n):
    return n % 2 == 1


L = list(filter(is_odd, range(1, 20)))
print(L)

l = list(filter(lambda x: x % 2 == 1, range(1, 20)))
print(l)
