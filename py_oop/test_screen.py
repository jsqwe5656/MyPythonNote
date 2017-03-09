#!/usr/bin/env python3
#-*- coding: utf-8 -*-

class Screen(object):

	@property
	def width(self):
		return self._width
	
	@width.setter
	def width(self,value):
		if not isinstance(value,int):
			raise ValueError('value must be int')
		self._width = value
		
	@property
	def height(self):
		return self._height
	
	@height.setter
	def height(self,value):
		if not isinstance(value,int):
			raise ValueError('value must be int')
		self._height = value
	
	@property
	def resolution(self):
		return self.width*self.height
		
s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
#assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution