# -*- coding: utf-8 -*-
#Python关于排序函数sorted()的demo

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
	return t[0]		#传过来的是tuple像 ('str',num)这样的 取第一位也就是字符串为排序依据

L2 = sorted(L,key=by_name)
print(L2)

def by_num(t):
	return t[1]
L2 = sorted(L,key=by_num,reverse = True)		#默认是从小到大排序 reverse表示是否反转排序
print(L2)