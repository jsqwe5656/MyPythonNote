# -*- coding: utf-8 -*-
#Python关于装饰器 decorator的另一个例子 引入 functools包
import functools



#个完整的decorator的写法如下
def log(func):
	@functools.wraps(func)
	def wrapper(*args,**kw):
		print('call %s():' %(func.__name__))
		return func(*args,**kw)
	return wrapper

@log
def now():
	print('zbf is the best')
	
now()

#或者是针对带参数的decorator
def log2(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print('%s %s():' %(text,func.__name__))
			return func(*args,**kw)
		return wrapper
	return decorator
	
@log2('haha')
def now():
	print('zbf is the best')
	
now()
	