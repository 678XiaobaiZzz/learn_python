# -*- coding: utf-8 -*-
# @author: baiwenhui
# @email: 19241106@bjtu.edu.cn
# @date: 2022/10/27


# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量
# 如果一定要引用循环变量怎么办？
# 方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变
# 使用闭包时，对外层变量赋值前，需要先使用nonlocal声明该变量不是当前函数的局部变量

# 利用闭包返回一个计数器函数，每次调用它返回递增整数：
def createCounter():
    x = 0

    def counter():
        nonlocal x
        x += 1
        return x

    return counter


f = createCounter()
for i in range(5):
    print(f())
