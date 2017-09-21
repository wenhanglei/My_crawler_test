#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql

#查看所有数据库
def show_database(cursor):
    cursor.execute("show databases;")
    return [x for (x,) in cursor.fetchall()]

#查看数据库中的所有表
def show_tables(cursor):
    cursor.execute("show tables;")
    return [x for (x,) in cursor.fetchall()]

#创建表
def create_talbe(cursor, table_name):
    sql = 'create table %s (id int auto_increment primary key, text varchar(100));' % table_name;
    cursor.execute(sql)

#删除表
def drop_table(cursor, table_name):
    sql = 'drop table %s;' % table_name
    cursor.execute(sql)

#插入数据
def insert(cursor, table_name, text):
    sql = "insert %s (text) value ('%s')" % (table_name, text)
    cursor.execute(sql)




connection = pymysql.connect(host='localhost',
                             user='root',
                             password='*****',
                             db='test')
cursor = connection.cursor()
sql = """CREATE TABLE my_shanbay_time (
        'id' INT PRIMARY KEY ('id'),
        'text_data' VARCHAR(40));"""

# drop_table(cursor,'study')

# create_talbe(cursor, 'study')

# for database in show_tables(cursor):
#     print(database)

table = 'study'
text = 'hahah da sb'
insert(cursor, table, text)
connection.commit()
connection.close()