# -*- coding: utf-8 -*-
#pyhton循环的demo
names = ['z','zz','zbf']
for name in names:
	print(name)
sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
	sum += x
print(sum)
for x in range(101):
	sum += x
	#print(x)
print(sum)
sum = 0
n = 99
while n>0:
	sum +=n
	n -=2
	if n<0:
		print(n)
print(sum)
L = ['zbf','zzz','asdasd']
for name in L:
	print('Hello,%s'%(name))
