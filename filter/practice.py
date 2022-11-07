# -*- coding: utf-8 -*-
# @author: baiwenhui
# @email: 19241106@bjtu.edu.cn
# @date: 2022/10/27


# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909
# 请利用filter()筛选出回数：
def is_reverse(x: int):
    tmp = int(str(x)[::-1])
    return tmp == x

rs = list(filter(is_reverse, range(1000)))
print(rs)
