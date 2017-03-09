#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'zbf'

class Fib(object):
	def __init__(self):
		self.a,self.b = 0,1		#初始化两个值
	def __iter__(self):
		return self				#实例本身就是迭代对象，所以返回自己
	def __next__(self):
		self.a,self.b = self.b,self.a + self.b	#计算下一个值
		if self.a >	100000:						#设置退出循环条件
			raise StopIteration()
		return self.a							#返回下一个数
	def __getitem__(self,n):
		if isinstance(n,int):					#n是索引
			a,b = 1,1
			for x in range(n):
				a,b = b,a+b
			return a
		if isinstance(n,slice):					#n是切片
			start = n.start
			stop = n.stop
			if start is None:
				start = 0
			a,b = 1,1
			L = []
			for x in range(stop):
				if x>= start:
					L.append(a)
				a,b = b,a+b
			return L		
	def __getattr__(self,attr):
		if attr == 'name'
			return	'i am Fib'
		return AttributeError('\'Fib\' object has no attribute \'%s\'' %attr)
	def __call__(self):
		print('this is fib object')
			
#for n in Fib():
#	print(n)
f = Fib()
print(f[10])
print(f[:10])
#print(f[:10:2])




























