#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#python关于filter（）也就是筛选函数的应用 求素数

def main():
	for n in primes():
		if n<1000:
			print(n)
		else:
			break
#生成间隔为2的自然数
def _odd_iter():
	n = 1
	while True:
		n +=2
		yield n

def _not_dicisible(n):
	return lambda x:x%n>0

def primes():
	yield 2
	it = _odd_iter
	while True:
		n = next(it)
		yield n
		it = filter(_not_dicisible(n),it)

if _name_ == '_main_':
	main()
