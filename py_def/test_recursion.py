# -*- coding: utf-8 -*-
#python 递归小练习

def move(n,a,b,c):
	if n == 1:
		print('%s--->%s'%(a,c))	#移动目标盘
		return
	else:
		move(n-1,a,c,b)			#一步一步走
		#print('%s--->%s'%(a,c),n)
		move(1,a,b,c)	
		move(n-1,b,a,c)	
		#print('%s--->%s'%(a,c),n) 
		
	print(n)						
move(int(input()),'A','B','C')
