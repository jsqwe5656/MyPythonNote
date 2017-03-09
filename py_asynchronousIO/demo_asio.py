#-*- coding: utf-8 -*-

'将生产者消费者改用协程，通过yield跳转到消费者开始执行，直到消费者执行完毕后，切换回生产者继续生产'

#函数是一个generator
def consumoer():
    r = ''
    while True:
        #consumer通过yield拿到消息，处理，又通过yield把结果传回
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s ...' %n)
        r = '200 OK'
def produce(c):
    #启动生成器
    c.send(None)
    n = 0
    while n<5:
        n = n+1
        print('[PRODUCER] Producing %s..' %n)
        r = c.send(n)
        #produce拿到consumer处理的结果，继续生产下一条消息
        print('[PRODUCER] Consumer return:%s' % r)
    #produce决定不生产了，通过c.close()关闭consumer，整个过程结束。
    c.close()

c = consumoer()
produce(c)



