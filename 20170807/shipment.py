# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
import tool
import os

#url = 'http://www.qingdaoport.net/ywzx/zhcx/cd_cqbcx.dw?jumptopage=/ywzx/zhcx/cd_cqbcx.jsp'
#r = requests.get(url)
#r.encoding = 'GBK'
#print r.text
#定义一个爬虫
class Spider:
      #页面初始化
    def__init__(self):
        self.siteURL = 'http://www.qingdaoport.net/ywzx/zhcx/cd_cqbcx.dw?jumptopage=/ywzx/zhcx/cd_cqbcx.jsp' 
        self.tool = tool.Tool()
        
