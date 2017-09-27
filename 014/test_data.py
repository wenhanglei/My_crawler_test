#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql
import sqlutil
import re

def get_time_data(s):
    regex = re.compile(r'(\d*) 分钟')
    m = regex.search(s)
    return int(m.group(1))


#连接数据库获得连接对象
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='712342',
                             db='test',
                             charset='utf8')
# #获取光标对象
cursor = connection.cursor()
sql = 'select * from study;'
cursor.execute(sql)
sum = 0
for r in cursor.fetchall():
    sum += get_time_data(r[1])
print(str(sum) + ' --- ' + str(sum/10))










