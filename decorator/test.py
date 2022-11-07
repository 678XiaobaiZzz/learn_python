# -*- coding: utf-8 -*-
# @author: baiwenhui
# @email: 19241106@bjtu.edu.cn
# @date: 2022/10/27


# 现在，假设我们要增强now()函数的功能
# 比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义
# 这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
def log(func):
    def wrapper():
        print(f'call {func.__name__}()')
        return func()

    return wrapper


# 因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。
# 相当于now = log(now)
@log
def now():
    print('2022-10-27')


now()
