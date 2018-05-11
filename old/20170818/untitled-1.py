#！/usr/bin/python
#encoding:utf-8
import re
print (re.match('www', 'www.runoob.com').span())  #span  span([group]): 返回(start(group), end(group))。
print (re.match('com', 'www.runoob.com'))