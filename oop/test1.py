# -*- coding: utf-8 -*-
# @author: baiwenhui
# @email: 19241106@bjtu.edu.cn
# @date: 2022/10/28
from types import MethodType


# MethodType可以给实例对象或类绑定方法
class Student:
    pass


def set_age(self, age):
    self.age = age


s = Student()
# 给一个实例绑定的方法，对另一个实例是不起作用的
s.set_age = MethodType(set_age, s)
s.set_age(25)

Student.set_age = set_age
s1 = Student()
s1.set_age(20)


# Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性
# __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
# 若在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__
class Person:
    __slots__ = ('name', 'age')  # 只能添加'name', 'age'的属性了

