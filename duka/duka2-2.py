#!/usr/bin/env python
#__*__ encoding:utf-8__*__
import sys
import time
import re
import os
import datetime
import math
import string
#print (time.strftime('%Y-%m-%d',time.localtime(time.time())))
str_time=time.strftime('%Y-%m-%d',time.localtime(time.time()))
#print(str_time[5:])
b=str_time[5:]
lujing_name="G:\\ceshi\\CardLog\\2018\\"
#print(lujing_name)
a1=lujing_name+b
#print (type(a1))
b1_txt=r".txt"
#print (type(b1_txt))
c1=a1+b1_txt
print(c1)



f = open(c1)             # 返回一个文件对象  
line = f.readline()             # 调用文件的 readline()方法  
while line:  
    print (line, )                # 后面跟 ',' 将忽略换行符  
    # print(line, end = '')　　　# 在 Python 3中使用  
    line = f.readline()  
    if line.find('本卡正在被其他用户使用',1):
        print("找到了")
        
    else:
        continue
f.close()









































'''
class TraceManagerBase(object):  
    dblocation =""
    def __init__(self):  
        self.init()  
  
    def init(self):  
        self.dblocation = os.path.join(os.path.join(os.path.abspath(os.path.dirname(__file__) + os.path.sep + ".."), "data","traceCoords")) #  os.getcwd(),"data","traceCoords"  
        if not os.path.exists(self.dblocation):  
            os.makedirs(self.dblocation)  
  
    #从文件末尾向前读取，逆序  
    def get1(self,sn,n):  
        filename = c1 % sn  
        path = os.path.join(self.dblocation, filename)  
        data = []  
        with open(path,'r') as fs:  
            for i in range(n+1):  
                if i>0:  
                    fs.seek(-113*i,2) #113为每行文本的长度，包含\r\n  
                    data.append(fs.readline())  
                    print (fs.tell()  )
            #读取后几条  
            # fs.seek(-113*n,2)  
            # print fs.tell()  
            # data.append(fs.readlines())  
            # print fs.tell()  
            print (data )


'''

'''
def read_reverse(c1):  #c1 wenjianming
    f = open(c1)
    f.seek(0,2)
    last_postion =f.tell()
    
    
    while True:
        line =f.readline()
        current_position = f.tell()
        i = 1
        while current_position == last_postion:
            if len(line) == current_position:
                yield line
                return
            i +=0.5
            f.seek(max(int(-72*i),-current_position),1)
            line = f.readline()
            current_position = f.tell()
            
        while current_position != last_postion:
            line = f.readline()
            current_position= f.tell()
            
        yield line
        last_postion = last_postion - len(line)
        f.seek(max(-72,-last_postion)-len(line),1)
        
        
read_reverse()
print (f)
'''