#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'关于枚举enum的demo'
__author__='zbf'

from enum import Enum,unique

@unique
class Weekday(Enum):
	Sun = 0
	Mon = 1
	Tur = 2
	Wed = 3
	Thu = 4
	Fri = 5
	Sat = 6

