#-*- coding: utf-8 -*- 
#python 关于map与reduce的应用

from functools import reduce

#编写数字字典
def char2num(ch):
	return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[ch]

def f(x,y):
	return x*10 + y

#将字符串转换成浮点数
def str2float(s):
	a = s.index('.')
	s1 = s[:a]
	s2 = s[a+1:]
	n = len(s2)
	return reduce(f,map(char2num,s1)) + reduce(f,map(char2num,s2))*(0.1**n)
	
print('str2float(\'123.456\') =',str2float('123.456'))
print('asdasd')

