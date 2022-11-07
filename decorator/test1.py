# -*- coding: utf-8 -*-
# @author: baiwenhui
# @email: 19241106@bjtu.edu.cn
# @date: 2022/10/27
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log('execute')
def now():
    print('2015-3-25')
