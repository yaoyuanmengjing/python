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

html = getHtml("https://back.21eline.com/ysdUpdate/see/GetCookie?cardID=8930000092276")

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
    
else:
    print "过期"
    from email.mime.text import MIMEText
    from email.header import Header

    sender = 'lyz'
    receiver = 'duka2@mail.ysdtg.cn'
    subject = '天津正式读卡检测'
    smtpserver = 'mail.ysdtg.cn'
    username = 'duka'
    password = 'See123456'

    msg = MIMEText('你好，天津正式读卡已经过期，请检查读卡程序','text','utf-8')#中文需参数‘utf-8’，单字节字符不需要
    msg['Subject'] = Header(subject, 'utf-8')

    smtp = smtplib.SMTP()
    smtp.connect('mail.ysdtg.cn')
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()    

