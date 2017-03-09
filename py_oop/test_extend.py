#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'a test for extends'

__author__ = 'zbf'

class Animal(object):
	def run(self):
		print('animal is running...')
		
class Dog(Animal):
	def run(self):
		print('dog is running..')

class Cat(Animal):
	def run(self):
		print('cat is running..')

dog = Dog()
dog.run()

cat = Cat()
cat.run()