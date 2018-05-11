#coding=utf-8
import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

html = getHtml("http://www.qingdaoport.net/ywzx/zhcx/cd_cqbcx.dw")

print html.decode('gbk').encode('utf8')  