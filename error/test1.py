# -*- coding: utf-8 -*-
# @author: baiwenhui
# @email: 19241106@bjtu.edu.cn
# @date: 2022/10/28


# 凡是用print()来辅助查看的地方，都可以用断言（assert）来替代

import logging

# 这就是logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别
# 当我们指定level=INFO时，logging.debug就不起作用了
# 同理，指定level=WARNING后，debug和info就不起作用了
logging.basicConfig(level=logging.INFO)
s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)
