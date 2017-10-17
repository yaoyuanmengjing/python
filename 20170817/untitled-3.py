#!/usr/bin/python
#encoding:utf-8
import MySQLdb

db = MySQLdb.connect("localhost","root","root","test")


#使用cursor()方法获取游标
cursor = db.cursor()
#SQL 查询语句
sql  =  ''' select *from employee where income > 1000  '''
try:
    #执行SQL语句
    cursor.execute(sql)
    #获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        fname = row [0]
        lname = row [1]
        age   = row [2]
        sex   = row [3]
        income = row [4]
        #打印结果
        print "fname=%s,lname=%s,age=%d,sex=%s,income=%d" %  (fname, lname, age, sex, income )
        
except:
    print "错误 无法连接数据库"
    
db.close()