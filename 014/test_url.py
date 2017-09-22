#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql
import util
from bs4 import BeautifulSoup

#连接数据库获得连接对象
# connection = pymysql.connect(host='localhost',
#                              user='root',
#                              password='712342',
#                              db='test')
# #获取光标对象
# cursor = connection.cursor()

#获取保存的html
html = util.load_obj('html')
#创建BeautifulSoup对象
bsobj = BeautifulSoup(html, 'html.parser')
# 获取包含数据的容器
ctan = bsobj.find('div', id='checkin')
# 获得所有的文本
texts = ctan.find_all('div', class_='note')
#获得所有的时间数据
time = ctan.find_all('div', class_='span4')
#打印文本
for text in time:
    print(text.string.strip())
