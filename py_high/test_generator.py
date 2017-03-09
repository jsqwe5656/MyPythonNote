# -*- coding: utf-8 -*-
#python高级特性,生成器练习

#杨辉三角形
def triangles():
	L = [1]
	a = 1
	while True:
		if a == 1:
			yield L
		else:
			L = [L[i-1] + L[i] for i in range(1,a-1)]
			L = [1] + L + [1]
			yield L
		a = a+1
n = 0
for t in triangles():
	print(t)
	n +=1
	if n == 20:
		break