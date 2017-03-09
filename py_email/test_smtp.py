#!/usr/bin/python3
# -*- coding: utf-8 -*-

from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import parseaddr,formataddr

import smtplib,os
#用来格式化邮件地址
def _format_addr(s):
    name,addr = parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))

#然后通过SMTP发出去
from_addr = 'qwe597983960@126.com'
#使用邮箱的授权码
pwd = 'qwe5656'
#输入收件人的地址
to_addr = '516845590@qq.com'
#输入SMTP服务器地址
smtp_server = 'smtp.126.com'
#一参是发送的征文，二参表示纯文本，三参表示编码格式好让其他语言更好的兼容
#msg = MIMEText('hellp,this is send by python.','plain','utf-8')
#发送html
#msg = MIMEText('<html><body><h1>Hello</h1>'
#               '<p>send by <a href="http://www.python.org">Python</a>...</p>'
#               '</body></html>','html','utf-8')
#发送附件
msg = MIMEMultipart()
msg.attach(MIMEText('附件，请查收2333','html','utf-8'))

msg.attach(MIMEText('<html><body><h1>Hello</h1>'
    '<p><img src="cid:0"></p>'
    '</body></html>', 'html', 'utf-8'))

path =r'c:\Users\zbf\Desktop\py_workspace\py_moudle\end.jpg'
#添加附件就是加上一个MineBase从本地读取一个图片
with open(path,'rb') as f:
    #设置附件的MIME和文件名
    mime = MIMEBase('image','jpeg',filename='end.jpg')
    #加上必要的头信息
    mime.add_header('Content-Disposition','attachment',filename='end.jpg')
    mime.add_header('Content-ID','0')
    mime.add_header('X-Attachment-Id','0')
    #将附件的内容读进来
    mime.set_payload(f.read())
    #用base64编码
    encoders.encode_base64(mime)
    #天假到MimeMultipart
    msg.attach(mime)

msg['From'] = _format_addr('python<%s>'%from_addr)
msg['To'] = _format_addr('zbf<%s>' % to_addr)
#标题，如果含有中文要用Header转码
msg['Subject'] = Header('来自python的邮件。','utf-8').encode()
#msg['Data'] = formatdate()
#SMTP默认端口是25
server = smtplib.SMTP(smtp_server,25)
#可以打印出和SMTP服务器交互的所有信息
server.set_debuglevel(1)
#登录邮箱
server.login(from_addr,pwd)
#发送邮件
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()





