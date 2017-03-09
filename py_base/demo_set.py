# -*- coding: utf-8 -*-
#set是小括号里面包着中括号s = set([])
#set中不能有重复的key(重复值会被自动过滤) 创建set需要提供list作为输入集合
s = set([1,2,3])
print(s)
#通过add(key)添加值到set中
s.add(4)
print(s)
#remove(key)方法删除元素
s.remove(1)
print(s)
s2 = set([2,4,5,6])
#并集
print(s | s2)
#交集
print(s & s2)
#set同样不可放入list

