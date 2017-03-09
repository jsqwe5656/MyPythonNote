# -*- coding: utf-8 -*-

import socket

#指定ipv4,以及指定了这个sockets的类型是UDP
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#绑定端口与tcp一样 但是不需要使用监听 Listen()
s.bind(('127.0.0.1',9000))
print('Bind UDP on 9000.,,')
while True:
    #接受数据并指定大小
    data,addr = s.recvfrom(1024)
    print('Received from %s:%s'%addr)
    #将数据发送给客户端
    s.sendto(b'Hello %s' % data,addr)
    print(data)


