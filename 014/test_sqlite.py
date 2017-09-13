#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

conn = sqlite3.connect('example.db')

c = conn.cursor()

c.execute('''CREATE TABLE stocks
            (date text, trans text, symol text, qty real, price real)''')