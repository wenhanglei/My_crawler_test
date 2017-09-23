#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
def insert(cursor, table_name, text, date):
    sql = "insert into %s (text, date) values ('%s', '%s')" % (table_name, text, date)
    cursor.execute(sql)

#删除表中的一列
def drop_culumn(cursor, table_name, culumn):
    sql = "alter table %s drop %s" % (table_name, culumn)
    cursor.execute(sql)

#查询表中的数据
def select_table(cursor, table_name):
    sql = 'select * from %s;' % table_name
    cursor.execute(sql)
    return cursor.fetchall()
