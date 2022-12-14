# -*- coding: utf-8 -*-
# @author: baiwenhui
# @email: 19241106@bjtu.edu.cn
# @date: 2022/10/28
class Sample:
    def __enter__(self):
        print("in __enter__")

        return "Foo"

    def __exit__(self, exc_type, exc_val, exc_tb):
        # exc_type：　错误的类型
        # exc_val：　错误类型对应的值
        # exc_tb：　代码中错误发生的位置
        print("in __exit__")


def get_sample():
    return Sample()


with get_sample() as sample:
    print("Sample: ", sample)
    print('执行完毕')
