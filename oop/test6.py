# -*- coding: utf-8 -*-
# @author: baiwenhui
# @email: 19241106@bjtu.edu.cn
# @date: 2022/10/28
class Mymeta(type):

    def __new__(cls, *args, **kwargs):
        print('type 调用了 Mymeta 的 new 方法--生成一个空对象，即 People 类')
        "这里调用的是 type 的 new 方法,传入参数需要注意全部传会 type 元类"
        return super().__new__(cls, *args, **kwargs)

    def __init__(self, class_name, class_bases, class_dic):
        print('初始化这个对象--- People 类，给 People 类添加额外的功能')
        super(Mymeta, self).__init__(class_name, class_bases, class_dic)  # 重用父类的功能
        # 自定义的类的功能
        if not class_name.istitle():
            raise TypeError('类名%s请修改为首字母大写' % class_name)

        if '__doc__' not in class_dic or len(class_dic['__doc__'].strip(' \n')) == 0:
            raise TypeError('类中必须有文档注释，并且文档注释不能为空')

    # 传入 Mymeta的参数：People, 以及传入People的参数
    def __call__(self, *args, **kwargs):
        """
        self---<class '__main__.People'>
        :param args: (1,)
        :param kwargs: {'y': 2}
        :return: 返回最终初始化好的代码
        """
        print('调用了 Mymeta 的 call 方法')
        # 调用 People 类里的 __new__方法，生成空对象
        People_obj = self.__new__(self, *args, **kwargs)
        # 调用 People 类里的 __init__方法，初始化空对象,注意：第一个传入的参数是生成好的空对象
        self.__init__(People_obj, *args, **kwargs)
        # 给 People 类生成的对象 obj 添加额外的功能
        print("给 People 类生成的对象 obj 添加额外的功能")
        People_obj.__dict__["新增一个属性"] = None
        # 返回初始化好的对象
        return People_obj


class People(metaclass=Mymeta):
    """People 类的注释"""

    # 产生 People 类真正的对象
    def __new__(cls, *args, **kwargs):
        # 在这里就可以定制功能
        print('生成 People 类的空对象')
        print('传入的位置参数', args)
        print('传入的位置参数', kwargs)
        # 调用所继承的父类的__new__方法，这里就是 object 类,一定要传入 cls(当前这个类)
        "这里要区别于自定义元类的 new 方法，自定义元类调用的是 type 的 new 方法,传入参数是不一样的"
        return super().__new__(cls)

    def __init__(self, x, y=None):
        print("初始化 People 类的对象")
        self.x = x
        self.y = y
        print("初始化 People 类的对象结束")


# 调用People 类生成对象---> People()= Mymeta.__call__()
obj = People(1, y=2)
print('最终的对象字典：', obj.__dict__)
