# -*- coding: utf-8 -*-
#python关于map的小练习

#将首字母大写
def normalize(name):
	return name.capitalize()

L1 = ['adsa','ASDA','vasdR']
L2 = list(map(normalize,L1))
print(L2)