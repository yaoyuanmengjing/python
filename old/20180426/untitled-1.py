#print ('Hi''\nThere')
'''
print( 'ABC''\tXYZ')
print( 'ABCD''\tXYZ')
print( 'ABCDE''\tXYZ')
print( 'ABCDEF''\tXYZ')
print( 'ABCDEFG''\tXYZ')
print( 'ABCDEFGH''\tXYZ')
'''
'''
print ("Number \tSquare \tCube")
for i in range (1,11):
    print (i,'\t',i**2,'\t',i**3)
'''
'''
#!/usr/bin/env python
#_*_coding:utf-8_*_
#if__name__=="__main__"

import datetime
'''
'''
when = datetime.datetime(2008,10,24,10,45,56)
print (when)
'''
'''
when = datetime.datetime(hour=10,year=2008,minute=45,month=10,second=56,day=24)
print (when.year)
print (when.day)
print (when.ctime())

'''
import turtle
window = turtle.Screen()