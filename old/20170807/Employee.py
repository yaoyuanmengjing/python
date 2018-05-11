#!/usr/bin/python
# -*- coding: UTF-8 -*-
class Employee:
    '所有员工的基类'
    empCount = 0
    def __init__(self,name,salary):
        self.name =name
        self.salary =salary
        Employee.empCount =  Employee.empCount +1
        
    def  displayCount(self):
        print "雇员的总数是 %d" %  Employee.empCount
        
    def displayEmployee(self):
        print "Name:" ,self.name,",Salary:",self.salary
        

class Test:
    def prt(self):
        print (self)
        print(self.__class__)
        
t=Test()
t.prt()
        