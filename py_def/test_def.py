# -*- coding: utf-8 -*-
#python函数小练习
import math

def quadratic(a,b,c):
	y = b*b-4*a*c
	if y>0:
		x = math.sqrt(y)
		x1 = (-b + x)/(2*a)
		x2 = (-b - x)/(2*a)
		print(x1,x2)
	elif y == 0:
		print('有且只有一个实根,为',quadratic(a,b,c)[0])
	else:
		print('该方程无实根')
print('欢迎来到一元二次方程求解~')
a = int(input('请输入a：'))
if not isinstance(a,(int,float)):
	raise TypeError('只能输入整数或者小数')
b = int(input('请输入b：'))
if not isinstance(b,(int,float)):
	raise TypeError('只能输入整数或者小数')
c = int(input('请输入c：'))
if not isinstance(c,(int,float)):
	raise TypeError('只能输入整数或者小数')
quadratic(a,b,c)