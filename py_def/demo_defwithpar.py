# -*- coding: utf-8 -*-
#python关于带参函数的demo
#def power(x):
#	return x*x
#跟java不一样 函数名是唯一的 就算参数不同也会覆盖相同函数名的函数

#默认参数 注：默认参数必须放在后 如果放在前调用的时候会把前面默认参数覆盖掉
def power(x,n = 2):
	s = 1
	while n>0:
		n -=1
		s = s*x
	return s
#print(power(2))
print(power(2))