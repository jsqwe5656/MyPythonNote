#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'关于使用@property的demo'

__author__ = 'zbf'

class Student(object):
	
	@property		#相当于get_score  property意义在于调用的时候直接将score变成属性 而不是需要通过get取值
	def score(self):
		return self._score
		
	@score.setter	#相当于set_score，如果不写入这个方法相当于属性只可读不可写
	def score(self,value):
		if not isinstance(value,int):
			raise ValueError('score must be int')
		if value < 0 or value > 100:
			raise ValueError('wrong value,value must betton 1-100')
		self._score = value
		
	@property
	def birth_year(self):
		return self._birth_year
		
	@birth_year.setter
	def birth_year(self,num):
		self._birth_year = num
	
	@property
	def age(self):
		return 2017 - self._birth_year
		