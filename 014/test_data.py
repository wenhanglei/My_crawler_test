#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql
import sqlutil
import re
import time

def get_time_data(s):
    regex = re.compile(r'(\d*) 分钟')
    m = regex.search(s)
    return int(m.group(1))


#连接数据库获得连接对象
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='*****',
                             db='test',
                             charset='utf8')
# #获取光标对象
cursor = connection.cursor()
sql = 'select * from study;'
cursor.execute(sql)
sum = 0
start = time.time()
for r in cursor.fetchall():
    sum += get_time_data(r[1])
end = time.time()
elp_time = '%.2f' % (end-start)
study_time = str(sum/60)
print('本次统计耗时 %s 秒' % elp_time)
print('你总共学习了 %s 小时！' % sum)










