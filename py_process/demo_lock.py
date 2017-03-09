# -*- coding: utf-8 -*-

'关于锁的demo'

import threading,time

#假设是余额
balance = 0
#添加线程锁
lock = threading.Lock()

def change(n):
	#将balance变成全局变量
	global balance
	#先存后取
	balance = balance + n
	print(balance,threading.current_thread().name)
	balance = balance - n
	print(balance, threading.current_thread().name)
def run_thread(n):
	for i in range(1000):
		# 让执行此方法的线程先获取锁
		lock.acquire()
		try:
			change(n)
		finally:
			#方法执行完毕后一定释放线程锁
			lock.release()
t1 = threading.Thread(target = run_thread,args=(5,))
t2 = threading.Thread(target = run_thread,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

