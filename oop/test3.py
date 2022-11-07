# -*- coding: utf-8 -*-
# @author: baiwenhui
# @email: 19241106@bjtu.edu.cn
# @date: 2022/10/28
from time import localtime
from time import time

now = localtime(time())


class Student:
    def get_score(self):
        return self.score

    def set_score(self, score):
        if not isinstance(score, int):
            raise ValueError('score must be int')
        elif score < 0 or score > 100:
            raise ValueError('score must be 0~100')
        else:
            self.score = score


# 把一个getter方法变成属性，只需要加上@property就可以了
class Person:
    @property
    def birth(self):
        return self.__birth

    @property
    def age(self):
        return now[0] - self.__birth

    @birth.setter
    def birth(self, value):
        if not isinstance(value, int):
            raise ValueError
        if value < 0 or value > 100:
            raise ValueError
        self.__birth = value


# 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution
class Screen(object):
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def resolution(self):
        return self.__width * self.__height


# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
