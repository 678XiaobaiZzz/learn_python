# -*- coding: utf-8 -*-
# @author: baiwenhui
# @email: 19241106@bjtu.edu.cn
# @date: 2022/10/28


# __str__()
# __repr__()
class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Student Object (name: {self.name})'

    __repr__ = __str__


# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法
# 该方法返回一个迭代对象
# Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环
class Fib:
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a >= 100:
            raise StopIteration()
        return self.a

    # 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法
    def __getitem__(self, item):
        if isinstance(item, int):
            a, b = 1, 1
            for x in range(item):
                a, b = b, a + b
            return a
        if isinstance(item, slice):
            start = item.start
            stop = item.stop
            if start is None:
                start = 0
            a, b = 1, 1
            l = []
            for x in range(stop):
                if x >= start:
                    l.append(a)
                a, b = b, a + b
            return l


f = Fib()
print(f[0:5])
