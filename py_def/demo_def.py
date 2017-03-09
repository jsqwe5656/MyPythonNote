# -*- coding: utf-8 -*-
#python函数小demo
def my_abs(x):
	#添加参数检查使用内置函数
	if not isinstance(x,(int,float))
		raise TypeError('bad operand type')
	if x>=0:
		return x
	else:
		return -x
#print(my_abs(1))
