# -*- coding: utf-8 -*-
# @author: baiwenhui
# @email: 19241106@bjtu.edu.cn
# @date: 2022/10/27


# 此外，sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# rs = sorted(L, key=lambda x: x[0])
rs = sorted(L, key=lambda x: x[1])
print(rs)