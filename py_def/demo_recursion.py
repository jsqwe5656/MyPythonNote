# -*- coding: utf-8 -*-
#python 递归函数的demo
#递归概念：如果一个函数在自身内部调用自己那么这个函数就是一个递归函数
#因为teturn包含表达式 所以不算是尾递归 数值过大事会产生栈帧溢出
def fact(n):
	if n==1:
		return 1;
	return n*fact(n-1)
#print(fact(int(input())))
#一参为求阶乘的数 二参为阶乘和
def fact_iter(num,product):
	if num == 1:
		return product
	return fact_iter(num-1,num*product)
print(fact_iter(999,1))