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

html = getHtml("https://back.21eline.com/ysdUpdate/see/GetCookie?cardID=2000030001724")

print eval(html)["updateTime"]  #将获取的字符串变成字典并取出updatetime的值

a= eval(html)["updateTime"]

QpTime=time.mktime(time.strptime(a,'%Y-%m-%d %H:%M:%S'))
#print QpTime
now=time.time()
#print now
TimeCha =  now -    QpTime
print TimeCha
if TimeCha < 1600  :
    print "不过期"
    import mail
else:
    print "过期"
    import mail
    

