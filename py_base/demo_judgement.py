# -*- coding: utf-8 -*-
height = 1.75
weight = 80.5
bmi = 80.5/(1.75*1.75)
if bmi < 18.5:
	print('太轻了')
elif 18.5<bmi<25:
	print('这才对嘛')
elif 25<bmi<28:
	print('有点胖')
elif 28<bmi<32:
	print('胖了哦~')
else :
	print('死胖子，该减肥了')