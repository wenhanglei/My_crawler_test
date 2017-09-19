#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

conn = sqlite3.connect('mydata.db')
c = conn.cursor()
c.execute('PRAGMA stats;')
print(c.fetchone())
# t = ('RHAT',)
# c.execute('select * from stocks where symbol = ?', t)
# print(c.fetchone())

# conn = sqlite3.connect('mydata.db')
#
# c = conn.cursor()
#
# c.execute('''create table stocks
#             (date text, trans text, symbol text, qty real, price real)''')
# c.execute("insert into stocks values ('2017-09-19', 'BUY', 'RHAT', 100, 35.14)")
#
# conn.commit()
#
# conn.close()