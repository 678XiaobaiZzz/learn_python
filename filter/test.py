# -*- coding: utf-8 -*-
# @author: baiwenhui
# @email: 19241106@bjtu.edu.cn
# @date: 2022/10/27


# 和map()类似，filter()也接收一个函数和一个序列。
# 和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

def _odd_iter():
    n = 1
    while True:
        n += 2
        # 从3开始, 产生3、5、7……等的迭代器
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列


for i in primes():
    if i <= 20:
        print(i)
    else:
        break
