# -*- coding: utf-8 -*-

import socket

#创建一个socket,AF_INET指定使用IPV4协议，SOCK_STREAM，指定使用面向流的TCP协议
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#建立连接
s.connect(('www.sina.com.cn',80))
#发送数据
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
#接受数据
buffer = []
#调用recv(max)方法，一次最多接收指定的字节数，因此，在一个while循环中反复接收，直到recv()返回空数据，表示接收完毕，退出循环。
while True:
    #每次最多接受1k的字节
    d =s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
#调用完成后关闭连接
s.close()
header,html = data.split(b'\r\n\r\n',1)
print(header.decode('utf-8'))
#将接受的数据写入文件
with open('sina.html','wb') as f:
    f.write(html)
