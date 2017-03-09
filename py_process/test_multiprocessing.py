# -*- coding: utf-8 -*-

from multiprocessing import Process
import os

def run_proc(name):
	print('child is running %s (%s)..' %(name,os.getpid()))

if __name__ == '__main__':
	print('father process %s..' % os.getpid())
	p = Process(target = run_proc,args = ('test',))
	print('Child process will start.')
	p.start()
	p.join()
	print('Child run over.')