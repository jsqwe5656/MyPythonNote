# -*- coding: utf-8 -*-

import threading

#创建全局local_thread对象
local_school = threading.local()

def process_student():
    #获取当前实例的student对象
    std = local_school.student
    print('this is %s,%s' % (std,threading.current_thread().name))

def process_thread(name):
    #绑定local_school的student
    local_school.student = name
    process_student()

t1 = threading.Thread(target=process_thread,args=('zbf',))
t2 = threading.Thread(target=process_thread,args=('bf',))
t1.start()
t2.start()
t1.join()
t2.join()