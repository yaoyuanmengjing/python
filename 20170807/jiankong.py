#coding=utf-8
import urllib
import string 
import time
import datetime
import smtplib

#status=urllib.urlopen("https://back.21eline.com/ysdUpdate/see/GetCookie?cardID=8930000092276").code
#print status

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

html = getHtml("http://www.qingdaoport.net/ywzx/zhcx/cd_cqbcx.dw?jumptopage=/ywzx/zhcx/cd_cqbcx.jsp")

print  type(html)

