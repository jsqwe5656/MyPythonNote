#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

def serach_fire(firename):
	dir = 'c:'
	for root,dirs,files in os.walk(dir):
		for file in files:
			if firename in file:
				path = os.path.join(root,file)
				replath = os.path.replath(path,dir)
				print(replath)

if __name__ == '__main__':
	str = input('请输入要查询的字段:')
	serach_fire(str)

