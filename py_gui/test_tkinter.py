# -*- coding: utf-8 -*-

from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):

    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        #self.winfo_width(60)
        #self.winfo_height(20)
        self.createrWidgets()

    def createrWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self,text='Hello',command=self.hello)
        self.alertButton.pack()
        #self.helloLabel = Label(self,text = 'Hello,world!')
        #self.helloLabel.pack()
        #self.quitButton = Button(self,text='Quit',command=self.quit)
        #self.quitButton.pack()

    def hello(self):
        #获取用户输入的文本 若没有则显示默认的 world
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('我叫标题','hello,%s' % name)
app = Application()
#设置窗口标题
app.master.title('hello world!')
#主消息循环
app.mainloop()
