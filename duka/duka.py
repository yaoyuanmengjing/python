#!/usr/bin/env python
#__*__ encoding:utf-8__*__
"""
import pygame,sys
pygame.init()
screen = pygame.display.set_mode([640,480])  #
screen.fill([199,237,204])  #白色背景墙填充窗口
pygame.draw.rect(screen,[0,0,0],[250,150,300,200],2)
pygame.display.flip()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
"""

"""
机器之声
"""

"""
import pygame,sys,random
pygame.init()

screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
for i in range (100):
    width = random.randint(0, 250)
    height = random.randint(0, 100)
    top = random.randint(0, 400)
    left = random.randint(0, 500)
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    
    pygame.draw.rect(screen,[red,green,blue],[left,top,width,height],1)
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
"""


"""
import pygame,sys,random
from pygame.color import THECOLORS
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
for i in range(100):
    width = random.randint(0, 255)
    height = random.randint(0, 100)
    top = random.randint(0,400)
    left = random.randint(0, 250)
    color_name = random.choice(THECOLORS.keys())
    color = THECOLORS[color_name]
    line_width = random.randint(1, 3)
    pygame.draw.rect(screen,color,[left,top,width,height],line_width)
    pygame.display.flip()
    
while True:
    for  event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
"""


"""
正弦曲线
"""

"""
import pygame,sys
import math
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
for x in range(0,640):
    y = int(math.sin(x/640.0 * 4* math.pi)*200 +240)
    pygame.draw.rect(screen,[0,0,0],[x,y,1,1],1)
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
"""

"""
import pygame,sys
pygame.init()

dots = [[221,432],[225,331],[133,342],[141,310],[51,230],[74,217],[58,153],[114,164],[123,135],[176,190],[159,77],[193.93],[230,28],[267,93],[301,77],[284,190],[327,135],336,164],[402,153],[386,217],[409,230],[319,310],[327,342],[233,331],[237,432]]
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
pygame.draw.lines(screen,[255,0,0],True,dots,2)
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT():
            sys.exit()
            
"""
"""
import pygame,sys
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
my_ball = pygame.image.load("beach_ball.png")
x=50
y=50
screen.blit(my_ball,[x,y])
pygame.display.flip()
for looper in range (1,100):
    pygame.time.delay(20)
    pygame.draw.rect(screen,[255,255,255],[x,y,90,90],0)
    x=x+5
    screen.blit(my_ball,[x,y])
    pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:sys.exit()
        
"""
"""
import pygame,sys
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
my_ball = pygame.image.load()


"""
"""

import pygame,sys
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
my_ball = pygame.image.load('beach_ball.png')
x=50
y=50
x_speed = 10
y_speed = 10




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
    pygame.time.delay(20)
    pygame.draw.rect(screen,[255,255,255],[x,y,90,90],0)
    x = x + x_speed 
    y = y + y_speed 
    if x > screen.get_width() - 90 or x < 0:
        x_speed = - x_speed
    if y > screen.get_height() - 90 or y < 0:
        y_speed = - y_speed    
        
    screen.blit(my_ball,[x,y])
    pygame.display.flip()
    
"""
"""
import easygui
a=easygui.msgbox("Hello There!")
print (a)
"""




"""
def printMyAddress():
    print ("123123")
    print ("456456")
    print ("789798")
    
printMyAddress()
"""
"""
def printMyaddress(myName,age):
    print (myName)
    print (age)
    print ("789798")    
    
printMyaddress("xiaoming","18")
"""
"""
f = open(r"G:\\ceshi\CardLog\2018\time.txt")
line = f.readline()
while line:
    print(line,end="")
    line = f.readline()
    
f.closed()
"""

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






'''







'''
f = open(c1)
line = f.readline()
while line:
    print(line,end="")
    line = f.readline()
    
f.closed()
'''
'''
def get_last_line(inputfile):
    filesize = os.path.getsize(inputfile)
    blocksize =1024
    dat_file = open(inputfile,'r')
    last_line = ""
    lines = dat_file.readlines()
    count = len(lines)
    if count>60:
        num=60
    else:
        num=count
    i=1;
    lastre=[]
    for i in range (1,(num+1)):
        if lines:
            n=-i
            last_line = lines[n].strip()
            dat_file.close()
            lastre.append(last_line)
        return lastre
re = get_last_line(c1)
print (len(re))
for n in re:
    strlist = n.split()
    print (strlist)
    
    if strlist[1] == 'OK' and string.atoi(strlist[2])>10:
        print("shujutiao,zhengchang")
    else:
        print ("shujutaishao")
    
    
    
    
if os.access(c1, os.F_OK):
    print ("Given file path is exist.")
    
    
    
    
    
    
else:
    print("文件不存在退出")
    exit()

lines = []
with open(c1, "r") as f:
    while True:
        tlines = f.readlines(-100)
        if not tlines:
            break
        tlineslen = len(tlines)
        if tlineslen <= 30:
            lines = lines[tlineslen - 30:] + tlines
            break
        lines = tlines[-30:]
print(lines)
str4 = "".join(lines)  
#print (type(str4)) 
#print (str4)
#print (re.findall(r"正在使用",str4))
'''