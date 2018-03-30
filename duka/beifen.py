#!/usr/bin/env python
# -*- coding: cp936 -*-  
import os  
import time 
import sys
import re
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

#print(c1)
c2= '"'+c1+'"'
#print(c2)
# 在列表中写明需要备份的文件名和或目录  
source=[c2]
#source=[r'"c:\users\wangxiaozhen\desktop\lala.txt"']  
print(source)


# 备份到下面的目录中  
target_dir='D:\\'  

# 备份为rar文件，文件名是: 年月日时分秒.rar  
target = target_dir + "lalala" + '.rar'  

# 用winrar的命令行来压缩文件，前提是winrar在windowsXP的path中  
zip_command="rar a %s %s"%(target, ' '.join(source) )   

#运行这个备份程序来备份  
if os.system(zip_command) == 0:  
    print ('Successful backup to', target  )
else:  
    print ('Backup FAILED!'  )