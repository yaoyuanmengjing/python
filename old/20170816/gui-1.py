#!/usr/bin/python
#encoding:utf-8
from Tkinter import *
root = Tk()  # 创建窗口对象的背景色
 #创建两个列表
li = ['1','2','3','4']
movie = ['6','7','8','9']
#创建连个列表组件

listb = Listbox(root)
listb2 =Listbox(root)

#往第一个表里面插入数据
for item in li:
     listb.insert(0,item)
#往第二个表里面插入数据    
for item in movie:
     listb2.insert(0,item)
     

listb.pack()
listb2.pack()
root.mainloop()
   