# -*- coding: utf-8 -*-
#python 关于装饰器（Decorator）的demo

def log(func):
	def wrapper(*args,**kw):
		print('call %s():' % func.__name__)
		return func(*args,**kw)
	return wrapper
	
@log
def now():
	print('2016-01-13')	
	
#now = log('execute')(now)
now()
print(now.__name__)