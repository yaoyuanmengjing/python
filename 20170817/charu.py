#!/usr/bin/python
#encoding:utf-8
import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost","root","root","test")

# 使用cursor()方法获取操作游标
cursor = db.cursor()
# 如果数据表已经存在使用 execute() 方法删除表。
#cursor.execute("drop table if exists employee")
#   创建数据表SQL语句
sql = """
        insert into employee(first_name,last_name,age,sex,income)VALUES ('mac','mohan',20,'M',2000)        

        """
try:
    #执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except:
    #Rollback in case there is any error
    db.rollback()
# 使用 fetchone() 方法获取一条数据库。
# 关闭数据库lianjie
db.close