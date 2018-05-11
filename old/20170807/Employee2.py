#!/usr/bin/python
# -*- coding: UTF-8 -*-
class Paraent:  #定义父类
    paraentAttr =100  #父类的属性
    def __init__(self):
        print "调用父类构造函数"
        
    def paraentMethod(self):
        print  "调用父类方法"
    def setAttr(self,attr):
        Paraent.paraentAttr= attr
        
    def getAttr(self):
        print "父类属性:",Paraent.paraentAttr
        
        
        
class Chind(Paraent):#定义子类
    def __init__(self):
        print "调用子类构造方法"
        
    def chindMethod(self):
        print "调用子类方法 chind method"
        
        
        
        
newzhilei = Chind()   # 实例化子类
newzhilei.chindMethod() # 调用子类的方法
newzhilei.paraentMethod() #调用父类方法
newzhilei.setAttr(200)   # 再次调用父类方法
newzhilei.getAttr()   #再次调用父类的方法    