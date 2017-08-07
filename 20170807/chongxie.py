#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Pararent: #定义父类
    def myMethond(self):
        print "调用父类方法"
        
        
        
class Chind(Pararent):  #定义子类
    def myMethond(self):
        print "调用子类的方法"
        
c = Chind() #子类实例
c.myMethond() #子类调用方法重写
    