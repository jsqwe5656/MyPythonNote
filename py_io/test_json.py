#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

class Student(object):
	def __init__(self,name,age,single):
		self.name = name 
		self.age = age 
		self.single = single

def studentresult(d):
	return Student(d['name'],d['age'],d['single'])
s = Student('zbf',23,True)
s1 = json.dumps(s,default = lambda obj : obj.__dict__)
s2 = json.loads(s1,object_hook = studentresult)				#
print(s2,s2.name,s2.age,s2.single)
