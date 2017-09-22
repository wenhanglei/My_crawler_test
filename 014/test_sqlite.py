#!/usr/bin/env python
# -*- coding: utf-8 -*-

import util
import pymysql
import requests

#访问入口
entry = 'https://www.shanbay.com/checkin/user/20272978'

#连接数据库获得连接对象
# connection = pymysql.connect(host='localhost',
#                              user='root',
#                              password='712342',
#                              db='test')
#获取光标对象
# cursor = connection.cursor()

#获取user-agent头
header = util.load_header('../header.txt')
#获取cookies
cookie = util.get_cookie_dic_from_file('cookie.txt')
#获取html并保存
resp = requests.get(entry, headers=header, cookies=cookie)
util.save_obj(resp.text, 'html')
