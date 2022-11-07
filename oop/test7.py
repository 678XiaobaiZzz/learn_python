# -*- coding: utf-8 -*-
# @author: baiwenhui
# @email: 19241106@bjtu.edu.cn
# @date: 2022/10/28


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def change(obj):
    obj.name = 'change' + obj.name
    obj.age = 10 + obj.age

p = Person('Henry', 20)
change(p)
print(p.__dict__)
