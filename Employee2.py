#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Employee:
    '所有员工的基类'
    empCount = 0
    
    
def __init__(self,name,salary):
    self.name   = name
    self.salary = salary
    Employee.empCount+=1
    
def dsiplayCount(self):
    print "总数是%d" % Employee.empCount
    
def  displayEmployee(self):
    print "name:",self.name, ",salary:",self.salary
    
    
    
    
    
#"创建雇员类的第一个对象"
#emp1= Employee("Zara",2000)
emp1 = Employee("Zara", 2000)
#"创建 Employee 类的第二个对象"
emp2 = Employee("Manni",5000)
emp1.displayEmployee()
emp2.displayEmployee()
print "雇员总数 %d" % Employee.empCount








    
    

    
    
