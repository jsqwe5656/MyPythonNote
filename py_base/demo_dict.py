# -*- coding: utf-8 -*-
#Python中关于dict的实现demo 用的大括号 
#list 用中括号  l = ['a','b']
#tuple 小括号是不可变的数组	l = ('a','b')
d = {'z' : 20,'zz' : 30,'zzz' : 40,'zbf' : 50,'bf' : 60}
#取值
for key in d:
	print(d[key])
#判断值是否在dict中
if 'zbf' in d:
	print('Yes')
else:
	print('NO')
#使用dict提供的get方法,如果值不存在返回None，或者自己定义的value
print(d.get('zbf'))
print(d.get('zbff'))
print(d.get('zbff',-1))
print(d.get('zbff','不存在'))
#删除一个key用pop(key)方法
print(d.pop('zbf'))
print(d.get('zbf',-1))