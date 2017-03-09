# -*- coding: utf-8 -*-

from multiprocessing import Process,Queue
import os,time,random

#写入数据进程执行的代码
def write(q):
    print('Process to write :%s' % os.getpid())
    for value in ['a','b','c']:
        print('put %s to the queue' %value)
        q.put(value)
        time.sleep(random.random())

#读取数据进程执行的代码
def read(q):
    print('Process to read:%s' % os.getpid())
    while True:
        value = q.get(True)
        print('get %s from queue' % value)

if __name__ == '__main__':
    #父进程创建Queue，并传给各个子进程
    q = Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))
    #pw = Process(target=write(q,))
    #pr = Process(target=read(q,))
    #启动紫禁城pw并开始写入
    pw.start()
    #启动子进程pr并开始读取
    pr.start()
    #等待pw结束
    pw.join()
    #pr进程写成了死循环，无法等待其主动结束，只能强行停止
    pr.terminate()