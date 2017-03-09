# -*- coding: utf-8 -*-
#python 关于reduce的demo
from functools import reduce

#def ji(x,y):
#	return x*y
#lambda 匿名函数
def prod(L):
	return reduce(lambda x,y: x*y,L)

print('3*5*7*9=',prod([3,5,7,9]))