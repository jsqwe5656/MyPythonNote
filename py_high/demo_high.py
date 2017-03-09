# -*- coding: utf-8 -*-
#Python 高级特性小练习
import os

L = [d for d in os.listdir('.')]	#列出当前路径下文件和目录
print(L)


L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x, str)]
print(L2)
g = (x*x for x in range(10))
for n in g:
	print(n)
#实现斐波拉契数列
def fib(max):
	n,a,b = 0,0,1
	while n<max:
		yield b
		a,b = b,a+b
		n +=1
	return 'done'
f = fib(10)
print('fib(10):',f)
for x in f:
	print(x)
#手动生成
g = fib(5)
while 1:
	try:
		x = next(g)
		print('g:',x)
	except StopIteration as e:			#在生成器中没有下一个值的时候回报这个错误 如果不捕获 不会报错
		print('生成器返回值：',e.value)
		break
