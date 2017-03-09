#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#这是注释
a=input('请输入：')
b = len(a.encode('utf-8'))
if b > 10:
	print('大于10',b)
else:
	print(b)
c = input('请再次输入：')
print('您刚才输入的是：%s'%(c))