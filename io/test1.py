# -*- coding: utf-8 -*-
# @author: baiwenhui
# @email: 19241106@bjtu.edu.cn
# @date: 2022/10/28
import json

obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)

print(s)
