#!/usr/bin/python
#encoding:utf-8
import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost","root","root","test")

# 使用cursor()方法获取操作游标
cursor = db.cursor()
# 如果数据表已经存在使用 execute() 方法删除表。
cursor.execute("drop table if exists employee")
#   创建数据表SQL语句
sql = """
        create table employee(
        first_name char(20) not null,
        last_name char(20),
        age int,
        sex char(1),
        income float
        )        
        
        """
# 使用 fetchone() 方法获取一条数据库。
cursor.execute(sql)
print "ok"
db.close