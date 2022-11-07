# -*- coding: utf-8 -*-
# @author: baiwenhui
# @email: 19241106@bjtu.edu.cn
# @date: 2022/10/27

"""
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
"""


def yanghui(row):
    a = [1]
    iter = 1
    while iter <= row:
        yield a
        tmp = []
        for i in range(len(a)):
            if i == 0:
                tmp.append(1)
            else:
                tmp.append(a[i - 1] + a[i])
        tmp.append(1)
        a = tmp
        iter += 1
    return 'done'


g = yanghui(10)
while True:
    try:
        print(next(g))
    except StopIteration as e:
        print('func return: ', e.value)
        break
print(g)