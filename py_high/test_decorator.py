# -*- coding: utf-8 -*-
#python关于decorator（装饰器）的练习

import functools

def whoisbest(test):
		
	if test == str(test):
		def decorator(func):
			@functools.wraps(func)		
			def wrapper(*args,**kw):
				print(test,'begin call')
				return func(*args,**kw),print('after call')
			return wrapper
		return decorator
	else:
		func = test
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print('begin call now ')
			return func(*args,**kw),print('after call now ')
		return wrapper

@whoisbest
def now():
	print('zbf is the best!')
	
@whoisbest('who is the best')
def now2():
	print('zbf is always best!')
	
now()
now2()
