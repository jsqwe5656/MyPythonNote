# -*- coding: utf-8 -*-
#python 关于filter()函数的demo 写出1-1000内的回数

#实现回数的筛选函数
def is_palindrome(n):
	temp_s = '%d'%n			#将数变成字符串
	temo_s2 = temp_s[::-1]	#将字符串反转
	temp_n = int(temo_s2)	#将字符串变成数字
	if temp_n == n:			#判断是不是回数
		return(n)			
		
output = filter(is_palindrome,range(1,1000))
print(list(output))