# -*- coding: utf-8 -*-

import time,threading

#新线程执行的代码
def loop():
	
	print('thread %s is running.' % threading.current_thread().name) 
	n = 0
	while n<5:
		n = n+1
		print('thread %s >>> %s' %(threading.current_thread().name,n))
		time.sleep(1)
	print('thread %s ended.' %threading.current_thread().name)
	
print('thread %s is running.' % threading.current_thread().name)
#参数线程执行的方法，线程名字
t = threading.Thread(target = loop,name = 'zbfThread')
t.start()
#阻塞主线程直到子线程结束
t.join()
print('thread %s ended..' %threading.current_thread().name)