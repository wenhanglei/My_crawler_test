#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='****',
                             db='test')
cursor = connection.cursor()
sql = """CREATE TABLE my_shanbay_time (
        'id' INT PRIMARY KEY ('id'),
        'text_data' VARCHAR(40));"""
cursor.execute(sql)
