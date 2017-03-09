# -*- coding: utf-8 -*-
#python第二个例子 函数返回多个值
import math

def move(x,y,step,angle=0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx,ny
x,y = move(100,100,60,math.pi/6)
print(x,y)
z = x,y
print(z)