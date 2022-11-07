# -*- coding: utf-8 -*-
# @author: baiwenhui
# @email: 19241106@bjtu.edu.cn
# @date: 2022/10/27

def fib(max_iter):
    n, a, b = 0, 0, 1
    while n < max_iter:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'


g = fib(6)
while True:
    try:
        print(next(g))
    except StopIteration as s:
        print('generation return value: ', s.value)
        break
