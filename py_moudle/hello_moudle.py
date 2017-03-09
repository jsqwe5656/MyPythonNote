#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a test moudle'		#是一个字符串，表示模块的文档注释，任何模块代码的第一个字符都被视为模块的文档注释

__author__ = 'zbf'

import sys

def test():
	args = sys.argv
	if len(args) == 1:
		print('hello,world!')
	elif len(args) == 2:
		print('Hello,%s!' %args[1])
	else:
		print('Too many arguments!')
		
if __name__=='__main__':
	test()