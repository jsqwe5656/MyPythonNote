# -*- coding: utf-8 -*-
'socket的客户端程序'

import socket,threading,time

def tcplink(sock,addr):
    print('accept new connection from %s:%s..'%addr)
    sock.send(b'Welcome')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') =='exit':
            break
        sock.send(('hello,%s' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed' % addr)

#ipv4,tcp协议
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#监听端口
s.bind(('127.0.0.1',9999))
#开始监听
s.listen(5)
print('waiting for connection..')
while True:
    #接受一个新连接
    sock,addr = s.accept()
    #创建新线程来处理tcp连接,每个连接都必须创建新进程来处理，否则单线程在处理连接中无法接受其他客户端的连接
    t = threading.Thread(target=tcplink,args=(sock,addr))
    t.start()




