#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql
import util
from bs4 import BeautifulSoup
import re
import sqlutil

#连接数据库获得连接对象
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='****',
                             db='test',
                             charset='utf8')
# #获取光标对象
cursor = connection.cursor()

#获取保存的html
html = util.load_obj('html')
#创建BeautifulSoup对象
bsobj = BeautifulSoup(html, 'html.parser')
# 获取包含数据的容器
ctans = bsobj.find_all('div', class_='span7 content')
for num, ctan in enumerate(ctans):
    text = ctan.find('div', class_='note').string.strip()
    date = ctan.find('div', class_='span4').string.strip()
    d_time = util.convert_timeformat(date)
    print('保存第%s条记录：' % num)
    #保存记录
    sqlutil.insert(cursor, 'study', text, d_time)
    print('保存成功！')
    if(num == 5):
        connection.commit()
    if(num == 8):
        raise Exception("中断")
connection.close()

# for s in sqlutil.select_table(cursor, 'study'):
#     print(s)






